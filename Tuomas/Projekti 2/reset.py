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
from suspects import Suspect
from player1 import *
import random

Suspects = []
player = ()
person_dictionary = {}
def resetGame():
    kursori.execute(
        "UPDATE gameCountries SET suspectName = NULL WHERE suspectName is not null;")

    kursori.execute("SELECT name from suspects;")
    suspects = kursori.fetchall()
    suspectslist = []
    suspectslist.append(suspects)

    countries = ['Unkari', 'Kroatia', 'Itävalta', 'Tsekki', 'Saksa', 'Tanska', 'Alankomaat', 'Italia', 'Ranska',
                 'Puola',
                 'Ruotsi', 'Kreikka', 'Albania', 'Romania', 'Iso-Britannia']
    murderer = None

    global Player
    player = Player('ilkka')

    global person_dictionary
    person_dictionary = {}

    Mary = Suspect('Mary')
    Luke = Suspect('Luke')
    Sandra = Suspect('Sandra')
    Tom = Suspect('Tom')
    Adam = Suspect('Adam')
    Kristen = Suspect('Kristen')
    Stefan = Suspect('Stefan')
    Jake = Suspect('Jake')

    global Suspects
    Suspects = [Mary, Luke, Sandra, Tom, Adam, Kristen, Stefan, Jake]

    # Murderer is set
    murderer = random.choice(Suspects)
    murderer.set_murderer(True)

    # Suspect location randomized and set
    for i in Suspects:
        x = random.choice(countries)
        i.set_location(x)
        countries.remove(x)
        kursori.execute("UPDATE gameCountries SET suspectName='" + i.name + "' WHERE name= '" + i.location + "';")
        print(f'{i.name} on paikassa {i.location}')

        global playerLocation
        playerLocation = random.choice(countries)
        player.setLocation(playerLocation)

    print(f'\nMurhaaja on {murderer.name}')
    print(f'\nPelaaja on maassa {playerLocation}')

    # Suspect accusation randomiser
    while len(person_dictionary) < 8:
        randomized_person = random.choice(Suspects).name
        if randomized_person != murderer.name and randomized_person != Suspects[len(person_dictionary)].name:
            person_dictionary[Suspects[len(person_dictionary)]] = randomized_person
    print()