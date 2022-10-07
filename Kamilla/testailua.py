#import:
import mysql.connector
import random
import time

#MySQL yhteys:
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='lentopeli',
         password='peli',
         autocommit=True
         )
kursori=yhteys.cursor()

#Käytettävien maiden lista:
maat = []
#Käytettävien henkilöiden lista:
henkilo = []
suspect = []
henkilot = {}
murhaaja = []


#Määritelmät
nykMaa = 0
lennot = 0
moni = 0
murhaaja_index = 0

playerName = ''

def gameLoop():
    resetGame()
    startGame()
    loppu = input('''
    (1): Pelaa uudelleen
    (2): Lopeta peli 
    ''')
    if loppu == "1":
        gameLoop()
    else:
        print('Kiitos, kun pelasit!')

def selectUser():
    global playerName
    playerName = input('Anna käyttäjänimesi: ')

    # Uusi käyttäjänimi lisätään tauluun, jos käyttäjänimi on sama, tämä ohitetaan:
    try:
        kursori.execute(
            "INSERT INTO players (playerID, playerName, wins, losses, amountPlayed, winStreak, Highest_Win_Streak)SELECT COALESCE(MAX(playerID),0)+1,'" + playerName + "',0,0,0,0,0 FROM players;")
    except:
        print()


def startGame():
    global moni
    #Tähän pelin nimi ja säännöt

    # Peli pyytää painamaan enteriä aloittaakseen pelin
    valmis = input('\nPaina enter-näppäintä, kun olet valmis aloittamaan!')

    # Jos pelaaja painaa jotain muuta kun enter, peli kysyy uudestaan. Jos pelaaja painaa enter, peli alkaa:
    while valmis != '':
        valmis = input('\nPaina enter-näppäintä, kun olet valmis aloittamaan!')

    # Alkutarina:
    dialogue('\nTervetuloa Puolan Varsovaan!')
    dialogue(f'Olet rikostutkija {playerName}')
    dialogue('Eilen myöhään yöllä Ilkka löydettiin murhattuna Varsovasta.')
    dialogue('Sinun tehtäväsi on selvittää kuka murhasi Ilkan.')
    dialogue('Apulaisrikostutkija on kerännyt sinulle viisi epäiltyä, jotka ovat karanneet eri lentokentille ympäri Eurooppaa. ')
    dialogue('Käy haastattelemassa heitä ja selvitä kuka on murhaaja')
    dialogue('mutta muista sinulla on vain 7 lentolippua eli pystyt lentämään vain seitsemään eri kohteeseen, joten käytä lentolippusi harkiten.')
    dialogue('Onnea matkaan!')

    # Tulostetaan lista epäiltyjen sijainneista
    dialogue(f'\nHenkilön nimi:{henkilo[suspect[0]]} ja maa:{maat[suspect[0]]}')
    dialogue(f'\nHenkilön nimi:{henkilo[suspect[1]]} ja maa:{maat[suspect[1]]}')
    dialogue(f'\nHenkilön nimi:{henkilo[suspect[2]]} ja maa:{maat[suspect[2]]}')
    dialogue(f'\nHenkilön nimi:{henkilo[suspect[3]]} ja maa:{maat[suspect[3]]}')
    dialogue(f'\nHenkilön nimi:{henkilo[suspect[4]]} ja maa:{maat[suspect[4]]}')

    # Peli kysyy uudelleen enter, edetäkseen:
    valmis = input('\nPaina enter-näppäintä, kun olet valmis aloittamaan!')
    while valmis != '':
        valmis = input("Paina enter-näppäintä, kun olet valmis aloittamaan pelin.")

    # Jos lentoja on jäljellä, voit jatkaa matkustamista:
    while lennot > 0:
        matkustaminen()

    # Tulostaa listan murhaajaehdokkaista:
    print(f"{murhaaja[murhaaja_index]}")
    for x in murhaaja:
        print(f'({moni + 1}): {x}')
        moni += 1

    # Peli kysyy murhaajaan viittaavaa numeroa:
    arvaus = int(input('Mikä on murhaajan numero? '))
    # Jos oikein = voitit, jos väärin = hävisit:
    if arvaus - 1 == murhaaja_index:
        kursori.execute("select winStreak, Highest_Win_Streak from players where playerName='" + str(playerName) + "';")
        streakTiedot = kursori.fetchone()

        if streakTiedot[0] == streakTiedot[1] or streakTiedot[0] == '0':
            kursori.execute(
                "UPDATE players SET wins=wins+1, amountPlayed=amountPlayed+1, winStreak=winStreak+1, Highest_Win_Streak=Highest_Win_Streak+1 WHERE playerName='" + playerName + "';")
        else:
            kursori.execute(
                "UPDATE players SET wins=wins+1, amountPlayed=amountPlayed+1, winStreak=winStreak+1 WHERE playerName='" + playerName + "';")
        print('Oikein, voitit pelin :)')
    else:
        kursori.execute(
            "UPDATE players SET losses=losses+1, amountPlayed=amountPlayed+1, winStreak=0 WHERE playerName='" + playerName + "';")
        print(f'Väärin, hävisit pelin :( Murhaaja oli: {murhaaja[murhaaja_index]}')

