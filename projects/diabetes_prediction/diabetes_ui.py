import streamlit as st
import numpy as np

st.set_page_config(page_title="Diabetes Prediction", layout="wide")

st.header("Diabetes using Decision Tree Classifier")
st.divider()

col1, col2, col3 = st.columns((1,1, 1))

with col1:
    Glucose = st.number_input("Glucose", placeholder="Enter glucose")
with col2:
    BloodPressure = st.number_input("BloodPressure", placeholder="Enter BP")
with col3:
    SkinThickness = st.number_input("SkinThickness", placeholder="Enter skin thickness")


col4, col5, col6, col7 = st.columns((1,1,1,1))

with col4:
    Insulin = st.number_input("Insulin", placeholder="Enter Insulin")
with col5:
    BMi = st.number_input("BMI", placeholder="Enter BMI")
with col6:
    DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction", placeholder="Enter DiabetesPedigreeFunction")
with col7:
    Age = st.number_input("Age", placeholder="Enter Age")

arr = np.array([Glucose,BloodPressure, SkinThickness, Insulin, BMi, DiabetesPedigreeFunction, Age])

import joblib

predictive_price = joblib.load('diabetes.pkl')

def p():
    pp = predictive_price.predict([arr])
    if pp == 1:
        #st.write("Diabetes Present")
        st.markdown("<h1 style='color:red'>Diabetes are Present</h1>", unsafe_allow_html=True)

    if pp == 0:
        #st.write("Diabetes are not Present")
        st.markdown("<h1 style='color:green'>Diabetes are not Present</h1>", unsafe_allow_html=True)
        st.balloons()
    
if st.button('View Result'):
    p()
