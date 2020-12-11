class PairedHotspotsRepository:

    class PairedHotspots:
        def __init__(self, first_hotspot_name, second_hotspot_name, cnt):
            self.first_hotspot_name = first_hotspot_name 
            self.second_hotspot_name = second_hotspot_name
            self.cnt = cnt

    @staticmethod
    def select_all_records(db_cursor) -> []:
        db_cursor.execute(
            'SELECT  h1.name as source '
            +'		,h2.name as target '
            +'		,COUNT(h_id2) as ile '
            +'FROM ( '
            +'	SELECT '
            +'		t1.id id,t1.user_id u_id '
            +'		,t1.hotspot_id h_id1 '
            +'		,Date(t1.entry_time) entry_t,Date(t1.exit_time) exit_t '
            +'		,t2.hotspot_id as h_id2 '
            +'	FROM CP_database.traces t1 '
            +'	INNER JOIN CP_database.traces t2 '
            +'	ON t1.id = t2.id-1 '
            +'	WHERE 1=1 '
            +'	ORDER BY t2.id asc '
            +') der '
            +'INNER JOIN CP_database.hotspots h1 ON h_id1 = h1.id '
            +'INNER JOIN CP_database.hotspots h2 ON h_id2 = h2.id '
            +'WHERE der.id NOT IN ( '
            +'	SELECT MAX(id) '
            +'	FROM CP_database.traces '
            +'	GROUP BY user_id, DATE(entry_time) '
            +') '
            +'GROUP BY h_id1,h_id2 '
            +'ORDER BY h_id1, ile desc '
            )
        records = []
        for res in db_cursor.fetchall():
            records.append(PairedHotspotsRepository.get_record_from_result(res))
        return records

    @staticmethod
    def get_record_from_result(res) -> PairedHotspots:
        return PairedHotspotsRepository.PairedHotspots(res[0],res[1],res[2])