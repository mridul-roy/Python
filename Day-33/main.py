import requests
import datetime as dt

LANGITUDE = 90.356331
LATATUDE = 23.684994

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()
#
# iss_position = data["iss_position"]
#
# print(iss_position)
# print(data)

parameters = {
    "lat": "LATATUDE",
    "lan" : "LANGITUDE",
    "formatted" : "0"

}

response = requests.get("https://api.sunrise-sunset.org/json", params= parameters )
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]


print(sunrise)
print(sunset)

now = dt.datetime.now()
print(now.hour)
