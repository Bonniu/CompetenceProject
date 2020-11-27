from model.hotspot import Hotspot


class HotspotRepository:

    @staticmethod
    def insert_hotspot(db, db_cursor, hotspot: Hotspot):
        query = "INSERT INTO CP_database.hotspots (x, y, name, description, type) VALUES (%s, %s, %s, %s, %s)"
        type_ = "outdoor"
        if not hotspot.outdoor:
            type_ = "indoor"
        db_cursor.execute(query, (hotspot.x, hotspot.y, hotspot.name, hotspot.description, type_))
        db.commit()
        hotspot.id = db_cursor.lastrowid
        return hotspot

    @staticmethod
    def insert_hotspots(db, db_cursor, hotspots: []):
        for hotspot in hotspots:
            HotspotRepository.insert_hotspot(db, db_cursor, hotspot)
        db.commit()

    @staticmethod
    def select_hotspot_by_id(db_cursor, id_) -> Hotspot:
        db_cursor.execute("SELECT * FROM CP_database.hotspots WHERE id=%s" % id_)
        return HotspotRepository.get_hotspot_from_result(db_cursor.fetchall()[0])

    @staticmethod
    def select_all_hotspots(db_cursor) -> []:
        db_cursor.execute("SELECT * FROM CP_database.hotspots")
        hotspots = []
        for result_hotspot in db_cursor.fetchall():
            hotspots.append(HotspotRepository.get_hotspot_from_result(result_hotspot))
        return hotspots

    @staticmethod
    def select_hotspots_by_key(db_cursor, key_name: str, value) -> []:
        query = "SELECT * FROM CP_database.hotspots WHERE " + key_name + " = '%s'" % value
        db_cursor.execute(query)
        hotspots = []
        for result_hotspot in db_cursor.fetchall():
            hotspots.append(HotspotRepository.get_hotspot_from_result(result_hotspot))
        return hotspots

    @staticmethod
    def get_hotspot_from_result(result) -> Hotspot:
        # 0id 1name 2description 3x 4y 5outdoor
        outdoor_boolean = True
        if result[5] == "indoor":
            outdoor_boolean = False
        hotspot = Hotspot(result[3], result[4], outdoor=outdoor_boolean)
        hotspot.id = result[0]
        hotspot.name = result[1]
        hotspot.description = result[2]
        return hotspot
