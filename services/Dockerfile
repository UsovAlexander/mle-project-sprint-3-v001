FROM python:3.11-slim

LABEL author=${AUTHOR}

COPY . ./real_estate_app

WORKDIR real_estate_app 

RUN pip3 install -r requirements.txt

EXPOSE ${APP_DOCKER_PORT}

VOLUME /models

CMD uvicorn app.real_estate_app:app --reload --port ${APP_DOCKER_PORT} --host 0.0.0.0