# P1 evidence and assumption registry

**Version:** 0.1  
**Deep dive:** Short-drama coins  
**Purpose:** Separate externally supported facts, original analytical inferences and synthetic demonstration assumptions before revising the model.

## Evidence policy

Every material statement must belong to one of three classes:

1. **External evidence** — supported by a public source.
2. **Original inference** — Charlene's reasoned interpretation of evidence, clearly presented as analysis rather than fact.
3. **Synthetic assumption** — a configurable numerical input used only to demonstrate how the system behaves.

Public Insight pages should use unobtrusive numbered notes and collect the full source list at the end. The Work page should show assumption provenance near model outputs because those assumptions affect interpretation.

## Research-question chain

| Layer | Statement | Class | Required validation |
|---|---|---|---|
| Problem | Coin top-ups and subscriptions separate payment from consumption and can leave an unconsumed customer obligation | External evidence + original inference | Confirm business-model mechanics; model obligation balance synthetically |
| Mechanism | Instant, intangible fulfillment makes delivery evidence different from shipment-based proof | External evidence + original inference | Map access, device, account, episode-unlock and consumption records |
| Mechanism | High-frequency episode unlocking and renewal flows can increase customer-recognition and dispute complexity | External evidence + original inference | Do not claim higher fraud incidence without comparable data |
| Architecture | Risk should be decomposed into payment fraud, conduct, fulfillment, contingent obligation, continuity and evidence uncertainty | Original framework | Demonstrate that mechanisms produce different controls |
| Demonstration | Horizon and loss assumptions change the reserve requirement | Synthetic assumption | Test 30/60/90 days and low/base/high cases |
| Conclusion | A targeted control package can preserve more viable volume than a blanket restriction at the same synthetic risk constraint | Model result, not external fact | Must be shown through paired counterfactual scenarios |

## Supported industry observations

### Business-model mechanics

- Short-drama services use a mix of memberships and account top-ups; purchased coins are consumed as users unlock content. A public-company filing describes weekly, monthly and annual membership plans, coin top-ups, task-earned coins and revenue recognition as memberships lapse or coins are consumed.[1]
- Industry research describes subscription and transactional payments as a major part of microdrama monetization and identifies free introductory viewing followed by paid access.[2]
- These mechanics justify modeling payment, stored balance, episode access and content consumption as separate events. This is an original modeling implication, not a claim that every merchant uses the same ledger design.

### Disputes and fulfillment evidence

- Visa identifies digital goods and subscriptions as contexts in which fulfillment may be difficult to prove and recommends retaining usage information relevant to the transaction.[3]
- Visa's public explanation of compelling evidence references prior undisputed transactions and matching identity signals such as IP address or device ID.[3]
- Mastercard describes first-party misuse as including forgotten purchases, unrecognized descriptors, family-member use and intentional attempts to obtain goods without paying.[4]
- These sources support collecting evidence-quality and consumption records. They do not support using IP address alone as a fraud verdict.

### Subscription conduct

- FTC materials and enforcement activity identify disclosure, informed consent and cancellation friction as recurring consumer-protection concerns. The agency's broader 2024 Click-to-Cancel rule was vacated in 2025, and the FTC reopened the rulemaking question in 2026; the project should therefore present these as conduct-risk principles, not as a claim that the vacated federal rule is currently in force.[5]
- The project should therefore treat disclosure, consent, renewal and cancellation evidence as conduct controls distinct from stolen-payment-credential controls.

## Original risk mechanism map

| Mechanism | Short-drama manifestation | Candidate signals | Appropriate control family |
|---|---|---|---|
| Payment credential abuse | Stolen card funds coin top-up followed by rapid consumption | Device novelty, payment velocity, authentication result, account age | Step-up authentication, velocity limit, delayed availability for anomalous top-ups |
| First-party misuse | Customer consumes episodes and later disputes a recognized purchase | Prior undisputed history, descriptor recognition, account access and episode consumption | Clear descriptors, receipts, consumption evidence, dispute deflection |
| Household or account misuse | Child or another household member purchases coins | Device/account relationship, parental-control settings, unusual spend change | Spend controls, confirmation, account security |
| Renewal conduct | Customer misunderstands trial conversion or recurring charge | Consent artifact, term disclosure, renewal reminder, cancellation log | Clear consent, reminder, easy cancellation, refund remediation |
| Stored customer obligation | Coins are sold before episodes or services are delivered | Unspent balance, expected redemption, breakage assumption, content availability | Exposure-based reserve, settlement staging, balance reconciliation |
| Metering mismatch | Payment ledger, coin wallet and episode unlocks do not reconcile | Ledger variance, duplicate debit, failed unlock, reversal timing | Automated reconciliation, exception queue, customer remediation |
| Content continuity | Rights issue or removal prevents expected access | Rights status, takedown rate, catalog concentration, availability incident | Content review, concentration limit, reserve uplift tied to outstanding obligation |
| Promotion abuse | Multiple accounts farm bonus coins or discounts | Linked devices, repeated identities, promotion velocity, redemption pattern | Eligibility rules, graph/velocity checks, bonus limits |
| Merchant misrepresentation | Merchant obscures business model, content source or fulfillment | Domain/app mismatch, descriptor mismatch, ownership and rights evidence | Enhanced underwriting, processing limits, manual review |

