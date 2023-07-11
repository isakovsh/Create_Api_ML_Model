from fastapi import FastAPI
from pydantic import BaseModel
import pickle 
from main import  *

# Define the data model
class DiabetesData(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int



# Create the FastAPI application instance
app = FastAPI()

# Prediction endpoint
@app.post("/predict")
def predict_diabetes(data: DiabetesData):
    # Prepare the input data for prediction
    input_features = [
        data.Pregnancies, 
        data.Glucose,
        data.BloodPressure,
        data.SkinThickness, 
        data.Insulin,
        data.BMI,
        data.DiabetesPedigreeFunction,
        data.Age
    ]

    # Make the prediction using the ML model
    
    prediction = predict_func(input_features)[0]

    # Map the prediction to the corresponding class label
    if prediction == 0:
        result = "Non-Diabetic"
    else:
        result = "Diabetic"

    return result

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
