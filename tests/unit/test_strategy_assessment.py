"""Unit tests for the balanced-growth strategy assessment."""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from merchant_risk.domain.models import DecisionAction
from merchant_risk.strategy.assessment import assess
from merchant_risk.strategy.models import StrategyAssessmentInput


def _payload() -> dict[str, object]:
    return {
        "merchant_id": "SYN-SD-01",
        "scenario_id": "SD-01-P0",
        "merchant_category": "short_drama",
        "merchant_age_months": 6,
        "monthly_attempted_payment_volume": 1_000_000,
        "payment_approval_rate": 0.955,
        "successful_fulfillment_rate": 0.99,
        "average_ticket_size": 12,
        "mom_volume_growth": 0.18,
        "refund_rate": 0.02,
        "dispute_rate": 0.006,
        "fraud_loss_rate": 0.0025,
        "complaint_rate": 0.003,
        "cross_border_share": 0.25,
        "prepaid_exposure_ratio": 0.18,
        "outstanding_customer_obligation": 180_000,
        "content_integrity_indicator": 0.20,
        "platform_dependency": 0.35,
        "service_reliability": 0.97,
        "support_response_within_sla": 0.92,
        "data_confidence_level": "medium",
        "purchased_coin_value": 300_000,
        "consumed_purchased_coin_value": 110_000,
        "refunded_purchased_coin_value": 10_000,
        "unused_purchased_coin_value": 180_000,
        "available_merchant_balance": 100_000,
    }


def test_short_drama_baseline_returns_explainable_controls() -> None:
    result = assess(StrategyAssessmentInput.model_validate(_payload()))
    assert result.decision in {
        DecisionAction.APPROVE_WITH_CONTROLS,
        DecisionAction.MANUAL_REVIEW,
    }
    assert "rolling_reserve" in result.recommended_controls
    assert result.normalized_commercial_view.attempted_volume == 100
    assert result.dollar_commercial_view.attempted_volume == 1_000_000
    assert result.reserve.amount > 0


def test_coin_ledger_must_reconcile() -> None:
    payload = _payload()
    payload["unused_purchased_coin_value"] = 1
    with pytest.raises(ValidationError):
        StrategyAssessmentInput.model_validate(payload)


def test_service_credit_ledger_must_reconcile() -> None:
    payload = _payload()
    payload.update(
        {
            "merchant_category": "ai_subscription",
            "purchased_service_credit_value": 100_000,
            "consumed_service_credit_value": 70_000,
            "refunded_service_credit_value": 5_000,
            "unused_service_credit_value": 1,
        }
    )
    with pytest.raises(ValidationError):
        StrategyAssessmentInput.model_validate(payload)


def test_ai_renewal_stress_surfaces_conduct_control() -> None:
    from merchant_risk.strategy.scenarios import get_scenario

    result = assess(get_scenario("AI-02", "P1_EARLY_SIGNAL"))
    assert "subscription_practice_review" in result.recommended_controls
    assert "RENEWAL_CONDUCT" in {driver.code for driver in result.primary_risk_drivers}


def test_ai_renewal_control_releases_after_high_confidence_remediation() -> None:
    from merchant_risk.strategy.scenarios import get_scenario

    result = assess(get_scenario("AI-02", "P3_OUTCOME"))
    assert "subscription_practice_review" not in result.recommended_controls


def test_ai_key_abuse_stress_surfaces_targeted_controls() -> None:
    from merchant_risk.strategy.scenarios import get_scenario

    result = assess(get_scenario("AI-03", "P2_STRESS"))
    assert result.decision == DecisionAction.MANUAL_REVIEW
    assert "account_and_key_security_review" in result.recommended_controls
    assert "usage_meter_reconciliation" in result.recommended_controls
    assert "usage_spend_limit" in result.recommended_controls


def test_hard_boundary_cannot_be_offset_by_commercial_value() -> None:
    payload = _payload()
    payload["prohibited_activity_confirmed"] = True
    payload["mom_volume_growth"] = 5.0
    result = assess(StrategyAssessmentInput.model_validate(payload))
    assert result.decision == DecisionAction.DECLINE
    assert result.recommended_controls == ["decline_or_offboard"]


def test_normalized_and_dollar_views_scale_consistently() -> None:
    result = assess(StrategyAssessmentInput.model_validate(_payload()))
    ratio = (
        result.dollar_commercial_view.approved_volume
        / result.normalized_commercial_view.approved_volume
    )
    assert ratio == pytest.approx(10_000)
