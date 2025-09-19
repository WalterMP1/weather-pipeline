# extract.py
import requests
import logging
from datetime import datetime, timezone
from config import API_KEY
from logger_config import get_logger

logger = get_logger(__name__)

def get_city_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        logging.info(f"Extracting weather for {city}")
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
        main = data.get("main", {})
        weather_list = data.get("weather", [])
        temp = main.get("temp")
        feels_like = main.get("feels_like")

        if weather_list and len(weather_list) > 0:
            weather_main = weather_list[0].get("main")
            weather_desc = weather_list[0].get("description")
        else:
            weather_main = None
            weather_desc = None
        
        return {
            "city": data.get("name"),
            "country": data.get("sys", {}).get("country"),
            "timestamp_utc": datetime.fromtimestamp(data.get("dt"), tz=timezone.utc),
            "temp": temp,
            "feels_like_c": feels_like,
            "weather_main": weather_main,
            "weather_desc": weather_desc,
        }
    
    except requests.exceptions.RequestException as e:
            logging.error(f"Connection error for {city}: {e}", exc_info=True)
    except Exception as e:
            logging.error(f"Error processing data for {city}: {e}",exc_info=True)


def fetch_all(cities):
    rows = []
    for c in cities:
        try:
            rows.append(get_city_weather(c))
        except Exception as e:
            print(f"Error {c}: {e}")
    return rows