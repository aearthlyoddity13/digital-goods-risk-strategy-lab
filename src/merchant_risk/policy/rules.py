"""Hard policy rules and action selection."""

from __future__ import annotations

from merchant_risk.domain.config import get_policy_config
from merchant_risk.domain.models import (
    DecisionAction,
    MerchantFeatures,
    VerificationStatus,
)


def evaluate_hard_flags(m: MerchantFeatures) -> list[str]:
    cfg = get_policy_config()
    flags: list[str] = []
    if m.chargeback_rate >= float(cfg["hard_decline_chargeback_rate"]):
        flags.append("HARD_DECLINE_CHARGEBACK_RATE")
    if m.fraud_alert_rate >= float(cfg["hard_decline_fraud_alert_rate"]):
        flags.append("HARD_DECLINE_FRAUD_ALERT_RATE")
    if m.negative_balance_flag and m.cash_buffer_months < 0.5:
        flags.append("HARD_REVIEW_NEGATIVE_BALANCE_THIN_BUFFER")
    if (
        cfg.get("hard_review_unverified")
        and m.verification_status == VerificationStatus.UNVERIFIED
    ):
        flags.append("HARD_REVIEW_UNVERIFIED")
    if m.verification_status == VerificationStatus.PARTIAL:
        flags.append("PARTIAL_VERIFICATION")
    return flags


def select_action(
    m: MerchantFeatures,
    risk_score: float,
    expected_loss: float,
    hard_flags: list[str],
) -> tuple[DecisionAction, bool]:
    """Return (action, requires_human_review)."""
    cfg = get_policy_config()
    approve_max = float(cfg["approve_max_score"])
    controls_max = float(cfg["controls_max_score"])
    review_max = float(cfg["review_max_score"])
    mr = cfg["manual_review"]

    decline_flags = [f for f in hard_flags if f.startswith("HARD_DECLINE_")]
    if decline_flags:
        return DecisionAction.DECLINE, True

    # Score-based ladder
    if risk_score <= approve_max:
        action = DecisionAction.APPROVE
    elif risk_score <= controls_max:
        action = DecisionAction.APPROVE_WITH_CONTROLS
    elif risk_score <= review_max:
        action = DecisionAction.MANUAL_REVIEW
    else:
        action = DecisionAction.DECLINE

    requires_review = action == DecisionAction.MANUAL_REVIEW

    # Escalations into review
    if "HARD_REVIEW_UNVERIFIED" in hard_flags and action in {
        DecisionAction.APPROVE,
        DecisionAction.APPROVE_WITH_CONTROLS,
    }:
        action = DecisionAction.MANUAL_REVIEW
        requires_review = True

    thin_buffer = "HARD_REVIEW_NEGATIVE_BALANCE_THIN_BUFFER" in hard_flags
    if thin_buffer and action != DecisionAction.DECLINE:
        action = DecisionAction.MANUAL_REVIEW
        requires_review = True

    if mr.get("partial_verification") and "PARTIAL_VERIFICATION" in hard_flags:
        if action == DecisionAction.APPROVE:
            action = DecisionAction.MANUAL_REVIEW
            requires_review = True

    growth_spike = float(mr.get("growth_spike", 2.0))
    if m.tpv_growth_3m >= growth_spike and action == DecisionAction.APPROVE_WITH_CONTROLS:
        action = DecisionAction.MANUAL_REVIEW
        requires_review = True

    el_ratio = expected_loss / max(m.projected_monthly_tpv, 1.0)
    if el_ratio >= float(mr.get("el_over_tpv", 0.08)) and action != DecisionAction.DECLINE:
        if action == DecisionAction.APPROVE:
            action = DecisionAction.APPROVE_WITH_CONTROLS
        elif action == DecisionAction.APPROVE_WITH_CONTROLS:
            action = DecisionAction.MANUAL_REVIEW
            requires_review = True

    if action == DecisionAction.DECLINE:
        requires_review = True

    return action, requires_review
