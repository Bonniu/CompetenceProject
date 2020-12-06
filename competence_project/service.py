import datetime
import random
import traceback
from math import radians, cos, sin, pi, sqrt, atan2

# import plotly.utils
import numpy
import pandas as pd

from database.repository.PersonRepository import PersonRepository
from database.repository.TraceRepository import TraceRepository
from database.repository.RouteRepository import RouteRepository
from model.hotspot import Hotspot
from model.person import Person
from model.trace import Trace
from model.route import Route

R = 6373.0

START_DATE = datetime.datetime.strptime('2020-10-20', '%Y-%m-%d')
END_DATE = datetime.datetime.strptime('2020-12-20', '%Y-%m-%d')


def initialize_hotspots(number_of_hotspots, CITY_CENTRE_X, CITY_CENTRE_Y, MIN_DISTANCE, MAX_DISTANCE):
    try:
        new_hotspots = []
        angles = numpy.random.uniform(low=0.0, high=360.0, size=2 * number_of_hotspots)
        new_hotspots_number = 0
        for numb, dist in enumerate(numpy.random.exponential(scale=0.1, size=2 * number_of_hotspots), start=0):
            if new_hotspots_number > number_of_hotspots - 1:
                break
            if MIN_DISTANCE < dist < MAX_DISTANCE:
                angle = angles[numb]
                new_coordination = new_coordinates(CITY_CENTRE_X, CITY_CENTRE_Y, dist, angle)
                new_hotspots.append(Hotspot(float(new_coordination[0]), float(new_coordination[1])))
                new_hotspots_number += 1
            else:
                dist = random.uniform(MIN_DISTANCE, MAX_DISTANCE)
                angle = angles[numb]
                new_coordination = new_coordinates(CITY_CENTRE_X, CITY_CENTRE_Y, dist, angle)
                new_hotspots.append(Hotspot(float(new_coordination[0]), float(new_coordination[1])))
                new_hotspots_number += 1

        return new_hotspots

    except Exception:
        traceback.print_exc()
        return []


def new_coordinates(x0, y0, d, theta):
    theta_rad = pi / 2 - radians(theta)
    return x0 + d * cos(theta_rad), y0 + d * sin(theta_rad)


def initialize_persons(number_of_persons, CITY_CENTRE_X, CITY_CENTRE_Y, MIN_DISTANCE, MAX_DISTANCE):
    try:
        new_persons = []
        angles = numpy.random.uniform(low=0.0, high=360.0, size=2 * number_of_persons)
        new_persons_number = 0
        for numb, dist in enumerate(numpy.random.exponential(scale=0.1, size=2 * number_of_persons), start=0):
            if new_persons_number > number_of_persons - 1:
                break
            if MIN_DISTANCE < dist < MAX_DISTANCE:
                angle = angles[numb]
                new_coordination = new_coordinates(CITY_CENTRE_X, CITY_CENTRE_Y, dist, angle)
                random_phone_number = random.randint(100000000, 999999999)
                new_persons.append(Person(new_coordination[0], new_coordination[1], random_phone_number))
                new_persons_number += 1
            else:
                dist = random.uniform(MIN_DISTANCE, MAX_DISTANCE)
                angle = angles[numb]
                new_coordination = new_coordinates(CITY_CENTRE_X, CITY_CENTRE_Y, dist, angle)
                random_phone_number = random.randint(100000000, 999999999)
                new_persons.append(Person(new_coordination[0], new_coordination[1], random_phone_number))
                new_persons_number += 1

        return new_persons

    except Exception:
        traceback.print_exc()
        return []


