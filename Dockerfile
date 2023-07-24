FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /home/app
RUN addgroup -S app && adduser -S app -G app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

COPY . $APP_HOME

RUN set -ex \
    && apk add --no-cache --virtual .build-deps postgresql-client build-base postgresql-dev \
    && pip install --upgrade pip

RUN pip install --no-cache-dir -r ./requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g'  $APP_HOME/entrypoint.sh
RUN chmod +x  $APP_HOME/entrypoint.sh

RUN chown -R app:app $APP_HOME

USER app

ENTRYPOINT ["/home/app/web/entrypoint.sh"]

CMD ["gunicorn", "--bind", ":5000", "config.wsgi:application", "--workers", "3", "--log-level=debug"]