# P1 analytical credibility audit

**Date:** 2026-08-14  
**Scope:** Decision methodology, synthetic scenarios, reserve logic, commercial comparison, explanations and employer-facing evidence  
**Current state:** Strong strategy demonstrator; not yet analytically mature enough to imply calibrated decision science

## Executive assessment

P1 already demonstrates valuable product and engineering capability: a coherent problem definition, versioned scenarios, explainable outputs, a tested API and a usable interactive lab. Its next improvement should not be more categories, controls or interface features. The highest-return work is to make the existing decision logic more internally defensible.

The core weakness is that several outputs are produced by fixed weights, thresholds and posture multipliers that encode the desired narrative directly. This is acceptable for an explicitly synthetic demonstrator, but a sophisticated reviewer may ask whether the engine is discovering a trade-off or merely restating assumptions. Version 2 should therefore emphasize **assumption transparency, exposure mechanics, sensitivity and counterfactual decisions**.

## Locked project thesis and audience

**Primary research question:** How should a digital payment platform adapt merchant-risk decisions when emerging digital goods create business models, fulfillment mechanics and contingent obligations that traditional physical-goods controls do not represent well?

**Business objective:** Support the growth of legitimate digital-goods merchants while keeping expected loss, contingent customer obligations and operational burden within explicit risk constraints.

**Primary reviewers:** Risk Strategy, Payment Risk, Risk Analyst, Quantitative Risk Strategy and Portfolio Risk internship hiring teams. The project should remain employer-neutral and must not imply use of proprietary payment-platform methods or data.

**Flagship categories:** Comparative coverage across short drama, web fiction, games and AI services; deeper demonstrations for short-drama coin systems and AI subscriptions/credits. Web payments only; app-store purchases are out of scope.

**Core analytical pipeline:**

1. Problem — identify where physical-goods assumptions fail for digital SKUs.
2. Architecture — translate those differences into mechanisms, exposures, controls and decision constraints.
3. Evidence — distinguish sourced industry observations, original inference and synthetic assumptions.
4. Demonstration — test the framework with controlled synthetic scenarios and sensitivity ranges.
5. Conclusions — state what the demonstration supports, what remains uncertain and what a real platform would validate with proprietary data.

The public narrative must follow this pipeline in order. A conclusion cannot appear unless the page shows the mechanism and demonstration that support it.

## What is already credible

- Clear data boundary: aggregated synthetic inputs only.
- Appropriate separation between hard policy boundaries and scored risk.
- Risk, merchant strength and commercial value are displayed separately.
- Short-drama coins and AI credits have explicit reconciliation rules.
- Combined deterioration can trigger human review before an aggregate score becomes severe.
- Controls have release conditions rather than permanent category treatment.
- The API, versioned configuration and automated tests make the methodology inspectable.
- The project avoids predictive-accuracy claims.

## Priority findings

### P0 — Replace reserve-by-decision with exposure-based reserve design

**Current issue:** Reserve rates begin with fixed amounts based on the decision label—5% for approve-with-controls and 10% for manual review—then receive simple uplifts. Reserve amount is calculated as a percentage of approved volume. The relationship between the selected reserve and the actual customer-obligation gap is therefore indirect.

**Why it matters:** The project’s strongest thesis is that digital-goods reserves should respond to contingent exposure. The implemented formula should visibly support that thesis.

**Required redesign:**

1. Define a protection target over a selected risk horizon.
2. Calculate expected and stressed recoverable exposure separately.
3. Recognize available merchant balance, current reserve and expected settlement inflows.
4. Size incremental protection to the target coverage gap.
5. Convert the dollar requirement into a reserve rate subject to transparent floors, caps and liquidity constraints.
6. Return a decomposition: obligation, expected realization, available protection, target gap and recommended reserve.

**Success test:** A reviewer can trace every recommended reserve dollar back to an exposure component rather than a decision label.

### P0 — Rebuild policy postures as control packages, not generic multipliers

**Current issue:** Permissive, balanced-growth and conservative postures apply universal multipliers to approval, fraud, disputes and refunds. The same effect pattern is used across distinct mechanisms.

**Why it matters:** Account compromise, renewal conduct, prepaid obligations and content interruption should not respond identically to the same posture.

**Required redesign:**

- Define mechanism-specific controls: authentication/velocity, subscription remediation, processing bands, settlement delay, rolling reserve, evidence retention, metering reconciliation and human review.
- Give each control an explicit assumed effect vector, cost, latency and applicability condition.
- Construct each posture as a selectable package of those controls.
- Show which assumptions drive the recommendation.
- Preserve synthetic labels; do not present control effects as empirical estimates.

**Success test:** Two merchants with equal summary risk but different mechanisms receive different control packages and economics.

### P0 — Remove cross-border share as an intrinsic risk score

**Current issue:** Cross-border share contributes directly and linearly to risk.

**Why it matters:** Geographic reach is not itself misconduct or loss. Treating it as a generic adverse factor is analytically weak and may encode an unjustified proxy.

**Required redesign:** Treat cross-border activity as an exposure context that interacts with specific factors such as corridor mismatch, localization quality, sanctions restrictions, support capacity, settlement currency, dispute evidence and data confidence. Preserve confirmed sanctions prohibitions as a hard policy boundary.

