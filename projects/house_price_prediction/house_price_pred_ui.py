import streamlit as st
import numpy as np

st.set_page_config(page_title="House Price Prediction", layout="wide")

st.header("House Price Prediction using Linear Regression")
st.divider()

col1, col2,col3, col4 = st.columns((1,1,1,1))

with col1:
    area = st.number_input("Area",placeholder="Enter Area")

with col2:
    bedrooms = st.number_input("BedRoom",placeholder="Enter no. of bedrooms")

with col3:
    bathrooms = st.number_input("Bathroom",placeholder="Enter no. of bathrooms")

with col4:
    stories = st.number_input("Stories",placeholder="Enter no. of stories")

arr = np.array([area,bathrooms,bathrooms,stories])

import joblib

predictive_price = joblib.load('housing2.pkl')


def p():
    pp = predictive_price.predict([arr])
    st.write(pp)
    st.balloons()

st.button("Predict",on_click=p)
