# Synthetic scenario catalog

**Version:** 0.1.0  
**Payment scope:** Direct web payments only  
**Default economics:** USD 1,000,000 monthly attempted payment volume, configurable

## 1. Channel boundary

The demonstrator models merchants that accept customer payments through their own web checkout using a general digital payment platform.

### Included

- Browser-based card or wallet checkout
- Web subscriptions
- Web purchases of coins, credits and virtual items
- Merchant-maintained entitlement and credit ledgers
- Consumption through web or linked merchant experiences after a web purchase
- Direct merchant refunds and card disputes
- Browser, account, IP, geolocation and payment-velocity signals available to the merchant or payment platform
- Cross-border web payments

### Excluded

- Apple App Store billing
- Google Play billing
- App-store settlement, refund and commission mechanics
- App-store purchases used as payment-platform transactions
- Claims that app-store telemetry is available to the modeled payment platform

External platforms may still appear as acquisition, content-distribution or dependency risks, but not as the modeled payment rail.

## 2. Scenario design

The catalog contains eight synthetic merchants. Short drama and AI services receive three scenarios each; web fiction and games provide comparative coverage.

| ID | Category | Scenario | Primary question |
|----|----------|----------|------------------|
| SD-01 | Short drama | Controlled launch | Can a new coin-based merchant grow under progressive controls? |
| SD-02 | Short drama | Viral cross-border growth | How should controls change when volume accelerates faster than evidence? |
| SD-03 | Short drama | Post-consumption dispute deterioration | When do refund, complaint and dispute patterns justify stronger intervention? |
| AI-01 | AI services | Established subscription and credits | What protective factors justify lower controls? |
| AI-02 | AI services | Trial-to-paid renewal stress | How should subscription conduct and renewal disputes influence decisions? |
| AI-03 | AI services | Account/API-key abuse and usage spike | How should the platform separate legitimate growth from compromised access? |
| WF-01 | Web fiction | Creator platform with prepaid chapter credits | How do customer credits and creator obligations interact? |
| GM-01 | Games | Web store with transferable virtual items | How does transferability reduce recoverability after account takeover or dispute? |

## 3. Shared scenario structure

Each scenario must contain:

1. Merchant profile and monetization model.
2. Web-payment and fulfillment flow.
3. Publicly observable information.
4. Merchant-provided underwriting information.
5. Synthetic platform-internal indicators.
6. Derived interaction variables.
7. Baseline assessment.
8. Triggering event or trend.
9. Permissive, balanced-growth and conservative control packages.
10. Normalized and USD 1,000,000 commercial results.
11. Conditions for reducing controls.
12. Escalation triggers.
13. Known limitations and unavailable data.

## 4. Short-drama deep-dive product model

The synthetic short-drama merchant sells coin bundles through web checkout. Customers use coins to unlock serialized episodes.

### Baseline assumptions

- Coins are recorded in a merchant-controlled customer ledger.
- Purchased coins do not expire.
- Purchased coins are not redeemable for cash.
- Purchased coins are not transferable between customers.
- Promotional coins are tracked separately and may expire only under clearly disclosed terms.
- A purchase creates an outstanding obligation until the associated coins are consumed or refunded.
- Episode access and coin-consumption events create fulfillment evidence, but do not guarantee successful dispute representment.
- Checkout, auto-recharge and refund terms are visible inputs in the conduct assessment.
- The payment platform sees web payments and aggregated merchant performance; customer-level telemetry is synthetic.

### Core calculated variables

```text
unused_purchased_coin_value
  = purchased_coin_value − consumed_coin_value − refunded_coin_value

prepaid_exposure_ratio
  = unused_purchased_coin_value / monthly_approved_payment_volume

post_consumption_dispute_share
  = disputed_volume_after_consumption / total_disputed_volume

coin_purchase_intensity
  = coin_purchase_transaction_count / active_paying_customers

exposure_after_available_protection
  = contingent_customer_obligation
    + expected_dispute_loss
    − available_merchant_balance
    − eligible_reserve
```

## 5. Short-drama scenarios

### SD-01 — Controlled launch

**Profile:** Six-month-old US-based merchant launching web coin bundles for short-drama episodes. Moderate cross-border customer share, limited processing history, clear purchase terms and functioning customer support.

**Risk tension:** Low demonstrated loss but limited evidence and a growing unused-coin balance.

**Balanced-growth posture:** Approve with progressive volume limit, enhanced monitoring and a modest temporary reserve or settlement control tied to outstanding exposure.

**Release conditions:** Stable dispute/refund trends, verified coin-liability reporting, stronger fulfillment evidence and sufficient observation history.

**Learning objective:** Newness should reduce confidence and increase exposure controls without being treated as evidence of misconduct.

### SD-02 — Viral cross-border growth

**Profile:** Healthy merchant experiences a rapid marketing-driven volume increase across several countries.

**Trigger:** Monthly attempted payment volume increases several-fold; new-customer and cross-border shares rise; retry activity increases, while complaints remain initially stable.

