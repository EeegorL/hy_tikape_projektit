### Testi 1:
- Rivien lisääminen: 3 sek
- SELECT-kysely: 35 sek
- Tiedoston koko: 37 Mb

### Testi 2:
- Rivien lisääminen: 5 sek
- SELECT-kysely: 0 sek
- Tiedoston koko: 49 Mb

### Testi 3:
- Rivien lisääminen: 3 sek
- SELECT-kysely: 0 sek
- Tiedoston koko: 48 Mb

Testi 1 luo tietokannan ilman indeksilisäämisen vaatimaa lisätyötä, ja on siksi nopea. Myös tiedostokoko on testeistä pienin, sillä indeksit eivät ole viemässä tilaa.
Hakuvaiheessa prosessi kuitenkin hidastuu, koska tietokanta joudutaan skannaamaan ja jokainen rivi nuuhkimaan läpi.


Testi 2 on hitain, sillä testi tekee "tuplatyötä", lisäten tauluun itse tietoa ja sitä vastaavia indeksejä, päivittäen indeksejä joka lisäyksellä.
Kun indeksit ovat olemassa, haku kuitenkin nopeutuu merkittävästi (vrt. 35s vs 0s), kun tietokanta "tietää" missä halutut arvot ovat indeksejen perusteella.


Testi 3 on kuitenkin voittaja, joka on kaikilta osin nopea.
Se eroaa ensimmäisestä tesistä indeksillään, ja toisesta sillä, että indeksi luodaan vasta kun kaikki rivit ovat lisätty tauluun. Tämä aiheuttaa sen, että indeksit luodaan vain kerran, eikä niitä tarvitse päivittää jokaisen lisäyksen yhteydessä kuin edellisessä testissä.