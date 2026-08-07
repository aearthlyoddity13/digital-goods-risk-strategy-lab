FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml README.md ./
COPY src ./src
COPY api ./api
COPY config ./config
COPY data ./data

RUN pip install --no-cache-dir -e .

RUN addgroup --system app && adduser --system --ingroup app app

ENV HOST=0.0.0.0
ENV PORT=8000
EXPOSE 8000

USER app

CMD ["sh", "-c", "uvicorn api.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
