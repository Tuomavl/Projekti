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

class Suspect:
    def __init__(self, name):
        self.name = name
        self.location = ''
        self.murderer = False
        self.murdererName = None

        kursori.execute("UPDATE suspects SET status=0 WHERE name= '" + self.name + "';")


    def set_location(self, location):
        self.location = location
        kursori.execute("UPDATE gameCountries SET suspectName='" + self.name + "' WHERE name= '" + self.location + "';")

# Defining who of the suspects is a murderer
    def set_murderer(self, murderer):
        self.murderer = murderer
        kursori.execute("UPDATE suspects SET status=1 WHERE name= '" + self.name + "';")

        murdererName == self.name

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
        #print(result[0].format(playerName=player.username, addSuspect=person_dictionary[Suspects[selfIndex]]))
