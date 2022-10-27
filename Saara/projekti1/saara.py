import random

kaupungit = ['Berliini', 'Praha', 'Wien', 'Budapest', 'Zagreb', 'München', 'Milano', 'Amsterdam', 'Pariisi']

class hahmo:
    def __init__(self, nimi):
        self.nimi = nimi
        self.lokaatio = ''
        self.murhaaja = False

    def asetaLokaatio(self, lokaatio):
        self.lokaatio = lokaatio

    def asetaMurhaaja(self, murhaaja):
        self.murhaaja = murhaaja

Mary = hahmo('Mary')
Luke = hahmo('Luke')
Sandra = hahmo('Sandra')
Tom = hahmo('Tom')
Adam = hahmo('Adam')

hahmot = [Jari, Tero, Masa, Pena, Kake]

random.choice(hahmot).asetaMurhaaja(True)

for i in hahmot:
    x = random.choice(kaupungit)
    i.asetaLokaatio(x)
    kaupungit.remove(x)
    print(i.nimi + " on paikassa " + i.lokaatio)