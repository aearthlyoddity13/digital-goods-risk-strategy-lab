# Backlog

Prioritized for portfolio MVP. Status: `todo` | `doing` | `done`.

## Epic E0 — Foundation

| ID | Story | Priority | Status | Acceptance |
|----|-------|----------|--------|------------|
| E0-1 | Repository structure and docs index | P0 | done | Docs linked from README |
| E0-2 | PRD + architecture + 2 ADRs | P0 | done | Reviewer can understand boundaries |
| E0-3 | Data dictionary + synthetic spec | P0 | done | Leakage fields tagged |
| E0-4 | Tooling: Makefile, CI, env example | P0 | done | `make test` / CI green |
| E0-5 | `GET /health` | P0 | done | Contract test passes |
| E0-6 | Baseline `POST /v1/merchants/decision` | P0 | done | Four actions via samples |
| E0-7 | Minimal reviewer page | P0 | done | Decision-first editorial UI |

## Epic E1 — Baseline engine hardening

| ID | Story | Priority | Status |
|----|-------|----------|--------|
| E1-1 | Batch endpoint with size cap | P1 | todo |
| E1-2 | Model-card and schema endpoints | P1 | todo |
| E1-3 | Override structure persistence | P2 | todo |
| E1-4 | Expanded golden tests / missing data | P1 | todo |

## Epic E2 — Validation

| ID | Story | Priority | Status |
|----|-------|----------|--------|
| E2-1 | Synthetic vintage generator | P1 | todo |
| E2-2 | Out-of-time metrics pipeline | P1 | todo |
| E2-3 | Validation report population | P1 | todo |

## Epic E3 — Policy simulator

| ID | Story | Priority | Status |
|----|-------|----------|--------|
| E3-1 | Threshold/reserve scenario API | P1 | todo |
| E3-2 | Frontiers + capacity constraint | P1 | todo |

## Epic E4 — Portfolio interface & deploy

| ID | Story | Priority | Status |
|----|-------|----------|--------|
| E4-1 | Full reviewer UX states | P1 | todo |
| E4-2 | Remote deploy + CORS verify | P1 | todo |
| E4-3 | Static fallback package | P1 | todo |
