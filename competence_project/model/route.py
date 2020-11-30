class Route:
    def __init__(self, user_id, longest_route):
        self.user_id = user_id
        self.longest_route = longest_route

    def __str__(self):
        return "(user_id=" + str(self.user_id) + ", longest_route=" + str(self.longest_route) + ")"
