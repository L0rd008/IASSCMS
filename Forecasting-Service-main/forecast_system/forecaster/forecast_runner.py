import joblib
import importlib
import pandas as pd
import os
from .utils.warehouse_api import get_current_stock

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, 'models')


def forecast_for_product(product_SKU: str, days: int = 30) -> dict:
    model_path = os.path.join(MODEL_DIR, f"{product_SKU}.joblib")
    if not os.path.isfile(model_path):
        return {"error": f"Model for '{product_SKU}' not found."}

    try:
        model = joblib.load(model_path)
        pipeline = importlib.import_module(f'forecaster.feature_pipelines.pipeline')

        future_dates = pd.DataFrame({'ds': pd.date_range(start=pd.Timestamp.today(), periods=days)})
        features = pipeline.prepare_features(future_dates.copy())
        forecast = model.predict(features)

        current_stock = get_current_stock(product_SKU)
        total_forecast = round(forecast['yhat'].sum(), 2)

        total_maximum = round(forecast['yhat_upper'].sum(), 2)
        total_minimum = round(forecast['yhat_lower'].sum(), 2)
        stock_shortfall = max(0, round(total_forecast - current_stock, 2))

        # Convert dates to string format YYYY-MM-DD
        forecast_copy = forecast.copy()
        forecast_copy['ds'] = forecast_copy['ds'].dt.strftime('%Y-%m-%d')

        return {
            "product_SKU": product_SKU,
            "current_stock": current_stock,
            "average_forecasted_demand": total_forecast,
            "maximum_forecast": total_maximum,
            "minimum_forecast": total_minimum,
            "stock_shortfall": stock_shortfall,
            "daily_predictions": forecast_copy[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].rename(columns={
            'ds': 'date', 'yhat': 'predicted', 'yhat_lower': 'lower_bound', 'yhat_upper': 'upper_bound'
            }).round({'predicted': 2, 'lower_bound': 2, 'upper_bound': 2}).to_dict(orient='records')
        }

    except Exception as e:
        return {"error": f"Failed to forecast for '{product_SKU}': {str(e)}"}
