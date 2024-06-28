


import streamlit as st 
import pickle 
import os
from streamlit_option_menu import option_menu
import numpy as np
import sklearn
print(sklearn.__version__)
st.set_page_config(page_title="Stomach Ulcer Disease Prediction", layout="wide", page_icon="👨‍🦰🤶")

# Get the directory where this script is located
working_dir = os.path.dirname(os.path.abspath(__file__))

# Use a relative path to load the model
model_path = os.path.join(working_dir, 'saved_models', 'ulcer.pkl')

# Load the model
if os.path.exists(model_path):
    try:
        with open(model_path, 'rb') as f:
            ulcers_model = pickle.load(f)
        st.write("Model loaded successfully.")
    except Exception as e:
        st.error(f"Error loading the model: {e}")
else:
    st.error(f"Model file not found: {model_path}")

# Streamlit sidebar and main UI
with st.sidebar:
    selected = option_menu(" Disease Prediction", 
                ['Stomach Ulcers Prediction'],
                 menu_icon='hospital-fill',
                 icons=['person'],
                 default_index=0)

if selected == 'Stomach Ulcers Prediction':
    st.title("Stomach Ulcers Prediction Using Machine Learning")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Age")
    with col2:
        gender = st.selectbox("Gender", ["Male", "Female"])
    with col3:
        family_ulcer_problem = st.selectbox("Family Ulcer Problem", ["Yes", "No"])

    col4, col5, col6 = st.columns(3)

    with col4:
        smoking = st.selectbox("Smoking Status", ["Yes", "No"])
    with col5:
        alcohol_consumption = st.selectbox("Alcohol Consumption", ["Yes", "No"])
    with col6:
        stress_level = st.selectbox("Stress Level", ["Low", "Medium", "High"])

    col7, col8 = st.columns(2)

    with col7:
        h_pylori_infection = st.selectbox("H. pylori Infection", ["Yes", "No"])
    with col8:
        nsaid_use = st.selectbox("NSAID Use", ["Yes", "No"])

    col9, col10 = st.columns(2)

    with col9:
        acidity = st.text_input("Acidity Level (pH)")
    with col10:
        abdominal_pain = st.selectbox("Abdominal Pain", ["Yes", "No"])

    ulcer_result = ""
    if st.button("Stomach Ulcers Test Result"):
        smoking = 1 if smoking == "Yes" else 0
        alcohol_consumption = 1 if alcohol_consumption == "Yes" else 0
        stress_level_mapping = {"Low": 0, "Medium": 0, "High": 0}
        stress_level = stress_level_mapping[stress_level]
        h_pylori_infection = 1 if h_pylori_infection == "Yes" else 0
        nsaid_use = 1 if nsaid_use == "Yes" else 0
        abdominal_pain = 1 if abdominal_pain == "Yes" else 0
        family_ulcer_problem = 0 if family_ulcer_problem == "Yes" else 1
        gender = 1 if gender == "Male" else 0
        
        user_input = [float(age), gender, family_ulcer_problem, smoking, alcohol_consumption, stress_level, 
                      h_pylori_infection, nsaid_use, float(acidity), abdominal_pain]
        
        prediction = ulcers_model.predict([user_input])
        if prediction[0] == 1 or h_pylori_infection == 1:
             ulcer_result = "The person has stomach ulcers"
        else:
             ulcer_result = "The person has no stomach ulcers"
    st.success(ulcer_result)
