import csv

from database.repository.HotspotRepository import HotspotRepository
from database.repository.PersonRepository import PersonRepository
from database.repository.TraceRepository import TraceRepository

prefix = "../data_csv/"


class DbImport:

    @staticmethod
    def read_hotspots(db, db_cursor, size_of_data: str):
        hotspot_list = []
        # Read CSV file
        with open(prefix + size_of_data + "/hotspots.csv") as fp:
            reader = csv.reader(fp, delimiter=",", quotechar='"')
            next(reader, None)  # skip the headers
            data_read = [row for row in reader]
            for obj in data_read:
                obj1 = HotspotRepository.get_hotspot_from_result(obj)
                hotspot_list.append(obj1)

        HotspotRepository.insert_hotspots(db, db_cursor, hotspot_list)

    @staticmethod
    def read_persons(db, db_cursor, size_of_data: str):
        person_list = []
        # Read CSV file
        with open(prefix + size_of_data + "/persons.csv") as fp:
            reader = csv.reader(fp, delimiter=",", quotechar='"')
            next(reader, None)  # skip the headers
            data_read = [row for row in reader]
            for obj in data_read:
                obj1 = PersonRepository.get_person_from_result(obj)
                person_list.append(obj1)

        PersonRepository.insert_persons(db, db_cursor, person_list)

    @staticmethod
    def read_traces(db, db_cursor, size_of_data: str):
        trace_list = []
        # Read CSV file
        with open(prefix + size_of_data + "/traces.csv") as fp:
            reader = csv.reader(fp, delimiter=",", quotechar='"')
            next(reader, None)  # skip the headers
            data_read = [row for row in reader]
            for obj in data_read:
                obj1 = TraceRepository.get_trace_from_result(obj)
                trace_list.append(obj1)

        TraceRepository.insert_traces(db, db_cursor, trace_list)

    @staticmethod
    def read_traces2(db, db_cursor, size_of_data: str):
        # Read CSV file
        with open(prefix + size_of_data + "/traces.sql") as sql_file:
            sql = sql_file.read()
            db_cursor.execute(sql)
