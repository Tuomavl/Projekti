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

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

