import dill
import pandas as pd
from sklearn.pipeline import Pipeline, FunctionTransformer
from sklearn.preprocessing import StandardScaler, PolynomialFeatures, KBinsDiscretizer
from catboost import CatBoostClassifier


def load_real_estate_model(model_path: str):
    """Загружаем обученную модель оттока.
    Args:
        model_path (str): Путь до модели.
    """
    try:
        print("Start model loading")
        with open(model_path, 'rb') as file:
            model = dill.load(file)
        print("Model loaded successfully")
    except Exception as e:
        print(f"Failed to load model: {e}")
    return model


if __name__ == "__main__":
    model = load_real_estate_model(model_path="models/model_cb.bin")
    print(f"Model parameter names: {model.feature_names_}")
