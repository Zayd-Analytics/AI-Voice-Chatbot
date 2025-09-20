import streamlit as st
import stt
import tts
import chatbot

st.set_page_config(
    page_title="Voice AI Chatbot",  # Appears in browser tab
    page_icon="🗣️",                # Optional: emoji or icon
    layout="centered",              # Or "wide"
    initial_sidebar_state="auto"    # Or "expanded"/"collapsed"
)

st.title("🎙️ AI Voice Chatbot")
st.markdown("Talk with an AI Assistant using Speech-to-Text and Text-to-Speech.")

if st.button("🎤 Start Recording"):
    st.write("Listening...")
    query = stt.speech_to_text()
    st.write("🗣️ You said:", query)

    if query:
        response = chatbot.get_gemini_response(query)
        st.write("🤖 AI Response:", response)

        audio_file = tts.text_to_speech(response)
        st.audio(audio_file, format="audio/mp3")


