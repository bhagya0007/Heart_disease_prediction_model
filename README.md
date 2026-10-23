# Heart Disease Prediction

A Streamlit app that uses a trained K-nearest neighbors (KNN) model to estimate heart disease risk from a set of health measurements. Enter the requested values and select **Predict** to see the model's result.

## Project files

- `app.py` — Streamlit user interface and prediction flow.
- `KNN_heart.pkl` — trained KNN model.
- `heart_scaler.pkl` — fitted feature scaler used before prediction.
- `heart_columns.pkl` — expected model feature names and order.

## Requirements

- Python 3.8 or later
- Streamlit
- pandas
- joblib
- scikit-learn

Install the Python packages:

```bash
python -m pip install streamlit pandas joblib scikit-learn
```

## Run locally

From the project directory, run:

```bash
streamlit run app.py
```

Streamlit will print a local URL to open in your browser.

## Using the app

Provide the requested information, including age, sex, chest pain type, resting blood pressure, cholesterol, fasting blood sugar, resting ECG, maximum heart rate, exercise-induced angina, oldpeak, and ST slope. Select **Predict** to view the model's result.

## Important

This app is for educational and informational use only. Its prediction is not a medical diagnosis or a substitute for advice from a qualified healthcare professional. Consult a healthcare professional about health concerns.