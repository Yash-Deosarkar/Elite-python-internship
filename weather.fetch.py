import requests

API_KEY = '13cef7bcf1963e5c9983c1b643a78d52'
CITY = 'Pune'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

params = {
    'q': CITY,
    'appid': API_KEY,
    'units': 'metric'
}

response = requests.get(BASE_URL, params=params)
data = response.json()

if response.status_code == 200:
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']} °C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Weather: {data['weather'][0]['description']}")
else:
    print("Error:", data)
