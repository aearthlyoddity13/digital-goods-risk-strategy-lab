# Portfolio case study — Digital Goods Merchant Risk Strategy Lab

**Owner:** Charlene Yang
**Status:** Interactive strategy-lab MVP
**Scope:** Employer-neutral digital payment platform; US-centered with cross-border considerations; direct web payments only
**Data boundary:** Aggregated and synthetic demonstration data only

## Executive thesis

Digital-goods merchant risk is not defined by ticket size or dispute rate alone. It emerges from interactions among payment behavior, fulfillment, prepaid customer obligations, merchant maturity, content integrity and the platform's ability to recover losses after settlement.

This project asks how a payment platform can protect against that exposure without suppressing legitimate growth. The demonstrator compares explainable control packages across short drama, AI services, web fiction and games, with deep dives into short-drama coin systems and AI subscriptions or credits.

## The decision problem

Physical-commerce controls often rely on shipping records, recoverable inventory and discrete fulfillment events. Digital products alter those assumptions:

- Access, content, virtual currency or compute can be consumed immediately.
- Low-ticket purchases can become material through high frequency.
- Unused coins, credits and subscription value remain customer obligations after payment.
- Disputes can arrive after the merchant has received settlement and after value has been consumed.
- Content, IP or external-platform events can interrupt fulfillment even when current payment metrics look stable.
- Reserves reduce platform exposure but can weaken merchant liquidity and sustainable growth.

The strategy must therefore answer two questions together: **what can go wrong, and what is the least-restrictive control that keeps the resulting exposure within appetite?**

## What I built

1. A MECE research-question tree covering legitimacy, conduct, fraud, contingent exposure, content/integrity, cross-border risk and control economics.
2. A digital-goods risk taxonomy connecting mechanisms to leading indicators, financial impact, controls and residual limitations.
3. Eight synthetic merchant scenarios across four observation periods, producing 32 versioned assessments.
4. An explainable decision engine returning risk exposure, merchant strength, commercial value, controls, reserve treatment, release conditions and escalation triggers.
5. A commercial simulator comparing permissive, balanced-growth and conservative policy postures.
6. A FastAPI interface and embeddable interactive lab with normalized and illustrative-dollar views.

## Decision architecture

The engine applies a defined hierarchy:

1. Check non-negotiable legitimacy, sanctions and prohibited-activity boundaries.
2. Assess payment/conduct, contingent exposure, content/dependency, cross-border and maturity/confidence mechanisms.
3. Evaluate merchant strength and protective evidence separately from risk.
4. Estimate commercial value and control-adjusted contribution.
5. Select among eligible policy postures using residual-risk appetite and ecosystem-adjusted value.
6. Prefer balanced growth when it is economically near-equivalent to a more restrictive posture.
7. Attach measurable release conditions and escalation triggers.

The posture comparison uses a probability-weighted uncovered-exposure assumption. It does not treat every dollar of outstanding customer obligation as an expected loss. Reserve liquidity burden is included when comparing ecosystem value, preventing reserve intensity from appearing costless.

## What the scenarios show

All values below are synthetic results for demonstration—not observed merchant performance or industry benchmarks.

| Scenario | Change tested | Risk score | Decision change | Reserve change | Monthly contribution change | Stress posture |
|---|---|---:|---|---:|---:|---|
| Viral cross-border short drama | Volume, cross-border share and obligations rise faster than evidence | 21.6 → 32.4 | Controls → Manual review | 5% → 10% | $7.0K → -$51.4K | Conservative |
| Post-consumption dispute deterioration | Complaints, disputes, integrity concerns and unused value worsen together | 17.3 → 47.3 | Controls → Manual review | 5% → 16% | $7.8K → -$20.2K | Conservative |
| AI account/API-key abuse | Fraud and disputes concentrate during an abuse event | 13.0 → 19.1 | Approve → Manual review | 0% → 10% | $17.4K → $5.7K | Conservative |
| Web-fiction creator obligations | Rights concerns and obligation coverage deteriorate jointly | 16.9 → 29.8 | Controls → Manual review | 5% → 13% | $13.1K → -$8.1K | Conservative |
| Transferable game items | Account abuse and post-transfer recoverability deteriorate | 23.2 → 29.8 | Controls → Manual review | 5% → 10% | $12.5K → -$5.4K | Conservative |

### Finding 1 — Interaction effects matter more than isolated thresholds

Several stress periods remain below a severe summary-score threshold but still require manual review because two mechanisms deteriorate together. Examples include fraud plus disputes, or content-integrity concerns plus material prepaid obligations. The model makes those interaction triggers visible instead of burying them inside one score.

### Finding 2 — Prepaid value is contingent exposure, not automatically a loss

Unused purchased coins and credits remain obligations until consumed or refunded, but only a probability-weighted uncovered gap enters expected contribution. This distinguishes exposure measurement from loss prediction and avoids overstating reserve benefits.

### Finding 3 — Healthy merchants should not inherit stress-period controls

Established AI subscription and credit scenarios remain on balanced growth throughout moderate operational stress because tenure, reliability, support and high data confidence remain protective. Web-fiction, games and API-abuse cases return to balanced growth after synthetic remediation.

### Finding 4 — Conservative controls should be temporary and mechanism-specific

Conservative treatment is selected during material stress, not as a permanent category label. The engine returns conditions for reducing controls: stable disputes and complaints, verified obligation coverage, improved evidence, and performance within agreed processing bands.

### Finding 5 — The economically highest-control posture is not automatically the best strategy

The simulator compares platform contribution, residual risk, false-positive cost and merchant liquidity burden. Balanced growth wins when its ecosystem-adjusted value is within a transparent near-equivalence band of a more restrictive eligible posture. Manual-review stress periods require the stronger case-specific result.

## Product and risk recommendations

- Underwrite monetization and fulfillment mechanics, not only merchant category.
- Track outstanding customer obligations separately from current disputes.
- Use progressive limits and monitoring while evidence matures.
- Link reserve intensity to recoverable exposure and release conditions.
- Combine payment indicators with customer-conduct and content-integrity signals where those mechanisms can interrupt fulfillment.
- Preserve human review for high-impact ambiguity and combined deterioration.
- Measure control cost through approval opportunity, operating expense and merchant liquidity—not loss reduction alone.

## Technical implementation

- Python domain layer with Pydantic contracts
- FastAPI strategy endpoints
- Versioned YAML scenarios and posture assumptions
- Normalized per-$100 and configurable illustrative-dollar calculations
- HTML, CSS and JavaScript interactive lab designed for portfolio embedding
- Automated unit, contract, lint and type checks

## Limitations

- No confidential merchant, customer or payment-platform data is used.
- Thresholds, control effects, loss probabilities and dollar results are synthetic.
- The project demonstrates methodology and product judgment; it does not claim predictive accuracy or an optimal production reserve.
- Real deployment would require internal loss and settlement data, legal review, model-risk governance, fairness testing and controlled experimentation.

## My contribution

I defined the product question, research structure, taxonomy, risk appetite, scenario architecture, decision logic, commercial simulation, API, test suite, interactive interface and portfolio narrative.

## Supporting material

[Project overview](PROJECT_OVERVIEW.md) · [Research report](RESEARCH_REPORT.md) · [Risk taxonomy](DIGITAL_GOODS_RISK_TAXONOMY.md) · [Decision policy](DECISION_POLICY.md) · [Commercial simulation](COMMERCIAL_SIMULATION_SPEC.md) · [Model card](MODEL_CARD.md) · [API specification](API_SPECIFICATION.md)
