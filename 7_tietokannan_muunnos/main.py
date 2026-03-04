import sqlite3, os;

# https://infopalvelut.storage.hsldev.com/citybikes/od-trips-2023/od-trips-2023.zip

files = os.listdir("od-trips-2023");
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

# Departure,Return,Departure station id,Departure station name,Return station id,Return station name,Covered distance (m),Duration (sec.)
#     0        1               2                     3                  4                   5                 6                  7                              
trips = [];
stations = {};


for file in files:
    with open(f'od-trips-2023/{file}') as f:
        next(f); # skip headers
        for i, line in enumerate(f):
            data = line.split(",");
            
            # Aalto-yliopisto yrittää niin pahasti olla erilainen et pitää sitä varten tehdä omat ehdot
            if(not data[4].isnumeric()):
                data[3] = (data[3] + "," + data[4]).replace('"', "");
                del data[4];
            
            if(not data[6].isnumeric()):
                data[5] = (data[5] + "," + data[6]).replace('"', "");
                del data[6];
            #  and not data[6].replace(".","").isdigit() # floatteja löytyy integerejen sijaan...
            try:
                trips.append(
                    {
                        "id": i,
                        "start_time": data[0],
                        "end_time": data[1],
                        "start_station_id": int(data[2]),
                        "end_station_id": int(data[4]),
                        "distance": int(float(data[6])),
                        "duration": int(float(data[7]))
                    }
                );
            except Exception as e:
                continue; # aineistossa on yllättävästi viallista tietoa, pitääpi varmistaa ohjaajilta miten toimia virhedatan kanssa...
            
            stations[int(data[2])] = data[3];
            stations[int(data[4])] = data[5];

        f.close();

# print(trips);
# print(stations);