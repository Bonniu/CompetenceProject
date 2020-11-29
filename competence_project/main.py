from database.initDB import init_database
from database.repository.HotspotRepository import HotspotRepository
from database.repository.PersonRepository import PersonRepository
from service import *
from service import initialize_hotspots

db_cursor, db = init_database()

hotspots = initialize_hotspots(3)
HotspotRepository.insert_hotspots(db, db_cursor, hotspots)

persons = initialize_persons(10)
PersonRepository.insert_persons(db, db_cursor, persons)
########################################################################################################################
# TODO czasami po uruchomieniu programu wywala błąd:
#  mysql.connector.errors.IntegrityError: 1452 (23000): Cannot add or update a child row: a foreign key constraint fails
#  dzieje sie tak jak inserty nie zdążą dodać do bazy person/insert, a potem jest próba dodania trace
#  workaround:     wystarczy jeszcze raz odpalić program
########################################################################################################################
# śmietnik #############################################################################################################

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


TraceRepository.insert_traces(db, db_cursor, [Trace(1, 1, datetime.datetime(2020, 9, 5, 14, 20, 53), datetime.datetime(2021, 2, 7, 13, 30, 13)),
                                               Trace(1, 2, datetime.datetime(2020, 5, 6, 13, 30, 13), datetime.datetime(2021, 4, 7, 13, 30, 13)),
                                               Trace(2, 2, datetime.datetime(2021, 5, 6, 13, 30, 13), datetime.datetime(2021, 5, 7, 13, 30, 13)),
                                              Trace(1, 3, datetime.datetime(2020, 7, 6, 13, 30, 13),datetime.datetime(2021, 4, 7, 13, 30, 13)),
                                              Trace(1, 2, datetime.datetime(2020, 8, 6, 13, 30, 13),datetime.datetime(2021, 4, 7, 13, 30, 13))])
#
# for trace in TraceRepository.select_traces_for_ids(db_cursor, None, None):
#     print(trace)

#generate_traces_for_persons(persons, hotspots, db, db_cursor)
calculate_longest_route(db_cursor)
# plt.scatter(x1, y1, c='coral')
# plt.scatter(x2, y2, c='lightblue')
# plt.show()

########################################################################################################################
db.close()
