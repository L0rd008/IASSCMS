# import requests

# WAREHOUSE_API_BASE = "http://localhost:8001/api"

# def get_current_stock(product_SKU: str) -> int:
#     try:
#         response = requests.get(f"{WAREHOUSE_API_BASE}/stock/{product_SKU}/")
#         if response.status_code == 200:
#             return response.json().get("current_stock", 0)
#     except Exception:
#         pass
#     return 0

def get_current_stock(product_SKU: str) -> int:
    """Return hardcoded stock values for different products."""
    stock_data = {
        "SKU001": 10000,
        "SKU002": 5000050,
        "SKU003": 750000,
        "SKU004": 500998,
        "SKU005": 42000,
        "SKU006": 585000,
        "SKU007": 270000,
        "SKU008": 45500,
        "SKU009": 900000,
        "SKU010": 4000000,
    }
    return stock_data.get(product_SKU, 0)