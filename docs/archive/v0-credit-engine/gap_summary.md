# Repository audit and gap summary

**Date:** 2026-08-06  
**Status:** Phase 0 kickoff

## What existed

| Artifact | Status |
|----------|--------|
| `CURSOR_MASTER_PROMPT.md` | Present — build authority |
| `Project Brief - Updated.docx` | Present — product authority |
| Source code, tests, CI, docs, Docker, frontend | Absent |

## Conflicts with the brief

None material. The repository was greenfield; the master prompt and brief agree on product, architecture, phases, and public-data boundary.

## Gaps closed in this vertical slice

1. Domain terminology freeze and documentation set  
2. Typed schemas and core library / API separation  
3. Project tooling (Makefile, lint, typecheck, pytest, CI)  
4. `GET /health` and `POST /v1/merchants/decision`  
5. Deterministic sample merchants for all four actions  
6. Unit and contract tests  
7. Minimal reviewer page with editorial design system  

## Deferred (by design)

| Phase | Deferred work |
|-------|---------------|
| 1+ | Full batch endpoint hardening, override API surface |
| 2 | Synthetic vintages, out-of-time metrics, validation report evidence |
| 3 | Policy simulator frontiers and capacity constraint |
| 4 | Full portfolio packaging, remote deploy verification, walkthrough assets |
| 5 | Two-page risk memo, video, publication package |

## Acceptance for this slice

See [sprint_plan.md](sprint_plan.md). Baseline labeled **illustrative** until Phase 2.
