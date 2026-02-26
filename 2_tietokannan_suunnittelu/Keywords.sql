CREATE TABLE Keywords(
    id INT PRIMARY KEY,
    category INT REFERENCES Categories(id),
    listing INT REFERENCES Listings(id)
);

/* alternatively, the system could use user-written keywords instead of the predefined ones in the Categories-table, but typos and alternating spelling could make things messy */