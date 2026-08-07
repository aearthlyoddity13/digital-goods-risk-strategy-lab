"""Tests for permissive, balanced-growth and conservative simulations."""

from merchant_risk.strategy.models import PolicyPosture
from merchant_risk.strategy.postures import compare_postures
from merchant_risk.strategy.scenarios import get_scenario


def _by_posture(result):
    return {item.posture: item for item in result.postures}


def test_three_postures_are_returned() -> None:
    result = compare_postures(get_scenario("SD-02", "P2_STRESS"))
    assert {item.posture for item in result.postures} == set(PolicyPosture)
    assert result.assumption_version == "postures-0.2.0"


def test_conservative_posture_reduces_risk_and_approval_but_increases_reserve() -> None:
    result = compare_postures(get_scenario("SD-02", "P2_STRESS"))
    items = _by_posture(result)
    permissive = items[PolicyPosture.PERMISSIVE]
    conservative = items[PolicyPosture.CONSERVATIVE]
    assert conservative.residual_risk_score < permissive.residual_risk_score
    assert conservative.effective_approval_rate < permissive.effective_approval_rate
    assert conservative.reserve_rate > permissive.reserve_rate
    assert conservative.holding_days > permissive.holding_days


def test_normalized_and_dollar_posture_views_reconcile() -> None:
    result = compare_postures(get_scenario("AI-02", "P2_STRESS"))
    for posture in result.postures:
        expected_scale = 1_000_000 / 100
        actual_scale = posture.dollar_view.approved_volume / posture.normalized_view.approved_volume
        assert actual_scale == expected_scale


def test_hard_boundary_blocks_all_posture_recommendations() -> None:
    merchant = get_scenario("AI-01", "P0_BASELINE").model_copy(
        update={"sanctions_prohibition_confirmed": True}
    )
    result = compare_postures(merchant)
    assert result.recommended_posture is None
    assert not any(item.within_risk_appetite for item in result.postures)


def test_healthy_established_merchant_prefers_balanced_growth() -> None:
    result = compare_postures(get_scenario("AI-01", "P0_BASELINE"))
    assert result.recommended_posture == PolicyPosture.BALANCED_GROWTH


def test_severe_combined_stress_can_prefer_conservative_controls() -> None:
    result = compare_postures(get_scenario("SD-03", "P3_OUTCOME"))
    assert result.recommended_posture == PolicyPosture.CONSERVATIVE


def test_short_drama_recovery_prefers_balanced_growth_when_near_equivalent() -> None:
    result = compare_postures(get_scenario("SD-02", "P3_OUTCOME"))
    assert result.recommended_posture == PolicyPosture.BALANCED_GROWTH
