import xgboost as xgb
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import pickle

# 1. Create dummy dataset similar to a fraud detection dataset
X, y = make_classification(n_samples=1000, n_features=30, n_informative=10, random_state=42)

# 2. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train XGBoost model
model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss')
model.fit(X_train, y_train)

# 4. Save model as model.pkl
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ model.pkl saved successfully.")
