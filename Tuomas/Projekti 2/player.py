import json
import requests
import mysql.connector


yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='lentopeli',
    password='peli',
    autocommit=True
)
kursori = yhteys.cursor()

class Player:
    def __init__(self, username):
        self.username = username
        self.suspectIndex = ['Mary', 'Luke', 'Sandra', 'Tom', 'Adam', 'Kristen', 'Stefan', 'Jake']
        self.location = None
        self.flight_number = 0

        try:
            kursori.execute(
                "INSERT INTO players (playerID, playerName, wins, losses, amountPlayed, winStreak, Highest_Win_Streak)SELECT COALESCE(MAX(playerID),0)+1,'" + self.username + "',0,0,0,0,0 FROM players;")
            print("Player created")
        except:
            print("Player exists")
            pass

    def setLocation(self, location):
        self.location = location

    def flyTo(self, maa):
        kursori.execute(
            "select countryID from gameCountries where gameCountries.name='" + str(self.location) + "';")
        locationID = kursori.fetchone()

        kursori.execute(
            "select name from flights, gameCountries where gameCountries.countryID=flights.joinID and flights.countryID='" + str(
                locationID[0]) + "';")
        flightOptions = kursori.fetchall()

        print(flightOptions)

        flightOptionsList = []
        for x in flightOptions:
            flightOptionsList.append(x[0])

        print(flightOptionsList)

        if maa in flightOptionsList:
            self.flight_number += 1
            self.location = maa

            kursori.execute(
                "select suspectName from gameCountries where name='" + str(self.location) + "';")
            locationSuspect = kursori.fetchone()

            if locationSuspect[0] != None:
                index = self.suspectIndex.index(locationSuspect[0])
                return index
            else:
                return 1
        else:
            return 0

        # for x in flightOptions:
        #     kursori.execute(
        #         "select suspectName from gameCountries where name='" + str(x[0]) + "';")
        #     optionSuspect = kursori.fetchone()
        #
        #     if optionSuspect[0] != None :
        #         person_country = ', jossa on ' + optionSuspect[0]
        #     else:
        #         person_country = ''
        #
        #     flight_number += 1
        #     print(f'({flight_number}): {x[0]}' + person_country)
        #
        # flight = int(input("Syötä numero: "))
        # self.location = flightOptions[flight-1][0]
        # print(self.location)
        #
        # kursori.execute(
        #     "select suspectName from gameCountries where name='" + str(self.location) + "';")
        # locationSuspect = kursori.fetchone()
        #
        # if locationSuspect[0]!=None:
        #     index = self.suspectIndex.index(locationSuspect[0])
        #     return index
        # else:
        #     return -1

    def welcomeText(self):
        kursori.execute("SELECT cityName from gameCountries where name='" + str(self.location) + "';")
        cityname = kursori.fetchone()
        city_name = cityname[0]

        kursori.execute("SELECT airportName from gameCountries where name='" + str(self.location) + "';")
        airportname = kursori.fetchone()
        airport_name = airportname[0]

        # weather data taken from openweathermap api with cityname
        apikey = '57d9761bd41e88656771c5c3745a9924'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={apikey}&units=metric'
        response = requests.get(url)
        data = json.loads(response.text)
        temp = data['main']['temp']

        # Welcome text:
        print(
            f'Tervetuloa {airport_name} nimiselle lentokentälle!\nOlet nyt kaupungissa {city_name}. Lämpötila on {temp} celsius astetta.')
        return (f'Tervetuloa {airport_name} nimiselle lentokentälle! Olet nyt kaupungissa {city_name}. Lämpötila on {temp} celsius astetta.')

    def win(self):
        kursori.execute("select winStreak, Highest_Win_Streak from players where playerName='" + str(self.username) + "';")
        streakTiedot = kursori.fetchone()

        if streakTiedot[0] == streakTiedot[1]:
            kursori.execute(
                "UPDATE players SET wins=wins+1, amountPlayed=amountPlayed+1, winStreak=winStreak+1, Highest_Win_Streak=Highest_Win_Streak+1 WHERE playerName='" + self.username + "';")
        else:
            kursori.execute(
                "UPDATE players SET wins=wins+1, amountPlayed=amountPlayed+1, winStreak=winStreak+1 WHERE playerName='" + self.username + "';")

    def lose(self):
        kursori.execute(
            "UPDATE players SET losses=losses+1, amountPlayed=amountPlayed+1, winStreak=0 WHERE playerName='" + self.username + "';")


