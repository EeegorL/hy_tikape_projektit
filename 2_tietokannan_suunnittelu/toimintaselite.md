Muutos- ja lisäysoperaatioissa oletetaan, että käyttäjä on kirjautunut järjestelmään, ja siten valtuutettu tekemään muutoksia. Syntyisi turhaa toistoa, jos asia mainittaisiin aina erikseen.

Esim. tekstissä "Myyjä voi lisätä ilmoitu*kseensa* asiasanoja..." oletetaan, että myyjä on tunnistettu ilmoituksen omistajaksi kirjautumistiedoista.

## Käyttäjä voi kirjautua järjestelmään antamalla tunnuksen ja salasanan.

Käyttäjä kirjautuu järjestelmään tauluun **Users** tallennetun käyttäjänimeä (*username*) ja salasanaa vastaavaa hashia (*passwordHash*) käyttämällä.

## Käyttäjä pystyy katsomaan muiden käyttäjien lähettämiä ilmoituksia sekä lähettämään omia ilmoituksia.

Järjestelmä hakee käyttäjälle näytettäväksi taulun **Listings** mukaiset ilmoitukset.
Ilmoituksesta ilmenee sen tekijä. Tietokantatasolla yksittäinen *listing* viittaa taulun **Users** *id*-kenttään oman kenttänsä *owner* arvolla.

Käyttäjä voi myös itse luoda ilmoituksia, jolloin *listingin* *owner*-kenttään tulee kyseisen käyttäjän *id*.

## Ilmoituksessa näkyy myytävän tavaran tiedot (otsikko, kuvaus, hinta) sekä yksi tai useampia kuvia.

Ilmoitus sisältää niin tekstimuotoista tietoa, kuten otsikon ja kuvauksen jotka tallentuvat **Listings**-taulun, sekä tarvittaessa kuvia, jotka tallentuvat tauluun **Images**, linkittyen asianmukaiseen *listingiin* sen *id*:n perusteella oman *listing*-kentän arvolla.

## Ilmoituksessa voi olla luokittelu myytävälle tavaralle (esimerkiksi osasto kirjat, sijainti Helsinki).

Myyjä voi lisätä ilmoitukseensa asiasanoja parantaakseen ilmoituksensa näkyvyyttä asiakkaan suodattaessa tuloksia.

Asiasanavaihtoehdot ovat määritelty taulussa **Categories**, sisältäen kategorian nimen.
Myyjän lisättyä ilmoitukselleen asiasanan, tämä tallentuu "välikäsitauluun" **Keywords**, joka sisältää *listing*-viiteavaimen kyseisen *listingin* *id*:hen, sekä *category*-viiteavaimen, joka viittaa **Categories**-taulun kategorioihin.


## Käyttäjä voi merkitä ilmoituksen suosikikseen.

Käyttäjä voi merkitä ilmoituksen suosikikseen, jolloin tieto tästä tallentuu tauluun **Favorites**, joka sisältää **Listings**-taulun *id*:hen viittaavat viiteavaimen *listing* ilmoituksesta jota tietue koskee, ja viiteavaimen *user*, joka viittaa ilmoituksen suosikiksi lisänneen käyttäjän **Users**-taulun mukaiseen *id*:hen.

Tällöin voidaan hakea vain ne ilmoitukset, joiden id löytyy Favorites-taulusta.

## Kaksi käyttäjää pystyy viestittelemään keskenään ilmoitukseen liittyen.
Kaksi käyttäjää voivat keskustella ilmoituksen suhteen, jolloin keskustelu itse tallentuu tauluun **Conversations**, ja keskustelun viestit tauluun **Messages**. 
Nämä taulut linkittyvät **Messages**-taulun viiteavaimen *conversation* viitaten **Conversations**-taulun *id*-kenttään.

**Conversations**-taulu itsessään sisältää osapuolista tiedon vain kysyjästä/ostajasta kentällä *asker*, viitaten taulun **Users** *id*:hen. Myyjän tiedot voidaan selvittää kyselyllä **Conversations**-taulun viiteavaimella *listing*, joka viittaa *listingin* *id*:hen. **Listing**-taulu puolestaan sisältää tiedon sen luojasta.

Taulu **Messages** sisältää tiedon sen lähettäneestä käyttäjästä *id*:n muodossa kentässä *user*, joka viittaa tauluun **User**, tiedon keskustelusta johon se liittyy, avaimen *conversation*-muodossa, sekä itse lähetetyn viestin tekstisisällön.

Käyttäjät eivät pysty jakamaan toisilleen kuvia tms. tietomuotoja, ainoastaan tekstiä.

## Käyttäjä pystyy merkitsemään tavaran varatuksi ja myydyksi.

Myyjä voi vaihtaa listauksensa tilan oletuksesta joko varatuksi tai myydyksi, joka näkyy muille käyttäjille.

Myyjän päivitys tallentuu **Listings**-taulun tietueen *state*-kenttään, jolla on ilmoituksen tilaa kuvaava numeerinen arvo, esim. 0 = myynnissä, 1 = myyty ja 2 = varattu.

## Tavaran myynnin jälkeen myyjä ja ostaja pystyvät antamaan toisilleen palautteen.

Kun tavara on myyty, eli *listingin* kentän state arvo on edellisen kohdan mukaisesti 1, myyjälle ja ostajalle avautuu mahdollisuus antaa toisilleen palautetta.

Palaute tallentuu tauluun **Feedback**, joka linkittyy kentän *conversation*-viitteen avulla taulun **Conversations**-keskusteluun.
Taulussa käyttäjältä pyydetään perinteinen 1-5 arviointi ja mahdollisuus tekstimuotoiseen palautteeseen.

Taulussa on myös kenttä *role*, joka määrää missä roolissa arvosteleva käyttäjä on, myyjä vai ostaja. Näin, käyttäjällä voi olla esim. mainio maine myyjänä, mutta surkea maine ostajana, jos arvostelut ovat julkisia.