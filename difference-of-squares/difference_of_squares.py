"""exercism difference of squares module."""


def square_of_sum(number):
    number_sum = 0
    for number in range(1, number + 1):
        number_sum += number

    return number_sum ** 2


def sum_of_squares(number):
    squares_sum = 0
    for number in range(1, number + 1):
        squares_sum += number ** 2

    return squares_sum


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)