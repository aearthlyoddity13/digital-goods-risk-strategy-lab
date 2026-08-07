# P1 publication-readiness audit

**Audit date:** 2026-08-08  
**Target route:** `/work/digital-goods-risk-strategy-lab`  
**Decision:** Content-ready for local portfolio integration; not ready for public launch until the repository and API destinations are resolved.

## 1. Executive status

| Workstream | Status | Publication decision |
|---|---|---|
| Core thesis and project positioning | Ready | Publish using `PORTFOLIO_PUBLICATION_PACKAGE.md`. |
| Short-drama deep dive | Ready with scoped claims | Publish the mechanism summary; retain market figures as directional app-store context. |
| AI-services deep dive | Ready with scoped claims | Publish billing structures and control logic; do not imply sector-wide loss prevalence. |
| Synthetic scenarios and economics | Ready | Publish three selected scenarios with the synthetic/illustrative disclosure. |
| Interactive frontend | Ready locally | Embed only after a production API and fallback are configured. |
| Automated verification | Ready | 40 tests pass in the project virtual environment. |
| Public source-code destination | Blocked | Current Git remote points to the portfolio repository, not an intentional standalone P1 repository. |
| Production API destination | Blocked | Frontend configuration still points to `http://127.0.0.1:8000`. |
| Public research-note destinations | Pending implementation | Create portfolio routes or omit the deep-dive links until those routes exist. |
| Preview/OG asset | Missing | Create after the production page layout is stable. |

## 2. Public claim register

### Claims approved for prominent use

| Public claim | Claim class | Support and condition |
|---|---|---|
| Digital goods can create exposure after settlement because access is immediate and customer-funded value may remain unused. | Strategic inference | Supported by documented product structures; present as the project’s analytical framing. |
| Short-drama apps exceeded 850M estimated downloads and roughly $750M estimated IAP revenue in Q1 2026. | External market context | Sensor Tower page verified 2026-08-08. Label as estimated **app-store** activity and do not present as direct-web payment volume. |
| OpenAI’s terms distinguish prepaid from promotional service credits and describe advance payment, transfer restrictions and expiry. | First-party structural example | OpenAI terms verified 2026-08-08. State explicitly that this is one provider example, not a sector-wide rule. |
| Digital activity and provisioning records were associated with stronger “product not received” dispute outcomes in Stripe’s analysis. | Observational evidence | Keep the correlation limitation and source adjacent to the claim. Do not convert the association into a model coefficient. |
| US subscription practices require clear material terms, informed consent and a simple cancellation mechanism under ROSCA. | Legal context | Cite the statute in the long-form note; state that the project is not legal advice. |
| Subscription disclosure and cancellation remain enforcement concerns. | Enforcement context | DOJ Adobe announcement verified 2026-08-08; describe the conduct as allegations resolved by a proposed stipulated order, not as a universal underwriting standard. |

### Claims approved only as synthetic demonstration results

- Risk scores, reserve percentages, decisions and monthly contribution changes.
- The $1 million monthly attempted-payment-volume merchant.
- Probability-weighted uncovered exposure and posture-effect assumptions.
- Thresholds, near-equivalence bands, release conditions and escalation triggers.

At first meaningful appearance use: `Illustrative results from aggregated synthetic scenarios; not observed merchant performance or industry benchmarks.`

### Claims not approved for public promotion

- Predictive accuracy, expected real-world loss reduction or production readiness.
- Industry-wide fraud, chargeback, reserve or attrition rates.
- Causal claims about complaints, disputes or merchant failure.
- Any implication that PayPal, Stripe or another processor supplied data or methodology.
- Automated legal, sanctions, content-rights or prohibited-activity conclusions.
- Claims that a specific reserve rate is optimal for a real merchant.

## 3. Source review outcome

The source register is sufficient for the **two flagship applications** and the public decision framework. The following gaps do not block the current flagship page because they concern secondary categories or empirical calibration:

