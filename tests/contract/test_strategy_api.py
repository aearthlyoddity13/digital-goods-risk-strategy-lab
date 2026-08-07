"""Contract tests for strategy-lab endpoints."""

from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def _payload() -> dict[str, object]:
    return {
        "merchant_id": "SYN-AI-01",
        "scenario_id": "AI-01-P0",
        "merchant_category": "ai_subscription",
        "merchant_age_months": 30,
        "monthly_attempted_payment_volume": 1_000_000,
        "payment_approval_rate": 0.972,
        "successful_fulfillment_rate": 0.995,
        "average_ticket_size": 28,
        "mom_volume_growth": 0.08,
        "refund_rate": 0.015,
        "dispute_rate": 0.0035,
        "fraud_loss_rate": 0.0012,
        "complaint_rate": 0.002,
        "cross_border_share": 0.18,
        "prepaid_exposure_ratio": 0.10,
        "outstanding_customer_obligation": 100_000,
        "content_integrity_indicator": 0.12,
        "platform_dependency": 0.25,
        "service_reliability": 0.997,
        "support_response_within_sla": 0.95,
        "data_confidence_level": "high",
        "available_merchant_balance": 150_000,
    }


def test_local_cors_preflight_accepts_loopback_hosts_and_arbitrary_dev_ports() -> None:
    for origin in (
        "http://localhost:4173",
        "http://127.0.0.1:8080",
        "http://0.0.0.0:5173",
        "http://[::1]:5173",
    ):
        response = client.options(
            "/api/v1/archetypes",
            headers={
                "Origin": origin,
                "Access-Control-Request-Method": "GET",
            },
        )
        assert response.status_code == 200
        assert response.headers["access-control-allow-origin"] == origin


def test_unlisted_remote_origin_is_not_allowed() -> None:
    response = client.options(
        "/api/v1/archetypes",
        headers={
            "Origin": "https://untrusted.example",
            "Access-Control-Request-Method": "GET",
        },
    )
    assert response.status_code == 400
    assert "access-control-allow-origin" not in response.headers


def test_strategy_assess_contract() -> None:
    response = client.post("/api/v1/assess", json=_payload())
    assert response.status_code == 200
    body = response.json()
    assert body["methodology_version"] == "strategy-0.4.0"
    assert "risk_exposure_score" in body
    assert "merchant_strength_score" in body
    assert "commercial_value_score" in body
    assert body["normalized_commercial_view"]["attempted_volume"] == 100
    assert body["dollar_commercial_view"]["attempted_volume"] == 1_000_000


def test_methodology_contract() -> None:
    response = client.get("/api/v1/methodology")
    assert response.status_code == 200
    body = response.json()
    assert body["posture"] == "balanced_growth"
    assert body["payment_scope"] == "direct_web_payments"


def test_archetypes_contract() -> None:
    response = client.get("/api/v1/archetypes")
    assert response.status_code == 200
    body = response.json()
    assert body["catalog_version"] == "scenarios-0.1.0"
    assert len(body["items"]) == 8


def test_compare_contract() -> None:
    response = client.post(
        "/api/v1/compare",
        json={
            "baseline": {"scenario_key": "SD-03", "period": "P0_BASELINE"},
            "candidate": {"scenario_key": "SD-03", "period": "P2_STRESS"},
        },
    )
    assert response.status_code == 200
    body = response.json()
    assert body["score_deltas"]["risk_exposure_score"] > 0
    assert body["baseline"]["scenario_id"] == "SD-03-P0_BASELINE"
    assert body["candidate"]["scenario_id"] == "SD-03-P2_STRESS"


def test_compare_unknown_scenario_returns_404() -> None:
    response = client.post(
        "/api/v1/compare",
        json={
            "baseline": {"scenario_key": "UNKNOWN", "period": "P0_BASELINE"},
            "candidate": {"scenario_key": "SD-03", "period": "P2_STRESS"},
        },
    )
    assert response.status_code == 404


def test_compare_postures_contract() -> None:
    response = client.post(
        "/api/v1/compare-postures",
        json={"scenario_key": "SD-02", "period": "P2_STRESS"},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["assumption_version"] == "postures-0.2.0"
    assert {item["posture"] for item in body["postures"]} == {
        "permissive",
        "balanced_growth",
        "conservative",
    }
