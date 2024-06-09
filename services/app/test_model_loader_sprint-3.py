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
            pipeline = dill.load(file)
        print("Model loaded successfully")
    except Exception as e:
        print(f"Failed to load model: {e}")
    return pipeline


if __name__ == "__main__":
    pipeline = load_real_estate_model(model_path="models/pipeline.pkl")
    print(f"Model parameter names: {pipeline[0].feature_names_in_}")
