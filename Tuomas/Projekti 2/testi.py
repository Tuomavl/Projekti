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
@app.route('/newgame', methods=['GET','POST'])
def newgame():
    if request.method =='POST':
        print(request.get_json())
        return 'Ok'
    else:
        return json.dumps(game.find_airports())

if __name__ == '__main__':
    app.run(use_reloader=True)
