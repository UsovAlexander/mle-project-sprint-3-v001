# coding: utf-8
"""Класс FastApiHandler, который обрабатывает запросы API."""

import dill
import pandas as pd
from sklearn.pipeline import Pipeline, FunctionTransformer
from sklearn.preprocessing import StandardScaler, PolynomialFeatures, KBinsDiscretizer
from catboost import CatBoostClassifier


class FastApiHandler:
    """Класс FastApiHandler, который обрабатывает запрос и возвращает предсказание."""

    def __init__(self):
        """Инициализация переменных класса."""

        # Типы параметров запроса для проверки
        self.param_types = {
            "flat_id": str,
            "model_params": dict
        }

        self.model_path = "models/model_cb.bin"
        self.load_real_estate_model(model_path=self.model_path)
        
        # Необходимые параметры для предсказаний модели оттока
        self.required_model_params = [
            'floor', 'is_apartment', 'kitchen_area', 'living_area', 'rooms',  'studio', 'total_area',
            'build_year', 'building_type_int', 'latitude', 'longitude', 'ceiling_height', 'flats_count', 'floors_total', 'has_elevator'
        ]

    def load_real_estate_model(self, model_path: str):
        """Загружаем обученную модель оттока.
        Args:
            model_path (str): Путь до модели.
        """
        try:
            print("Start model loading")
            with open(model_path, 'rb') as file:
                self.model = dill.load(file)
            print("Model loaded successfully")
        except Exception as e:
            print(f"Failed to load model: {e}")

    def real_estate_predict(self, model_params: dict) -> float:
        """Предсказываем вероятность оттока.

        Args:
            model_params (dict): Параметры для модели.

        Returns:
            float - вероятность оттока от 0 до 1
        """
        param_values_list = pd.DataFrame(model_params, index=[0])
        return self.model.predict(param_values_list)[0]
        
    def check_required_query_params(self, query_params: dict) -> bool:
        """Проверяем параметры запроса на наличие обязательного набора параметров.
        
        Args:
            query_params (dict): Параметры запроса.
        
        Returns:
                bool: True - если есть нужные параметры, False - иначе
        """
        if "flat_id" not in query_params or "model_params" not in query_params:
            return False
        
        if not isinstance(query_params["flat_id"], self.param_types["flat_id"]):
            return False
                
        if not isinstance(query_params["model_params"], self.param_types["model_params"]):
            return False
        return True
    
    def check_required_model_params(self, model_params: dict) -> bool:
        """Проверяем параметры пользователя на наличие обязательного набора.
    
        Args:
            model_params (dict): Параметры пользователя для предсказания.
    
        Returns:
            bool: True - если есть нужные параметры, False - иначе
        """
        if set(model_params.keys()) == set(self.required_model_params):
            return True
        return False
    
    def validate_params(self, params: dict) -> bool:
        """Разбираем запрос и проверяем его корректность.
    
        Args:
            params (dict): Словарь параметров запроса.
    
        Returns:
            - **dict**: Cловарь со всеми параметрами запроса.
        """
        if self.check_required_query_params(params):
            print("All query params exist")
        else:
            print("Not all query params exist")
            return False
        
        if self.check_required_model_params(params["model_params"]):
            print("All model params exist")
        else:
            print("Not all model params exist")
            return False
        return True
		
    def handle(self, params):
        """Функция для обработки запросов API параметров входящего запроса.
    
        Args:
            params (dict): Словарь параметров запроса.
    
        Returns:
            - **dict**: Словарь, содержащий результат выполнения запроса.
        """
        try:
            # Валидируем запрос к API
            if not self.validate_params(params):
                print("Error while handling request")
                response = {"Error": "Problem with parameters"}
            else:
                model_params = params["model_params"]
                flat_id = params["flat_id"]
                print(f"Predicting for flat_id: {flat_id} and model_params:\n{model_params}")
                # Получаем предсказания модели
                price = self.real_estate_predict(model_params)
                response = {
                    "flat_id": flat_id, 
                    "price": price
                }
        except Exception as e:
            print(f"Error while handling request: {e}")
            return {"Error": "Problem with request"}
        else:
            return response

if __name__ == "__main__":

    # Создаем тестовый запрос
    test_params = {
	    "flat_id": "123",
        "model_params": {
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
    }

    # Создаем обработчик запросов для API
    handler = FastApiHandler()

    # Делаем тестовый запрос
    response = handler.handle(test_params)
    print(f"Response: {response}")
