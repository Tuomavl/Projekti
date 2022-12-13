#The neccessary imports
import json
import requests

#Mysql connector
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

#Player object
class Player:
    def __init__(self, username):
        self.username = username
        self.suspectIndex = ['Mary', 'Luke', 'Sandra', 'Tom', 'Adam', 'Kristen', 'Stefan', 'Jake']
        self.location = None
        self.flight_number = 0

        #Attempts to create a user with the players username
        try:
            kursori.execute(
                "INSERT INTO players (playerID, playerName, wins, losses, amountPlayed, winStreak, Highest_Win_Streak)"
                "SELECT COALESCE(MAX(playerID),0)+1,'" + self.username + "',0,0,0,0,0 FROM players;")
        except:
            pass

    #Sets the location of the player
    def setLocation(self, location):
        self.location = location

    #Gets the current countries ID from the database
    def getLocationID(self):
        kursori.execute(
            "select countryID from gameCountries where gameCountries.name='" + str(self.location) + "';")
        self.locationID = kursori.fetchone()

    #Attempts to fly to the inputted country, and returns the result
    def flyTo(self, maa):
        kursori.execute(
            "select countryID from gameCountries where gameCountries.name='" + str(self.location) + "';")
        self.locationID = kursori.fetchone()

        kursori.execute(
            "select name from flights, gameCountries where gameCountries.countryID=flights.joinID and flights.countryID='" + str(
                self.locationID[0]) + "';")
        flightOptions = kursori.fetchall()

        flightOptionsList = []
        for x in flightOptions:
            flightOptionsList.append(x[0])

        print(flightOptionsList)

        if maa in flightOptionsList:
            self.flight_number += 1
            self.location = maa

            kursori.execute(
                "select suspectName from gameCountries where name='" + str(self.location) + "';")
            self.locationSuspect = kursori.fetchone()

            if self.locationSuspect[0] != None:
                index = self.suspectIndex.index(self.locationSuspect[0])
                return index
            else:
                return 1
        else:
            return 0

    #Returns the welcome text
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
        return (f'Tervetuloa {airport_name} nimiselle lentokentälle! Olet nyt kaupungissa {city_name}. Lämpötila on {temp} celsius astetta.')

    # Updates the information in the database
    def win(self):
        kursori.execute("select winStreak, Highest_Win_Streak from players where playerName='" + str(self.username) + "';")
        streakTiedot = kursori.fetchone()

        if streakTiedot[0] == streakTiedot[1]:
            kursori.execute(
                "UPDATE players SET wins=wins+1, amountPlayed=amountPlayed+1, winStreak=winStreak+1, Highest_Win_Streak=Highest_Win_Streak+1 WHERE playerName='" + self.username + "';")
        else:
            kursori.execute(
                "UPDATE players SET wins=wins+1, amountPlayed=amountPlayed+1, winStreak=winStreak+1 WHERE playerName='" + self.username + "';")

    #Updates the information in the database
    def lose(self):
        kursori.execute(
            "UPDATE players SET losses=losses+1, amountPlayed=amountPlayed+1, winStreak=0 WHERE playerName='" + self.username + "';")
