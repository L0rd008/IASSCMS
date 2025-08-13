from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
import joblib
import os


model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'loan_default_pipeline.joblib')
model = joblib.load(model_path)

# Column names expected by the model
input_columns = ['Age', 'Annual_Income', 'Credit_Score', 'Employment_Years', 'Loan_Amount_Requested']

@api_view(['GET'])
def root_view(request):
    return Response({"message": "Loan Default Prediction API"})

@api_view(['POST'])
def predict_view(request):
    try:
        input_data = request.data['data'] 
        input_df = pd.DataFrame([input_data], columns=input_columns)
        prediction = model.predict_proba(input_df)[:, 1][0] 
        return Response({"prediction": float(prediction)})
    except Exception as e:
        return Response({"error": str(e)}, status=400)
