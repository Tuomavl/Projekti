import json
from reset import resetGame
import mysql.connector
from flask import Flask, request
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

resetGame()


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
