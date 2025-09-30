# Various functions for input handling and etc.

import subprocess
import sys

from shared.commands import Command

from memory import context 
from memory import context, save_into_memory, delete_from_memory
from options import applications
from utils.jarvis import prompt
from utils.speech import speak_and_print
from utils.web import get_weather, fetch_website
from utils.notifications import schedule_notification, send_notification_instant

def command_input(answer: str, command: Command) -> bool:
    return answer.startswith(command.value)

def response_notification_instant(answer: str):
    
    content = answer.replace("NOTIFY", "", 1).strip()
    parts = content.split(" ", 1)
    title = parts[0]
    body = parts[1] if len(parts) > 1 else ""
    if send_notification_instant(title, body):
        response = prompt(f"SYSTEM INFO: Sending a notification with title: {title} and body: {body} was successful. Confirm to the user, but do not repeat the title, or the body.")
    else:
        response = prompt(f"SYSTEM INFO: Sending a notification with title: {title} and body: {body} was unsuccessful. Confirm to the user, but do not repeat the title, or the body.")
    speak_and_print(response)
    
    
def response_notification_delay(answer: str):
    
    # Remove the NOTIFY_DELAY keyword
    content = answer.replace("NOTIFY_DELAY", "", 1).strip()
    parts = content.rsplit(" ", 1)
    delay = int(parts[1])
    title_body = parts[0].split(" ", 1)
    title = title_body[0]
    body = title_body[1] if len(title_body) > 1 else ""
    schedule_notification(title, body, delay)
    response = prompt(f"SYSTEM INFO: Scheduling a notification with title: {title} and body: {body} after delay: {delay} was successful. Confirm to the user, but do not repeat the title, or the body.")
    speak_and_print(response)

def response_del_mem(answer: str):
    memory_content = answer.replace('REMOVE', '')
    delete_from_memory(memory_content)
    response = prompt(f"SYSTEM INFO: {memory_content} has been deleted from memory. Confirm to the user.")
    speak_and_print(response)


def response_add_mem(answer: str):
    memory_content = answer.replace('ADD', '')
    save_into_memory(memory_content)
    response = prompt(f"SYSTEM INFO: {memory_content} has been saved into memory. Confirm to the user.")
    speak_and_print(response)


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
        elif command_input(answer, Command.SEND_NOTIFICATION_DELAYED):
            response_notification_delay(answer=answer)
        elif command_input(answer, Command.SEND_NOTIFICATION):
            response_notification_instant(answer=answer)
        elif command_input(answer, Command.SAVE_MEM):
            response_add_mem(answer=answer)
        elif command_input(answer, Command.DEL_MEM):
            response_del_mem(answer=answer)

        else:
           speak_and_print(answer) 

        if answer == "Very well sir, I will stand by.":
            sys.exit()
