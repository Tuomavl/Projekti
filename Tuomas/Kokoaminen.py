#SQL
import mysql.connector
import time
import random
maat = ['Unkari','Kroatia','Itävalta','Tsekki','Saksa','Tanska','Alankomaat','Italia','Ranska']
henkilo = ['Mary','Luke','Sandra','Tom','Adam']
random.shuffle(maat)
print(f'Epäillyistä henkilöistä ensimmäinen on nimeltään: {henkilo[0]}. Hän on lähtenyt tapahtuman jälkeen maahan nimeltä: {maat[0]}')
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
    import time
    def dialogue(text):
        for i in text:
            print(i, end="")
            time.sleep(0.05)
        print()
        time.sleep(len(text) / 20)

    dialogue("Tervetuloa Puolan Varsovaan!")
    dialogue(f"Olet rikostutkija {playerName}")
    dialogue("Eilen myöhään yöllä Ilkka löydettiin murhattuna Varsovasta.")
    dialogue("Sinun tehtäväsi on selvittää kuka murhasi Ilkan.")
    dialogue(
        "Apulaisrikostutkija on kerännyt sinulle viisi epäiltyä, jotka ovat karanneet eri lentokentille ympäri Eurooppaa. ")
    dialogue("Käy haastattelemassa heitä ja selvitä kuka on murhaaja")
    dialogue(
        "mutta muista sinulla on vain 7 lentolippua eli pystyt lentämään vain seitsemään eri kohteeseen, joten käytä lentolippusi harkiten.")
    dialogue("Onnea matkaan!")
    valmis = input("Paina enter-näppäintä, kun olet valmis aloittamaan pelin.")

#Matkustaminen
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

arvaus = int(input('Kuka on murhaaja? '))

if arvaus == 0:
    kursori.execute("UPDATE players SET losses=losses+1, amountPlayed=amountPlayed+1, winStreak=0 WHERE playerName='"+playerName+"';")
    print('Väärin, hävisit pelin :(')
else:
    kursori.execute("UPDATE players SET wins=wins+1, amountPlayed=amountPlayed+1, winStreak=winStreak+1 WHERE playerName='"+playerName+"';")
    print('Oikein, voitit pelin :)')