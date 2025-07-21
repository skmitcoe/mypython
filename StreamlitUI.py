import streamlit as st
import speech_recognition as sr
from googletrans import Translator

async def translate(text, dest_lang="en"):
    try:
        translator = Translator()
        print("def translate(): input text: ", text)
        translation = await translator.translate(text, dest=dest_lang)
        translated_text = translation.text
        print("def translate(): translated text: ", translated_text)
        return translated_text
    except Exception as ex:
        print(f"Translation exception: {ex}")
        return None


st.title(":rainbow[Sumit Kumar's AI Space]")
st.write("My web page to explore Natural Language Processing")

if st.button('Generate'):
    st.write("This is the generated text on click of Generate button")

audio_file = st.audio_input("Record your voice message")
r = sr.Recognizer()


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

async def main():
    if st.button('Translate to Marathi'):
        translated_text = await translate(input_text, dest_lang="mr")
        st.write(translated_text)

    if st.button('Translate to Hindi'):
        translated_text = await translate(input_text, dest_lang="hi")
        st.write(translated_text)

    if st.button('Translate to Kannada'):
        translated_text = await translate(input_text, dest_lang="kn")
        st.write(translated_text)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

select_option = st.selectbox('What is you favourite color?', ("Red", "Blue", "Green"), index=None, placeholder="Enter your favourite color")
if select_option:
    st.write('Your favourite color is:', select_option)

radio_option = st.radio("What is you favourite movie genre?", ("Comedy", "Drama", "Documentary"), index=None)
if radio_option:
    st.write('Your favourite movie genre is:', radio_option)

multiselect_option = st.multiselect("What are your favourite colors?", ("Red", "Blue", "Green", "Yellow"), placeholder="Enter your favourite color(s)")
if multiselect_option:
    st.write('You selected:', multiselect_option)