def insert_hotspot(db, db_cursor):
    name = input("Name: ")
    description = input("Description: ")
    x = input("X: ")
    y = input("Y: ")
    type_of_hotspot = input("Type of hotspot: ")
    query = "INSERT INTO CP_database.hotspots (name, description, x, y, type) VALUES (%s, %s, %s, %s, %s)"
    print(query)
    db_cursor.execute(query, (name, description, x, y, type_of_hotspot))
    db.commit()


def select_hotspot(db_cursor):
    select = input("ID: ")
    query = "SELECT * FROM CP_database.hotspots WHERE id=" + select
    print(query)
    db_cursor.execute(query)
    result = db_cursor.fetchall()
    for x in result:
        print(x)


def select_all_hotspots(db_cursor):
    query = "SELECT * FROM CP_database.hotspots"
    print(query)
    db_cursor.execute(query)
    result = db_cursor.fetchall()
    for x in result:
        print(x)


def delete_hotspot(db, db_cursor):
    delete = input("ID: ")
    query = "DELETE FROM CP_database.hotspots WHERE id=" + delete
    print(query)
    db_cursor.execute(query)
    db.commit()
    print(db_cursor.rowcount, "record(s) deleted")


def update_hotspot(db, db_cursor):
    query = ""
    which = input("Hotspot ID: ")
    column = input("Which column should be updated(name/description/x/y/type): ")
    if column == "name":
        name = input("New hotspot name: ")
        query = "UPDATE CP_database.hotspots SET name = " + name + " WHERE id = " + which
    elif column == "description":
        description = input("New description: ")
        query = "UPDATE CP_database.hotspots SET profile = '" + description + "' WHERE id = " + which
    elif column == "x":
        x = input("New x coord: ")
        query = "UPDATE CP_database.hotspots SET x = '" + x + "' WHERE id = " + which
    elif column == "y":
        y = input("New y coord: ")
        query = "UPDATE CP_database.hotspots SET y = '" + y + "' WHERE id = " + which
    elif column == "type":
        type = input("New type: ")
        query = "UPDATE CP_database.hotspots SET type = '" + type + "' WHERE id = " + which

    print(query)
    db_cursor.execute(query)
    db.commit()
    print(db_cursor.rowcount, "record(s) updated")
