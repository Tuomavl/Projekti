#Mysql connector
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

#Suspect object
class Suspect:
    def __init__(self, name):
        self.name = name
        self.location = ''
        self.murderer = False
        self.murdererName = None

        kursori.execute("UPDATE suspects SET status=0 WHERE name= '" + self.name + "';")

    #Sets the suspects location
    def set_location(self, location):
        self.location = location
        kursori.execute("UPDATE gameCountries SET suspectName='" + self.name + "' WHERE name= '" + self.location + "';")

    #Defining who of the suspects is a murderer
    def set_murderer(self, murderer):
        self.murderer = murderer
        kursori.execute("UPDATE suspects SET status=1 WHERE name= '" + self.name + "';")

    #Suspects tell their story
    def tellStory(self,name):
        kursori.execute("SELECT story from suspects where name= '" + name + "';")
        story = kursori.fetchone()
        print(story)
        return story

    #Gets the current suspects accusation text
    def accuse(self):
        kursori.execute("SELECT story from suspects where name='" + self.name + "';")
        result = kursori.fetchone()
        #print(result[0])
        return result[0]
