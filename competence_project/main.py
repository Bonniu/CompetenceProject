from database.CRUD.hotspotCRUD import select_all_hotspots
from database.CRUD.personCRUD import select_all_persons
from database.CRUD.traceCRUD import select_all_traces
from database.initDB import init_database
from database.repository.HotspotRepository import HotspotRepository
from database.repository.PersonRepository import PersonRepository
from database.repository.TraceRepository import TraceRepository
from service import *
from service import initialize_hotspots

db_cursor, db = init_database()
hotspots = initialize_hotspots(150)
persons = initialize_persons(50)
# print(persons[0])

HotspotRepository.insert_hotspots(db, db_cursor, hotspots)
PersonRepository.insert_persons(db, db_cursor, persons)
TraceRepository.insert_traces(db, db_cursor, [Trace(1, 1, datetime.datetime(2020, 5, 5, 13, 30, 13), None),
                                              Trace(1, 1, datetime.datetime(2020, 5, 5, 13, 30, 13), None)])

select_all_hotspots(db_cursor)
select_all_persons(db_cursor)
select_all_traces(db_cursor)
# traceRepository.insert_trace(Trace(1, 1, 22.232, 11.22))

# generate_traces_for_persons(persons, hotspots)

# plt.scatter(x1, y1, c='coral')
# plt.scatter(x2, y2, c='lightblue')
# plt.show()

# print(Hotspot("hotspot_1", 1.232, 11.22))
# print(Person(1, 2))
# print(Trace("user_id", Hotspot("hotspot_1", 22.232, 11.22), 123, 123))

db.close()
