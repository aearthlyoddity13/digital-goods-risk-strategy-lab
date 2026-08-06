# Changelog

All notable changes to this project will be documented in this file.

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
