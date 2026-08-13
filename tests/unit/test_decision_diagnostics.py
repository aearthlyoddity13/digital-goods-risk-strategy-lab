"""Tests for counterfactual and sensitivity diagnostics."""

from merchant_risk.strategy.diagnostics import diagnose
from merchant_risk.strategy.scenarios import get_scenario


def test_diagnostics_return_three_sensitivity_cases() -> None:
    result = diagnose(get_scenario("SD-01", "P0_BASELINE"))
    assert [case.case for case in result.sensitivity_cases] == ["low", "base", "high"]
    assert result.robustness in {"robust_within_tested_range", "assumption_sensitive"}


def test_manual_review_has_binding_constraint_and_counterfactuals() -> None:
    result = diagnose(get_scenario("SD-03", "P2_STRESS"))
    assert result.current_decision.value == "MANUAL_REVIEW"
    assert result.binding_constraints
    assert result.counterfactual_changes
    assert all(
        item.resulting_decision.value in {"APPROVE_WITH_CONTROLS", "APPROVE"}
        for item in result.counterfactual_changes
    )


def test_hard_boundary_has_no_single_metric_counterfactual() -> None:
    merchant = get_scenario("SD-01", "P0_BASELINE").model_copy(
        update={"sanctions_prohibition_confirmed": True}
    )
    result = diagnose(merchant)
    assert result.current_decision.value == "DECLINE"
    assert result.counterfactual_changes == []
    assert "CONFIRMED_SANCTIONS_PROHIBITION" in result.binding_constraints


def test_high_loss_sensitivity_is_not_lower_than_low_loss_case() -> None:
    result = diagnose(get_scenario("SD-02", "P2_STRESS"))
    by_case = {case.case: case for case in result.sensitivity_cases}
    assert by_case["high"].risk_score >= by_case["low"].risk_score
    assert by_case["high"].control_adjusted_contribution <= (
        by_case["low"].control_adjusted_contribution
    )
