import streamlit as st
import pandas as pd
import joblib

model = joblib.load("KNN_heart.pkl")
scaler = joblib.load("heart_scaler.pkl")
expected_columns = joblib.load("heart_columns.pkl") 

st.title("Heart Stroke Prediction")
st.markdown("Provide the following information to predict the risk of heart stroke.")

age = st.slider("Age",18,100,40)
sex = st.selectbox("Sex",["Male","Female"])
chest_pain = st.selectbox("Chest Pain Type",["Typical Angina(TA)","Atypical Angina (ATA)","Non-Anginal Pain (NAP)","Asymptomatic (ASY)"])
resting_bp = st.number_input("Resting Blood Pressure (in mm Hg)",80,200,120)
cholesterol = st.number_input("Cholestrol (in mg/dl)",100,600,200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl",[0,1])
resting_ecg  = st.selectbox("Resting Electrocardiographic Results",["Normal","ST-T Wave Abnormality","Left Ventricular Hypertrophy"])
max_hr = st.slider("Maximum Heart Rate Achieved",60,220,150)
exercise_angina = st.selectbox("Exercise Induced Angina",["Yes","No"])
oldpeak = st.slider("Oldpeak (ST depression induced by exercise relative to rest)",0.0,6.0,1.0)     
st_slope = st.selectbox("ST slope",["Upsloping","Flat","Downsloping"])

if(st.button("Predict")):
    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    input_df = pd.DataFrame([raw_input])
    
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]
    
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]

    if(prediction == 1):
        st.error("High Risk of heart disease. Please consult a doctor.")
    else:
        st.success("Low Risk of heart disease. Keep maintaining a healthy lifestyle.")