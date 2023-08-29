import requests
import os
from twilio.rest import Client

OMW_endpoint = "https://api.openweathermap.org/data/2.8/onecall"
api_key = "0fdf311e3f3577d25c91e6e2a6956173"
account_sid = 'AC1728d85efe54abf0e2e78fa31910a459'
auth_token = 'cc25fa3a418308970f0d54f4d3c38a01'
client = Client(account_sid, auth_token)

weather_params = {
    "lat":18.074090,
    "lon":83.014230,
    "appid":api_key,
    "exclude":"current,minutely,daily"
}

response = requests.get(OMW_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Padaće kiša danas, ponesi kišobran!",
        from_='+12187353820',
        to='+381692298722'
    )
    print(message.status)

# print(data)

# weather_data = data["hourly"][0]["weather"][0]["id"]
# print(weather_data)

# slice() operatori
# a[start:stop] items start through stop-1
# a[start:] items start through the rest of the array
# a[:stop] items from the beginning through stop-1
# a[:] copy of the while array

# python env u terminalu
# kad se radi sa env-om odnosno menja
# npr OMW_API_KEY=nas api
# u kodu u promenljivoj menjano
# api_key = os.environ.get("OMW_API_KEY")
# isto i za token vazi i sakriveni su pod tim u envu kako niko ne bi mogao da koristi sa strane

# API List sajt za Free apije za sajtove






