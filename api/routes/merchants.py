"""Merchant decision routes."""

from __future__ import annotations

import logging

from fastapi import APIRouter, Request

from api.schemas.decision import MerchantDecisionRequest, MerchantDecisionResponse
from merchant_risk.domain.engine import decide
from merchant_risk.domain.models import MerchantFeatures

router = APIRouter(prefix="/v1/merchants", tags=["merchants"])
logger = logging.getLogger("merchant_risk.api")


@router.post("/decision", response_model=MerchantDecisionResponse)
def create_decision(
    body: MerchantDecisionRequest, request: Request
) -> MerchantDecisionResponse:
    request_id = getattr(request.state, "request_id", "unknown")
    features = MerchantFeatures.model_validate(body.model_dump())
    result = decide(features)
    logger.info(
        "decision_created",
        extra={
            "request_id": request_id,
            "merchant_id": result.merchant_id,
            "action": result.action.value,
            "model_version": result.model_version,
            "policy_version": result.policy_version,
        },
    )
    return MerchantDecisionResponse(
        **result.model_dump(),
        request_id=request_id,
    )
