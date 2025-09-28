# Various text related functions. 

import time

def print_slow(text: str, delay: float = 0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print() 
    