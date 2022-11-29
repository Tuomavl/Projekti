import mysql.connector
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='LeptuoMARIA2002',
    autocommit=True
)
kursori = yhteys.cursor()

playername = input('Give me a name:')
kursori.execute("SELECT story from suspects where name='Luke'")
result = kursori.fetchone()
txt = result[0]
print(txt.format(playerName = playername))
