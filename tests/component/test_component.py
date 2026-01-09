from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_health_check():
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_predict_endpoint_success():
    """Test the predict endpoint with valid data."""
    payload = {"feature_value": "test_user_id"}
    response = client.post("/predict", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert "feature_bucket" in data
    assert "predicted_value" in data
    assert data["status"] == "success"

def test_predict_consistency():
    """Test that the predict endpoint returns consistent results."""
    payload = {"feature_value": "consistent_id"}
    response1 = client.post("/predict", json=payload)
    response2 = client.post("/predict", json=payload)
    
    assert response1.json() == response2.json()
