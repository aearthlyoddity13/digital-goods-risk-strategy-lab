# Contributing

This is a portfolio project owned by Charlene Yang. External contributions are not expected; the notes below document the engineering conventions used in-repo.

## Conventions

- Conventional commits (`feat:`, `fix:`, `docs:`, `test:`, `chore:`).
- PR-sized changes; update docs and tests with behavior.
- Record material choices in `docs/adr/` and `docs/decision_log.md`.
- Never commit secrets, real merchant/customer data, or confidential employer material.
- Do not claim predictive performance without Phase 2 validation evidence.

## Local checks

```bash
make format
make lint
make typecheck
make test
```
