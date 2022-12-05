
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
    def __init__(self, username, playerdata):
        self.username = username
        self.playerdata = playerdata
        self.suspectIndex = ['Mary', 'Luke', 'Sandra', 'Tom', 'Adam', 'Kristen', 'Stefan', 'Jake']

    def flyTo(self):
        flight_number = 0

        kursori.execute(
            "select countryID from gameCountries where gameCountries.name='" + str(playerLocation) + "';")
        locationID = kursori.fetchone()

        kursori.execute(
            "select name from flights, gameCountries where gameCountries.countryID=flights.joinID and flights.countryID='" + str(
                locationID[0]) + "';")
        flightOptions = kursori.fetchall()

        for x in flightOptions:
            kursori.execute(
                "select suspectName from gameCountries where name='" + str(x[0]) + "';")
            optionSuspect = kursori.fetchone()

            if optionSuspect[0] != None :
                person_country = ', jossa on ' + optionSuspect[0]
            else:
                person_country = ''

            flight_number += 1
            print(f'({flight_number}): {x[0]}' + person_country)

        kursori.execute(
            "select suspectName from gameCountries where name='" + str(playerLocation) + "';")
        locationSuspect = kursori.fetchone()

        if locationSuspect[0]!=None:
            index = self.suspectIndex.index(locationSuspect[0])

            print(f'Maassa {playerLocation} on: {locationSuspect[0]}')
            Suspects[index].accuse()
        else:
            print(f'Maassa {playerLocation} ei ole ketään. {locationSuspect[0]}')
