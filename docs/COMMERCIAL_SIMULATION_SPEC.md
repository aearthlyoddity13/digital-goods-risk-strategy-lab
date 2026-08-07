# Commercial simulation specification

**Version:** 0.2.0  
**Status:** Methodology specification  
**Default merchant:** Synthetic merchant with USD 1,000,000 monthly attempted payment volume

## 1. Purpose

The simulator compares how permissive, balanced-growth and conservative control packages affect both platform risk and commercial outcomes. It provides two synchronized views:

1. **Normalized view** — results per USD 100 of attempted payment volume.
2. **Illustrative dollar view** — results for a configurable synthetic merchant, defaulting to USD 1,000,000 of monthly attempted payment volume.

All prices, rates, costs and behavioral responses are demonstration assumptions. They are not estimates of any payment company’s actual economics.

## 2. User-configurable inputs

### Merchant economics

| Input | Default | Purpose |
|-------|---------|---------|
| Monthly attempted payment volume | USD 1,000,000 | Scale for dollar results |
| Platform revenue rate | 2.50% | Synthetic gross platform revenue per successfully processed dollar |
| Baseline payment approval rate | 96.0% | Converts attempted to approved volume before strategy effects |
| Successful fulfillment rate | 99.0% | Separates approved payments from successfully fulfilled volume |
| Baseline refund rate | 3.0% | Customer refunds as share of approved volume |
| Baseline dispute rate | 0.80% | Disputed volume as share of approved volume |
| Baseline fraud-loss rate | 0.35% | Expected fraud loss as share of approved volume |
| Merchant data-confidence level | Medium | Affects uncertainty and control intensity |

### Cost assumptions

| Input | Default | Treatment |
|-------|---------|-----------|
| Net loss severity on disputed volume | 70% | Portion of disputed principal expected to remain a platform/merchant economic loss in the demonstration |
| Incremental dispute operating cost | USD 15 per dispute | Synthetic handling and fee proxy; separate from disputed principal |
| Average transaction size | USD 20 | Converts volume rates into approximate transaction counts where needed |
| Automated monitoring cost | USD 500 per month | Fixed demonstration cost for enhanced monitoring |
| Manual review cost | USD 75 per reviewed case | Synthetic labor/operations assumption |
| Merchant annual liquidity cost | 12% | Converts held funds and holding days into an illustrative merchant financing burden |

Defaults must remain editable in the interface and versioned in configuration. A visible disclosure must identify them as synthetic assumptions.

## 3. Strategy inputs

Each policy posture changes a limited number of interpretable levers:

| Lever | Meaning |
|-------|---------|
| Approval-rate change | Additional legitimate and suspicious volume allowed or blocked |
| Fraud-loss reduction | Expected change in fraud loss after controls |
| Dispute-rate reduction | Expected change after clearer practices, monitoring or intervention |
| Refund-rate change | May increase through proactive refunds while disputes decrease |
| Review volume | Number of merchant/customer cases requiring manual work |
| Fixed monitoring cost | Operational cost of the strategy |
| Reserve rate and holding period | Temporary merchant liquidity burden; not an immediate platform expense |
| Settlement delay | Additional merchant liquidity burden and exposure protection |
| Uncovered-exposure reduction | Expected reduction in loss not covered by balances, reserves or delayed settlement |

Strategy effects are demonstration assumptions and must be displayed, not hidden inside code.

## 4. Volume waterfall

```text
attempted_volume
  = user input

approved_volume
  = attempted_volume × control_adjusted_approval_rate

successfully_fulfilled_volume
  = approved_volume × fulfillment_rate

refunded_volume
  = approved_volume × control_adjusted_refund_rate

disputed_volume
  = approved_volume × control_adjusted_dispute_rate

sustainable_payment_volume
  = successfully_fulfilled_volume
    − refunded_volume
    − disputed_volume
```

The interface must show this waterfall so users can see where volume is lost. Removing refunded or disputed volume from `sustainable_payment_volume` reverses the associated platform-revenue base; it does not by itself assume that the platform loses the transaction principal. Refund principal is treated as funded by the merchant unless a scenario explicitly creates uncovered exposure. Disputed principal becomes a platform loss only to the extent represented by `net_dispute_loss_severity` and not recovered from the merchant, reserves or other balances.

## 5. Platform contribution

### Gross platform revenue

```text
gross_platform_revenue
  = sustainable_payment_volume × platform_revenue_rate
```

### Expected loss and operating cost

```text
expected_fraud_loss
  = approved_volume × control_adjusted_fraud_loss_rate

expected_dispute_principal_loss
  = disputed_volume × net_dispute_loss_severity

expected_dispute_operating_cost
  = estimated_dispute_count × dispute_operating_cost_per_case

expected_operating_cost
  = monitoring_cost
    + manual_review_cost
```

Fraud and dispute assumptions must be configured to avoid double counting. If fraudulent transactions are already represented inside disputed volume for a scenario, the scenario must specify the overlap and calculate only the incremental loss.

### Expected uncovered merchant exposure

```text
expected_uncovered_exposure
  = max(0,
      gross_contingent_exposure
      − available_merchant_balance
      − usable_reserve_protection
      − other_recoverable_amounts)
    × contingent_exposure_realization_rate
```

