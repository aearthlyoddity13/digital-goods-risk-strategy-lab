"""Versioned scenario-catalog loader."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

from merchant_risk.strategy.models import StrategyAssessmentInput

ROOT = Path(__file__).resolve().parents[3]
CATALOG_PATH = ROOT / "data" / "scenarios" / "scenarios-0.1.0.yaml"


@lru_cache(maxsize=1)
def load_catalog() -> dict[str, Any]:
    with CATALOG_PATH.open(encoding="utf-8") as source:
        catalog = yaml.safe_load(source)
    if not isinstance(catalog, dict) or not isinstance(catalog.get("scenarios"), list):
        raise ValueError("Scenario catalog must contain a scenarios list")
    return catalog


def list_scenarios() -> list[dict[str, object]]:
    catalog = load_catalog()
    return [
        {
            "scenario_key": item["scenario_key"],
            "merchant_id": item["merchant_id"],
            "name": item["name"],
            "merchant_category": item["merchant_category"],
            "periods": list(item["periods"].keys()),
        }
        for item in catalog["scenarios"]
    ]


def get_scenario(scenario_key: str, period: str) -> StrategyAssessmentInput:
    catalog = load_catalog()
    item = next(
        (row for row in catalog["scenarios"] if row["scenario_key"] == scenario_key),
        None,
    )
    if item is None:
        raise KeyError(f"Unknown scenario: {scenario_key}")
    if period not in item["periods"]:
        raise KeyError(f"Unknown period for {scenario_key}: {period}")
    payload = dict(catalog.get("defaults", {}))
    payload.update(item.get("base", {}))
    payload.update(item["periods"][period])
    payload.update(
        {
            "merchant_id": item["merchant_id"],
            "scenario_id": f"{scenario_key}-{period}",
            "merchant_category": item["merchant_category"],
            "merchant_age_months": item["merchant_age_months"],
        }
    )
    attempted = float(payload["monthly_attempted_payment_volume"])
    obligation = attempted * float(payload["prepaid_exposure_ratio"])
    payload["outstanding_customer_obligation"] = round(obligation, 2)
    if item["merchant_category"] == "short_drama":
        purchased = attempted * 0.45
        refunded = attempted * float(payload["refund_rate"]) * 0.5
        consumed = max(0.0, purchased - obligation - refunded)
        payload.update(
            {
                "purchased_coin_value": round(purchased, 2),
                "consumed_purchased_coin_value": round(consumed, 2),
                "refunded_purchased_coin_value": round(refunded, 2),
                "unused_purchased_coin_value": round(purchased - consumed - refunded, 2),
                "promotional_coin_value": round(attempted * 0.02, 2),
            }
        )
    if item["merchant_category"] == "ai_subscription":
        purchased_credits = attempted * 0.25
        refunded_credits = attempted * float(payload["refund_rate"]) * 0.25
        consumed_credits = max(0.0, purchased_credits - obligation - refunded_credits)
        payload.update(
            {
                "purchased_service_credit_value": round(purchased_credits, 2),
                "consumed_service_credit_value": round(consumed_credits, 2),
                "refunded_service_credit_value": round(refunded_credits, 2),
                "unused_service_credit_value": round(
                    purchased_credits - consumed_credits - refunded_credits, 2
                ),
                "promotional_service_credit_value": round(attempted * 0.015, 2),
            }
        )
    return StrategyAssessmentInput.model_validate(payload)
