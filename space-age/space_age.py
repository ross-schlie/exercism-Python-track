"""exercism space age module."""

class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def __earth_years(self):
        return self.seconds / 31557600

    def on_mercury(self):
        return float(format(self.__earth_years() / 0.2408467, ".2f"))

    def on_venus(self):
        return float(format(self.__earth_years() / 0.61519726, ".2f"))

    def on_earth(self):
        return float(format(self.__earth_years(), ".2f"))

    def on_mars(self):
        return float(format(self.__earth_years() / 1.8808158, ".2f"))

    def on_jupiter(self):
        return float(format(self.__earth_years() / 11.862615, ".2f"))

    def on_saturn(self):
        return float(format(self.__earth_years() / 29.447498, ".2f"))

    def on_uranus(self):
        return float(format(self.__earth_years() / 84.016846, ".2f"))

    def on_neptune(self):
        return float(format(self.__earth_years() / 164.79132, ".2f"))
