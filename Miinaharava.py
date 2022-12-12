# Kentän luonti ja koon valinta, toimittava myös muulla kuin neliön muotoisella kentällä.
# Miinojen sijoitus kentälle satunnaiseen järjestykseen
# Miinojen määrän valinta
# Pystyttävä tekemään valintoja hiirellä
# Peli tallentaa tilastoja pelatuista peleistä erilliseen tiedostoon.
# vähintään pelin ajankohdan (päivämäärä + kellonaika), keston minuuteissa,
# keston vuoroissa ja lopputuloksen (voitto tai häviö, kentän koko ja miinojen lukumäärä).
# Pelissä on alkuvalikko, josta voi valita uuden pelin, lopettamisen ja tilastojen katsomisen -
# huom! valikko voi olla tekstipohjainen, ainoastaan itse peli-ikkunan tulee olla graafinen.


"""
    Pelaaja voi valita hiirellä ruudukosta yhden ruudun kerrallaan.  
    Valittu koordinaatti aukaistaan eli pelaajalle näytetään ruudun sisältö. 
    Jos valitussa ruudussa oli miina, pelaaja häviää ja peli päättyy. Muuten menetellään seuraavasti:
    
        - Jos valitun ruudun viereisissä (myös viistosti!) ruuduissa on vähintään yksi piiloitettu miina, 
          kyseessä on numeroruutu ja sen kohdalla näytetään ympäröivien miinojen lukumäärä.
        - Jos valitun ruudun viereisissä ruuduissa ei ole miinoja (eli se on tyhjä), 
          aukaistaan kaikki ympäröivät ja niitä ympäröivät jne. ruudut joka suuntaan niin pitkälle, 
          että saavutetaan miinakentän raja tai ensimmäinen numeroruutu, joka myös aukaistaan.
"""

""" 
    Peli voi päättyä kahdella tavalla:
    - Pelaaja häviää avatessaan ruudun, johon on piilotettu miina.
    - Pelaaja voittaa, kun kaikki miinattomat ruudut on aukaistu kentältä.
"""


from random import randint
import haravasto
import time
tila = {
    "kentta": [],
    "avaamaton_kentta": [],
    "aloitusaika": 0,
    "lopetusaika": 0,
}


nappula = {
    "HIIRI_VASEN": "vasen",
    "HIIRI_KESKI": "keski",
    "HIIRI_OIKEA": "oikea"
}

tilasto = {
    "Pelaaja": None,
    "Kesto minuuteissa": 0,
    "Pelattu": 0,
    "Klikkaukset": 0,
    "Vaikeustaso": None,

}


def tyhjenna_tiedot():

    tilasto["Pelaaja"] = None,
    tila["aloitusaika"] = 0
    tila["lopetusaika"] = 0
    tilasto["Kesto minuuteissa"] = 0
    tilasto["Klikkaukset"] = 0
    tila["kentta"] = None


