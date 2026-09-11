# Car Price Prediction

A Machine Learning project that predicts the selling price of a used car based on its features.

## Project Overview

This project uses the Vehicle Dataset from CarDekho to build a machine learning model for predicting used car selling prices.

The project includes:

- Data loading and cleaning
- Feature engineering
- Exploratory Data Analysis (EDA)
- Categorical data encoding
- Correlation analysis
- Model training and evaluation
- Model comparison
- Feature importance analysis
- A Flask backend API
- A simple web interface for price prediction

## Dataset

The dataset used in this project is the **Vehicle Dataset from CarDekho**.

The dataset contains information such as:

- Car Name
- Year
- Selling Price
- Present Price
- Kilometers Driven
- Fuel Type
- Seller Type
- Transmission
- Previous Owners

## Machine Learning Workflow

The project follows these steps:

1. Load the dataset
2. Clean the data
3. Remove duplicate records
4. Perform feature engineering
5. Create `Car_Age`
6. Extract `Brand`
7. Perform Exploratory Data Analysis
8. Encode categorical features
9. Analyze feature correlations
10. Split the data into training and testing sets
11. Train Linear Regression
12. Train Random Forest
13. Compare model performance
14. Select the best-performing model
15. Analyze feature importance
16. Save the trained model

## Machine Learning Models

Two regression models were trained:

- Linear Regression
- Random Forest Regressor

The models were evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

Based on the model comparison in the notebook, **Linear Regression** was selected as the best model.

## Project Structure

```text
Car-price-prediction/
│
├── backend/
│   └── app.py
│
├── dataset/
│   └── car data.csv
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── model/
│   ├── car_price_model.pkl
│   └── feature_columns.pkl
│
├── notebook/
│   └── car_price_prediction.ipynb
│
└── .gitignore
Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Joblib
Flask
Flask-CORS
HTML
CSS
JavaScript
Jupyter Notebook
How to Run the Project
1. Run the Backend

Open a terminal and navigate to the backend folder:

cd backend

Run the Flask server:

python app.py

The backend will run at:

http://127.0.0.1:5000
2. Run the Frontend

Open another terminal and navigate to the frontend folder:

cd frontend

Start the local frontend server:

python -m http.server 5500

Open the application in your browser:

http://127.0.0.1:5500/index.html
Prediction

The web interface accepts the following inputs:

Car Name
Year
Present Price
Kilometers Driven
Fuel Type
Seller Type
Transmission
Previous Owners

After submitting the details, the application sends the input to the Flask backend and returns the predicted selling price.

Model Files

The trained model and feature columns are stored in the model folder:

car_price_model.pkl
feature_columns.pkl

These files are used by the Flask backend to make predictions.

Notebook

The complete machine learning workflow is available in:

notebook/car_price_prediction.ipynb

It contains the data preprocessing, EDA, model training, evaluation, comparison, feature importance analysis, and model saving steps.

Future Improvements
Improve model accuracy using additional algorithms
Add more detailed validation
Deploy the application online
License

This project is created for educational and machine learning project purposes.