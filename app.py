import streamlit as st
import numpy as np
import pickle
import pandas as pd  # <-- Add this import

# Load the trained model
with open('model.pkl', 'rb') as f:
    pipeline = pickle.load(f)

st.title("Heart Disease Detection App")

# Input fields
age = st.number_input("age", min_value=1, max_value=120, value=50)

chest_pain = st.selectbox(
    "chest pain",
    ["heart related pain", "non heart related", "not heart pain", "asymptomatic pain"]
)

heart_pain = st.number_input("heart pain (numeric value)", min_value=50, max_value=250, value=120)

exercise_pain = st.selectbox(
    "exercise pain",
    ["no angina", "present angina"]
)

oldpeak = st.number_input("oldpeak", min_value=0.0, max_value=10.0, value=1.0, step=0.1)

num_blood_vessels = st.number_input("number of blood vessels", min_value=0, max_value=4, value=0)

blood_disorder = st.selectbox(
    "blood disorder",
    ["reversable defect", "fixed defect", "normal"]
)


# create a button to make prediction using function
if st.button("Predict"):
    # Pass input as a DataFrame with correct column names
    input_df = pd.DataFrame({
        'age': [age],
        'chest pain': [chest_pain],
        'heart pain': [heart_pain],
        'exercise pain': [exercise_pain],
        'oldpeak': [oldpeak],
        'number of blood vessels': [num_blood_vessels],
        'blood disorder': [blood_disorder],
    })

    prediction = pipeline.predict(input_df)
    if prediction[0] == 1:
        st.error("Prediction: Heart Disease Detected")
    else:
        st.success("Prediction: No Heart Disease Detected")