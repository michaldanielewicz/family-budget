FROM python:3.10-alpine
ENV PYTHONUNBUFFERED=1
RUN apk update \
    && apk add bash \
    && apk add --no-cache --virtual .build-deps \
    ca-certificates \
    gcc  \
    postgresql-dev  \
    linux-headers  \
    musl-dev \
    libffi-dev  \
    jpeg-dev  \
    zlib-dev
WORKDIR /home/app
COPY pyproject.toml poetry.lock ./
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install -n --no-ansi
COPY . .