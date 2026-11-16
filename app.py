import streamlit as st

st.title("Simple Streamlite App")

name = st.text_input("Enter your name")

if name:
    st.write("Hello", name)
