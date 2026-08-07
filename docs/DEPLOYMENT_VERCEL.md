# Deploy the strategy API on Vercel

**Target:** Free HTTPS serverless API for the portfolio’s interactive P1 lab  
**Repository:** `https://github.com/aearthlyoddity13/digital-goods-risk-strategy-lab`  
**Entrypoint:** `/app.py`

## Deployment architecture

Vercel packages the FastAPI application as one Python serverless function. The service is stateless and reads versioned policy configuration and synthetic scenarios bundled with the deployment. It requires no database, persistent disk or background worker.

The repository includes:

- `app.py` — Vercel-recognized FastAPI entry point;
- `vercel.json` — includes the API, Python package, configuration and synthetic data in the function bundle;
- `.vercelignore` — excludes development, documentation, frontend and container artifacts from upload.

## 1. Create the Vercel project

1. Sign in to Vercel using the account that hosts `charlene-yang.com`.
2. Select **Add New → Project**.
3. Import `aearthlyoddity13/digital-goods-risk-strategy-lab`.
4. Keep the repository root as the project root.
5. Do not set a frontend framework, build command or output directory.
6. Add the environment variables below.
7. Deploy.

The API should receive its own Vercel domain, for example:

```text
https://digital-goods-risk-strategy-lab.vercel.app
```

Use the exact URL assigned by Vercel.

## 2. Environment variables

Add these to **Production**:

| Variable | Value |
|---|---|
| `APP_NAME` | `digital-goods-risk-strategy-lab-api` |
| `LOG_LEVEL` | `INFO` |
| `CORS_ORIGINS` | `https://www.charlene-yang.com,https://charlene-yang.com` |
| `CORS_ORIGIN_REGEX` | `^$` |

No credentials or secrets are required. Do not upload a local `.env` file.

If the portfolio’s preview deployments need the API, add only a narrowly scoped Vercel preview-domain regex after confirming the exact project slug. Do not use a universal `https://.*\.vercel\.app` allowlist.

## 3. Verify the deployed API

Set the exact deployed origin locally for the following commands:

```bash
P1_API_ORIGIN=https://your-exact-api-domain.vercel.app

curl -i "$P1_API_ORIGIN/health"
curl -s "$P1_API_ORIGIN/api/v1/methodology"
curl -s "$P1_API_ORIGIN/api/v1/archetypes"
```

Expected health behavior:

- HTTPS succeeds;
- status is `200`;
- JSON contains `"status":"ok"`;
- model and policy versions are present.

Verify allowed-origin CORS:

```bash
curl -i -X OPTIONS "$P1_API_ORIGIN/api/v1/archetypes" \
  -H 'Origin: https://www.charlene-yang.com' \
  -H 'Access-Control-Request-Method: GET'
```

Expected header:

```text
access-control-allow-origin: https://www.charlene-yang.com
```

Verify rejection of an unlisted origin:

```bash
curl -i -X OPTIONS "$P1_API_ORIGIN/api/v1/archetypes" \
  -H 'Origin: https://untrusted.example' \
  -H 'Access-Control-Request-Method: GET'
```

The unlisted response must not contain `access-control-allow-origin`.

## 4. Connect the portfolio

In the portfolio’s Vercel project, add:

```text
NEXT_PUBLIC_MERCHANT_RISK_API_URL=https://your-exact-api-domain.vercel.app
```

Apply the variable to Production. Redeploy the portfolio after saving it.

The website client must:

- read the API address from the environment variable;
- use a bounded request timeout;
- render a static synthetic result if the API is unavailable;
- provide retry without resetting scroll position;
- retain the synthetic-data disclosure in every state;
- never accept confidential, personal or real merchant data.

## 5. Optional API subdomain

A branded address such as `risk-api.charlene-yang.com` is optional. It requires adding the subdomain to the P1 Vercel project and creating the DNS record Vercel specifies. The default `vercel.app` HTTPS domain is sufficient for initial publication and does not appear in the visible portfolio interface.

## 6. Pre-launch gate

- [ ] Deployment uses the latest passing `main` commit.
- [ ] `/health`, `/api/v1/methodology` and `/api/v1/archetypes` return `200`.
- [ ] Scenario comparison endpoints return expected synthetic results.
- [ ] Allowed production-origin preflight succeeds.
- [ ] Unlisted-origin preflight is rejected.
- [ ] Portfolio environment variable uses the exact HTTPS API origin.
- [ ] Static fallback and retry states are tested.
- [ ] No local path, `.env`, secret or real merchant data is bundled.
- [ ] Production Chrome, Edge and Safari smoke tests pass.

## Rollback

If the live integration fails, unset `NEXT_PUBLIC_MERCHANT_RISK_API_URL` in the portfolio project and redeploy the portfolio. The static case study and fallback must remain available. Use Vercel’s deployment history to promote the previous passing API deployment if an API regression caused the problem.
