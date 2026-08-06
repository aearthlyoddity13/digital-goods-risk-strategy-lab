# Validation plan

**Status:** Planned for Phase 2  
**Owner:** Charlene Yang

## Objectives

Measure discrimination, calibration, and commercial outcomes of the baseline engine on synthetic vintages with out-of-time holdout.

## Design

1. Generate synthetic merchant vintages with documented feature–outcome links and drift ([synthetic_data_spec.md](synthetic_data_spec.md)).  
2. Split **by time**: earlier vintages for development; later for holdout.  
3. Metrics: AUC/Gini, calibration plots/tables, Brier score, score-band adverse-event and loss rates, approval rate, realized vs expected loss, reserve coverage, manual-review rate.  
4. Sensitivity: thresholds, PD, LGD, exposure, reserve floor/cap, cost/revenue assumptions.  
5. Document label delay, missingness, stability, leakage controls, and synthetic limitations.

## Exit criteria

Reproducible metrics from repository commands; limitations documented; no unsupported effectiveness claims.

## Current status

Not started. Baseline remains illustrative.
