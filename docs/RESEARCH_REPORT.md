# Research report — Digital goods merchant risk for payment platforms

**Document version:** 0.2.0-draft  
**As-of date for market statistics:** 2026-08-06 (sources dated 2024–2025 unless noted)  
**Claim labeling:** **Evidence** = cited public reporting; **Inference** = strategic conclusion from evidence; **Hypothesis** = plausible mechanism not directly measured here; **Demonstration** = synthetic lab assumption

**Disclaimer:** This report supports an educational strategy demonstrator. It does not use confidential processor, platform, or merchant data.

---

## 1. Executive framing

Payment platforms that historically optimized underwriting around physical goods increasingly encounter merchants whose inventory is intangible and whose fulfillment can be immediate. The strategic problem is not merely “higher fraud rates,” but a different evidence and exposure structure: limited shipping proof, consumed digital value, prepaid obligations, high-frequency microtransactions, and content/platform-integrity events that can interrupt merchant continuity.

**Central question:** How should a payment platform evaluate and control emerging digital-goods merchants when products are intangible, consumption can be immediate, transaction frequency can be high, and traditional underwriting and fulfillment evidence are limited?

---

## 2. Rise of digital goods

### 2.1 Structural growth drivers

| Driver | Type | Notes |
|--------|------|-------|
| Mobile-first consumption | Evidence / Inference | Mobile app stores concentrate discovery and payment; consumer spending on iOS/Google Play IAP, subscriptions, and paid apps reached about **USD 150B in 2024** (+13% YoY) per Sensor Tower State of Mobile 2025 coverage (as of reporting on 2024). |
| Global distribution | Inference | Digital delivery removes physical logistics constraints, enabling rapid cross-border reach. |
| Instant delivery | Inference | Access provisioning replaces shipping; dispute evidence shifts to logs and account state. |
| Subscriptions and microtransactions | Evidence | Subscription revenue on mobile reported around **USD 79.5B in 2025** (Business of Apps compilation of app-store spending; as of 2026 summary citing 2025). Microtransactions remain core to games and virtual goods. |
| Virtual currencies and prepaid credits | Inference / Hypothesis | Prepaid value creates contingent merchant obligations even when current chargebacks are low. |
| Creator-economy monetization | Inference | Platforms pay creators while collecting from consumers; payout timing interacts with dispute windows. |
| AI-enabled product creation | Inference | Lower content-production cost accelerates merchant and catalog experimentation; raises synthetic-content and IP concerns. |
| Low marginal distribution cost | Inference | Scaling volume does not require proportional inventory build; growth can outpace control maturity. |
| Cross-border reach | Inference | Corridor mix affects dispute patterns, FX, and compliance friction. |
| Rapid experimentation | Inference | New SKUs and monetization mechanics appear faster than historical loss series accumulate. |

### 2.2 Market context (cited)

- **Evidence (as of 2024 reporting):** Global consumer spending across iOS and Google Play on in-app purchases, subscriptions, and paid apps/games reached approximately **USD 150 billion in 2024**, +13% YoY; non-gaming growth outpaced gaming (Sensor Tower, *State of Mobile 2025* highlights).  
  Source: https://sensortower.com/blog/2025-state-of-mobile-consumers-usd150-billion-spent-on-mobile-highlights  
- **Evidence (as of 2025 / compiled 2026):** App and game consumer spending reported at about **USD 166.8 billion in 2025**; subscriptions about **USD 79.5 billion** (Business of Apps, App Revenue Data).  
  Source: https://www.businessofapps.com/data/app-revenues/  
- **Evidence / vendor estimate (as of 2025 base year):** Some market researchers estimate a broader “digital goods” market on the order of **USD ~124B in 2025** with high projected CAGRs (Mordor Intelligence digital goods report summary). Definitions differ across vendors; treat magnitude as directional, not precise.  
  Source: https://www.mordorintelligence.com/industry-reports/digital-goods-market  

**Hypothesis:** Short-form drama and paid serialized fiction concentrate risk in low-ticket, high-frequency unlocks and aggressive acquisition funnels—patterns that can look “small” per transaction while creating large aggregate exposure.

### 2.3 Categories in scope

Short-form drama / serialized video; web fiction and paid chapters; mobile and online games; AI subscriptions and generative applications; usage-based AI APIs; virtual goods, credits, and digital memberships.

---

## 3. Digital goods versus traditional products

### 3.1 Comparison table

