# Implementation plan — Digital Goods Merchant Risk Strategy Lab

**Date:** 2026-08-06  
**Status:** Phase 1 complete (audit + plan). Awaiting systematic execution of Phases 2–8.  
**Repositioning:** From “Merchant Credit & Reserve Decision Engine” → **Digital Goods Merchant Risk Strategy Lab**

---

## 1. Repository audit summary

### 1.1 What exists

A working Phase 0 / Sprint 0 vertical slice under `P1 Merchant Credit & Reserve Decision Engine/`:

| Area | Contents | Maturity |
|------|----------|----------|
| **Authority docs** | `Project Brief - Updated.docx`, `CURSOR_MASTER_PROMPT.md` | Prior product definition (credit/reserve engine + PD/LGD/EAD) |
| **Docs** | PRD, architecture, API, data dictionary, synthetic spec, model card, validation plan/report placeholders, ADRs (2), backlog, sprint plan, case study draft, runbook, risk register, test strategy, decision log, gap summary, completion report | Complete for prior positioning; incomplete for research-lab positioning |
| **Domain library** | `src/merchant_risk/` — scorecard, PD calibration, EAD/LGD/EL, hard policy, reserve | Functional, ~600 LOC; credit-model framing |
| **Config** | `config/model/scorecard-0.1.0.yaml`, `config/policy/policy-0.1.0.yaml` | Versioned; illustrative thresholds |
| **API** | FastAPI: `GET /health`, `POST /v1/merchants/decision`; CORS, request IDs, env settings | Solid adapter pattern (ADR-001) |
| **Data** | 4 hand-authored synthetic merchants in `data/sample/merchants.json`; `data/generated/` empty | Synthetic boundary already stated (ADR-002) |
| **Frontend** | Static HTML/CSS/JS reviewer demo; sample select → run decision; API fallback | Editorial but cream/terracotta/serif cluster; not a scenario lab |
| **Tests / CI** | Unit + contract (~11 tests); GitHub Actions; Makefile; Docker skeleton | Keep and extend |
| **Tooling** | `pyproject.toml`, ruff, mypy, `.env.example`, LICENSE, CHANGELOG, CONTRIBUTING | Keep |
| **Notebooks / design files** | None | N/A |
| **Research report / taxonomy / content framework** | Absent | Must create |

### 1.2 Useful work to preserve

- Core/API separation and ADR mindset  
- Synthetic-data and public-use boundary discipline  
- Decision actions: `APPROVE` | `APPROVE_WITH_CONTROLS` | `MANUAL_REVIEW` | `DECLINE`  
- Versioned YAML policy/model config pattern  
- Explainable reason-code structure  
- Reserve recommendation as a *policy output* (reframe as illustrative, not EL-optimal)  
- FastAPI + Pydantic validation, CORS, request IDs, structured errors  
- Makefile, CI, Docker, `.env.example`  
- Deterministic sample-driven tests  
- Editorial, content-first UI intent (rebuild visual language)

### 1.3 Conflicts with revised positioning

| Conflict | Current state | Required state |
|----------|---------------|----------------|
| **Product identity** | Credit & reserve *decision engine*; PD/LGD/EAD economics | Research-led *strategy lab*; rules/score demonstrator |
| **Implied authority** | Mentions PayPal only as “do not use confidential data,” but product still reads like underwriting software | Explicit research demonstrator; no implication of processor/merchant-confidential data |
| **Central narrative** | Risk-adjusted contribution / north-star metric | Central research question on evaluating digital-goods merchants |
| **Research depth** | Thin risk-family table in brief; no research report | Full research narrative, comparison table, risk taxonomy, content-risk framework |
| **Content monitoring** | Explicitly out of MVP in PRD | Major strategic pillar |
| **Data model** | Credit-scorecard features (cash buffer, device concentration, etc.) | Archetypes + aggregated scenario variables (ticket size, frequency, prepaid exposure, content-risk, multi-period) |
| **API surface** | `/v1/merchants/decision` (+ planned batch/simulate) | `/api/v1/archetypes`, `risk-factors`, `assess`, `compare`, `methodology` |
| **Outputs** | PD, LGD, EAD, EL as primary economics | Decision, risk band, drivers, protective factors, controls, illustrative reserve, escalation, confidence, limitations |
| **UI** | Load sample → run decision | Interactive scenario lab + guided demos + research publication feel |
| **Docs set** | Engine/validation-oriented filenames | Required corporate doc set (research, taxonomy, content, reserve, limitations, interview talk track, etc.) |
| **Roadmap** | Phase 2 synthetic vintages → AUC/Gini validation; Phase 3 policy frontiers | Deprioritize predictive-validation theater; prioritize research + explainable strategy + scenarios |
| **Visual design** | Warm cream + terracotta + serif (AI-design cluster risk) | Restrained editorial; warm off-white OK if palette/type diverge from cliché |
| **Package/folder name** | `merchant-credit-reserve-engine` | Rename toward `digital-goods-risk-strategy-lab` (or similar) |

