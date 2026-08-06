# Audit and plan — Digital Goods Merchant Risk Strategy Lab

**Date:** 2026-08-06  
**Status:** Phase 1 complete · Phase 2 docs complete · Phase 3 data/policy draft started  
**Prior product name:** Merchant Credit & Reserve Decision Engine  
**Target product name:** Digital Goods Merchant Risk Strategy Lab

---

## 1. Current-state summary

The repository contains a working Sprint 0 vertical slice framed as an explainable **credit and rolling-reserve decision engine**.

| Layer | Status |
|-------|--------|
| Authority sources | `Project Brief - Updated.docx`, `CURSOR_MASTER_PROMPT.md` (engine + PD/LGD/EAD roadmap) |
| Domain | `src/merchant_risk/` — scorecard → PD → EAD/LGD/EL → hard rules → reserve |
| Config | `scorecard-0.1.0`, `policy-0.1.0` YAML |
| API | FastAPI: `GET /health`, `POST /v1/merchants/decision` |
| Data | 4 synthetic merchants; empty `data/generated/` |
| Frontend | Static sample → decision UI; editorial cream/terracotta palette |
| Tests/CI | Unit + contract tests; GitHub Actions; Makefile; Docker |
| Research | No research report, taxonomy, or content-risk framework |
| Notebooks / design assets | None |

**Preserve:** core/API separation, synthetic-data boundary, four decision actions, reason codes, versioned YAML, CORS/env config, CI tooling.

---

## 2. Repositioning gaps

| Gap | Gap severity |
|-----|--------------|
| Product reads as production-style underwriting software | High |
| PD/LGD/EAD primary surface implies calibrated credit model | High |
| Missing research narrative and digital-vs-physical comparison | High |
| Content monitoring out of MVP; must become a pillar | High |
| No merchant archetypes / multi-period stress scenarios | High |
| API paths and payloads do not match strategy-lab contract | Medium |
| UI is not an interactive scenario lab | Medium |
| Required corporate doc set incomplete / misnamed | Medium |
| Validation AUC/Gini roadmap overweighted vs strategy demo | Medium |
| Visual language risks generic “AI fintech” cream/terracotta | Low–Medium |
| Residual PayPal mentions only as “do not use” — keep, but strengthen “no confidential data” disclosures everywhere | Low |

---

## 3. Proposed information architecture

Public narrative flow (site + case study):

1. Executive summary (problem → question → approach → deliverable → insight → limitations)  
2. Market shift toward digital goods  
3. Why conventional frameworks need adaptation  
4. Category differences (short drama, web fiction, games, AI)  
5. Risk taxonomy  
6. Content monitoring → payments risk  
7. Decision and reserve framework  
8. Interactive scenarios  
9. Example findings  
10. Best practices  
11. Limitations and next steps  

Doc map (canonical filenames):

| Doc | Role |
|-----|------|
| `PROJECT_OVERVIEW.md` | Two-minute recruiter entry |
| `PRODUCT_REQUIREMENTS_DOCUMENT.md` | Scope, users, acceptance |
| `RESEARCH_REPORT.md` | Evidence + analysis |
| `DIGITAL_GOODS_RISK_TAXONOMY.md` | Risk catalog |
| `CONTENT_RISK_FRAMEWORK.md` | Content → payments linkage |
| `SYNTHETIC_DATA_METHODOLOGY.md` | Scenario construction |
| `DATA_DICTIONARY.md` | Variables |
| `DECISION_POLICY.md` | Rules and score logic |
| `RESERVE_FRAMEWORK.md` | Illustrative reserves |
| `MODEL_CARD.md` | Demonstrator governance |
| `LIMITATIONS_AND_ETHICS.md` | Boundaries |
| `ARCHITECTURE.md` / `API_SPECIFICATION.md` | System + API |
| `PORTFOLIO_CASE_STUDY.md` / `INTERVIEW_TALK_TRACK.md` | Portfolio packaging |
| `TEST_STRATEGY.md` / `CHANGELOG.md` | Quality |

---

## 4. Proposed technical architecture

```text
frontend/          Research publication + scenario lab (embeddable)
       │ HTTPS/JSON
api/               FastAPI adapter: /health, /api/v1/*
       │
src/…              Framework-free strategy library
  domain/          Assess + compare orchestration
  scoring/         Interaction-aware illustrative score
  policy/          Decision + controls
  reserve/         Illustrative bands
  content/         Content-signal influence
  scenarios/       Growth/stress transforms
  synthetic/       Seeded archetype generation
config/            Versioned policy / scoring / reserve YAML
data/archetypes/   Synthetic scenarios + disclaimer
docs/              Research + governance
tests/             Unit, contract, FE smoke
```

