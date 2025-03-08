import joblib
import pandas as pd

# Load the trained model
model = joblib.load("fraud_call_model.pkl")

# Example new call data (duration=100 sec, frequency=2 calls, location=New York, call_type=spam)
new_call = pd.DataFrame([[100, 2, 0, 1]], columns=["duration", "frequency", "location", "call_type"])

# Predict
prediction = model.predict(new_call)

if prediction[0] == 1:
    print("Fraud Call 🚨")
else:
    print("Safe Call ✅")
