# Synthetic data specification

**Version:** 0.1.0  
**Status:** Spec frozen before bulk generation. Phase 0 ships hand-crafted deterministic samples; Phase 2 adds vintage generators.

## Principles

1. Deterministic for a fixed seed.  
2. Documented relationships between features and outcomes (Phase 2).  
3. Never presented as observed production performance.  
4. No personal demographics; fairness claims out of scope.

## Sample merchants (Phase 0)

Four fixed fixtures in `data/sample/merchants.json`:

| ID | Intended action | Design intent |
|----|-----------------|---------------|
| `SYN-APPROVE-001` | APPROVE | Mature, verified, low loss rates, healthy buffer |
| `SYN-CONTROLS-001` | APPROVE_WITH_CONTROLS | Elevated growth/refund risk → reserve |
| `SYN-REVIEW-001` | MANUAL_REVIEW | Ambiguous mid-score / partial verification |
| `SYN-DECLINE-001` | DECLINE | Hard policy and/or extreme loss signals |

Generation method for these four: **hand-authored** JSON aligned to policy thresholds in `config/policy/policy-0.1.0.yaml`. Seed for future bulk generation: `42`.

## Planned Phase 2 generator (not implemented yet)

- Monthly vintages of synthetic merchants.  
- Latent risk factor → features with noise + temporal drift.  
- Labels delayed 90–180 days.  
- Development vs out-of-time holdout split **by time**, not random.

## Limitations

- Hand-authored samples prove plumbing and explainability, not discrimination.  
- Correlations are illustrative.  
- Label delay and missingness patterns are deferred to Phase 2 documentation updates.
