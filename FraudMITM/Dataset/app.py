# Install Flask and Ngrok for local tunneling
!pip install flask flask-ngrok

# Import necessary libraries
from flask import Flask, request, jsonify
import random

# Initialize Flask app
app = Flask(__name__)

# Example fraud detection logic
@app.route('/detect-fraud', methods=['POST'])
def detect_fraud():
    # Parse input JSON
    data = request.json
    
    email = data.get('email', '')
    credit_card = data.get('credit_card', '')
    
    # Basic fraud detection logic
    banned_domains = ['fraudmail.com', 'scammer.com']
    domain = email.split('@')[-1]
    
    # Check for suspicious email domain
    if domain in banned_domains:
        return jsonify({"fraud": True, "reason": "Suspicious email domain detected."})
    
    # Simulated random fraud detection (for demonstration)
    is_fraud = random.choice([True, False])
    reason = "Random fraud detection triggered." if is_fraud else "No fraud detected."
    
    return jsonify({"fraud": is_fraud, "reason": reason})

# Start the Flask server using ngrok
from flask_ngrok import run_with_ngrok
run_with_ngrok(app)  # Start ngrok when app runs
app.run()
