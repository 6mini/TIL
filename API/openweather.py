import requests
import json

API_URL = 'https://api.openweathermap.org/data/2.5/weather?q=Seoul&appid=16d025a15855d89923b7f0596620b840'

raw_data = requests.get(API_URL)

parsed_data = json.loads(raw_data.text)

print(parsed_data)
'''
{'coord': {'lon': 126.9778, 'lat': 37.5683}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 'base': 'stations', 'main': {'temp': 297.94, 'feels_like': 298.12, 'temp_min': 297.81, 'temp_max': 299.38, 'pressure': 1004, 'humidity': 63}, 'visibility': 10000, 'wind': {'speed': 5.66, 'deg': 240}, 'clouds': {'all': 20}, 'dt': 1632213819, 'sys': {'type': 1, 'id': 8105, 'country': 'KR', 'sunrise': 1632172726, 'sunset': 1632216711}, 'timezone': 32400, 'id': 1835848, 'name': 'Seoul', 'cod': 200}
'''