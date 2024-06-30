FROM python:3.10.1-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt update -y && \
    apt install -y python3-dev \
    gcc \
    musl-dev

WORKDIR /service/

COPY poetry.lock .
COPY pyproject.toml .

RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

COPY src src

EXPOSE 8000
CMD uvicorn --factory api.main:create_app --reload --port 80 --host 0.0.0.0