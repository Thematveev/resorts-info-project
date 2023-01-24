import requests
import config
import urllib.parse


def detect_ski_type(snow_depth):
    if 1 <= snow_depth < 15:
        return "Slalom Skies"
    elif 15 <= snow_depth < 25:
        return "Universal Skies"
    else:
        return "Free Ride Skies"


def detect_clothes_type(temp):
    if temp < -15:
        return "Heavy Clothing"
    elif -15 <= temp < 5:
        return "Medium Clothing"
    else:
        return "Light Clothing"

def get_weather(resort_name):
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    querystring = {"q": resort_name}
    headers = {
        "X-RapidAPI-Key": config.weather_rapid_api_key,
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    return response.json()


def get_snow(resort_name):
    url = f"https://ski-resort-forecast.p.rapidapi.com/{urllib.parse.quote(resort_name)}/snowConditions"
    querystring = {"units": "i"}

    headers = {
        "X-RapidAPI-Key": config.weather_rapid_api_key,
        "X-RapidAPI-Host": "ski-resort-forecast.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()
