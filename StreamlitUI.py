import streamlit as st

st.title(":rainbow[My first streamlit page]")
st.write("My first app on streamlit cloud")

if st.button('Generate'):
    st.write("This is the generated text on click of Generate button")

audio_file = st.audio_input("Record your voice message")

if audio_file:
    print(audio_file.name)
    print(audio_file)

select_option = st.selectbox('What is you favourite color?', ("Red", "Blue", "Green"), index=None, placeholder="Enter your favourite color")
if select_option:
    st.write('Your favourite color is:', select_option)

radio_option = st.radio("What is you favourite movie genre?", ("Comedy", "Drama", "Documentary"), index=None)
if radio_option:
    st.write('Your favourite movie genre is:', radio_option)

multiselect_option = st.multiselect("What are your favourite colors?", ("Red", "Blue", "Green", "Yellow"), placeholder="Enter your favourite color(s)")
if multiselect_option:
    st.write('You selected:', multiselect_option)