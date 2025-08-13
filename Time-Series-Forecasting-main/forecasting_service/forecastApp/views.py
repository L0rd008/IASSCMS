from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
import joblib
import os

model_path = os.path.join(os.path.dirname(__file__), 'models', 'Cardigans_Dust_CoatsDataSet.joblib')
model = joblib.load(model_path)

@api_view(['GET'])
def root_view(request):
    return Response({"message": "Forecasting Service API"})


def get_season(month):
    """Determine season based on month number."""
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Autumn'


def add_model_features(df):
    """Add all required features to the dataframe for the Prophet model."""
    # Extract month
    df['month'] = df['ds'].dt.month
    
    # Add season
    df['season'] = df['month'].apply(get_season)
    
    # Create dummy variables for season
    season_dummies = pd.get_dummies(df['season'])
    df = pd.concat([df, season_dummies], axis=1)
    df = df.drop('season', axis=1)
    
    # Add Oct/Nov indicator
    df['is_oct_nov'] = df['ds'].dt.month.isin([10, 11]).astype(int)
    
    # For lag features (simplified since we don't have historical data in this endpoint)
    # We'll use default values - in a production system, you might want to
    # have access to the most recent historical data
    df['prev_y'] = 0  # Default value
    df['increasing_week'] = 0  # Default value
    
    return df


@api_view(['POST'])
def forecast_view(request):
    """
    API endpoint to generate forecasts based on a date range.
    Expects a JSON body with start_date and end_date.
    """
    try:
        # Get the date range from request data
        data = request.data
        
        if 'start_date' not in data or 'end_date' not in data:
            return Response(
                {"error": "Both start_date and end_date are required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Parse dates
        try:
            start_date = pd.to_datetime(data['start_date'])
            end_date = pd.to_datetime(data['end_date'])
        except ValueError:
            return Response(
                {"error": "Invalid date format. Use YYYY-MM-DD format"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Calculate number of months between dates
        months_diff = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
        if months_diff <= 0:
            return Response(
                {"error": "end_date must be after start_date"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Create a future dataframe for the specified date range
        future_dates = pd.date_range(start=start_date, end=end_date, freq='ME')
        future_df = pd.DataFrame({'ds': future_dates})
        
        # Add required features for the model
        future_df = add_model_features(future_df)
        
        # Run forecast
        forecast = model.predict(future_df)
        
        # Post-process results
        # forecast['yhat'] = forecast['yhat'].clip(lower=0)
        forecast['yhat_lower'] = forecast['yhat_lower'].clip(lower=0)
        forecast['yhat_upper'] = forecast['yhat_upper'].clip(lower=0)
        # forecast['yhat'] = forecast['yhat'].round()
        
        # Format results for JSON response
        result = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].copy()
        result['ds'] = result['ds'].dt.strftime('%Y-%m-%d')
        result = result.rename(columns={
            'ds': 'date',
            'yhat': 'forecast_value',
            'yhat_lower': 'lower_bound',
            'yhat_upper': 'upper_bound'
        })
        
        return Response(result.to_dict(orient='records'), status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )