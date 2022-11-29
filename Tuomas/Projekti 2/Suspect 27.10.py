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
class Suspect:
    def __init__(self,name,status):
        self.name = name
        self.status = status

    def tellStory(self,name):

        kursori.execute("SELECT story from suspects where name= '" + name + "';")
        tarina = kursori.fetchone()
        print(tarina)
    # Metodit:
    # Kerro tarina
    pass

s1 = Suspect('Mary',0)
s1.tellStory('Luke')
