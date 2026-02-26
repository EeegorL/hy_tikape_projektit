CREATE TABLE Conversations(
    id INT PRIMARY KEY,
    listing INT REFERENCES Listings(id),
    asker INT REFERENCES User(id)
    /* the id of the owner could also be added here, but if needed it can be fetched by the listing's id to keep the data 'atomic' */
);