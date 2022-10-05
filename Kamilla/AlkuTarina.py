import time
def dialogue(text):
    for i in text:
        print(i, end = "")
        time.sleep(0.1)
    print()
    time.sleep(len(text) / 20)

dialogue("Tervetuloa Puolan Varsovaan!")
dialogue("Olet rikostutkija {syötetty käyttäjänimi mahdollisesti?}")
dialogue("Eilen myöhään yöllä Ilkka löydettiin murhattuna Varsovasta.")
dialogue("Sinun tehtäväsi on selvittää kuka murhasi Ilkan.")
dialogue("Apulaisrikostutkija on kerännyt sinulle viisi epäiltyä, jotka ovat karanneet eri lentokentille ympäri Eurooppaa. ")
dialogue("Käy haastattelemassa heitä ja selvitä kuka on murhaaja")
dialogue("mutta muista sinulla on vain 7 lentolippua eli pystyt lentämään vain seitsemään eri kohteeseen, joten käytä lentolippusi harkiten.")
dialogue("Onnea matkaan!")
valmis = input("Paina enter-näppäintä, kun olet valmis aloittamaan pelin.")
