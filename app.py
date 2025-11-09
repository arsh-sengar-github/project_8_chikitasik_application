# Import the packages
import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the model and scaler
with open('project_8_model/heart_disease_rf_model.pkl', 'rb') as file:
    model, scaler = pickle.load(file)

# Define categorical and numerical features
categorical_features = [
    'Gender', 'ChestPainType', 'FastingBS',
    'RestingECG', 'ExerciseAngina', 'ST_Slope',
    'MajorVessels', 'Thalassemia'
]
numerical_features = [
    'Age', 'RestingBP', 'Cholesterol',
    'MaxHR', 'ST_Depression'
]

# Streamlit configuration
st.set_page_config(page_title="Chikitasik", page_icon="⚕️")
st.title("⚕️ Chikitasik")
st.write(
    "Welcome to Chikitasik, your personal heart disease risk assessment tool! "
    "This application leverages machine learning to help you understand your risk of heart disease "
    "based on various health parameters. Please provide the necessary information below to get started."
)
st.markdown("---")

# Input fields
col1, col2 = st.columns(2)
with col1:
    Age = st.number_input("Age", min_value=10, max_value=100, value=30, step=1)
    Gender = st.selectbox("Gender", ['Male', 'Female'])
    ChestPainType = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
    RestingBP = st.number_input("Resting Blood Pressure (mm Hg)", min_value=80, max_value=200, value=120, step=1)
    Cholesterol = st.number_input("Cholesterol (mg/dl)", min_value=100, max_value=600, value=200, step=1)

with col2:
    FastingBS = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
    RestingECG = st.selectbox("Resting ECG", [0, 1, 2])
    MaxHR = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220, value=120, step=1)
    ExerciseAngina = st.selectbox("Exercise Induced Angina", [0, 1])
    ST_Depression = st.number_input("ST Depression Induced by Exercise Relative to Rest", min_value=0.0, max_value=6.0, value=1.0, step=0.1)
    ST_Slope = st.selectbox("Slope of the Peak Exercise ST Segment", [0, 1, 2])
    MajorVessels = st.selectbox("Number of Major Vessels Colored by Fluoroscopy", [0, 1, 2, 3])
    Thalassemia = st.selectbox("Thalassemia", [1, 2, 3])

# Convert categorical gender feature to numeric
Gender = 1 if Gender == 'Male' else 0

# Create dataframe from user inputs
user_input = {
    'Age': Age,
    'Gender': Gender,
    'ChestPainType': ChestPainType,
    'RestingBP': RestingBP,
    'Cholesterol': Cholesterol,
    'FastingBS': FastingBS,
    'RestingECG': RestingECG,
    'MaxHR': MaxHR,
    'ExerciseAngina': ExerciseAngina,
    'ST_Depression': ST_Depression,
    'ST_Slope': ST_Slope,
    'MajorVessels': MajorVessels,
    'Thalassemia': Thalassemia,
}
user_input_df = pd.DataFrame([user_input])

# Encode categorical features
user_input_encoded = pd.get_dummies(user_input_df, columns=categorical_features, drop_first=True)

# Align with model’s expected columns (handle missing columns safely)
expected_encoded_cols = model.feature_names_in_ if hasattr(model, "feature_names_in_") else user_input_encoded.columns
user_input_encoded = user_input_encoded.reindex(columns=expected_encoded_cols, fill_value=0)

# Scale numerical features
user_input_encoded[numerical_features] = scaler.transform(user_input_encoded[numerical_features])

# Prediction
if st.button("Predict Heart Disease Risk"):
    prediction = model.predict(user_input_encoded)[0]
    if prediction == 1:
        st.error("⚠️ Based on the provided information, there is a **high risk of heart disease**. Please consult a healthcare professional for a comprehensive evaluation.")
    else:
        st.success("✅ Based on the provided information, there is a **low risk of heart disease**. Keep maintaining a healthy lifestyle and regular check-ups!")

st.caption(
    "Disclaimer: This tool is for informational purposes only and should not replace professional medical advice, "
    "diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any "
    "questions you may have regarding a medical condition."
)
