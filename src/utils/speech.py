# Functions for speech recognition.
import speech_recognition as sr 
import threading
from voice import speak
from text import print_slow

recognizer = sr.Recognizer()

# pyright: ignore[reportArgumentType]
# pyright: ignore[reportAttributeAccessIssue]

def listen_from_mic(phrase_limit: int | None = None) -> str:
    
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        print("Listening... Speak now.")
        audio = recognizer.listen(source, phrase_time_limit=phrase_limit)

    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("Sorry I couldn't understand that.")
    except sr.RequestError as e:
        print(f"Could not request results: {e}")
    return ""

def record_until_success() -> str:
  
    while True:
        text = listen_from_mic()
        if text:
            return text

def speak_and_print(text: str, wait: bool = False):
    
    t1 = threading.Thread(target=speak, args=(text,), daemon=True)
    t1.start()

    print("J.A.R.V.I.S: ", end="", flush=True)
    print_slow(text)

    if wait:
        t1.join()