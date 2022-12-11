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
from player import Player


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/kirjaudu/<player>")
def kirjaudu(player):
    global player1
    player1 = Player(player)
    print(player1)
    print(player1.username)

    vastaus = {
        "username": player1.username
    }
    return vastaus

@app.route("/tarina")
def tarina():
    print("Tarina "+player1.username)

    vastaus = {
        "username": player1.username
    }
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)


