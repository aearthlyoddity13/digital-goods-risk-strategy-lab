# Changelog

All notable changes to this project will be documented in this file.

## [0.6.0-research-model-alignment] — 2026-08-08

- Added the research-to-model gap audit.
- Added AI credit-ledger, renewal, metering, account/key-abuse and postpaid-exposure fields.
- Added targeted controls, drivers and golden tests.
- Advanced the methodology to `strategy-0.4.0`.

## [0.5.0-ai-services-research] — 2026-08-07

- Added the flagship AI subscriptions, credits, usage and account-abuse chapter.
- Added supporting first-party product-structure and API-security evidence.
- Linked AI payment mechanisms to AI-01–AI-03 decisions and control-release conditions.

## [0.4.0-short-drama-research] — 2026-08-07

- Added the flagship short-drama coin-system and post-consumption risk chapter.
- Added supporting market, product-mechanics and digital-dispute evidence to the source register.
- Linked research mechanisms to the implemented SD-01–SD-03 scenarios and release conditions.

## [0.3.1-calibration] — 2026-08-07

- Probability-weighted uncovered contingent exposure.
- Ecosystem-adjusted posture selection including merchant liquidity burden.
- Least-restrictive balanced-growth near-equivalence rule.
- Implemented findings added to the portfolio case study.
- Posture assumptions advanced to `postures-0.2.0`; 36 tests pass.

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
