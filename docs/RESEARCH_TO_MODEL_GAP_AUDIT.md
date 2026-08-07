# Research-to-model gap audit

**Version:** 0.1.0
**Methodology target:** `strategy-0.4.0`
**Purpose:** Ensure the public research narrative and interactive engine describe the same decision system without converting every interesting signal into a score.

## Decision rule for adding an input

An indicator enters the quantitative engine only when it:

1. represents an aggregated mechanism rather than raw sensitive customer data;
2. has a distinct decision or control use;
3. can be varied coherently in a synthetic scenario;
4. changes an explanation, control or exposure calculation;
5. can be bounded and validated without claiming empirical calibration.

Indicators that fail these tests remain qualitative review evidence or out of scope.

## Gap disposition

| Research indicator | Previous representation | Disposition | Rationale |
|---|---|---|---|
| Purchased/consumed/refunded/unused AI credits | Generic prepaid ratio only | **Added quantitative ledger** | Reconciliation is decision-relevant and parallels the coin ledger without requiring customer-level data. |
| Promotional AI credits | Not explicit | **Added contextual quantitative field** | Separates merchant-funded incentives from customer-funded principal exposure. |
| Renewal disclosure | Documentation only | **Added quantitative analyst score** | Directly selects subscription-practice remediation; must not be treated as a legal conclusion. |
| Renewal-specific dispute share | Generic dispute rate | **Added quantitative interaction** | Distinguishes subscription conduct from unrelated fraud and fulfillment disputes. |
| Usage-meter reconciliation | Documentation only | **Added quantitative control input** | Selects meter reconciliation and combined manual-review trigger. |
| Anomalous usage concentration | Generic payment growth | **Added quantitative control input** | Supports usage/spend limits without requiring raw prompts or events. |
| Account/API-key compromise | Generic fraud-loss rate | **Added quantitative interaction** | Allows account/key-specific containment before merchant-wide restriction. |
| Postpaid usage exposure | Not explicit | **Added quantitative control input** | Captures merchant compute or service cost incurred before collection. |
| Upstream provider concentration | `platform_dependency` | **Retained existing field** | A second overlapping score would double count dependency. |
| Service reliability | Existing field | **Retained existing field** | Already affects merchant strength and scenario outcomes. |
| Content/IP complaint process | Content-integrity proxy | **Qualitative human-review evidence** | Legal and rights conclusions cannot be credibly automated in this demonstrator. |
| Raw API keys, prompts or outputs | Out of scope | **Remain out of scope** | Unnecessary, sensitive and inconsistent with the aggregated-data boundary. |
| Raw IP, device or geolocation records | Out of scope | **Remain out of scope** | The model uses only an aggregated abuse indicator; raw telemetry would create privacy and misuse risk. |
| Provider continuity-plan quality | Generic dependency proxy | **Qualitative human-review evidence** | Requires document review and judgment rather than a synthetic universal score. |
| Exact legal treatment of credits | Not modeled | **Remain outside model** | Product and jurisdiction-specific legal analysis requires counsel. |

## Implemented decision effects

### Renewal conduct

- Low disclosure clarity and high renewal-dispute concentration increase the payment-and-conduct component.
- Material renewal weakness selects `subscription_practice_review`.
- Renewal stress combined with customer complaints creates an explicit interaction uplift.
- Proactive-refund remediation can improve the renewal indicators even when the total refund rate temporarily rises.

### Account and API-key abuse

- A material compromise indicator selects `account_and_key_security_review`.
- High anomalous usage or postpaid exposure selects `usage_spend_limit`.
- Concentrated compromise, anomalous usage and fraud loss together require manual review.
- Recovery removes targeted controls when synthetic evidence improves.

### Usage-meter integrity

- A reconciliation rate below the policy threshold selects `usage_meter_reconciliation`.
- Severe meter divergence combined with complaints requires manual review.
- The rate is an aggregated reconciliation result, not raw customer usage.

### Service-credit ledger

```text
unused_service_credit_value
  = purchased_service_credit_value
    − consumed_service_credit_value
    − refunded_service_credit_value
```

The ledger validates customer-funded value. The existing `prepaid_exposure_ratio` remains the financial input to the reserve and contingent-exposure calculation, avoiding double counting.

## Scenario coverage

| Scenario | New mechanism made explicit | Expected model behavior |
|---|---|---|
| AI-01 | Strong disclosure, low renewal concentration, reconciled credit ledger | Approval and balanced growth remain stable. |
| AI-02 | Trial/renewal disclosure and dispute concentration, followed by remediation | Subscription-practice control appears during stress and recedes with evidence. |
| AI-03 | Key compromise, anomalous usage, metering divergence and postpaid exposure | Targeted controls and manual review during abuse; recovery returns to balanced growth. |

## Governance constraints

- No input is described as an industry benchmark.
- No raw customer content, key, device, IP address or location is stored.
- Renewal-disclosure scoring requires a documented analyst rubric before production consideration.
- Missing telemetry reduces confidence; it is not automatically assigned an adverse value.
- New fields require schema bounds, scenario coverage, explanation output and tests.
- A future production system would require privacy, legal, security, fairness and model-risk review.
