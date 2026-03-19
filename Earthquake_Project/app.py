import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("🌍 Earthquake Magnitude Predictor")

data = pd.read_csv("earthquake_1995-2023.csv")
data = data[['latitude','longitude','depth','magnitude']]

X = data[['latitude','longitude','depth']]
y = data['magnitude']

model = LinearRegression()
model.fit(X, y)

st.header("Enter Earthquake Details")

lat = st.number_input("Enter Latitude")
lon = st.number_input("Enter Longitude")
depth = st.number_input("Enter Depth")

if st.button("Predict"):
    prediction = model.predict([[lat, lon, depth]])
    st.success(f"Predicted Magnitude: {prediction[0]:.2f}")