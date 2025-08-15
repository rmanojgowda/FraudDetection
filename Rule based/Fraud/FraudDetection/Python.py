import flask
from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock fraud detection model (a simple function)
def detect_fraud(card_number, transaction_value):
    # Example logic (use a real model here)
    if transaction_value > 1000:  # Random rule-based logic for demo
        return "fraud"
    else:
        return "no fraud"

@app.route('/detect_fraud', methods=['POST'])
def detect():
    data = request.json
    card_number = data['card_number']
    transaction_value = data['transaction_value']
    
    result = detect_fraud(card_number, transaction_value)
    
    return jsonify({'fraud_status': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
