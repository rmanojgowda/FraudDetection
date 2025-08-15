from flask import Flask, request, jsonify
from flask_cors import CORS  # ✅ add this
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)  # ✅ enable CORS for all routes

# Load your model
with open("fraud_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/detect_fraud", methods=["POST"])
def detect_fraud():
    data = request.json
    features = data.get("features")

    if not features or len(features) != 30:
        return jsonify({"error": "Expected 30 numerical features"}), 400

    input_array = np.array(features).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    return jsonify({"fraud_status": "fraud" if prediction == 1 else "no fraud"})

if __name__ == "__main__":
    app.run()
