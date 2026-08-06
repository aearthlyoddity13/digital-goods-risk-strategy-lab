"""API schemas — stable Pydantic contracts."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from merchant_risk.domain.models import (
    DecisionAction,
    GeographyTier,
    IndustrySubtype,
    ReasonCode,
    VerificationStatus,
)


class MerchantDecisionRequest(BaseModel):
    merchant_id: str = Field(min_length=1, max_length=64)
    industry_subtype: IndustrySubtype
    geography_tier: GeographyTier
    tenure_months: int = Field(ge=0, le=600)
    verification_status: VerificationStatus
    avg_monthly_tpv: float = Field(ge=0)
    projected_monthly_tpv: float = Field(ge=0)
    tpv_growth_3m: float = Field(ge=-1, le=10)
    tpv_volatility: float = Field(ge=0, le=5)
    chargeback_rate: float = Field(ge=0, le=1)
    refund_rate: float = Field(ge=0, le=1)
    fraud_alert_rate: float = Field(ge=0, le=1)
    unauthorized_claim_rate: float = Field(ge=0, le=1)
    negative_balance_flag: bool
    instant_delivery_share: float = Field(ge=0, le=1)
    subscription_share: float = Field(ge=0, le=1)
    virtual_asset_transferability: bool
    refund_window_days: int = Field(ge=0, le=365)
    new_user_share: float = Field(ge=0, le=1)
    repeat_purchase_rate: float = Field(ge=0, le=1)
    device_concentration: float = Field(ge=0, le=1)
    cash_buffer_months: float = Field(ge=0, le=36)
    cross_border_share: float = Field(ge=0, le=1)
    decision_timestamp: datetime


class MerchantDecisionResponse(BaseModel):
    merchant_id: str
    action: DecisionAction
    risk_score: float
    probability_of_adverse_outcome: float
    loss_given_default: float
    exposure_at_default: float
    expected_loss: float
    reserve_rate: float
    reserve_amount: float
    reason_codes: list[ReasonCode]
    hard_policy_flags: list[str]
    model_version: str
    policy_version: str
    assumptions: list[str]
    requires_human_review: bool
    component_scores: dict[str, float] | None = None
    request_id: str


class HealthResponse(BaseModel):
    status: str
    service: str
    api_version: str
    model_version: str
    policy_version: str


class ErrorResponse(BaseModel):
    error_code: str
    message: str
    request_id: str
    details: list[dict[str, Any]] | None = None
