from utils.speech import listen_from_mic
from src.utils.executor import handle
from utils.speech import listen_from_mic, speak_and_print
from utils.executor import handle
from utils.jarvis import initialize
from memory import context

def main():
    global context
    initialize()
    while True:
        prompt = listen_from_mic()
        if len(context) > 25:
            context = []
        if prompt.lower().strip() == "jarvis" or prompt.lower().strip() == "hey jarvis":
            speak_and_print("Yes, sir?")
            prompt = listen_from_mic()
            handle(prompt)
        elif "jarvis" in prompt.lower():
            handle(prompt)
  
if __name__ == "__main__":
    main()