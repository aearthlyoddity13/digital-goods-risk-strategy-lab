# Digital Goods Merchant Risk Strategy Lab

Research-led strategy demonstrator for how payment platforms could evaluate **emerging digital-goods merchants** (short drama, web fiction, games, AI services, virtual goods)—without implying use of confidential processor or merchant data.

**Status:** Phase 2 documentation foundation (repositioning from Sprint 0 credit/reserve engine).  
**Data boundary:** Aggregated and synthetic demonstration data only.  
**Not:** A production underwriting model. Thresholds are illustrative. No predictive-accuracy claims.

## Central question

How should a payment platform evaluate and control emerging digital-goods merchants when products are intangible, consumption can be immediate, transaction frequency can be high, and traditional underwriting and fulfillment evidence are limited?

## Quick start

Requires **Python 3.11+** (3.12 recommended).

```bash
python3.12 -m venv .venv
source .venv/bin/activate
make install
cp .env.example .env
make test
make run-api
```

- API: http://127.0.0.1:8000 (Sprint 0 endpoints still present during transition)  
- OpenAPI: http://127.0.0.1:8000/docs  
- UI: `cd frontend && python3 -m http.server 5173`  

> Note: Phase 4 replaces the primary API with `/api/v1/assess` and related routes. Until then, legacy `POST /v1/merchants/decision` remains for regression.

## Documentation

Start at [docs/PROJECT_OVERVIEW.md](docs/PROJECT_OVERVIEW.md) · index [docs/README.md](docs/README.md) · audit [docs/AUDIT_AND_PLAN.md](docs/AUDIT_AND_PLAN.md)

## Disclaimer

Demonstration data: aggregated and synthetic. No confidential merchant, customer or payment-platform data is used.

## License

MIT — see [LICENSE](LICENSE).
