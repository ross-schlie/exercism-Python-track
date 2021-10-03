"""exercism grains module."""

import math

def square(number):
    if number == 1:
        return 1

    if number > 64:
        raise ValueError('Chessboard only has 64 squares')

    if number < 1:
        raise ValueError('Chessboard square number must be positive')

    # print(math.pow(2, number - 1))
    return int(math.pow(2, number - 1))


def total():
    return square(64) * 2 - 1
