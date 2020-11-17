def insert_person(db, db_cursor):
    phone = input("Phone number: ")
    profile = input("Profile: ")
    query = "INSERT INTO CP_database.persons (phone_number, profile) VALUES (%s, %s)"
    print(query)
    db_cursor.execute(query, (phone, profile))
    db.commit()


def select_person(db_cursor):
    select = input("ID: ")
    query = "SELECT * FROM CP_database.persons WHERE id=" + select
    print(query)
    db_cursor.execute(query)
    result = db_cursor.fetchall()
    for x in result:
        print(x)


def select_all_persons(db_cursor):
    query = "SELECT * FROM CP_database.persons"
    print(query)
    db_cursor.execute(query)
    result = db_cursor.fetchall()
    for x in result:
        print(x)


def delete_person(db, db_cursor):
    delete = input("ID: ")
    query = "DELETE FROM CP_database.persons WHERE id=" + delete
    print(query)
    db_cursor.execute(query)
    db.commit()
    print(db_cursor.rowcount, "record(s) deleted")


def update_person(db, db_cursor):
    query = ""
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
    print(db_cursor.rowcount, "record(s) updated")
