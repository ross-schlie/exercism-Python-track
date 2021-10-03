"""exercism darts module."""


def score(x, y):
    """
    Score the points on a dart game based on coordinates of a dart.

    :param x int - the x coordinate (with 0 being the center of a dart board) of the dart.
    :param y int - the y coordinate (with 0 being the center of a dart board) of the dart.
    :return int - points scored based on where the dart landed.
    """
    points = 0
    dart = x * x + y * y
    radius_center = 1
    radius_middle = 5
    raidus_outer = 10
    if dart - radius_center * radius_center <= 0:
        points = 10 # center
    elif dart - radius_middle * radius_middle <= 0:
        points = 5 #middle circle
    elif dart - raidus_outer * raidus_outer <= 0:
        points = 1 #outer circle
    else:
        points = 0 #outside target

    return points
