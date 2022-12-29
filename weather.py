import requests


def get_weather(resort_name):
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    querystring = {"q": resort_name}
    headers = {
        "X-RapidAPI-Key": "d7a0edba2fmshb5939cf9d313cacp10e2d9jsn2964ededae8a",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    return response.json()
