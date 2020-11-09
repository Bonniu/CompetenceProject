class Trace:
    def __init__(self, user_id, hotspot, entry_time, exit_time):
        self.user_id = user_id
        self.hotspot = hotspot
        self.entry_time = entry_time
        self.exit_time = exit_time

    def __str__(self):
        return str(self.user_id) + " " + str(self.hotspot) + " " + str(self.entry_time) + " " + str(self.exit_time)
