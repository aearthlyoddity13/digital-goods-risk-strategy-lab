"""Counterfactual and sensitivity diagnostics for synthetic strategy decisions."""

from __future__ import annotations

from merchant_risk.domain.models import DecisionAction
from merchant_risk.strategy.assessment import assess
from merchant_risk.strategy.models import (
    CounterfactualChange,
    DecisionDiagnostics,
    SensitivityCase,
    StrategyAssessmentInput,
)

DECISION_RANK = {
    DecisionAction.APPROVE: 0,
    DecisionAction.APPROVE_WITH_CONTROLS: 1,
    DecisionAction.MANUAL_REVIEW: 2,
    DecisionAction.DECLINE: 3,
}


def _next_less_restrictive(decision: DecisionAction) -> DecisionAction | None:
    return {
        DecisionAction.DECLINE: DecisionAction.MANUAL_REVIEW,
        DecisionAction.MANUAL_REVIEW: DecisionAction.APPROVE_WITH_CONTROLS,
        DecisionAction.APPROVE_WITH_CONTROLS: DecisionAction.APPROVE,
        DecisionAction.APPROVE: None,
    }[decision]


def _binding_constraints(merchant: StrategyAssessmentInput) -> list[str]:
    result = assess(merchant)
    constraints = list(result.hard_policy_flags)
    review_codes = {
        "LOW_CONFIDENCE_AT_MATERIAL_EXPOSURE",
        "COMBINED_INTEGRITY_AND_COMPLAINT_DETERIORATION",
        "CONCENTRATED_FRAUD_AND_DISPUTE_EVENT",
        "INTEGRITY_EVENT_WITH_MATERIAL_OBLIGATION_GAP",
        "CONCENTRATED_ACCOUNT_OR_KEY_ABUSE",
        "USAGE_METER_AND_COMPLAINT_DIVERGENCE",
    }
    constraints.extend(
        driver.code for driver in result.primary_risk_drivers if driver.code in review_codes
    )
    if not constraints:
        if result.risk_exposure_score >= 55:
            constraints.append("RISK_SCORE_AT_OR_ABOVE_MANUAL_REVIEW_THRESHOLD")
        elif result.risk_exposure_score >= 30:
            constraints.append("RISK_SCORE_AT_OR_ABOVE_CONTROL_THRESHOLD")
        elif result.recommended_controls != ["standard_monitoring"]:
            constraints.append("NON_STANDARD_CONTROL_REQUIREMENT")
    return list(dict.fromkeys(constraints))


def _candidate_values(merchant: StrategyAssessmentInput) -> dict[str, list[float | str]]:
    return {
        "dispute_rate": [0.012, 0.0099, 0.0079, 0.005],
        "fraud_loss_rate": [0.0079, 0.0049, 0.002],
        "complaint_rate": [0.0099, 0.0079, 0.0049, 0.002],
        "content_integrity_indicator": [0.59, 0.49, 0.44, 0.25],
        "prepaid_exposure_ratio": [0.29, 0.24, 0.139, 0.08],
        "account_or_key_compromise_indicator": [0.64, 0.44, 0.20],
        "anomalous_usage_share": [0.119, 0.099, 0.04],
        "usage_meter_reconciliation_rate": [0.90, 0.97, 0.99],
        "renewal_disclosure_score": [0.75, 0.85, 0.95],
        "renewal_dispute_share": [0.39, 0.29, 0.15],
        "data_confidence_level": ["medium", "high"],
    }


def _is_improvement(variable: str, current: float | str, candidate: float | str) -> bool:
    if isinstance(current, str) or isinstance(candidate, str):
        order = {"low": 0, "medium": 1, "high": 2}
        return order[str(candidate)] > order[str(current)]
    higher_is_better = variable in {
        "usage_meter_reconciliation_rate",
        "renewal_disclosure_score",
    }
    return candidate > current if higher_is_better else candidate < current


