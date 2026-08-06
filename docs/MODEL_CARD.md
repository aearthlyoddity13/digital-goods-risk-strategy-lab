# Model card — Digital Goods Merchant Risk Strategy Lab

**Methodology version:** `strategy-0.2.0-draft`  
**Policy version:** `policy-strategy-0.2.0` (draft)  
**Status:** Strategy demonstrator — not a production model

## Required disclosures

- This is a **strategy demonstrator**, not a production model.  
- Data are **aggregated and synthetic**.  
- **No confidential** platform or merchant data are used.  
- Thresholds are **illustrative**.  
- Results should **not** be used for real merchant decisions.  
- Production deployment would require **internal** loss, dispute, settlement, and merchant-performance data.  
- **Fairness, regulatory, legal, and model-risk reviews** would be required before any production use.

## Intended use

Education and portfolio demonstration of digital-goods merchant risk strategy for payment platforms: research framing, taxonomy, scenario analysis, and explainable control recommendations.

## Out of scope

Live underwriting; predictive accuracy claims; automated content moderation; AML case management; autonomous adverse action.

## Inputs / outputs

See [DATA_DICTIONARY.md](DATA_DICTIONARY.md). Primary outputs are decision, risk level, drivers, protective factors, controls, illustrative reserve, escalation/reduce conditions, confidence, versions, disclaimer, limitations.

## Methodology summary

Interaction-aware rules and transparent score components configured in versioned YAML. Hard integrity and extreme-payment rules can override score bands. Reserve bands are illustrative policy outputs.

## Human oversight

`MANUAL_REVIEW` and control recommendations assume human judgment. This lab does not automate final production credit decisions.

## Metrics

No AUC/Gini or calibrated loss metrics are claimed. Prior v0 PD/LGD/EAD framing is archived and not part of the primary demonstrator surface.

## Limitations

See [LIMITATIONS_AND_ETHICS.md](LIMITATIONS_AND_ETHICS.md).
