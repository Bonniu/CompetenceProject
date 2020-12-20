class ClusterRepository:

    class Cluster:
        def __init__(self, hotspot_name, user_id, cnt, total_min):
            self.hotspot_name = hotspot_name
            self.user_id = user_id
            self.cnt = cnt
            self.total_min = total_min

    @staticmethod
    def select_all_records(db_cursor) -> []:
        db_cursor.execute(
            'SELECT '
            +'h.name, t.user_id, COUNT(t.user_id) AS cnt '
            +',SUM(TIMESTAMPDIFF(MINUTE,entry_time, exit_time)) AS total_min '
            +'FROM CP_database.traces t '
            +'INNER JOIN CP_database.hotspots h '
            +'ON t.hotspot_id = h.id '
            +'GROUP BY h.name, t.user_id '
            +'ORDER BY h.name, cnt desc'
            )
        records = []
        for res in db_cursor.fetchall():
            records.append(ClusterRepository.get_record_from_result(res))
        return records

    @staticmethod
    def get_record_from_result(res) -> Cluster:
        return ClusterRepository.Cluster(res[0],res[1],res[2],res[3])