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
