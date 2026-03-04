CREATE TABLE Stations (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE Trips (
    id INTEGER PRIMARY KEY,
    start_time TEXT,
    end_time TEXT,
    start_station_id INTEGER REFERENCES Stations,
    end_station_id INTEGER REFERENCES Stations,
    distance INTEGER,
    duration INTEGER
);