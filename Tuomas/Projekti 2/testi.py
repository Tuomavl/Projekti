import json
from flask import Flask,request
from flask_cors import CORS
from game import Game

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
game = Game()
ok = game.find_airports()

# http://127.0.0.1:5000/newgame?player=playerName)
@app.route('/newgame/<playerName>/<loc>')
def newgame(playerName,loc):
   Player = playerName
   location =loc

   vastaus = {
       "username":Player,
       "location":location
   }
   return vastaus
if __name__ == '__main__':
    app.run(use_reloader=True)
