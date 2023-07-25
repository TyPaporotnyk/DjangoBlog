FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /home/app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

COPY . $APP_HOME

RUN set -ex \
    && apk add --no-cache --virtual .build-deps postgresql-client build-base postgresql-dev \
    && pip install --upgrade pip

RUN pip install --no-cache-dir -r ./requirements.txt