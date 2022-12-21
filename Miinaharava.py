
from random import randint
import haravasto
import time

tila = {
    "kentta": [],
    "nakyva_kentta": [],
    "aloitusaika": 0,
    "lopetusaika": 0,
    "korkeus": 0,
    "leveys": 0,
    "sec": 0,
    "min": 0
}

kulunut_aika = None

nappula = {
    "HIIRI_VASEN": "vasen",
    "HIIRI_OIKEA": "oikea"
}

tilasto = {
    "Pelaaja": None,
    "Tulos": "",
    "Kesto_minuuteissa": 0,
    "Pelattu": 0,
    "Klikkaukset": 0,
    "Vaikeustaso": None,
    "Miinoja": 0,
    "Miinoja_jaljella": None,
}


def tyhjenna_tiedot():

    tila["aloitusaika"] = 0
    tila["lopetusaika"] = 0
    tilasto["Klikkaukset"] = 0
    tila["min"] = 0
    tila["sec"] = 0


def kysy_kentta():
    """
    Kysytään käyttäjältä, mikä vaikeusaste valitaan. Vaikeusasteita on neljä:
    helppo, keskivaikea, vaikea ja custom.
    Helpossa, keskivaikeassa ja vaikeassa kentän koot ja miinojen lukumäärät ovat vakioita.
    Customissa käyttäjä voi päättää kentän koon ja miinojen määrän itse.
    """

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
                tila["korkeus"] = korkeus
                tila["leveys"] = leveys
                tilasto["Miinoja"] = miinoja
                tilasto["Miinoja_jaljella"] = miinoja
                luo_kentta(korkeus, leveys, miinoja)
                return False

            if valinta == 2:
                korkeus = 16
                leveys = 16
                miinoja = 40
                tilasto["Vaikeustaso"] = "Keskitaso"
                tila["korkeus"] = korkeus
                tila["leveys"] = leveys
                tilasto["Miinoja"] = miinoja
                tilasto["Miinoja_jaljella"] = miinoja
                luo_kentta(korkeus, leveys, miinoja)
                return False

            if valinta == 3:
                korkeus = 16
                leveys = 30
                miinoja = 99
                tilasto["Vaikeustaso"] = "Vaikea"
                tila["korkeus"] = korkeus
                tila["leveys"] = leveys
                tilasto["Miinoja"] = miinoja
                tilasto["Miinoja_jaljella"] = miinoja
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
                                tila["korkeus"] = korkeus
                                tila["leveys"] = leveys
                                tilasto["Miinoja"] = miinoja
                                tilasto["Miinoja_jaljella"] = miinoja
                                luo_kentta(korkeus, leveys, miinoja)
                                return False
            else:
                raise ValueError

        except ValueError:
            print("")
            print("Anna kokonaisluku väliltä 1 - 4!")
            print("")
            continue


def luo_kentta(korkeus, leveys, miinoja):

    nakyva_kentta = []

    for rivi in range(korkeus):
        kentta.append([])
        for sarake in range(leveys):
            kentta[-1].append(" ")

    tila["kentta"] = kentta

    for rivi in range(korkeus):
        nakyva_kentta.append([])
        for sarake in range(leveys):
            nakyva_kentta[-1].append(" ")

    tila["nakyva_kentta"] = nakyva_kentta

    jaljella = []
    for x in range(leveys):
        for y in range(korkeus):
            jaljella.append((x, y))

    miinoita(kentta, jaljella, miinoja)


def miinoita(kentta, vapaat, lkm):
    """
    Asettaa kentälle N kpl miinoja satunnaisiin paikkoihin.
    """
    miinat = 0
    vapaat = []
    while miinat < lkm:
        x = randint(0, len(kentta) - 1)
        y = randint(0, len(kentta[0])-1)
        if kentta[x][y] != "x":
            kentta[x][y] = "x"
            miinat += 1

    print("Peli on käynnissä, rupeahan klikkailemaan!")


