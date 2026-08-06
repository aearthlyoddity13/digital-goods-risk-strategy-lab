# Runbook

## Local setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
make test
make run-api
```

API: `http://127.0.0.1:8000` — OpenAPI at `/docs`.

Frontend (static):

```bash
cd frontend && python3 -m http.server 5173
```

Set `window` / meta API base or edit `frontend/config.js` to point at the API. Default `http://127.0.0.1:8000`.

## Health check

```bash
curl -sf http://127.0.0.1:8000/health
```

## Configuration

See `.env.example`: `CORS_ORIGINS`, `LOG_LEVEL`, `HOST`, `PORT`, `MAX_BATCH_SIZE`.

## Docker

```bash
docker compose -f docker/docker-compose.yml up --build
```

## Incident diagnosis

1. Check `/health`.  
2. Inspect structured logs for `request_id`.  
3. Reproduce with `data/sample` merchant.  
4. Confirm model/policy versions in response match `config/`.

## Rollback

Redeploy previous image/tag; config is version-pinned in response metadata. No DB migrations in Phase 0.

## Known limitations

Baseline illustrative; batch/simulate endpoints not complete; no auth (demo only — add auth before any sensitive deploy).
