import pytest
import random
import datetime

from model.person import Person
from model.hotspot import Hotspot
from model.trace import Trace

USER_INTERESTS = ["football", "cinemagoer", "sport", "bowling", "shopping", "books"]
USER_PROFILES = ["student", "cook", "seller", "athlete", "retired"]
HOTSPOT_DESCRIPTIONS = ["cafe", "bowlingPlace", "restaurant", "shop", "park", "library", "parking", "university",
                        "stadium", "cinema"]
repeat_test_amount = 100


def generate_x_y_and_phone_number():
    return random.uniform(-50.0, 50.0), random.uniform(-50.0, 50.0), random.randint(111111111, 999999999)


def generate_x_y_and_outdoor():
    return random.uniform(-50.0, 50.0), random.uniform(-50.0, 50.0), random.choice([True, False])


def generate_entry_and_exit_time():
    min_hour = 6
    max_hour = 16

    hour = random.randint(min_hour, max_hour)
    minute = random.randint(0, 59)

    new_date = datetime.datetime.strptime('2020-10-20', '%Y-%m-%d')
    new_date = new_date.replace(minute=minute, hour=hour)
    return new_date, new_date + datetime.timedelta(seconds=random.randint(1, 10) * 60)


@pytest.mark.parametrize("x, y, phone_number", [
    (generate_x_y_and_phone_number()) for i1 in range(repeat_test_amount)
])
def test_person_initialization(x, y, phone_number):
    person_test = Person(x, y, phone_number)
    assert person_test.x is not None
    assert person_test.x == x
    assert isinstance(person_test.y, float) or isinstance(person_test.y, int)
    assert person_test.y is not None
    assert person_test.y == y
    assert isinstance(person_test.y, float) or isinstance(person_test.y, int)
    assert person_test.phone_number is not None
    assert person_test.phone_number == phone_number
    assert isinstance(person_test.id, int)
    assert person_test.interests in USER_INTERESTS
    assert person_test.current_hotspot is None
    assert isinstance(person_test.route, list)
    assert person_test.route.__len__() == 0
    assert person_test.profile in USER_PROFILES
    assert person_test.__str__() == "(id=" + str(person_test.id) + ", x=" + str(person_test.x) + ", y=" + str(
        person_test.y) + ", profile=" + str(person_test.profile) + ", interests=" + str(
        person_test.interests) + ", phone_number=" + str(person_test.phone_number) + ")"
    assert isinstance(person_test.__str__(), str)


@pytest.mark.parametrize("x, y, outdoor", [
    (generate_x_y_and_outdoor()) for i2 in range(repeat_test_amount)
])
def test_hotspot_initialization(x, y, outdoor):
    hotspot_test = Hotspot(x, y, outdoor)
    assert hotspot_test.x is not None
    assert hotspot_test.x == x
    assert isinstance(hotspot_test.x, float) or isinstance(hotspot_test.x, int)
    assert hotspot_test.y is not None
    assert hotspot_test.y == y
    assert isinstance(hotspot_test.y, float) or isinstance(hotspot_test.y, int)
    assert hotspot_test.outdoor == outdoor
    assert isinstance(hotspot_test.outdoor, bool)
    assert hotspot_test.description in HOTSPOT_DESCRIPTIONS
    assert hotspot_test.name == hotspot_test.description + "_" + str(hotspot_test.id)
    assert hotspot_test.__str__() == "(id=" + str(hotspot_test.id) + ", name=" + hotspot_test.name + ", x=" + str(
        hotspot_test.x) + ", y=" + str(hotspot_test.y) + ", outdoor?=" + str(
        hotspot_test.outdoor) + ", description=" + hotspot_test.description + ")"
    assert isinstance(hotspot_test.__str__(), str)


@pytest.mark.parametrize("entry_time, exit_time", [
    (generate_entry_and_exit_time()) for i3 in range(repeat_test_amount)
])
def test_trace_initialization(entry_time, exit_time):
    person_test = Person(1.002, 2.001, 666111222)
    hotspot_test = Hotspot(2.009, 1.009, True)
    trace_test = Trace(person_test.id, hotspot_test.id, entry_time, exit_time)
    assert trace_test.user_id == person_test.id
    assert trace_test.hotspot_id == hotspot_test.id
    assert trace_test.entry_time == entry_time
    assert isinstance(trace_test.entry_time, datetime.date)
    assert trace_test.exit_time == exit_time
    assert isinstance(trace_test.exit_time, datetime.date)


def test_people_ids():
    people = [Person(random.uniform(-50.0, 50.0), random.uniform(-50.0, 50.0), random.randint(111111111, 999999999))
              for i in range(1000)]
    people_ids = []
    for p in people:
        people_ids.append(p.id)

    assert len(people_ids) == len(set(people_ids))


def test_hotspots_ids():
    hotspots = [Hotspot(random.uniform(-50.0, 50.0), random.uniform(-50.0, 50.0), random.choice([True, False]))
              for i in range(1000)]
    hotspots_ids = []
    for h in hotspots:
        hotspots_ids.append(h.id)

    assert len(hotspots_ids) == len(set(hotspots_ids))
