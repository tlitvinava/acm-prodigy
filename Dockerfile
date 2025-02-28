FROM python:3.12-alpine

ENV APP_HOME=/app

WORKDIR $APP_HOME

RUN mkdir -p $APP_HOME/staticfiles
RUN mkdir -p $APP_HOME/media

COPY pyproject.toml poetry.lock $APP_HOME/

RUN python -m pip install --no-cache-dir poetry==1.7.1 \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi \
    && rm -rf $(poetry config cache-dir)/{cache,artifacts}

COPY entrypoint.sh $APP_HOME/
COPY . $APP_HOME

RUN chmod +x $APP_HOME/entrypoint.sh

ENTRYPOINT ["sh", "/app/entrypoint.sh"]