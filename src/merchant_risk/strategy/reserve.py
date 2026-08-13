"""Exposure-based rolling-reserve methodology for the strategy demonstrator."""

from __future__ import annotations

from dataclasses import dataclass

from merchant_risk.domain.models import DecisionAction
from merchant_risk.strategy.models import (
    DataConfidence,
    HorizonExposure,
    ReserveRecommendation,
    StrategyAssessmentInput,
)


@dataclass(frozen=True)
class ReserveAssumptions:
    """Synthetic assumptions; these are not calibrated platform estimates."""

    horizons: tuple[int, ...] = (30, 60, 90)
    coverage_target: float = 0.95
    dispute_loss_severity: float = 0.70
    payment_loss_stress_multiplier: float = 1.50
    obligation_realization_by_horizon: tuple[float, ...] = (0.35, 0.60, 0.80)
    postpaid_realization_by_horizon: tuple[float, ...] = (0.50, 0.75, 0.90)
    merchant_balance_haircut_high: float = 0.10
    merchant_balance_haircut_medium: float = 0.25
    merchant_balance_haircut_low: float = 0.45
    maximum_reserve_rate: float = 0.20


def _balance_haircut(confidence: DataConfidence, assumptions: ReserveAssumptions) -> float:
    return {
        DataConfidence.HIGH: assumptions.merchant_balance_haircut_high,
        DataConfidence.MEDIUM: assumptions.merchant_balance_haircut_medium,
        DataConfidence.LOW: assumptions.merchant_balance_haircut_low,
    }[confidence]


def _recommended_horizon(merchant: StrategyAssessmentInput) -> int:
    """Select a visible demonstration horizon from obligation and evidence conditions."""
    if (
        merchant.prepaid_exposure_ratio >= 0.30
        or merchant.content_integrity_indicator >= 0.60
        or merchant.data_confidence_level == DataConfidence.LOW
    ):
        return 90
    if (
        merchant.prepaid_exposure_ratio >= 0.14
        or merchant.postpaid_usage_exposure_ratio >= 0.10
        or merchant.dispute_rate >= 0.008
    ):
        return 60
    return 30


def recommend_exposure_reserve(
    merchant: StrategyAssessmentInput,
    decision: DecisionAction,
    assumptions: ReserveAssumptions | None = None,
) -> ReserveRecommendation:
    """Size incremental protection from stressed exposure rather than a decision label."""
    a = assumptions or ReserveAssumptions()
    approved_volume = merchant.monthly_attempted_payment_volume * merchant.payment_approval_rate
    existing_reserve = approved_volume * merchant.current_reserve_rate
    collectible_balance = merchant.available_merchant_balance * (
        1 - _balance_haircut(merchant.data_confidence_level, a)
    )
    maximum_reserve = approved_volume * a.maximum_reserve_rate
    analyses: list[HorizonExposure] = []

    for index, horizon in enumerate(a.horizons):
        horizon_factor = horizon / 30
        expected_payment_loss = approved_volume * (
            merchant.fraud_loss_rate
            + merchant.dispute_rate * a.dispute_loss_severity
        ) * horizon_factor
        stressed_payment_loss = expected_payment_loss * a.payment_loss_stress_multiplier
        obligation_exposure = (
            merchant.outstanding_customer_obligation
            * a.obligation_realization_by_horizon[index]
        )
        postpaid_exposure = (
            approved_volume
            * merchant.postpaid_usage_exposure_ratio
            * a.postpaid_realization_by_horizon[index]
        )
        gross_exposure = stressed_payment_loss + obligation_exposure + postpaid_exposure
        target_protection = gross_exposure * a.coverage_target
        protection_gap = max(
            0.0,
            target_protection - collectible_balance - existing_reserve,
        )
        incremental_reserve = min(protection_gap, maximum_reserve)
        implied_rate = incremental_reserve / approved_volume if approved_volume else 0.0
        analyses.append(
            HorizonExposure(
                horizon_days=horizon,
                expected_payment_loss=round(expected_payment_loss, 2),
                stressed_payment_loss=round(stressed_payment_loss, 2),
                contingent_obligation_exposure=round(obligation_exposure, 2),
                postpaid_usage_exposure=round(postpaid_exposure, 2),
                gross_stressed_exposure=round(gross_exposure, 2),
                coverage_target=a.coverage_target,
                target_protection=round(target_protection, 2),
                available_merchant_balance=round(collectible_balance, 2),
                existing_reserve=round(existing_reserve, 2),
                incremental_protection_gap=round(protection_gap, 2),
                implied_reserve_rate=round(implied_rate, 4),
            )
        )

    selected_horizon = _recommended_horizon(merchant)
    selected = next(item for item in analyses if item.horizon_days == selected_horizon)
    if decision == DecisionAction.DECLINE:
        reserve_rate = 0.0
        reserve_amount = 0.0
    else:
        reserve_rate = selected.implied_reserve_rate
        reserve_amount = min(selected.incremental_protection_gap, maximum_reserve)

    rationale = [
        (
            f"Protection is sized to {a.coverage_target:.0%} of modeled stressed "
            f"exposure over {selected_horizon} days."
        ),
        (
            "The calculation recognizes haircut-adjusted merchant balance and the "
            "existing rolling reserve."
        ),
    ]
    if merchant.outstanding_customer_obligation > 0:
        rationale.append("Unconsumed customer value contributes to contingent obligation exposure.")
    if reserve_amount == 0 and decision != DecisionAction.DECLINE:
        rationale.append("Available protection covers the selected synthetic exposure target.")
    capped = selected.incremental_protection_gap > maximum_reserve
    if capped:
        rationale.append("The calculated protection gap exceeds the illustrative 20% reserve cap.")

    return ReserveRecommendation(
        rate=round(reserve_rate, 4),
        amount=round(reserve_amount, 2),
        holding_days=0 if decision == DecisionAction.DECLINE else selected_horizon,
        rationale=rationale,
        coverage_target=a.coverage_target,
        gross_stressed_exposure=selected.gross_stressed_exposure,
        available_protection=round(collectible_balance + existing_reserve, 2),
        incremental_protection_gap=selected.incremental_protection_gap,
        capped_by_policy=capped,
        horizon_analysis=analyses,
    )
