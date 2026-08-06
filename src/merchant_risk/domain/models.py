"""Domain types and enums."""

from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, field_validator


class IndustrySubtype(str, Enum):
    GAME_PUBLISHER = "game_publisher"
    SHORT_FORM_ENTERTAINMENT = "short_form_entertainment"
    WEB_FICTION = "web_fiction"
    AI_APPLICATION = "ai_application"
    SUBSCRIPTION_PRODUCT = "subscription_product"
    VIRTUAL_ITEMS = "virtual_items"
    OTHER_DIGITAL = "other_digital"


class GeographyTier(str, Enum):
    TIER_1 = "tier_1"
    TIER_2 = "tier_2"
    TIER_3 = "tier_3"
    CROSS_BORDER_HEAVY = "cross_border_heavy"


class VerificationStatus(str, Enum):
    UNVERIFIED = "unverified"
    PARTIAL = "partial"
    VERIFIED = "verified"


class DecisionAction(str, Enum):
    APPROVE = "APPROVE"
    APPROVE_WITH_CONTROLS = "APPROVE_WITH_CONTROLS"
    MANUAL_REVIEW = "MANUAL_REVIEW"
    DECLINE = "DECLINE"


class MerchantFeatures(BaseModel):
    """Decision-time inputs only — no outcome fields."""

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

    @field_validator("merchant_id")
    @classmethod
    def strip_id(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("merchant_id must be non-empty")
        return v


class ReasonCode(BaseModel):
    code: str
    label: str
    contribution: float = Field(
        description="Approximate points contributed to the 0–100 risk score"
    )


class OverrideRecord(BaseModel):
    """Structure for auditable human overrides (persistence later)."""

    original_action: DecisionAction
    override_action: DecisionAction
    rationale: str = Field(min_length=1, max_length=2000)
    reviewer_id: str = Field(min_length=1, max_length=128)
    overridden_at: datetime


class DecisionResult(BaseModel):
    merchant_id: str
    action: DecisionAction
    risk_score: float = Field(ge=0, le=100)
    probability_of_adverse_outcome: float = Field(ge=0, le=1)
    loss_given_default: float = Field(ge=0, le=1)
    exposure_at_default: float = Field(ge=0)
    expected_loss: float = Field(ge=0)
    reserve_rate: float = Field(ge=0, le=1)
    reserve_amount: float = Field(ge=0)
    reason_codes: list[ReasonCode]
    hard_policy_flags: list[str]
    model_version: str
    policy_version: str
    assumptions: list[str]
    requires_human_review: bool
    component_scores: dict[str, float] | None = None
