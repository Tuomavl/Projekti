#Paina mitä vain aloittaaksesi
#Pelaaja syöttää käyttäjännimensä ja peli alkaa
#Tarina alkaa, antaa epäiltyjen sijainnit, kertoo pelin kulun
#Pelaaja valitsee mihin lähtee lentämään
#Jos kentällä on henkilö, alkaa keskustelu, jos ei pelaaja voi valita seuraavan kentän mihin mennä

#10 lentokenttää, 5 henkilöä, pelaaja saa suorittaa 7 lentoa, 5 tarinaa jossa muuttujina 1 epäillyn nimi
#Kaikkilta lentokentiltä ei voi lentää jokaiseen, ja kartta miten tää toimii pysyy aina samana.
#Kuvan laittaminen kartasta pelin sisälle ?


#Paina mitä vain aloittaaksesi (tietty)
#Pelaaja syöttää käyttäjänimen joka lisätään tietokantaan
#Randomoidaan vaadittavat muuttujat
#Peli alkaa (Tarina ja säännöt) tekstit printataan osissa hitaasti
#Peli antaa epäillyjen sijainnit
#Peli tulostaa mahdolliset suunnat mihin voi lentää
#Lentojen määrä vähenee joka kerralla
#Jos kentällä on henkilö -> juttele henkilölle, jos ei anna uusi mahdollisuus lentää muualle
#Kun lennot on käyttetty, peli kysyy murhaajaa, pelaaja syöttää tiedon
#Riippuen tuloksesta, printataan joko voitit pelin tai hävisit ja kerrotaan murhaaja.
#Voitosta lisätään streak ja lisätään voitot listaan jos häviää aloitetaan streak ja lisätään häviöt listaan
#Lopussa voit painaa jotain aloittaaksesi uudestaan tai lopetaaksesi (print kiitos että pelasit)

#print vaihtoehdoista, minne lentää. Hups sori tuomas tein tän printin en tiiä onks tää hyvä mut sä saat kuiteki tehä sen toiminnallisuuden -Kamilla :)
minne = None
minne = minne.lower()
if valmis == "":
    minne = input('''Minne haluaisit lentää? Epäillyt ovat: {epäillyn nimi} {epäillyn sijainti}, {epäillyn nimi} {epäillyn sijainti},
        {epäillyn nimi} {epäillyn sijainti}, {epäillyn nimi} {epäillyn sijainti} ja  {epäillyn nimi} {epäillyn sijainti}.
        Sinulla on lentoja jäljellä: {lentojajäljellä}. Kirjoita sijainnin nimi: ''')