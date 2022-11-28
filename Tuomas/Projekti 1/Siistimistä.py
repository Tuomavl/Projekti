# import
import mysql.connector
import random
import time
from PIL import Image

# MySQL yhteys:
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='lentopeli',
    password='peli',
    autocommit=True
)
kursori = yhteys.cursor()

# Käytettävien maiden lista:
countries = []
# Käytettävien henkilöiden lista:
person = []
suspect = []
person_dictionary = {}
stories = {}
visited = {}
murderer = []

# Määritelmät
location = 0
flights = 0
murderer_order = 0
murderer_index = 0
playerName = ''

firstTime = True


def gameLoop():
    resetGame()
    startGame()
    leaderboard()
    ending = input('''
    (1): Pelaa uudelleen
    (2): Lopeta peli 
    ''')
    if ending == "1":
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
    global murderer_order
    # Tähän pelin nimi ja säännöt
    dialogue('Family Friendly Murhamysteeri!')

    # Peli pyytää painamaan enteriä aloittaakseen pelin
    ready = input('\nPaina enter-näppäintä, kun olet valmis aloittamaan!')

    # Jos pelaaja painaa jotain muuta kun enter, peli kysyy uudestaan. Jos pelaaja painaa enter, peli alkaa:
    while ready != '':
        ready = input('\nPaina enter-näppäintä, kun olet valmis aloittamaan!')

    global firstTime
    if firstTime:
        intro()
        picture()
        firstTime = False

    # Tulostetaan lista epäiltyjen sijainneista
    dialogue(f'\nHenkilö {person[suspect[0]]} on maassa {countries[suspect[0]]}')
    dialogue(f'Henkilö {person[suspect[1]]} on maassa {countries[suspect[1]]}')
    dialogue(f'Henkilö {person[suspect[2]]} on maassa {countries[suspect[2]]}')
    dialogue(f'Henkilö {person[suspect[3]]} on maassa {countries[suspect[3]]}')
    dialogue(f'Henkilö {person[suspect[4]]} on maassa {countries[suspect[4]]}')

    # Peli kysyy uudelleen enter, edetäkseen:
    ready = input('\nPaina enter-näppäintä, kun olet valmis aloittamaan!')
    while ready != '':
        ready = input("Paina enter-näppäintä, kun olet valmis aloittamaan pelin.")

    # Jos lentoja on jäljellä, voit jatkaa matkustamista:
    while flights > 0:
        travelling()

    print('\n')

    dialogue(
        'Olet nyt käyttänyt kaikki lentolippusi ja nyt on aika kerätä saamasi tiedot yhteen ja selvittää kuka on murhaaja!\n')
    # Tulostaa listan kyselyistä:
    for x in visited:
        dialogue(f'{x}: Mielestäni murhaaja ei ole {visited[x]}')

    print('\n')

    # Tulostaa listan murhaajaehdokkaista:

    for x in murderer:
        print(f'({murderer_order + 1}): {x}')
        murderer_order += 1

    # Peli kysyy murhaajaan viittaavaa numeroa:
    guess = input('\nMikä on murhaajan numero? ')
    while guess not in ['1', '2', '3', '4', '5']:
        print('Ei hyväksytty.')
        guess = input('\nMikä on murhaajan numero? ')

    # Jos oikein = voitit, jos väärin = hävisit:
    if guess == str(murderer_index + 1):
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
        print(f'Väärin, hävisit pelin :( Murhaaja oli: {murderer[murderer_index]}')


def resetGame():
    global countries
    countries = ['Unkari', 'Kroatia', 'Itävalta', 'Tsekki', 'Saksa', 'Tanska', 'Alankomaat', 'Italia', 'Ranska']
    random.shuffle(countries)

    global person
    person = ['Mary', 'Luke', 'Sandra', 'Tom', 'Adam']
    random.shuffle(person)

    global suspect
    suspect = [0, 1, 2, 3, 4]
    random.shuffle(suspect)

    global person_dictionary
    person_dictionary = {}

    randomized_person = person[random.choice([1, 2, 3, 4])]
    person_dictionary[person[0]] = randomized_person

    randomized_person = person[random.choice([2, 3, 4])]
    person_dictionary[person[1]] = randomized_person

    randomized_person = person[random.choice([1, 3, 4])]
    person_dictionary[person[2]] = randomized_person

    randomized_person = person[random.choice([1, 2, 4])]
    person_dictionary[person[3]] = randomized_person

    randomized_person = person[random.choice([1, 2, 3])]
    person_dictionary[person[4]] = randomized_person

    global stories
    stories = {
        'Mary': f'Mary: He-he-hei ri-rikos-rikostutkija {playerName}. A-ai tu-tulit haas-haastattelemaan mi-mi-minua. \nA-ai mi-mi-mi-miksi pa-pakenin? No tuo-tuota mi-minä va-vain pe-peläs-tyin. Mu-mutta se en o-le oikeasti minä! Mi-minä lupaan! \nUskoi-sit mi-minua! Mu-mutta näi-in, että {person_dictionary["Mary"]} me-meni vessaan, joten en usko, että hän on murhaaja. Kiva, jos pystyin olla avuksi!',
        'Luke': f'Luke: Minulla olisi tässä nyt kiire en millään ehtisi... jaahas epäillään murhasta vai? No en se minä ollut. \nEnkä tiedä kuka se oli. Voisinko nyt mennä? Ei minulla ole mitään kerrottavaa! \nPaitsi että... no tuota näin, kun {person_dictionary["Luke"]} lähti aikaisemmalla lennolla, joten se on tuskin hän. Nyt minun on kuitenkin pakko mennä näkemiin.',
        'Sandra': f'Sandra: Ai hei rikostutkija... {playerName}. Teilläpä on ihana nimi. Ai tulitte haastattelemaan minua. Sepä kovin mukavaa. \nJatkettaisiinko haastattelua jossain mukavammassa paikassa. Ai sinulla on kiire? \nNo kyllä me kerkeäisimme nope- selvä selvä pysytään asiassa, vaikka se onkin vaikeaa, kun katselee noita silmiäsi. \nNäinkö jotain epäilyttävää? En. En sitten mitään. Toki, jos haluaisit jatkaa juttelemista minun hotellillani- \nAi jaaha selvä no {person_dictionary["Sandra"]} se ei ole, koska minä olin hänen kanssaan. Eikö rikostutkijalla olisi edes pieni hetki aikaa- aha no heippa sitten. Nähdään taas pian!',
        'Tom': f'Tom: No terve. Tietenkään minä en ole murhaaja eikä ole myöskään {person_dictionary["Tom"]}. \nAi mistä tiedän? Koska tiedän vain. Häivyhän siitä sitten jo.',
        'Adam': f'Adam: Terveppä terve! Murhatutkimuksen tiimoilta tullut minua tapaamaan? Hahah. Naurettava ajatus, että minua edes epäillään. \nMutta kuulepas tätä. Näin, että {person_dictionary["Adam"]} hiippaili hotellihuoneeseen jonkun tuntemattoman kanssa! \nMehukas juoru, mutta samalla taitaa todistaa, ettei hän voi olla murhaaja.'}

    global visited
    visited = {}

    global location
    location = 1

    global flights
    flights = 7

    global murderer_order
    murderer_order = 0

    global murderer
    murderer = person.copy()
    random.shuffle(murderer)

    global murderer_index
    murderer_index = murderer.index(person[0])

    global country_number
    country_number = []


