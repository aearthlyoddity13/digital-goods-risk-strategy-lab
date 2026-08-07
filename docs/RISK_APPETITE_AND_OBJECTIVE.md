# Risk appetite and commercial objective

**Version:** 0.1.0  
**Posture:** Balanced growth  
**Status:** Methodology foundation; thresholds remain illustrative

## 1. Policy statement

The hypothetical digital payment platform seeks to enable legitimate emerging digital-goods merchants while keeping fraud, disputes, contingent merchant exposure, compliance risk and operational cost within defined limits.

The platform does not treat uncertainty as equivalent to misconduct. When risk is potentially manageable, it prefers proportionate, reversible controls and evidence-building periods over immediate rejection. It does not trade away legal, sanctions, merchant-legitimacy or severe integrity requirements for payment volume.

## 2. Balanced-growth principles

1. **Legitimacy before growth.** Unresolved merchant identity, prohibited activity or sanctions concerns cannot be offset by commercial value.
2. **Control before decline when risk is remediable.** Monitoring, information requests, progressive limits, settlement delay and reserves should be considered before rejection.
3. **Exposure, not category labels, drives financial protection.** A digital-goods label is not itself a reason for a reserve.
4. **Newness is uncertainty, not guilt.** Short tenure lowers confidence and may justify progressive controls, but must not automatically imply severe risk.
5. **Commercial cost is part of risk strategy.** False positives, delayed settlement, reserve burden and review friction can damage legitimate merchants and reduce sustainable volume.
6. **Controls must have release conditions.** Every restrictive action requires measurable conditions for reduction or removal.
7. **Severe non-remediable risk overrides commercial value.** Illegal activity, confirmed sanctions exposure, material deception, deliberate laundering or unresolvable ownership concerns may justify decline or offboarding.
8. **Explainability is mandatory.** Decisions must identify evidence, assumptions, uncertainty, primary drivers and protective factors.

## 3. Risk-appetite matrix

| Risk family | Appetite | Balanced-growth interpretation | Default response |
|-------------|----------|--------------------------------|------------------|
| Merchant legitimacy and prohibited activity | Very low | Commercial potential cannot compensate for unresolved identity, illegal activity or intentional misrepresentation. | Information request, manual review, decline if unresolved or confirmed |
| Sanctions and restricted jurisdictions | Very low | A risk-based compliance program is required; confirmed prohibited exposure is outside appetite. | Screening, geographic restriction, manual review, decline where required |
| Fraud and account abuse | Low, controlled | Some fraud is inherent in digital commerce, but concentrated or accelerating loss must be controlled. | Monitoring, authentication/velocity controls, limits, reserve or review |
| Consumer conduct and subscriptions | Low to moderate if remediable | Disclosure, consent, cancellation and support weaknesses may be remediated; deliberate deception is outside appetite. | Practice review, remediation period, monitoring; restrict if unresolved |
| Disputes and refunds | Moderate within protected exposure | Normal customer disputes can be accepted when trends are stable and the merchant can cover obligations. | Monitoring; reserve/settlement control when exposure is unprotected |
| Prepaid and outstanding obligations | Moderate when measured and funded | Coins, credits and subscriptions are supportable when obligations are transparent and protection scales with exposure. | Reporting, limits, reserve, settlement matching |
| Content and IP | Low to moderate if governed | Isolated remediable issues differ from systematic infringement, prohibited content or absent governance. | Rights evidence, content review, remediation, restriction or decline for severe cases |
| Operational and external-platform dependency | Moderate | Early merchants may have concentrated dependencies; the platform can accept them with stress monitoring and exposure limits. | Monitoring, continuity information, progressive limits, reserve where loss-bearing |
| Data uncertainty | Moderate at low exposure; low at high exposure | Missing evidence is tolerable only when exposure is constrained. | Progressive limits, information request, manual review when volume is material |

## 4. Decision hierarchy

The demonstrator applies decisions in this order:

1. **Non-negotiable boundary check** — prohibited activity, sanctions, confirmed illegitimacy, deliberate laundering and severe non-remediable integrity events.
2. **Risk exposure assessment** — payment/fraud, consumer conduct, contingent exposure, content/compliance and operational interruption.
3. **Merchant strength assessment** — tenure, financial capacity, governance, fulfillment evidence, support, remediation capability and data confidence.
4. **Commercial-value assessment** — sustainable volume, platform revenue, growth potential, review cost and merchant-retention implications.
5. **Least-restrictive effective control selection** — choose the lowest-friction package expected to bring residual risk within appetite.
6. **Release and escalation conditions** — define when controls decrease, remain or increase.

Commercial value may influence control choice only after non-negotiable boundaries are satisfied.

## 5. Control ladder