**API target:** `GET /health`, `GET /api/v1/archetypes`, `GET /api/v1/risk-factors`, `POST /api/v1/assess`, `POST /api/v1/compare`, `GET /api/v1/methodology`.

**Decision surface:** APPROVE / APPROVE_WITH_CONTROLS / MANUAL_REVIEW / DECLINE + controls + illustrative reserve + explanations + confidence + disclaimer.  
**Retire from primary API:** PD, LGD, EAD, EL (optional appendix only).

---

## 5. Documentation plan

Phase 2 creates/rewrites the canonical set above; archives v0 engine docs under `docs/archive/v0-credit-engine/`; preserves `Project Brief - Updated.docx` with a supersession note.

Writing rules: concise corporate tone; separate evidence / inference / demo assumptions; cite sources with “as of” dates; no inflated claims.

---

## 6. Synthetic-data plan

Eight archetypes (short-drama coins, web fiction, game+gifting, AI subscription, AI usage API, high-growth cross-border, mature low-risk subscription, complaint/chargeback deterioration).  
Multi-period panels: normal, growth, stress, deterioration.  
Aggregated variables only (no customer-level PII).  
Deterministic seed; documented assumptions.  
Visible disclaimer on every data file and UI surface:  
“Demonstration data: aggregated and synthetic. No confidential merchant, customer or payment-platform data is used.”

---

## 7. Decision-policy plan

Rules-and-score demonstrator in versioned YAML.  
Score reflects interactions (ticket × frequency, growth × tenure, prepaid × disputes, content × interruption risk).  
Controls menu: monitoring tiers, settlement delay, rolling reserve, volume limit, geo restriction, content review, subscription-practice review, fulfillment evidence, additional info, manual underwriting.  
Illustrative reserve ranges and holding periods — not mathematically optimal.  
Each result: decision, risk level, drivers, protective factors, controls, reserve, reduce-control conditions, escalation triggers, confidence, limitations.

---

## 8. Visual-design plan

Editorial research publication + interactive prototype.  
Light neutral/off-white ground, charcoal text, one restrained accent (cool slate-teal or ink-blue — not purple, not terracotta cliché).  
Expressive but disciplined type: strong display + clean sans body + mono for variables.  
Asymmetric controlled layouts, thin rules, numbered sections.  
Charts that explain ticket/frequency/exposure/disputes/reserves relationships.  
Subtle motion for hierarchy only.  
WCAG-oriented risk colors; responsive; no crypto clichés, glassmorphism, or dense metric dashboards.

---

## 9. Implementation milestones

| Phase | Focus | Exit criteria |
|-------|-------|---------------|
| **1** | Audit and plan | This document accepted; no broad rewrite before it |
| **2** | Research and documentation foundation | Overview, PRD, research structure, taxonomy, synthetic methodology, decision/reserve policies, limitations/governance |
| **3** | Scenario and policy engine | Archetypes, deterministic scenarios, explainable logic, reserves/controls, boundary tests |
| **4** | API | Versioned assess/compare + schemas + tests + docs |
| **5** | Interactive research experience | Exec summary, narrative, viz, scenario lab, explanations, portfolio-ready embed |
| **6** | Verification | Tests/quality, citations, disclosures, no proprietary claims, a11y/responsive, deploy instructions, final summary |

Each stage: small PR-sized change → changelog update → stage summary (what / why / verified).

---

## 10. Risks, assumptions and open questions

**Risks**

- Research statistics vary by vendor definition — mitigate with citations and claim labeling.  
- Overclaiming via leftover credit-model language — mitigate with copy sweeps and model-card gate.  
- Scope creep into full content moderation — stay conceptual/aggregated.  

**Assumptions**

- Portfolio recruiters value strategic reasoning over predictive metrics.  
- Synthetic scenarios are sufficient to teach control logic.  
- Static HTML/JS frontend remains acceptable for embeddability (React optional later).  

**Open questions**

1. Rename folder/package now or after Phase 2? **Default:** after Phase 2 content lands.  
2. Keep legacy `/v1/merchants/decision` temporarily? **Default:** deprecate after `/api/v1/assess` ships; document in changelog.  
3. Host research charts as static SVG/CSS first, or add a chart library? **Default:** CSS/SVG first.  

---

## Acceptance criteria (Phase 1)

- [x] Repository inspected  
- [x] Current state summarized  
- [x] Conflicts identified  
- [x] Target information and technical architectures proposed  
- [x] File disposition and milestones defined  
- [x] Risks / assumptions / open questions listed  
- [x] No broad rewrite begun before this audit existed  
