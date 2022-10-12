import random
maat = ['Unkari','Kroatia','Itävalta','Tsekki','Saksa','Tanska','Alankomaat','Italia','Ranska']
henkilo = ['Mary','Luke','Sandra','Tom','Adam']

random.shuffle(maat)

print(f'Epäillyistä henkilöistä ensimmäinen on nimeltään: {henkilo[0]}. Hän on lähtenyt tapahtuman jälkeen maahan nimeltä: {maat[0]}')

