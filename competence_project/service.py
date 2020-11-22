from math import radians, cos, sin, pi, sqrt

#import plotly.utils
import numpy
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
        return x,y

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
        
        return x,y

    except Exception as exc:
        print(exc)
        return False

def choose_next_hospot(user, hotspots):
    current = user.current_hotspot
    distances = []
    for hotspot in hotspots:
        distance = sqrt((hotspot.x - current.x)**2 + (hotspot.y - current.y)**2)
        distances.append(distance)

    distances.sort()
    chance_multiplier = numpy.random.exponential(scale = 0.05, size = len(distances)).sort()

