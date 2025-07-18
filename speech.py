import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment

st.title(":rainbow[My first streamlit page]")
st.write("My first app on streamlit cloud")

if st.button('Generate'):
    st.write("This is the generated text on click of Generate button")

audio_file = st.audio_input("Record your voice message")

r = sr.Recognizer()

if audio_file:

    print(audio_file.name)
    print(audio_file)
    with open("sumit.wav", "wb") as f:
        f.write(audio_file.getbuffer())
        print("Audio file saved successfully")

    with sr.AudioFile("sumit.wav") as source:
        audio_data = r.record(source)
        try:
            text = r.recognize_google(audio_data)
            st.write(text)
            print("Transcribed text: ", text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")