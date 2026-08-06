"""Transparent component scorecard."""

from __future__ import annotations

from merchant_risk.domain.config import get_model_config
from merchant_risk.domain.models import (
    GeographyTier,
    MerchantFeatures,
    ReasonCode,
    VerificationStatus,
)


def _clip(x: float, lo: float = 0.0, hi: float = 100.0) -> float:
    return max(lo, min(hi, x))


def score_viability(m: MerchantFeatures) -> tuple[float, list[ReasonCode]]:
    reasons: list[ReasonCode] = []
    tenure_risk = _clip(100 - min(m.tenure_months, 36) * (100 / 36))
    buffer_risk = _clip(100 - min(m.cash_buffer_months, 6) * (100 / 6))
    verify_map = {
        VerificationStatus.VERIFIED: 10.0,
        VerificationStatus.PARTIAL: 45.0,
        VerificationStatus.UNVERIFIED: 85.0,
    }
    verify_risk = verify_map[m.verification_status]
    neg = 80.0 if m.negative_balance_flag else 5.0
    score = 0.35 * tenure_risk + 0.30 * buffer_risk + 0.20 * verify_risk + 0.15 * neg
    if tenure_risk >= 50:
        reasons.append(
            ReasonCode(
                code="LOW_TENURE",
                label="Limited operating tenure",
                contribution=round(0.35 * tenure_risk, 2),
            )
        )
    if buffer_risk >= 50:
        reasons.append(
            ReasonCode(
                code="THIN_CASH_BUFFER",
                label="Thin cash buffer relative to volume",
                contribution=round(0.30 * buffer_risk, 2),
            )
        )
    if m.verification_status != VerificationStatus.VERIFIED:
        reasons.append(
            ReasonCode(
                code="VERIFICATION_GAP",
                label=f"Verification status: {m.verification_status.value}",
                contribution=round(0.20 * verify_risk, 2),
            )
        )
    if m.negative_balance_flag:
        reasons.append(
            ReasonCode(
                code="NEGATIVE_BALANCE",
                label="Historical negative balance flag",
                contribution=round(0.15 * neg, 2),
            )
        )
    return _clip(score), reasons


def score_payment_quality(m: MerchantFeatures) -> tuple[float, list[ReasonCode]]:
    reasons: list[ReasonCode] = []
    # Scale rates into 0–100 with steep penalties near policy hard limits
    cb = _clip(m.chargeback_rate / 0.05 * 100)
    rf = _clip(m.refund_rate / 0.20 * 100)
    fr = _clip(m.fraud_alert_rate / 0.08 * 100)
    un = _clip(m.unauthorized_claim_rate / 0.05 * 100)
    score = 0.35 * cb + 0.25 * rf + 0.25 * fr + 0.15 * un
    if cb >= 40:
        reasons.append(
            ReasonCode(
                code="ELEVATED_CHARGEBACKS",
                label="Elevated chargeback rate",
                contribution=round(0.35 * cb, 2),
            )
        )
    if rf >= 40:
        reasons.append(
            ReasonCode(
                code="ELEVATED_REFUNDS",
                label="Elevated refund rate",
                contribution=round(0.25 * rf, 2),
            )
        )
    if fr >= 40:
        reasons.append(
            ReasonCode(
                code="FRAUD_ALERTS",
                label="Elevated fraud-alert rate",
                contribution=round(0.25 * fr, 2),
            )
        )
    if un >= 40:
        reasons.append(
            ReasonCode(
                code="UNAUTHORIZED_CLAIMS",
                label="Elevated unauthorized-claim rate",
                contribution=round(0.15 * un, 2),
            )
        )
    return _clip(score), reasons


