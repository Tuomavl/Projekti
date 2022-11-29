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

suspects = []
kursori.execute("SELECT name from suspects;")
name = kursori.fetchall()

print(name)