import sqlite3;

class Bikes:
    def __init__(self):
        self.db = sqlite3.connect("bikes_2024.db");

    def trips_from_station(self, station_name):
        query = f"""
            SELECT COUNT(T.id) FROM Trips T
            JOIN Stations S ON S.id = T.start_station_id
            WHERE S.name = ?
        """;
        return self.db.execute(query, [station_name]).fetchone()[0];

    def trips_to_station(self, station_name):
        query = f"""
            SELECT COUNT(T.id) FROM Trips T
            JOIN Stations S ON S.id = T.end_station_id
            WHERE S.name = ?
        """;
        return self.db.execute(query, [station_name]).fetchone()[0];

    def longest_distance_trips(self, limit):
        query = f"""
            SELECT A.name, B.name, T.distance FROM Trips T
            INNER JOIN Stations A ON A.id = T.start_station_id
            INNER JOIN Stations B ON B.id = T.end_station_id
            GROUP BY T.id
            ORDER BY T.distance DESC
            LIMIT ?;
        """;
        return self.db.execute(query, [limit]).fetchall();

    def longest_duration_trips(self, limit):
        query = f"""
            SELECT A.name, B.name, T.duration FROM Trips T
            INNER JOIN Stations A ON A.id = T.start_station_id
            INNER JOIN Stations B ON B.id = T.end_station_id
            ORDER BY T.duration DESC
            LIMIT ?;
        """;
        return self.db.execute(query, [limit]).fetchall();

    def trips_during_month(self, month):
        months = {
            "01": "Tammikuu",
            "02": "Helmikuu",
            "03": "Maaliskuu",
            "04": "Huhtikuu",
            "05": "Toukokuu",
            "06": "Kesäkuu",
            "07": "Heinäkuu",
            "08": "Elokuu",
            "09": "Syyskuu",
            "10": "Lokakuu",
            "11": "Marraskuu",
            "12": "Joulukuu"
            };
        month = str(month) if month > 9 else f"0{month}";
    
        query = f"""
            SELECT COUNT(*) FROM Trips T
            WHERE T.start_time LIKE ?
        """;
        result = self.db.execute(query, [f"%-{month}-%"]).fetchone();
        return (months[month], result[0]);

    def trips_during_weekday(self, day): # https://sqlite.org/lang_datefunc.html
        if(day == 7): day = 0; # "Tässä 1 = maanantai, 2 = tiistai, jne." ei ole kovin kuvaava, sillä ei selviä onko sunnuntai 0 vai 7. Oletetaan, että käyttäjä syöttäisi 7:n
        days = {
            1: "Maanantai",
            2: "Tiistai",
            3: "Keskiviikko",
            4: "Torstai",
            5: "Perjantai",
            6: "Lauantai",
            0: "Sunnuntai"
        };

        query = """
            SELECT COUNT(*) FROM Trips T
            WHERE STRFTIME('%w', T.start_time) = ?;
        """;
        result = self.db.execute(query, [str(day)]).fetchone();
        return (days[day], result[0])

    def most_popular_start_stations(self, limit):
        query = """
            SELECT S.name, COUNT(T.id) AS x FROM Stations S
            INNER JOIN Trips T ON S.id = T.start_station_id
            GROUP BY S.id
            ORDER BY x DESC
            LIMIT ?;
        """;
        return self.db.execute(query, [limit]).fetchall();

    def least_popular_start_stations(self, limit):
        query = """
            SELECT S.name, COUNT(T.id) AS n FROM Stations S
            INNER JOIN Trips T ON S.id = T.start_station_id
            GROUP BY S.id
            ORDER BY n ASC
            LIMIT ?;
        """;
        return self.db.execute(query, [limit]).fetchall();

    def largest_differences(self, limit):
        # alussa IFNULLit siltä varalta, että jollakin asemalla ei ole ollut minkäänlaista liikettä (epätodennäköistä), niin null muuttuu nollaksi
        query = """ 
            SELECT S.name, IFNULL(A.c, 0), IFNULL(B.c, 0), ABS(IFNULL(A.c, 0) - IFNULL(B.c, 0))) AS diff
            FROM Stations S
            LEFT JOIN (
                SELECT start_station_id, COUNT(*) AS c FROM Trips
                GROUP BY start_station_id
            ) A ON A.start_station_id = S.id
            LEFT JOIN ( 
                SELECT end_station_id, COUNT(*) AS c FROM Trips
                GROUP BY end_station_id
            ) B ON B.end_station_id = S.id
            ORDER BY diff DESC
            LIMIT ?;
        """;
        return self.db.execute(query, [limit]).fetchall();

if(__name__ == "__main__"):
    db = Bikes();

    print(db.largest_differences(5))