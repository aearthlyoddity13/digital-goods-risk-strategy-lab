# ADR-003: Reposition to Digital Goods Merchant Risk Strategy Lab

**Status:** Accepted  
**Date:** 2026-08-06  
**Deciders:** Charlene Yang (portfolio owner)

## Context

Sprint 0 delivered an explainable credit/reserve engine with PD/LGD/EAD framing. The revised portfolio brief requires a **research-led strategy demonstrator** that:

- does not imply possession of processor or merchant-confidential data;  
- centers industry research, taxonomy, and content-risk strategy;  
- uses synthetic aggregated scenarios;  
- presents rules-and-score logic without predictive-accuracy claims.

Continuing the credit-engine narrative creates positioning risk for recruiting in payments and risk strategy roles.

## Decision

1. Reposition the product as **Digital Goods Merchant Risk Strategy Lab**.  
2. Make research, taxonomy, and content-risk frameworks first-class deliverables.  
3. Replace the primary decision surface with explainable strategy outputs (decision, drivers, controls, illustrative reserve, confidence, limitations).  
4. Retire PD/LGD/EAD/EL from the primary API and UI (optional documented appendix only).  
5. Archive v0 engine docs under `docs/archive/v0-credit-engine/`.  
6. Preserve `Project Brief - Updated.docx` unchanged; document supersession.  
7. Keep four decision actions and synthetic-data boundary (ADR-002 remains in force).

## Alternatives considered

| Option | Why not |
|--------|---------|
| Keep engine framing; add research as appendix | Still implies production underwriting posture |
| Dual-mode “research + credit model” | Dilutes message; increases overclaim risk |
| Greenfield rewrite deleting Sprint 0 | Discards sound API separation, tests, and governance patterns |

## Consequences

- Documentation and API contracts change in Phase 2–4.  
- Existing unit/contract tests will be rewritten against new schemas.  
- Portfolio story strengthens on strategy and governance; weakens on “validated PD model” claims (intentional).
