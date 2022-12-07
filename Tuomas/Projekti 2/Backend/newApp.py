from flask import Flask
import random
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
from player1 import Player

# Murderer is set
#random.choice(Suspects).set_murderer(True)

# Suspect location randomized and set
#playerLocation = random.choice(countries)

Suspects[7].accuse()

print('\n'+player.location)



value = player.flyTo()
if value == -1:
    print(f'Maassa {player.location} ei ole ketään.')
else:
    print(f'Maassa {player.location} on: {Suspects[value].name}')
    text = Suspects[value].accuse().format(playerName=player.username, addSuspect=person_dictionary[Suspects[value]])
    print(text)