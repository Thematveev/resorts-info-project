import requests
import config
import urllib.parse

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
    querystring = {"units":"i"}

    headers = {
        "X-RapidAPI-Key": config.weather_rapid_api_key,
        "X-RapidAPI-Host": "ski-resort-forecast.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()