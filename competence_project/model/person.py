import random

USER_PROFILES = ["student", "cook", "seller", "athlete", "retired"]
USER_INTERESTS = ["football", "cinemagoer", "sport", "bowling", "shopping", "books"]
PROFILES_CHOICE_WEIGHTS = [3, 1, 1, 3, 2]
INTERESTS_CHOICE_WEIGHTS = [1, 1, 2, 2, 2, 2]


class Person:
    def __init__(self, x, y, phone_number=None):
        self.id = id(self)
        self.x = x
        self.y = y
        self.phone_number = phone_number
        self.profile = random.choices(USER_PROFILES, PROFILES_CHOICE_WEIGHTS, k=1)[0]
        self.interests = random.choices(USER_INTERESTS, INTERESTS_CHOICE_WEIGHTS, k=1)[0]
        self.current_hotspot = None
        self.route = []

    def __str__(self):
        return "(id=" + str(self.id) + ", x=" + str(self.x) + ", y=" + str(
            self.y) + ", profile=" + str(self.profile) + ", interests=" + str(self.interests) + ", phone_number=" + str(
            self.phone_number) + ")"
