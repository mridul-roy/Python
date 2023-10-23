import requests

API_key = "58833639263de97074a9f2214c06e0ad"


END_point = "https://api.openweathermap.org/data/2.5/weather"
#END_point = "https://api.openweathermap.org/data/2.5/onecall"


weather_params = {
    "lat": 24.848078,
    "lon": 89.372963,
    "appid": API_key,
    "exclude": "current,minutely,hourly"

}

response = requests.get(END_point, params=weather_params)

response.raise_for_status()
data = response.json()

print(data)