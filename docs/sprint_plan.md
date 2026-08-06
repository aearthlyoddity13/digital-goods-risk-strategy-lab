# Sprint plan — Sprint 0 (Foundation vertical slice)

**Goal:** Ship Phase 0 foundation plus the smallest working decision path (health + single decision + samples + tests + minimal UI).

**Dates:** 2026-08-06 (kickoff)

## In scope

- Planning docs (PRD, architecture, ADRs, dictionary, synthetic spec, backlog)  
- Python package + FastAPI health/decision  
- Config versions, logging, CI, Docker skeleton  
- Four sample merchants  
- Unit + contract tests  
- Minimal editorial reviewer page  

## Out of scope

- Validation metrics, policy simulator, batch/model-card endpoints (stubs ok)  
- Production auth, PostgreSQL, polished dashboard chrome  

## Dependencies

Python 3.11+, Node not required for static frontend.

## Risks

Synthetic overclaim; incomplete OpenAPI coverage for deferred endpoints.

## Definition of done

- [x] Docs created and cross-linked  
- [x] `make test` passes  
- [x] `/health` and `/v1/merchants/decision` work locally  
- [x] Samples map to four actions  
- [x] Baseline labeled illustrative  
- [x] Completion report written  

## Retrospective notes

Vertical slice completed in one pass. Primary friction: local default `python3` was 3.9; project pins ≥3.11 and verifies on 3.12. Frontend kept static for portfolio portability.
