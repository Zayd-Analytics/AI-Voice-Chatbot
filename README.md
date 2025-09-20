# 🎙️ Voice AI Chatbot

A professional, voice-enabled chatbot built with **Streamlit** that converts user speech → text, queries the **Gemini** (Google Generative) API for a response, and converts the reply back to audio using **gTTS**. Designed for local demos and prepared for production deployment with guidance included.

---

## 🚀 Features
- 🎤 **Speech-to-Text (STT)**: Microphone input → text (using `speech_recognition`)
- 🤖 **LLM Responses**: Gemini API generates context-aware replies
- 🔊 **Text-to-Speech (TTS)**: gTTS converts responses to audio
- 🌐 **Streamlit UI**: Simple web interface with record button, transcript, response text, and audio playback
- 🔐 **Secure**: Uses environment variables / secrets for storing API keys (do not commit keys)

---

## 📁 Project structure
voice_chatbot/
├─ app.py # Main Streamlit app (entrypoint)
├─ stt.py # Speech-to-Text helper functions
├─ tts.py # Text-to-Speech helper functions
├─ chatbot.py # Gemini API wrapper
├─ requirements.txt
├─ README.md
├─ .env # (local - add to .gitignore)
└─ .gitignore

yaml
Copy code

> Note: For quick demo you can also keep everything in `app.py`. Modular layout is preferred for production.

---

## ⚙️ Prerequisites
- Python 3.8+ (recommended 3.9 or 3.10)
- Microphone connected & allowed for apps (OS microphone permissions)
- Internet connection (both `recognize_google` used by `speech_recognition` and `gTTS` require internet; Gemini needs internet and an API key)

---

## 📥 requirements.txt (example)
streamlit
speechrecognition
gtts
google-generativeai
pyaudio
python-dotenv

yaml
Copy code
> Add optional libs if you use browser-based audio or Gradio: `streamlit-webrtc`, `gradio`.

---

## 🔧 Setup (local)
1. Clone:
```bash
git clone https://github.com/Zayd-Analytics/voice-ai-chatbot.git
cd voice-ai-chatbot
Create & activate venv:


python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
Install deps:

bash
pip install -r requirements.txt
Add API key (local): create a .env file in project root:

ini
GEMINI_API_KEY="your_gemini_api_key_here"
or export in your shell:

bash
# Windows (PowerShell)
$env:GEMINI_API_KEY="your_gemini_api_key_here"
# macOS/Linux
export GEMINI_API_KEY="your_gemini_api_key_here"
Run:

bash
streamlit run app.py
Open the Streamlit URL shown in the terminal (usually http://localhost:8501).

🧩 How it works (short)
User clicks Start Recording → microphone audio captured (local machine).

speech_recognition transcribes audio to text (Google web recognizer by default).

The transcribed text is sent to the Gemini model via the google-generativeai client.

Gemini's text response is converted into a .mp3 using gTTS and played back.

Streamlit shows the original transcript, the LLM response text, and the audio player.

⚠️ Important Deployment Notes (Read carefully)
Local microphone code (speech_recognition with Microphone()) works only when the app runs on your local machine.
If you deploy the app to Streamlit Cloud or Hugging Face Spaces, server-side microphone capture will not capture the end-user’s browser microphone — the server has no direct access to the user’s device mic.

Options for deploying a voice-enabled web app:

Replace speech_recognition.Microphone() with a browser-side recorder and upload the audio to the server (or directly to a cloud STT service).

Use streamlit-webrtc to capture browser audio (requires additional setup).

Use Gradio for deployment (Gradio provides browser mic support and is friendly on Hugging Face Spaces).

For production STT/TTS, use cloud services (Google Cloud Speech-to-Text, Azure Speech, Amazon Transcribe/Polly, Deepgram) and stream/upload recorded audio to those services.

Recommendation: For a demo on Hugging Face Spaces → re-implement the frontend using Gradio (it supports microphone input in browser) and call the Gemini API plus TTS. For Streamlit Cloud → implement browser recording + upload or streamlit-webrtc.

🔁 Deployment (quick guide)
Streamlit Cloud
Push repo to GitHub.

Create new app on Streamlit Cloud → point to repo and branch.

Add GEMINI_API_KEY to Streamlit Secrets (Settings → Secrets) — DO NOT push .env.

IMPORTANT: For voice, either:

Use file upload to give audio (user records locally and uploads), or

Use streamlit-webrtc to capture browser audio (advanced).

Start the app.

Hugging Face Spaces (recommended for voice)
Create a new Space (select Gradio or Streamlit runtime — Gradio is easiest for browser mic).

Push code to the Space repo.

Add secrets in Space settings (GEMINI_API_KEY).

If using Gradio, you can use microphone=True in the interface and handle the uploaded audio server-side.

🔧 Troubleshooting (common issues)
ModuleNotFoundError: No module named 'pyaudio' on Windows

Install using pipwin:

bash
Copy code
pip install pipwin
pipwin install pyaudio
Or use an unofficial wheel for your Python version.

Linux (Ubuntu) pyaudio build error

bash
Copy code
sudo apt-get install portaudio19-dev python3-pyaudio
pip install pyaudio
Microphone not found / permission denied

Check OS microphone permissions and your browser permissions.

Speech not transcribing / Slow

recognize_google uses Google web API and needs internet. Consider cloud STT for production.

gTTS fails

Requires internet. For production-level TTS use Google Cloud TTS / Azure / Polly for high-quality voices.

🔒 Security & Privacy
Never commit API keys. Use .env and .gitignore or deployment secrets.

Be mindful of audio data — if you store recordings, clearly document retention and privacy policy.

Production: consider encrypting logs and restricting access to keys.

♻️ Future Improvements
Replace recognize_google with professional cloud STT for accuracy & multi-language support

Add RAG (Retrieval Augmented Generation) to answer from a knowledge base

Add PEFT / LoRA based fine-tuning for specialized domain answers

Implement browser-based real-time streaming and speaker diarization

📝 License
MIT License — see LICENSE (add if you want).

❤️ Credits / Contact
Built by:Mohd Zayd Quadri
Questions / demo in class — ping me and I’ll present the live demo.
