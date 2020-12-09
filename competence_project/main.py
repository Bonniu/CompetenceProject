import time

from database.dbImport import DbImport
from database.initDB import connect_to_mysql, reset_database
from database.repository.HotspotRepository import HotspotRepository
from service import *

import analyzer

def generate_data(nr_of_hotspots=200, nr_of_persons=100, CITY_CENTRE_X=51.759046,
                  CITY_CENTRE_Y=19.458062, MIN_DISTANCE=0.0005, MAX_DISTANCE=0.08):
    before = time.time()
    reset_database(db_cursor, db)  # drop and create database
    hotspots = initialize_hotspots(nr_of_hotspots, CITY_CENTRE_X, CITY_CENTRE_Y, MIN_DISTANCE, MAX_DISTANCE)
    HotspotRepository.insert_hotspots(db, db_cursor, hotspots)
    persons = initialize_persons(nr_of_persons, CITY_CENTRE_X, CITY_CENTRE_Y, MIN_DISTANCE, MAX_DISTANCE)
    PersonRepository.insert_persons(db, db_cursor, persons)
    generate_traces_for_persons(persons, hotspots, db, db_cursor)
    after = time.time()
    print("Data generated in " + str(after - before) + "s.")


def load_data_from_files_to_db(size_of_data_: str = "small"):
    print("Importing data...")
    reset_database(db_cursor, db)  # drop and create database
    DbImport.read_persons(db, db_cursor, size_of_data_)
    DbImport.read_hotspots(db, db_cursor, size_of_data_)
    DbImport.read_traces(db, db_cursor, size_of_data_)
    print("Importing data done.")


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

def get_size_of_data_from_user():
    size_flag = None
    dict_ = {"s": "small", "m": "medium", "l": "large"}
    size_input = ""
    while not size_flag:
        if dict_.keys().__contains__(size_input):
            size_flag = True
        else:
            size_input = input("Size of data to import (s/m/l): ")
    return dict_[size_input]

if __name__ == "__main__":

    db_cursor, db = connect_to_mysql()
    analyze_mode = ''
    while not (analyze_mode and analyze_mode.lower() in ['y', 'n']):
        analyze_mode = input('Want to analyze? (y/n)')
        if analyze_mode.lower() == 'y':
            analyzer.analyze(
                HotspotRepository.select_all_hotspots(db_cursor)
                ,PersonRepository.select_all_persons(db_cursor)
                ,TraceRepository.select_all_traces(db_cursor)
            )
    
    flag = False
    answerFile = None
    while not flag:
        if answerFile == 'y' or answerFile == 'Y' or answerFile == 'n' or answerFile == 'N':
            flag = True
        else:
            answerFile = input("Whether to use data from file? (y/n):")

    size_of_data_input = None

    if answerFile == "n" or answerFile == "n":
        answerParam = ""
        flag = False
        while not flag:
            if answerParam == 'y' or answerParam == 'Y' or answerParam == 'n' or answerParam == 'N':
                flag = True
            else:
                answerParam = input("Whether to use default parameters? (y/n):")

    if answerFile == "y" or answerFile == "Y":
        size_of_data = get_size_of_data_from_user()
        load_data_from_files_to_db(size_of_data)
    elif answerFile == "n" or answerFile == "N":
        if answerParam == "y" or answerParam == "Y":
            hotspots_ = input("Number of hotspots: ")
            people = input("Number of people: ")
            generate_data(int(hotspots_), int(people), 51.759046, 19.458062, 0.0005, 0.08)
        elif answerParam == "n" or answerParam == "N":
            hotspots_ = input("Number of hotspots: ")
            people = input("Number of people: ")
            centerX = input("Coordinates of the center X:")
            centerY = input("Coordinates of the center Y:")
            minDist = input("Minimal distance between hotspots:")
            maxDist = input("Maximal distance between hotspots:")
            generate_data(int(hotspots_), int(people), float(centerX), float(centerY), float(minDist), float(maxDist))

    db.close()
