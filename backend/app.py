from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import joblib
import pandas as pd
import os

app = Flask(
    __name__,
    static_folder="../frontend",
    static_url_path=""
)

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
    return send_from_directory("../frontend", "index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        input_data = pd.DataFrame([data])

        # Create Car Age
        input_data["Car_Age"] = 2026 - input_data["Year"]

        # Extract Brand
        input_data["Brand"] = (
            input_data["Car_Name"]
            .astype(str)
            .str.split()
            .str[0]
        )

        # Convert categorical columns to string
        categorical_columns = [
            "Fuel_Type",
            "Seller_Type",
            "Transmission",
            "Owner",
            "Brand"
        ]

        for column in categorical_columns:
            input_data[column] = input_data[column].astype(str)

        # Remove Car_Name
        input_data = input_data.drop(columns=["Car_Name"])

        # One-hot encoding
        input_data = pd.get_dummies(
            input_data,
            columns=categorical_columns,
            drop_first=True,
            dtype=int
        )

        # Match training features
        input_data = input_data.reindex(
            columns=feature_columns,
            fill_value=0
        )

        # Prediction
        prediction = model.predict(input_data)[0]

        return jsonify({
            "predicted_price": round(float(prediction), 2)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )