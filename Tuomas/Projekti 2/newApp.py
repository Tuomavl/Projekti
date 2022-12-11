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

@app.route('/',methods =['GET','POST'])
def resetGame():
    args = request.args

    return

@app.route('/leaderboard')
def leaderboard():
    leaderboards = ['Kameli', 'Poro', 'Hirvi', 'Kauris']
    json_data = json.dumps(leaderboards)
    return json_data

def toinen_funktio(loc):
    tulos = loc + "Meow"
    print(tulos)
    return tulos

@app.route("/newgame/<player>/<loc>")
def newgame(player, loc):
    player = f"{player}666"
    location = toinen_funktio(loc)

    vastaus = {
        "username": player,
        "location": location
    }
    return vastaus

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


