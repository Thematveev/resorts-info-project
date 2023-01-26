import requests



def get_map_info(resort_name):
    base_link = f"https://api.openskimap.org/search?query={resort_name}"
    response = requests.get(base_link).json()
    return response




