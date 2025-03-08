import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv("fraud_calls.csv")

# Convert categorical columns into numerical
df['call_type'] = df['call_type'].astype('category').cat.codes
df['location'] = df['location'].astype('category').cat.codes

# Split features and labels
X = df.drop(columns=['label', 'caller_id'])  # Features
y = df['label']  # Target variable

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

# Save the model
joblib.dump(model, "fraud_call_model.pkl")
