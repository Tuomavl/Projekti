#The necessary imports
from suspects import Suspect
from player import Player
import random

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

#Game object
class Game:
    def __init__(self, playerName):
        #The necessary lists and dictionaries
        self.suspectlocations = {"name": [], "location": []}
        self.Suspects = []
        self.player = ()
        self.person_dictionary = {}
        self.suspectslist = []
        self.person_dictionary = {}
        self.countries = ['Unkari', 'Kroatia', 'Itävalta', 'Tsekki', 'Saksa', 'Tanska', 'Alankomaat', 'Italia', 'Ranska',
                     'Puola',
                     'Ruotsi', 'Kreikka', 'Albania', 'Romania', 'Iso-Britannia']

        self.murderer = None

        self.player = Player(playerName)

        kursori.execute(
            "UPDATE gameCountries SET suspectName = NULL WHERE suspectName is not null;")

        kursori.execute("SELECT name from suspects;")
        self.suspects = kursori.fetchall()

        self.suspectslist.append(self.suspects)

        self.Mary = Suspect('Mary')
        self.Luke = Suspect('Luke')
        self.Sandra = Suspect('Sandra')
        self.Tom = Suspect('Tom')
        self.Adam = Suspect('Adam')
        self.Kristen = Suspect('Kristen')
        self.Stefan = Suspect('Stefan')
        self.Jake = Suspect('Jake')

        self.Suspects = [self.Mary, self.Luke, self.Sandra, self.Tom, self.Adam,
                         self.Kristen, self.Stefan, self.Jake]

        # Murderer is set
        self.murderer = random.choice(self.Suspects)
        self.murderer.set_murderer(True)

        # Suspect location randomized and set
        for i in self.Suspects:
            x = random.choice(self.countries)
            i.set_location(x)
            self.countries.remove(x)
            kursori.execute("UPDATE gameCountries SET suspectName='" + i.name + "' WHERE name= '" + i.location + "';")
            self.suspectlocations["name"].append(i.name)
            self.suspectlocations["location"].append(i.location)
            print(self.suspectlocations["name"][0])

            print(f'{i.name} on paikassa {i.location}')

            self.playerLocation = random.choice(self.countries)
            self.player.setLocation(self.playerLocation)

            self.player.getLocationID()

        # Suspect accusation randomiser
        while len(self.person_dictionary) < 8:
            randomized_person = random.choice(self.Suspects).name
            if randomized_person != self.murderer.name and randomized_person != self.Suspects[len(self.person_dictionary)].name:
                self.person_dictionary[self.Suspects[len(self.person_dictionary)]] = randomized_person

        print(f'\nMurhaaja on {self.murderer.name}')
        print(f'Pelaaja on maassa {self.playerLocation}')

    def find_airports(self):
        kursori.execute("SELECT lat,lon from gameCountries")
        self.res = kursori.fetchall()
        print(self.res)
