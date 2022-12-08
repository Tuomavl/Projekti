import json
import mysql.connector
from flask import Flask,render_template

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

@app.route('/')
def game():
    return render_template('Mapview.html')

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
