"""Controlled short-drama experiments with explicit manifests."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

from merchant_risk.strategy.assessment import assess
from merchant_risk.strategy.models import (
    ExperimentCase,
    ExperimentCaseResult,
    ExperimentManifest,
    ExperimentResult,
    StrategyAssessmentInput,
)

ROOT = Path(__file__).resolve().parents[3]
EXPERIMENT_PATH = ROOT / "data" / "scenarios" / "short-drama-experiments-0.1.0.yaml"


@lru_cache(maxsize=1)
def load_experiments() -> dict[str, Any]:
    with EXPERIMENT_PATH.open(encoding="utf-8") as source:
        payload = yaml.safe_load(source)
    if not isinstance(payload, dict) or not isinstance(payload.get("experiments"), list):
        raise ValueError("Experiment catalog must contain an experiments list")
    return payload


def list_experiments() -> list[ExperimentManifest]:
    return [_manifest(item) for item in load_experiments()["experiments"]]


def _manifest(item: dict[str, Any]) -> ExperimentManifest:
    return ExperimentManifest(
        experiment_key=str(item["experiment_key"]),
        name=str(item["name"]),
        mechanism=str(item["mechanism"]),
        hypothesis=str(item["hypothesis"]),
        variables_held_constant=list(item["variables_held_constant"]),
        expected_direction=list(item["expected_direction"]),
        alternative_explanation=str(item["alternative_explanation"]),
        falsification_check=str(item["falsification_check"]),
        cases=[
            ExperimentCase(
                case_id=str(case["case_id"]),
                label=str(case["label"]),
                changed_variables=dict(case["changes"]),
            )
            for case in item["cases"]
        ],
    )


def _scenario(payload: dict[str, Any], case_id: str) -> StrategyAssessmentInput:
    values = dict(payload)
    values["scenario_id"] = case_id
    return StrategyAssessmentInput.model_validate(values)


def run_experiment(experiment_key: str) -> ExperimentResult:
    catalog = load_experiments()
    item = next(
        (row for row in catalog["experiments"] if row["experiment_key"] == experiment_key),
        None,
    )
    if item is None:
        raise KeyError(f"Unknown experiment: {experiment_key}")
    baseline_input = _scenario(dict(catalog["baseline"]), f"{experiment_key}-BASE")
    baseline = assess(baseline_input)
    cases: list[ExperimentCaseResult] = []
    deltas: dict[str, dict[str, float]] = {}
    for case in item["cases"]:
        payload = dict(catalog["baseline"])
        payload.update(case["changes"])
        case_id = str(case["case_id"])
        assessment = assess(_scenario(payload, f"{experiment_key}-{case_id}"))
        cases.append(
            ExperimentCaseResult(
                case_id=case_id,
                label=str(case["label"]),
                changed_variables=dict(case["changes"]),
                assessment=assessment,
            )
        )
        deltas[case_id] = {
            "risk_exposure_score": round(
                assessment.risk_exposure_score - baseline.risk_exposure_score, 2
            ),
            "reserve_amount": round(assessment.reserve.amount - baseline.reserve.amount, 2),
            "gross_stressed_exposure": round(
                assessment.reserve.gross_stressed_exposure
                - baseline.reserve.gross_stressed_exposure,
                2,
            ),
            "control_adjusted_platform_contribution": round(
                assessment.dollar_commercial_view.control_adjusted_platform_contribution
                - baseline.dollar_commercial_view.control_adjusted_platform_contribution,
                2,
            ),
        }
    directional_passed = _directional_check(experiment_key, cases)
    return ExperimentResult(
        manifest=_manifest(item),
        baseline=baseline,
        cases=cases,
        observed_deltas=deltas,
        directional_check_passed=directional_passed,
        interpretation=[
            "Observed differences are produced by controlled synthetic inputs.",
            "A passed directional check validates internal behavior, not empirical accuracy.",
        ],
    )


def _directional_check(key: str, cases: list[ExperimentCaseResult]) -> bool:
    by_id = {item.case_id: item.assessment for item in cases}
    if key == "SD-X1-OBLIGATION":
        return (
            by_id["HIGH_OBLIGATION"].reserve.gross_stressed_exposure
            > by_id["LOW_OBLIGATION"].reserve.gross_stressed_exposure
            and by_id["HIGH_OBLIGATION"].reserve.amount
            > by_id["LOW_OBLIGATION"].reserve.amount
        )
    if key == "SD-X2-CREDENTIAL":
        return (
            by_id["HIGH_ABUSE"].risk_exposure_score > by_id["LOW_ABUSE"].risk_exposure_score
            and "account_and_key_security_review" in by_id["HIGH_ABUSE"].recommended_controls
        )
    if key == "SD-X3-CONDUCT":
        return (
            by_id["WEAK_EVIDENCE"].risk_exposure_score
            > by_id["STRONG_EVIDENCE"].risk_exposure_score
            and "usage_meter_reconciliation" in by_id["WEAK_EVIDENCE"].recommended_controls
        )
    if key == "SD-X4-INTERACTION":
        combined = by_id["COMBINED"]
        return (
            combined.risk_exposure_score > by_id["ACCOUNT_ONLY"].risk_exposure_score
            and combined.risk_exposure_score > by_id["EVIDENCE_ONLY"].risk_exposure_score
            and len(combined.recommended_controls)
            > max(
                len(by_id["ACCOUNT_ONLY"].recommended_controls),
                len(by_id["EVIDENCE_ONLY"].recommended_controls),
            )
        )
    return False