**Success test:** A mature, well-controlled cross-border merchant is not penalized merely because its international share is high.

### P1 — Strengthen commercial value beyond volume and growth

**Current issue:** Commercial value is primarily a function of monthly volume and month-over-month growth. This makes fast-growing, high-volume merchants appear valuable even when contribution, retention or durability is poor.

**Required redesign:** Separate:

- gross revenue opportunity;
- contribution after losses and operating cost;
- durability or retention evidence;
- concentration and dependency exposure;
- strategic value, if used, as a clearly qualitative field.

Do not combine these into a single opaque score unless the weights are shown.

### P1 — Add counterfactual and marginal-decision explanations

The engine currently returns drivers and general release conditions. Add:

- `Why this decision rather than the next-less-restrictive decision?`
- `Which binding constraint prevented approval?`
- `What minimum synthetic change would alter the decision?`
- `How much does each proposed control change residual exposure and contribution?`

This converts explainability from a list of reasons into a decision tool.

### P1 — Add sensitivity and robustness analysis

Every flagship scenario should show:

- one-way sensitivity for the 3–5 most influential assumptions;
- threshold proximity;
- stable versus fragile decisions;
- a low/base/high realization-rate range;
- whether the recommended posture changes under plausible assumption variation.

The public conclusion should distinguish “robust within the synthetic range” from “dependent on one assumption.”

### P1 — Improve scenario construction discipline

The four-period narratives are useful but several variables change together by author choice. Add a scenario manifest that identifies:

- mechanism being tested;
- variables intentionally changed;
- variables held constant;
- causal story being illustrated;
- expected directional result before running the engine;
- alternative explanation;
- falsification or inconsistency check.

Use paired scenarios where only one mechanism differs, followed by interaction scenarios. This will make the demonstrations more diagnostic.

### P2 — Add time and loss-lag mechanics

The current monthly view compresses authorization, consumption, settlement, dispute and reserve release into one period. Add a simple cohort timeline or monthly vintage view for:

- attempted and approved payments;
- value consumed;
- unused customer obligation;
- dispute arrival;
- settlement already released;
- reserve held and released.

This is particularly important for the project’s contingent-exposure thesis.

### P2 — Clarify the status of content and integrity signals

Keep content and rights indicators as human-review evidence. Avoid implying automated legal or moderation conclusions. Introduce evidence quality, recency and analyst confidence instead of adding more content-risk scoring detail.

## Recommended Version 2 decision architecture

1. **Eligibility boundary** — verified hard constraints only.
2. **Mechanism diagnosis** — payment fraud, conduct, fulfillment, contingent obligation, continuity/dependency and evidence uncertainty.
3. **Exposure engine** — expected and stressed dollar exposure by time horizon.
4. **Control library** — applicable mechanism-specific interventions and assumed effects.
5. **Constrained optimization** — minimize expected platform loss and merchant friction subject to risk appetite and policy constraints.
6. **Counterfactual explanation** — binding constraint, marginal control benefit and release condition.
7. **Sensitivity layer** — robustness of the result to synthetic assumptions.

## Version 2 delivery sequence

| Sprint | Deliverable | Acceptance criterion |
|---|---|---|
| 1 | Research-question map, assumption registry and revised exposure/reserve specification | Every output maps to the analytical pipeline; every reserve output has a dollar decomposition and horizon. |
| 2 | Mechanism-specific control-effect matrix | No universal posture multiplier remains. |
| 3 | Paired scenarios and interaction tests | Each key mechanism has an isolated and combined test. |
| 4 | Counterfactual and sensitivity API outputs | API explains binding constraints and decision robustness. |
| 5 | Interactive lab revision | Users can inspect exposure, control effects and sensitivity without entering real data. |
| 6 | Employer-facing Work and Insight refresh | The two entries are mutually exclusive, cross-linked and supported by the same validated analytical backbone. |

## Locked modeling decisions

- Use a formal balanced-growth objective: maximize control-adjusted contribution subject to explicit loss, exposure, policy and merchant-friction constraints. Report contribution and loss separately rather than hiding the trade-off inside one score.
- Test 30-, 60- and 90-day horizons. Do not select a preferred horizon by intuition. The recommendation should follow the synthetic obligation duration, settlement timing and dispute-lag assumptions, with sensitivity results visible.
- Model reserve liquidity cost both as a platform economics input and a merchant-welfare constraint.
- Optimize the narrative primarily for payment-risk and risk-strategy reviewers, while retaining inspectable quantitative and engineering evidence.
- Public capability evidence should emphasize Python, the API implementation, scenario design, Excel-based financial reasoning and reproducible AI-assisted development. Avoid unsupported claims of production-grade machine learning or proprietary industry calibration.

## Guardrails

- Do not add machine learning solely for sophistication; there is no legitimate training dataset.
- Do not scrape or fabricate merchant-level observations and present them as evidence.
- Do not optimize synthetic thresholds to produce preferred decisions.
- Do not expand to more merchant categories until the two flagship mechanisms are analytically stronger.
- Continue separating industry evidence, original inference and demonstration assumptions.
