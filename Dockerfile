FROM python:3.11-alpine

COPY ./ ./app
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN set -ex \
    && apk add --no-cache --virtual .build-deps postgresql-client build-base postgresql-dev \
    && pip install --upgrade pip

RUN pip install --no-cache-dir -r ./requirements.txt

EXPOSE 8000
