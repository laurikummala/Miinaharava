# Miinaharava

Oulun yliopiston Ohjelmoinnin alkeet -kurssin lopputyö.

Vaatii toimiakseen Haravasto.py ja spritet by Mika Oja, Oulun yliopisto.

Pelissä on tekstimuotoinen valikko, josta valitaan haluttu toiminto.

Toiminnot ovat: Uusi peli, Tilastot ja Lopeta peli

-UUSI PELI
  
  -> Ohjelma kysyy pelaajan nimeä
    -Nimi voi olla mikä tahansa kirjain- tai merkkiyhdistelmä
      
    -> Vaikeustason valinta:

        1 = Helppo, ruutuja 9 * 9 ja miinoja 10 kpl.
        
        2 = Keskitaso, ruutuja 16 * 16 ja miinoja 40  kpl.
        
        3 = Vaikea, ruutuja 16 * 30 ja miinoja 99 kpl.
        
        4 = Custom, ruutujen ja miinojen määrän voi itse valita
        
            - Jos kenttä liian pieni, tulee virheilmoitus
            - Jos miinoja alle 1 tai enemmän kuin ruutuja, tulee virheilmoitus
            - Jos ruutujen tai miinojen määrä ei ole kokonaisluku, tulee virheilmoitus

              -> Kun kaikki kysytyt tiedot on oikein asetettu, ohjelma luo halutun kokoisen kentän ja asettaa miinat kentälle satunnaisessa järjestyksessä.
                -> Peli-ikkuna avautuu ja miinojen etsiminen voi alkaa. Ikkunan ylälaidasta näkyvät tehtyjen klikkausten määrä, jäljellä olevien miinojen määrä, 
                   sekä kulunut aika.

                  - Ruutuja avataan painamalla hiiren vasenta painiketta, jos ruudussa on miina, peli loppuu ja kyseisen pelin tilastot näytetään tekstimuodossa.
                    Tiedot tallentuvat myös tulokset.txt -tekstitiedostoon.

                    - Jos ruudussa ei ole miinaa, ruudusta paljastuu joko numero tai tyhjä ruutu. 
                      - Numero kertoo sen, moneenko miinaan kyseinen ruutu on yhteydessä.
                      - Jos ruutu on tyhjä ja se on yhteydessä muihin tyhjiin ruutuihin, avautuvat kaikki siihen yhteydessä olevat tyhjät ruudut.
                        Avautuminen päättyy tyhjien ruutujen jälkeisiin numeroruutuihin, jotka vielä avatautuvat.

                  - Oletetun miinan sijainti voidaan merkata hiiren oikealla painikkeella. Ruutuun tulee tällöin huutomerkki. Merkki voidaan poistaa
                    painamalla hiiren oikeaa painiketta uudelleen.

                  - Jos kaikki ruudut on avattu osumatta miinaan, peli päättyy voitton. Kyseisen pelin tiedot näkyvät tekstimuodossa ja tallentuvat
                    tulokset.txt -tekstitiedostoon.
        
-TILASTOT
  -> Näyttää pelatut pelit järjestyksessä uusin alimmaisena
    - Tallentaa seuraavat tiedot tekstitiedostoon:
      - Pelaajan nimi
      - Tulos: Voitto tai häviö
      - Kesto minuuteissa
      - Pvm ja klo
      - Klikkaukset
      - Vaikeustaso
      - Kentän korkeus
      - Kentän leveys
      - Miinojen lukumäärä
      
-LOPETA
  -> Lopettaa pelin


