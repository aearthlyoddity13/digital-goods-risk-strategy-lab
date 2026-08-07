"""Health route."""

from fastapi import APIRouter

from api.schemas.decision import HealthResponse
from api.settings import get_settings
from merchant_risk.strategy.assessment import METHODOLOGY_VERSION, POLICY_VERSION

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    settings = get_settings()
    return HealthResponse(
        status="ok",
        service=settings.app_name,
        api_version="v1",
        model_version=METHODOLOGY_VERSION,
        policy_version=POLICY_VERSION,
    )