### 1.4 Non-conflicts (aligned already)

- Synthetic / demonstration-only data boundary  
- No production underwriting claims in model card tone  
- Four decision actions  
- Human-readable reasons and hard rules separate from scoring  
- API-first portfolio embeddability  
- Governance artifacts (versions, changelog, limitations)

---

## 2. Target product definition

**Name:** Digital Goods Merchant Risk Strategy Lab  

**Positioning:** Educational and strategic prototype examining how payment platforms *could* evaluate emerging digital-goods merchants. Not a production underwriting model; not trained on confidential platform data; no real-world predictive-accuracy claims.

**Central question:**  
How should a payment platform evaluate and control emerging digital-goods merchants when products are intangible, consumption can be immediate, transaction frequency can be high, and traditional underwriting and fulfillment evidence are limited?

**Deliverables stack:**

1. Industry research + comparison narrative  
2. Digital-goods risk taxonomy  
3. Content-risk → payments-risk framework  
4. Synthetic merchant archetypes (multi-period scenarios)  
5. Explainable rules-and-score decision demonstrator  
6. Interactive scenario lab  
7. Best-practice / limitations documentation  
8. Versioned API + embeddable frontend module  

---

## 3. Target architecture

```text
project-root/
├── README.md
├── docs/                          # Research + governance (required doc set)
├── config/
│   ├── policy/                    # Decision thresholds, controls, escalation
│   ├── scoring/                   # Illustrative factor weights (not “model fit”)
│   └── reserve/                   # Illustrative reserve bands / holding periods
├── research/                      # Optional: source notes, citation bib (or keep in docs)
├── data/
│   ├── archetypes/                # Merchant archetypes + period scenarios
│   └── generated/                 # Deterministic generator outputs
├── src/dg_risk_lab/               # Rename from merchant_risk (or keep + alias)
│   ├── domain/                    # Types, assessment orchestration
│   ├── taxonomy/                  # Structured risk factor metadata
│   ├── scoring/                   # Interaction-aware illustrative score
│   ├── policy/                    # Decision + control selection
│   ├── reserve/                   # Illustrative reserve ranges
│   ├── content/                   # Content-signal → monitoring influence
│   ├── scenarios/                 # Stress/growth transforms
│   └── synthetic/                 # Seeded archetype generation
├── api/                           # FastAPI /api/v1/*
├── frontend/                      # Research site + scenario lab (embeddable)
├── tests/
└── .github/workflows/
```

