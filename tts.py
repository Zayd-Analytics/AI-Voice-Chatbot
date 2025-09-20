from gtts import gTTS
import os

def text_to_speech(text, lang="en", slow=False):
    tts = gTTS(text=text, lang=lang, slow=slow)
    filename = "output.mp3"
    tts.save(filename)
    os.system(f"start {filename}")  # For Windows, adjust for Linux/Mac
    return filename
