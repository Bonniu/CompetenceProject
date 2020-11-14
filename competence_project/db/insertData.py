import datetime

sql_persons = "INSERT INTO CP_database.persons (phone_number, profile) VALUES (%s, %s)"
sql_hotspots = "INSERT INTO CP_database.hotspots (name, description, x, y, type) VALUES (%s, %s, %s, %s, %s)"
sql_traces = "INSERT INTO CP_database.traces (user_id, hotspot_id, entry_time, exit_time) VALUES (%s, %s, %s, %s)"


def insert_persons(db_cursor):
    db_cursor.execute(sql_persons, (222333444, "student"))
    db_cursor.execute(sql_persons, (222333445, "student"))
    db_cursor.execute(sql_persons, (222333446, "student"))
    db_cursor.execute(sql_persons, (222333447, "student"))


def insert_hotspots(db_cursor):
    db_cursor.execute(sql_hotspots, ("ftims", "wydział ftims", 51.424, 55.333, "indoor"))
    db_cursor.execute(sql_hotspots, ("weeia", "weeia dla geja", 1.424, 5.333, "outdoor"))


def insert_traces(db_cursor):
    db_cursor.execute(sql_traces,
                      ("1", "1", datetime.datetime(2020, 5, 5, 13, 30, 13), None))
    db_cursor.execute(sql_traces,
                      ("2", "2", datetime.datetime(2020, 11, 5, 13, 30, 13),
                       datetime.datetime(2020, 11, 5, 13, 42, 13)))
    db_cursor.execute(sql_traces,
                      ("2", "1", datetime.datetime(2020, 11, 5, 13, 44, 17),
                       datetime.datetime(2020, 11, 5, 13, 56, 13)))