## Synthetic model assumptions to register

The following values must be configurable and must not be presented as observed industry rates:

| Assumption family | Required parameters | Test design |
|---|---|---|
| Commercial scale | Attempted volume, approval rate, platform take rate | Per $100 and $1 million monthly volume |
| Coin economics | Top-up size, consumption rate, unused balance, breakage | Low/base/high redemption and consumption speed |
| Fraud | Unauthorized rate, first-party misuse rate, loss severity | Low/base/high; never merge authorization and conduct risk |
| Disputes | Dispute rate, arrival lag, evidence win rate, handling cost | 30/60/90-day cumulative vintages |
| Continuity | Content interruption probability and affected obligation share | Paired case with other inputs held constant |
| Controls | Effect, cost, friction, implementation latency | Mechanism-specific ranges, not universal multipliers |
| Reserve | Target coverage, release condition, liquidity cost, cap | Compare coverage gap across 30/60/90 days |
| Evidence | Completeness, recency and analyst confidence | Sensitivity test; low confidence may route to review |

## First short-drama paired demonstrations

### Pair A — Coin obligation

- Hold payment fraud, volume, merchant maturity and dispute behavior constant.
- Change only the unused coin balance and expected consumption duration.
- Expected directional result: exposure protection changes; authentication controls do not.

### Pair B — Credential abuse

- Hold outstanding coin obligation and content continuity constant.
- Change device novelty, top-up velocity and authentication strength.
- Expected directional result: payment controls change; reserve should change only if the attack affects recoverable exposure.

### Pair C — Conduct and recognition

- Hold unauthorized fraud constant.
- Change disclosure quality, descriptor recognition, cancellation accessibility and consumption evidence.
- Expected directional result: conduct remediation and dispute strategy change without treating the merchant as a stolen-card fraud case.

### Interaction — Rapid consumption under weak evidence

- Combine rapid post-top-up consumption, novel device activity and incomplete entitlement logs.
- Test whether layered authentication, temporary top-up availability limits and evidence repair outperform a blanket decline under the same synthetic loss constraint.

## Evidence gaps

- No public source located in this initial pass establishes a reliable fraud-rate benchmark specifically for direct-web short-drama coin purchases.
- Public market estimates often focus on mobile app purchases, while P1 excludes app-store payments. Market-size statistics therefore should be contextual only, not model inputs.
- Card-network materials describe dispute mechanisms and evidence practices but do not provide merchant-specific loss calibration.
- Numerical control effects, reserve coverage targets and dispute-lag distributions require sensitivity ranges until proprietary platform data is available.

## Source notes

1. [Mega Matrix Corp., Form 20-F filed with the U.S. Securities and Exchange Commission](https://www.sec.gov/Archives/edgar/data/1953021/000121390026044335/ea0281860-20f_mega.htm) — public description of membership, top-up, coin-consumption and revenue-recognition mechanics.
2. [Omdia, “Microdramas to generate $11bn in global revenue in 2025”](https://omdia.tech.informa.com/om139375/microdramas-to-generate-%2411bn-in-global-revenue-in-2025) — industry context on subscription and transactional monetization.
3. [Visa, “Friendly fraud explained: prevention and solutions”](https://corporate.visa.com/en/solutions/visa-protect/insights/friendly-fraud.html) — dispute, fulfillment and transaction-evidence context for digital goods and subscriptions.
4. [Mastercard, “Friendly fraud? Help for merchants on fraudulent chargebacks”](https://newsroom.mastercard.com/news/perspectives/2024/sellers-beware-getting-to-the-bottom-of-first-party-fraud/) — examples of first-party misuse and merchant evidence burden.
5. [Federal Trade Commission, 2026 request for comment on negative-option marketing practices](https://www.ftc.gov/news-events/news/press-releases/2026/03/ftc-seeks-public-comment-response-advance-notice-proposed-rulemaking-regarding-negative-option) — current federal rulemaking context and ongoing concerns about enrollment and cancellation practices. The FTC states that the broader 2024 rule was vacated; legal applicability must be rechecked before publication.