def kysy_kentta():
    """
    Kysytään käyttäjältä, mikä vaikeusaste valitaan. Vaikeusasteita on kolme:
    helppo, keskivaikea ja vaikea. 
    Valituissa vaikeusasteissa kentän koot ja miinojen lukumäärät ovat vakioita.
    Käyttäjä voi halutessaan päättää kentän koon ja miinojen määrän itse.
    """

    print("")
    print("Tervetuloa pelaamaan miinaharavaa!")
    print("")
    tilasto["Pelaaja"] = input("Anna nimesi: ")
    print("")

    while True:

        try:

            valinta = int(input(
                "Valitse vaikeustaso (1 = Helppo, 2 = Keskivaikea, 3 = Vaikea, 4 = Oma valinta): "))
            print("")

            if valinta == 1:
                korkeus = 9
                leveys = 9
                miinoja = 10
                tilasto["Vaikeustaso"] = "Helppo"
                luo_kentta(korkeus, leveys, miinoja)
                return False

            if valinta == 2:
                korkeus = 16
                leveys = 16
                miinoja = 40
                tilasto["Vaikeustaso"] = "Keskitaso"
                luo_kentta(korkeus, leveys, miinoja)
                return False

            if valinta == 3:
                korkeus = 16
                leveys = 30
                miinoja = 99
                tilasto["Vaikeustaso"] = "Vaikea"
                luo_kentta(korkeus, leveys, miinoja)
                return False

            if valinta == 4:

                while True:
                    try:
                        korkeus = int(
                            input("Anna kentän korkeus kokonaislukuna: "))
                        print("")
                        if korkeus <= 1:
                            print("Liian matala kenttä!")
                            continue
                    except ValueError:
                        print("")
                        print("Anna kokonaisluku!")
                        print("")
                        continue

                    while True:

                        try:

                            leveys = int(
                                input("Anna kentän leveys kokonaislukuna: "))
                            print("")
                            if leveys <= 1:
                                print("Liian kapea kenttä!")
                                continue
                        except ValueError:
                            print("")
                            print("Anna kokonaisluku!")
                            print("")
                            continue

                        while True:

                            try:

                                miinoja = int(
                                    input("Anna haluttu miinojen määrä kokonaislukuna: "))
                                print("")
                                if miinoja > leveys * korkeus:
                                    print("Kaikki miinat eivät mahdu kentälle!")
                                    continue

                                elif miinoja < 1:
                                    print("Anna vähintään yksi miina!")
                                    continue

                            except ValueError:
                                print("")
                                print("Anna kokonaisluku!")
                                print("")

                            else:
                                tilasto["Vaikeustaso"] = "Custom"
                                luo_kentta(korkeus, leveys, miinoja)
                                return False
            else:
                print("")
            print("Anna kokonaisluku väliltä 1 - 4!")
            print("")
            continue

        except ValueError:
            print("")
            print("Anna kokonaisluku väliltä 1 - 4!")
            print("")
            continue

        else:
            luo_kentta(korkeus, leveys, miinoja)


def luo_kentta(korkeus, leveys, miinoja):
    # Luodaan kenttä,
    # jonka korkeus on annettu korkeus.
    for rivi in range(korkeus):
        kentta.append([])                                                    #
        # ja leveys annettu leveys
        for sarake in range(leveys):
            kentta[-1].append(" ")

    jaljella = []
    for sarake in range(leveys):
        for rivi in range(korkeus):
            jaljella.append((sarake, rivi))

    tila["kentta"] = kentta

    miinoita(kentta, jaljella, miinoja)

    return kentta


def miinoita(kentta, vapaat, lkm):
    """
    Asettaa kentälle N kpl miinoja satunnaisiin paikkoihin.
    """
    miinat = 0
    vapaat = []

    # Luuppi, joka pyörii niin kauan, kunnes haluttu miinamäärä on asetettu kentälle.
    while miinat < lkm:
        # Käy läpi kentän x ja y -suunnassa
        x = randint(0, len(kentta) - 1)
        y = randint(0, len(kentta[0])-1)
        # Jos kentällä ei ole vielä miinaa,
        if kentta[x][y] != "x":
            # siihen asetetaan miina
            kentta[x][y] = "x"
            miinat += 1
    print("Peli on käynnissä, rupeahan klikkailemaan!")


def laske_miinat(lista, x, y):
    """
    Laskee annetussa huoneessa yhden ruudun ympärillä olevat miinat ja palauttaa
    niiden lukumäärän. Funktio toimii sillä oletuksella, että valitussa ruudussa ei
    ole miinaa - jos on, sekin lasketaan mukaan.
    """

    # Määritetään listan leveys
    leveys = len(lista[0])
    # Määritetään listan korkeus
    korkeus = len(lista)
    miinoja = 0

    try:
        # Haetaan poikkeuksia tältä riviltä
        lista[y][x]

    # Poikkeus syntyy, jos indeksi on listan ulkopuolella,
    except IndexError:
        # mutta se ohitetaan.
        pass

    # Jos poikkeusta ei löydy, siirrytään for -silmukkaan
    else:

        # Määritellään rivin minimit ja maksimit
        for r in range(min(max(x-1, 0), leveys), min(max(x+2, 0), leveys)):
            # Määritellään sarakkeen minimit ja maksimit
            for c in range(min(max(y-1, 0), korkeus), min(max(y+2, 0), korkeus)):

                # Jos listan indeksistä löytyy "x", eli miina,
                if lista[c][r] == "x":
                    # miinojen määrä kasvaa yhdellä
                    miinoja += 1

        return miinoja