| Dimension | Traditional physical goods | Digital goods |
|-----------|----------------------------|---------------|
| Fulfillment | Tangible shipment | Intangible access, unlock, credit, or compute |
| Evidence of delivery | Tracking, POD, carrier records | Access/consumption logs, entitlement records |
| Inventory | Recoverable (often) | Consumed or transferred; hard to reclaim |
| Delivery time | Hours to weeks | Seconds to minutes |
| Marginal cost | Material + logistics | Near-zero distribution; content/compute costs vary |
| Global scalability | Constrained by logistics/customs | High; policy and payments become binding constraints |
| Transaction frequency | Often lower | Often high (episodes, energy, tokens, API calls) |
| Average ticket | Wider range; often higher | Often low ticket with high repeat |
| Subscription exposure | Present but not universal | Common; delayed dispute timing |
| Refund verification | Return of goods | Partial; value may already be consumed |
| Chargeback representment | Shipping/fulfillment packets | Weaker traditional packets; log-based evidence |
| Identity / account sharing | Secondary | Central (shared logins, family plans, account markets) |
| Content / IP risk | Labeling, counterfeits | Core product integrity and policy risk |
| Merchant failure obligations | Open orders, returns | Unused credits, unfulfilled subscriptions, creator payouts |

**Inference:** Underwriting that overweights single-transaction ticket size will systematically understate digital-goods portfolio risk when frequency and prepaid liabilities are high.

---

## 4. Risk themes (summary)

Detailed catalog: [DIGITAL_GOODS_RISK_TAXONOMY.md](DIGITAL_GOODS_RISK_TAXONOMY.md).

Four families:

1. **Payment and fraud** — credential theft, card testing, ATO, multi-accounting, promotion abuse, friendly fraud, post-consumption chargebacks, virtual-asset transfer then dispute, refund abuse, subscription disputes, laundering, collusion, cross-border mismatch, velocity.  
2. **Credit and exposure** — negative balances, volume spikes, delayed disputes after payout, insolvency, prepaid/virtual balances, unfulfilled subscriptions, creator obligations, concentration, volatility, thin reserves.  
3. **Compliance and platform integrity** — prohibited content, IP, age, deceptive ads/subscriptions, dark patterns, synthetic/non-consensual AI content, sanctions/geo, consumer protection, privacy, store-policy violations.  
4. **Operational and reputational** — outages, content removal, store suspension, weak support/refunds, rating collapse, single-platform dependency, viral growth without controls, promise–delivery gaps.

---

## 5. Why content monitoring matters to payments

Full framework: [CONTENT_RISK_FRAMEWORK.md](CONTENT_RISK_FRAMEWORK.md).

**Inference:** Content-policy failure is not only a trust-and-safety issue. It can become payments risk through refunds and chargebacks, regulatory action, IP claims, app-store removal, ad-platform cuts, brand damage, merchant interruption, and residual processor/banking exposure after payout.

This lab treats aggregated content-risk indicators as **monitoring and control inputs**, not as a claim of automated moderation capability.

---

## 6. Strategic implications for platform controls

**Inference (best-practice direction):**

- Underwrite by **category and monetization structure**, not MCC alone.  
- Prefer **exposure-based** limits (prepaid liability, settlement lag × dispute lag, growth vs tenure) over revenue-only views.  
- Use progressive limits, delayed settlement, and rolling reserves when evidence is thin.  
- Couple payment metrics with complaint themes and content-integrity signals.  
- Keep human review for high-impact ambiguity; document remediation paths.  

Detail: later best-practice section in [PORTFOLIO_CASE_STUDY.md](PORTFOLIO_CASE_STUDY.md) and [DECISION_POLICY.md](DECISION_POLICY.md).

---

## 7. Separation of claim types

| Type | Examples in this project |
|------|--------------------------|
| Supported by external research | Mobile IAP/subscription spending scale (cited above) |
| Strategic conclusions inferred | Instant fulfillment weakens classical representment; prepaid creates contingent exposure |
| Demonstration assumptions | Synthetic archetype metrics and illustrative thresholds |
| Requires internal platform data to validate | Optimal reserve rates, true loss calibration, fairness impacts |

---

## 8. Limitations

Statistics depend on vendor definitions (app-store IAP vs broader digital goods). Short-drama and web-fiction public market sizes are fragmented; category statements lean on mechanisms more than precise TAM. This report does not estimate loss rates for any real portfolio.
