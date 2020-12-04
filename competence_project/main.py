import time

from database.dbImport import DbImport
from database.initDB import connect_to_mysql, reset_database
from database.repository.HotspotRepository import HotspotRepository
from service import *


def generate_data(nr_of_hotspots=200, nr_of_persons=100):
    before = time.time()
    reset_database(db_cursor, db)  # drop and create database
    hotspots = initialize_hotspots(nr_of_hotspots)
    HotspotRepository.insert_hotspots(db, db_cursor, hotspots)
    persons = initialize_persons(nr_of_persons)
    PersonRepository.insert_persons(db, db_cursor, persons)
    generate_traces_for_persons(persons, hotspots, db, db_cursor)
    after = time.time()
    print("Data generated in " + str(after - before) + "s.")


def load_data_from_files_to_db():
    reset_database(db_cursor, db)  # drop and create database
    DbImport.read_persons(db, db_cursor)
    DbImport.read_hotspots(db, db_cursor)
    DbImport.read_traces(db, db_cursor)


########################################################################################################################
# TODO czasami po uruchomieniu programu wywala błąd:
#  mysql.connector.errors.IntegrityError: 1452 (23000): Cannot add or update a child row: a foreign key constraint fails
#  dzieje sie tak jak inserty nie zdążą dodać do bazy person/insert, a potem jest próba dodania trace
#  workaround:     wystarczy jeszcze raz odpalić program
########################################################################################################################
# śmietnik #############################################################################################################


# h1000 p200 = 81086 -> 4MB
# h300  p50 = 20319 ->  1MB
# h100 p20 = 7967 -> 0.4MB

#
# for i in HotspotRepository.select_hotspots_by_key(db_cursor, "description", "park"):
#     print(i)
# for i in HotspotRepository.select_all_hotspots(db_cursor):
#     print(i)
# print(HotspotRepository.select_hotspot_by_id(db_cursor, 12))
#
# for i in PersonRepository.select_persons_by_key(db_cursor, "profile", "cook"):
#     print(i)
# for i in PersonRepository.select_all_persons(db_cursor):
#     print(i)
# print(PersonRepository.select_person_by_id(db_cursor, 12))


# TraceRepository.insert_traces(db, db_cursor, [Trace(1, 1, datetime.datetime(2020, 4, 5, 14, 20, 53), datetime.datetime(2020, 4, 5, 15, 20, 53)),
#                                               Trace(1, 2, datetime.datetime(2020, 5, 6, 13, 30, 13), datetime.datetime(2020, 5, 6, 14, 30, 13)),
#                                               Trace(2, 2, datetime.datetime(2021, 5, 6, 13, 30, 13),
#                                                     datetime.datetime(2021, 5, 7, 13, 30, 13))])


# calculate_longest_route(db, db_cursor)
# plt.scatter(x1, y1, c='coral')
# plt.scatter(x2, y2, c='lightblue')
# plt.show()

# for dict1 in calculate_length_of_stay(db_cursor):
#     print(dict1)

########################################################################################################################


if __name__ == "__main__":
    flag = False
    answer = input("Whether to use data from file? (y/n):")
    
    if answer == "y" or answer == "Y":
        db_cursor, db = connect_to_mysql()
        load_data_from_files_to_db()
        db.close()
    elif answer == "n" or answer == "N":
        db_cursor, db = connect_to_mysql()
        hotspots = input("Number of hotspots: ")
        people = input("Number of people: ")
        generate_data(int(hotspots), int(people))
        db.close()
