from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("fraud_call_model.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            duration = int(request.form["duration"])
            frequency = int(request.form["frequency"])
            location = int(request.form["location"])
            call_type = int(request.form["call_type"])

            # Create a DataFrame for prediction
            new_call = pd.DataFrame([[duration, frequency, location, call_type]],
                                    columns=["duration", "frequency", "location", "call_type"])
            
            # Predict
            prediction = model.predict(new_call)[0]

            result = "Fraud Call 🚨" if prediction == 1 else "Safe Call ✅"
            return render_template("index.html", prediction=result)
        except:
            return render_template("index.html", prediction="Invalid Input! Please enter valid numbers.")

    return render_template("index.html", prediction=None)

if __name__ == "__main__":
    app.run(debug=True)
