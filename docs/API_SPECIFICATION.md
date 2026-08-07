# API specification

**Version:** 0.2.0-draft  
**Base:** `/api/v1` (strategy lab)  
**OpenAPI:** FastAPI `/docs` when server running  
**Disclaimer on assess/compare responses:** Demonstration data: aggregated and synthetic. No confidential merchant, customer or payment-platform data is used.

## Endpoints

### `GET /health`

Liveness and version metadata (`methodology_version`, `policy_version`, service name).

### `GET /api/v1/archetypes`

Returns the eight versioned synthetic scenarios and four available period labels for each.

### `GET /api/v1/risk-factors`

Returns taxonomy factor catalog (codes, families, short descriptions).

### `POST /api/v1/assess`

**Request:** aggregated scenario fields per [DATA_DICTIONARY.md](DATA_DICTIONARY.md).  
**Response:** decision, risk_level, illustrative_risk_score, primary_risk_drivers, protective_factors, recommended_controls, illustrative_reserve, conditions_to_reduce_controls, escalation_triggers, confidence, methodology_version, policy_version, synthetic_data_disclaimer, limitations.

### `POST /api/v1/compare`

**Request:** baseline and candidate references: `{ "scenario_key", "period" }`.
**Response:** both assessments plus `delta_explanation` summarizing why the decision/controls changed.

### `POST /api/v1/compare-postures`

**Request:** one `{ "scenario_key", "period" }` reference.

**Response:** permissive, balanced-growth and conservative simulations with effective payment rates, residual risk, reserve settings, normalized economics, illustrative dollar economics, risk-appetite eligibility and a recommendation derived from the synthetic assumptions.

Policy effects are versioned in `config/strategy/postures-0.1.0.yaml` and are explicitly illustrative.

### `GET /api/v1/methodology`

Methodology summary, versions, and governance disclaimers (mirrors model card highlights).

## Errors

Structured `{ "error_code", "message", "request_id", "details" }`.

## CORS / config

`CORS_ORIGINS` comma-separated allowlist from environment. No wildcard default for production-like deploys.

## Samples

```bash
curl -s http://127.0.0.1:8000/health | python3 -m json.tool
curl -s http://127.0.0.1:8000/api/v1/methodology | python3 -m json.tool
curl -s http://127.0.0.1:8000/api/v1/archetypes | python3 -m json.tool
```

## Legacy

`POST /v1/merchants/decision` — Sprint 0 credit-engine endpoint; deprecate after assess ships.
