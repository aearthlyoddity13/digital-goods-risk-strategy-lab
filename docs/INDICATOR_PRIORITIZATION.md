# Indicator prioritization framework

**Version:** 0.1.0  
**Purpose:** Convert the broad risk taxonomy into a decision-ready indicator set.

## Priority definitions

- **P0 — essential:** Required to produce a minimally credible assessment.
- **P1 — important:** Materially improves control selection or explanation.
- **P2 — contextual:** Useful for deep review, stress testing or future internal-data calibration.

## Availability definitions

- **Public:** Can be researched externally.
- **Merchant-provided:** Would be requested during underwriting or review.
- **Platform-internal:** Requires processor or merchant telemetry; synthetic in this project.
- **Derived:** Calculated from other variables.

## Core indicator set

| Indicator family | Priority | Availability | Representative indicators | Primary decision use |
|------------------|----------|--------------|---------------------------|----------------------|
| Merchant identity and ownership | P0 | Public + merchant-provided | Entity age, ownership transparency, operating regions, website/app identity consistency | Onboarding, additional information, decline on unresolved legitimacy concerns |
| Product and monetization structure | P0 | Public + merchant-provided | Subscription share, coin/credit structure, auto-recharge, virtual-item transferability, refund and expiry terms | Category baseline, conduct review, exposure modeling |
| Payment performance | P0 | Platform-internal | Dispute, refund, fraud-loss, decline and retry rates | Monitoring, reserve, settlement and escalation |
| Volume and maturity | P0 | Platform-internal + derived | Monthly volume, growth, volatility, merchant tenure, new-customer share | Progressive limits, monitoring and data-confidence assessment |
| Outstanding customer obligation | P0 | Merchant-provided + derived | Unused coins/credits, unfulfilled subscription value, obligation-to-volume ratio | Reserve, settlement delay and stress loss |
| Customer conduct and support | P0 | Public + merchant-provided + platform-internal | Cancellation clarity, complaint rate, support responsiveness, descriptor clarity | Subscription review, remediation and dispute prevention |
| Content and IP governance | P0 for deep dives; P1 otherwise | Public + merchant-provided | Rights documentation, takedowns, repeat complaints, moderation processes, restricted-content exposure | Content review, geographic control, interruption stress |
| Cross-border and sanctions | P0 | Public + merchant-provided + platform-internal | Operating regions, corridor mix, sanctions screening, geo inconsistency | Geographic limits, enhanced due diligence, manual review |
| Fulfillment evidence | P1 | Merchant-provided + platform-internal | Entitlement, access, consumption, credit-balance and delivery logs | Dispute evidence, control reduction and confidence |
| Account and device integrity | P1 | Platform-internal | Account tenure, device reuse, IP risk, geolocation, velocity, session anomaly | Fraud monitoring and step-up controls |
| Merchant financial capacity | P1 | Merchant-provided | Liquidity, cash runway, negative-balance capacity, concentration | Reserve intensity and exposure capacity |
| External-platform dependency | P1 | Public + merchant-provided | App-store share, social-acquisition share, content-supplier concentration, model-provider dependency | Interruption stress and monitoring |
| Network and graph analytics | P2 | Platform-internal | Linked devices, accounts, cards, customers and merchant clusters | Collusion, promotion abuse and laundering analysis |

## Essential derived interactions

These interactions should be visible and separately explained; they must not be hidden inside an opaque score.

| Interaction | Strategic interpretation |
|-------------|--------------------------|
| Low ticket × high frequency | Small purchases can still create material aggregate fraud and dispute exposure. |
| Rapid growth × short tenure | Commercial opportunity rises before evidence matures. |
| Prepaid obligation × settlement speed | The platform may release funds before customer obligations are extinguished. |
| Consumption speed × weak fulfillment evidence | Recoverability and dispute defensibility may deteriorate. |
| Subscription share × cancellation complaints | Conduct problems can become delayed payment losses. |
| Content/IP risk × platform dependency | A policy or rights event can interrupt fulfillment and cash flow. |
| Cross-border share × weak geo confidence | Compliance and dispute complexity increase. |
| Reserve burden × merchant liquidity | A control can reduce platform exposure while weakening merchant sustainability. |

## Short-drama deep-dive indicators

### P0

- Coin purchase and consumption structure
- Auto-recharge and subscription terms
- Unused coin obligation
- Transaction frequency and retry behavior
- Dispute/refund rate after consumption
- Customer-support and cancellation accessibility
- Content licensing and takedown history
- App-store and acquisition-channel concentration

### P1

- Episodes consumed before dispute
- Promotion and multi-account concentration
- Payment descriptor recognition
- Cross-border customer and content mix
- Advertising complaint themes

## AI subscription and credit deep-dive indicators

### P0

- Trial-to-paid and renewal structure
- Credit purchase, expiry and refund terms
- Subscription and usage-based revenue mix
- Account/API-key security controls
- Sudden usage and transaction growth
- Dispute/refund rate around renewal
- Generated-content governance
- Third-party model-provider dependency

### P1

- Usage incurred before successful payment recovery
- Promotional-credit abuse
- Service reliability and latency complaints
- Product-performance claim complaints
- Rights, privacy and digital-replica complaint process

## Data-minimization rule

Do not collect or simulate a customer-level field merely because it is technically available. Each indicator must have a documented decision use, privacy rationale, retention assumption and known limitation. IP address, device and geolocation signals may support an assessment but must not independently determine a merchant outcome.

## Next design gate

Before assigning weights or thresholds, define:

1. The risk appetite constraints.
2. The loss and commercial objective functions.
3. Which P0 indicators are available in each synthetic scenario.
4. Missing-data behavior.
5. Conditions under which a hard rule is justified.
