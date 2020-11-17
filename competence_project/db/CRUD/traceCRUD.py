import datetime


def insert_trace(db, db_cursor):
    user = input("UserID: ")
    hotspot = input("HotspotID: ")
    time = datetime.datetime.now()
    exit_time = input("Time of exit(YYYY-MM-DD hh:mm:ss): ")
    d = datetime.datetime.strptime(exit_time, "%Y-%m-%d %H:%M:%S")
    d.strftime("YYYY-MM-DD HH:mm:ss (%Y%m%d %H:%M:%S)")

    query = "INSERT INTO CP_database.traces (user_id,hotspot_id,entry_time,exit_time) VALUES (%s, %s, %s, %s)"
    print(query)
    db_cursor.execute(query, (user, hotspot, time, d))
    db.commit()


def select_trace(db_cursor):
    query = ""
    column = input("Search by traceID/userID/hotspotID: ")
    if column == "traceID":
        select = input("TraceID: ")
        query = "SELECT * FROM CP_database.traces WHERE id=" + select
    elif column == "userID":
        select = input("UserID: ")
        query = "SELECT * FROM CP_database.traces WHERE user_id=" + select
    elif column == "hotspotID":
        select = input("HotspotID: ")
        query = "SELECT * FROM CP_database.traces WHERE hotspot_id=" + select

    print(query)
    db_cursor.execute(query)
    result = db_cursor.fetchall()

    for x in result:
        print(x)


def select_all_traces(db_cursor):
    query = "SELECT * FROM CP_database.traces"
    print(query)
    db_cursor.execute(query)
    result = db_cursor.fetchall()

    for x in result:
        print(x)


def delete_trace(db, db_cursor):
    query = ""
    column = input("Delete traces by userID/hotspotID: ")
    if column == "userID":
        delete = input("UserID: ")
        query = "DELETE FROM CP_database.traces WHERE user_id=" + delete
    elif column == "hotspotID":
        delete = input("HotspotID: ")
        query = "DELETE FROM CP_database.traces WHERE hotspot_id=" + delete

    print(query)
    db_cursor.execute(query)
    db.commit()

    print(db_cursor.rowcount, "record(s) deleted")


def update_trace(db, db_cursor):
    query = ""
    which = input("Trace ID: ")
    column = input("Which column should be updated(userID/hotspotID/entryTime/exitTime): ")
    if column == "userID":
        user = input("New userID: ")
        query = "UPDATE CP_database.traces SET user_id = " + user + " WHERE id = " + which
    elif column == "hotspotID":
        hotspot = input("New hotspotID: ")
        query = "UPDATE CP_database.traces SET hotspot_id = '" + hotspot + "' WHERE id = " + which
    elif column == "entryTime":
        time = input("Time of entry(YYYY-MM-DD hh:mm:ss): ")
        query = "UPDATE CP_database.traces SET entry_time = '" + time + "' WHERE id = " + which
    elif column == "exitTime":
        time = input("Time of exit(YYYY-MM-DD hh:mm:ss): ")
        query = "UPDATE CP_database.traces SET exit_time = '" + time + "' WHERE id = " + which

    print(query)
    db_cursor.execute(query)
    db.commit()

    print(db_cursor.rowcount, "record(s) updated")