def tulvataytto(kentta, x, y):
    """
    Merkitsee planeetalla olevat tuntemattomat alueet turvalliseksi siten, että
    täyttö aloitetaan annetusta x, y -pisteestä.
    """
    leveys = len(kentta[0]) - 1
    korkeus = len(kentta) - 1

    # tuntematon = " "
    # vaarallinen = "x"
    # turvallinen = "0"

    # Luodaan uusi lista, jossa on alkiona yksi monikko, joka sisältää täytön aloituspisteen
    aloituspiste = [(x, y)]
    if aloituspiste == "x":         # Jos tutkimusta yritetään aloittaa vaarallisen ruudun kohdalta kohdalta, ei tehdä mitään

        pass
    if kentta[y][x] == " ":
        # Tämän jälkeen mennään silmukkaan, jossa pyöritään niin kauan, että kaikki täytettävät alueet on täytetty.
        while len(aloituspiste) > 0:

            # 1. Otetaan listasta ulos yksi koordinaattipari käsiteltäväksi, (huom. se poistetaan listasta) - tähän on olemassa oma listametodinsa.
            x, y = aloituspiste.pop()
            miinat = laske_miinat(kentta, x, y)

            # 2. Merkitään se turvalliseksi, eli merkitään planeettaan siihen kohtaan "0"
            kentta[y][x] = "0"

            kentta[y][x] = str(miinat)

            # 3. Käydään vuorotellen läpi kaikki viereiset ruudut(8 kpl) (huomioiden planeetan reunat!)
            for r in range(y - 1, y + 2):
                for c in range(x - 1, x + 2):
                    if r < 0:
                        r = 0
                    if c < 0:
                        c = 0
                    if c > leveys:
                        c = leveys
                    if r > korkeus:
                        r = korkeus
                    if kentta[r][c] == " ":

                        if miinat == 0:
                            aloituspiste.append(tuple([c, r]))
    return None


def kasittele_hiiri(x, y, nappi, muokkausnapit):
    """
    Tätä funktiota kutsutaan kun käyttäjä klikkaa sovellusikkunaa hiirellä.
    """
    x = int(x/40)
    y = int(y/40)

    if nappi == haravasto.HIIRI_VASEN:
        tilasto["Klikkaukset"] += 1

        if tilasto["Klikkaukset"] == 1:
            tila["aloitusaika"] = time.time()

        if tila["kentta"][y][x] == "x":
            tila["lopetusaika"] = time.time()
            havitty_peli()
        elif tila["kentta"][y][x] == " ":
            tulvataytto(kentta, x, y)

    if nappi == haravasto.HIIRI_OIKEA:
        tilasto["Klikkaukset"] += 1

        if tilasto["Klikkaukset"] == 1:
            tila["aloitusaika"] = time.time()

        if tila["kentta"][y][x] == " ":
            tila["kentta"][y][x] = "f"
        elif tila["kentta"][y][x] == "f":
            tila["kentta"][y][x] = " "
        else:
            print("")
            print("Ruutuun ei voi laittaa lippua!")

    if tuliko_voitto():

        tilasto["Pelattu"] = time.strftime(
            "%d-%m-%Y, %H:%M:%S", time.localtime())
        print("")
        print("Voitit pelin!!")
        print("")
        haravasto.aseta_hiiri_kasittelija(kasittele_hiiri_loppu)
        print(tilasto)
        tallenna_tulokset()
        print("")
        print("Ruutu sulkeutuu automaattisesti 5 sekunnin kuluttua")
        time.sleep(5)
        haravasto.lopeta()

    return None


