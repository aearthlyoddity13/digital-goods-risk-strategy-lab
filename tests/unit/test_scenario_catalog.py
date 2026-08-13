"""Tests for versioned synthetic scenario records."""

from merchant_risk.domain.models import DecisionAction
from merchant_risk.strategy.assessment import assess
from merchant_risk.strategy.scenarios import get_scenario, list_scenarios


def test_catalog_contains_eight_scenarios_and_four_periods_each() -> None:
    items = list_scenarios()
    assert len(items) == 8
    assert all(len(item["periods"]) == 4 for item in items)


def test_all_32_records_validate_and_assess() -> None:
    for item in list_scenarios():
        for period in item["periods"]:
            result = assess(get_scenario(str(item["scenario_key"]), str(period)))
            assert result.methodology_version == "strategy-0.5.0"
            assert result.normalized_commercial_view.attempted_volume == 100


def test_short_drama_coin_ledgers_reconcile() -> None:
    for key in ("SD-01", "SD-02", "SD-03"):
        scenario = get_scenario(key, "P2_STRESS")
        assert scenario.unused_purchased_coin_value == (
            scenario.purchased_coin_value
            - scenario.consumed_purchased_coin_value
            - scenario.refunded_purchased_coin_value
        )


def test_documented_stress_periods_reach_manual_review_without_auto_decline() -> None:
    stress_cases = [
        ("SD-02", "P2_STRESS"),
        ("SD-03", "P2_STRESS"),
        ("AI-03", "P2_STRESS"),
        ("WF-01", "P2_STRESS"),
        ("GM-01", "P2_STRESS"),
    ]
    for scenario_key, period in stress_cases:
        result = assess(get_scenario(scenario_key, period))
        assert result.decision == DecisionAction.MANUAL_REVIEW


def test_established_ai_baseline_is_approved() -> None:
    result = assess(get_scenario("AI-01", "P0_BASELINE"))
    assert result.decision == DecisionAction.APPROVE


def test_young_ai_subscription_receives_practice_controls() -> None:
    result = assess(get_scenario("AI-02", "P0_BASELINE"))
    assert result.decision == DecisionAction.APPROVE_WITH_CONTROLS
    assert "subscription_practice_review" in result.recommended_controls
