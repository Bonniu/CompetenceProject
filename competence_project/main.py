from db.CRUD.hotspotCRUD import select_all_hotspots
from db.CRUD.personCRUD import select_all_persons
from db.CRUD.traceCRUD import select_all_traces
from db.initDB import init_database
from service import *
from service import initialize_hotspots

db_cursor, db = init_database()
hotspots = initialize_hotspots(150)
users = initialize_users(50)
# generate_traces_for_users(users, hotspots)

# plt.scatter(x1,y1, c='coral')
# plt.scatter(x2,y2, c='lightblue')
# plt.show()


# insert_person(db, db_cursor)
# select_person(db_cursor)
select_all_persons(db_cursor)
# delete_person(db, db_cursor)
# update_person(db, db_cursor)
# insert_hotspot(db, db_cursor)
# select_hotspot(db_cursor)
select_all_hotspots(db_cursor)
# delete_hotspot(db, db_cursor)
# update_hotspot(db, db_cursor)
# insert_trace(db, db_cursor)
# select_trace(db_cursor)
select_all_traces(db_cursor)
# delete_trace(db, db_cursor)
# update_trace(db, db_cursor)

# print(Hotspot("hotspot_1", 1.232, 11.22))
# print(Person(1, 2))
# print(Trace("user_id", Hotspot("hotspot_1", 22.232, 11.22), 123, 123))
