"""Unit tests for baseline decision engine."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from merchant_risk.domain.engine import decide
from merchant_risk.domain.models import DecisionAction, MerchantFeatures
from merchant_risk.scoring.calibration import score_to_pd

ROOT = Path(__file__).resolve().parents[2]
SAMPLES = json.loads((ROOT / "data" / "sample" / "merchants.json").read_text())


def _features(raw: dict) -> MerchantFeatures:
    payload = {k: v for k, v in raw.items() if not k.startswith("_")}
    return MerchantFeatures.model_validate(payload)


@pytest.mark.parametrize(
    "merchant_id,expected",
    [
        ("SYN-APPROVE-001", DecisionAction.APPROVE),
        ("SYN-CONTROLS-001", DecisionAction.APPROVE_WITH_CONTROLS),
        ("SYN-REVIEW-001", DecisionAction.MANUAL_REVIEW),
        ("SYN-DECLINE-001", DecisionAction.DECLINE),
    ],
)
def test_sample_merchants_map_to_intended_actions(
    merchant_id: str, expected: DecisionAction
) -> None:
    raw = next(m for m in SAMPLES if m["merchant_id"] == merchant_id)
    result = decide(_features(raw))
    assert result.action == expected
    assert result.model_version == "scorecard-0.1.0"
    assert result.policy_version == "policy-0.1.0"
    assert 0 <= result.risk_score <= 100
    assert 0 <= result.probability_of_adverse_outcome <= 1
    assert result.expected_loss >= 0
    assert result.reason_codes or expected == DecisionAction.APPROVE


def test_pd_bounds_and_monotonicity() -> None:
    low = score_to_pd(10)
    high = score_to_pd(90)
    assert 0 <= low < high <= 1


def test_hard_decline_on_chargeback() -> None:
    raw = next(m for m in SAMPLES if m["merchant_id"] == "SYN-APPROVE-001").copy()
    raw["chargeback_rate"] = 0.06
    result = decide(_features(raw))
    assert result.action == DecisionAction.DECLINE
    assert "HARD_DECLINE_CHARGEBACK_RATE" in result.hard_policy_flags


def test_reserve_capped() -> None:
    raw = next(m for m in SAMPLES if m["merchant_id"] == "SYN-CONTROLS-001")
    result = decide(_features(raw))
    assert result.reserve_rate <= 0.25
    if result.action == DecisionAction.APPROVE_WITH_CONTROLS:
        assert result.reserve_rate >= 0.05


def test_response_includes_assumptions() -> None:
    raw = next(m for m in SAMPLES if m["merchant_id"] == "SYN-APPROVE-001")
    result = decide(_features(raw))
    assert any("illustrative" in a.lower() or "synthetic" in a.lower() for a in result.assumptions)
