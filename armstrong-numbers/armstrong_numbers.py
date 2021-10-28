"""exercism armstrong numbers module."""


def is_armstrong_number(number):
    """
    Determine if the number provided is an Armstrong Number.

    An Armstrong Number is a number that is the sum of its own digits each raised to the power of the number of digits

    :param number int - Number to check.
    :return bool - Whether the provided number passes the check or not.

    >>> is_armstrong_number(9)
    True
    # because `9 = 9^1 = 9`

    >>> is_armstrong_number(10)
    False
    # because `10 != 1^2 + 0^2 = 1`
    """

    number_string = list(str(number))
    digit_sum = 0
    power = len(number_string)
    for digit in number_string:
        digit_sum += int(digit) ** power

    return digit_sum == number
