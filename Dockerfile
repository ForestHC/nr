FROM python:3.10-slim AS builder

ENV POETRY_VERSION=1.5.0
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

RUN python3 -m venv $POETRY_VENV \
  && $POETRY_VENV/bin/pip install -U pip setuptools \
  && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

ENV PATH="${PATH}:${POETRY_VENV}/bin"

WORKDIR /app

COPY pyproject.toml poetry.lock /app

RUN poetry config virtualenvs.create false \
  && poetry install --without dev \
  && poetry export --format requirements.txt --output requirements.txt

FROM python:3.10-slim

RUN apt-get update \
  && apt-get install -qy curl \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY nr /app/nr
COPY --from=builder /app/requirements.txt /app

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 8000

CMD ["uvicorn", "nr.main:app", "--host", "0.0.0.0"]
