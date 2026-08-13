"""Typed contracts for the strategy-lab assessment."""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field, model_validator

from merchant_risk.domain.models import DecisionAction


class MerchantCategory(str, Enum):
    SHORT_DRAMA = "short_drama"
    WEB_FICTION = "web_fiction"
    GAMES = "games"
    AI_SUBSCRIPTION = "ai_subscription"
    AI_API = "ai_api"
    OTHER_DIGITAL = "other_digital"


class DataConfidence(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class StrategyAssessmentInput(BaseModel):
    merchant_id: str = Field(min_length=1, max_length=64)
    scenario_id: str = Field(min_length=1, max_length=64)
    merchant_category: MerchantCategory
    merchant_age_months: int = Field(ge=0, le=600)
    monthly_attempted_payment_volume: float = Field(ge=0)
    payment_approval_rate: float = Field(ge=0, le=1)
    successful_fulfillment_rate: float = Field(ge=0, le=1)
    average_ticket_size: float = Field(gt=0)
    mom_volume_growth: float = Field(ge=-1, le=10)
    refund_rate: float = Field(ge=0, le=1)
    dispute_rate: float = Field(ge=0, le=1)
    fraud_loss_rate: float = Field(ge=0, le=1)
    complaint_rate: float = Field(ge=0, le=1)
    cross_border_share: float = Field(ge=0, le=1)
    prepaid_exposure_ratio: float = Field(ge=0, le=2)
    outstanding_customer_obligation: float = Field(ge=0)
    content_integrity_indicator: float = Field(ge=0, le=1)
    platform_dependency: float = Field(ge=0, le=1)
    service_reliability: float = Field(ge=0, le=1)
    support_response_within_sla: float = Field(ge=0, le=1)
    data_confidence_level: DataConfidence
    virtual_asset_transferability: bool = False
    purchased_coin_value: float = Field(default=0, ge=0)
    consumed_purchased_coin_value: float = Field(default=0, ge=0)
    refunded_purchased_coin_value: float = Field(default=0, ge=0)
    unused_purchased_coin_value: float = Field(default=0, ge=0)
    promotional_coin_value: float = Field(default=0, ge=0)
    purchased_service_credit_value: float = Field(default=0, ge=0)
    consumed_service_credit_value: float = Field(default=0, ge=0)
    refunded_service_credit_value: float = Field(default=0, ge=0)
    unused_service_credit_value: float = Field(default=0, ge=0)
    promotional_service_credit_value: float = Field(default=0, ge=0)
    post_consumption_dispute_share: float = Field(default=0, ge=0, le=1)
    renewal_dispute_share: float = Field(default=0, ge=0, le=1)
    renewal_disclosure_score: float = Field(default=1, ge=0, le=1)
    usage_meter_reconciliation_rate: float = Field(default=1, ge=0, le=1)
    anomalous_usage_share: float = Field(default=0, ge=0, le=1)
    account_or_key_compromise_indicator: float = Field(default=0, ge=0, le=1)
    postpaid_usage_exposure_ratio: float = Field(default=0, ge=0, le=2)
    available_merchant_balance: float = Field(default=0, ge=0)
    current_reserve_rate: float = Field(default=0, ge=0, le=1)
    current_holding_days: int = Field(default=0, ge=0, le=180)
    prohibited_activity_confirmed: bool = False
    sanctions_prohibition_confirmed: bool = False
    deliberate_transaction_laundering_confirmed: bool = False
    merchant_identity_resolved: bool = True

    @model_validator(mode="after")
    def validate_coin_ledger(self) -> StrategyAssessmentInput:
        calculated = max(
            0.0,
            self.purchased_coin_value
            - self.consumed_purchased_coin_value
            - self.refunded_purchased_coin_value,
        )
        if abs(calculated - self.unused_purchased_coin_value) > 0.01:
            raise ValueError(
                "unused_purchased_coin_value must equal purchased minus consumed minus refunded"
            )
        calculated_credits = max(
            0.0,
            self.purchased_service_credit_value
            - self.consumed_service_credit_value
            - self.refunded_service_credit_value,
        )
        if abs(calculated_credits - self.unused_service_credit_value) > 0.01:
            raise ValueError(
                "unused_service_credit_value must equal purchased minus consumed minus refunded"
            )
        return self


class Driver(BaseModel):
    code: str
    label: str
    value: float | str | None = None


class HorizonExposure(BaseModel):
    horizon_days: int = Field(ge=0, le=180)
    expected_payment_loss: float = Field(ge=0)
    stressed_payment_loss: float = Field(ge=0)
    contingent_obligation_exposure: float = Field(ge=0)
    postpaid_usage_exposure: float = Field(ge=0)
    gross_stressed_exposure: float = Field(ge=0)
    coverage_target: float = Field(ge=0, le=1)
    target_protection: float = Field(ge=0)
    available_merchant_balance: float = Field(ge=0)
    existing_reserve: float = Field(ge=0)
    incremental_protection_gap: float = Field(ge=0)
    implied_reserve_rate: float = Field(ge=0, le=1)


class ReserveRecommendation(BaseModel):
    rate: float = Field(ge=0, le=1)
    amount: float = Field(ge=0)
    holding_days: int = Field(ge=0, le=180)
    rationale: list[str]
    coverage_target: float = Field(default=0.95, ge=0, le=1)
    gross_stressed_exposure: float = Field(default=0, ge=0)
    available_protection: float = Field(default=0, ge=0)
    incremental_protection_gap: float = Field(default=0, ge=0)
    capped_by_policy: bool = False
    horizon_analysis: list[HorizonExposure] = Field(default_factory=list)


class CommercialView(BaseModel):
    scale_label: str
    attempted_volume: float
    approved_volume: float
    sustainable_payment_volume: float
    gross_platform_revenue: float
    expected_fraud_loss: float
    expected_dispute_principal_loss: float
    expected_dispute_operating_cost: float
    expected_uncovered_exposure: float
    monitoring_and_review_cost: float
    false_positive_opportunity_cost: float
    control_adjusted_platform_contribution: float
    reserved_funds: float
    merchant_liquidity_burden: float


class StrategyAssessmentResult(BaseModel):
    merchant_id: str
    scenario_id: str
    decision: DecisionAction
    risk_level: str
    risk_exposure_score: float = Field(ge=0, le=100)
    merchant_strength_score: float = Field(ge=0, le=100)
    commercial_value_score: float = Field(ge=0, le=100)
    component_scores: dict[str, float]
    primary_risk_drivers: list[Driver]
    protective_factors: list[str]
    recommended_controls: list[str]
    reserve: ReserveRecommendation
    normalized_commercial_view: CommercialView
    dollar_commercial_view: CommercialView
    conditions_to_reduce_controls: list[str]
    escalation_triggers: list[str]
    hard_policy_flags: list[str]
    confidence: DataConfidence
    methodology_version: str
    policy_version: str
    synthetic_data_disclaimer: str
    limitations: list[str]


class ScenarioReference(BaseModel):
    scenario_key: str = Field(min_length=1, max_length=64)
    period: str = Field(min_length=1, max_length=64)


class CompareRequest(BaseModel):
    baseline: ScenarioReference
    candidate: ScenarioReference


class CompareResult(BaseModel):
    baseline: StrategyAssessmentResult
    candidate: StrategyAssessmentResult
    score_deltas: dict[str, float]
    decision_changed: bool
    delta_explanation: list[str]


class ExperimentCase(BaseModel):
    case_id: str
    label: str
    changed_variables: dict[str, float | int | bool | str]


class ExperimentManifest(BaseModel):
    experiment_key: str
    name: str
    mechanism: str
    hypothesis: str
    variables_held_constant: list[str]
    expected_direction: list[str]
    alternative_explanation: str
    falsification_check: str
    cases: list[ExperimentCase]


class ExperimentCaseResult(BaseModel):
    case_id: str
    label: str
    changed_variables: dict[str, float | int | bool | str]
    assessment: StrategyAssessmentResult


class ExperimentResult(BaseModel):
    manifest: ExperimentManifest
    baseline: StrategyAssessmentResult
    cases: list[ExperimentCaseResult]
    observed_deltas: dict[str, dict[str, float]]
    directional_check_passed: bool
    interpretation: list[str]


class CounterfactualChange(BaseModel):
    variable: str
    current_value: float | int | str | bool
    threshold_value: float | int | str | bool
    absolute_change: float | None = None
    resulting_decision: DecisionAction
    resulting_risk_score: float = Field(ge=0, le=100)
    explanation: str


class SensitivityCase(BaseModel):
    case: str
    assumption_changes: dict[str, float]
    decision: DecisionAction
    risk_score: float = Field(ge=0, le=100)
    reserve_amount: float = Field(ge=0)
    reserve_rate: float = Field(ge=0, le=1)
    control_adjusted_contribution: float


class DecisionDiagnostics(BaseModel):
    scenario_id: str
    current_decision: DecisionAction
    next_less_restrictive_decision: DecisionAction | None
    binding_constraints: list[str]
    counterfactual_changes: list[CounterfactualChange]
    sensitivity_cases: list[SensitivityCase]
    robustness: str
    robustness_explanation: str
    limitation: str


class PolicyPosture(str, Enum):
    PERMISSIVE = "permissive"
    BALANCED_GROWTH = "balanced_growth"
    CONSERVATIVE = "conservative"


class AppliedControl(BaseModel):
    code: str
    label: str
    mechanism: str
    applicability_basis: str
    assumed_effects: dict[str, float]
    monthly_cost: float = Field(ge=0)
    friction_level: str
    release_condition: str


class PostureSimulationResult(BaseModel):
    posture: PolicyPosture
    label: str
    description: str
    effective_approval_rate: float = Field(ge=0, le=1)
    effective_refund_rate: float = Field(ge=0, le=1)
    effective_dispute_rate: float = Field(ge=0, le=1)
    effective_fraud_loss_rate: float = Field(ge=0, le=1)
    residual_risk_score: float = Field(ge=0, le=100)
    reserve_rate: float = Field(ge=0, le=1)
    holding_days: int = Field(ge=0, le=180)
    normalized_view: CommercialView
    dollar_view: CommercialView
    within_risk_appetite: bool
    assumption_version: str
    applied_controls: list[AppliedControl] = Field(default_factory=list)
    mechanism_coverage: list[str] = Field(default_factory=list)
    total_monthly_control_cost: float = Field(default=0, ge=0)


class PostureComparisonResult(BaseModel):
    scenario_id: str
    baseline_assessment: StrategyAssessmentResult
    postures: list[PostureSimulationResult]
    recommended_posture: PolicyPosture | None
    recommendation_rationale: list[str]
    assumption_version: str
