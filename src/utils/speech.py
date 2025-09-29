# Functions for speech recognition.
import speech_recognition as sr 
import threading
from voice import speak
from text import print_slow

r = sr.Recognizer()

def record() -> str:
    while True:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2) # pyright: ignore[reportArgumentType]
                audio2 = r.listen(source2)
                output = r.recognize_google(audio2) # pyright: ignore[reportAttributeAccessIssue]
                return output
        except Exception as e:
            print(e)

def record_until_silence(phrase_limit = None) -> str:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2) # type: ignore
        print("Listening... Speak now.")
        audio = r.listen(source, phrase_time_limit=phrase_limit)
    try:
        return r.recognize_google(audio) # type: ignore
    except Exception as e:
        print(e)
        return ""

def speak_and_print(text: str):
    # start speech in background
    t1 = threading.Thread(target=speak, args=(text,))
    t1.start()

    # print at the same time
    print("J.A.R.V.I.S: ", end="", flush=True)
    print_slow(text)

    # optional: wait until speech finishes
    t1.join()