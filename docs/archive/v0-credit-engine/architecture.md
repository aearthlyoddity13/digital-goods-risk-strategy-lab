# Architecture

**Version:** 0.1.0  
**Status:** Phase 0 foundation

## 1. Principles

- Framework-independent core risk library; FastAPI is an adapter.  
- API is the stable portfolio integration boundary.  
- Model scoring informs policy; hard rules are not silently overridden by the score.  
- Synthetic / public-demo data only at the trust boundary.

## 2. Component diagram

```text
┌─────────────────┐     HTTPS/JSON      ┌──────────────────┐
│ Reviewer UI     │ ──────────────────► │ FastAPI (api/)   │
│ (frontend/)     │ ◄────────────────── │ routes, schemas  │
└─────────────────┘                     └────────┬─────────┘
                                                 │
                                                 ▼
                                        ┌──────────────────┐
                                        │ merchant_risk    │
                                        │ scoring / EL /   │
                                        │ reserve / policy │
                                        └────────┬─────────┘
                                                 │
                                        ┌────────▼─────────┐
                                        │ config/model +   │
                                        │ config/policy    │
                                        └──────────────────┘
```

## 3. Layers

| Layer | Path | Responsibility |
|-------|------|----------------|
| Domain | `src/merchant_risk/` | Scorecard, PD, EAD, LGD, EL, reserve, policy, reason codes |
| API | `api/` | Validation, CORS, request IDs, OpenAPI, versioned routes |
| Config | `config/` | Versioned model and policy YAML |
| Frontend | `frontend/` | Reviewer demo; no duplicated decision logic |
| Tests | `tests/` | Unit, contract, integration, e2e |
| Data | `data/sample/` | Deterministic sample merchants |

## 4. Data flow (single decision)

1. Client `POST /v1/merchants/decision` with merchant features.  
2. API validates with Pydantic; assigns/propagates `request_id`.  
3. Domain engine: validate leakage → score → PD → EAD/LGD/EL → hard rules → reserve → action.  
4. Response includes economics, reason codes, flags, versions, assumptions.  
5. Structured log line with request ID, action, versions (no PII).

## 5. Trust boundaries

| Boundary | Rule |
|----------|------|
| Public demo | Synthetic merchants only; UI notice prohibits real confidential data |
| API | Input validation; bounded payloads; CORS allowlist from env |
| Core library | Pure functions; no network I/O; no secrets |
| Persistence | Optional later; SQLite local / PostgreSQL-compatible interface if needed |

## 6. Deployment

- Local: `make run-api` + static frontend or simple HTTP server.  
- Container: `docker/` images for API; frontend served statically or separately.  
- Cloud-agnostic: env vars for CORS, host, log level, API base URL.  
- Portfolio: configure `VITE_API_BASE_URL` (or equivalent); static fallback if API down.

## 7. Related ADRs

- [ADR-001](adr/001-core-library-api-separation.md) — core/API separation  
- [ADR-002](adr/002-synthetic-data-public-boundary.md) — synthetic/public-use boundary  
