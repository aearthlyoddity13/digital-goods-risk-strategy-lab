# Test strategy

**Version:** 0.2.0-draft

## Layers

| Layer | Focus |
|-------|-------|
| Unit | Policy interactions, score bands, reserve bands, hard rules, scenario transforms |
| Contract | `/health`, `/api/v1/*` schemas and status codes |
| Integration | API + sample archetypes end-to-end |
| Frontend smoke | Guided demos render; disclaimer visible |
| Accessibility | Keyboard paths, contrast of risk states, live regions |
| Governance | Copy checks for proprietary-data language; synthetic disclosure present |

## Gates

- `make test`, `make lint`, `make typecheck` green before merge  
- Golden scenarios for three guided demos stable across versions unless changelog notes intentional policy change  
- Model-card required disclosures present in methodology endpoint (Phase 4+)

## Non-goals

Claiming statistical model validation (AUC, etc.) for this demonstrator.
