import urllib.request
import json
from configS import OPENWEATHERMAP_WEATHER
import pprint

APIKEY = OPENWEATHERMAP_APIKEY
city = 'Wellesley'
country_code = 'us'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={WEATHER}'

# print(url)

with urllib.request.urlopen(url) as f:
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    
print(response_data)

pprint.pprint(response_data)

# How do we get current temperature?