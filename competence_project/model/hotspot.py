class Hotspot:
    def __init__(self, name, geo_position, outdoor=True, description=""):
        self.name = name
        self.geo_position = geo_position
        self.outdoor = outdoor
        self.description = description

    def __str__(self):
        return self.name + " " + " " + str(self.geo_position) + " " + str(self.outdoor) + " " + self.description
