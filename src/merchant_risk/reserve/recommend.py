"""Rolling reserve recommendation."""

from __future__ import annotations

from merchant_risk.domain.config import get_policy_config
from merchant_risk.domain.models import DecisionAction, MerchantFeatures


def recommend_reserve(
    m: MerchantFeatures,
    expected_loss: float,
    action: DecisionAction,
) -> tuple[float, float]:
    """Return (reserve_rate, reserve_amount)."""
    cfg = get_policy_config()["reserve"]
    floor_r = float(cfg["floor_rate"])
    cap_r = float(cfg["cap_rate"])
    mult = float(cfg["coverage_multiplier"])
    min_controls = float(cfg["approve_with_controls_min_rate"])
    zero_below = float(cfg["zero_reserve_below_el"])

    if action == DecisionAction.DECLINE:
        return 0.0, 0.0

    tpv = max(m.projected_monthly_tpv, 1.0)
    raw_rate = (expected_loss * mult) / tpv

    if action == DecisionAction.APPROVE:
        if expected_loss < zero_below:
            return 0.0, 0.0
        rate = max(0.0, min(cap_r, raw_rate))
        # Approve path: optional light reserve only if EL material
        if rate < floor_r * 0.5:
            return 0.0, 0.0
        rate = min(cap_r, max(floor_r, rate))
    elif action == DecisionAction.APPROVE_WITH_CONTROLS:
        rate = min(cap_r, max(min_controls, max(floor_r, raw_rate)))
    else:  # MANUAL_REVIEW — still recommend provisional reserve
        rate = min(cap_r, max(floor_r, raw_rate))

    amount = rate * m.projected_monthly_tpv
    return round(rate, 4), round(amount, 2)
