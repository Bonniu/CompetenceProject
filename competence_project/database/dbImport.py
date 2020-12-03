import csv

from database.repository.HotspotRepository import HotspotRepository
from database.repository.PersonRepository import PersonRepository
from database.repository.TraceRepository import TraceRepository
from model.hotspot import Hotspot


class DbImport:

    @staticmethod
    def read_hotspots(db, db_cursor):
        hotspot_list = []
        # Read CSV file
        with open("database/data_csv/small/hotspots.csv") as fp:
            reader = csv.reader(fp, delimiter=",", quotechar='"')
            next(reader, None)  # skip the headers
            data_read = [row for row in reader]
            for obj in data_read:
                obj1 = HotspotRepository.get_hotspot_from_result(obj)
                hotspot_list.append(obj1)

        HotspotRepository.insert_hotspots(db, db_cursor, hotspot_list)

    @staticmethod
    def read_persons(db, db_cursor):
        person_list = []
        # Read CSV file
        with open("database/data_csv/small/persons.csv") as fp:
            reader = csv.reader(fp, delimiter=",", quotechar='"')
            next(reader, None)  # skip the headers
            data_read = [row for row in reader]
            for obj in data_read:
                obj1 = PersonRepository.get_person_from_result(obj)
                person_list.append(obj1)

        PersonRepository.insert_persons(db, db_cursor, person_list)

    @staticmethod
    def read_traces(db, db_cursor):
        trace_list = []
        # Read CSV file
        with open("database/data_csv/small/traces.csv") as fp:
            reader = csv.reader(fp, delimiter=",", quotechar='"')
            next(reader, None)  # skip the headers
            data_read = [row for row in reader]
            for obj in data_read:
                obj1 = TraceRepository.get_trace_from_result(obj)
                trace_list.append(obj1)

        TraceRepository.insert_traces(db, db_cursor, trace_list)
