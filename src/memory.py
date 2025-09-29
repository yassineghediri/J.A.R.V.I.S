import os

# Short Term Memory (context)
context = []

# Base directory of the project (src/.. = project root)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MEMORY_FILE = os.path.join(BASE_DIR, "data", "memory.txt")

# Long Term Memory
def save_into_memory(memory: str):

    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
    with open(MEMORY_FILE, "a", encoding="utf-8") as memfile:
        memfile.write(memory + "\n")

def load_from_memory() -> str:
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
    if not os.path.exists(MEMORY_FILE):
        return ""
    with open(MEMORY_FILE, "r", encoding="utf-8") as memfile:
        return memfile.read()

def delete_from_memory(target: str):
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
    if not os.path.exists(MEMORY_FILE):
        return
    with open(MEMORY_FILE, "r", encoding="utf-8") as memfile:
        lines = memfile.readlines()
    lines = [line for line in lines if line.strip() != target]
    with open(MEMORY_FILE, "w", encoding="utf-8") as memfile:
        memfile.writelines(lines)
