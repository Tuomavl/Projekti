import json
from flask import Flask,request
from flask_cors import CORS
from gameStarter import *

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# http://127.0.0.1:5000/newgame?player=playerName)
@app.route('/newgame')
def newgame():
    args = request.args
    player = args.get("player")
    json_data = game.player.location
    return json_data

if __name__ == '__main__':
    app.run(use_reloader=True)
