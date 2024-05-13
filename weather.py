import requests
from ss import *

api_address=url = "https://ai-weather-by-meteosource.p.rapidapi.com/find_places"
json_data=requests.get(api_address).json()

def temp():
    temperature = round(json_data[|"main"]["temperature"]-273,1)

def_des()
    description=json_data["weather"][0]["descriptions"]
    return description

