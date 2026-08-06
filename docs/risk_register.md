# Risk register

| ID | Category | Risk | Mitigation | Status |
|----|----------|------|------------|--------|
| R1 | Reputational | Presenting synthetic metrics as production performance | Explicit illustrative labels; empty validation report until Phase 2 | Open |
| R2 | Data | Accidental use of confidential/real merchant data | ADR-002; UI notice; sample-only fixtures | Open |
| R3 | Model | Leakage of future outcomes into features | Data dictionary timing tags; validation checks | Open |
| R4 | Product | Score silently overrides hard policy | Policy applied after score; flags in response | Mitigated in design |
| R5 | Engineering | Scope creep before foundation | Phase 0 vertical slice discipline | Open |
| R6 | Deployment | Portfolio API unavailable | Static fallback decision + docs | Planned Phase 4 |
| R7 | Legal | Imitating employer policies/thresholds | Original parameters; public terminology | Open |
