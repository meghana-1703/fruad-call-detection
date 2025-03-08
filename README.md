📞 Fraud Call Detection System

This project is a Fraud Call Detection System that uses machine learning to classify whether a call is fraudulent or not. The system processes call data and predicts fraud risk using a trained model.

🚀 Features

📊 Machine Learning Model – Uses a trained model to detect fraudulent calls.

📂 CSV Data Processing – Reads call data from a dataset.

🔥 Flask Web App – Provides an interactive UI for users to check call status.

📈 Prediction API – Accepts call details and returns fraud probability.

🛠 Deployment on Render – Hosted as a web service for easy access.


🛠 Installation & Setup

⿡ Clone the Repository

git clone https://github.com/meghana-1703/fraud-call-detection.git
cd fraud-call-detection

⿢ Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

⿣ Install Dependencies

pip install -r requirements.txt

⿤ Run the Application

python app.py

Then, open http://127.0.0.1:5000/ in your browser.

🔍 How It Works

1. Upload Call Data – Users upload a CSV file containing call details.


2. Model Prediction – The system analyzes the data and detects fraudulent calls.


3. Results Display – The UI shows which calls are classified as fraud.



🖥 Technologies Used

Python (Flask, Pandas, Scikit-Learn)

Machine Learning (Logistic Regression, Decision Trees)

HTML, CSS (Frontend UI)

📜 License

This project is open-source and available under the MIT License.

