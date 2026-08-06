# Digital-goods risk taxonomy

**Version:** 0.2.0-draft  
**Purpose:** Organized catalog of risks relevant to payment-platform evaluation of digital-goods merchants.  
**Disclaimer:** Conceptual and educational. Not a complete regulatory inventory. Demonstration data only elsewhere in this repo.

For each risk: mechanism, leading indicators, impact, controls, residual limitations, most-affected categories.

**Category keys:** `drama` short-form drama/video · `fiction` web fiction · `games` · `ai_sub` AI subscription apps · `ai_api` usage-based AI · `virtual` virtual goods/credits/memberships · `all`

---

## A. Payment and fraud risk

### A1. Stolen payment credentials
- **Mechanism:** Compromised cards/wallets used to buy digital value quickly.  
- **Leading indicators:** Velocity spikes, geo/device mismatch, high new-account share, decline/retry bursts.  
- **Impact:** Direct fraud loss; network monitoring pressure.  
- **Controls:** Velocity limits, device/account risk checks, progressive auth, enhanced monitoring.  
- **Residual limitations:** Fast consumption reduces recoverability.  
- **Categories:** `all` (esp. `games`, `virtual`, `drama`)

### A2. Card testing
- **Mechanism:** Low-value authorizations probe card validity.  
- **Leading indicators:** Many small auths, high decline rate, sequential BINs, short session bursts.  
- **Impact:** Fees, fraud downstream, processor scrutiny.  
- **Controls:** Velocity/BIN controls, challenge low-ticket bursts, merchant volume caps while young.  
- **Residual limitations:** Testers adapt amounts and corridors.  
- **Categories:** `all`

### A3. Account takeover (ATO)
- **Mechanism:** Attacker accesses legitimate user accounts and spends stored value or payment methods.  
- **Leading indicators:** Login anomalies, password-reset spikes, sudden spend pattern change, support surge.  
- **Impact:** Friendly-looking transactions; hard disputes; CX damage.  
- **Controls:** Step-up auth, session risk, spend cool-downs, monitoring of entitlement changes.  
- **Residual limitations:** Shared accounts blur legitimate vs abusive use.  
- **Categories:** `games`, `virtual`, `ai_sub`, `fiction`

### A4. Multi-account abuse
- **Mechanism:** Linked accounts farm trials, promos, or risk limits.  
- **Leading indicators:** Device/payment graph concentration, repeated trial redemptions, correlated chargebacks.  
- **Impact:** Economics leakage; contaminated risk signals.  
- **Controls:** Graph limits, promo eligibility rules, enhanced review on concentration.  
- **Residual limitations:** Privacy-preserving linking is imperfect.  
- **Categories:** `ai_sub`, `drama`, `games`

### A5. Promotion and free-trial abuse
- **Mechanism:** Systematic exploitation of trials/credits without conversion intent.  
- **Leading indicators:** High trial start / low convert, dispute after trial, identity cycling.  
- **Impact:** Acquisition cost, dispute after partial use.  
- **Controls:** Trial friction by risk tier, payment-method reputation, subscription-practice review.  
- **Residual limitations:** Aggressive friction harms conversion.  
- **Categories:** `ai_sub`, `drama`, `fiction`

### A6. Friendly fraud
- **Mechanism:** Legitimate user disputes after use (“not recognized” / “not as described”).  
- **Leading indicators:** Dispute reasons vs consumption logs, repeat disputers, descriptor confusion.  
- **Impact:** Loss with weak representment.  
- **Controls:** Clear descriptors, consumption evidence packs, refund UX, cooling-off rules.  
- **Residual limitations:** Schemes favor cardholders in ambiguity.  
- **Categories:** `all`

### A7. Chargebacks after digital consumption
- **Mechanism:** Dispute filed after episodes/items/compute consumed.  
- **Leading indicators:** Time-to-dispute vs consumption, high unlock velocity then CB.  
- **Impact:** Unrecoverable COGS-like value + fees.  
- **Controls:** Settlement delay for young merchants, reserves, fulfillment-evidence standards.  
- **Residual limitations:** Evidence may not win representment.  
- **Categories:** `drama`, `fiction`, `games`, `ai_api`

### A8. Chargebacks after virtual-asset transfer
- **Mechanism:** Value moved (gift, trade, secondary) then original payment disputed.  
- **Leading indicators:** Transfer/gift features on, rapid transfer after purchase, CB uplift.  
- **Impact:** Near-zero recoverability.  
- **Controls:** Transfer limits for new payers, holds on giftable value, higher reserves.  
- **Residual limitations:** Social features drive engagement and risk together.  
- **Categories:** `games`, `virtual`

### A9. Refund abuse
- **Mechanism:** Repeated refunds after partial consumption or serial refund behavior.  
- **Leading indicators:** Refund rate ↑ with consumption complete; repeat refunders; support policy gaps.  
- **Impact:** Margin erosion; operational load.  
- **Controls:** Tiered refund policy, abuse scoring, merchant support SLAs.  
- **Residual limitations:** Strict policies raise complaints/CBs.  
- **Categories:** `all`

