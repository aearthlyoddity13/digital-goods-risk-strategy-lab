"""Strategy-lab assessment routes."""

from __future__ import annotations

from fastapi import APIRouter, HTTPException

from merchant_risk.strategy.assessment import (
    DISCLAIMER,
    METHODOLOGY_VERSION,
    POLICY_VERSION,
    assess,
)
from merchant_risk.strategy.diagnostics import diagnose
from merchant_risk.strategy.experiments import list_experiments, run_experiment
from merchant_risk.strategy.models import (
    CompareRequest,
    CompareResult,
    DecisionDiagnostics,
    ExperimentManifest,
    ExperimentResult,
    PostureComparisonResult,
    ScenarioReference,
    StrategyAssessmentInput,
    StrategyAssessmentResult,
)
from merchant_risk.strategy.postures import compare_postures
from merchant_risk.strategy.scenarios import get_scenario, list_scenarios

router = APIRouter(prefix="/api/v1", tags=["strategy-lab"])


@router.post("/assess", response_model=StrategyAssessmentResult)
def create_strategy_assessment(body: StrategyAssessmentInput) -> StrategyAssessmentResult:
    return assess(body)


@router.get("/archetypes")
def get_archetypes() -> dict[str, object]:
    return {"catalog_version": "scenarios-0.1.0", "items": list_scenarios()}


@router.get("/experiments", response_model=list[ExperimentManifest])
def get_experiments() -> list[ExperimentManifest]:
    return list_experiments()


@router.get("/experiments/{experiment_key}", response_model=ExperimentResult)
def get_experiment_result(experiment_key: str) -> ExperimentResult:
    try:
        return run_experiment(experiment_key)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.post("/compare", response_model=CompareResult)
def compare_scenarios(body: CompareRequest) -> CompareResult:
    try:
        baseline = assess(get_scenario(body.baseline.scenario_key, body.baseline.period))
        candidate = assess(get_scenario(body.candidate.scenario_key, body.candidate.period))
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    deltas = {
        "risk_exposure_score": round(
            candidate.risk_exposure_score - baseline.risk_exposure_score, 2
        ),
        "merchant_strength_score": round(
            candidate.merchant_strength_score - baseline.merchant_strength_score, 2
        ),
        "commercial_value_score": round(
            candidate.commercial_value_score - baseline.commercial_value_score, 2
        ),
        "control_adjusted_platform_contribution": round(
            candidate.dollar_commercial_view.control_adjusted_platform_contribution
            - baseline.dollar_commercial_view.control_adjusted_platform_contribution,
            2,
        ),
    }
    explanation: list[str] = []
    if deltas["risk_exposure_score"] > 0:
        explanation.append("Risk exposure increased in the candidate period.")
    elif deltas["risk_exposure_score"] < 0:
        explanation.append("Risk exposure decreased in the candidate period.")
    if candidate.decision != baseline.decision:
        explanation.append(
            f"Decision changed from {baseline.decision.value} to {candidate.decision.value}."
        )
    if candidate.recommended_controls != baseline.recommended_controls:
        explanation.append("The recommended control package changed with the risk mechanism.")
    if not explanation:
        explanation.append("No material decision change under the current illustrative policy.")
    return CompareResult(
        baseline=baseline,
        candidate=candidate,
        score_deltas=deltas,
        decision_changed=candidate.decision != baseline.decision,
        delta_explanation=explanation,
    )


@router.post("/compare-postures", response_model=PostureComparisonResult)
def compare_policy_postures(body: ScenarioReference) -> PostureComparisonResult:
    try:
        merchant = get_scenario(body.scenario_key, body.period)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return compare_postures(merchant)


@router.post("/diagnostics", response_model=DecisionDiagnostics)
def get_decision_diagnostics(body: ScenarioReference) -> DecisionDiagnostics:
    try:
        merchant = get_scenario(body.scenario_key, body.period)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return diagnose(merchant)


@router.get("/methodology")
def get_methodology() -> dict[str, object]:
    return {
        "methodology_version": METHODOLOGY_VERSION,
        "policy_version": POLICY_VERSION,
        "posture": "balanced_growth",
        "payment_scope": "direct_web_payments",
        "data_boundary": DISCLAIMER,
        "outputs": [
            "risk_exposure",
            "merchant_strength",
            "commercial_value",
            "recommended_controls",
            "normalized_commercial_view",
            "illustrative_dollar_view",
        ],
    }
