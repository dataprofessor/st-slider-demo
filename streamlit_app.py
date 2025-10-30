import streamlit as st

number = st.slider("Select a number", 0, 100, value=50)
st.write("Number is:", number)
