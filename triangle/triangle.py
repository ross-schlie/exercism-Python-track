"""exercism triangle module."""

def is_triangle(sides):
    """
    Check to see if this is a triangle

    :param sides: list[*int] - the length of the three sides of a triangle?
    :return bool - whether it is a triangle or not

    >>> is_triangle([1, 2, 3])
    True

    >>> is_triangle([0, 0, 0])
    False

    All sides have to be of length > 0
    The sum of the lengths of any two sides must be greater
        than or equal to the length of the third side.
    See https://en.wikipedia.org/wiki/Triangle_inequality
    """
    for length in sides:
        if length <= 0:
            return False

    if sides[0] + sides[1] < sides[2]:
        return False

    if sides[1] + sides[2] < sides[0]:
        return False

    if sides[0] + sides[2] < sides[1]:
        return False

    return True

def is_degenerate(sides):
    """
    Check to see if a triangle is 'degenerate'.

    :param sides: list[*int] - the length of the three sides of a triangle
    :return bool - whether a triangle is degenerate or not

    >>> is_degenerate([1, 2, 3])
    True

    >>> is_degenerate([4, 5, 6])
    False

    The sum of the lengths of two sides equals that of the third is known as a degenerate triangle
    It has zero area and looks like a single line.
    """

    if sides[0] + sides[1] == sides[2]:
        return True

    if sides[1] + sides[2] == sides[0]:
        return True

    if sides[0] + sides[2] == sides[1]:
        return True

    return False

def equilateral(sides):
    """
    Check to see if a triangle is equilateral.

    :param sides: list[*int] - the length of the three sides of a triangle
    :return bool - whether a triangle is equilateral or not

    An equilateral triangle has all three sides the same length.
    """

    if not is_triangle(sides):
        return False

    if sides[0] == sides[1] and sides[1] == sides[2]:
        return True

    return False


def isosceles(sides):
    """
    Check to see if a triangle is an isosceles.

    :param sides: list[*int] - the length of the three sides of a triangle
    :return bool - whether a triangle is an isosceles or not

    An isosceles triangle has at least two sides the same length.
    (It is sometimes specified as having exactly two sides the same length,
    but for the purposes of this exercise we'll say at least two.)
    """

    if not is_triangle(sides):
        return False

    if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
        return True

    return False


def scalene(sides):
    """
    Check to see if a triangle is a scalene.

    :param sides: list[*int] - the length of the three sides of a triangle
    :return bool - whether a triangle a scalene or not

    A scalene triangle has all sides of different lengths.
    """

    if not is_triangle(sides):
        return False

    if sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]:
        return True

    return False
