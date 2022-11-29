#SQL
import mysql.connector
import time
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='LeptuoMARIA2002',
         autocommit=True
         )
kursori=yhteys.cursor()

#Anna käyttäjänimi:
playerName = input("Anna käyttäjä nimesi: ")

kursori.execute("SELECT playerID FROM players WHERE playerName='"+playerName+"'")
tulos=kursori.fetchone()

try:
    kursori.execute("INSERT INTO players (playerID, playerName, wins, losses, amountPlayed, winStreak)SELECT COALESCE(MAX(playerID),0)+1,'"+playerName+"',0,0,0,0 FROM players;")
except:
    print(tulos[0])

nykMaa = 1
lennot = 7

winLoss = int(input('0 tai 1: '))

if winLoss == 0:
    kursori.execute("UPDATE players SET losses=losses+1, amountPlayed=amountPlayed+1, winStreak=0 WHERE playerName='"+playerName+"';")
else:
    kursori.execute("UPDATE players SET wins=wins+1, amountPlayed=amountPlayed+1, winStreak=winStreak+1 WHERE playerName='"+playerName+"';")
#Peli pyytää painamaan enteriä aloittaakseen pelin
valmis = input('Paina enter-näppäintä, kun olet valmis aloittamaan!')

#Jos pelaaja painaa jotain muuta kun enter, peli kysyy uudestaan. Jos painaa enter, tarina alkaa.
while valmis != '':
    valmis = input('Paina enter-näppäintä, kun olet valmis aloittamaan!')
else:
    print("Tervetuloa Puolan Varsovaan!")
    time.sleep(3)
    print(f"Olet rikostutkija {playerName}")
    time.sleep(3)
    print("Eilen myöhään yöllä Ilkka löydettiin murhattuna Varsovasta.")
    time.sleep(7)
    print("Sinun tehtäväsi on selvittää kuka murhasi Ilkan.")
    time.sleep(5)
    print(
        "Apulaisrikostutkija on kerännyt sinulle viisi epäiltyä, jotka ovat karanneet eri lentokentille ympäri Eurooppaa. ")
    time.sleep(8)
    print("Käy haastattelemassa heitä ja selvitä kuka on murhaaja")
    time.sleep(5)
    print(
        "mutta muista sinulla on vain 7 lentolippua eli voit lentää vain seitsemään eri kohteeseen, joten käytä ne harkiten.")
    time.sleep(9)
    print("Onnea matkaan!")
    time.sleep(2)
# Kun pelaaja painaa enter, peli alkaa:
    valmis = input("Paina enter-näppäintä, kun olet valmis aloittamaan!")
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
    #Tähän väliin henkilön keskustelu??

#Lentocounter
while lennot>0:
    matkustaminen()






