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

nykMaa = 1
lennot = 10

playerName = input("Anna käyttäjä nimesi: ")

try:
    kursori.execute("INSERT INTO players (playerID, playerName, wins, losses, amountPlayed, winStreak)SELECT COALESCE(MAX(playerID),0)+1,'"+playerName+"',0,0,0,0 FROM players;")
except:
    print()

def matkustaminen():
    global nykMaa
    global lennot
    mones = 0
    kursori.execute("select name from flights, gameCountries where gameCountries.countryID=flights.joinID and flights.countryID='" + str(nykMaa) + "';")
    tulos = kursori.fetchall()
    print(f'\nSinulla on {lennot} lentoa jäljellä.')
    for x in tulos:
        mones+=1
        print(f'({mones}): {x[0]}')
    lentoValinta = int(input('\nValitse numeron perusteella mihin maahan haluat lentää: '))
    nykMaa = lentoValinta - 1
    kursori.execute("select countryID from gameCountries where name='" + str(tulos[nykMaa][0]) + "';")
    tulos = kursori.fetchone()
    nykMaa = tulos[0]
    lennot-=1
    kursori.execute("select airportName from gameCountries where countryID='" + str(nykMaa) + "';")
    tulos = kursori.fetchone()
    print(f'Tervetuloa, olet saapunut lentoasemalle: {tulos[0]}')

while lennot>0:
    matkustaminen()

arvaus = int(input('Kuka on murhaaja? '))

if arvaus == 0:
    kursori.execute("UPDATE players SET losses=losses+1, amountPlayed=amountPlayed+1, winStreak=0 WHERE playerName='"+playerName+"';")
    print('Väärin, hävisit pelin :(')
else:
    kursori.execute("UPDATE players SET wins=wins+1, amountPlayed=amountPlayed+1, winStreak=winStreak+1 WHERE playerName='"+playerName+"';")
    print('Oikein, voitit pelin :)')
