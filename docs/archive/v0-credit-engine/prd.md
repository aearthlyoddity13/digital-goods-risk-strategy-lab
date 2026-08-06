# Product Requirements Document — Merchant Credit & Reserve Decision Engine

**Owner:** Charlene Yang  
**Status:** Planning baseline / MVP in progress  
**Version:** 0.1.0  
**Public-data boundary:** Synthetic data only

## 1. Problem

Emerging digital-product merchants (games, short-form entertainment, web fiction, AI apps, subscriptions, virtual items) present risk profiles poorly served by physical e-commerce underwriting: instant delivery, intangible goods, rapid scaling, cross-border exposure, refund abuse, and thin operating history. Weak decisions create direct losses, revenue leakage, manual-review cost, and network consequences.

## 2. Users

| Persona | Job |
|---------|-----|
| Merchant-risk strategy analyst / underwriter | Decide approve / controls / review / decline and set reserves with explainable drivers |
| Risk / product leadership | Understand approval–loss–friction trade-offs and policy alternatives |
| Portfolio reviewer / recruiter | Evaluate methodology, governance, and engineering quality |

## 3. Decision unit and windows

| Concept | Definition |
|---------|------------|
| Decision unit | One merchant at onboarding or scheduled/triggered periodic review |
| Observation window | Signals known at decision timestamp; no future information |
| Performance window | Loss and merchant outcomes over the following 90–180 days |
| Actions | `APPROVE`, `APPROVE_WITH_CONTROLS`, `MANUAL_REVIEW`, `DECLINE` |

## 4. Goals

- Explainable, API-first decisions with expected-loss economics and reserve recommendations.
- Visible trade-off: approval vs loss vs friction.
- North-star: `risk-adjusted contribution = approved payment revenue − fraud losses − chargeback/refund losses − manual-review cost − reserve-friction cost`.
- Corporate delivery artifacts (PRD, ADRs, model card, validation, runbook) alongside software.

## 5. Non-goals (MVP)

- Live production underwriting or real customer/merchant data  
- Transaction authorization in production  
- AML / content / formal regulatory compliance engines  
- Autonomous adverse action without human-readable reasons  
- Claims of real-world predictive effectiveness before Phase 2 validation  

## 6. Jobs to be done

1. Identify the few drivers that materially change merchant risk.  
2. Connect reserve amounts to exposure and policy, not unexplained percentages.  
3. Quantify approval, loss, reserve, review-capacity, and revenue consequences of threshold changes.  
4. Reproduce recommendations from documented inputs, model version, and policy version.

## 7. Functional requirements

1. Validate inputs (types, ranges, timestamps, leakage boundaries).  
2. Compute transparent scorecard score and reason codes.  
3. Map score → calibrated PD (replaceable component).  
4. Estimate EAD, LGD, expected loss.  
5. Apply hard policy rules separately from scoring.  
6. Recommend rolling reserve rate and amount with floors/caps.  
7. Return full decision payload via versioned API.  
8. Provide deterministic synthetic samples for all four actions.  
9. Expose health, model-card, and schema endpoints (schema/model-card may stub in early slice).  

## 8. Non-functional requirements

Explainability, reproducibility (seeds, versions), reliability (validation, health, tests), security (no secrets, env config), accessibility (WCAG AA target), governance (versions, changelog, limitations).

## 9. Metrics (illustrative until validated)

Risk, growth, CX, operations, and model-quality metrics per brief §5. Success criterion: increase legitimate approval/TPV while holding loss rates within policy and review capacity.

## 10. Acceptance criteria (MVP)

- [ ] Every decision and reserve is reproducible from input + model/policy versions.  
- [ ] API validates inputs and returns stable schemas with structured errors.  
- [ ] No future outcome fields used as decision inputs.  
- [ ] Public examples are synthetic and labeled as such.  
- [ ] Frontend uses env-configured API base URL and includes degraded/static fallback path.  
- [ ] Core flows covered by unit and contract tests in this slice; broader layers in later phases.  
- [ ] Documentation set current with code.

## 11. Risks

See [risk_register.md](risk_register.md). Primary: synthetic-data overclaim; leakage; policy/model conflation; portfolio API availability.
