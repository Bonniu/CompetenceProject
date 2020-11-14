from db.initDB import init_database
from model.hotspot import Hotspot
from model.trace import Trace
from model.user import User

db_cursor, db = init_database()

db_cursor.execute("SELECT * FROM CP_database.persons")
print("persons: " + str(db_cursor.fetchall()))

db_cursor.execute("SELECT * FROM CP_database.hotspots")
print("hotspots: " + str(db_cursor.fetchall()))

db_cursor.execute("SELECT * FROM CP_database.traces")
print("traces: " + str(db_cursor.fetchall()))

print(Hotspot("hotspot_1", 1.232, 11.22))
print(User())
print(Trace("user_id", Hotspot("hotspot_1", 22.232, 11.22), 123, 123))
