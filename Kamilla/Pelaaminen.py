import time

#valmis toistuu nyt molemmissa fileissani. Kun lopulta yhdistetään kaikki otetaan toinen pois.
valmis = input("Paina enter-näppäintä, kun olet valmis aloittamaan!")
##Miten estän muiden merkkien laiton?

#print vaihtoehdoista, minne lentää. Hups sori tuomas tein tän en tiiä onks tää hyvä mut sä saat kuiteki tehä sen toiminnallisuuden -Kamilla :)
minne = None

if valmis == "":
    minne = input('''Minne haluaisit lentää? Epäillyt ovat: {epäillyn nimi} {epäillyn sijainti}, {epäillyn nimi} {epäillyn sijainti},
        {epäillyn nimi} {epäillyn sijainti}, {epäillyn nimi} {epäillyn sijainti} ja  {epäillyn nimi} {epäillyn sijainti}.
        Sinulla on lentoja jäljellä: {lentojajäljellä}. Kirjoita sijainnin nimi: ''')

while lennot != 0:
    print(minne)
    lennot -= 1

#Jos kentällä on henkilö juttele tälle jossei kysy minne uudestaan
if #kentällä on henkilö funktio = True:
    print(henkilönpuhe kuka kentällä on)
else:
    print(f"Kukaan epäillyistä ei ole täällä. {minne} ")

#Voitit pelin tai hävisit
arvaus = input("Kuka on murhaaja? Kirjoita murhaajan nimi: ")
arvaus = arvaus.lower()

if arvaus == #"muuttuja johon tallentuu arvottu murhaaja":
    voitto = True

if voitto = True
    print("Hyvä ratkaisit kuka oli murhaaja! Voitit pelin!")
else:
    print("{arvaus} ei ollut murhaaja. Murhaaja oli {murhaaja}. Hävisit pelin!")