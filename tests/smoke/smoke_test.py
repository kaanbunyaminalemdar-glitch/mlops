import sys
import time
import requests

def run_smoke_test(url: str):
    """
    Runs a smoke test against the deployed service.
    
    Args:
        url (str): Base URL of the service.
    """
    print(f"Starting smoke test against {url}...")
    
    # Check Health
    try:
        health_resp = requests.get(f"{url}/health", timeout=5)
        if health_resp.status_code == 200:
            print("✅ Health check passed!")
        else:
            print(f"❌ Health check failed with status {health_resp.status_code}")
            sys.exit(1)
            
        # Check Predict
        payload = {"feature_value": "smoke_test_value"}
        predict_resp = requests.post(f"{url}/predict", json=payload, timeout=5)
        
        if predict_resp.status_code == 200:
            data = predict_resp.json()
            if data.get("status") == "success":
                print("✅ Prediction endpoint passed!")
                print(f"   Response: {data}")
            else:
                print("❌ Prediction returned unexpected content")
                sys.exit(1)
        else:
            print(f"❌ Prediction failed with status {predict_resp.status_code}")
            sys.exit(1)
            
    except requests.exceptions.ConnectionError:
        print(f"❌ Could not connect to {url}. Service might be down.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_url = sys.argv[1]
    else:
        target_url = "http://localhost:8000"
    
    # Wait a bit for service to come up if running in CI
    time.sleep(2) 
    run_smoke_test(target_url)
