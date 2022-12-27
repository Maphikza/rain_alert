import requests
import os
from twilio.rest import Client

api_key = "49b4ead1fbe4e4428c01412e9ec96409"
account_sid = 'AC803c14eeab4de3c5b7e85d6507579cf8'
auth_token = '3003f3997add7e4d64f4a5eb72283cbd'


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
                         from_='+19592712407',
                         to='+27615360089'
                     )

    print(message.status)