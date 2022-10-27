import requests
import json
apikey = '57d9761bd41e88656771c5c3745a9924'
cityname = input('Anna kaupungin nimi:')
url = f'https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={apikey}&units=metric'
response = requests.get(url)
data = json.loads(response.text)
print(data)
temp = data['main']['temp']
print(f'{cityname} nimisessä kaupungissa lämpötila on {temp} celsius astetta.')