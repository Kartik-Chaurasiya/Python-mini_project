import requests
import json
from twilio.rest import Client
from twilio.http_client import TwilioHttpClient
import os


end_point = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = 'weather api'
account_sid = 'twilio acc'
auth_token = 'twilio acc'

parameters = {
    'lat' : 19.456360,
    'lon' : 72.792458,
    'exclude' : 'current,minutely,daily',
    'appid' : api_key
}

will_rain = False

response = requests.get(url = end_point, params = parameters)
data = response.json()
data = data['hourly'][:12]
for each_hour_data in data:
    condition_code = each_hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https' : os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client = proxy_client)

    message = client.messages \
                    .create(
                        body="Its gonna rain.",
                        from_='your twilio no ',
                        to='your no'
                    )

    print(message.status)
