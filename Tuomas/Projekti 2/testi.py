import json
import mysql.connector
from flask import Flask,render_template
from flask_cors import CORS

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='lentopeli',
    password='peli',
    autocommit=True
)
kursori = yhteys.cursor()
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/username')
def home():
    vastaus = {
        "playerName":
    }
    return vastaus

@app.route('/leaderboard.html', methods=['GET','POST'])
def leaderboard():

    return render_template('leaderboard.html')
@app.route('/Mapview.html',methods=['GET','POST'])
def game():
    return render_template('Mapview.html')

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
