import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib

#Creating the flask app
app = Flask(__name__)

model = joblib.load("Diabetes_Model1.pkl")
scaler = joblib.load("scaler.pkl")

@app.route('/')
def home():
    return render_template('Diabetes_App.html', prediction_test="")

@app.route('/predict', methods=['POST'])

def predict():
    try:
        # Step 1: Get user inputs
        int_features = [float(x) for x in request.form.values()]
        final_features = np.array([int_features])  # 2D array for scaler

        # Step 2: Apply scaling
        final_scaled = scaler.transform(final_features)

        # Step 3: Make prediction
        prediction = model.predict(final_scaled)

        if prediction[0] == 1:
            return render_template('Diabetes_App.html', prediction_text='RESULTS: You are in high risk of diabetes')
        else:
            return render_template('Diabetes_App.html', prediction_text='RESULTS: You are in low risk of diabetes')

    except ValueError:
        return render_template('Diabetes_App.html', prediction_text="⚠️ Please enter valid numeric values in all fields.")


if __name__ == "__main__":
    app.run(debug=True)