# Various functions for input handling and etc.
import subprocess
import sys 

from jarvis import prompt 
from memory import context 
from options import applications
from speech import speak_and_print
from web import get_weather, fetch_website



def handle(userinput: str):
        print(f"User: {userinput}")
        answer = prompt(userinput)
        context.append(f"User: {userinput}")
        context.append(f"J.A.R.V.I.S: {answer}")
        if answer.startswith("OPEN"): 
            application_name = answer.replace('OPEN: ', '')
            if applications.get(application_name):
                answer = f"Opening {answer.replace('OPEN: ', '')}..."
                speak_and_print(answer) 
                subprocess.Popen(applications[application_name])
            else:
                answer = f"{application_name} is not in the list of apps!"
                speak_and_print(answer)
            speak_and_print(answer) 
        elif answer.startswith("WEATHER"):
            city_name = answer.replace("WEATHER", '')
            weather_data = get_weather(city_name)
            answer = prompt("SYSTEM INFO: " + weather_data) 
            speak_and_print(answer)
        elif "NEWS" == answer:
            answer = prompt("SYSTEM INFO: What follow is the HTML of the current Hacker News front page, fetch important news and tell the user what news are available today. \n\n" + fetch_website("https://news.ycombinator.com/"))
            speak_and_print(answer) 
        else:
           speak_and_print(answer) 
        if answer == "Very well sir, I will stand by.":
            sys.exit()