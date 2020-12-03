import random
from datetime import datetime

HOTSPOT_DESCRIPTIONS = ["cafe", "bowlingPlace", "restaurant", "shop", "park", "library", "parking", "university",
                        "stadium", "cinema"]
weights = [2, 1, 2, 2, 2, 2, 2, 2, 2, 2]


class Hotspot:
    def __init__(self, x, y, outdoor=True):
        self.id = id(self)
        self.x = x
        self.y = y
        self.outdoor = outdoor
        self.description = random.choices(HOTSPOT_DESCRIPTIONS, weights, k=1)[0]
        self.name = self.description + "_" + str(self.id)

    def __str__(self):
        return "(id=" + str(self.id) + ", name=" + self.name + ", x=" + str(self.x) + ", y=" + str(
            self.y) + ", outdoor?=" + str(
            self.outdoor) + ", description=" + self.description + ")"