### A10. Subscription-renewal disputes
- **Mechanism:** Users dispute renewals citing surprise, cancel friction, or forgotten trials.  
- **Leading indicators:** Cancel complaints, dark-pattern signals, renewal CB clustering.  
- **Impact:** Delayed losses; regulatory/CX risk.  
- **Controls:** Subscription-practice review, transparent cancel, reminder policies, monitoring.  
- **Residual limitations:** Jurisdiction rules vary.  
- **Categories:** `ai_sub`, `fiction`, `drama`, `virtual`

### A11. Transaction laundering
- **Mechanism:** Approved merchant processes for undisclosed business.  
- **Leading indicators:** Descriptor mismatch, sudden category shift, content vs MCC inconsistency.  
- **Impact:** Network brand risk; catastrophic offboarding.  
- **Controls:** Content/category monitoring, volume anomaly review, manual underwriting.  
- **Residual limitations:** Detection often lagging.  
- **Categories:** `all`

### A12. Collusive merchant–customer behavior
- **Mechanism:** Coordinated purchases and refunds/chargebacks to extract value.  
- **Leading indicators:** Tight graph clusters, mirrored timestamps, repeated pairs.  
- **Impact:** Structured loss.  
- **Controls:** Graph analytics, enhanced monitoring, decline on confirmed collusion.  
- **Residual limitations:** Needs sufficient network data (not available in this demo).  
- **Categories:** `virtual`, `games`

### A13. Cross-border payment mismatch
- **Mechanism:** Billing region, content region, and user region diverge in risky ways.  
- **Leading indicators:** High cross-border share + geo-restricted content; corridor CB spikes.  
- **Impact:** Higher dispute complexity; sanctions/geo issues.  
- **Controls:** Geo restrictions, corridor limits, enhanced review.  
- **Residual limitations:** VPN obfuscation.  
- **Categories:** `drama`, `fiction`, `games`, `ai_api`

### A14. Rapid transaction and retry velocity
- **Mechanism:** Bursts of attempts (fraud, outages, or bot farms).  
- **Leading indicators:** TPS spikes, retry rate, decline storms.  
- **Impact:** Fraud and ops overload.  
- **Controls:** Rate limits, processing-volume caps, monitoring.  
- **Residual limitations:** Legitimate viral events look similar.  
- **Categories:** `all`

---

## B. Credit and exposure risk

### B1. Negative merchant balances
- **Mechanism:** Refunds/CBs/fees exceed available balance.  
- **Leading indicators:** Balance trend, CB/refund surge, thin buffer.  
- **Impact:** Direct platform credit loss.  
- **Controls:** Reserves, settlement delay, volume limits.  
- **Residual limitations:** Sudden spikes still breach.  
- **Categories:** `all`

### B2. Sudden processing-volume growth
- **Mechanism:** TPV jumps faster than history supports.  
- **Leading indicators:** MoM growth, new-customer share, marketing spikes.  
- **Impact:** Unseasoned exposure.  
- **Controls:** Progressive limits, enhanced monitoring, reserves.  
- **Residual limitations:** Caps constrain revenue.  
- **Categories:** `drama`, `ai_sub`, `games`

### B3. Delayed disputes after payout
- **Mechanism:** Chargebacks arrive after settlement.  
- **Leading indicators:** Long refund windows, subscription renewals, cross-border lags.  
- **Impact:** Unsecured loss.  
- **Controls:** Settlement delay matched to dispute lag, rolling reserves.  
- **Residual limitations:** Holding capital has friction cost.  
- **Categories:** `all`

### B4. Merchant insolvency or disappearance
- **Mechanism:** Operator stops supporting obligations.  
- **Leading indicators:** Support collapse, content freeze, payout irregularity, complaints.  
- **Impact:** Customer harm; residual disputes hit platform.  
- **Controls:** Reserves, prepaid exposure caps, continuity review.  
- **Residual limitations:** Early detection imperfect.  
- **Categories:** `all`

### B5–B8. Outstanding prepaid credits / unused virtual currency / unfulfilled subscriptions / creator payout obligations
- **Mechanism:** Customer or creator liabilities exceed liquid capacity.  
- **Leading indicators:** Prepaid liability ratio, unused balance growth, subscription backlog, creator payable aging.  
- **Impact:** Contingent credit + conduct risk.  
- **Controls:** Exposure-based reserves, liability reporting, payout pacing.  
- **Residual limitations:** Merchant-reported liability may be incomplete (demo uses proxies).  
- **Categories:** `virtual`, `games`, `fiction`, `ai_sub`

### B9. High customer or product concentration
- **Mechanism:** Few SKUs or whales dominate revenue.  
- **Leading indicators:** Concentration indices, top-SKU share.  
- **Impact:** Shock sensitivity.  
- **Controls:** Monitoring, reserves under growth, product review.  
- **Residual limitations:** Concentration can be normal early.  
- **Categories:** `games`, `drama`, `ai_api`

