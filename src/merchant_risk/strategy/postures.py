"""Mechanism-specific synthetic control packages and commercial comparison."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

from merchant_risk.strategy.assessment import assess
from merchant_risk.strategy.commercial import CommercialAssumptions, calculate_commercial_view
from merchant_risk.strategy.models import (
    AppliedControl,
    DataConfidence,
    PolicyPosture,
    PostureComparisonResult,
    PostureSimulationResult,
    StrategyAssessmentInput,
)
from merchant_risk.strategy.reserve import ReserveAssumptions, recommend_exposure_reserve

ROOT = Path(__file__).resolve().parents[3]
POSTURE_PATH = ROOT / "config" / "strategy" / "postures-0.1.0.yaml"


def _clip_rate(value: float) -> float:
    return max(0.0, min(1.0, value))


@lru_cache(maxsize=1)
def load_posture_config() -> dict[str, Any]:
    with POSTURE_PATH.open(encoding="utf-8") as source:
        config = yaml.safe_load(source)
    if not isinstance(config, dict) or not isinstance(config.get("control_library"), dict):
        raise ValueError("Posture configuration must contain a control_library mapping")
    if not isinstance(config.get("postures"), dict):
        raise ValueError("Posture configuration must contain a postures mapping")
    return config


def _mechanisms(merchant: StrategyAssessmentInput) -> dict[str, str]:
    mechanisms = {"always": "Baseline controls apply to every eligible merchant."}
    if merchant.fraud_loss_rate >= 0.003 or merchant.account_or_key_compromise_indicator >= 0.25:
        mechanisms["payment_abuse"] = "Fraud loss or account-compromise evidence is material."
    if (
        merchant.dispute_rate >= 0.006
        or merchant.post_consumption_dispute_share >= 0.40
        or merchant.renewal_disclosure_score < 0.85
        or merchant.renewal_dispute_share >= 0.30
    ):
        mechanisms["conduct"] = "Recognition, post-consumption or renewal conduct needs control."
    if (
        merchant.usage_meter_reconciliation_rate < 0.99
        or merchant.outstanding_customer_obligation > 0
    ):
        mechanisms["metering"] = "Payment, stored-value and consumption evidence must reconcile."
    if merchant.outstanding_customer_obligation > 0 or merchant.prepaid_exposure_ratio >= 0.10:
        mechanisms["obligation"] = "Unconsumed customer value creates contingent exposure."
    if merchant.content_integrity_indicator >= 0.30 or merchant.platform_dependency >= 0.50:
        mechanisms["continuity"] = "Content or platform dependency can interrupt fulfillment."
    if merchant.mom_volume_growth >= 0.35 or merchant.merchant_age_months <= 12:
        mechanisms["growth_uncertainty"] = (
            "Growth or limited tenure increases observation uncertainty."
        )
    if (
        merchant.data_confidence_level == DataConfidence.LOW
        or not merchant.merchant_identity_resolved
    ):
        mechanisms["material_uncertainty"] = "Material evidence or identity uncertainty remains."
    return mechanisms


def _apply_controls(
    merchant: StrategyAssessmentInput,
    control_codes: list[str],
    library: dict[str, Any],
) -> tuple[StrategyAssessmentInput, list[AppliedControl], float]:
    mechanisms = _mechanisms(merchant)
    approval = merchant.payment_approval_rate
    fraud = merchant.fraud_loss_rate
    disputes = merchant.dispute_rate
    refunds = merchant.refund_rate
    applied: list[AppliedControl] = []
    total_cost = 0.0

    for code in control_codes:
        settings = library[code]
        condition = str(settings["applies_when"])
        if condition not in mechanisms:
            continue
        approval = _clip_rate(approval + float(settings["approval_rate_delta"]))
        fraud = _clip_rate(fraud * float(settings["fraud_loss_multiplier"]))
        disputes = _clip_rate(disputes * float(settings["dispute_rate_multiplier"]))
        refunds = _clip_rate(refunds * float(settings["refund_rate_multiplier"]))
        cost = float(settings["monthly_cost"])
        total_cost += cost
        applied.append(
            AppliedControl(
                code=code,
                label=str(settings["label"]),
                mechanism=str(settings["mechanism"]),
                applicability_basis=mechanisms[condition],
                assumed_effects={
                    "approval_rate_delta": float(settings["approval_rate_delta"]),
                    "fraud_loss_multiplier": float(settings["fraud_loss_multiplier"]),
                    "dispute_rate_multiplier": float(settings["dispute_rate_multiplier"]),
                    "refund_rate_multiplier": float(settings["refund_rate_multiplier"]),
                },
                monthly_cost=cost,
                friction_level=str(settings["friction_level"]),
                release_condition=str(settings["release_condition"]),
            )
        )

    return (
        merchant.model_copy(
            update={
                "payment_approval_rate": approval,
                "fraud_loss_rate": fraud,
                "dispute_rate": disputes,
                "refund_rate": refunds,
            }
        ),
        applied,
        total_cost,
    )


def compare_postures(merchant: StrategyAssessmentInput) -> PostureComparisonResult:
    """Compare three transparent, mechanism-specific control packages."""
    config = load_posture_config()
    baseline = assess(merchant)
    maximum_risk = float(config["risk_appetite"]["maximum_residual_risk_score"])
    simulations: list[PostureSimulationResult] = []

    for posture in PolicyPosture:
        settings = config["postures"][posture.value]
        adjusted, applied, control_cost = _apply_controls(
            merchant,
            list(settings["controls"]),
            config["control_library"],
        )
        adjusted_assessment = assess(adjusted)
        reserve = recommend_exposure_reserve(
            adjusted,
            adjusted_assessment.decision,
            ReserveAssumptions(
                coverage_target=float(settings["reserve_coverage_target"]),
                maximum_reserve_rate=float(settings["maximum_reserve_rate"]),
            ),
        )
        assumptions = CommercialAssumptions(monitoring_and_review_cost=control_cost)
        normalized = calculate_commercial_view(
            adjusted,
            scale=100,
            reserve_rate=reserve.rate,
            holding_days=reserve.holding_days,
            assumptions=assumptions,
        )
        dollars = calculate_commercial_view(
            adjusted,
            scale=merchant.monthly_attempted_payment_volume,
            reserve_rate=reserve.rate,
            holding_days=reserve.holding_days,
            assumptions=assumptions,
        )
        residual_risk = adjusted_assessment.risk_exposure_score
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
                residual_risk_score=residual_risk,
                reserve_rate=reserve.rate,
                holding_days=reserve.holding_days,
                normalized_view=normalized,
                dollar_view=dollars,
                within_risk_appetite=within_appetite,
                assumption_version=str(config["posture_version"]),
                applied_controls=applied,
                mechanism_coverage=sorted({control.mechanism for control in applied}),
                total_monthly_control_cost=control_cost,
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
        rationale.append("No posture is recommended because a hard boundary is unresolved.")
    elif recommended is None:
        rationale.append("No control package brings modeled residual risk within appetite.")
    else:
        rationale.extend(
            [
                f"{recommended.label} is the highest-value eligible mechanism-specific package.",
                (
                    "The recommendation compares contribution after modeled loss, "
                    "control cost and merchant liquidity burden."
                ),
                "Control effects are editable synthetic assumptions, not production estimates.",
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
