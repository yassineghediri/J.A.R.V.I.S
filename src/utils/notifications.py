import requests
from options import pushbullet_secret

def send_notification(title: str, body: str) -> bool:
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

    if response.status_code == 200:
        return True 
    else:
        return False
