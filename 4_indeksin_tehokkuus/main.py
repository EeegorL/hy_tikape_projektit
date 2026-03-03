import sqlite3, random, string, os;
from time import time;

drop = "DROP TABLE IF EXISTS Movies;";
create = "CREATE TABLE Movies(id INT PRIMARY KEY, name VARCHAR(255), release_year INT);";
insert = "INSERT INTO Movies VALUES(?, ?, ?);";
select = "SELECT COUNT(*) FROM Movies WHERE release_year = ?;";

def test1():
    db = sqlite3.connect("t1.sql");
    db.execute("BEGIN;");
    db.execute(drop);
    
    db.execute(create);

    rowAddStart = time();
    for i in range(0, 10**6):
        randName = "".join([random.choice(string.ascii_lowercase) for i in range(0, 8)]);
        randYear = random.randint(1900, 2000);
        db.execute(insert, [i, randName, randYear]);
    rowAddEnd = time();

    queryStart = time();
    for i in range(0, 10**3):
        randYear = random.randint(1900, 2000);
        db.execute(select, [randYear]);
    queryEnd = time();

    fileSize = os.path.getsize("./t1.sql");
    db.execute("COMMIT;");
    return (
        f'{round(rowAddEnd - rowAddStart)}s',
        f'{round(queryEnd - queryStart)}s',
        f'{round(fileSize / 10**6)} Mb'
    );

def test2():
    db = sqlite3.connect("t2.sql");
    db.execute("BEGIN;");
    index = "CREATE INDEX year ON Movies(release_year);";
    db.execute(drop);
    
    db.execute(create);
    db.execute(index);

    rowAddStart = time();
    for i in range(0, 10**6):
        randName = "".join([random.choice(string.ascii_lowercase) for i in range(0, 8)]);
        randYear = random.randint(1900, 2000);
        db.execute(insert, [i, randName, randYear]);
    rowAddEnd = time();

    queryStart = time();
    for i in range(0, 10**3):
        randYear = random.randint(1900, 2000);
        db.execute(select, [randYear]);
    queryEnd = time();

    fileSize = os.path.getsize("./t2.sql");
    db.execute("COMMIT;");
    return (
        f'{round(rowAddEnd - rowAddStart)}s',
        f'{round(queryEnd - queryStart)}s',
        f'{round(fileSize / 10**6)} Mb'
    );

def test3():
    db = sqlite3.connect("t3.sql");
    db.execute("BEGIN;");
    index = "CREATE INDEX year ON Movies(release_year);";
    db.execute(drop);
    
    db.execute(create);

    rowAddStart = time();
    for i in range(0, 10**6):
        randName = "".join([random.choice(string.ascii_lowercase) for i in range(0, 8)]);
        randYear = random.randint(1900, 2000);
        db.execute(insert, [i, randName, randYear]);
    rowAddEnd = time();

    db.execute(index);
    queryStart = time();
    for i in range(0, 10**3):
        randYear = random.randint(1900, 2000);
        db.execute(select, [randYear]);
    queryEnd = time();
    db.execute("COMMIT;");
    fileSize = os.path.getsize("./t3.sql");
    
    return (
        f'{round(rowAddEnd - rowAddStart)}s',
        f'{round(queryEnd - queryStart)}s',
        f'{round(fileSize / 10**6)} Mb'
    );

print(test1());
print(test2());
print(test3());