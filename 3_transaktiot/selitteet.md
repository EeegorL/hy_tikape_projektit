### Kuvatkoon K1 ja K2 kahta erillistä konsolia / käyttäjäistuntoa

# Testi 1
Testi menee läpi.
1. SELECT-lause palauttaa arvon 1
2. SELECT-lause palauttaa arvon 2

Molemmat transaktiot onnistuvat, koska toisin kuin esim päivitys- tai lisäysoperaatiossa, lukuoperaatio ei lukitse tietokantaa transaktion ajaksi.

# Testi 2
Testi menee läpi.
1. SELECT-lause palauttaa arvon 1
2. SELECT-lause palauttaa arvon 2

Molemmat transaktiot onnistuvat. Toinen SELECT-lause kuitenkin eroaa ensimmäisen testin tuloksesta, koska toisessa transaktiossa oleva SELECT-lause ei näe muiden transaktioiden "luonnosarvoja" ennen kuin ne commitataan.

# Testi 3
Testi ei mene läpi.

1. SELECT-lause palauttaa arvon 1
2. SELECT-lause palauttaa arvon 2

Vain ensimmäinen transaktio onnistuu. Toinen transaktio (K2) kaatuu, sillä K1:n transaktion UPDATE-lause lukitsee tietokannan käyttöönsä estäen sen muokkaamista siihen asti, kunnes tämä (K1) transaktio committaa (tai peruu) muutoksensa.¨

# Testi 4
Testi ei mene läpi.

1. SELECT-lause palauttaa 1
2. SELECT-lause palauttaa 2

Vain K1-transaktio onnistuu, sillä K2 yrittää päivittää tietokannan tilaa sen ollen lukittuna keskenolevan K1-transaktion vuoksi.

## Testi 5

Testi ei mene läpi.

1. SELECT-lause palauttaa 1
2. SELECT-lause palauttaa 1

Kumpikin transaktio epäonnistuu.

Etenemisjärjestyksessä, K2 transaktio epäonnistuu, koska se ei saa *commitoitua* muutostaan tietokannan ollen myös toisen transaktion käytössä. Transaktion UPDATE-lause kyllä menee läpi, mutta sitä ei saada "vahvistettua".

K1 transaktio ei puolestaan onnistu, koska tietokanta on lukittu muutoksilta K2-transaktiolla. 
Syntyy tällainen noidankehä.

Eteenpäin päästään vasta kun K1-transaktio viedään loppuun commitilla (joka ei "muutoslukon" vuoksi voi tehdä muuta kuin committaa ilman muutoksia) jonka jälkeen K2 voi tehdä mitä lystää vapautuneella tietokannalla.