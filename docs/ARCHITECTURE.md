# Architecture

**Version:** 0.2.0-draft  
**Product:** Digital Goods Merchant Risk Strategy Lab

## Principles

- Research content, policy configuration, domain logic, API, and UI are separated.  
- FastAPI is an adapter; strategy logic lives in a framework-independent library.  
- Demonstrator, not production underwriting.  
- Synthetic/aggregated data only at the trust boundary (ADR-002, ADR-003).

## Component view

```text
┌────────────────────────────┐
│ Research + Scenario Lab UI │
│ (frontend/, embeddable)    │
└─────────────┬──────────────┘
              │ /api/v1/*
┌─────────────▼──────────────┐
│ FastAPI (api/)             │
│ validation, CORS, OpenAPI  │
└─────────────┬──────────────┘
              │
┌─────────────▼──────────────┐
│ Strategy library           │
│ scoring · policy · reserve │
│ content · scenarios        │
└─────────────┬──────────────┘
              │
┌─────────────▼──────────────┐
│ config/*.yaml + data/      │
│ archetypes (synthetic)     │
└────────────────────────────┘
```

## Target API

| Endpoint | Role |
|----------|------|
| `GET /health` | Liveness + versions |
| `GET /api/v1/archetypes` | List archetypes/scenarios |
| `GET /api/v1/risk-factors` | Taxonomy metadata |
| `POST /api/v1/assess` | Scenario assessment |
| `POST /api/v1/compare` | Baseline vs stressed |
| `GET /api/v1/methodology` | Methodology + disclaimers |

Legacy `POST /v1/merchants/decision` remains until Phase 4 cutover; then deprecate.

## Trust boundaries

| Boundary | Rule |
|----------|------|
| Public demo | Synthetic merchants only; UI notice |
| API | Pydantic validation; CORS allowlist; no secrets in repo |
| Core library | Pure functions; no network I/O |
| Logs | No personal data |

## Deployment

Local: `make run-api` + static frontend server.  
Env: `HOST`, `PORT`, `CORS_ORIGINS`, frontend API base URL.  
Container: `docker/` retained and updated in Phase 4–6.
