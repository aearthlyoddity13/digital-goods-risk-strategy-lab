"""Decision engine orchestration."""

from __future__ import annotations

from merchant_risk import MODEL_VERSION, POLICY_VERSION
from merchant_risk.domain.config import get_model_config
from merchant_risk.domain.models import DecisionResult, MerchantFeatures
from merchant_risk.exposure.metrics import estimate_ead, estimate_lgd, expected_loss
from merchant_risk.policy.rules import evaluate_hard_flags, select_action
from merchant_risk.reserve.recommend import recommend_reserve
from merchant_risk.scoring.calibration import score_to_pd
from merchant_risk.scoring.scorecard import compute_risk_score


def decide(merchant: MerchantFeatures) -> DecisionResult:
    """Run transparent baseline decision for one merchant."""
    risk_score, components, reasons = compute_risk_score(merchant)
    pd = score_to_pd(risk_score)
    lgd = estimate_lgd(merchant)
    ead = estimate_ead(merchant)
    el = expected_loss(pd, lgd, ead)
    hard_flags = evaluate_hard_flags(merchant)
    action, requires_review = select_action(merchant, risk_score, el, hard_flags)
    reserve_rate, reserve_amount = recommend_reserve(merchant, el, action)

    assumptions = list(get_model_config().get("assumptions", []))
    if merchant.projected_monthly_tpv <= 0:
        assumptions.append("Projected TPV is zero; EAD and reserve amount may be zero.")

    return DecisionResult(
        merchant_id=merchant.merchant_id,
        action=action,
        risk_score=round(risk_score, 2),
        probability_of_adverse_outcome=round(pd, 6),
        loss_given_default=round(lgd, 4),
        exposure_at_default=round(ead, 2),
        expected_loss=round(el, 2),
        reserve_rate=reserve_rate,
        reserve_amount=reserve_amount,
        reason_codes=reasons,
        hard_policy_flags=hard_flags,
        model_version=MODEL_VERSION,
        policy_version=POLICY_VERSION,
        assumptions=assumptions,
        requires_human_review=requires_review,
        component_scores={k: round(v, 2) for k, v in components.items()},
    )
