# ADR-001: Core library / API separation

**Status:** Accepted  
**Date:** 2026-08-06  
**Deciders:** Charlene Yang (portfolio owner)

## Context

The decision engine must be testable without HTTP, reusable from batch jobs and simulators, and integrable into a separately hosted portfolio frontend. Embedding scoring logic in FastAPI route handlers or in the UI would couple delivery concerns to risk methodology.

## Decision

Implement all scoring, expected-loss, reserve, and policy logic in `src/merchant_risk/` as a typed, framework-independent Python package. FastAPI (`api/`) validates HTTP payloads, maps to domain types, invokes the engine, and serializes responses. The frontend calls the API only.

## Alternatives considered

| Option | Why not |
|--------|---------|
| Logic inside FastAPI routes | Harder unit testing; couples web framework to domain |
| Logic in frontend | Duplicates methodology; breaks API-as-boundary; harder governance |
| Monolithic notebook | Not deployable or portfolio-integrable |

## Consequences

- Domain tests run without a web server.  
- API and UI can deploy independently.  
- Slight mapping overhead between Pydantic schemas and domain models (acceptable).  