- web-fiction creator and prepaid obligations;
- gaming account takeover and transferable-item recoverability;
- sector-wide AI refund, overage or credit outcomes;
- empirical reserve friction and merchant attrition;
- evidence-based chargeback timing distributions.

Do not expand web fiction or gaming beyond concise scenario context until those gaps are researched. The public page should continue to emphasize short drama and AI services.

## 4. Required launch destinations

| Destination | Required value | Current state | Action |
|---|---|---|---|
| Portfolio case-study URL | `https://www.charlene-yang.com/work/digital-goods-risk-strategy-lab` | Route specification only | Build locally in portfolio repository. |
| Production API base URL | HTTPS origin serving `/health` and `/api/v1/*` | Missing | Deploy API, then set the portfolio environment variable and CORS allowlist. |
| P1 source-code URL | Dedicated public repository or deliberate monorepo path | Incorrect/unclear remote | Create or identify the intended repository before showing `View source code`. |
| Standalone lab URL | HTTPS frontend or portfolio-native lab route | Missing | Prefer portfolio-native component; standalone URL is optional if fallback is robust. |
| Short-drama note | Portfolio Insights route or omitted link | Missing | Publish note or remove the CTA. No placeholder link. |
| AI-services note | Portfolio Insights route or omitted link | Missing | Publish note or remove the CTA. No placeholder link. |
| OG image | 1200×630 project preview | Missing | Capture/design after final route is stable. |

## 5. Repository issue requiring an intentional decision

The current local P1 directory reports this remote:

```text
origin  https://github.com/aearthlyoddity13/charlene-portfolio.git
```

Do not push P1 from this directory until the repository relationship is confirmed. Recommended default: create a dedicated public repository such as `digital-goods-risk-strategy-lab`, preserve commit history if appropriate, and use that URL for the public source CTA. An alternative is an explicit P1 subdirectory inside the portfolio monorepo, but only if that reflects the actual deployment architecture.

## 6. API deployment contract

Before enabling the live lab:

1. Deploy the FastAPI service to an HTTPS origin.
2. Configure `CORS_ORIGINS=https://www.charlene-yang.com,https://charlene-yang.com` and remove production reliance on the localhost regex.
3. Confirm `/health`, `/api/v1/archetypes`, `/api/v1/compare` and `/api/v1/compare-postures` from the production website origin.
4. Keep OpenAPI public only if intentional; the service has no authentication and must accept synthetic demonstration inputs only.
5. Add bounded request timeouts, error handling and basic rate protection at the hosting layer.
6. Configure the portfolio through an environment variable; do not edit and commit `frontend/config.js` with a private or temporary deployment address.
7. Preserve the permanent synthetic-data disclosure inside every result view.

## 7. Public asset checklist

- [ ] Production project route implemented from the publication package.
- [ ] Dedicated source-code destination confirmed.
- [ ] HTTPS API deployed and cross-origin requests verified.
- [ ] Static API-failure fallback tested.
- [ ] Short-drama and AI-services destinations published or their CTAs removed.
- [ ] 1200×630 OG image created from the final interface.
- [ ] One 16:9 lab screenshot prepared for Work index and LinkedIn sharing.
- [ ] Alt text written for every project image.
- [ ] Page title, description, canonical, OG and structured data verified.
- [ ] No `draft`, `pending`, `localhost`, TODO, internal version or developer note visible.
- [ ] Chrome, Edge and Safari production smoke completed.

## 8. Go/no-go gate

P1 may be integrated locally now. Public launch is **GO** only when:

- the source CTA points to an intentional public destination or is removed;
- the lab uses an HTTPS production API and passes CORS testing;
- every visible CTA resolves to a real route;
- synthetic-data and limitations disclosures remain visible;
- production metadata and cross-browser smoke checks pass.

Until then, keep the portfolio route unpublished or omit the interactive/source CTAs rather than exposing placeholders.
