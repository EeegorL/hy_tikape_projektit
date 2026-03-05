import sqlite3, os;

# https://infopalvelut.storage.hsldev.com/citybikes/od-trips-2023/od-trips-2023.zip

files = os.listdir("od-trips-2023");
# Departure,Return,Departure station id,Departure station name,Return station id,Return station name,Covered distance (m),Duration (sec.)
#     0        1               2                     3                  4                   5                 6                  7                              

trips = [];
stations = {};

for file in files:
    with open(f'od-trips-2023/{file}', encoding="utf-8") as f:
        next(f); # skip headers
        for line in f:
            data = line.split(",");
            
            # Aalto-yliopisto yrittää niin pahasti olla erilainen et pitää sitä varten tehdä omat ehdot
            if(not data[4].isnumeric()):
                data[3] = (data[3] + "," + data[4]).replace('"', "");
                del data[4];
            
            if(not data[6].isnumeric()):
                if(data[6].replace(".","").isdigit()):
                    data[6] = round(float(data[6])); # löytyy floateja integerejen sijaan...
                    continue;
                data[5] = (data[5] + "," + data[6]).replace('"', "");
                del data[6];
            
                if(data[6] == ""): data[6] = 0; # erikois-erikoistapaus: Aalto + puuttuva data

            if(len(data) == 7): # Virheellisen datan käsittely
                data[5] = data[5][:-1]; # poistaa pilkun virhedatassa
                data.append(data[6]);
                data[6] ="0"; # asettaa puuttuvan Covered distance -arvon nollaksi

            trips.append(
                {
                    "start_time": data[0],
                    "end_time": data[1],
                    "start_station_id": int(data[2]),
                    "end_station_id": int(data[4]),
                    "distance": round(float(data[6])), # joissakin on float-muotoista dataa
                    "duration": round(float(data[7]))
                }
            );

            stations[int(data[2])] = data[3];
            stations[int(data[4])] = data[5];

        f.close();


db = sqlite3.connect("bikes_2023.db");

db.execute("DROP TABLE IF EXISTS Trips");
db.execute("""CREATE TABLE Trips (
    id INTEGER PRIMARY KEY,
    start_time TEXT,
    end_time TEXT,
    start_station_id INTEGER REFERENCES Stations,
    end_station_id INTEGER REFERENCES Stations,
    distance INTEGER,
    duration INTEGER
);""");

db.execute("DROP TABLE IF EXISTS Stations");
db.execute("""CREATE TABLE Stations (
    id INTEGER PRIMARY KEY,
    name TEXT
);""");

# Stations
db.execute("BEGIN;");
for x in stations:
    db.execute("INSERT INTO Stations(id, name) VALUES(?, ?)", [x, stations[x]]);
db.execute("COMMIT;");

# Trips
db.execute("BEGIN;");
for x in trips:
    data = [x for x in x.values()];
    db.execute("INSERT INTO Trips(start_time, end_time, start_station_id, end_station_id, distance, duration) VALUES(?, ?, ?, ?, ?, ?);", data);
db.execute("COMMIT;");

if(__name__ == "__main__"):
    print(db.execute("SELECT COUNT(*) FROM Stations;").fetchone());
    print(db.execute("SELECT COUNT(*) FROM Trips;").fetchone());
    print(db.execute("SELECT * FROM Stations WHERE id = 100;").fetchone());
    print(db.execute("SELECT * FROM Trips WHERE id = 123456;").fetchone());