"""exercism clock module."""

class Clock:
    def __init__(self, hour, minute):
        self.minute = minute % 60
        self.hour = (hour + (minute // 60)) % 24

    def __repr__(self):
        return '{:0>2d}:{:0>2d}'.format(self.hour, self.minute)

    def __eq__(self, other):
        return (self.minute == other.minute) and (self.hour == other.hour)

    def __add__(self, minutes):
        newminute = (self.minute + minutes) % 60
        newhour = self.hour + ((self.minute + minutes) // 60)
        return Clock(newhour, newminute)

    def __sub__(self, minutes):
        newminute = (self.minute - minutes) % 60
        newhour = self.hour + ((self.minute - minutes) // 60)
        return Clock(newhour, newminute)