def tuliko_voitto():
    """
    Tutkii pelin kuluessa, milloin kaikki ruudut on avattu niin, ettei ole osuttu miinaan. 
    """

    for x in kentta:
        for y in x:
            if y == " " or y == "f":
                return False
    tila["lopetusaika"] = time.time()
    return True


def havitty_peli():

    tilasto["Pelattu"] = time.strftime("%d-%m-%Y, %H:%M:%S", time.localtime())
    print("")
    print("Voi voi, osuit miinaan.. peli loppui!!")
    print("")
    haravasto.aseta_hiiri_kasittelija(kasittele_hiiri_loppu)
    pelin_kesto()
    print(tilasto)
    tallenna_tulokset()
    print("")
    print("Ruutu sulkeutuu automaattisesti 5 sekunnin kuluttua")
    time.sleep(5)
    haravasto.lopeta()


def tallenna_tulokset():

    try:
        with open("tulokset.txt", "a+") as kohde:
            kohde.write("Pelaaja: {}\nKesto minuuteissa: {}\nPvm ja klo: {}\nKlikkaukset: {}\nVaikeustaso: {}\n-------\n"
                        .format(tilasto["Pelaaja"],
                                tilasto["Kesto minuuteissa"],
                                tilasto["Pelattu"],
                                tilasto["Klikkaukset"],
                                tilasto["Vaikeustaso"]))

    except IOError:
        print("Tallennus epäonnistui!")


def kasittele_hiiri_loppu(x, y, nappi, muokkausnapit):
    '''
    Ottaa hiiren toiminnot pois käytöstä, kun peli on päättynyt.
    '''

    if nappi == haravasto.HIIRI_VASEN:
        nappi = None
    elif nappi == haravasto.HIIRI_OIKEA:
        nappi = None


def pelin_kesto():

    tilasto["Kesto minuuteissa"] = round((int(
        tila["lopetusaika"]) - int(tila["aloitusaika"]))/60, 2)
    


def piirra_kentta():
    """
    Käsittelijäfunktio, joka piirtää kaksiulotteisena listana kuvatun miinakentän
    ruudut näkyviin peli-ikkunaan. Funktiota kutsutaan aina kun pelimoottori pyytää
    ruudun näkymän päivitystä.
    """

    x = 0
    y = 0
    teksti = ""

    haravasto.aseta_piirto_kasittelija(piirra_kentta)
    haravasto.tyhjaa_ikkuna()
    haravasto.piirra_tausta()
    haravasto.piirra_tekstia(teksti, x, y, vari=(
        0, 0, 0, 255), fontti="serif", koko=32)
    haravasto.aloita_ruutujen_piirto()
    for y in range(len(tila["kentta"])):
        for x in range(len(tila["kentta"][0])):
            haravasto.lisaa_piirrettava_ruutu(
                tila["kentta"][y][x], x * 40, y * 40)
    haravasto.piirra_ruudut()


def main(kentta):
    """
    Lataa pelin grafiikat, luo peli-ikkunan ja asettaa siihen piirtokäsittelijän.
    """

    haravasto.lataa_kuvat("spritet")
    haravasto.luo_ikkuna(len(kentta[0] * 40), len(kentta * 40))
    haravasto.aseta_piirto_kasittelija(piirra_kentta)
    haravasto.aseta_hiiri_kasittelija(kasittele_hiiri)
    haravasto.aloita()


if __name__ == "__main__":

    kentta = []

    tyhjenna_tiedot()

    while True:

        print("")
        aloitus = str(
            input("Valitse haluamasi toiminto: (U)usi peli, (T)ilastot, (L)opeta peli): "))
        print("")

        if aloitus == "L" or aloitus == "l":
            print("Lopetit pelin!")
            print("")
            break

        elif aloitus == "T" or aloitus == "t":
            print(tilasto)

        elif aloitus == "U" or aloitus == "u":

            kysy_kentta()
            main(kentta)

        else:
            print("")
            print("Anna oikea komento!")
            print("")
