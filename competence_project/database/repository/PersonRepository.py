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
        db.commit()

    @staticmethod
    def select_all_persons(db_cursor) -> []:
        db_cursor.execute("SELECT * FROM CP_database.persons")
        persons = []
        for result_person in db_cursor.fetchall():
            persons.append(PersonRepository.get_person_from_result(result_person))
        return persons

    @staticmethod
    def select_person_by_id(db_cursor, id_) -> Person:
        db_cursor.execute("SELECT * FROM CP_database.persons WHERE id=%s" % id_)
        return PersonRepository.get_person_from_result(db_cursor.fetchall()[0])

    @staticmethod
    def select_persons_by_key(db_cursor, key_name: str, value) -> []:
        query = "SELECT * FROM CP_database.persons WHERE " + key_name + " = '%s'" % value
        db_cursor.execute(query)
        persons = []
        for result_person in db_cursor.fetchall():
            persons.append(PersonRepository.get_person_from_result(result_person))
        return persons

    @staticmethod
    def get_person_from_result(result) -> Person:
        # 0id 1phone_number 2profile 3interests
        person = Person(0.0, 0.0)
        person.id = result[0]
        person.phone_number = result[1]
        person.profile = result[2]
        person.interests = result[3]
        return person
