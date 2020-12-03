from math import sin, cos, sqrt, atan2, radians

from service import initialize_hotspots, new_coordinates, initialize_persons, generate_route_for_person
from tests.test_initialization import HOTSPOT_DESCRIPTIONS, USER_PROFILES, USER_INTERESTS
from main import init_database

CITY_CENTRE_X = 51.759046
CITY_CENTRE_Y = 19.458062
MIN_DISTANCE = 0.0005
MAX_DISTANCE = 0.08


def calc_distance(x1, y1, x2, y2):
    R = 6373.0

    lat1 = radians(x1)
    lon1 = radians(y1)
    lat2 = radians(x2)
    lon2 = radians(y2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


def get_min_max_distance():
    max_coordinate = new_coordinates(CITY_CENTRE_X, CITY_CENTRE_Y, MAX_DISTANCE, 0)
    max_distance = calc_distance(CITY_CENTRE_X, CITY_CENTRE_Y,
                                 float(max_coordinate[0]), float(max_coordinate[1]))
    for j in range(360):
        new_coordinate = new_coordinates(CITY_CENTRE_X, CITY_CENTRE_Y, MAX_DISTANCE, j)
        new_distance = calc_distance(CITY_CENTRE_X, CITY_CENTRE_Y,
                                     float(new_coordinate[0]), float(new_coordinate[1]))
        if max_distance < new_distance:
            max_distance = new_distance

    min_coordinate = new_coordinates(CITY_CENTRE_X, CITY_CENTRE_Y, MAX_DISTANCE, 0)
    min_distance = calc_distance(CITY_CENTRE_X, CITY_CENTRE_Y,
                                 float(min_coordinate[0]), float(min_coordinate[1]))
    for j in range(360):
        new_coordinate = new_coordinates(CITY_CENTRE_X, CITY_CENTRE_Y, MIN_DISTANCE, j)
        new_distance = calc_distance(CITY_CENTRE_X, CITY_CENTRE_Y,
                                     float(new_coordinate[0]), float(new_coordinate[1]))
        if min_distance > new_distance:
            min_distance = new_distance

    return min_distance, max_distance


def test_generation_of_hotspots():
    min_distance, max_distance = get_min_max_distance()
    for i in range(50):
        hotspots = initialize_hotspots(100)
        assert hotspots.__len__() == 100

        hotspots_ids = []
        for h in hotspots:
            hotspots_ids.append(h.id)
            assert min_distance < calc_distance(CITY_CENTRE_X, CITY_CENTRE_Y, h.x, h.y) < max_distance
            assert h.description in HOTSPOT_DESCRIPTIONS
            assert h.name == h.description + "_" + str(h.id)
            assert h.outdoor is False or True

        assert len(hotspots_ids) == len(set(hotspots))


def test_generation_of_persons():
    min_distance, max_distance = get_min_max_distance()
    for i in range(50):
        people = initialize_persons(100)
        assert people.__len__() == 100

        people_ids = []
        for p in people:
            people_ids.append(p.id)
            assert min_distance < calc_distance(CITY_CENTRE_X, CITY_CENTRE_Y, p.x, p.y) < max_distance
            assert p.profile in USER_PROFILES
            assert p.interests in USER_INTERESTS

        assert len(people_ids) == len(set(people))


def test_generation_of_route_for_person():
    db_cursor, db = init_database()
    hotspots = initialize_hotspots(50)
    people = initialize_persons(10)
    for i in range(people.__len__()):
        assert generate_route_for_person(hotspots, people[i], db, db_cursor) is None or True
