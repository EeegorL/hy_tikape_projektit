CREATE TABLE Favorites(
    id INT PRIMARY KEY,
    user INT REFERENCES Users(id),
    listing INT REFERENCES Listings(id)
);