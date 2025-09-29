# Various functions for input handling and etc.

import subprocess
import sys

from utils.jarvis import prompt
from memory import context, save_into_memory, delete_from_memory
from options import applications
from utils.speech import speak_and_print
from utils.web import get_weather, fetch_website

from enum import Enum

class Command(Enum):
  OPEN_APP = 'OPEN'
  WEATHER_INFO = 'WEATHER'
  NEWS_INFO = 'NEWS'

def command_input(answer: str, command: Command) -> bool:
    return answer.startswith(command.value)

def response_open_application(answer: str):
    
    application_name = answer.replace('OPEN: ', '')

    response = ''

    if applications.get(application_name):
        response = f"Opening {application_name}..."
        speak_and_print(f"Opening {application_name}...") 
        subprocess.Popen(applications[application_name])
    else:
        response = f"{application_name} is not in the list of apps!"

    speak_and_print(response) 

def response_weather_info(answer: str):
    
    city_name = answer.replace("WEATHER", '')
    weather_data = get_weather(city_name)

    response = prompt("SYSTEM INFO: " + weather_data) 

    speak_and_print(response)

def response_news():
    
    html_page = fetch_website("https://news.ycombinator.com/")

    response = prompt(
        "SYSTEM INFO: What follows is the HTML of the current Hacker News front page. "
        f"Fetch important news and tell the user what news are available today.\n\n{html_page}"
    )

    speak_and_print(response) 

def handle(userinput: str):
        
        print(f"User: {userinput}")

        answer = prompt(userinput)
        context.append(f"User: {userinput}")
        context.append(f"J.A.R.V.I.S: {answer}")

        if command_input(answer, Command.OPEN_APP):
            response_open_application(answer=answer)
        elif command_input(answer, Command.WEATHER_INFO):
            response_weather_info(answer=answer)
        elif command_input(answer, Command.NEWS_INFO):
            response_news()
        else:
           speak_and_print(answer) 

        if answer == "Very well sir, I will stand by.":
            sys.exit()
