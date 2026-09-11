from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

# Load trained model
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "model",
    "car_price_model.pkl"
)

FEATURE_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "model",
    "feature_columns.pkl"
)

model = joblib.load(MODEL_PATH)
feature_columns = joblib.load(FEATURE_PATH)


@app.route("/")
def home():
    return jsonify({
        "message": "Car Price Prediction API is running"
    })


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Create input dataframe
        input_data = pd.DataFrame([data])

        # Create Car Age
        input_data["Car_Age"] = 2026 - input_data["Year"]

        # Extract Brand using the same logic used in the notebook
        input_data["Brand"] = (
            input_data["Car_Name"]
            .astype(str)
            .str.split()
            .str[0]
        )

        # Convert categorical columns to string
        input_data["Fuel_Type"] = input_data["Fuel_Type"].astype(str)
        input_data["Seller_Type"] = input_data["Seller_Type"].astype(str)
        input_data["Transmission"] = input_data["Transmission"].astype(str)
        input_data["Owner"] = input_data["Owner"].astype(str)
        input_data["Brand"] = input_data["Brand"].astype(str)

        # Remove Car_Name because it was removed before model training
        input_data = input_data.drop(columns=["Car_Name"])

        # One-hot encode categorical columns
        categorical_columns = [
            "Fuel_Type",
            "Seller_Type",
            "Transmission",
            "Owner",
            "Brand"
        ]

        input_data = pd.get_dummies(
            input_data,
            columns=categorical_columns,
            drop_first=True,
            dtype=int
        )

        # Match exactly the features used during training
        input_data = input_data.reindex(
            columns=feature_columns,
            fill_value=0
        )

        # Make prediction
        prediction = model.predict(input_data)[0]

        return jsonify({
            "predicted_price": round(float(prediction), 2)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)