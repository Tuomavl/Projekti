import mysql.connector
import random

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='lentopeli',
    password='peli',
    autocommit=True
)
kursori = yhteys.cursor()

# Import suspects names from database and save them in suspects variable
kursori.execute("SELECT name from suspects;")
suspects = kursori.fetchall()
suspectslist = []
suspectslist.append(suspects)

countries = ['Unkari', 'Kroatia', 'Itävalta', 'Tsekki', 'Saksa', 'Tanska', 'Alankomaat', 'Italia', 'Ranska', 'Puola',
             'Ruotsi', 'Kreikka', 'Albania', 'Romania', 'Iso-Britannia']

person_dictionary = {}


#print(suspects)
#print(suspects[6][0])

#kursori.execute("SELECT countryID from gameCountries;")
#countries = kursori.fetchall()
#countrieslist = []
#countrieslist.append(countries)
#print(countrieslist)


class Suspect:
    def __init__(self, name):
        self.name = name
        self.location = ''
        self.murderer = False

        kursori.execute("UPDATE suspects SET status=0 WHERE name= '" + self.name + "';")


    def set_location(self, location):
        self.location = location
        kursori.execute("UPDATE gameCountries SET suspectName='" + self.name + "' WHERE name= '" + self.location + "';")

# Defining who of the suspects is a murderer
    def set_murderer(self, murderer):
        self.murderer = murderer
        kursori.execute("UPDATE suspects SET status=1 WHERE name= '" + self.name + "';")

        global murdererName
        murdererName=self.name

# Suspects tell their story
    def tellStory(self,name):
        kursori.execute("SELECT story from suspects where name= '" + name + "';")
        story = kursori.fetchone()
        print(story)

    def accuse(self):
        selfIndex = Suspects.index(self)
        kursori.execute("SELECT story from suspects where name='" + Suspects[selfIndex].name + "';")
        result = kursori.fetchone()
        #print(result[0],Suspects[0])

        # playerName and suspect name is added to suspects story
        print(result[0].format(playerName=player.username, addSuspect=person_dictionary[Suspects[selfIndex]]))

class Player:
    def __init__(self, username, playerdata):
        self.username = username
        self.playerdata = playerdata
        self.suspectIndex = ['Mary', 'Luke', 'Sandra', 'Tom', 'Adam', 'Kristen', 'Stefan', 'Jake']

    def flyTo(self):
        flight_number = 0

        kursori.execute(
            "select countryID from gameCountries where gameCountries.name='" + str(playerLocation) + "';")
        locationID = kursori.fetchone()

        kursori.execute(
            "select name from flights, gameCountries where gameCountries.countryID=flights.joinID and flights.countryID='" + str(
                locationID[0]) + "';")
        flightOptions = kursori.fetchall()

        for x in flightOptions:
            kursori.execute(
                "select suspectName from gameCountries where name='" + str(x[0]) + "';")
            optionSuspect = kursori.fetchone()

            if optionSuspect[0] != None :
                person_country = ', jossa on ' + optionSuspect[0]
            else:
                person_country = ''

            flight_number += 1
            print(f'({flight_number}): {x[0]}' + person_country)

        kursori.execute(
            "select suspectName from gameCountries where name='" + str(playerLocation) + "';")
        locationSuspect = kursori.fetchone()

        if locationSuspect[0]!=None:
            index = self.suspectIndex.index(locationSuspect[0])

            print(f'Maassa {playerLocation} on: {locationSuspect[0]}')
            Suspects[index].accuse()
        else:
            print(f'Maassa {playerLocation} ei ole ketään. {locationSuspect[0]}')




player = Player('Ilkka', 0)

def resetGame():
    kursori.execute(
        "UPDATE gameCountries SET suspectName = NULL WHERE suspectName is not null;")

    Mary = Suspect('Mary')
    Luke = Suspect('Luke')
    Sandra = Suspect('Sandra')
    Tom = Suspect('Tom')
    Adam = Suspect('Adam')
    Kristen = Suspect('Kristen')
    Stefan = Suspect('Stefan')
    Jake = Suspect('Jake')

    global Suspects
    Suspects = [Mary, Luke, Sandra, Tom, Adam, Kristen, Stefan, Jake]

    # Murderer is set
    random.choice(Suspects).set_murderer(True)

    # Suspect location randomized and set
    for i in Suspects:
        x = random.choice(countries)
        i.set_location(x)
        countries.remove(x)
        kursori.execute("UPDATE gameCountries SET suspectName='" + i.name + "' WHERE name= '" + i.location + "';")
        print(f'{i.name} on paikassa {i.location}')

    # Player location randomized
    global playerLocation
    playerLocation = random.choice(countries)

    print(f'\nMurhaaja on {murdererName}')
    print(f'\nPelaaja on maassa {playerLocation}')

    # Suspect accusation randomiser
    while len(person_dictionary) < 8:
        randomized_person = random.choice(Suspects).name
        if randomized_person != murdererName and randomized_person != Suspects[len(person_dictionary)].name:
            person_dictionary[Suspects[len(person_dictionary)]] = randomized_person

    print(f'Henkilö {Suspects[1].name} syyttää {person_dictionary[Suspects[1]]}\n')



resetGame()

Suspects[7].accuse()

print('\n'+playerLocation)

player.flyTo()

#playername = input('Give me a name:')
#playername = 'Ilkka'
#kursori.execute("SELECT story from suspects where name='" + Suspects[1].name +"';")
#result = kursori.fetchone()

# playerName and suspect name is added to suspects story
#print(result[0].format(playerName = playername, addSuspect = person_dictionary[Suspects[1]]))
