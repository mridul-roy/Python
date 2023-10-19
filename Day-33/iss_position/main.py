import time
import requests
from datetime import datetime
import smtplib

MY_LAT = 23.684994  # Your latitude
MY_LONG = 90.356331  # Your longitude
MY_ADDRESS = "arnobroy0007@gmail.com"
MY_PASSWORD = "1234567889"  # Your Password


def iss_on_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= MY_LAT >= MY_LAT + 5 and MY_LONG - 5 <= MY_LONG >= MY_LONG + 5:
        print(iss_longitude)
        print(iss_latitude)
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if sunset <= time_now or sunrise >= time_now:
        return True


while True:
    time.sleep(60)
    if iss_on_overhead() and is_night():
        with smtplib.SMTP("mail.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_ADDRESS, MY_PASSWORD)
            connection.sendmail(from_addr=MY_ADDRESS,
                                to_addrs="mridulroy010@yahoo.com",
                                msg="Subject:ISS on your head\n\nHello, Look up.Hope that you have a grate day.")
