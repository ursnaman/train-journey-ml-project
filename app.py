import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

st.title("Train Journey Time Prediction")

st.write("Enter journey details below:")

distance = st.number_input("Distance (km)", min_value=0.0)
stops = st.number_input("Total Stops",min_value=0)

if st.button("Predict Journey Time"):

    input_data = np.array([[distance, stops]])
    prediction = model.predict(input_data)

    hours = prediction[0] // 60
    minutes = prediction[0] % 60

    st.success(f"Predicted Journey Time: {hours:.2f} hours")