The result cannot fall below zero. The realization rate is a synthetic scenario-horizon probability, not an observed default rate. This prevents the model from treating every uncovered obligation as an immediate expected loss.

### Platform contribution before merchant-friction effects

```text
platform_contribution_before_friction
  = gross_platform_revenue
    − expected_fraud_loss
    − expected_dispute_principal_loss
    − expected_dispute_operating_cost
    − expected_operating_cost
    − expected_uncovered_exposure
```

## 6. Opportunity and merchant-friction costs

### False-positive opportunity cost

```text
false_positive_blocked_volume
  = attempted_volume
    × estimated_legitimate_share_of_incrementally_blocked_volume

false_positive_opportunity_cost
  = false_positive_blocked_volume
    × expected_net_contribution_margin_on_legitimate_volume
```

### Reserve liquidity burden

```text
average_reserved_funds
  = approved_volume × reserve_rate

reserve_liquidity_burden
  = average_reserved_funds
    × merchant_annual_liquidity_cost
    × holding_days / 365
```

A reserve is not treated as a platform expense or merchant loss merely because funds are held. Only its estimated liquidity burden is shown as friction.

### Settlement-delay liquidity burden

```text
settlement_delay_burden
  = delayed_settlement_amount
    × merchant_annual_liquidity_cost
    × additional_delay_days / 365
```

Reserve and settlement burdens must not be double counted when they apply to the same funds and period. The implementation should calculate the incremental burden of each layer.

## 7. Control-adjusted contribution

```text
expected_control_adjusted_platform_contribution
  = platform_contribution_before_friction
    − false_positive_opportunity_cost
```

Merchant liquidity burden is reported beside platform contribution rather than automatically deducted from platform profit. It affects the qualitative merchant-sustainability assessment and may be included in an optional broader ecosystem-value view.

### Ecosystem-adjusted value used for posture selection

```text
ecosystem_adjusted_value
  = expected_control_adjusted_platform_contribution
    − merchant_liquidity_burden
```

Among postures within residual-risk appetite, the demonstrator prefers balanced growth when its ecosystem-adjusted value is within 0.50% of monthly attempted volume of the highest-value eligible posture. Manual-review stress periods use the highest case-specific ecosystem-adjusted value. This is an explicit synthetic policy preference for the least-restrictive near-equivalent control package, not an optimization claim.

## 8. Required normalized outputs

For every USD 100 of attempted volume, show:

- Approved volume
- Sustainable payment volume
- Gross platform revenue
- Expected fraud loss
- Expected dispute-related loss and operating cost
- Expected uncovered exposure
- Review and monitoring cost
- False-positive opportunity cost
- Expected control-adjusted platform contribution
- Funds reserved
- Merchant reserve/settlement liquidity burden

## 9. Required dollar outputs

For the default USD 1,000,000 monthly synthetic merchant, show the same metrics in dollars plus:

- Approximate monthly transaction count
- Approximate dispute count
- Reserve amount
- Holding period
- Settlement delay
- Total monthly operating cost
- Contribution difference versus the no-control baseline
- Contribution difference versus the balanced-growth strategy

## 10. Comparison presentation

The simulator must display the three postures side by side:

| Output | Permissive | Balanced growth | Conservative |
|--------|------------|-----------------|--------------|
| Sustainable volume | — | — | — |
| Expected platform contribution | — | — | — |
| Expected fraud/dispute loss | — | — | — |
| Expected uncovered exposure | — | — | — |
| False-positive opportunity cost | — | — | — |
| Merchant liquidity burden | — | — | — |
| Residual-risk posture | — | — | — |

Balanced growth is the default highlighted strategy, but the interface must allow another strategy to perform better in a particular scenario. The conclusion must follow the assumptions rather than being hard-coded.

## 11. Sensitivity analysis

At minimum, support sensitivity tests for:

- Attempted payment volume
- Platform revenue rate
- Approval-rate impact
- Fraud-loss rate
- Dispute rate and loss severity
- Refund rate
- Prepaid/outstanding-obligation ratio
- Reserve rate
- Holding period
- Merchant liquidity cost
- Manual-review rate and unit cost
- Data confidence

## 12. Guardrails

- Never label a default as an industry average unless supported by appropriate evidence.
- Never label the selected reserve as optimal.
- Keep rates, counts and dollar amounts traceable through a calculation breakdown.
- Show when an output is especially sensitive to an assumption.
- Prevent negative volumes, rates outside permitted ranges and reserve protection above eligible exposure.
- Make overlap assumptions among fraud, disputes and refunds explicit.
- Round only for display; calculate with full precision.
- Include methodology and assumption version identifiers in API responses.

## 13. Acceptance criteria

- Normalized and dollar views reconcile mathematically.
- USD 1,000,000 is a default, not a fixed volume.
- Changing volume scales dollar results while normalized rates remain consistent unless a scenario includes scale effects.
- Refund, dispute and fraud losses are not double counted.
- Reserve principal is not presented as a cost.
- Reserve and settlement liquidity burdens do not overlap.
- All defaults are visibly synthetic and editable.
- Each strategy shows both risk reduction and commercial friction.
