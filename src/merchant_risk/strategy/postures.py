"""Synthetic policy-posture effects and commercial comparison."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

from merchant_risk.strategy.assessment import assess
from merchant_risk.strategy.commercial import (
    CommercialAssumptions,
    calculate_commercial_view,
)
from merchant_risk.strategy.models import (
    PolicyPosture,
    PostureComparisonResult,
    PostureSimulationResult,
    StrategyAssessmentInput,
)

ROOT = Path(__file__).resolve().parents[3]
POSTURE_PATH = ROOT / "config" / "strategy" / "postures-0.1.0.yaml"


def _clip_rate(value: float) -> float:
    return max(0.0, min(1.0, value))


@lru_cache(maxsize=1)
def load_posture_config() -> dict[str, Any]:
    with POSTURE_PATH.open(encoding="utf-8") as source:
        config = yaml.safe_load(source)
    if not isinstance(config, dict) or not isinstance(config.get("postures"), dict):
        raise ValueError("Posture configuration must contain a postures mapping")
    return config


def compare_postures(merchant: StrategyAssessmentInput) -> PostureComparisonResult:
    """Compare three synthetic control strategies for one merchant period."""
    config = load_posture_config()
    baseline = assess(merchant)
    maximum_risk = float(config["risk_appetite"]["maximum_residual_risk_score"])
    simulations: list[PostureSimulationResult] = []

    for posture in PolicyPosture:
        settings = config["postures"][posture.value]
        adjusted = merchant.model_copy(
            update={
                "payment_approval_rate": _clip_rate(
                    merchant.payment_approval_rate + float(settings["approval_rate_delta"])
                ),
                "refund_rate": _clip_rate(
                    merchant.refund_rate * float(settings["refund_rate_multiplier"])
                ),
                "dispute_rate": _clip_rate(
                    merchant.dispute_rate * float(settings["dispute_rate_multiplier"])
                ),
                "fraud_loss_rate": _clip_rate(
                    merchant.fraud_loss_rate * float(settings["fraud_loss_multiplier"])
                ),
            }
        )
        reserve_rate = _clip_rate(baseline.reserve.rate + float(settings["reserve_rate_delta"]))
        holding_days = max(
            0,
            min(180, baseline.reserve.holding_days + int(settings["holding_days_delta"])),
        )
        assumptions = CommercialAssumptions(
            monitoring_and_review_cost=float(settings["monitoring_and_review_cost"]),
            false_positive_volume_share=float(settings["false_positive_volume_share"]),
            contingent_exposure_realization_rate=float(
                config["commercial_assumptions"]["contingent_exposure_realization_rate"]
            ),
        )
        normalized = calculate_commercial_view(
            adjusted,
            scale=100,
            reserve_rate=reserve_rate,
            holding_days=holding_days,
            assumptions=assumptions,
        )
        dollars = calculate_commercial_view(
            adjusted,
            scale=merchant.monthly_attempted_payment_volume,
            reserve_rate=reserve_rate,
            holding_days=holding_days,
            assumptions=assumptions,
        )
        residual_risk = min(
            100.0,
            baseline.risk_exposure_score * float(settings["residual_risk_multiplier"]),
        )
        within_appetite = not baseline.hard_policy_flags and residual_risk <= maximum_risk
        simulations.append(
            PostureSimulationResult(
                posture=posture,
                label=str(settings["label"]),
                description=str(settings["description"]),
                effective_approval_rate=adjusted.payment_approval_rate,
                effective_refund_rate=adjusted.refund_rate,
                effective_dispute_rate=adjusted.dispute_rate,
                effective_fraud_loss_rate=adjusted.fraud_loss_rate,
                residual_risk_score=round(residual_risk, 2),
                reserve_rate=round(reserve_rate, 4),
                holding_days=holding_days,
                normalized_view=normalized,
                dollar_view=dollars,
                within_risk_appetite=within_appetite,
                assumption_version=str(config["posture_version"]),
            )
        )

    eligible = [item for item in simulations if item.within_risk_appetite]
    def ecosystem_value(item: PostureSimulationResult) -> float:
        return (
            item.dollar_view.control_adjusted_platform_contribution
            - item.dollar_view.merchant_liquidity_burden
        )

    recommended = max(eligible, key=ecosystem_value) if eligible else None
    balanced = next(
        (item for item in eligible if item.posture == PolicyPosture.BALANCED_GROWTH),
        None,
    )
    if recommended and balanced and baseline.decision.value != "MANUAL_REVIEW":
        near_equivalence = merchant.monthly_attempted_payment_volume * float(
            config["risk_appetite"]["balanced_growth_near_equivalence_share"]
        )
        if ecosystem_value(recommended) - ecosystem_value(balanced) <= near_equivalence:
            recommended = balanced
    rationale: list[str] = []
    if baseline.hard_policy_flags:
        rationale.append(
            "No posture is recommended because a non-negotiable boundary is unresolved."
        )
    elif recommended is None:
        rationale.append("No simulated posture brings residual risk within appetite.")
    else:
        rationale.extend(
            [
                f"{recommended.label} provides the preferred synthetic balance of "
                "ecosystem-adjusted contribution, residual risk and control intensity.",
                "Balanced growth is preferred when it is within the configured "
                "near-equivalence band of the highest-value eligible posture; manual-review "
                "stress cases require the stronger case-specific result.",
                "The result depends on editable policy-effect assumptions and is not "
                "an optimal production strategy claim.",
            ]
        )
    return PostureComparisonResult(
        scenario_id=merchant.scenario_id,
        baseline_assessment=baseline,
        postures=simulations,
        recommended_posture=recommended.posture if recommended else None,
        recommendation_rationale=rationale,
        assumption_version=str(config["posture_version"]),
    )
