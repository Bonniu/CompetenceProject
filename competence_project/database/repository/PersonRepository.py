from model.person import Person


class PersonRepository:

    @staticmethod
    def insert_person(db, db_cursor, person: Person):
        query = "INSERT INTO CP_database.persons (phone_number, profile, interests) VALUES (%s, %s, %s)"
        db_cursor.execute(query, (person.phone_number, person.profile, person.interests))
        db.commit()
        person.id = db_cursor.lastrowid
        return person

    @staticmethod
    def insert_persons(db, db_cursor, persons: []):
        for person in persons:
            PersonRepository.insert_person(db, db_cursor, person)
