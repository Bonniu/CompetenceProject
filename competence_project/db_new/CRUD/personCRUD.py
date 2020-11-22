import mysql.connector

from competence_project.db_new.databaseCredentials import get_database_credentials


def insert_person():
    phone = input("Phone number: ")
    profile = input("Profile: ")

    credentials = get_database_credentials()
    db = mysql.connector.connect(
        host=credentials[0],
        user=credentials[1],
        password=credentials[2]
    )
    db_cursor = db.cursor()

    query = "INSERT INTO CP_database.persons (phone_number, profile) VALUES (%s, %s)"
    print(query)
    db_cursor.execute(query, (phone, profile))
    db.commit()
    db.close()


def select_person():
    credentials = get_database_credentials()
    db = mysql.connector.connect(
        host=credentials[0],
        user=credentials[1],
        password=credentials[2]
    )
    db_cursor = db.cursor()

    select = input("ID: ")
    query = "SELECT * FROM CP_database.persons WHERE id="+select
    print(query)
    db_cursor.execute(query)
    result = db_cursor.fetchall()
    db.close()
    for x in result:
        print(x)


def select_all_persons():
    credentials = get_database_credentials()
    db = mysql.connector.connect(
        host=credentials[0],
        user=credentials[1],
        password=credentials[2]
    )
    db_cursor = db.cursor()

    query = "SELECT * FROM CP_database.persons"
    print(query)
    db_cursor.execute(query)
    result = db_cursor.fetchall()
    db.close()
    for x in result:
        print(x)


def delete_person():
    credentials = get_database_credentials()
    db = mysql.connector.connect(
        host=credentials[0],
        user=credentials[1],
        password=credentials[2]
    )
    db_cursor = db.cursor()

    delete = input("ID: ")
    query = "DELETE FROM CP_database.persons WHERE id="+delete
    print(query)
    db_cursor.execute(query)
    db.commit()
    db.close()
    print(db_cursor.rowcount, "record(s) deleted")


def update_person():
    credentials = get_database_credentials()
    db = mysql.connector.connect(
        host=credentials[0],
        user=credentials[1],
        password=credentials[2]
    )
    db_cursor = db.cursor()
    which = input("Person ID: ")
    column = input("Which column should be updated(phone/profile): ")
    if column == "phone":
        phone = input("New Phone Number: ")
        query = "UPDATE CP_database.persons SET phone_number = " + phone + " WHERE id = " + which
    elif column == "profile":
        person = input("New profile: ")
        query = "UPDATE CP_database.persons SET profile = '" + person + "' WHERE id = " + which

    print(query)
    db_cursor.execute(query)
    db.commit()
    db.close()
    print(db_cursor.rowcount, "record(s) updated")
