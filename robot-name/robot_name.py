"""exercism robot module."""

import random
import string

robots = {}

class Robot:
    def __init__(self):
        self.reset()

    def __generate_name(self):
        name = ""
        for index in [0, 1]:
            name += self.__generate_letter()

        for index in [0, 1, 2]:
            name += self.__generate_number()

        return name

    def __generate_letter(self):
        return string.ascii_uppercase[random.randint(0, 25)]

    def __generate_number(self):
        return str(random.randint(0, 9))

    def reset(self):
        name = self.__generate_name()
        while robots.get(name) is not None:
            name = self.__generate_name()

        robots[name] = 1
        self.name = name