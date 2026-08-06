# API specification

**Base path:** versioned under `/v1`  
**OpenAPI:** served by FastAPI at `/docs` and `/openapi.json`

## Endpoints

### `GET /health`

Liveness and version metadata.

**Response 200**

```json
{
  "status": "ok",
  "service": "merchant-credit-reserve-engine",
  "api_version": "v1",
  "model_version": "scorecard-0.1.0",
  "policy_version": "policy-0.1.0"
}
```

### `POST /v1/merchants/decision`

Single merchant decision.

**Request:** see [data_dictionary.md](data_dictionary.md) request features.  
**Response:** decision payload with economics, reasons, flags, versions.  
**Errors:** structured `{ "error_code", "message", "request_id", "details" }`.

### Planned (stubs / later slices)

| Endpoint | Status |
|----------|--------|
| `GET /v1/model-card` | Phase 1 |
| `GET /v1/schema` | Phase 1 |
| `POST /v1/merchants/batch` | Phase 1 (bounded) |
| `POST /v1/policies/simulate` | Phase 3 |

## CORS

Allowlist from `CORS_ORIGINS` (comma-separated). Default localhost only. No broad production `*` by default.

## Examples

### curl

```bash
curl -s http://127.0.0.1:8000/health | jq
curl -s -X POST http://127.0.0.1:8000/v1/merchants/decision \
  -H 'Content-Type: application/json' \
  -d @data/sample/merchants.json
```

(Use a single merchant object from the sample file.)

### Python

```python
import httpx, json
from pathlib import Path
merchants = json.loads(Path("data/sample/merchants.json").read_text())
r = httpx.post("http://127.0.0.1:8000/v1/merchants/decision", json=merchants[0])
print(r.json())
```

### Browser JavaScript

```javascript
const res = await fetch(`${import.meta.env.VITE_API_BASE_URL}/v1/merchants/decision`, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(merchant),
});
```

## Batch limit (when implemented)

`MAX_BATCH_SIZE` env (default 50).
