# Functions related to sending and scheduling notifications.

import requests
import threading 
from options import pushbullet_secret
from time import sleep

def send_notification_instant(title: str, body: str) -> bool:
    
    ACCESS_TOKEN = pushbullet_secret

    url = "https://api.pushbullet.com/v2/pushes"

    headers = {
        "Access-Token": ACCESS_TOKEN,
        "Content-Type": "application/json"
    }

    data = {
        "type": "note",
        "title": f"{title}",
        "body": f"{body}"
    }

    response = requests.post(url, json=data, headers=headers)

    return response.status_code == 200

# Delay in seconds.
def send_notification_delay(title: str, body: str, delay: int) -> bool:
    sleep(delay)
    return send_notification_instant(title, body)

def schedule_notification(title: str, body: str, delay: int):
    noti_thread = threading.Thread(
        target=send_notification_delay, args=(title, body, delay), daemon=True
    )
    noti_thread.start()