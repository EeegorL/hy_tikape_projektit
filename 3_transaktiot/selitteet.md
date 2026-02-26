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

Vain ensimmäinen transaktio onnistuu. Toinen transaktio (K2) kaatuu, sillä K1:n transaktion UPDATE-lause lukitsee tietokannan käyttöönsä estäen sen muokkaamista siihen asti, kunnes tämä (K1) transaktio committaa (tai peruu) muutoksensa.