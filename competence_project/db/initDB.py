import mysql.connector

from db.databaseCredentials import get_database_credentials
from db.insertData import insert_persons, insert_hotspots, insert_traces


def init_database():
    credentials = get_database_credentials()
    db = mysql.connector.connect(
        host=credentials[0],
        user=credentials[1],
        password=credentials[2]
    )
    db_cursor = db.cursor()

    db_cursor.execute("DROP DATABASE if exists CP_database")
    db_cursor.execute("CREATE DATABASE if not exists CP_database")

    create_tables(db_cursor)

    insert_persons(db_cursor)
    insert_hotspots(db_cursor)
    insert_traces(db_cursor)
    db.commit()
    return db_cursor, db


def create_tables(db_cursor):
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
             id MEDIUMINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
             user_id MEDIUMINT not null,
             FOREIGN KEY (user_id)
                     REFERENCES persons(id)
                     ON DELETE CASCADE,

             hotspot_id mediumint not null,   
             FOREIGN KEY (hotspot_id)
                     REFERENCES hotspots(id)
                     ON DELETE CASCADE,
             entry_time datetime,
             exit_time datetime)
     """)


if __name__ == "__main__":
    init_database()
