import requests
import os
from twilio.rest import Client


OMW_Endpoint = 'https://api.openweathermap.org/data/3.0/onecall'
api_key = os.environ.get('OMW_API_KEY')
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
personal_cell = os.environ.get('PERSONAL_CELL')


parameters = {
    'lat': 39.739235,
    'lon': -104.990250,
    'appid': api_key,
    'exclude': 'current,minutely,daily'
}

response = requests.get(OMW_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 600:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
         body="It's going to rain today. Remember to bring an umbrella.",
         from_='+18666983577',
         to=personal_cell
    )
    print(message.status)