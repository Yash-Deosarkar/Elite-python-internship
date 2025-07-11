import requests
import matplotlib.pyplot as plt

API_KEY = '13cef7bcf1963e5c9983c1b643a78d52'
CITIES = ['Pune', 'Mumbai', 'Delhi', 'Kolkata', 'Chennai']
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

temperatures = []
humidities = []

for city in CITIES:
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        temperatures.append(data['main']['temp'])
        humidities.append(data['main']['humidity'])
    else:
        print(f"Failed to get data for {city}")
        temperatures.append(None)
        humidities.append(None)

# 📊 Plot temperature and humidity
plt.figure(figsize=(10, 5))

# Temperature bar chart
plt.subplot(1, 2, 1)
plt.bar(CITIES, temperatures, color='orange')
plt.title('Temperature (°C)')
plt.ylabel('Temp (°C)')
plt.xticks(rotation=30)

# Humidity bar chart
plt.subplot(1, 2, 2)
plt.bar(CITIES, humidities, color='skyblue')
plt.title('Humidity (%)')
plt.ylabel('Humidity')
plt.xticks(rotation=30)

plt.tight_layout()
plt.show()
