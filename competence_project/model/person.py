class Person:
    def __init__(self, phone_number=None, profile="student"):
        self.id = id(self)
        self.phone_number = phone_number
        self.profile = profile

    def __str__(self):
        return str(self.id) + " " + str(self.phone_number) + " " + self.profile
