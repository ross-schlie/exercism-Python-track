'''
Introduction
Implement a clock that handles times without dates.

You should be able to add and subtract minutes to it.

Two clocks that represent the same time should be equal to each other.
'''

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

# Test code
# c = Clock(8, 0)
# print(str(c)) # "08:00"
# c = Clock(23, 59) + 2
# print(str(c))
# a = Clock(7, 32)
# b = Clock(-12, -268)
# print(str(a))
# print(str(b))
# c = Clock(0, 3) - 4 # "23:59"
# print(str(c))