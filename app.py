import os
import pickle
import streamlit as st
import numpy as np
import pandas as pd

# ---------------- SAFE PIPELINE LOADER ---------------- #
def load_pipeline(pickle_path="model.pkl"):
    """
    Safely load a pickled ML pipeline with clear error handling.
    """
    if not os.path.exists(pickle_path):
        st.error(f"❌ Model file not found: {pickle_path}")
        st.info("👉 Make sure the .pkl file is in your GitHub repo and the correct path is used.")
        st.stop()

    try:
        with open(pickle_path, "rb") as f:
            pipeline = pickle.load(f)
        return pipeline
    except Exception as e:
        st.error("⚠️ Failed to load the pipeline.")
        st.code(str(e))
        st.info("This may be due to version mismatch between scikit-learn locally and on Streamlit Cloud.")
        st.stop()

# ---------------- LOAD PIPELINE ---------------- #
pipeline = load_pipeline("model.pkl")

# ---------------- STREAMLIT APP ---------------- #
st.title("❤️ Heart Disease Prediction App")

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

target = st.selectbox(
    "target",
    ["less chance of heart disease", "more chance of heart disease"]
)

# Define input_df and prediction with default values
input_df = {}
prediction = None

# Prediction button
if st.button("Predict"):
    input_df = {
        "age": age,
        "chest pain": chest_pain,
        "heart pain": heart_pain,
        "exercise pain": exercise_pain,
        "oldpeak": oldpeak,
        "number of blood vessels": num_blood_vessels,
        "blood disorder": blood_disorder,
        "target": target
    }

    try:
        prediction = pipeline.predict(pd.DataFrame([input_df]))
        if prediction[0] == 1:
            st.error("🚨 Prediction: Heart Disease Detected")
        else:
            st.success("✅ Prediction: No Heart Disease Detected")
    except Exception as e:
        st.error("⚠️ Error during prediction")
        st.code(str(e))

