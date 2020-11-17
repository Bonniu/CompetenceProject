from db.CRUD.hotspotCRUD import *
from db.CRUD.personCRUD import *
from db.CRUD.traceCRUD import *
from db.initDB import init_database
from model.hotspot import Hotspot
from model.trace import Trace
from model.user import User

db_cursor, db = init_database()
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

print(Hotspot("hotspot_1", 1.232, 11.22))
print(User())
print(Trace("user_id", Hotspot("hotspot_1", 22.232, 11.22), 123, 123))
