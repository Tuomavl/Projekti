import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='lentopeli',
         password='peli',
         autocommit=True
         )
kursori=yhteys.cursor()


playerName = input("Anna käyttäjä nimesi: ")

kursori.execute("SELECT playerID FROM players WHERE playerName='"+playerName+"'")
tulos=kursori.fetchone()

try:
    kursori.execute("INSERT INTO players (playerID, playerName, wins, losses, amountPlayed, winStreak)SELECT COALESCE(MAX(playerID),0)+1,'"+playerName+"',0,0,0,0 FROM players;")
except:
    print(tulos[0])


winLoss = int(input('0 tai 1: '))

if winLoss == 0:
    kursori.execute("UPDATE players SET losses=losses+1, amountPlayed=amountPlayed+1, winStreak=0 WHERE playerName='"+playerName+"';")
else:
    kursori.execute("UPDATE players SET wins=wins+1, amountPlayed=amountPlayed+1, winStreak=winStreak+1 WHERE playerName='"+playerName+"';")



nykMaa = input('Nykyisen maan numero: ')

kursori.execute("select name from flights, gameCountries where gameCountries.countryID=flights.joinID and flights.countryID='"+nykMaa[0]+"';")
tulos=kursori.fetchall()

print(tulos[0][0],tulos[1][0])