import requests
import json
city = 'Lalitpur'
api_key = '230ad6234ddee8d059a98dafb9d217ca'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

def test():
    print('Hello world')

response = requests.get(url)


if response.status_code == 200:
    weather_data = response.json()
    #print(json.dumps(weather_data , indent=2))
    #print('Connection Secured')

    main_weather = weather_data['weather'][0]['description']
    max_temp = weather_data['main']['temp_max']
    min_temp = weather_data['main']['temp_min']
    rounded_max_cel = round((max_temp-273.15) ,2)
    rounded_min_cel = round((min_temp-273.15) , 2)


    #print(main_weather)
    #print(rounded_max_cel)
    #print(rounded_min_cel)
else:
    print('Status Failed')
