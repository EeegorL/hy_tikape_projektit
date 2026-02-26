CREATE TABLE Images(
    id INT PRIMARY KEY,
    image TEXT, /* path referencing the image on the server serving the client. Could alternately be a blob storing the (preferably rather small) image itself as binary data */
    /* image BLOB NOT NULL */
    listing INT REFERENCES Listings(id)
);