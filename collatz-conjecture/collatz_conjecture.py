"""exercism collatz conjecture module."""


def steps(number):
    """
    Count steps needed to get to 1 from provided number.

    :param number int - the number provided.
    :return int - the number of steps taken to reach 1.
    """
    if number < 1:
        raise ValueError("Provided number is less than 1.")

    steps = 0
    while number != 1:
        steps += 1
        # Even
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1

    return steps
