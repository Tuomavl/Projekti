import json
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

from flask import Flask, request
from flask_cors import CORS
from game import Game

global startGameTracker
startGameTracker = 0

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/kirjaudu/<player>")
def kirjaudu(player):
    global player1
    player1 = player

    vastaus = {
        "username": player1
    }
    return vastaus

@app.route("/tarina")
def tarina():
    print("Tarina " + player1)

    vastaus = {
        "username": player1
    }
    return vastaus

@app.route("/startGame")
def startGame():
    if startGameTracker > 0:
        global game_olio
        game_olio = Game(player1)
        game_olio.find_airports()


    startGameTracker += 1

    vastaus = {
        "player": game_olio,
        "res": game_olio.res
    }
    print(vastaus)
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)