def intro():
    dialogue('\nTervetuloa Puolan Varsovaan!')
    dialogue(f'Olet rikostutkija {playerName}')
    dialogue('Eilen myöhään yöllä Ilkka löydettiin murhattuna Varsovasta.')
    dialogue('Sinun tehtäväsi on selvittää kuka murhasi Ilkan.')
    dialogue(
        'Apulaisrikostutkija on kerännyt sinulle viisi epäiltyä, jotka ovat karanneet eri maihin ympäri Eurooppaa. ')
    dialogue('Käy haastattelemassa heitä ja selvitä kuka on murhaaja')
    dialogue(
        'mutta muista sinulla on vain 7 lentolippua eli pystyt lentämään vain seitsemään eri kohteeseen, joten käytä lentolippusi harkiten.')
    dialogue('Onnea matkaan!')


# Kuva Kartasta:
def picture():
    picture = Image.open("Näyttökuva 2022-10-6 kello 22.29.23.png")
    picture.show()


def dialogue(text):
    for i in text:
        print(i, end="")
        time.sleep(0.001)
    print()
    time.sleep(len(text) / 1000)


# Leaderboard:
def leaderboard():
    print('\nLeaderboard:')
    kursori.execute(
        "select PlayerName, Highest_Win_Streak from players where Highest_win_Streak !=0 order by Highest_Win_Streak desc limit 0, 10;")
    leaderboard = kursori.fetchall()
    instance = 0
    for x in leaderboard:
        nameLenght = len(leaderboard[instance][0])
        print(f'| Nimi: {leaderboard[instance][0]}' + ' ' * (
                    20 - nameLenght) + f'| Korkein streak: {leaderboard[instance][1]} |')
        instance += 1


# Matkustaminen:
def travelling():
    global location
    global flights
    flight_number = 0
    kursori.execute(
        "select name from flights, gameCountries where gameCountries.countryID=flights.joinID and flights.countryID='" + str(
            location) + "';")
    result = kursori.fetchall()
    country_number = []
    # Lentocounter
    dialogue(f'\nSinulla on {flights} lentoa jäljellä.')
    for x in result:
        try:
            person_country = countries.index(x[0])
        except:
            person_country = 100
        if person_country < 5:
            person_country = ', jossa on ' + person[person_country]
        else:
            person_country = ''
        flight_number += 1
        country_number.append(flight_number)
        print(f'({flight_number}): {x[0]}' + person_country)

    # Lentosuunnan valinta:
    try:
        flight_option = 2343478675
        while flight_option not in country_number:
            flight_option = int(input('Valitse numeron perusteella mihin maahan haluat lentää: '))
    except:
        while flight_option not in country_number:
            try:
                flight_option = int(input('Valitse numeron perusteella mihin maahan haluat lentää: '))
            except:
                print()
    location = flight_option - 1
    kursori.execute("select countryID from gameCountries where name='" + str(result[location][0]) + "';")
    result = kursori.fetchone()
    location = result[0]
    flights -= 1
    kursori.execute("select airportName from gameCountries where countryID='" + str(location) + "';")
    result = kursori.fetchone()
    kursori.execute("select name from gameCountries where countryID='" + str(location) + "';")
    country = kursori.fetchone()

    dialogue(f'\nTervetuloa, olet saapunut lentoasemalle: {result[0]}')

    if country[0] != 'Puola' and countries.index(country[0]) < 5:
        dialogue(f'{stories[person[countries.index(country[0])]]}')
        visited[person[countries.index(country[0])]] = person_dictionary[person[countries.index(country[0])]]

    else:
        dialogue('\nTämä on välipysäkkisi')


selectUser()
gameLoop()
