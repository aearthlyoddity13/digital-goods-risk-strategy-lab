"""Exposure at default and loss given default."""

from __future__ import annotations

from merchant_risk.domain.config import get_model_config
from merchant_risk.domain.models import MerchantFeatures


def estimate_ead(m: MerchantFeatures) -> float:
    cfg = get_model_config()["exposure"]
    base_days = float(cfg["default_exposure_days"])
    rw = float(cfg["refund_window_weight"])
    # Blend default exposure days with refund window
    days = base_days * (1.0 - rw) + float(m.refund_window_days) * rw
    days = max(7.0, min(90.0, days))
    return max(0.0, m.projected_monthly_tpv * (days / 30.0))


def estimate_lgd(m: MerchantFeatures) -> float:
    base = float(get_model_config()["lgd_base"][m.industry_subtype.value])
    # Adjust for product structure and resilience
    adj = 0.0
    if m.virtual_asset_transferability:
        adj += 0.08
    if m.instant_delivery_share > 0.7:
        adj += 0.05
    if m.cash_buffer_months < 1.0:
        adj += 0.07
    if m.negative_balance_flag:
        adj += 0.10
    if m.subscription_share > 0.5:
        adj -= 0.05
    return max(0.05, min(0.95, base + adj))


def expected_loss(pd: float, lgd: float, ead: float) -> float:
    return max(0.0, pd * lgd * ead)