def score_growth(m: MerchantFeatures) -> tuple[float, list[ReasonCode]]:
    reasons: list[ReasonCode] = []
    growth = _clip(max(m.tpv_growth_3m, 0) / 3.0 * 100)
    vol = _clip(m.tpv_volatility / 2.0 * 100)
    score = 0.6 * growth + 0.4 * vol
    if growth >= 50:
        reasons.append(
            ReasonCode(
                code="RAPID_GROWTH",
                label="Rapid TPV growth vs thin history",
                contribution=round(0.6 * growth, 2),
            )
        )
    if vol >= 50:
        reasons.append(
            ReasonCode(
                code="VOLUME_VOLATILITY",
                label="High volume volatility",
                contribution=round(0.4 * vol, 2),
            )
        )
    return _clip(score), reasons


def score_product(m: MerchantFeatures) -> tuple[float, list[ReasonCode]]:
    reasons: list[ReasonCode] = []
    instant = m.instant_delivery_share * 100
    transfer = 70.0 if m.virtual_asset_transferability else 15.0
    # Longer refund windows increase exposure uncertainty
    window = _clip(m.refund_window_days / 90 * 100)
    sub = (1.0 - m.subscription_share) * 40  # more one-off → slightly higher
    score = 0.35 * instant + 0.30 * transfer + 0.20 * window + 0.15 * sub
    if instant >= 60:
        reasons.append(
            ReasonCode(
                code="INSTANT_DELIVERY",
                label="High instant-delivery share",
                contribution=round(0.35 * instant, 2),
            )
        )
    if m.virtual_asset_transferability:
        reasons.append(
            ReasonCode(
                code="TRANSFERABLE_ASSETS",
                label="Transferable virtual assets",
                contribution=round(0.30 * transfer, 2),
            )
        )
    return _clip(score), reasons


def score_behavior(m: MerchantFeatures) -> tuple[float, list[ReasonCode]]:
    reasons: list[ReasonCode] = []
    new_u = m.new_user_share * 100
    low_repeat = (1.0 - m.repeat_purchase_rate) * 100
    device = m.device_concentration * 100
    score = 0.4 * new_u + 0.3 * low_repeat + 0.3 * device
    if new_u >= 60:
        reasons.append(
            ReasonCode(
                code="NEW_USER_CONCENTRATION",
                label="High new-user share",
                contribution=round(0.4 * new_u, 2),
            )
        )
    if device >= 60:
        reasons.append(
            ReasonCode(
                code="DEVICE_CONCENTRATION",
                label="High device concentration",
                contribution=round(0.3 * device, 2),
            )
        )
    return _clip(score), reasons


def score_geography(m: MerchantFeatures) -> tuple[float, list[ReasonCode]]:
    reasons: list[ReasonCode] = []
    tier_map = {
        GeographyTier.TIER_1: 15.0,
        GeographyTier.TIER_2: 35.0,
        GeographyTier.TIER_3: 55.0,
        GeographyTier.CROSS_BORDER_HEAVY: 70.0,
    }
    tier = tier_map[m.geography_tier]
    xb = m.cross_border_share * 100
    score = 0.6 * tier + 0.4 * xb
    if tier >= 50 or xb >= 60:
        reasons.append(
            ReasonCode(
                code="GEO_EXPOSURE",
                label="Elevated geographic / cross-border exposure",
                contribution=round(score * 0.5, 2),
            )
        )
    return _clip(score), reasons


def compute_risk_score(
    m: MerchantFeatures,
) -> tuple[float, dict[str, float], list[ReasonCode]]:
    cfg = get_model_config()
    weights = cfg["weights"]
    components = {
        "viability": score_viability(m),
        "payment_quality": score_payment_quality(m),
        "growth_volatility": score_growth(m),
        "product_structure": score_product(m),
        "behavior": score_behavior(m),
        "geography": score_geography(m),
    }
    scores = {k: v[0] for k, v in components.items()}
    all_reasons: list[ReasonCode] = []
    for k, (s, reasons) in components.items():
        # Scale contribution display by weight for ranking honesty
        for r in reasons:
            all_reasons.append(
                ReasonCode(
                    code=r.code,
                    label=r.label,
                    contribution=round(r.contribution * weights[k], 2),
                )
            )
    total = sum(scores[k] * weights[k] for k in weights)
    all_reasons.sort(key=lambda r: r.contribution, reverse=True)
    return _clip(total), scores, all_reasons[:5]