Controls should generally be considered from lower to higher restriction, while matching the specific risk mechanism:

1. Standard monitoring
2. Enhanced monitoring
3. Additional merchant information
4. Subscription, content/IP or fulfillment-practice remediation
5. Transaction, corridor or product-specific controls
6. Progressive processing-volume limit
7. Settlement delay
8. Rolling reserve
9. Manual review before further expansion
10. Temporary restriction or suspension
11. Decline or offboarding

This is not a mechanical sequence. For example, sanctions or confirmed prohibited activity may bypass lower steps.

## 6. Commercial objective

The strategy seeks to maximize **expected control-adjusted platform contribution**, subject to non-negotiable compliance constraints and a defined residual-risk appetite.

### 6.1 Base contribution

```text
expected_base_contribution
  = expected_processed_volume × platform_take_rate
  − expected_fraud_loss
  − expected_dispute_and_refund_cost
  − expected_uncovered_merchant_exposure
  − expected_review_and_monitoring_cost
```

### 6.2 Control-adjusted contribution

```text
expected_control_adjusted_contribution
  = expected_base_contribution_after_controls
  − expected_false_positive_opportunity_cost
  − expected_merchant_friction_cost
```

### 6.3 Optimization statement

```text
Choose the control package that maximizes
expected_control_adjusted_contribution

subject to:
  non_negotiable_boundary_check = passed
  residual_fraud_risk <= appetite
  residual_dispute_exposure <= appetite
  residual_contingent_exposure <= appetite
  residual_content_and_compliance_risk <= appetite
```

The project will not claim that the synthetic output is economically optimal. The formula is an analytical structure for comparing strategies.

## 7. Three policy postures for demonstration

Every guided stress test should compare:

| Posture | Description | Expected trade-off |
|---------|-------------|--------------------|
| Permissive | Minimal friction and faster volume growth | Higher uncovered loss and interruption exposure |
| Balanced growth | Mechanism-specific controls with release conditions | Moderate residual risk and preserved legitimate growth |
| Conservative | Wider use of review, reserves, delays and limits | Lower exposure but higher false-positive and merchant-liquidity cost |

Balanced growth is the default recommendation. The other postures exist to reveal trade-offs, not to imply that one fixed policy fits every portfolio.

## 8. Control-effect channels

| Control | Primary benefit | Principal commercial cost |
|---------|-----------------|---------------------------|
| Enhanced monitoring | Earlier detection without immediate merchant restriction | Operating and tooling cost |
| Additional information | Reduces uncertainty | Onboarding delay and abandonment |
| Velocity/authentication control | Reduces automated and stolen-credential abuse | Customer friction and false declines |
| Processing limit | Caps unseasoned exposure | Foregone legitimate volume |
| Settlement delay | Keeps funds available during early loss emergence | Merchant working-capital pressure |
| Rolling reserve | Protects against refunds, disputes and negative balances | Liquidity burden and merchant dissatisfaction |
| Subscription-practice remediation | Reduces conduct complaints and renewal disputes | Product changes and possible short-term conversion decline |
| Content/IP review | Reduces interruption and rights exposure | Review delay and operational burden |
| Geographic restriction | Reduces sanctions/corridor exposure | Lost cross-border volume |
| Manual review | Resolves high-impact ambiguity | Cost, delay and inconsistent judgment risk |

## 9. Release conditions

Every control recommendation must include measurable release conditions. Examples:

- Sustained dispute, refund and complaint performance for a defined observation period
- Stable growth within an agreed processing band
- Improved data confidence
- Verified ownership or rights documentation
- Lower outstanding-obligation ratio
- Sufficient reserve coverage relative to exposure
- Completed subscription or cancellation remediation
- No new severe content, platform or sanctions events
- Demonstrated fulfillment and customer-support evidence

## 10. Governance constraints

- No protected-class or demographic variables.
- No sole reliance on IP address, geolocation, device or proxy/VPN status.
- Missing data must reduce confidence, not silently become adverse evidence.
- Hard rules require a documented policy rationale and test cases.
- Manual overrides require a reason code and audit entry.
- Policy changes require versioning, changelog entry and golden-scenario tests.
- Real calibration would require internal loss, settlement, dispute-timing and merchant-outcome data unavailable to this project.

## 11. Next methodology gate

The commercial calculation is specified in [COMMERCIAL_SIMULATION_SPEC.md](COMMERCIAL_SIMULATION_SPEC.md). The next stage must convert this posture into:

1. Separate risk, merchant-strength and commercial-value component definitions.
2. Synthetic cost and revenue assumptions.
3. Missing-data behavior.
4. Hard-rule eligibility criteria.
5. Control-effect assumptions.
6. Scenario-specific release and escalation logic.
