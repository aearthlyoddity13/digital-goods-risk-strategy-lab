# Product requirements document — Digital Goods Merchant Risk Strategy Lab

**Owner:** Charlene Yang  
**Version:** 0.2.0-draft  
**Status:** Phase 2 foundation  
**Public-data boundary:** Aggregated and synthetic demonstration data only

## 1. Problem

Payment platforms increasingly face merchants whose products are digital: short-form drama and serialized video, web fiction, games, AI subscriptions and usage-based AI services, virtual goods, credits, and memberships. Conventional physical-goods underwriting assumptions—shipping evidence, recoverable inventory, slower fulfillment—do not map cleanly to instant, intangible consumption.

Weak strategy creates direct losses, delayed dispute exposure after payout, contingent obligations from prepaid value, content-driven platform interruptions, and unnecessary friction on legitimate growth.

## 2. Product definition

An educational and strategic prototype that combines:

1. Industry research and strategic analysis  
2. A digital-goods risk taxonomy  
3. Transparent aggregated/synthetic merchant scenarios  
4. An explainable rules-and-score decision demonstrator  
5. Interactive scenario analysis  
6. Illustrative reserve and control recommendations  
7. Explicit limitations and data-governance documentation  

## 3. Users

| Persona | Job to be done |
|---------|----------------|
| Recruiter / hiring manager | Understand problem framing, contribution, and judgment in ≤2 minutes |
| Risk / payments professional | Inspect assumptions, taxonomy, and decision logic |
| Product / strategy reviewer | Evaluate category thinking and control design |
| Portfolio visitor | Explore scenarios interactively via API-backed module |

## 4. Central and supporting questions

**Central:** How should a payment platform evaluate and control emerging digital-goods merchants when products are intangible, consumption can be immediate, transaction frequency can be high, and traditional underwriting and fulfillment evidence are limited?

**Supporting:** Why digital goods are growing; how they differ from physical goods; instant-fulfillment risks; ticket × frequency × maturity interactions; subscriptions/credits/IAP exposure; refunds/chargebacks/ATO/friendly fraud/content risk; when to approve/monitor/delay settlement/reserve/review/decline; category-specific controls; why content monitoring connects to payments risk.

## 5. In scope

- Research report with cited public sources and labeled hypotheses  
- Risk taxonomy across payment/fraud, credit/exposure, compliance/integrity, operational/reputational  
- Content-risk conceptual framework (aggregated signals → monitoring/reserve influence)  
- Synthetic merchant archetypes and multi-period scenarios  
- Explainable decisions: APPROVE / APPROVE_WITH_CONTROLS / MANUAL_REVIEW / DECLINE  
- Control and illustrative reserve recommendations  
- Versioned API and embeddable interactive lab  
- Corporate documentation set and model card  

## 6. Out of scope

- Live production underwriting or real merchant/customer data  
- Claims of real-world predictive accuracy  
- Fully automated content moderation  
- Transaction authorization in production  
- Country-specific legal advice or formal regulatory certification  
- Opaque machine-learning models presented as validated  

## 7. Functional requirements

1. Present research narrative and comparison of digital vs traditional goods.  
2. Expose taxonomy and content-risk framework in docs and API metadata.  
3. Load archetypes; allow scenario variable adjustment; assess and compare.  
4. Return decision, risk level, drivers, protective factors, controls, illustrative reserve, escalation/reduce-control conditions, confidence, methodology version, synthetic-data disclaimer, limitations.  
5. Keep thresholds in version-controlled policy files.  
6. Disclose synthetic/aggregated data on every data file and primary UI.  
7. Support portfolio embedding via env-configured API base URL and CORS allowlist.

## 8. Non-functional requirements

Explainability, reproducibility (seeds, versions), reliability (validation, tests, health), security (no secrets, no PII retention), accessibility (WCAG AA target), maintainable modular architecture, concise corporate documentation.

## 9. Success metrics (portfolio)

| Metric | Target |
|--------|--------|
| Time-to-understand | Recruiter grasps problem + contribution ≤2 minutes |
| Inspectability | Risk professional can trace a decision to policy rules |
| Interactivity | ≥3 guided demos + free-form scenario controls |
| Governance | Model card + limitations + synthetic disclosures present |
| Quality | Documented tests and checks pass |

## 10. Acceptance criteria (definition of done — excerpt)

Aligned to project DoD: clear positioning, digital-vs-traditional distinction, content↔payments linkage, interactive scenarios, explained decisions, synthetic disclosures, no proprietary-data implication, documented API, embeddable module, polished responsive accessible UI, tests pass.

## 11. Supersession

This PRD supersedes the v0 “Merchant Credit & Reserve Decision Engine” PRD for active development. Historical brief preserved; see [PROJECT_BRIEF_SUPERSESSION.md](PROJECT_BRIEF_SUPERSESSION.md).
