class Hotspot:
    def __init__(self, name, x, y, outdoor=True, description=""):
        self.id = id(self)
        self.name = name
        self.x = x
        self.y = y
        self.outdoor = outdoor
        self.description = description

    def __str__(self):
        return self.name + " " + " " + str(self.x) + " " + str(self.y) + " " + str(
            self.outdoor) + " " + self.description
