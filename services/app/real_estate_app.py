"""FastAPI-приложение для модели оттока."""

from fastapi import FastAPI, Body
from .fast_api_handler import FastApiHandler
from fastapi.responses import PlainTextResponse
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Histogram
from prometheus_client import Counter

"""
Пример запуска из директории mle-project-sprint-3-v001/services/app:
uvicorn real_estate_app:app --reload --port 8081 --host 0.0.0.0

Для просмотра документации API и совершения тестовых запросов зайти на http://127.0.0.1:8081/docs

Если используется другой порт, то заменить 8081 на этот порт
"""

# создаём FastAPI-приложение 
app = FastAPI()

# инициализируем и запускаем экпортёр метрик
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

main_app_predictions = Histogram(
    # имя метрики
    "main_app_predictions",
    #описание метрики
    "Histogram of predictions",
    #указаываем корзины для гистограммы
    buckets=(1, 2, 4, 5, 10)
)

main_app_counter_pos = Counter("main_app_counter_pos", "Count of positive predictions")

# создаём обработчик запросов для API
app.handler = FastApiHandler()

# ваш код функции-обработчика get_prediction_for_item здесь
@app.post("/api/price/")
def get_prediction_for_item(flat_id: str, model_params: dict):
    all_params = {
        "flat_id": flat_id,
        "model_params": model_params
    }
    price_prediction = app.handler.handle(all_params)
    main_app_predictions.observe(price_prediction)
    if price_prediction > 0:
        main_app_counter_pos.inc()
    return price_prediction