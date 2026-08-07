# Synthetic scenario calibration specification

**Version:** 0.2.0  
**Status:** Initial numerical assumptions for implementation  
**Data classification:** Entirely synthetic; not industry benchmarks

## 1. Calibration principles

1. Values demonstrate internally coherent decisions; they do not estimate real merchant performance.
2. Every numeric assumption is version-controlled and editable.
3. Correlated variables move together only when a documented mechanism connects them.
4. Golden decisions test policy consistency, not predictive accuracy.
5. Balanced growth is the default policy posture.

## 2. Shared commercial assumptions

| Variable | Default |
|----------|---------|
| Monthly attempted payment volume | USD 1,000,000 |
| Platform revenue rate | 2.50% |
| Baseline payment approval rate | 96.0% |
| Successful fulfillment rate | 99.0% |
| Net disputed-principal loss severity | 70% |
| Dispute operating cost | USD 15 per dispute |
| Enhanced monitoring cost | USD 500 per month |
| Manual review cost | USD 75 per reviewed case |
| Merchant annual liquidity cost | 12% |
| Contingent-exposure realization rate | 10% per modeled monthly horizon |
| Balanced-growth near-equivalence band | 0.50% of monthly attempted volume |

These values are editable demonstration assumptions inherited from [COMMERCIAL_SIMULATION_SPEC.md](COMMERCIAL_SIMULATION_SPEC.md).

## 3. Confirmed coin policy

- Purchased coins do not expire.
- Promotional or free coins may expire only under clearly disclosed terms.
- Purchased coins are not transferable or cash-redeemable.
- Purchased and promotional balances are tracked separately.
- Unused purchased coins remain an outstanding customer obligation until consumed or refunded.
- Promotional coins do not create customer-funded principal exposure, although unclear terms can create conduct risk.

## 4. Synthetic baselines

| ID | Age | Attempted volume | Avg ticket | Approval | Refund | Dispute | Fraud loss | Cross-border | Obligation ratio | Complaint | Integrity indicator | Confidence | Balanced-growth baseline |
|----|----:|-----------------:|-----------:|---------:|-------:|--------:|-----------:|-------------:|-----------------:|----------:|--------------------:|------------|--------------------------|
| SD-01 | 6 mo | $1.00M | $12 | 95.5% | 2.0% | 0.60% | 0.25% | 25% | 18% | 0.30% | 0.20 | Medium | APPROVE_WITH_CONTROLS |
| SD-02 | 14 mo | $1.00M | $11 | 96.0% | 2.2% | 0.65% | 0.28% | 35% | 16% | 0.35% | 0.22 | Medium | APPROVE_WITH_CONTROLS |
| SD-03 | 20 mo | $1.00M | $13 | 96.2% | 2.4% | 0.70% | 0.24% | 20% | 14% | 0.40% | 0.25 | High | APPROVE_WITH_CONTROLS |
| AI-01 | 30 mo | $1.00M | $28 | 97.2% | 1.5% | 0.35% | 0.12% | 18% | 10% | 0.20% | 0.12 | High | APPROVE |
| AI-02 | 10 mo | $1.00M | $24 | 96.0% | 2.0% | 0.55% | 0.18% | 22% | 12% | 0.35% | 0.18 | Medium | APPROVE_WITH_CONTROLS |
| AI-03 | 18 mo | $1.00M | $42 | 96.5% | 1.2% | 0.40% | 0.16% | 30% | 8% | 0.20% | 0.16 | High | APPROVE |
| WF-01 | 36 mo | $1.00M | $10 | 97.0% | 1.8% | 0.40% | 0.14% | 28% | 20% | 0.25% | 0.18 | High | APPROVE_WITH_CONTROLS |
| GM-01 | 24 mo | $1.00M | $18 | 96.2% | 1.7% | 0.55% | 0.22% | 32% | 15% | 0.25% | 0.15 | High | APPROVE_WITH_CONTROLS |

No baseline is described as an industry average.

## 5. Observation periods

Every scenario contains `P0_BASELINE`, `P1_EARLY_SIGNAL`, `P2_STRESS` and `P3_OUTCOME`. P3 represents remediation unless the scenario is designed to show unresolved escalation.

## 6. Short-drama progressions

### SD-01 — Controlled launch

| Metric | P0 | P1 | P2 | P3 |
|--------|---:|---:|---:|---:|
| Attempted volume | $1.00M | $1.20M | $1.45M | $1.55M |
| Approval rate | 95.5% | 95.3% | 94.8% | 95.4% |
| Refund rate | 2.0% | 2.1% | 2.5% | 2.1% |
| Dispute rate | 0.60% | 0.65% | 0.82% | 0.58% |
| Fraud-loss rate | 0.25% | 0.28% | 0.36% | 0.22% |
| Unused purchased-coin ratio | 18% | 21% | 26% | 20% |

**Golden progression:** controls → controls → manual review or strengthened controls → controls reduced but retained.

### SD-02 — Viral cross-border growth