def choose_next_hotspot(person, hotspots, previous_location):
    try:
        if isinstance(previous_location, Hotspot):
            previous_x = previous_location.x
            previous_y = previous_location.y
        else:
            previous_x = person.x
            previous_y = person.y

        hotspot_dict = {}
        for hotspot in hotspots:
            distance = sqrt((hotspot.x - previous_x) ** 2 + (hotspot.y - previous_y) ** 2)
            hotspot_dict[hotspot] = distance

        sorted_hotspots = sorted(hotspot_dict.items(), key=lambda x: x[1])
        chance_multiplier = sorted(numpy.random.exponential(scale=5, size=len(list(sorted_hotspots))))
        chance_multiplier = [int(x) for x in chance_multiplier]
        hotspots_with_chances = {}
        for i, tup in enumerate(sorted_hotspots, start=1):
            hotspots_with_chances[tup[0]] = chance_multiplier[-i]
            hotspots_with_chances[tup[0]] *= return_multiplier(person, tup[0])
            hotspots_with_chances[tup[0]] = int(hotspots_with_chances[tup[0]] * 100)

        #print(hotspots_with_chances)
        return random.choices(list(hotspots_with_chances.keys()), list(hotspots_with_chances.values()), k=1)[0]
    except Exception as exc:
        print(exc)

        return False


def return_multiplier(person, hotspot):
    connections = {
        "cafe": [("football", 1), ("cinemagoer", 1), ("sport", 1), ("bowling", 1), ("shopping", 1.2), ("books", 1.5)],
        "bowlingPlace": [("football", 1), ("cinemagoer", 0.9), ("sport", 1.1), ("bowling", 2), ("shopping", 1),
                         ("books", 0.9)],
        "restaurant": [("football", 1), ("cinemagoer", 1.3), ("sport", 1.1), ("bowling", 1), ("shopping", 1.5),
                       ("books", 1)],
        "shop": [("football", 1), ("cinemagoer", 1), ("sport", 1.2), ("bowling", 0.9), ("shopping", 1.8),
                 ("books", 1.4)],
        "park": [("football", 0.8), ("cinemagoer", 1), ("sport", 1.6), ("bowling", 1), ("shopping", 1), ("books", 1.8)],
        "library": [("football", 0.3), ("cinemagoer", 1.2), ("sport", 0.7), ("bowling", 0.5), ("shopping", 1.8),
                    ("books", 2.0)],
        "parking": [("football", 0.5), ("cinemagoer", 1.0), ("sport", 1.2), ("bowling", 1.4), ("shopping", 2.0),
                    ("books", 1.6)],
        "university": [("football", 1.4), ("cinemagoer", 1.7), ("sport", 1.2), ("bowling", 0.6), ("shopping", 1.3),
                       ("books", 1.8)],
        "stadium": [("football", 2.0), ("cinemagoer", 1.0), ("sport", 1.5), ("bowling", 1.2), ("shopping", 0.6),
                    ("books", 0.2)],
        "cinema": [("football", 1.2), ("cinemagoer", 2.0), ("sport", 1.5), ("bowling", 1.3), ("shopping", 1.7),
                   ("books", 1.9)]
    }

    for key, val in connections.items():
        if key == hotspot.description:
            for e in val:
                if person.interests == e[0]:
                    return e[1]