### B10. Revenue volatility
- **Mechanism:** Unstable cash generation impairs loss absorption.  
- **Leading indicators:** Volume volatility, seasonal spikes.  
- **Impact:** Reserve inadequacy risk.  
- **Controls:** Higher floors under volatility, delayed settlement.  
- **Residual limitations:** Volatility ≠ fraud.  
- **Categories:** `ai_api`, `games`

### B11. Insufficient reserves vs contingent liabilities
- **Mechanism:** Control settings lag liability growth.  
- **Leading indicators:** Prepaid ↑ while reserve flat; CB lag.  
- **Impact:** Gap at stress.  
- **Controls:** Recalibrate reserve bands to exposure metrics.  
- **Residual limitations:** Illustrative only in this lab.  
- **Categories:** `all`

---

## C. Compliance and platform-integrity risk

### C1–C12 (summary catalog)

| ID | Risk | Mechanism (short) | Leading indicators | Impact | Controls | Limitations | Categories |
|----|------|-------------------|--------------------|--------|----------|-------------|------------|
| C1 | Prohibited/restricted content | Policy-violating catalog | Category flags, reports | Removal, disputes | Content review, geo limits | Signal lag | `drama`,`fiction`,`ai_sub` |
| C2 | Copyright / IP infringement | Unlicensed material | Claims volume, repeat strikes | Legal + interruption | Content review, manual UW | Fair use ambiguity | `drama`,`fiction`,`ai_sub` |
| C3 | Age-inappropriate content | Minors exposure | Age-gate gaps, complaints | Regulatory/reputation | Age restrictions, review | Enforcement gaps | `drama`,`games` |
| C4 | Misleading advertising | Promise ≠ product | Ad complaints, refund themes | CB + brand | Ad/practice review | Attribution hard | `drama`,`ai_sub` |
| C5 | Deceptive subscriptions | Hidden renewals | Cancel complaints | Conduct + CB | Subscription-practice review | Legal variance | `ai_sub`,`fiction` |
| C6 | Dark-pattern cancellations | Cancel friction | Support tickets, UX audits | Regulatory | Practice review, remediation | Detection qualitative | `ai_sub` |
| C7 | Synthetic / non-consensual AI content | Harmful generative output | Disclosure gaps, reports | Severe integrity event | Content review, enhanced monitoring | Fast-evolving norms | `ai_sub`,`ai_api` |
| C8 | Illegal / jurisdiction-restricted content | Local law breach | Geo mismatch | Forced exit | Geo restriction | VPN | `all` |
| C9 | Sanctions / geographic restrictions | Restricted corridors | Geo/payment mismatch | Legal | Geo controls | Complex ownership | `all` |
| C10 | Consumer-protection violations | Unfair practices | Regulator themes | Fines + offboarding | Manual review | Jurisdiction-specific | `all` |
| C11 | Privacy / data-use concerns | Misuse of user data | Privacy complaints | Trust + legal | Info requests, review | Hard to observe externally | `ai_sub`,`ai_api` |
| C12 | App-store / platform-policy violations | Store rule breaches | Removal events, warnings | Volume cliff | Platform-dependency monitoring | Single-point failure | `drama`,`games`,`ai_sub` |

---

## D. Operational and reputational risk

| ID | Risk | Mechanism | Leading indicators | Impact | Controls | Limitations | Categories |
|----|------|-----------|--------------------|--------|----------|-------------|------------|
| D1 | Service outages | Downtime | Reliability metrics, complaints | Refunds, CB | Monitoring, support review | Outages ≠ fraud | `ai_api`,`games` |
| D2 | Content removal | Catalog purge | Moderation spikes | Revenue shock | Content + reserve | Sudden | `drama`,`fiction` |
| D3 | App-store suspension | Distribution loss | Store notices | Near-total volume loss | Dependency review, reserves | Binary event | `drama`,`games`,`ai_sub` |
| D4 | Weak customer support | Unresolved issues | Complaint rate, response time | Refund/CB conversion | Enhanced monitoring | Proxy metrics | `all` |
| D5 | Poor refund handling | Friction/conflict | Refund disputes | CB migration | Policy review | Trade-off with abuse | `all` |
| D6 | Ratings/complaints deterioration | Trust collapse | Review velocity, themes | Leading loss indicator | Escalation triggers | Review bombing | `all` |
| D7 | Platform/infrastructure dependence | Single point of failure | Store share of volume | Correlated shock | Diversification review | Hard for startups | `all` |
| D8 | Viral growth without controls | Demand >> ops/risk | Growth + thin tenure | Control failure | Progressive limits | Caps vs growth | `drama`,`games` |
| D9 | Promise–delivery misalignment | Over-marketing | Complaint themes | Friendly fraud | Content/ad review | Subjective | `ai_sub`,`drama` |

---

## How the lab uses this taxonomy

Assessment outputs map drivers to taxonomy codes (e.g., `A7`, `B5`, `C2`). Not every risk is independently scored; interactions are handled in [DECISION_POLICY.md](DECISION_POLICY.md).
