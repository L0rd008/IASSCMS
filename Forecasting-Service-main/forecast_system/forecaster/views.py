from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forecast_runner import forecast_for_product

@api_view(['GET'])
def root_view(request):
    return Response({"message": "Forecasting Service API"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def forecast_view(request):
    product_SKU = request.data.get("product_SKU")
    days = int(request.data.get("days", 30))

    if not product_SKU:
        return Response({"error": "Missing product_SKU"}, status=400)

    result = forecast_for_product(product_SKU, days=days)
    return Response(result, status=200 if 'error' not in result else 500)