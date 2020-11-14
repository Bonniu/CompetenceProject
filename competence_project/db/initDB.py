import mysql.connector

from db.insertData import insert_persons, insert_hotspots, insert_traces

db = mysql.connector.connect(
    host="localhost",
    user="root",  # można zmienić ale nie commitować
    password="admin"  # tu też
)

db_cursor = db.cursor()

db_cursor.execute("DROP DATABASE if exists CP_database")
db_cursor.execute("CREATE DATABASE if not exists CP_database")
db_cursor.execute("""
    create table if not exists CP_database.persons (
        id MEDIUMINT NOT NULL AUTO_INCREMENT,
        phone_number int NOT NULL,
        profile ENUM('student', 'teacher', 'staff'),
        PRIMARY KEY (id))
""")
db_cursor.execute("""
    create table if not exists CP_database.hotspots (
        id MEDIUMINT NOT NULL AUTO_INCREMENT,
        name varchar(32) NOT NULL,
        description varchar(255),
        x double NOT NULL,
        y double NOT NULL,
        type enum('indoor', 'outdoor'),
        PRIMARY KEY (id))
""")
db_cursor.execute("""
    create table if not exists CP_database.traces (
        user_id MEDIUMINT not null,
        FOREIGN KEY (user_id)
                REFERENCES persons(id)
                ON DELETE CASCADE,

        hotspot_id mediumint not null,   
        FOREIGN KEY (hotspot_id)
                REFERENCES hotspots(id)
                ON DELETE CASCADE,
        entry_time time,
        exit_time time)
""")

insert_persons(db_cursor, db)
insert_hotspots(db_cursor, db)
insert_traces(db_cursor, db)

db_cursor.execute("SELECT * FROM CP_database.persons")
print("persons: " + str(db_cursor.fetchall()))

db_cursor.execute("SELECT * FROM CP_database.hotspots")
print("hotspots: " + str(db_cursor.fetchall()))

db_cursor.execute("SELECT * FROM CP_database.traces")
print("traces: " + str(db_cursor.fetchall()))


