import streamlit as st 

option = st.selectbox(
    "What is your favorite vegetable?"
    ("Broccoli", "spinnach", "Carrots")
)

st.write("You selected:", option)