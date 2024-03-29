#import:
import mysql.connector
import random
import time
from PIL import Image

#Käytettävien maiden lista:
maat = ['Unkari','Kroatia','Itävalta','Tsekki','Saksa','Tanska','Alankomaat','Italia','Ranska']


#Käytettävien henkilöiden lista:
henkilo = ['Mary','Luke','Sandra','Tom','Adam']


#Epäiltyjen randomisointi
suspect = [0, 1, 2, 3, 4]
random.shuffle(suspect)


#sanakirja henkilöiden tiedoista:
henkilot = {}


#Määritelmät
nykMaa = 1
lennot = 7
moni = 0


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


#Anna käyttäjänimi:
playerName = input('Anna käyttäjänimesi: ')


#Uusi käyttäjänimi lisätään tauluun, jos käyttäjänimi on sama tämä ohitetaan:
try:
    kursori.execute("INSERT INTO players (playerID, playerName, wins, losses, amountPlayed, winStreak)SELECT COALESCE(MAX(playerID),0)+1,'"+playerName+"',0,0,0,0 FROM players;")
except:
    print()


#Alkuteksti:
def dialogue(text):
    for i in text:
        print(i, end='')
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
    kursori.execute("select name from gameCountries where countryID='" + str(nykMaa) + "';")
    maa = kursori.fetchone()


#Henkilöiden tekstit ja epäilyt:
    if maa[0] !='Puola' and maat.index(maa[0])<5 and henkilo[maat.index(maa[0])] in henkilot:
        print(f'\nTervetuloa! Nimeni on {henkilo[maat.index(maa[0])]}, mielestäni murhaaja ei ole {henkilot[henkilo[maat.index(maa[0])]]}')
        print(henkilot)
    elif maa[0] !='Puola' and maat.index(maa[0])<5:
        moi = henkilo[random.randint(1, 4)]
        dialogue(f'Tervetuloa! Nimeni on {henkilo[maat.index(maa[0])]}, mielestäni murhaaja ei ole {moi}')
        henkilot[henkilo[maat.index(maa[0])]] = moi
        print(henkilot)

    dialogue(f'\nSinulla on {lennot} lentoa jäljellä.')
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
    dialogue(f'\nTervetuloa, olet saapunut lentoasemalle: {tulos[0]}')



#Peli pyytää painamaan enteriä aloittaakseen pelin
valmis = input('Paina enter-näppäintä, kun olet valmis aloittamaan!')


#Jokaisen pelin alussa (Lennot on 7) randomisoidaan molemmat listat:
if lennot == 7:
    random.shuffle(maat)
    random.shuffle(henkilo)


#Murhaajakyselyn lista randomisoituna:
murhaaja = henkilo.copy()
random.shuffle(murhaaja)
murhaaja_index = murhaaja.index(henkilo[0])


#Jos pelaaja painaa jotain muuta kun enter, peli kysyy uudestaan. Jos pelaaja painaa enter, peli alkaa:
while valmis != '':
    valmis = input('Paina enter-näppäintä, kun olet valmis aloittamaan!')


#Alkutarina:
dialogue('\nTervetuloa Puolan Varsovaan!')
dialogue(f'Olet rikostutkija {playerName}')
dialogue('Eilen myöhään yöllä Ilkka löydettiin murhattuna Varsovasta.')
dialogue('Sinun tehtäväsi on selvittää kuka murhasi Ilkan.')
dialogue('Apulaisrikostutkija on kerännyt sinulle viisi epäiltyä, jotka ovat karanneet eri lentokentille ympäri Eurooppaa. ')
dialogue('Käy haastattelemassa heitä ja selvitä kuka on murhaaja')
dialogue('mutta muista sinulla on vain 7 lentolippua eli pystyt lentämään vain seitsemään eri kohteeseen, joten käytä lentolippusi harkiten.')
dialogue('Onnea matkaan!')


#Tulostetaan lista epäiltyjen sijainneista
dialogue(f'\nHenkilön nimi:{henkilo[suspect[0]]} ja maa:{maat[suspect[0]]}')
dialogue(f'Henkilön nimi:{henkilo[suspect[1]]} ja maa:{maat[suspect[1]]}')
dialogue(f'Henkilön nimi:{henkilo[suspect[2]]} ja maa:{maat[suspect[2]]}')
dialogue(f'Henkilön nimi:{henkilo[suspect[3]]} ja maa:{maat[suspect[3]]}')
dialogue(f'Henkilön nimi:{henkilo[suspect[4]]} ja maa:{maat[suspect[4]]}')

testi = Image.open("Näyttökuva 2022-10-6 kello 22.29.23.png")
testi.show()

#Peli kysyy uudelleen enter, edetäkseen:
while valmis != '':
    valmis = input('Paina enter-näppäintä, kun olet valmis aloittamaan pelin.')


#Jos lentoja on jäljellä, voit jatkaa matkustamista:
while lennot>0:
    matkustaminen()

#pitäskö tähä välii joku tämä on viimeinen lentokenttäsi, arvaa nyt murhaaja tmv?

#Tulostaa listan murhaajaehdokkaista:
print(f'{murhaaja[murhaaja_index]}')
for x in murhaaja:
    print(f'({moni + 1}): {x}')
    moni += 1


#Peli kysyy murhaajaan viittaavaa numeroa:
arvaus = input('\nMikä on murhaajan numero? ')


#Jos oikein = voitit, jos väärin = hävisit:

while arvaus not in ['1', '2', '3', '4', '5']:
    print('Ei hyväksytty.')
    arvaus = input('\nMikä on murhaajan numero? ')
if arvaus == str(murhaaja_index+1):
    kursori.execute("UPDATE players SET wins=wins+1, amountPlayed=amountPlayed+1, winStreak=winStreak+1 WHERE playerName='"+playerName+"';")
    print('\nOikein, voitit pelin :)')
else:
    kursori.execute("UPDATE players SET losses=losses+1, amountPlayed=amountPlayed+1, winStreak=0 WHERE playerName='"+playerName+"';")
    print('\nVäärin, hävisit pelin :(')
