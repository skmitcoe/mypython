import streamlit as st
import speech_recognition as sr
from googletrans import Translator
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/home")
def getname():
    return "This is backend in python"


@app.route("/translate", methods=["POST"])
async def translate():
    input_params = request.get_json()
    text = input_params["text"]
    print("def translate(): param text: ", text)
    dest_lang = input_params["dest_lang"]
    print("def translate(): param dest_lang: ", dest_lang)
    try:
        translator = Translator()
        print("def translate(): input text: ", text)
        translation = await translator.translate(text, dest=dest_lang)
        print("Translated json: ", translation)
        translated_text = translation.text
        print("def translate(): translated text: ", translated_text)
        return translated_text
    except Exception as ex:
        print(f"Translation exception: {ex}")
        return None


st.title(":rainbow[Sumit Kumar's AI Space]")
st.write("My web page to explore Natural Language Processing")

audio_file = st.audio_input("Record your voice message")
r = sr.Recognizer()

st.write("or")

input_text = st.text_input(label="Enter your text")

if audio_file:
    print(audio_file.name)
    with open("sumit.wav", "wb") as f:
        f.write(audio_file.getbuffer())
        print("Audio file saved successfully")

    with sr.AudioFile("sumit.wav") as source:
        audio_data = r.record(source)
        try:
            transcribed_text = r.recognize_google(audio_data)
            input_text = transcribed_text
            st.write(transcribed_text)
            print("Transcribed text: ", transcribed_text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

def post_call(input_text, dest_lang_code):
    with app.test_client() as client:
        response = client.post('/translate',json={'text': input_text, 'dest_lang': dest_lang_code})
        return response.text

dest_lang_code = st.text_input(label="Enter destination language")
if st.button('Translate to input language'):
    translated_text = post_call(input_text, dest_lang_code)
    st.write(translated_text)

if st.button('Translate to Marathi'):
    translated_text = post_call(input_text, "mr")
    st.write(translated_text)

if st.button('Translate to Hindi'):
    translated_text = post_call(input_text, "hi")
    st.write(translated_text)

if st.button('Translate to Kannada'):
    translated_text = post_call(input_text, "kn")
    st.write(translated_text)

select_option = st.selectbox('What is you favourite color?', ("Red", "Blue", "Green"), index=None,
                             placeholder="Enter your favourite color")
if select_option:
    st.write('Your favourite color is:', select_option)

radio_option = st.radio("What is you favourite movie genre?", ("Comedy", "Drama", "Documentary"), index=None)
if radio_option:
    st.write('Your favourite movie genre is:', radio_option)

multiselect_option = st.multiselect("What are your favourite colors?", ("Red", "Blue", "Green", "Yellow"),
                                    placeholder="Enter your favourite color(s)")
if multiselect_option:
    st.write('You selected:', multiselect_option)

if __name__ == "__main__":
    app.run()
    # import asyncio
    # asyncio.run(main())
