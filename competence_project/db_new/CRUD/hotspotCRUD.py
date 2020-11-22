import mysql.connector

from competence_project.db_new.databaseCredentials import get_database_credentials


def insert_hotspot():
    name = input("Name: ")
    description = input("Description: ")
    x = input("X: ")
    y = input("Y: ")
    typeOfHotspot = input("Type of hotspot: ")

    credentials = get_database_credentials()
    db = mysql.connector.connect(
        host=credentials[0],
        user=credentials[1],
        password=credentials[2]
    )
    db_cursor = db.cursor()

    query = "INSERT INTO CP_database.hotspots (name, description, x, y, type) VALUES (%s, %s, %s, %s, %s)"
    print(query)
    db_cursor.execute(query, (name, description, x, y, typeOfHotspot))
    db.commit()
    db.close()


def select_hotpost():
    credentials = get_database_credentials()
    db = mysql.connector.connect(
        host=credentials[0],
        user=credentials[1],
        password=credentials[2]
    )
    db_cursor = db.cursor()

    select = input("ID: ")
    query = "SELECT * FROM CP_database.hotspots WHERE id=" + select
    print(query)
    db_cursor.execute(query)
    result = db_cursor.fetchall()
    db.close()
    for x in result:
        print(x)


def select_all_hotposts():
    credentials = get_database_credentials()
    db = mysql.connector.connect(
        host=credentials[0],
        user=credentials[1],
        password=credentials[2]
    )
    db_cursor = db.cursor()

    query = "SELECT * FROM CP_database.hotspots"
    print(query)
    db_cursor.execute(query)
    result = db_cursor.fetchall()
    db.close()
    for x in result:
        print(x)


def delete_hotspot():
    credentials = get_database_credentials()
    db = mysql.connector.connect(
        host=credentials[0],
        user=credentials[1],
        password=credentials[2]
    )
    db_cursor = db.cursor()

    delete = input("ID: ")
    query = "DELETE FROM CP_database.hotspots WHERE id=" + delete
    print(query)
    db_cursor.execute(query)
    db.commit()
    db.close()
    print(db_cursor.rowcount, "record(s) deleted")


def update_hotspot():
    credentials = get_database_credentials()
    db = mysql.connector.connect(
        host=credentials[0],
        user=credentials[1],
        password=credentials[2]
    )
    db_cursor = db.cursor()
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
    db.close()
    print(db_cursor.rowcount, "record(s) updated")