**Risk tension:** Legitimate viral growth can resemble fraud or outgrow the merchant’s support and loss-absorption capacity.

**Balanced-growth posture:** Preserve processing with staged volume expansion, corridor monitoring, velocity controls, reserve/exposure recalculation and a scheduled review.

**Release conditions:** Cohort performance stabilizes, retry and decline patterns normalize, customer support capacity is demonstrated and contingent exposure remains funded.

**Learning objective:** Compare the value of progressive controls with both permissive exposure and conservative volume suppression.

### SD-03 — Post-consumption dispute deterioration

**Profile:** A previously stable merchant introduces aggressive episode promotions and optional auto-recharge.

**Trigger:** Cancellation and refund complaints rise, followed by disputes after substantial coin consumption. Advertising complaints and content-rights questions also increase.

**Risk tension:** Payment performance, customer conduct and content continuity deteriorate together.

**Balanced-growth posture:** Pause expansion, require subscription/auto-recharge remediation, increase monitoring and protection against outstanding exposure, and route unresolved content-rights concerns to manual review.

**Escalation:** Continued deceptive practices, severe dispute acceleration, absent rights evidence or insufficient funds to cover obligations.

**Learning objective:** Content and conduct signals can change payment exposure even before merchant failure occurs.

## 6. AI-service deep-dive product models

The AI scenarios use direct web checkout and distinguish:

- Monthly subscriptions
- Free-trial conversion
- Prepaid generation credits
- Usage-based web/API billing
- Hybrid subscription plus overage credits

Credits are merchant ledger entries, not cryptocurrencies. The model does not assume that credits are transferable or cash-redeemable.

## 7. AI-service scenarios

### AI-01 — Established subscription and credits

**Profile:** Thirty-month-old AI productivity service with transparent monthly subscriptions, optional prepaid credits, low complaint rates and strong account security.

**Risk tension:** Moderate prepaid exposure exists, but tenure, reliability, clear terms and financial capacity are protective.

**Balanced-growth posture:** Approve with standard monitoring and periodic obligation reporting; avoid unnecessary reserve burden.

**Learning objective:** Protective factors should materially reduce controls rather than merely decorate the explanation.

### AI-02 — Trial-to-paid renewal stress

**Profile:** Fast-growing consumer AI-generation service using a free trial that converts to a monthly plan.

**Trigger:** Renewal disputes and cancellation complaints increase after a promotional campaign; refunds rise as the merchant proactively remediates some cases.

**Risk tension:** A temporary increase in refunds may reduce later disputes and should not automatically be treated as worsening risk.

**Balanced-growth posture:** Require clearer trial and cancellation practices, monitor renewal cohorts, use targeted controls and reassess before imposing broad payment limits.

**Learning objective:** Separate proactive refund cost from delayed dispute loss and measure whether conduct remediation improves sustainable contribution.

### AI-03 — Account/API-key abuse and usage spike

**Profile:** Usage-based AI service with customer accounts and optional API keys paid through web checkout.

**Trigger:** A small group of accounts generates sudden usage and payment attempts from new devices and geographies. Service cost rises before all payments settle.

**Risk tension:** Genuine enterprise usage expansion and compromised access can appear similar at first.

**Balanced-growth posture:** Apply account-specific limits, step-up authentication, velocity monitoring and temporary exposure controls while preserving unaffected merchant volume.

**Learning objective:** Mechanism-specific controls can outperform a merchant-wide block.

## 8. Comparative scenarios

### WF-01 — Web-fiction creator platform

**Profile:** Web platform sells chapter credits and shares revenue with contracted authors.

**Risk tension:** Customer prepaid balances and creator payables create different obligations with different timing.

**Balanced-growth posture:** Require separate reporting of customer and creator obligations, monitor rights complaints and align settlement protection with the uncovered obligation gap.

### GM-01 — Web game store with transferable virtual items

**Profile:** Browser-based game sells virtual currency and allows purchased items to be gifted or traded within a closed merchant ecosystem.

**Risk tension:** Account takeover followed by item transfer reduces recoverability after a dispute.

**Balanced-growth posture:** Use transfer cooling periods for newly funded accounts, account-security controls and exposure-sensitive protection rather than blocking all web-store purchases.

## 9. Scenario progression

Each merchant should have at least four observation periods:

1. Baseline
2. Growth or early warning
3. Stress or deterioration
4. Remediation or escalation

This makes the project a monitoring and control-adjustment demonstrator, not a one-time onboarding scorecard.

## 10. Next implementation gate

Initial numeric assumptions and golden decisions are specified in [SCENARIO_CALIBRATION_SPEC.md](SCENARIO_CALIBRATION_SPEC.md). Before generating data, verify:

- Numeric baseline values and permitted ranges
- Correlations and overlap among fraud, disputes and refunds
- Policy-posture effects
- Missing-data cases
- Hard-rule triggers
- Commercial and liquidity-cost assumptions
- Golden expected decisions