def resetGame():
    global maat
    maat = ['Unkari', 'Kroatia', 'Itävalta', 'Tsekki', 'Saksa', 'Tanska', 'Alankomaat', 'Italia', 'Ranska']
    random.shuffle(maat)

    global henkilo
    henkilo = ['Mary', 'Luke', 'Sandra', 'Tom', 'Adam']
    random.shuffle(henkilo)

    global suspect
    suspect = [0, 1, 2, 3, 4]
    random.shuffle(suspect)

    global henkilot
    henkilot = {}

    global nykMaa
    nykMaa = 1

    global lennot
    lennot = 7

    global moni
    moni = 0

    global murhaaja
    murhaaja = henkilo.copy()
    random.shuffle(murhaaja)

    global murhaaja_index
    murhaaja_index = murhaaja.index(henkilo[0])

    global maanumero
    maanumero = []

#Alkuteksti:
def dialogue(text):
    for i in text:
        print(i, end="")
        time.sleep(0.005)
    print()
    time.sleep(len(text) / 100)

#Matkustaminen:
def matkustaminen():
    global nykMaa
    global lennot
    mones = 0
    kursori.execute("select name from flights, gameCountries where gameCountries.countryID=flights.joinID and flights.countryID='" + str(nykMaa) + "';")
    tulos = kursori.fetchall()
    maanumero = []
    #Lentocounter
    dialogue(f'\nSinulla on {lennot} lentoa jäljellä.')
    for x in tulos:
        try:
            maaIndexHenkilo = maat.index(x[0])
        except:
            maaIndexHenkilo = 100
        if maaIndexHenkilo < 5:
            maaIndexHenkilo = ', jossa on ' + henkilo[maaIndexHenkilo]
        else:
            maaIndexHenkilo = ''
        mones += 1
        maanumero.append(mones)
        print(f'({mones}): {x[0]}' + maaIndexHenkilo)

    #Lentosuunnan valinta:
    try:
        lentoValinta = 23452345
        while lentoValinta not in maanumero:
            lentoValinta = int(input('\nValitse numeron perusteella mihin maahan haluat lentää: '))
    except:
        print('Yritä uudelleen')
        while lentoValinta not in maanumero:
            try:
                lentoValinta = int(input('\nValitse numeron perusteella mihin maahan haluat lentää: '))
            except:
                print('Yritä uudelleen')
    nykMaa = lentoValinta - 1
    kursori.execute("select countryID from gameCountries where name='" + str(tulos[nykMaa][0]) + "';")
    tulos = kursori.fetchone()
    nykMaa = tulos[0]
    lennot-=1
    kursori.execute("select airportName from gameCountries where countryID='" + str(nykMaa) + "';")
    tulos = kursori.fetchone()
    kursori.execute("select name from gameCountries where countryID='" + str(nykMaa) + "';")
    maa = kursori.fetchone()

    dialogue(f'\nTervetuloa, olet saapunut lentoasemalle: {tulos[0]}')

    # Henkilöiden tekstit ja epäilyt:
    if maa[0] != 'Puola' and maat.index(maa[0]) < 5 and henkilo[maat.index(maa[0])] in henkilot:
        print(
            f'\nTervetuloa! Nimeni on {henkilo[maat.index(maa[0])]}, mielestäni murhaaja ei ole {henkilot[henkilo[maat.index(maa[0])]]}')
        print(henkilot)
    elif maa[0] != 'Puola' and maat.index(maa[0]) < 5:
        moi = henkilo[random.randint(1, 4)]
        dialogue(f'\nTervetuloa! Nimeni on {henkilo[maat.index(maa[0])]}, mielestäni murhaaja ei ole {moi}')
        henkilot[henkilo[maat.index(maa[0])]] = moi
        print(henkilot)
    else:
        print('\nTämä on välipysäkkisi')

selectUser()
gameLoop()