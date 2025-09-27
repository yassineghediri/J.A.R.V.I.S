import os
from groq import Groq  # type: ignore
import datetime
import pytz
import socket
from playsound import playsound  # type: ignore
import tempfile
from gtts import gTTS  # type: ignore
import speech_recognition as sr  # type: ignore
import subprocess


# TODO: modularize

# VARIABLES
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
r = sr.Recognizer()


# applications dictionary
applications = {
    # Browsers
    "Browser": "C:\\Program Files\\Mozilla Firefox\\firefox.exe",
    "Firefox": "C:\\Program Files\\Mozilla Firefox\\firefox.exe",
    "Chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "Edge": "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
    "Opera": "C:\\Program Files\\Opera\\launcher.exe",

    # Office / Productivity
    "Word": "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
    "Excel": "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE",
    "PowerPoint": "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE",
    "Notepad": "C:\\Windows\\system32\\notepad.exe",
    "Calculator": "C:\\Windows\\system32\\calc.exe",
    "Paint": "C:\\Windows\\system32\\mspaint.exe",
    "Snipping Tool": "C:\\Windows\\system32\\SnippingTool.exe",
    "WordPad": "C:\\Program Files\\Windows NT\\Accessories\\wordpad.exe",

    # Media
    "Spotify": "C:\\Users\\%USERNAME%\\AppData\\Roaming\\Spotify\\Spotify.exe",
    "VLC": "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe",
    "Movies": "C:\\Program Files\\WindowsApps\\Microsoft.ZuneVideo_8wekyb3d8bbwe\\Video.UI.exe",
    "Windows Media Player": "C:\\Program Files\\Windows Media Player\\wmplayer.exe",

    # System Tools
    "Command Prompt": "C:\\Windows\\system32\\cmd.exe",
    "PowerShell": "C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\powershell.exe",
    "Task Manager": "C:\\Windows\\system32\\Taskmgr.exe",
    "File Explorer": "C:\\Windows\\explorer.exe",
    "Registry Editor": "C:\\Windows\\regedit.exe",
    "Control Panel": "C:\\Windows\\system32\\control.exe",

    # Communication
    "Teams": "C:\\Users\\%USERNAME%\\AppData\\Local\\Microsoft\\Teams\\Update.exe --processStart \"Teams.exe\"",
    "Zoom": "C:\\Users\\%USERNAME%\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe",
    "Discord": "C:\\Users\\%USERNAME%\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    "Skype": "C:\\Program Files (x86)\\Microsoft\\Skype for Desktop\\Skype.exe",
    "Slack": "C:\\Users\\%USERNAME%\\AppData\\Local\\slack\\slack.exe"
}

# context list
context = [] 


def get_context() -> (str | None):
    output = ""
    if len(context) < 1:
        return None
    for message in context:
        if message:
            output += (message + "\n")
        else:
            break 
    return output if output != "" else None

        
def get_relevant_info():
    tz = pytz.timezone("Africa/Tunis")
    now = datetime.datetime.now(tz)
    current_time = now.strftime("%Y-%m-%d %H:%M:%S %Z")
    hostname = socket.gethostname()
    info = f"Current local time and date: {current_time}\nHostname of the user's machine: {hostname}\nLocation: Tunis, Tunisia"
    return info


def record() -> str:
    while True:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                output = r.recognize_google(audio2)
                return output
        except Exception as e:
            print(e)


def speak(text: str):
    chunks = [text[i:i + 500] for i in range(0, len(text), 500)]
    for chunk in chunks:
        tts = gTTS(text=chunk, lang="en", slow=False)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            filename = fp.name
        tts.save(filename)
        playsound(filename)
        os.remove(filename)


def prompt(user_instruction: str) -> str:
    app_list_str = ", ".join(applications.keys())
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"""
                    You are Jarvis (Just A Rather Very Intelligent System), an advanced AI designed for precision, intelligence, and subtle wit. 
                    Follow these rules strictly:

                    RULES:
                    1. If the user asks to open a program, respond ONLY as: OPEN: <program name>. No extra words. Auto-correct near-misses using the app list: {app_list_str}. Do not ask for confirmation. If the request is absurd or fictional, pass it exactly as given.
                    2. If the user hints at leaving, stopping, or saying goodbye, respond ONLY: Very well sir, I will stand by.
                    3. Always address the user as 'Sir' unless instructed otherwise.
                    4. Keep humor dry, understated, and subtle.
                    5. Provide structured, actionable responses.
                    6. All other instructions: respond accurately, concisely, and optimize outcomes.

                    Relevant info: {get_relevant_info()}
                    Context: {get_context() if len(context) > 0 else "None, ignore this for now."}
                    User instruction: {user_instruction}
                    """
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message.content

# Main loop
while True:
    txt = record()
    if "jarvis" in txt.lower():
        userinput = txt
        print(f"User: {userinput}")
        answer = prompt(userinput)
        context.append(f"User: {userinput}")
        context.append(f"J.A.R.V.I.S: {answer}")
        if "OPEN" in answer: 
            application_name = answer.replace('OPEN: ', '')
            if applications.get(application_name):
                answer = f"Opening {answer.replace('OPEN: ', '')}..."
                print(f"J.A.R.V.I.S: {answer}")
                speak(answer) 
                subprocess.Popen(applications[application_name])
            else:
                answer = f"{application_name} is not in the list of apps!"
                print(f"J.A.R.V.I.S: {answer}")
                speak(answer)
        else:
            print(f"J.A.R.V.I.S:  {answer}")
            speak(answer)
        if answer == "Very well sir, I will stand by.":
            break

