CREATE TABLE Listings(
    id INT PRIMARY KEY,
    owner INT REFERENCES Users(id),
    title TEXT NOT NULL,
    description TEXT, /* allow to be null, maybe the title is self-explanatory or the user is shy */
    price REAL NOT NULL,
    state INT NOT NULL, /* an integer that defines the state of the listed items, e.g. 0 = available, 1 = sold, 2 = reserved. Can be changed by the owner */
);

/* in this schema, it is assumed that each listing only sells a singular item (or multiple which are sold together).
    alternatively, each item could reside in an Items-table and be referenced in Listings-table, for example through a middleman ListingItems-table like:
    Items -> ListingItems -> Listings
 */