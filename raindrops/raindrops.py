"""exercism raindrops module."""


def convert(number):
    """Convert a number to a series of rain tones.

    Parameters
    ----------
    arg1 : int
        A number to convert to rain tones

    Returns
    ------
    string
        A string containing rain tones or the number if it's not converted.

    >>> convert(1)
    "1"

    >>> convert(3)
    "Pling"

    >>> convert(5)
    "Plang"

    >>> convert(7)
    "Plong"
    """
    rain = ''
    if number % 3 == 0:
        rain += 'Pling'

    if number % 5 == 0:
        rain += 'Plang'

    if number % 7 == 0:
        rain += 'Plong'

    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        # Instructions says "does not have any of 3, 5, or 7 as a factor,
        # the result should be the digits of the number."
        # However the unit test tests for 52 and fails when using 5 + 2  = 7
        # which would be divisible by 7 instead claiming it should result in 52
        # The example also uses 34 and the same would be true for it,
        # so this is commented out.

        # numberstr = format(number)
        # sum = 0
        # for i in range(0, len(numberstr)):
        #     sum += int(numberstr[i])

        # rain = format(sum)
        rain = format(number)

    return rain
