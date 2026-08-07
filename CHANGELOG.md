# Changelog

All notable changes to this project will be documented in this file.

## [0.7.0-portfolio-publication] — 2026-08-08

### Added

- Recruiter-first publication package with exact public copy, progressive disclosure, visibility rules and acceptance criteria.
- Single-route MECE architecture connecting the general framework, category applications, scenario evidence, interactive lab and governance.
- Copy-ready Cursor prompt for integrating P1 into the portfolio without exposing internal project artifacts.
- Publication-readiness audit covering approved claims, source scope, required live destinations, repository risk and go/no-go criteria.

## [0.6.0-research-model-alignment] — 2026-08-08

### Added

- Research-to-model gap audit with quantitative, qualitative and excluded indicator dispositions.
- AI service-credit ledger validation.
- Renewal-conduct, usage-meter integrity, anomalous usage, account/API-key compromise and postpaid-exposure inputs.
- Targeted AI subscription, meter, account/key and usage-limit controls with explanation drivers.
- Golden tests for credit reconciliation, renewal stress and concentrated key-abuse stress.

### Changed

- Methodology advanced to `strategy-0.4.0`; policy advanced to `balanced-growth-0.2.0`.
- AI-01–AI-03 scenarios now encode the mechanisms described in the AI-services research chapter.

## [0.5.0-ai-services-research] — 2026-08-07

### Added

- Flagship AI-services research chapter covering subscriptions, prepaid credits, usage-based billing, account/API-key abuse, reliability, provider dependency, integrity and compute-cost exposure.
- Decision-ready indicator map, control ladder, release conditions and AI-01–AI-03 interpretations.
- First-party credit/billing structures and NIST API-protection guidance added to the source register with limitations.

## [0.4.0-short-drama-research] — 2026-08-07

### Added

- Flagship short-drama research chapter covering the direct-web coin lifecycle, post-consumption disputes, customer conduct, contingent exposure, content continuity and viral cross-border growth.
- Decision-ready indicator map, control ladder, release conditions and SD-01–SD-03 interpretations.
- Current market, first-party product and digital-dispute evidence added to the source register with explicit limitations.

## [0.3.1-calibration] — 2026-08-07

### Changed

- Probability-weighted uncovered contingent exposure instead of treating the full uncovered obligation gap as expected loss.
- Posture selection now compares platform contribution after merchant reserve-liquidity burden.
- Balanced growth is preferred when economically near-equivalent to a more restrictive eligible posture; manual-review stress cases retain case-specific selection.
- Posture assumption version advanced to `postures-0.2.0`.
- Portfolio case study now reports implemented scenario findings rather than pending placeholders.

### Verification

- Added golden tests for healthy, recovery and severe-stress posture behavior.
- Full suite: 36 tests passed.

## [0.3.0-strategy-slice] — 2026-08-07

### Added

- Employer-neutral research question tree, evidence register and indicator priorities.
- Balanced-growth risk appetite and commercial objective.
- Direct-web synthetic scenario catalog and numerical calibration specification.
- Normalized and USD 1,000,000 illustrative commercial views.
- Strategy-lab domain models, coin-ledger validation, assessment and commercial calculator.
- `POST /api/v1/assess` and `GET /api/v1/methodology`.
- Unit and API contract tests for the strategy-lab vertical slice.
- Versioned YAML catalog generating eight scenarios across four periods (32 records).
- `GET /api/v1/archetypes` and scenario-reference `POST /api/v1/compare`.
- Golden-decision tests for combined stress mechanisms and balanced-growth manual review.
- Versioned permissive, balanced-growth and conservative policy-effect assumptions.
- `POST /api/v1/compare-postures` with risk-appetite-constrained recommendation logic.

### Changed

- Confirmed direct-web payment scope; app-store billing is excluded.
- Confirmed purchased coins are non-expiring, non-transferable and non-cash-redeemable.
- API public title now reflects the Digital Goods Merchant Risk Strategy Lab.

### Verification

- Ruff formatting and lint passed.
- Mypy passed for the new strategy-lab source and route.
- Full suite: 31 tests passed.
- `git diff --check` passed.

## [0.2.0-docs] — 2026-08-06

### Changed

- Repositioned product identity from “Merchant Credit & Reserve Decision Engine” to **Digital Goods Merchant Risk Strategy Lab** (ADR-003).
- Archived Sprint 0 engine docs under `docs/archive/v0-credit-engine/`.
- Rewrote README and documentation index for research-led strategy-lab framing.

### Added

- `docs/AUDIT_AND_PLAN.md` — Phase 1 audit return.
- `docs/PROJECT_OVERVIEW.md`, `docs/PRODUCT_REQUIREMENTS_DOCUMENT.md`.
- `docs/RESEARCH_REPORT.md`, `docs/DIGITAL_GOODS_RISK_TAXONOMY.md`, `docs/CONTENT_RISK_FRAMEWORK.md`.
- `docs/SYNTHETIC_DATA_METHODOLOGY.md`, `docs/DATA_DICTIONARY.md`.
- `docs/DECISION_POLICY.md`, `docs/RESERVE_FRAMEWORK.md`.
- `docs/MODEL_CARD.md`, `docs/LIMITATIONS_AND_ETHICS.md`.
- `docs/ARCHITECTURE.md`, `docs/API_SPECIFICATION.md`, `docs/TEST_STRATEGY.md`.
- `docs/PORTFOLIO_CASE_STUDY.md`, `docs/INTERVIEW_TALK_TRACK.md`.
- `docs/PROJECT_BRIEF_SUPERSESSION.md`, `docs/adr/003-repositioning-to-strategy-lab.md`.
- `data/archetypes/archetypes.json` — eight archetypes × four periods (synthetic).
- `config/policy/policy-strategy-0.2.0.yaml` — illustrative strategy-lab policy draft.

### Notes

- Application code still runs the Sprint 0 credit-engine API until Phase 3 engine cutover.
- PD/LGD/EAD remain in legacy code paths only; not part of the new public strategy surface.

### Verification

- Documentation set present and cross-linked from `docs/README.md`.
- Historical brief (`Project Brief - Updated.docx`) preserved untouched.
- Archetype JSON parses; contains required synthetic-data disclaimer.
- Legacy automated tests not modified in this stage (still target Sprint 0 API).

## [0.1.0] — 2026-08-06

### Added

- Phase 0 foundation: docs, ADRs, data dictionary, synthetic-data spec.
- Transparent scorecard baseline (`scorecard-0.1.0`) and policy (`policy-0.1.0`).
- `GET /health` and `POST /v1/merchants/decision`.
- Deterministic sample merchants for all four actions.
- Unit and contract tests, CI workflow, Docker skeleton.
- Minimal editorial reviewer page with API fallback.
