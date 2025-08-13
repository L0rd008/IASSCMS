# 📦 Forecasting Service – Django-based Demand Prediction

This microservice forecasts product demand using pre-trained ML models and integrates with a warehouse service to determine restocking needs.

---

## 🗂️ Project Structure

| Folder/File              | Purpose                                                  |
|--------------------------|----------------------------------------------------------|
| `forecast_system/`       | Main Django project config (settings, URLs, wsgi/asgi)   |
| `forecaster/`            | App containing all forecast logic                        |
| `feature_pipelines/`     | Per-product feature engineering modules                  |
| `models/`                | Pre-trained `.joblib` models for each product            |
| `utils/warehouse_api.py` | Makes HTTP requests to warehouse management service      |
| `forecast_runner.py`     | Orchestrates model loading, forecasting, warehouse fetch |
| `views.py`               | Exposes the forecast API endpoint                        |
| `migrations/`            | Django migration folder                                  |
| `manage.py`              | Django project entry point                               |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/IASSCMS/Forecasting-Service.git
cd forecast_system
````

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate          # Linux/macOS
# or
. venv\Scripts\activate             # Windows in GitBash
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the Project

```bash
python manage.py migrate
python manage.py runserver
```

- Or use Make commands in the root dir

```bash
make run
```

- for migrations

```bash
make migrate
```

- Now can find the root view at [http://localhost:8000/api/](http://localhost:8000/api/)

---

## 🧪 Sample Forecast API

### Endpoint

`POST /api/forecast/`

### Request Body

```json
{
  "product_SKU": "SKU001",
  "days" : 30
}
```

### Response

```json
{
    "product_SKU": "SKU001",
    "current_stock": 10000,
    "average_forecasted_demand": 14608.27,
    "maximum_forecast": 16425.71,
    "minimum_forecast": 12764.46,
    "stock_shortfall": 4608.27,
    "daily_predictions": [
        {
            "date": "2025-05-03",
            "predicted": 593.5,
            "lower_bound": 530.5,
            "upper_bound": 651.77
        },
        {
            "date": "2025-05-04",
            "predicted": 635.67,
            "lower_bound": 575.94,
            "upper_bound": 697.32
        },
        ...
  ]
}
```

---

## 🔗 Dependencies

- **Django** – Backend web framework
- **Prophet** – Time series forecasting
- **Pandas** – Data manipulation
- **Joblib** – Model serialization
- **Requests** – HTTP requests to warehouse service

---

## 📡 Warehouse Service Integration

The service calls the external warehouse API:

```REST
GET http://warehouse-service/api/stock/<product_SKU>/
→ Expected response: { "current_stock": 120 }
```

You can change the warehouse base URL in `forecaster/utils/warehouse_api.py`.

---

## 📁 Adding a New Product

To support a new product:

1. Save its trained model as `forecaster/models/<product>.joblib`
2. Add a feature engineering file: `forecaster/feature_pipelines/<product>.py` with a function:

```python
def prepare_features(df):
    # Add custom columns to df
    return df
```

---