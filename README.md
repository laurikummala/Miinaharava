# Miinaharava

Oulun yliopiston Ohjelmoinnin alkeet -kurssin lopputyö.

Vaatii toimiakseen Haravasto.py ja spritet by Mika Oja, Oulun yliopisto.

Karvalakkiversio.

Pelissä on tekstimuotoinen valikko, josta valitaan haluttu toiminto.

Toiminnot ovat:

-UUSI PELI
  
  -> Kysytään pelaajan nimi
      -Nimi voi olla mikä tahansa kirjain tai merkkiyhdistelmä
      
    -> Vaikeustason valinta:

        - Helppo, ruutuja 9 * 9 ja miinoja 10 kpl
        - Keskitaso, ruutuja 16 * 16 ja miinoja 40
        - Vaikea, ruutuja 16 * 30 ja miinoja 99
        - Custom, ruutujen ja miinojen määrän voi itse valita
          - Jos kenttä liian, pieni, tulee virheilmoitus
          - Jos miinoja liian vähän tai liikaa, tulee virheilmoitus
          - Jos ruutujen tai miinojen määrä ei ole kokonaisluku, tulee virheilmoitus
            
            -> Kun kaikki kysytyt tiedot on oikein asetettu, ohjelma luo halutun kokoisen kentän ja asettaa miinat kentälle satunnaisessa järjestyksessä.
              -> Peli-ikkuna avautuu ja miinojen etsiminen voi alkaa. Ikkunan ylälaidasta näkyvät tehtyjen klikkausten määrä, jäljellä olevien miinojen määrä, 
                 sekä kulunut aika.
                 
                - Ruutuja avataan painamalla hiiren vasenta painiketta, jos ruudussa on miina, peli loppuu ja kyseisen pelin tilastot näytetään tekstimuodossa.
                  Tiedot tallentuvat myös tekstitiedostoon.
                  
                  - Jos ruudussa ei ole miinaa, ruudusta paljastuu joko numero tai tyhjä ruutu. 
                    - Numero kertoo sen, moneenko miinaan kyseinen ruutu on yhteydessä.
                    - Jos ruutu on tyhjä ja se on yhteydessä muihin tyhjiin ruutuihin, avautuvat kaikki siihen yhteydessä olevat tyhjät ruudut.
                      Avautuminen päättyy tyhjien ruutujen jälkeisiin numeroruutuihin, jotka vielä avatautuvat.
                      
                - Oletetun miinan sijainti voidaan merkata hiiren oikealla painikkeella. Ruutuun tulee tällöin huutomerkki.
                
                - Jos kaikki ruudut on avattu osumatta miinaan, peli päättyy voitton. Kyseisen pelin tiedot näkyvät tekstimuodossa ja tallentuvat tekstitiedostoon.
        
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


