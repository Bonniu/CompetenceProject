from math import radians, cos, sin, pi, sqrt

#import plotly.utils
import numpy
import random
from random import choices
from scipy.stats import expon

from model.hotspot import Hotspot
from model.person import Person

CITY_CENTRE_X = 51.759046
CITY_CENTRE_Y = 19.458062
MIN_DISTANCE = 0.0005
MAX_DISTANCE = 0.08


def initialize_hotspots(number_of_hotspots):
    try:
        new_hotspots = []
        angles = numpy.random.uniform(low=0.0, high=360.0, size = 2*number_of_hotspots)
        new_hotspots_number = 0
        for numb, dist in enumerate(numpy.random.exponential(scale=0.1, size = 2*number_of_hotspots), start=0):
            if new_hotspots_number > number_of_hotspots-1:
                break
            if dist > MIN_DISTANCE and dist < MAX_DISTANCE:
                angle = angles[numb]
                new_coordination = new_coordinates(CITY_CENTRE_X, CITY_CENTRE_Y, dist, angle)
                new_hotspots.append(Hotspot(new_coordination[0], new_coordination[1], "nazwa"))
                new_hotspots_number += 1

        x=[o.x for o in new_hotspots]
        y=[o.y for o in new_hotspots]

        # TODO funkcja dodajaca do bazy danych liste obiektow
        #db_function_to_add_hotspots_list_to_mysql(new_hotspots)
        return new_hotspots

    except Exception as exc:
        print(exc)
        return False


def new_coordinates(x0, y0, d, theta):
    theta_rad = pi/2 - radians(theta)
    return x0 + d*cos(theta_rad), y0 + d*sin(theta_rad)


def initialize_users(number_of_users):
    try:
        new_users = []
        angles = numpy.random.uniform(low=0.0, high=360.0, size = 2*number_of_users)
        new_users_number = 0
        for numb, dist in enumerate(numpy.random.exponential(scale=0.1, size = 2*number_of_users), start=0):
            if new_users_number > number_of_users-1:
                break
            if dist > MIN_DISTANCE and dist < MAX_DISTANCE:
                angle = angles[numb]
                new_coordination = new_coordinates(CITY_CENTRE_X, CITY_CENTRE_Y, dist, angle)
                new_users.append(Person(x=new_coordination[0], y=new_coordination[1]))
                new_users_number += 1

        x=[o.x for o in new_users]
        y=[o.y for o in new_users]
        
        return new_users

    except Exception as exc:
        print(exc)
        return False

def choose_next_hospot(user, hotspots):
    try:
        hotspot_dict = {}
        for hotspot in hotspots:
            distance = sqrt((hotspot.x - user.x)**2 + (hotspot.y - user.y)**2)
            hotspot_dict[hotspot] = distance

        sorted_hotspots = sorted(hotspot_dict.items(), key=lambda x: x[1])
        chance_multiplier = sorted(numpy.random.exponential(scale = 5, size = len(list(sorted_hotspots))))
        chance_multiplier = [int(x) for x in chance_multiplier]
        hotspots_with_chances = {}
        for i, tup in enumerate(sorted_hotspots, start=1):
            hotspots_with_chances[tup[0]] = chance_multiplier[-i]
            hotspots_with_chances[tup[0]] *= return_multiplier(user, tup[0])
            hotspots_with_chances[tup[0]] = int(hotspots_with_chances[tup[0]]*100)

        print(hotspots_with_chances)
        return random.choices(list(hotspots_with_chances.keys()), list(hotspots_with_chances.values()), k=1)
    except Exception as exc:
        print(exc)

        return False


def return_multiplier(user, hotspot):

    connections = { "cafe":[("football", 1),  ("cinemagoer", 1),  ("sport", 1),  ("bowling", 1),  ("shopping", 1.2),  ("books", 1.5)],
                    "bowlingPlace": [("football", 1),  ("cinemagoer", 0.9),  ("sport", 1.1),  ("bowling", 2),  ("shopping", 1),  ("books", 0.9)],
                    "restaurant": [("football", 1),  ("cinemagoer", 1.3),  ("sport", 1.1),  ("bowling", 1),  ("shopping", 1.5),  ("books", 1)],
                    "shop": [("football", 1),  ("cinemagoer", 1),  ("sport", 1.2),  ("bowling", 0.9),  ("shopping", 1.8),  ("books", 1.4)],
                    "park": [("football", 0.8),  ("cinemagoer", 1),  ("sport", 1.6),  ("bowling", 1),  ("shopping",1),  ("books", 1.8)],
                    "library": [("football",0.3),  ("cinemagoer",1.2),  ("sport",0.7),  ("bowling",0.5),  ("shopping",1.8),  ("books",2.0)],
                    "parking": [("football",0.5),  ("cinemagoer",1.0),  ("sport",1.2),  ("bowling",1.4),  ("shopping",2.0),  ("books",1.6)],
                    "university": [("football",1.4),  ("cinemagoer",1.7),  ("sport",1.2),  ("bowling",0.6),  ("shopping",1.3),  ("books",1.8)],
                    "stadium": [("football",2.0),  ("cinemagoer",1.0),  ("sport",1.5),  ("bowling",1.2),  ("shopping",0.6),  ("books",0.2)],
                    "cinema": [("football",1.2),  ("cinemagoer",2.0),  ("sport",1.5),  ("bowling",1.3),  ("shopping",1.7),  ("books",1.9)]
                    }

    for key, val in connections.items():
        if key == hotspot.description:
            for e in val:
                if user.interests[0] == e[0]:
                    return e[1]



