# Prefer project venv, then PYTHON override, then python3
PYTHON ?= $(shell if [ -x .venv/bin/python ]; then echo .venv/bin/python; else echo python3; fi)

.PHONY: install test lint typecheck format run-api docker-up clean

install:
	$(PYTHON) -m pip install -e ".[dev]"

test:
	$(PYTHON) -m pytest -q

lint:
	$(PYTHON) -m ruff check src api tests

format:
	$(PYTHON) -m ruff format src api tests
	$(PYTHON) -m ruff check --fix src api tests

typecheck:
	$(PYTHON) -m mypy src api

run-api:
	$(PYTHON) -m uvicorn api.main:app --host $${HOST:-127.0.0.1} --port $${PORT:-8000} --reload

docker-up:
	docker compose -f docker/docker-compose.yml up --build

clean:
	rm -rf .pytest_cache .mypy_cache .ruff_cache **/__pycache__ *.egg-info
