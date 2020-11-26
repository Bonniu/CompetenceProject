import datetime
import random
from math import radians, cos, sin, pi, sqrt, atan2

# import plotly.utils
import numpy

from model.hotspot import Hotspot
from model.person import Person
from model.trace import Trace

CITY_CENTRE_X = 51.759046
CITY_CENTRE_Y = 19.458062
MIN_DISTANCE = 0.0005
MAX_DISTANCE = 0.08

START_DATE = datetime.datetime.strptime('2020-10-20', '%Y-%m-%d')
END_DATE = datetime.datetime.strptime('2020-12-20', '%Y-%m-%d')


def initialize_hotspots(number_of_hotspots):
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
                new_hotspots.append(Hotspot(new_coordination[0], new_coordination[1], "nazwa"))
                new_hotspots_number += 1

        x = [o.x for o in new_hotspots]
        y = [o.y for o in new_hotspots]

        # TODO funkcja dodajaca do bazy danych liste obiektow
        # db_function_to_add_hotspots_list_to_mysql(new_hotspots)
        return new_hotspots

    except Exception as exc:
        print(exc)
        return False


def new_coordinates(x0, y0, d, theta):
    theta_rad = pi / 2 - radians(theta)
    return x0 + d * cos(theta_rad), y0 + d * sin(theta_rad)


def initialize_users(number_of_users):
    try:
        new_users = []
        angles = numpy.random.uniform(low=0.0, high=360.0, size=2 * number_of_users)
        new_users_number = 0
        for numb, dist in enumerate(numpy.random.exponential(scale=0.1, size=2 * number_of_users), start=0):
            if new_users_number > number_of_users - 1:
                break
            if MIN_DISTANCE < dist < MAX_DISTANCE:
                angle = angles[numb]
                new_coordination = new_coordinates(CITY_CENTRE_X, CITY_CENTRE_Y, dist, angle)
                new_users.append(Person(x=new_coordination[0], y=new_coordination[1]))
                new_users_number += 1

        x = [o.x for o in new_users]
        y = [o.y for o in new_users]

        return new_users

    except Exception as exc:
        print(exc)
        return False


def choose_next_hotspot(user, hotspots, previous_location):
    try:
        if isinstance(previous_location, Hotspot):
            previous_x = previous_location.x
            previous_y = previous_location.y
        else:
            previous_x = user.x
            previous_y = user.y

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
            hotspots_with_chances[tup[0]] *= return_multiplier(user, tup[0])
            hotspots_with_chances[tup[0]] = int(hotspots_with_chances[tup[0]] * 100)

        print(hotspots_with_chances)
        return random.choices(list(hotspots_with_chances.keys()), list(hotspots_with_chances.values()), k=1)[0]
    except Exception as exc:
        print(exc)

        return False


def return_multiplier(user, hotspot):
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
                if user.interests[0] == e[0]:
                    return e[1]


def generate_route_for_user(hotspots, user):
    try:
        visited_hotspots = []
        today_traces = []
        all_traces_for_user = []

        current_date = START_DATE

        while current_date < END_DATE:
            start_time = generate_start_time(current_date)
            next_hotspot = choose_next_hotspot(user, hotspots, None)
            trace_walking_time = needed_time(distance_between_two_points(user, next_hotspot))
            arriving_time = start_time + datetime.timedelta(seconds=trace_walking_time * 60)
            exit_time = arriving_time + datetime.timedelta(seconds=visiting_time() * 60)
            new_trace = Trace(user.id, next_hotspot.id, arriving_time, exit_time)
            today_traces.append(new_trace)
            all_traces_for_user.append(new_trace)
            visited_hotspots.append(next_hotspot.id)

            max_activity_time = current_date.replace(minute=0, hour=23)
            while exit_time < max_activity_time:
                previous_trace = today_traces[-1]
                previous_hotspot = next((x for x in hotspots if x.id == today_traces[-1].hotspot_id), None)
                start_time = previous_trace.exit_time
                next_hotspot = choose_next_hotspot(user, hotspots, previous_hotspot)
                while next_hotspot.id in visited_hotspots:
                    next_hotspot = choose_next_hotspot(user, hotspots, previous_hotspot)
                trace_walking_time = needed_time(distance_between_two_points(previous_hotspot, next_hotspot))
                arriving_time = start_time + datetime.timedelta(seconds=trace_walking_time * 60)
                exit_time = arriving_time + datetime.timedelta(seconds=visiting_time() * 60)
                new_trace = Trace(user.id, next_hotspot.id, arriving_time, exit_time)
                today_traces.append(new_trace)
                all_traces_for_user.append(new_trace)
                visited_hotspots.append(next_hotspot.id)

            visited_hotspots = []
            today_traces = []
            current_date = current_date + datetime.timedelta(days=1)
        # TODO dodac trasy do bazy
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
    R = 6373.0

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


def generate_traces_for_users(users, hotspots):
    try:
        for user in users:
            generate_route_for_user(hotspots, user)

    except Exception as exc:
        print(exc)
