"""Explainable balanced-growth assessment orchestration."""

from __future__ import annotations

from merchant_risk.domain.models import DecisionAction
from merchant_risk.strategy.commercial import calculate_commercial_view
from merchant_risk.strategy.models import (
    DataConfidence,
    Driver,
    StrategyAssessmentInput,
    StrategyAssessmentResult,
)
from merchant_risk.strategy.reserve import recommend_exposure_reserve

METHODOLOGY_VERSION = "strategy-0.5.0"
POLICY_VERSION = "balanced-growth-0.2.0"
DISCLAIMER = (
    "Demonstration data: aggregated and synthetic. No confidential merchant, customer "
    "or payment-platform data is used."
)


def _clip(value: float) -> float:
    return max(0.0, min(100.0, value))


def _scores(m: StrategyAssessmentInput) -> tuple[dict[str, float], float, float, float]:
    payment = _clip(
        m.dispute_rate / 0.03 * 35
        + m.refund_rate / 0.10 * 20
        + m.fraud_loss_rate / 0.03 * 35
        + m.complaint_rate / 0.03 * 10
        + (1 - m.renewal_disclosure_score) * 15
        + m.renewal_dispute_share * 10
    )
    exposure = _clip(
        m.prepaid_exposure_ratio / 0.75 * 60
        + min(m.outstanding_customer_obligation / max(m.monthly_attempted_payment_volume, 1), 1)
        * 40
    )
    integrity = _clip(m.content_integrity_indicator * 75 + m.platform_dependency * 25)
    cross_border = _clip(m.cross_border_share * 100)
    maturity_penalty = _clip((12 - min(m.merchant_age_months, 12)) / 12 * 100)
    confidence_penalty = {
        DataConfidence.HIGH: 10.0,
        DataConfidence.MEDIUM: 45.0,
        DataConfidence.LOW: 80.0,
    }[m.data_confidence_level]
    interaction = 0.0
    if m.mom_volume_growth >= 0.5 and m.merchant_age_months <= 12:
        interaction += 10
    if m.prepaid_exposure_ratio >= 0.5:
        interaction += 8
    if m.post_consumption_dispute_share >= 0.65:
        interaction += 8
    if m.virtual_asset_transferability:
        interaction += 7
    if m.account_or_key_compromise_indicator >= 0.50 and m.fraud_loss_rate >= 0.005:
        interaction += 8
    if m.usage_meter_reconciliation_rate < 0.95 and m.complaint_rate >= 0.005:
        interaction += 6
    if m.renewal_dispute_share >= 0.50 and m.complaint_rate >= 0.005:
        interaction += 6
    components = {
        "payment_and_conduct": round(payment, 2),
        "contingent_exposure": round(exposure, 2),
        "content_and_dependency": round(integrity, 2),
        "cross_border": round(cross_border, 2),
        "maturity_and_confidence": round((maturity_penalty + confidence_penalty) / 2, 2),
        "interaction_uplift": round(min(interaction, 20), 2),
    }
    risk = _clip(
        payment * 0.32
        + exposure * 0.24
        + integrity * 0.18
        + cross_border * 0.10
        + ((maturity_penalty + confidence_penalty) / 2) * 0.16
        + min(interaction, 20)
    )
    strength = _clip(
        min(m.merchant_age_months / 36, 1) * 30
        + m.service_reliability * 25
        + m.support_response_within_sla * 20
        + (100 - confidence_penalty) * 0.25
    )
    commercial = _clip(
        50
        + min(max(m.mom_volume_growth, -0.5), 1.0) * 25
        + min(m.monthly_attempted_payment_volume / 1_000_000, 1.0) * 25
    )
    return components, risk, strength, commercial


