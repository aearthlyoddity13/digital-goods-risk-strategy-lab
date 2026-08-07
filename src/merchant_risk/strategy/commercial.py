"""Traceable commercial calculations for normalized and dollar views."""

from __future__ import annotations

from dataclasses import dataclass

from merchant_risk.strategy.models import CommercialView, StrategyAssessmentInput


@dataclass(frozen=True)
class CommercialAssumptions:
    platform_revenue_rate: float = 0.025
    dispute_loss_severity: float = 0.70
    dispute_cost_per_case: float = 15.0
    monitoring_and_review_cost: float = 500.0
    merchant_annual_liquidity_cost: float = 0.12
    false_positive_volume_share: float = 0.0
    legitimate_share_of_blocked_volume: float = 0.85
    contingent_exposure_realization_rate: float = 0.10


def calculate_commercial_view(
    merchant: StrategyAssessmentInput,
    *,
    scale: float,
    reserve_rate: float,
    holding_days: int,
    assumptions: CommercialAssumptions | None = None,
) -> CommercialView:
    """Calculate one view; scale is attempted volume for the requested presentation."""
    a = assumptions or CommercialAssumptions()
    approved = scale * merchant.payment_approval_rate
    fulfilled = approved * merchant.successful_fulfillment_rate
    refunded = approved * merchant.refund_rate
    disputed = approved * merchant.dispute_rate
    sustainable = max(0.0, fulfilled - refunded - disputed)
    gross_revenue = sustainable * a.platform_revenue_rate
    fraud_loss = approved * merchant.fraud_loss_rate
    dispute_principal_loss = disputed * a.dispute_loss_severity
    tx_count = approved / merchant.average_ticket_size
    dispute_count = tx_count * merchant.dispute_rate
    dispute_cost = dispute_count * a.dispute_cost_per_case
    scale_ratio = scale / max(merchant.monthly_attempted_payment_volume, 1.0)
    obligation = merchant.outstanding_customer_obligation * scale_ratio
    available_balance = merchant.available_merchant_balance * scale_ratio
    reserved_funds = approved * reserve_rate
    gross_uncovered = max(0.0, obligation - available_balance - reserved_funds)
    uncovered = gross_uncovered * a.contingent_exposure_realization_rate
    operating_cost = a.monitoring_and_review_cost * scale_ratio
    blocked_volume = scale * a.false_positive_volume_share
    false_positive_cost = (
        blocked_volume * a.legitimate_share_of_blocked_volume * a.platform_revenue_rate
    )
    contribution = (
        gross_revenue
        - fraud_loss
        - dispute_principal_loss
        - dispute_cost
        - uncovered
        - operating_cost
        - false_positive_cost
    )
    liquidity_burden = reserved_funds * a.merchant_annual_liquidity_cost * holding_days / 365
    return CommercialView(
        scale_label="per_usd_100" if scale == 100 else "illustrative_dollars",
        attempted_volume=round(scale, 2),
        approved_volume=round(approved, 2),
        sustainable_payment_volume=round(sustainable, 2),
        gross_platform_revenue=round(gross_revenue, 2),
        expected_fraud_loss=round(fraud_loss, 2),
        expected_dispute_principal_loss=round(dispute_principal_loss, 2),
        expected_dispute_operating_cost=round(dispute_cost, 2),
        expected_uncovered_exposure=round(uncovered, 2),
        monitoring_and_review_cost=round(operating_cost, 2),
        false_positive_opportunity_cost=round(false_positive_cost, 2),
        control_adjusted_platform_contribution=round(contribution, 2),
        reserved_funds=round(reserved_funds, 2),
        merchant_liquidity_burden=round(liquidity_burden, 2),
    )
