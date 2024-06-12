FROM python:3.11-slim
# возьмем образ, который мы скачали ранее и в котором уже установлен python

LABEL author=${LABEL}
# добавим label, используя переменную среды

COPY . ./real_estate_app
# копируем файлы в Docker
# название директории внутри контейнера: real_estate_app

WORKDIR real_estate_app 
# изменяем рабочую директорию Docker 

RUN pip3 install -r requirements.txt
# инструкция для установки библиотек

EXPOSE ${APP_DOCKER_PORT}
# инструкции для открытия порта, указанного в переменной среды


VOLUME /models
# примонтируйте том с моделями


CMD uvicorn app.real_estate_app:app --reload --port ${APP_DOCKER_PORT} --host 0.0.0.0
# измените команду запуска, учитывая порт из .env