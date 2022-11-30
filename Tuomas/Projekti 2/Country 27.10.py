import mysql.connector
import requests
import json

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='lentopeli',
    password='peli',
    autocommit=True
)
kursori = yhteys.cursor()


class Country:
    def __init__(self,city_name,):

    pass

# Fetching cityName and airportName from the database
kursori.execute("SELECT cityName from gameCountries where name='Unkari'")
cityname = kursori.fetchone()
city_name = cityname[0]

kursori.execute("SELECT airportName from gameCountries where name ='Unkari'")
airportname = kursori.fetchone()
airport_name = airportname[0]

# weather data taken from openweathermap api with cityname
apikey = '57d9761bd41e88656771c5c3745a9924'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={apikey}&units=metric'
response = requests.get(url)
data = json.loads(response.text)
temp = data['main']['temp']

# Welcome text:
print(f'Tervetuloa {airport_name} nimiselle lentokentälle!\nOlet nyt kaupungissa {city_name}. Lämpötila on {temp} celsius astetta.')
