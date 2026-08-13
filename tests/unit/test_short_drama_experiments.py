"""Controlled experiment tests for short-drama risk mechanisms."""

from merchant_risk.strategy.experiments import list_experiments, run_experiment


def test_four_experiments_have_complete_manifests() -> None:
    manifests = list_experiments()
    assert len(manifests) == 4
    for manifest in manifests:
        assert manifest.hypothesis
        assert manifest.variables_held_constant
        assert manifest.expected_direction
        assert manifest.alternative_explanation
        assert manifest.falsification_check
        assert len(manifest.cases) >= 2


def test_all_directional_checks_pass() -> None:
    for manifest in list_experiments():
        assert run_experiment(manifest.experiment_key).directional_check_passed


def test_obligation_pair_holds_payment_risk_constant() -> None:
    result = run_experiment("SD-X1-OBLIGATION")
    by_id = {case.case_id: case.assessment for case in result.cases}
    low = by_id["LOW_OBLIGATION"]
    high = by_id["HIGH_OBLIGATION"]
    assert low.component_scores["payment_and_conduct"] == high.component_scores[
        "payment_and_conduct"
    ]
    assert high.reserve.gross_stressed_exposure > low.reserve.gross_stressed_exposure


def test_credential_pair_holds_obligation_exposure_constant() -> None:
    result = run_experiment("SD-X2-CREDENTIAL")
    by_id = {case.case_id: case.assessment for case in result.cases}
    low = by_id["LOW_ABUSE"]
    high = by_id["HIGH_ABUSE"]
    low_horizon = {x.horizon_days: x for x in low.reserve.horizon_analysis}
    high_horizon = {x.horizon_days: x for x in high.reserve.horizon_analysis}
    for horizon in (30, 60, 90):
        assert (
            low_horizon[horizon].contingent_obligation_exposure
            == high_horizon[horizon].contingent_obligation_exposure
        )
