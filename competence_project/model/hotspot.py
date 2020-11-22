from datetime import datetime
import random

HOTSPOT_DESCRIPTIONS = ["cafe", "bowlingPlace", "restaurant", "shop", "park", "library", "cafeteria", "parking lot", "university",
                        "football stadium", "cinema"]
weights = [2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]


class Hotspot:
    def __init__(self, x, y, outdoor=True):
        self.id = id(self)
        self.x = x
        self.y = y
        self.outdoor = outdoor
        self.description = str(random.choices(HOTSPOT_DESCRIPTIONS, weights, k=1))
        self.name = self.description + "_" + str(datetime.now().microsecond)

    def __str__(self):
        return self.name + " " + " " + str(self.x) + " " + str(self.y) + " " + str(
            self.outdoor) + " " + self.description


