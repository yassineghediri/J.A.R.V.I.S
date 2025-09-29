from utils.speech import record
from src.utils.executor import handle

def main():
    global context
    initialize()
    while True:
        prompt = record()
        if len(context) > 25:
            context = []
        if prompt.lower().strip() == "jarvis":
            speak_and_print("Yes, sir?")
            prompt = record()
            handle(prompt)
        elif "jarvis" in prompt.lower():
            handle(prompt)
        
            
            
              
if __name__ == "__main__":
    main()