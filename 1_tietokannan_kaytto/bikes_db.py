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

    def trips_during_weekday(self, day):
        pass;

    def most_popular_start_stations(self, limit):
        pass;

    def least_popular_start_stations(self, limit):
        pass;

    def largest_differences(self, limit):
        pass;
