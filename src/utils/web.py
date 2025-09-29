# Internet / Web related functions.
from options import weather_key
import requests 

def fetch_website(uri: str) -> str:
    try:
        response = requests.get(uri)
        response.raise_for_status()
        html = response.text 

        return html

    except Exception as e:
        return f"Something has went wrong, notify the user of likely missing internet connection. API CALL FAILED. Exception: {e}"

def get_weather(city: str) -> str:
    try:
        URI = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}&units=metric"
        response = requests.get(URI)
        response.raise_for_status()
        weather_data = response.json()

        if weather_data["cod"] == 200:
            main_weather = weather_data["weather"][0]["main"]
            description = weather_data["weather"][0]["description"]
            temperature = weather_data["main"]["temp"]
            return f"The weather in {city} is {main_weather}. Description: {description}. The temperature is {temperature}."
        else: 
            return "Something has went wrong, notify the user of likely missing internet connection. API CALL FAILED."

    except Exception as e: 
        return f"Something has went wrong, notify the user of likely missing internet connection. API CALL FAILED. Exception: {e}"