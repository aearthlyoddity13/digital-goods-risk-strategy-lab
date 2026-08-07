# Deploy the strategy API on Render

**Target:** HTTPS API for the portfolio’s interactive P1 lab  
**Repository:** `https://github.com/aearthlyoddity13/digital-goods-risk-strategy-lab`  
**Blueprint:** `/render.yaml`

## Deployment choice

The initial Blueprint uses a free Render web service so the deployment can be validated without committing to recurring infrastructure cost. Free services spin down after inactivity and can take approximately one minute to wake. That delay is unsuitable as the only recruiter-facing experience.

Before promoting the live lab, either:

1. upgrade the service to an always-on paid instance; or
2. retain the free service but make the portfolio’s static fallback immediate and let the interactive model become available after it wakes.

The API is stateless and reads versioned configuration and synthetic scenarios packaged with the image. It does not require a database or persistent disk.

## 1. Commit the deployment files

From the P1 repository:

```bash
git status
git add .dockerignore render.yaml docker/Dockerfile docs/DEPLOYMENT_RENDER.md docs/README.md CHANGELOG.md
git commit -m "Prepare strategy API for Render deployment"
git push origin main
```

Confirm GitHub Actions pass before creating the Render service.

## 2. Create the Blueprint

1. Sign in to Render.
2. Select **New → Blueprint**.
3. Connect `aearthlyoddity13/digital-goods-risk-strategy-lab`.
4. Select the repository’s `render.yaml`.
5. Review the proposed service named `digital-goods-risk-strategy-lab-api`.
6. Confirm the initial instance type is **Free**.
7. Apply the Blueprint and wait for the health check to pass.

Render will provide an HTTPS address resembling:

```text
https://digital-goods-risk-strategy-lab-api.onrender.com
```

Use the exact address shown in the Render dashboard.

## 3. Verify the deployed API

Replace `<API_ORIGIN>` below:

```bash
curl -i <API_ORIGIN>/health
curl -s <API_ORIGIN>/api/v1/methodology
curl -s <API_ORIGIN>/api/v1/archetypes
```

Expected health behavior:

- HTTPS connection succeeds;
- HTTP status is `200`;
- response contains `"status":"ok"`;
- service and version metadata are present.

Verify production CORS:

```bash
curl -i -X OPTIONS <API_ORIGIN>/api/v1/archetypes \
  -H 'Origin: https://www.charlene-yang.com' \
  -H 'Access-Control-Request-Method: GET'
```

Expected header:

```text
access-control-allow-origin: https://www.charlene-yang.com
```

An unlisted origin must not receive that header:

```bash
curl -i -X OPTIONS <API_ORIGIN>/api/v1/archetypes \
  -H 'Origin: https://untrusted.example' \
  -H 'Access-Control-Request-Method: GET'
```

## 4. Connect the portfolio

In the portfolio/Vercel project, add a public environment variable using the project’s established naming convention, for example:

```text
NEXT_PUBLIC_MERCHANT_RISK_API_URL=<API_ORIGIN>
```

Use the variable in the lab client; do not hard-code the Render URL in source. Apply it to Production and Preview only if preview domains are separately allowed by CORS. Redeploy the portfolio after adding the variable.

The portfolio integration must:

- use a bounded connection timeout;
- show the static synthetic result immediately when the API is sleeping or unavailable;
- offer a retry without resetting the reader’s scroll position;
- retain the synthetic-data disclosure in both live and fallback states;
- never send personal, confidential or real merchant data.

## 5. Pre-launch gate

- [ ] Render deploy uses the latest passing `main` commit.
- [ ] `/health` and all three strategy endpoints return `200` over HTTPS.
- [ ] Allowed-origin preflight succeeds from `www.charlene-yang.com`.
- [ ] Unlisted-origin preflight is rejected.
- [ ] Portfolio fallback appears promptly during a cold start.
- [ ] API wake-up does not leave an indefinite loading state.
- [ ] Render logs contain no secrets, real merchant data or raw user telemetry.
- [ ] Paid always-on service or an acceptable cold-start experience is chosen before external promotion.

## Rollback

If integration fails, remove or unset the portfolio API environment variable and redeploy the portfolio. The static case study and fallback should continue to render without the API. Roll back the Render service to the previous passing deploy from its dashboard if an API regression caused the failure.
