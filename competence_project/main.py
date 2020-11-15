from db.CRUD.hotspotCRUD import *
from db.CRUD.personCRUD import *
from db.CRUD.traceCRUD import *
from db.initDB import init_database

db_cursor, db = init_database()
#insert_person()
#select_person()
#delete_person()
#update_person()
#insert_hotspot()
#select_hotpost()
#delete_hotspot()
#update_hotspot()
#insert_trace()
#select_trace()
#delete_trace()

"""
db_cursor.execute("SELECT * FROM CP_database.persons")
print("persons: " + str(db_cursor.fetchall()))

db_cursor.execute("SELECT * FROM CP_database.hotspots")
print("hotspots: " + str(db_cursor.fetchall()))

db_cursor.execute("SELECT * FROM CP_database.traces")
print("traces: " + str(db_cursor.fetchall()))

print(Hotspot("hotspot_1", 1.232, 11.22))
print(User())
print(Trace("user_id", Hotspot("hotspot_1", 22.232, 11.22), 123, 123))
"""