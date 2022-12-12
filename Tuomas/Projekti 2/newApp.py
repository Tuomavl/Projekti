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

from flask import Flask
from flask_cors import CORS
from game import Game
global startGameTracker


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


@app.route("/mapview")
def modal():
    suspects = game_olio.Suspects
    stories = []
    for i in suspects:
        stories.append(i.tellStory(i.name))
    return {"stories": stories}

@app.route("/getWelcomeText")
def getWelcomeText():
    welcomeText = game_olio.player.welcomeText()
    return {"welcomeText": welcomeText}

@app.route("/startGame")
def startGame():
    global game_olio
    game_olio = Game(player1)

    vastaus = {
        "player": game_olio.player.username,
        "res": "testi"
    }
    print(vastaus)
    return vastaus


@app.route("/murdererGuess/<murderer>")
def checkMurderer(murderer):
    global guess
    guess = murderer
    if game_olio.murderer.name == murderer:
        game_olio.player.win()
        return {"data": "win"}
    else:
        game_olio.player.lose()
        return {"data": "loss"}

@app.route("/getsuspect")
def getSuspect():
    return {"suspect": guess}

@app.route("/getmurderer")
def getMurderer():
    return {"murderer": game_olio.murderer.name}

@app.route("/getsuspectlist")
def getsuspectlist():
    vastaus = {
        "Mary":game_olio.suspectlocations["location"][0],
        "Luke":game_olio.suspectlocations["location"][1],
        "Sandra":game_olio.suspectlocations["location"][2],
        "Tom":game_olio.suspectlocations["location"][3],
        "Adam":game_olio.suspectlocations["location"][4],
        "Kristen":game_olio.suspectlocations["location"][5],
        "Stefan":game_olio.suspectlocations["location"][6],
        "Jake":game_olio.suspectlocations["location"][7]
    }
    return vastaus

@app.route("/getLeaderBoard")
def getLeaderBoard():
    kursori.execute("select * from players order by wins desc;")
    mostWins = kursori.fetchall()

    kursori.execute("select * from players order by amountPlayed desc;")
    mostPlayed = kursori.fetchall()

    kursori.execute("select * from players order by Highest_Win_Streak desc;")
    biggestWinstreak = kursori.fetchall()

    vastaus = {
        "mostWins": mostWins,
        "mostPlayed": mostPlayed,
        "biggestWinstreak": biggestWinstreak
    }
    return vastaus

@app.route("/flyTooo/<maa>")
def flyTooo(maa):
    value = game_olio.player.flyTo(maa)
    if value==10:
        print("Lensit maahan: " + maa)
        return {"value": 1}
    else:
        print("Et voinut lentää maahan: " + maa)
        return {"value": 0}


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)


