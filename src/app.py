from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.feature_engineering import hash_feature
import uvicorn

app = FastAPI(title="High-Cardinality Prediction Service")

class PredictionRequest(BaseModel):
    feature_value: str

class PredictionResponse(BaseModel):
    feature_bucket: int
    predicted_value: float
    status: str

@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    """
    Mock prediction endpoint.
    Hashes the feature and returns a mock prediction based on the hash.
    """
    try:
        bucket = hash_feature(request.feature_value, n_buckets=100)
        # Mock model logic: simple deterministic value based on bucket
        prediction = float(bucket) / 100.0 
        
        return {
            "feature_bucket": bucket,
            "predicted_value": prediction,
            "status": "success"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
