# P1 Version 2 content and model plan

**Project:** Digital Goods Merchant Risk Strategy Lab  
**Owner:** Charlene Yang  
**Status:** Approved direction; implementation pending  
**Primary objective:** Build a coherent, employer-facing demonstration of how a payment platform could adapt risk strategy for emerging web-based digital goods without proprietary merchant data.

## 1. Research question

How should a digital payment platform evaluate and control merchants selling emerging digital goods when subscriptions, credits, token plans, instant consumption and content-dependent fulfillment create exposures that conventional physical-goods controls do not represent well?

## 2. Thesis to test

Digital-goods risk is not simply higher or lower than physical-goods risk. It is structurally different. The payment platform should diagnose the merchant's business model, transaction lifecycle, customer obligation and fraud mechanism, then choose targeted controls that preserve legitimate growth while keeping expected loss and stressed exposure within explicit constraints.

This is a hypothesis for structured demonstration, not an empirical claim about any named payment platform.

## 3. Decision objective

Recommend the least restrictive viable control package that maximizes control-adjusted contribution subject to:

- expected-loss tolerance;
- stressed-exposure coverage;
- hard policy boundaries;
- operational-review capacity;
- merchant-liquidity and customer-experience constraints.

Never collapse growth and risk into one unexplained score. Display revenue opportunity, expected loss, contingent exposure, control cost and contribution separately.

## 4. Analytical pipeline

| Stage | Required output | Quality gate |
|---|---|---|
| Problem | Business-model gap versus physical goods | Names the affected transaction or obligation mechanism |
| Architecture | Eligibility, diagnosis, exposure, controls, optimization and explanation | Every component has an explicit role and input |
| Evidence | Sources, original inferences and synthetic assumptions | All three evidence classes are visibly separated |
| Demonstration | Paired scenarios, interactions and 30/60/90-day sensitivity | Variables changed and held constant are documented |
| Conclusion | Supported findings, caveats and real-data validation plan | No conclusion exceeds the demonstration evidence |

## 5. Scope

**Comparative categories:** short drama, web fiction, games and AI services.  
**Deep dives:** short-drama coin systems and AI subscriptions/credits.  
**Channel:** direct web payments. App-store purchases are excluded.  
**Data:** synthetic merchant scenarios and clearly labeled configurable assumptions.  
**Illustrative scale:** $1 million monthly payment volume, with per-$100 normalization available.

## 6. Work entry specification

The Work page proves technical and analytical execution. Its narrative sequence is:

1. Decision brief.
2. Why physical-goods assumptions break.
3. Risk-mechanism taxonomy.
4. Input and assumption registry.
5. Decision-system architecture.
6. Exposure and reserve engine.
7. Mechanism-specific control library.
8. Balanced-growth optimization.
9. Synthetic scenario design.
10. Results, sensitivity and counterfactuals.
11. API, testing and reproducibility.
12. Limitations and proprietary-data validation plan.

Primary evidence objects:

- architecture diagram;
- assumption registry;
- risk-mechanism-to-signal map;
- exposure waterfall for 30/60/90 days;
- control-effect and cost matrix;
- paired-scenario results;
- decision counterfactual;
- sensitivity chart;
- live API and test summary.

## 7. Insight entry specification

The Insight page proves business judgment and sector understanding. Its narrative sequence is:

1. Executive insight.
2. What changes when the product is digital.
3. Business-model comparison.
4. Fraud and abuse taxonomy.
5. Deep dive: short-drama coins.
6. Deep dive: AI subscriptions and credits.
7. Implications for payment platforms.
8. Growth-versus-control principles.
9. What the P1 system operationalizes.
10. Boundaries and open questions.

The fraud taxonomy should distinguish at minimum:

- stolen credentials and account takeover;
- first-party misuse and friendly fraud;
- subscription and renewal disputes;
- credit or token laundering and promotional abuse;
- bot-driven consumption or resource exhaustion;
- content-rights, deceptive-content and availability risk;
- non-delivery, access interruption and metering mismatch;
- merchant collusion, transaction laundering or misrepresentation;
- cross-border evidence, localization and support gaps without treating geography itself as misconduct.

## 8. Required tests

- Test 30-, 60- and 90-day reserve horizons.
- Run low/base/high loss severity, realization and dispute-lag assumptions.
- Use paired scenarios in which one mechanism changes and other inputs remain fixed.
- Add interaction scenarios for high frequency plus low ticket size, prepaid obligations plus content interruption, and rapid growth plus weak evidence quality.
- Test whether different mechanisms with equal summary risk receive different controls.
- Report threshold proximity and whether each recommendation is robust or assumption-sensitive.
- Verify that a well-controlled cross-border merchant is not penalized solely for cross-border volume.

## 9. Definition of done

- Every major insight maps to a mechanism, evidence class and demonstrated result.
- Every reserve dollar maps to a stated exposure component and horizon.
- Every recommended control has applicability, assumed effect, cost and release condition.
- The API exposes the decision decomposition, binding constraint and minimum change needed for a less restrictive outcome.
- The Work and Insight pages add distinct value and cross-link cleanly.
- No proprietary-data, predictive-accuracy or employer-method claims appear.
- A risk-strategy recruiter can understand the business decision; a technical reviewer can inspect how it was implemented.

## 10. Next build sprint

1. Create the evidence and assumption registry.
2. Specify the exposure equation and reserve coverage logic for 30/60/90 days.
3. Replace generic posture multipliers with mechanism-specific controls.
4. Define the first paired cases for short-drama coins and AI credits.
5. Implement and test the revised API outputs.
6. Only then rewrite the public Work and Insight pages.
