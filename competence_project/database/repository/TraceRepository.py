from model.trace import Trace


class TraceRepository:

    @staticmethod
    def insert_trace(db, db_cursor, trace: Trace):
        query = "INSERT INTO CP_database.traces (user_id, hotspot_id, entry_time, exit_time) VALUES (%s, %s, %s, %s)"
        db_cursor.execute(query, (trace.user_id, trace.hotspot_id, trace.entry_time, trace.exit_time))
        db.commit()
        trace.id = db_cursor.lastrowid
        return trace

    @staticmethod
    def insert_traces(db, db_cursor, traces: []):
        for trace in traces:
            TraceRepository.insert_trace(db, db_cursor, trace)

    @staticmethod
    def select_traces_for_ids(db_cursor, user_id, hotspot_id) -> []:
        query = "SELECT * FROM CP_database.traces"
        if hotspot_id is not None:
            query += " WHERE hotspot_id=" + str(hotspot_id)
        if user_id is not None:
            query += " WHERE user_id=" + str(user_id)
        if query.count("WHERE") == 2:
            query = query[:36] + query[36:].replace("WHERE", "AND")
        print("QUERY: " + query)
        db_cursor.execute(query)
        traces = []
        for result_trace in db_cursor.fetchall():
            traces.append(TraceRepository.get_trace_from_result(result_trace))
        return traces

    @staticmethod
    def select_all_traces(db_cursor) -> []:
        db_cursor.execute("SELECT * FROM CP_database.traces")
        traces = []
        for res in db_cursor.fetchall():
            traces.append(TraceRepository.get_trace_from_result(res))
        return traces

    @staticmethod
    def get_trace_from_result(result) -> Trace:
        # 0id 1user_id 2hotspot_id 3entry_time 4exit_time
        trace = Trace(result[1], result[2], result[3], result[4])
        return trace
