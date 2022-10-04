#Insert name
import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='LeptuoMARIA2002',
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
#Peli pyytää painamaan enteriä aloittaakseen pelin
valmis = input('Paina enter-näppäintä, kun olet valmis aloittamaan!')

#Jos pelaaja painaa jotain muuta kun enter, peli kysyy uudestaan
while valmis != '':
    valmis = input('Paina enter-näppäintä, kun olet valmis aloittamaan!')

#Kun pelaaja painaa enter, peli alkaa ja printtaa epäiltyjen henkilöiden sijainnit:
    if valmis == '':
        print()
#Lentojen määrä tällähetkellä
lennot = 7
while lennot != 0:
    lennot -=1
print(lennot)
#Anna sijainnin nimi:
Sijainti = input('Kirjoita seuraava paikka mihin haluat lentää:')





