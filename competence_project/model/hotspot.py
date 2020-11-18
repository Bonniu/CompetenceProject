from datetime import datetime
from random import choices

HOTSPOT_DESCRIPTIONS = ["cafe", "bowlingPlace", "restaurant", "shop", "park", "library"]
weights = [0.35, 0.05, 0.2, 0.3, 0.08, 0.02]


class Hotspot:
    def __init__(self, x, y, outdoor=True):
        self.id = id(self)
        self.x = x
        self.y = y
        self.outdoor = outdoor
        self.description = choices(HOTSPOT_DESCRIPTIONS, weights)[0]
        self.name = self.description + "_" + str(datetime.now().microsecond)

    def __str__(self):
        return self.name + " " + " " + str(self.x) + " " + str(self.y) + " " + str(
            self.outdoor) + " " + self.description