### 3.1 API contract (target)

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/health` | Liveness + methodology/policy versions |
| GET | `/api/v1/archetypes` | List synthetic merchant archetypes |
| GET | `/api/v1/risk-factors` | Taxonomy / factor catalog |
| POST | `/api/v1/assess` | Scenario assessment |
| POST | `/api/v1/compare` | Baseline vs stressed (or A vs B) |
| GET | `/api/v1/methodology` | Methodology summary + disclaimers |

**Assess response (minimum):** decision, risk level/band, primary drivers, protective factors, recommended controls, illustrative reserve range + holding period, conditions to reduce controls, escalation triggers, confidence/data-sufficiency, methodology version, synthetic-data disclaimer, explicit limitations.

### 3.2 Decision logic principles

- Rules + transparent score; **not** presented as validated ML  
- Interaction effects (ticket × frequency, growth × tenure, prepaid × disputes, content × interruption)  
- Controls menu: monitoring, settlement delay, rolling reserve, volume limit, geo restriction, content review, subscription-practice review, fulfillment evidence, additional info, manual underwriting  
- Confidence downgrades when data-sufficiency is low  
- PD/LGD/EAD may be **retired from the public surface** or demoted to an optional internal appendix labeled “illustrative credit-style decomposition — not calibrated”

**Recommendation:** Retire PD/LGD/EAD from primary UI/API to match the strategy-lab positioning; keep a short “optional exposure sketch” in docs if useful for interview depth.

---

## 4. File disposition

### 4.1 Retain (adapt lightly)

- `LICENSE`, `CONTRIBUTING.md`, `Makefile`, `.gitignore`, `.env.example`, `docker/`, `.github/workflows/ci.yml`  
- ADR pattern under `docs/adr/` (add ADR-003: repositioning)  
- Core/API separation idea; request-ID middleware; settings/CORS  
- Test skeleton and CI gates  

### 4.2 Revise heavily

| Path | Change |
|------|--------|
| `README.md` | New name, research question, disclaimers, doc map |
| `docs/prd.md` → `docs/PRODUCT_REQUIREMENTS_DOCUMENT.md` | Strategy-lab PRD |
| `docs/architecture.md` → `docs/ARCHITECTURE.md` | New components + API |
| `docs/api.md` → `docs/API_SPECIFICATION.md` | New endpoints/schemas |
| `docs/data_dictionary.md` → `docs/DATA_DICTIONARY.md` | Archetype/scenario variables |
| `docs/synthetic_data_spec.md` → `docs/SYNTHETIC_DATA_METHODOLOGY.md` | Construction assumptions |
| `docs/model_card.md` → `docs/MODEL_CARD.md` | Demonstrator disclaimers (required text) |
| `docs/portfolio_case_study.md` → `docs/PORTFOLIO_CASE_STUDY.md` | 10-part narrative + exec summary |
| `docs/test_strategy.md` → `docs/TEST_STRATEGY.md` | Expand FE/a11y |
| `CHANGELOG.md` / `docs/CHANGELOG.md` | Repositioning entry |
| `config/*` | New policy/scoring/reserve versions (`*-0.2.0` or `strategy-1.0.0`) |
| `src/merchant_risk/*` | Refactor to interaction-aware strategy engine |
| `api/*` | New routes and schemas |
| `frontend/*` | Research + scenario lab redesign |
| `data/sample/merchants.json` | Replace with archetype scenario set |
| `pyproject.toml` | Package rename/description |
| `CURSOR_MASTER_PROMPT.md` | Archive or supersede with new master brief pointer |

### 4.3 Create (required)

- `docs/PROJECT_OVERVIEW.md`  
- `docs/RESEARCH_REPORT.md`  
- `docs/DIGITAL_GOODS_RISK_TAXONOMY.md`  
- `docs/DECISION_POLICY.md`  
- `docs/RESERVE_FRAMEWORK.md`  
- `docs/CONTENT_RISK_FRAMEWORK.md`  
- `docs/LIMITATIONS_AND_ETHICS.md`  
- `docs/INTERVIEW_TALK_TRACK.md`  
- `docs/IMPLEMENTATION_PLAN.md` (this file)  

### 4.4 Archive (do not delete authority sources)

- Move prior-positioning docs that conflict into `docs/archive/v0-credit-engine/` (or keep stubs that redirect)  
- Preserve `Project Brief - Updated.docx` untouched as historical authority; add `docs/PROJECT_BRIEF_SUPERSESSION.md` noting the 2026-08-06 research-lab brief supersedes product framing for active development  
- Deprioritize/archive validation AUC/Gini roadmap docs as optional future work, not MVP  

### 4.5 Remove or empty carefully

- Do not commit secrets (`.env` already gitignored; verify)  
- Empty `synthetic` / validation modules until reimplemented with clear non-predictive purpose  

---

## 5. Phased execution plan

### Phase 1 — Audit and plan ✅

- [x] Inspect repository  
- [x] Summarize existence and conflicts  
- [x] Propose target architecture  
- [x] File disposition  
- [x] Write this plan  

**Acceptance:** Plan reviewed; no silent overwrite of `Project Brief - Updated.docx`.

### Phase 2 — Documentation and research foundation

1. ADR-003: repositioning decision  
2. Project overview + PRD rewrite  
3. Research report (A/B sections + citations + “as of” dates)  
4. Risk taxonomy (all four families; per-risk fields)  
5. Content-risk framework  
6. Limitations & ethics + model card required language  
7. Decision policy + reserve framework (illustrative)  
8. Data dictionary + synthetic methodology  
9. Case study + interview talk track  
10. Architecture + API spec stubs aligned to target  

**Acceptance:** Recruiter can read overview + case study in ≤2 minutes and understand non-confidential positioning.

### Phase 3 — Synthetic archetypes and data

1. Define 8 archetypes (per brief)  
2. Multi-period panels: normal / growth / stress / deterioration  
3. Deterministic generator + seed  
4. Visible disclaimer on every data file  
5. Document construction assumptions  

**Acceptance:** Archetypes load via API; no proprietary-data language anywhere.

### Phase 4 — Decision demonstrator (domain)

1. New schemas for scenario inputs  
2. Interaction-aware scoring from config  
3. Control selection + illustrative reserve bands  
4. Confidence / data-sufficiency  
5. Golden unit tests for guided scenarios  

**Acceptance:** Three guided demos produce expected decision *families* with stable explanations.

### Phase 5 — API

1. Implement `/api/v1/*` endpoints  
2. Keep `/health`; optionally deprecate old `/v1/merchants/decision` with redirect note in changelog  
3. Contract tests + OpenAPI examples  
4. CORS + env configuration  

**Acceptance:** Contract tests green; sample curl scripts in docs.

### Phase 6 — Interactive scenario lab (frontend)

1. Research publication layout (comparison table, taxonomy summaries)  
2. Archetype select + variable controls  
3. Assess + compare views  
4. Three guided demonstrations  
5. Embeddable route/module notes  
6. Visual redesign away from terracotta-cream cliché while staying editorial  
7. Accessibility pass  

**Acceptance:** Recruiter can run guided demos and read why the decision changed.

### Phase 7 — Quality, CI, packaging

1. Expand tests (policy, API, FE smoke)  
2. Lint/format/typecheck  
3. Update README quick start  
4. Changelog + decision log  
5. Optional Docker update  

**Acceptance:** `make test` / CI green; local run documented.

### Phase 8 — Portfolio polish

1. Finalize case study example findings  
2. Interview talk track  
3. Static fallback for API-down portfolio use  
4. Final limitations sweep  

---

## 6. Dependencies and risks

| Risk | Mitigation |
|------|------------|
| Overclaiming via PD/EL language leftover | Global copy sweep; model card gate |
| Research stats without sources | Cite public sources; mark hypotheses; “as of” dates |
| Scope explosion (full moderation system) | Conceptual content signals only |
| Breaking prior tests during rename | Version bump; compatibility shim briefly if needed |
| Design cliché | Explicit palette/type tokens in frontend CSS variables |
| Brief conflict (docx vs new prompt) | Supersession note; preserve docx |

---

## 7. Recommended immediate next step

Execute **Phase 2** documentation/research foundation and **ADR-003**, then **Phase 3** archetypes, then domain/API/UI in order. Do not jump to a polished dashboard before taxonomy, methodology, and policy configs exist.

---

## 8. Naming proposal

| Current | Proposed |
|---------|----------|
| Folder: `P1 Merchant Credit & Reserve Decision Engine` | `P1 Digital Goods Merchant Risk Strategy Lab` (rename when convenient) |
| Package: `merchant_risk` / `merchant-credit-reserve-engine` | `dg_risk_lab` / `digital-goods-risk-strategy-lab` |
| Service title in OpenAPI | `Digital Goods Merchant Risk Strategy Lab` |

Folder rename can wait until after content migration to avoid path churn mid-edit.
