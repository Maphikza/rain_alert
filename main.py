import requests
import os
from twilio.rest import Client

api_key = os.environ.get("api_key")
account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")
twilio_num = os.environ.get("twilio_num")
my_num = os.environ.get("my_num")


parameters = {
    "lat": 45.815010,
    "lon": 15.981919,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

data = response.json()
hourly_data = data["hourly"][:12]


def rain_check(day_weather):
    for weather in day_weather:
        if weather["weather"][0]["id"] < 700:
            return True


if rain_check(hourly_data):
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                         body="Hey man, Bring an Umbrella. It's about to come down.",
                         from_=twilio_num,
                         to=my_num
                     )

    print(message.status)