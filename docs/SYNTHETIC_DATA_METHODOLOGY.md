# Synthetic data methodology

**Version:** 0.2.0-draft  
**Seed (planned generator):** `42`  
**Disclaimer (required on every data file and UI):**  
Demonstration data: aggregated and synthetic. No confidential merchant, customer or payment-platform data is used.

---

## 1. Purpose

Create transparent merchant **archetypes** and **multi-period scenarios** that illustrate how digital-goods risk drivers interact. Data exist to teach strategy—not to estimate real portfolio loss rates.

## 2. Design principles

1. Aggregated merchant-level variables only (no customer PII).  
2. Deterministic given seed and versioned generator.  
3. Explicit scenario labels: `normal`, `growth`, `stress`, `deterioration`.  
4. Documented assumptions; never presented as observed platform performance.  
5. Visible synthetic-data disclosure on files and interfaces.

## 3. Archetypes (target set)

The active scenario catalog is [SYNTHETIC_SCENARIO_CATALOG.md](SYNTHETIC_SCENARIO_CATALOG.md). Primary payment flows are direct web payments; app-store billing is outside the modeled transaction scope.
Initial numerical assumptions and expected balanced-growth decisions are documented in [SCENARIO_CALIBRATION_SPEC.md](SCENARIO_CALIBRATION_SPEC.md).

| ID | Archetype | Behaviors illustrated |
|----|-----------|----------------------|
| `ARCH-DRAMA-COINS` | Early-stage short-drama web merchant with coin unlocks | Low ticket, high frequency, prepaid coins |
| `ARCH-FICTION-CREATORS` | Established web-fiction with creator payouts | Subscriptions + creator payables |
| `ARCH-GAME-GIFTING` | Web game store with virtual currency and gifting | Transferability, ATO/gifting risk |
| `ARCH-AI-SUB-TRIAL` | AI image service: free trial + monthly sub | Trial abuse, renewal disputes |
| `ARCH-AI-API-USAGE` | Usage-based AI API | Volatile compute, volume spikes |
| `ARCH-GROWTH-XBORDER` | High-growth cross-border digital merchant | Growth × thin history × corridors |
| `ARCH-MATURE-SUB` | Mature low-risk digital subscription | Protective factors / approve path |
| `ARCH-DETERIORATE-CB` | Complaint and chargeback deterioration event | Metric drift over periods |

## 4. Variable families

See [DATA_DICTIONARY.md](DATA_DICTIONARY.md). Core groups: profile, volume/growth, ticket/frequency, monetization structure, payment quality, integrity/content, exposure/obligations, controls in force, data confidence.

## 5. Construction method

**Phase 2 (docs):** schemas and methodology frozen.  
**Phase 3 (engine):** hand-authored baseline periods per archetype, then deterministic transforms:

| Scenario | Transform intent |
|----------|------------------|
| `normal` | Baseline operating state |
| `growth` | ↑ volume, ↑ new customers, mild payment stress |
| `stress` | ↑ volatility, ↑ cross-border, ↑ refunds; tenure unchanged |
| `deterioration` | ↑ disputes/complaints/content-risk; possible reliability drop |

Assumptions (demonstration):

- Chargeback and refund rates are monthly aggregates, not scheme-reported exacts.  
- `content_risk_indicator` is an analyst-style index (0–1), not a moderation model score.  
- `outstanding_customer_obligation` proxies prepaid + unused subscription value.  
- Correlations are illustrative (e.g., gift features co-move with transferability risk).

## 6. What scenarios are intended to teach

1. Healthy high growth can still warrant progressive controls.  
2. Low ticket ≠ low risk when frequency and retries rise.  
3. Moderate payment metrics can still force review when content/integrity deteriorates.  
4. Prepaid exposure matters even when current CB is low.  
5. Protective factors (tenure, low concentration, strong reliability) can offset some stress.

## 7. Limitations

Not sampled from any real processor portfolio. Not suitable for calibrating production thresholds. Not for fairness assessments across protected classes (no demographic features).
