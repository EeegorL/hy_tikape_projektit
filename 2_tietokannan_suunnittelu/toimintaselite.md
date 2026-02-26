Käyttäjä kirjautuu palveluun käyttäen Users-taulun username-käyttäjänimeä ja salasanallaan, jota verrataan passwordHash-arvoon taulussa.

Käyttäjä voi selata muiden Listings-taulun mukaisia listauksia, joissa näkyy ilmoitukseen liittyviä tietoja (mm. otsikko, kuvaus, hinta), tai tahtoessaan omiksi suosikeiksi (Favorites-taulu) merkittyjä erikseen.
Käyttäjä voi myös merkitä uusia Listingejä suosikeiksiin.

Halutessaan käyttäjä voi luoda omia Listings-ilmoituksia. Näihin voi lisätä tuotekuvia (Images-taulu) ja sijaintia, tuotekategoriaa tms. kuvaavia asiasanoja (Categories, jotka linkittyvät tiettyyn Listingiin taulun Keywords kautta). 
Asiasanat ovat valmiiksi luotuja, mutta vaihtoehtoisesti käyttäjä voisi luoda/suositella uuden luomista.

Käyttäjä voi ostajana keskustella myyjien kanssa, jolloin keskustelut tallentuvat Messages-tauluun, ja linkittyvät keskusteluksi Conversations-taulun mukaisesti.
Listingillä on kenttä state, joka kuvaa Listingin tilaa. 
Jos keskustelu päättyy tuotteen ostamiseen tai sen varaamiseen, myyjä voi merkitä Listingille uuden tilan (esim. 0 = saatavilla, 1 = myyty, 2 = varattu). 
Jos osto toteutuu, keskustelu mahdollistaa palautteen jättämisen, joka tallentuu keskustelukohtaisesti Feedback-taulun