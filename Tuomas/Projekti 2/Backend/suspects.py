from reset import *
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

# Suspects tell their story
    def tellStory(self,name):
        kursori.execute("SELECT story from suspects where name= '" + name + "';")
        story = kursori.fetchone()
        print(story)

    def accuse(self):
        kursori.execute("SELECT story from suspects where name='" + self.name + "';")
        result = kursori.fetchone()
        #print(result[0])
        return result[0]
