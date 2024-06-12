# Инструкции по запуску микросервиса

### 1. FastAPI микросервис в виртуальном окружение

Введите следующие команды для запуска микросервиса:
```
python3.10 -m venv .mle-sprint3-venv
source .mle-sprint3-venv/bin/activate
uvicorn real_estate_app:app --reload --port 8081 --host 0.0.0.0
```
Для просмотра документации API и совершения тестовых запросов зайти на http://127.0.0.1:8081/docs .
После запуска через Swagger UI для проверки необходимо вбить тестовые параметры:

flat_id: 123

Request body:

{
"floor": 9,
"is_apartment": 0,
"kitchen_area": 9.9,
"living_area": 19.9,
"rooms": 0.0,
"studio": 0,
"total_area": 35.099998,
"build_year": 1965,
"building_type_int": 6,
"latitude": 55.717113,
"longitude": 37.781120,
"ceiling_height": 3.0,
"flats_count": 84,
"floors_total": 12,
"has_elevator": 1
}


### 2. FastAPI микросервис в Docker-контейнере
Чтобы запустить контейнер из директории /services необходимо запустить следующую команду:

docker container run --publish 4601:8081 --volume=./models:/real_estate_app/models   --env-file .env real_estate:1

либо в фоновом режиме:

docker container run --publish 4601:8081 -d --volume=./models:/real_estate_app/models   --env-file .env real_estate:1

Для остановки контейнера найдите ID или name контейнера через команду docker ps, затем введите docker stop (ID или name)
