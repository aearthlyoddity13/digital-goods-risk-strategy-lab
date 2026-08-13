"""API contract tests."""

from __future__ import annotations

import json
from pathlib import Path

from fastapi.testclient import TestClient

from api.main import app

ROOT = Path(__file__).resolve().parents[2]
SAMPLES = json.loads((ROOT / "data" / "sample" / "merchants.json").read_text())

client = TestClient(app)


def test_health_contract() -> None:
    r = client.get("/health")
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ok"
    assert body["api_version"] == "v1"
    assert body["model_version"] == "strategy-0.5.0"
    assert body["policy_version"] == "balanced-growth-0.2.0"
    assert "X-Request-ID" in r.headers


def test_root_discovers_public_api_without_exposing_internal_state() -> None:
    r = client.get("/")
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ok"
    assert body["health"] == "/health"
    assert body["documentation"] == "/docs"
    assert "synthetic" in body["data_boundary"].lower()


def test_decision_contract_approve_sample() -> None:
    payload = {k: v for k, v in SAMPLES[0].items() if not k.startswith("_")}
    r = client.post("/v1/merchants/decision", json=payload)
    assert r.status_code == 200
    body = r.json()
    required = {
        "merchant_id",
        "action",
        "risk_score",
        "probability_of_adverse_outcome",
        "loss_given_default",
        "exposure_at_default",
        "expected_loss",
        "reserve_rate",
        "reserve_amount",
        "reason_codes",
        "hard_policy_flags",
        "model_version",
        "policy_version",
        "assumptions",
        "requires_human_review",
        "request_id",
    }
    assert required.issubset(body.keys())
    assert body["action"] == "APPROVE"
    assert body["request_id"] == r.headers["X-Request-ID"]


def test_decision_validation_error_shape() -> None:
    r = client.post("/v1/merchants/decision", json={"merchant_id": ""})
    assert r.status_code == 422
    body = r.json()
    assert body["error_code"] == "VALIDATION_ERROR"
    assert "request_id" in body
    assert isinstance(body["details"], list)
