import json
import mysql.connector
from flask import Flask,request,render_template
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
@app.route('/')
def index():
    return render_template('Kirjaudu.html')
@app.route('/test', methods=['GET','POST'])



if __name__ == '__main__':
    app.run(use_reloader=True)
