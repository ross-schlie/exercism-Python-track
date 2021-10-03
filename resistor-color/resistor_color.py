"""exercism resistor color module."""


def color_code(color):
    color_list = colors()
    return color_list.index(color)


def colors():
    return [
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white",
        ]