def generate_route_for_person(hotspots, person, db, db_cursor):
    try:
        visited_hotspots = []
        today_traces = []
        all_traces_for_person = []

        current_date = START_DATE

        while current_date < END_DATE:
            start_time = generate_start_time(current_date)
            next_hotspot = choose_next_hotspot(person, hotspots, None)
            trace_walking_time = needed_time(distance_between_two_points(person, next_hotspot))
            arriving_time = start_time + datetime.timedelta(seconds=trace_walking_time * 60)
            exit_time = arriving_time + datetime.timedelta(seconds=visiting_time() * 60)
            new_trace = Trace(person.id, next_hotspot.id, arriving_time, exit_time)
            today_traces.append(new_trace)
            all_traces_for_person.append(new_trace)
            visited_hotspots.append(next_hotspot.id)

            max_activity_time = current_date.replace(minute=0, hour=23)
            while exit_time < max_activity_time:
                previous_trace = today_traces[-1]
                previous_hotspot = next((x for x in hotspots if x.id == today_traces[-1].hotspot_id), None)
                start_time = previous_trace.exit_time
                next_hotspot = choose_next_hotspot(person, hotspots, previous_hotspot)
                while next_hotspot.id in visited_hotspots:
                    next_hotspot = choose_next_hotspot(person, hotspots, previous_hotspot)
                trace_walking_time = needed_time(distance_between_two_points(previous_hotspot, next_hotspot))
                arriving_time = start_time + datetime.timedelta(seconds=trace_walking_time * 60)
                exit_time = arriving_time + datetime.timedelta(seconds=visiting_time() * 60)
                new_trace = Trace(person.id, next_hotspot.id, arriving_time, exit_time)
                today_traces.append(new_trace)
                all_traces_for_person.append(new_trace)
                visited_hotspots.append(next_hotspot.id)

            visited_hotspots = []
            today_traces = []
            current_date = current_date + datetime.timedelta(days=1)
        TraceRepository.insert_traces(db, db_cursor, all_traces_for_person)
        return True
    except Exception as exc:
        print(exc)


def generate_start_time(date):
    min_hour = 6
    max_hour = 16

    hour = random.randint(min_hour, max_hour)
    minute = random.randint(0, 59)

    new_date = date
    new_date = new_date.replace(minute=minute, hour=hour)
    return new_date


def distance_between_two_points(hotspot1, hotspot2):
    lat1 = radians(hotspot1.x)
    lon1 = radians(hotspot1.y)
    lat2 = radians(hotspot2.x)
    lon2 = radians(hotspot2.y)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


def needed_time(distance):
    min_minute_for_km = 5
    max_minute_for_km = 15

    walk_time = random.randint(min_minute_for_km, max_minute_for_km)
    return walk_time * distance


# ewentualnie dorzucic rozklad
def visiting_time():
    min_visiting_time = 1
    max_visiting_time = 180

    visit_time = random.randint(min_visiting_time, max_visiting_time)
    return visit_time


def generate_traces_for_persons(persons, hotspots, db, db_cursor):
    try:
        for person in persons:
            generate_route_for_person(hotspots, person, db, db_cursor)

    except Exception as exc:
        print(exc)


def calculate_longest_route(db, db_cursor):
    traces = TraceRepository.select_traces_for_ids(db_cursor, None, None)
    people = PersonRepository.select_all_persons(db_cursor)
    for x in people:
        results = [t for t in traces if t.user_id == x.id]
        results.sort(key=lambda x: x.entry_time)
        dates = [obj.entry_time for obj in results]
        s = pd.to_datetime(pd.Series(dates), format='%Y-%m-%d %H:%M:%S')
        s.index = s.dt.to_period('D')
        s = s.groupby(level=0).size()
        s = s.reindex(pd.period_range(s.index.min(), s.index.max(), freq='D'))
        print('Maksymalna trasa wynosi: ', s.max())
        RouteRepository.insert_route(db, db_cursor, Route(x.id, int(s.max())))


def calculate_length_of_stay(db_cursor):
    traces = TraceRepository.select_traces_for_ids(db_cursor, None, None)

    # init
    list_of_dict = []
    for trace in traces:
        hs_user_length_dict = {"hotspot_id": trace.hotspot_id, "user_id": trace.user_id, "length_of_stay": 0}
        if hs_user_length_dict not in list_of_dict:
            list_of_dict.append(hs_user_length_dict)

    for trace in traces:
        for dictionary in list_of_dict:
            # jesli ten slownik ma hotspot_id i user_id takie jak chce to:
            if dictionary["hotspot_id"] == trace.hotspot_id and dictionary["user_id"] == trace.user_id:
                dictionary["length_of_stay"] += diff_dates(trace.exit_time, trace.entry_time)

    return list_of_dict


# return in minutes
def diff_dates(date1, date2):
    return abs(date2 - date1).total_seconds() / 60.0

