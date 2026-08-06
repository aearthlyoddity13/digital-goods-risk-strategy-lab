# ADR-002: Synthetic data and public-use boundary

**Status:** Accepted  
**Date:** 2026-08-06  
**Deciders:** Charlene Yang (portfolio owner)

## Context

This is a public portfolio project. Using, inferring, or imitating confidential employer (e.g., PayPal) data, policies, thresholds, source code, or internal terminology would create legal and reputational risk. Real merchant PII must not enter the demo.

## Decision

1. All demonstration merchants and outcomes are **synthetic**, deterministic given a documented seed.  
2. UI and docs include a clear **public-data notice** prohibiting uploads of real personal, customer, or confidential merchant data.  
3. Performance metrics from synthetic data are labeled **illustrative** until Phase 2 validation exists; even then, they are not claimed as production platform performance.  
4. Field names and policy parameters are original to this project, not copied from confidential systems.

## Alternatives considered

| Option | Why not |
|--------|---------|
| Anonymized real production extracts | Residual re-identification and confidentiality risk |
| Public merchant registries as decision inputs | Incomplete for risk labels; still not a production loss process |
| Undocumented “realistic” random data | Non-reproducible; reviewer cannot audit assumptions |

## Consequences

- Requires a written synthetic-data specification before generation.  
- Cannot claim real-world predictive effectiveness from this dataset alone.  
- Strengthens portfolio credibility on governance and ethics.
