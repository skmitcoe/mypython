import streamlit as st

st.title("My first streamlit page")
st.write("My first app on streamlit cloud")

if st.button('Generate'):
    st.write("This is the generated text on click of button")
else:
    st.write('This is the default message')