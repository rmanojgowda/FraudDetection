from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

@app.route("/payment", methods=["POST"])
def check_mitm_fraud():
    data = request.json
    card = data.get("card")
    amount = data.get("amount")
    shown_amount = data.get("shownAmount")

    if not card or amount is None or shown_amount is None:
        return jsonify({"status": "invalid input"}), 400

    # MITM detection logic
    if shown_amount > amount:
        return jsonify({"status": "fraud"})
    else:
        return jsonify({"status": "no fraud"})

if __name__ == "__main__":
    app.run(debug=True)
