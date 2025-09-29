# Various functions for input handling and etc.

import subprocess
import sys

from utils.jarvis import prompt
from memory import context, save_into_memory, delete_from_memory
from options import applications
from utils.speech import speak_and_print
from utils.web import get_weather, fetch_website



def handle(userinput: str):
    global context
    print(f"User: {userinput}")
    answer = prompt(userinput)
    context.append(f"User: {userinput}")
    context.append(f"J.A.R.V.I.S: {answer}")

    match True:
        case _ if answer.startswith("OPEN:"):
            application_name = answer.replace("OPEN:", "").strip()
            if applications.get(application_name):
                msg = f"Opening {application_name}..."
                speak_and_print(msg)
                subprocess.Popen(applications[application_name])
            else:
                msg = f"{application_name} is not in the list of apps!"
                speak_and_print(msg)

        case _ if answer.startswith("WEATHER"):
            city_name = answer.replace("WEATHER", "").strip()
            weather_data = get_weather(city_name)
            result = prompt("SYSTEM INFO: " + weather_data)
            speak_and_print(result)

        case _ if answer == "NEWS":
            news_html = fetch_website("https://news.ycombinator.com/")
            result = prompt(
                "SYSTEM INFO: What follow is the HTML of the current Hacker News front page, "
                "fetch important news and tell the user what news are available today.\n\n" + news_html
            )
            speak_and_print(result)
        
        case _ if answer.startswith("ADD"):
            memory_content = answer.replace("ADD", "").strip()
            print(memory_content)
            save_into_memory(memory_content)
            answer = prompt(f"SYSTEM INFO: {memory_content} has been added into memory, respond with a short, confirmation that the memory has been remembered. do NOT tell the user the memory content again.")
            speak_and_print(answer)
        case _ if answer.startswith("REMOVE"):
            memory_content = answer.replace("REMOVE", "").strip()
            print(memory_content)
            delete_from_memory(memory_content)
            answer = prompt(f"SYSTEM INFO: {memory_content} has been remove from memory, respond with a short, confirmation that the memory has been remembered. do NOT tell the user the memory content again.")
            speak_and_print(answer)
        case _:
            speak_and_print(answer)

    if answer == "Very well sir, I will stand by.":
        sys.exit()

