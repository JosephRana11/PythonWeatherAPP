import requests
import json
from datetime import datetime
city = input('Enter City:')
api_key = '230ad6234ddee8d059a98dafb9d217ca'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    print('Connection Established')
    weather_data = response.json()
    print(json.dumps(weather_data , indent=2))

    main_weather = weather_data['weather'][0]['main']
    location = weather_data['name']
    temp = weather_data['main']['temp']
    cel_temp = (temp-273.15)
    rounded_cel_temp = round(cel_temp, 2)
    if 'sys' in weather_data and 'sunset' in weather_data['sys']:
        sunset_timestamp = weather_data['sys']['sunset']
        if isinstance(sunset_timestamp, int):
            sunset_datetime = datetime.fromtimestamp(sunset_timestamp)
            sunset_time = sunset_datetime.strftime('%H:%M:%S')
        else:
            print('Invalid sunset timestamp')
    else:
        print('Sunset data not found')
    print('Location:', location)
    print('Temperature Today:', rounded_cel_temp, 'degree celsius')
    print('Main weather Today:', main_weather)
    print('Sunset Time Today:', sunset_time)
else:
    print('Request failed with status code:', response.status_code)