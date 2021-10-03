"""exercism series module."""


def slices(series, length):
    """
    Given a string of digits, output all the contiguous substrings
        of length n in that string in the order that they appear.

    :param series string - string of digits.
    :param length int - the length of the series to find.
    :return list - List of substrings of specified length from series.
    """

    if len(series) < length:
        raise ValueError("Length requested is shorter than series.")

    if length < 1:
        raise ValueError("Length requested is less than 1.")

    substrings = []
    for index, number in enumerate(series):
        sub = series[index:index + length]
        if len(sub) == length:
            substrings.append(sub)

    return substrings
