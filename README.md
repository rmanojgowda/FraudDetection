<<<<<<< HEAD
# 🔐 FraudDetection – Real-Time Transaction Protection System

This project demonstrates **three powerful fraud detection systems** under a single domain:

1. **MITM (Man-in-the-Middle) Fraud Simulation** – shows how fraud *happens*
2. **Machine Learning Based Fraud Detection** – predicts fraud from transaction patterns
3. **Rule-Based Detection Engine** – catches fraud based on business rules

🎯 **Purpose**: To simulate, detect, and prevent financial fraud in real-time using both intelligent and rule-based systems.

---

## 📌 Project Modules Overview

### 1️⃣ MITM Fraud Simulation (Fraud Happening)
- Simulates a **Man-in-the-Middle (MITM)** attack where a hacker modifies the amount seen by the user.
- Two fields are displayed:
  - **Displayed Amount** – visible to the user (can be tampered)
  - **Actual Transaction Amount** – submitted internally
- The frontend randomly inflates the amount to simulate an attack.
- Helps visualize how scams or MITM attacks can deceive users in real time.

💡 **Technology**: HTML, CSS, JavaScript

---

### 2️⃣ ML-Based Fraud Detection
- Detects fraud using a **trained XGBoost model** on transaction data (30 numerical features).
- When a user enters an amount:
  - Generates a feature vector
  - Sends the data to a Flask backend API
  - Predicts if the transaction is **FRAUD** or **NO FRAUD**

💡 **Technology**: Python, Flask, XGBoost, NumPy, JavaScript

---

### 3️⃣ Rule-Based Fraud Detection
- Applies pre-defined business rules to detect fraudulent activity:
  - Suspicious card number patterns
  - Transactions above a certain limit
  - Too many transactions from the same card in a short time
- The backend triggers alerts or blocks transactions when rules are violated.

💡 **Technology**: Python, Flask

---

## 📂 Folder Structure
FraudDetection/
├── FraudHappening/ # MITM Simulation UI
│ └── payment_mitm.html
│
├── FraudDetection/ # ML Model + UI
│ ├── Python.py # Flask API
│ ├── model.pkl # Trained XGBoost model
│ ├── payment.html # ML frontend
│
├── RuleBasedFraud/ # Logic-based detection
│ └── rule_engine.py
│
├── style.css # Shared styling
>>>>>>> 8aef9992e1f745c214db35cd1148be4cf5a735af
=======
# FraudDetection – Real-Time Transaction Protection System

This project demonstrates **three powerful fraud detection systems** under a single domain:

1. **MITM (Man-in-the-Middle) Fraud Simulation** – shows how fraud *happens*
2. **Machine Learning Based Fraud Detection** – predicts fraud from transaction patterns
3. **Rule-Based Detection Engine** – catches fraud based on business rules

**Purpose**: To simulate, detect, and prevent financial fraud in real-time using both intelligent and rule-based systems.

---

## Project Modules Overview

### 1️) MITM Fraud Simulation (Fraud Happening)
- Simulates a **Man-in-the-Middle (MITM)** attack where a hacker modifies the amount seen by the user.
- Two fields are displayed:
  - **Displayed Amount** – visible to the user (can be tampered)
  - **Actual Transaction Amount** – submitted internally
- The frontend randomly inflates the amount to simulate an attack.
- Helps visualize how scams or MITM attacks can deceive users in real time.

**Technology**: HTML, CSS, JavaScript

---

### 2️) ML-Based Fraud Detection
- Detects fraud using a **trained XGBoost model** on transaction data (30 numerical features).
- When a user enters an amount:
  - Generates a feature vector
  - Sends the data to a Flask backend API
  - Predicts if the transaction is **FRAUD** or **NO FRAUD**

**Technology**: Python, Flask, XGBoost, NumPy, JavaScript

---

### 3️) Rule-Based Fraud Detection
- Applies pre-defined business rules to detect fraudulent activity:
  - Suspicious card number patterns
  - Transactions above a certain limit
  - Too many transactions from the same card in a short time
- The backend triggers alerts or blocks transactions when rules are violated.

**Technology**: Python, Flask

---

## Folder Structure
>>>>>>> 5377f8d372cf3e7e961a34d41a28020d4b2bf262
