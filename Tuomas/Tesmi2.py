#Insert name
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
else:
    print("Tervetuloa Puolan Varsovaan!")
    time.sleep(3)
    print("Olet rikostutkija {syötetty käyttäjänimi mahdollisesti?}")
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