| Metric | P0 | P1 | P2 | P3 |
|--------|---:|---:|---:|---:|
| Attempted volume | $1.00M | $2.20M | $3.80M | $3.20M |
| MoM growth | 18% | 120% | 73% | -16% |
| New-customer share | 42% | 68% | 74% | 55% |
| Cross-border share | 35% | 48% | 57% | 50% |
| Retry rate | 6% | 10% | 15% | 8% |
| Dispute rate | 0.65% | 0.72% | 1.05% | 0.68% |
| Unused purchased-coin ratio | 16% | 19% | 24% | 18% |

**Golden progression:** controls → progressive limits and monitoring → manual review with constrained processing → controls reduced after cohort stabilization.

### SD-03 — Post-consumption deterioration

| Metric | P0 | P1 | P2 | P3 unresolved |
|--------|---:|---:|---:|--------------:|
| Refund rate | 2.4% | 3.1% | 4.8% | 5.2% |
| Dispute rate | 0.70% | 0.92% | 1.65% | 2.10% |
| Post-consumption dispute share | 45% | 57% | 71% | 76% |
| Complaint rate | 0.40% | 0.75% | 1.40% | 1.70% |
| Integrity indicator | 0.25 | 0.38 | 0.62 | 0.76 |
| Support within SLA | 92% | 80% | 61% | 55% |

**Golden progression:** controls → stronger controls/remediation → manual review with expansion paused → decline only if deception, prohibited activity or rights failure is confirmed; otherwise continued restriction.

## 7. AI-service progressions

### AI-01 — Established subscription and credits

Moderate operational stress raises disputes from 0.35% to 0.48% and lowers reliability from 99.7% to 99.0%, followed by recovery. High confidence and strong tenure remain protective.

**Golden progression:** approve → approve → approve with targeted monitoring → approve.

### AI-02 — Trial-to-paid renewal stress

| Metric | P0 | P1 | P2 remediation | P3 |
|--------|---:|---:|---------------:|---:|
| Trial-user share | 20% | 34% | 30% | 24% |
| Refund rate | 2.0% | 3.4% | 5.0% | 3.0% |
| Dispute rate | 0.55% | 0.95% | 0.82% | 0.50% |
| Cancellation complaints | 0.30% | 0.85% | 0.60% | 0.25% |
| Renewal-disclosure score | 0.85 | 0.62 | 0.90 | 0.95 |

P2 refunds rise because the merchant proactively resolves complaints. Falling disputes and improved disclosures prevent the refund increase from being treated as simple deterioration.

**Golden progression:** controls → subscription-practice review → controls maintained during remediation → controls reduced.

### AI-03 — Account/API-key abuse

| Metric | P0 | P1 | P2 abuse | P3 recovery |
|--------|---:|---:|---------:|------------:|
| Attempted volume | $1.00M | $1.35M | $1.70M | $1.50M |
| New-device share | 18% | 28% | 52% | 24% |
| High-risk session share | 3% | 7% | 16% | 4% |
| Retry rate | 4% | 8% | 18% | 6% |
| Fraud-loss rate | 0.16% | 0.28% | 0.85% | 0.20% |
| Dispute rate | 0.40% | 0.52% | 1.10% | 0.43% |

**Golden progression:** approve → targeted controls → manual review plus account-specific restrictions while preserving unaffected volume → approve with monitoring.

## 8. Comparative progressions

**WF-01:** stress customer prepaid credits, creator-payable timing and content-rights complaints separately, then jointly. Golden progression: controls → controls → manual review only when obligation coverage and rights evidence deteriorate together → controls reduced after remediation.

**GM-01:** stress new funding source, account-takeover indicators, rapid item transfer and post-transfer dispute. Golden progression: controls → transfer cooling period → manual review during concentrated abuse → controls reduced after account-security remediation.

## 9. Hard-rule candidates

- Confirmed prohibited or illegal activity
- Confirmed sanctions prohibition
- Confirmed deliberate transaction laundering
- Unresolved merchant identity at material exposure
- Confirmed systematic deception after remediation opportunity
- Severe content/rights event preventing lawful fulfillment

High dispute rates, rapid growth, VPN use, short tenure and cross-border activity do not independently trigger decline.

## 10. Missing-data behavior

| Missing field | Balanced-growth response |
|---------------|--------------------------|
| Ownership or identity | Manual review; do not approve material exposure until resolved |
| Customer-obligation balance | Constrain exposure and request reporting |
| Fulfillment evidence | Lower confidence; consider settlement/reserve control |
| Content-rights evidence | Escalate only when rights risk is material to the category and exposure |
| Device/IP telemetry | Do not impute adverse values; use available payment/account signals |
| Merchant financial capacity | Use a conservative uncovered-exposure assumption and request information |

## 11. Acceptance criteria

- Rates remain within schema bounds.
- Dollar and normalized views reconcile.
- Coin balances follow the confirmed expiry and transfer policy.
- Refund, fraud and dispute overlap is explicit.
- AI-02 remediation refunds are not automatically treated as worsening risk.
- AI-03 controls can target affected accounts without a merchant-wide block.
- Hard-rule cases cannot be offset by commercial value.
- Golden decisions are covered by tests.
