from utils.speech import record
from src.utils.executor import handle

def main():
    while True:
        prompt = record()
        if len(context) > 25:
            context = []
        if "jarvis" in prompt.lower():
            handle(prompt)
              
if __name__ == "__main__":
    main()