"""FastAPI-приложение для модели оттока."""

from fastapi import FastAPI, Body
from .fast_api_handler import FastApiHandler

"""
Пример запуска из директории mle-project-sprint-3-v001/services/app:
uvicorn real_estate_app:app --reload --port 8081 --host 0.0.0.0

Для просмотра документации API и совершения тестовых запросов зайти на http://127.0.0.1:8081/docs

Если используется другой порт, то заменить 8081 на этот порт
"""

# создаём FastAPI-приложение 
app = FastAPI()

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
    return price_prediction