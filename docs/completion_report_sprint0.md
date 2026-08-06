# Sprint 0 completion report

**Date:** 2026-08-06  
**Phase:** 0 + first vertical slice  
**Version:** 0.1.0

## Outcome

Greenfield repository initialized from the project brief and master prompt. Delivered planning docs, core risk library, FastAPI health + decision endpoints, four deterministic synthetic merchants, unit/contract tests, CI/Docker skeleton, and a minimal editorial reviewer page.

**Baseline remains illustrative** — no predictive-effectiveness claims.

## Material implementation decisions

| Decision | Choice |
|----------|--------|
| Core vs API | Framework-independent `merchant_risk` + FastAPI adapter ([ADR-001](adr/001-core-library-api-separation.md)) |
| Data | Synthetic only ([ADR-002](adr/002-synthetic-data-public-boundary.md)) |
| Model | Transparent weighted scorecard + logistic PD |
| Frontend | Static HTML/CSS/JS for portability; env-style `config.js` API base |
| Python | ≥3.11 (local verify on 3.12) |

## Documentation created

PRD, architecture, ADRs (2), data dictionary, synthetic-data spec, model card, validation plan/report placeholders, API docs, test strategy, risk register, runbook, backlog, sprint plan, decision log, portfolio case study draft, gap summary.

## Verification

```text
make test       → 11 passed
make lint       → clean
make typecheck  → clean
```

Sample action mapping verified:

| Merchant | Action |
|----------|--------|
| SYN-APPROVE-001 | APPROVE |
| SYN-CONTROLS-001 | APPROVE_WITH_CONTROLS |
| SYN-REVIEW-001 | MANUAL_REVIEW |
| SYN-DECLINE-001 | DECLINE |

## Assumptions

- Expert-prior coefficients, not production-fitted.  
- Hand-authored samples prove plumbing, not discrimination.  
- Demo API has no authentication (add before any sensitive host).

## Remaining limitations / next sprint

1. `GET /v1/model-card`, `GET /v1/schema`, `POST /v1/merchants/batch`  
2. Hardening for missing/boundary inputs beyond current validators  
3. Phase 2 synthetic vintages + out-of-time validation pipeline  
4. Policy simulator (Phase 3)  
5. Full reviewer UX states, remote deploy, accessibility pass (Phase 4)

## Recommended next action

Start **Sprint 1 / Phase 1**: batch + schema/model-card endpoints, expanded golden tests, then begin synthetic vintage generator scaffolding for Phase 2.
