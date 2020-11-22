import random

USER_PROFILES = ["student", "cook", "seller", "athlete", "retired"]
USER_INTERESTS = ["football", "cinema lover", "sport", "bowling", "shopping", "books"]
PROFILES_CHOICE_WEIGHTS = [3, 1, 1, 3, 2]
INTERESTS_CHOICE_WEIGHTS = [1, 1, 2, 2, 2, 2]
class Person:
    def __init__(self, x,y, current_hotspot, phone_number=None):
        self.id = id(self)
        self.phone_number = phone_number
        self.profile = random.choices(USER_PROFILES, PROFILES_CHOICE_WEIGHTS, k=1)
        self.interests = random.choices(USER_INTERESTS, INTERESTS_CHOICE_WEIGHTS, k=2)
        self.current_hotspot = current_hotspot
        self.route = []
        self.x = x
        self.y = y


    def __str__(self):
        return str(self.id) + " " + str(self.phone_number) + " " + self.profile
