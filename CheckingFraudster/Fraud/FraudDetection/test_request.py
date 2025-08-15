import requests
import json

# Step 1: Load the test sample JSON (you saved earlier)
with open("sample_fraud_input.json", "r") as f:
    data = json.load(f)

# Step 2: Send POST request to your running Flask API
url = "http://127.0.0.1:5000/detect_fraud"  # OR your ngrok URL
response = requests.post(url, json=data)

# Step 3: Print results
print("Status Code:", response.status_code)
print("Raw Response:", response.text)

try:
    result = response.json()
    print("Prediction Response:", result)
except Exception as e:
    print("Error parsing response:", e)