def laske_miinat(lista, x, y):
    """
    Laskee annetussa huoneessa yhden ruudun ympärillä olevat miinat ja palauttaa
    niiden lukumäärän. Funktio toimii sillä oletuksella, että valitussa ruudussa ei
    ole miinaa - jos on, sekin lasketaan mukaan.
    """

    leveys = len(tila["kentta"][0])
    korkeus = len(tila["kentta"])
    miinoja = 0

    try:
        tila["nakyva_kentta"][y][x]

    except IndexError:
        pass

    else:

        for r in range(min(max(x-1, 0), leveys), min(max(x+2, 0), leveys)):
            for c in range(min(max(y-1, 0), korkeus), min(max(y+2, 0), korkeus)):

                if lista[c][r] == "x":
                    miinoja += 1

        return miinoja


def tulvataytto(kentta, x, y):
    """
    Merkitsee planeetalla olevat tuntemattomat alueet turvalliseksi siten, että
    täyttö aloitetaan annetusta x, y -pisteestä.
    """
    leveys = len(kentta[0]) - 1
    korkeus = len(kentta) - 1
    aloituspiste = [(x, y)]
    if aloituspiste == "x":         
        pass
    if tila["kentta"][y][x] == " ":
        while len(aloituspiste) > 0:

            x, y = aloituspiste.pop()
            miinat = laske_miinat(kentta, x, y)

            tila["kentta"][y][x] = "0"

            tila["nakyva_kentta"][y][x] = str(miinat)

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
                    if tila["nakyva_kentta"][r][c] == " ":

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
        tilasto["Tulos"] = "Kesken"

        if tilasto["Klikkaukset"] == 1:
            tila["aloitusaika"] = time.time()
            piirra_kentta()

        if tila["kentta"][y][x] == "x":
            for j, rivi in enumerate(tila["kentta"]):  
                for i, sarake in enumerate(rivi):
                    if tila["kentta"][j][i] == "x":
                        tila["nakyva_kentta"][j][i] = "x"
            tila["lopetusaika"] = time.time()
            havitty_peli()

        elif tila["kentta"][y][x] == " ":
            tulvataytto(kentta, x, y)

    if nappi == haravasto.HIIRI_OIKEA:
        tilasto["Klikkaukset"] += 1
        tilasto["Tulos"] = "Kesken"

        if tilasto["Klikkaukset"] == 1:
            tila["aloitusaika"] = time.time()

        if tila["nakyva_kentta"][y][x] == " ":
            tila["nakyva_kentta"][y][x] = "f"
            if tilasto["Miinoja_jaljella"] < 1:
                print("")
                print("Miinoja ei voi olla vähemmän kuin nolla!")
            else:
                tilasto["Miinoja_jaljella"] -= 1
        elif tila["nakyva_kentta"][y][x] == "f":
            tila["nakyva_kentta"][y][x] = " "
            tilasto["Miinoja_jaljella"] += 1
        else:
            print("")
            print("Ruutuun ei voi laittaa lippua!")

    if tuliko_voitto():

        tilasto["Pelattu"] = time.strftime(
            "%d-%m-%Y, %H:%M:%S", time.localtime())
        tilasto["Tulos"] = "Voitto"
        print("")
        print("Voitit pelin!!")
        print("")
        haravasto.aseta_hiiri_kasittelija(hiiri_pois_kaytosta)
        pelin_kesto()
        print(tilasto)
        tallenna_tulokset()

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
    tilasto["Tulos"] = "Häviö"
    print("")
    print("Voi voi " + tilasto["Pelaaja"] + ", osuit miinaan.. peli loppui!!")
    print("")
    haravasto.aseta_hiiri_kasittelija(hiiri_pois_kaytosta)
    pelin_kesto()
    print(tilasto)
    tallenna_tulokset()


def tallenna_tulokset():

    try:
        with open("tulokset.txt", "a+") as tulos:
            tulos.write("Pelaaja: {}\nTulos: {}\nKesto minuuteissa: {}\nPvm ja klo: {}\nKlikkaukset: {}\nVaikeustaso: {}\nKentän korkeus: {}\nKentän leveys: {}\nMiinojen lkm: {}\n-------\n"
                        .format(tilasto["Pelaaja"],
                                tilasto["Tulos"],
                                tilasto["Kesto_minuuteissa"],
                                tilasto["Pelattu"],
                                tilasto["Klikkaukset"],
                                tilasto["Vaikeustaso"],
                                tila["korkeus"],
                                tila["leveys"],
                                tilasto["Miinoja"]))

    except IOError:
        print("Tallennus epäonnistui!") 


