# Decision policy

**Version:** `policy-strategy-0.2.0` (draft; implemented in Phase 3)  
**Type:** Explainable rules-and-score strategy demonstrator  
**Not:** A statistically validated machine-learning model

**Governing posture:** Balanced growth. See [RISK_APPETITE_AND_OBJECTIVE.md](RISK_APPETITE_AND_OBJECTIVE.md). Commercial value may influence control selection only after non-negotiable legitimacy, legal, sanctions and severe-integrity boundaries are satisfied.

---

## 1. Decisions

| Decision | Meaning |
|----------|---------|
| `APPROVE` | Proceed with standard monitoring |
| `APPROVE_WITH_CONTROLS` | Proceed with one or more protective controls |
| `MANUAL_REVIEW` | Human underwriting / integrity review required before expansion |
| `DECLINE` | Do not approve processing under stated policy posture |

## 2. Control catalog

- `standard_monitoring`  
- `enhanced_monitoring`  
- `settlement_delay`  
- `rolling_reserve`  
- `processing_volume_limit`  
- `geographic_restriction`  
- `content_review`  
- `subscription_practice_review`  
- `proof_of_fulfillment_review`  
- `additional_merchant_information`  
- `manual_underwriting_review`  

## 3. Scoring philosophy

Illustrative score 0–100 (higher = more concern) from weighted components, then **interaction uplifts**:

| Interaction | Intent |
|-------------|--------|
| Low ticket × high frequency | Aggregate exposure may still be large |
| Rapid growth × short tenure / low confidence | Commercial upside with thin evidence |
| Instant consumption × transferability | Recoverability collapse |
| High subscription share × cancel/complaint themes | Delayed dispute exposure |
| High prepaid exposure × low current disputes | Contingent liability still material |
| Content deterioration × platform dependency | Interruption probability rises |
| High refund rate × weak reliability / support proxies | Refunds may migrate to chargebacks |

Component families (illustrative weights to be encoded in YAML): payment quality, growth/volatility, structure (subscription/prepaid/transfer), integrity/content, maturity/confidence, geography/cross-border.

The 0–100 score is a summary aid, not the complete decision. The implementation must also expose separate risk-exposure, merchant-strength and commercial-value assessments. It should select the least-restrictive effective control package consistent with the balanced-growth appetite.

## 4. Hard rules (illustrative)

Examples to encode in config (not production thresholds):

- Extreme dispute or fraud-proxy rates → `DECLINE` or hard `MANUAL_REVIEW`  
- Severe content-risk indicator and/or simulated removal event → escalate regardless of short-term payment calm  
- Very low data confidence on high volume → `MANUAL_REVIEW` + `additional_merchant_information`  
- Negative obligation gap signals (obligation >> reserve capacity proxies) → controls + reserve uplift  

## 5. Mapping score bands to decisions (illustrative)

| Score band | Default posture |
|------------|-----------------|
| 0–29 | `APPROVE` + standard monitoring |
| 30–54 | `APPROVE_WITH_CONTROLS` |
| 55–74 | `MANUAL_REVIEW` |
| 75–100 | `DECLINE` (unless hard rule already decided) |

Hard rules may override band defaults upward in severity. Protective factors may reduce recommended reserve intensity but should not silently bypass hard integrity rules.

## 6. Required explanation payload

Every assessment must return:

1. Decision  
2. Risk level  
3. Primary risk drivers  
4. Protective factors  
5. Recommended controls  
6. Illustrative reserve recommendation  
7. Conditions for reducing controls  
8. Escalation triggers  
9. Confidence / data-sufficiency  
10. Explicit limitations + synthetic-data disclaimer  

## 7. Governance

Policy changes require version bump, changelog entry, and golden-scenario re-test. Thresholds remain illustrative until validated on internal platform data (not available in this portfolio).