def assess(m: StrategyAssessmentInput) -> StrategyAssessmentResult:
    components, risk, strength, commercial = _scores(m)
    hard_flags: list[str] = []
    if m.prohibited_activity_confirmed:
        hard_flags.append("CONFIRMED_PROHIBITED_ACTIVITY")
    if m.sanctions_prohibition_confirmed:
        hard_flags.append("CONFIRMED_SANCTIONS_PROHIBITION")
    if m.deliberate_transaction_laundering_confirmed:
        hard_flags.append("CONFIRMED_TRANSACTION_LAUNDERING")
    if not m.merchant_identity_resolved and m.monthly_attempted_payment_volume >= 100_000:
        hard_flags.append("UNRESOLVED_IDENTITY_AT_MATERIAL_EXPOSURE")

    if hard_flags:
        decision = DecisionAction.DECLINE
    elif risk < 30:
        decision = DecisionAction.APPROVE
    elif risk < 55:
        decision = DecisionAction.APPROVE_WITH_CONTROLS
    else:
        decision = DecisionAction.MANUAL_REVIEW

    review_triggers: list[str] = []
    if (
        m.data_confidence_level == DataConfidence.LOW
        and m.monthly_attempted_payment_volume >= 1_000_000
    ):
        review_triggers.append("LOW_CONFIDENCE_AT_MATERIAL_EXPOSURE")
    if m.content_integrity_indicator >= 0.60 and m.complaint_rate >= 0.01:
        review_triggers.append("COMBINED_INTEGRITY_AND_COMPLAINT_DETERIORATION")
    if m.fraud_loss_rate >= 0.008 and m.dispute_rate >= 0.01:
        review_triggers.append("CONCENTRATED_FRAUD_AND_DISPUTE_EVENT")
    if m.content_integrity_indicator >= 0.50 and m.prepaid_exposure_ratio >= 0.30:
        review_triggers.append("INTEGRITY_EVENT_WITH_MATERIAL_OBLIGATION_GAP")
    if (
        m.account_or_key_compromise_indicator >= 0.65
        and m.anomalous_usage_share >= 0.12
        and m.fraud_loss_rate >= 0.005
    ):
        review_triggers.append("CONCENTRATED_ACCOUNT_OR_KEY_ABUSE")
    if m.usage_meter_reconciliation_rate < 0.90 and m.complaint_rate >= 0.008:
        review_triggers.append("USAGE_METER_AND_COMPLAINT_DIVERGENCE")
    if review_triggers and decision != DecisionAction.DECLINE:
        decision = DecisionAction.MANUAL_REVIEW

    controls: list[str] = []
    if decision == DecisionAction.APPROVE:
        controls.append("standard_monitoring")
    else:
        controls.append("enhanced_monitoring")
    if m.prepaid_exposure_ratio >= 0.14:
        controls.append("rolling_reserve")
    if m.mom_volume_growth >= 0.5:
        controls.append("progressive_processing_limit")
    if m.content_integrity_indicator >= 0.45:
        controls.append("content_and_rights_review")
    if m.complaint_rate >= 0.008:
        controls.append("customer_practice_remediation")
    if m.data_confidence_level == DataConfidence.LOW:
        controls.append("additional_merchant_information")
    if m.merchant_category.value == "ai_subscription" and (
        (m.merchant_age_months <= 12 and m.data_confidence_level != DataConfidence.HIGH)
        or m.renewal_disclosure_score < 0.75
        or m.renewal_dispute_share >= 0.40
    ):
        controls.append("subscription_practice_review")
    if m.account_or_key_compromise_indicator >= 0.45:
        controls.append("account_and_key_security_review")
    if m.usage_meter_reconciliation_rate < 0.97:
        controls.append("usage_meter_reconciliation")
    if m.anomalous_usage_share >= 0.10 or m.postpaid_usage_exposure_ratio >= 0.10:
        controls.append("usage_spend_limit")
    if decision == DecisionAction.MANUAL_REVIEW:
        controls.append("manual_underwriting_review")
    if decision == DecisionAction.DECLINE:
        controls = ["decline_or_offboard"]
    controls = list(dict.fromkeys(controls))

    # The public decision label must agree with the actual control package.
    # An approval that requires a reserve, remediation or another non-standard
    # control is APPROVE_WITH_CONTROLS even when the summary risk score is low.
    if decision == DecisionAction.APPROVE and controls != ["standard_monitoring"]:
        decision = DecisionAction.APPROVE_WITH_CONTROLS
        controls = [
            "enhanced_monitoring" if control == "standard_monitoring" else control
            for control in controls
        ]

    reserve = recommend_exposure_reserve(m, decision)
    reserve_rate = reserve.rate
    holding_days = reserve.holding_days

    normalized = calculate_commercial_view(
        m, scale=100, reserve_rate=reserve_rate, holding_days=holding_days
    )
    dollar = calculate_commercial_view(
        m,
        scale=m.monthly_attempted_payment_volume,
        reserve_rate=reserve_rate,
        holding_days=holding_days,
    )
    drivers: list[Driver] = []
    if m.dispute_rate >= 0.008:
        drivers.append(
            Driver(
                code="DISPUTE_PRESSURE", label="Elevated synthetic disputes", value=m.dispute_rate
            )
        )
    if m.prepaid_exposure_ratio >= 0.15:
        drivers.append(
            Driver(
                code="CUSTOMER_OBLIGATION",
                label="Outstanding prepaid exposure",
                value=m.prepaid_exposure_ratio,
            )
        )
    if m.content_integrity_indicator >= 0.45:
        drivers.append(
            Driver(
                code="INTEGRITY_SIGNAL",
                label="Content or rights concern",
                value=m.content_integrity_indicator,
            )
        )
    if m.mom_volume_growth >= 0.5:
        drivers.append(
            Driver(
                code="RAPID_GROWTH",
                label="Rapid growth with limited observation",
                value=m.mom_volume_growth,
            )
        )
    if m.renewal_disclosure_score < 0.75 or m.renewal_dispute_share >= 0.40:
        drivers.append(
            Driver(
                code="RENEWAL_CONDUCT",
                label="Trial or renewal conduct requires remediation",
                value=m.renewal_disclosure_score,
            )
        )
    if m.account_or_key_compromise_indicator >= 0.45:
        drivers.append(
            Driver(
                code="ACCOUNT_OR_KEY_ABUSE",
                label="Concentrated account or API-key abuse signal",
                value=m.account_or_key_compromise_indicator,
            )
        )
    if m.usage_meter_reconciliation_rate < 0.97:
        drivers.append(
            Driver(
                code="USAGE_METER_INTEGRITY",
                label="Usage meter requires reconciliation",
                value=m.usage_meter_reconciliation_rate,
            )
        )
    for trigger in review_triggers:
        drivers.append(
            Driver(
                code=trigger,
                label="Combined indicators require human review",
            )
        )

    protective: list[str] = []
    if m.merchant_age_months >= 24:
        protective.append("Established operating tenure")
    if m.service_reliability >= 0.98:
        protective.append("Strong service reliability")
    if m.support_response_within_sla >= 0.90:
        protective.append("Strong support responsiveness")
    if m.data_confidence_level == DataConfidence.HIGH:
        protective.append("High synthetic data confidence")

    risk_level = (
        "low" if risk < 30 else "moderate" if risk < 55 else "elevated" if risk < 75 else "high"
    )
    return StrategyAssessmentResult(
        merchant_id=m.merchant_id,
        scenario_id=m.scenario_id,
        decision=decision,
        risk_level=risk_level,
        risk_exposure_score=round(risk, 2),
        merchant_strength_score=round(strength, 2),
        commercial_value_score=round(commercial, 2),
        component_scores=components,
        primary_risk_drivers=drivers,
        protective_factors=protective,
        recommended_controls=controls,
        reserve=reserve,
        normalized_commercial_view=normalized,
        dollar_commercial_view=dollar,
        conditions_to_reduce_controls=[
            "Sustained improvement in disputes, complaints and fraud loss",
            "Stable growth within the agreed processing band",
            "Verified customer-obligation and fulfillment evidence",
        ],
        escalation_triggers=[
            "Confirmed prohibited activity, sanctions exposure or transaction laundering",
            "Accelerating uncovered customer obligations",
            "Continued conduct or integrity deterioration after remediation",
        ],
        hard_policy_flags=hard_flags,
        confidence=m.data_confidence_level,
        methodology_version=METHODOLOGY_VERSION,
        policy_version=POLICY_VERSION,
        synthetic_data_disclaimer=DISCLAIMER,
        limitations=[
            "Illustrative rules and assumptions; not calibrated to real platform losses.",
            "Not for production merchant decisions.",
            "Customer-level telemetry is synthetic and aggregated for demonstration.",
        ],
    )
