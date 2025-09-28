# Functions for text to speech.
from gtts import gTTS  
import tempfile
from playsound import playsound  
import os

def speak(text: str):
    chunks = [text[i:i + 500] for i in range(0, len(text), 500)]
    for chunk in chunks:
        tts = gTTS(text=chunk, lang="en", slow=False)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            filename = fp.name
        tts.save(filename)
        playsound(filename)
        os.remove(filename)