# Model card — Transparent digital-merchant scorecard

**Model version:** `scorecard-0.1.0`  
**Policy version paired:** `policy-0.1.0`  
**Validation status:** **Illustrative baseline — not validated**

## Intended use

Support merchant-level onboarding/periodic-review decisions for synthetic digital-product merchants in this portfolio demonstration. Informs APPROVE / APPROVE_WITH_CONTROLS / MANUAL_REVIEW / DECLINE and rolling-reserve recommendations.

## Out of scope

Production underwriting; real customer data; AML; autonomous adverse action; fairness claims on protected classes.

## Inputs / outputs

See [data_dictionary.md](data_dictionary.md). Outputs include risk score, PD, LGD, EAD, EL, reserve, reason codes, hard flags, versions, assumptions.

## Methodology (summary)

Bounded component scorecard (0–100) across viability, payment quality, growth, product structure, behavior, and geography. Logistic calibration maps score → PD. EAD from projected TPV × exposure days factor. LGD from industry/product priors adjusted by recovery-related signals. EL = PD × LGD × EAD. Hard policy rules applied after scoring.

## Human oversight

Manual-review triggers and `requires_human_review` flag. Overrides are structured in domain types for later API persistence (Phase 1+).

## Limitations

- Coefficients are expert-illustrative, not fitted to production losses.  
- Synthetic samples only.  
- Do not cite AUC/Gini or loss rates as predictive proof until [validation_report.md](validation_report.md) contains Phase 2 evidence.
