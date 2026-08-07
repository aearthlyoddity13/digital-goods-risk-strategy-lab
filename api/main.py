"""FastAPI application entrypoint."""

from __future__ import annotations

import logging
import sys
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# Ensure project root and src are importable when launched as `uvicorn api.main:app`
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
for p in (str(ROOT), str(SRC)):
    if p not in sys.path:
        sys.path.insert(0, p)

from api.middleware.request_id import RequestIdMiddleware  # noqa: E402
from api.routes import health, merchants, strategy  # noqa: E402
from api.schemas.decision import ErrorResponse  # noqa: E402
from api.settings import get_settings  # noqa: E402

settings = get_settings()

logging.basicConfig(
    level=getattr(logging, settings.log_level.upper(), logging.INFO),
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)

app = FastAPI(
    title="Digital Goods Merchant Risk Strategy Lab",
    version="0.3.0",
    description=(
        "Employer-neutral, explainable strategy demonstrator for direct-web digital-goods "
        "merchants. Aggregated synthetic data only; not for production merchant decisions."
    ),
)

app.add_middleware(RequestIdMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_origin_regex=settings.cors_origin_regex,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["X-Request-ID"],
)

app.include_router(health.router)
app.include_router(merchants.router)
app.include_router(strategy.router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    request_id = getattr(request.state, "request_id", "unknown")
    details = []
    for err in exc.errors():
        details.append(
            {
                "field": ".".join(str(x) for x in err.get("loc", [])),
                "message": err.get("msg"),
                "type": err.get("type"),
            }
        )
    body = ErrorResponse(
        error_code="VALIDATION_ERROR",
        message="Request validation failed",
        request_id=request_id,
        details=details,
    )
    return JSONResponse(status_code=422, content=body.model_dump())


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    request_id = getattr(request.state, "request_id", "unknown")
    logging.getLogger("merchant_risk.api").exception(
        "unhandled_error", extra={"request_id": request_id}
    )
    body = ErrorResponse(
        error_code="INTERNAL_ERROR",
        message="An unexpected error occurred",
        request_id=request_id,
        details=None,
    )
    return JSONResponse(status_code=500, content=body.model_dump())
