import requests

url = "https://world-of-jokes1.p.rapidapi.com/v1/jokes/categories"
json_data=requests.get(url).json()

arr=["".""]
arr[0]=json_data["setup"]
arr[1]=json_data["punchlone"]
def joke():
    return arr
