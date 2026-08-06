# Portfolio case study (draft)

**Project:** Digital-Product Merchant Credit & Reserve Decision Engine  
**Status:** In progress — Phase 0 / illustrative baseline

## Problem

Digital-product merchants need underwriting and reserve strategies that reflect instant delivery, intangible goods, and thin history—without blocking legitimate growth.

## Decision

Build an explainable, API-first engine that returns APPROVE / APPROVE_WITH_CONTROLS / MANUAL_REVIEW / DECLINE plus a traceable rolling reserve, with expected-loss economics visible to reviewers.

## Methodology

Transparent component scorecard → calibrated PD → EAD/LGD/EL → hard policy → reserve floors/caps. Synthetic merchants only.

## Findings

_Pending Phase 2 validation._

## Trade-offs

Approval vs loss vs reserve friction vs manual-review capacity; transparency vs potential lift from opaque models (challenger only after baseline evidence).

## Limitations

Synthetic data; illustrative coefficients; no production performance claims.

## Personal contribution

Product framing, risk methodology design, architecture, implementation, documentation, and portfolio packaging (in progress).

## Links

- [PRD](prd.md) · [Architecture](architecture.md) · [Model card](model_card.md) · [API](api.md)
