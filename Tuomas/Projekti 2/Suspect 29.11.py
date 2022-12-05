import random
import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='lentopeli',
    password='peli',
    autocommit=True
)
kursori = yhteys.cursor()

countries = ['Unkari', 'Kroatia', 'Itävalta', 'Tsekki', 'Saksa', 'Tanska', 'Alankomaat', 'Italia', 'Ranska', 'Puola',
             'Ruotsi', 'Kreikka', 'Albania', 'Romania', 'Iso-Britannia']

class Suspect:
    def __init__(self, name):
        self.name = name
        self.location = ''
        self.murderer = False

        kursori.execute("UPDATE suspects SET status=0 WHERE name= '" + self.name + "';")


    def set_location(self, location):
        self.location = location

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
    pass

Mary = Suspect('Mary')
Luke = Suspect('Luke')
Sandra = Suspect('Sandra')
Tom = Suspect('Tom')
Adam = Suspect('Adam')
Kristen = Suspect('Kristen')
Stefan = Suspect('Stefan')
Jake = Suspect('Jake')

Suspects = [Mary, Luke, Sandra, Tom, Adam, Kristen, Stefan, Jake]

# Murderer is set
random.choice(Suspects).set_murderer(True)

# Suspect location randomized and set
for i in Suspects:
    x = random.choice(countries)
    i.set_location(x)
    countries.remove(x)
    print(f'{i.name} on paikassa {i.location}')

# Player location randomized
playerLocation = random.choice(countries)

print(f'\nMurhaaja on {murdererName}')
print(f'\nPelaaja on maassa {playerLocation}')