def _counterfactuals(merchant: StrategyAssessmentInput) -> list[CounterfactualChange]:
    baseline = assess(merchant)
    target = _next_less_restrictive(baseline.decision)
    if target is None or baseline.hard_policy_flags:
        return []
    candidates: list[CounterfactualChange] = []
    for variable, values in _candidate_values(merchant).items():
        current = getattr(merchant, variable)
        for value in values:
            comparison_value = current.value if hasattr(current, "value") else current
            if not _is_improvement(variable, comparison_value, value):
                continue
            updates: dict[str, object] = {variable: value}
            if variable == "prepaid_exposure_ratio":
                obligation = merchant.monthly_attempted_payment_volume * float(value)
                updates["outstanding_customer_obligation"] = obligation
                if merchant.merchant_category.value == "short_drama":
                    updates["unused_purchased_coin_value"] = obligation
                    updates["consumed_purchased_coin_value"] = max(
                        0.0,
                        merchant.purchased_coin_value
                        - merchant.refunded_purchased_coin_value
                        - obligation,
                    )
            try:
                changed = StrategyAssessmentInput.model_validate(
                    merchant.model_dump() | updates
                )
            except ValueError:
                continue
            result = assess(changed)
            if DECISION_RANK[result.decision] <= DECISION_RANK[target]:
                numeric_current = current.value if hasattr(current, "value") else current
                absolute_change = (
                    round(abs(float(value) - float(numeric_current)), 6)
                    if not isinstance(value, str)
                    else None
                )
                candidates.append(
                    CounterfactualChange(
                        variable=variable,
                        current_value=numeric_current,
                        threshold_value=value,
                        absolute_change=absolute_change,
                        resulting_decision=result.decision,
                        resulting_risk_score=result.risk_exposure_score,
                        explanation=(
                            f"Changing only {variable} to {value} reaches "
                            f"{result.decision.value} under the synthetic policy."
                        ),
                    )
                )
                break
    return sorted(
        candidates,
        key=lambda item: item.absolute_change if item.absolute_change is not None else 1.0,
    )[:5]


def _scaled_input(merchant: StrategyAssessmentInput, factor: float) -> StrategyAssessmentInput:
    return merchant.model_copy(
        update={
            "fraud_loss_rate": min(1.0, merchant.fraud_loss_rate * factor),
            "dispute_rate": min(1.0, merchant.dispute_rate * factor),
            "refund_rate": min(1.0, merchant.refund_rate * factor),
            "complaint_rate": min(1.0, merchant.complaint_rate * factor),
        }
    )


def _sensitivity(merchant: StrategyAssessmentInput) -> list[SensitivityCase]:
    cases = (("low", 0.75), ("base", 1.0), ("high", 1.25))
    output: list[SensitivityCase] = []
    for label, factor in cases:
        result = assess(_scaled_input(merchant, factor))
        output.append(
            SensitivityCase(
                case=label,
                assumption_changes={
                    "fraud_dispute_refund_complaint_multiplier": factor,
                },
                decision=result.decision,
                risk_score=result.risk_exposure_score,
                reserve_amount=result.reserve.amount,
                reserve_rate=result.reserve.rate,
                control_adjusted_contribution=(
                    result.dollar_commercial_view.control_adjusted_platform_contribution
                ),
            )
        )
    return output


def diagnose(merchant: StrategyAssessmentInput) -> DecisionDiagnostics:
    baseline = assess(merchant)
    sensitivity = _sensitivity(merchant)
    decisions = {case.decision for case in sensitivity}
    robust = len(decisions) == 1
    return DecisionDiagnostics(
        scenario_id=merchant.scenario_id,
        current_decision=baseline.decision,
        next_less_restrictive_decision=_next_less_restrictive(baseline.decision),
        binding_constraints=_binding_constraints(merchant),
        counterfactual_changes=_counterfactuals(merchant),
        sensitivity_cases=sensitivity,
        robustness="robust_within_tested_range" if robust else "assumption_sensitive",
        robustness_explanation=(
            "The decision is unchanged across the low, base and high synthetic loss cases."
            if robust
            else "The decision changes within the tested synthetic assumption range."
        ),
        limitation=(
            "Counterfactuals vary one field at a time and do not establish causality or "
            "production thresholds."
        ),
    )
