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
