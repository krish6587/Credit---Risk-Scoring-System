from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
from src.predict import CreditRiskModel

app = FastAPI(title="Credit Risk Scoring API")

# Initialize the model
model = CreditRiskModel()

class PredictionRequest(BaseModel):
    age: int
    income: float
    loan_amount: float
    credit_score: int
    employment_length: int

@app.post("/predict")
def predict_credit_risk(request: PredictionRequest):
    try:
        data = request.dict()
        result = model.predict(data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Mount static files for the frontend
static_dir = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(static_dir, exist_ok=True)
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
def read_index():
    index_file = os.path.join(static_dir, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return {"message": "Frontend not found"}