def lataa_tulokset():

    tulokset = []

    try:
        with open("tulokset.txt", "r") as tulokset:
            print(tulokset.read())
                
    except IOError:
        print("Tiedoston avaaminen epäonnistui!")


def hiiri_pois_kaytosta(x, y, nappi, muokkausnapit):
    '''
    Ottaa hiiren toiminnot pois käytöstä, kun peli on päättynyt.
    '''

    if nappi == haravasto.HIIRI_VASEN:
        nappi = None
    elif nappi == haravasto.HIIRI_OIKEA:
        nappi = None


def pelin_kesto():

    tilasto["Kesto_minuuteissa"] = round((int(
        tila["lopetusaika"]) - int(tila["aloitusaika"]))/60, 2)


def sekuntikello(kulunut_aika):

    if tilasto["Tulos"] == "Kesken":
        tila["sec"] += 1
        if tila["sec"] == 60:
            tila["min"] += 1
            tila["sec"] = 0

    return (tila["sec"])


def piirra_kentta():
    """
    Käsittelijäfunktio, joka piirtää kaksiulotteisena listana kuvatun miinakentän
    ruudut näkyviin peli-ikkunaan. Funktiota kutsutaan aina kun pelimoottori pyytää
    ruudun näkymän päivitystä.
    """

    haravasto.tyhjaa_ikkuna()
    haravasto.piirra_tausta()
    haravasto.aloita_ruutujen_piirto()

    for y in range(len(tila["nakyva_kentta"])):
        for x in range(len(tila["nakyva_kentta"][0])):
            haravasto.lisaa_piirrettava_ruutu(
                tila["nakyva_kentta"][y][x], x * 40, y * 40)
    haravasto.piirra_ruudut()
    haravasto.piirra_tekstia("Klikkaukset: {}".format(tilasto["Klikkaukset"]), 10, tila["korkeus"] * 40, vari=(
        0, 0, 0, 255), fontti="serif", koko=13)
    haravasto.piirra_tekstia("Miinoja: {}".format(tilasto["Miinoja_jaljella"]), 140, tila["korkeus"] * 40, vari=(
        0, 0, 0, 255), fontti="serif", koko=13)
    haravasto.piirra_tekstia("Aika: {:2}: {:2}".format(str(tila["min"]), str(tila["sec"])), 250, tila["korkeus"] * 40, vari=(
        0, 0, 0, 255), fontti="serif", koko=13)


def main():
    """
    Lataa pelin grafiikat, luo peli-ikkunan ja asettaa siihen piirtokäsittelijän.
    """

    haravasto.lataa_kuvat("spritet")
    haravasto.luo_ikkuna(
        len(tila["nakyva_kentta"][0] * 40), len(tila["nakyva_kentta"] * 40) + 40)
    haravasto.aseta_piirto_kasittelija(piirra_kentta)
    haravasto.aseta_toistuva_kasittelija(sekuntikello, 1)
    haravasto.aseta_hiiri_kasittelija(kasittele_hiiri)
    haravasto.aloita()


if __name__ == "__main__":
  
    print("")
    print("Tervetuloa pelaamaan miinaharavaa! Valitse jokin seuraavista toiminnoista:")

    while True:

        print("")
        print("(U)usi peli")
        print("(T)ilastot")
        print("(L)opeta peli")
        print("")
        aloitus = str(input("Valitse toiminto: ").strip().lower())

        if aloitus == "l":
            print("")
            print("Lopetit pelin!")
            print("")
            break

        elif aloitus == "t":
            print("")
            print("TULOKSET LISTATTUNA, UUSIN VIIMEISENÄ:")
            print("")
            lataa_tulokset()

        elif aloitus == "u":
            kentta = []
            tyhjenna_tiedot()
            kysy_kentta()
            main()

        else:
            print("")
            print("Anna oikea komento!")
            print("")
