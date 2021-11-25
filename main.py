import requests
from twilio.rest import Client

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
# BASH script: $ export OWM_API_KEY=5ab2712474784f6121a244dfea15ae1a
# API_KEY = os.environ.get("OWM_API_KEY")
API_KEY = "5ab2712474784f6121a244dfea15ae1a"
account_sid = 'ACe183e5cdad3da600bcaca85d245fb075'
# BASH script: $ export AUT_TOKEN=fad224f8c7ec893799e350b76910341e
# auth_token = os.environ.get("AUT_TOKEN")
auth_token = 'fad224f8c7ec893799e350b76910341e'

parameters = {
    # Joburg: -26.204103, 28.047304
    "lat": -26.204103,
    "lon": 28.047304,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

# weather_data["hourly"][each_day]["weather"][0]["id"]

# Slice notation
# a[start:stop]  # items start through stop-1
# a[start:]      # items start through the rest of the array
# a[:stop]       # items from the beginning through stop-1
# a[:]           # a copy of the whole array

will_rain = False

# Creating a list of all the hours from 0 - 11 (1 - 12)
weather_slice = weather_data["hourly"][:12]
for each_hour in weather_slice:
    condition_code = each_hour["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

phone_numbers = ['+27765831900', '+27629232051']

if will_rain:
    for each_number in phone_numbers:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="It's going to rain today. Bring an Umbella.",
            from_='+18128073534',
            to=each_number
        )
        print(message.status)
