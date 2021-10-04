"""exercism say module."""


def say(number):
    """
    Make the 'spelled out' equivalent of a number between 0 and 999,999,999,999

    :param number int - The number to 'say'.
    :return string - Number spelled out that number in English.
    """
    if number < 0:
        raise ValueError("Number less than 0.")

    if number > 999999999999:
        raise ValueError("Number too big.")

    small_numbers = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen"
    }

    speech = ""

    if number < 14:
        speech = small_numbers.get(number)
    elif number < 20:
        speech = say(number % 10) + "teen"
    elif number < 100:
        divisors = [90, 80, 70, 60, 50, 40, 30, 20]
        multiples_of_ten = {
            20: "twenty",
            30: "thirty",
            40: "forty",
            50: "fifty",
            60: "sixty",
            70: "seventy",
            80: "eighty",
            90: "ninety"
        }

        for num in divisors:
            fits_into = number / num
            if fits_into >= 1:
                speech = multiples_of_ten.get(num)

                if number % 10 > 0:
                    speech += "-" + say(number % 10)

                break

    else:
        divisors = [100, 1000, 1000000, 1000000000]
        divisors.reverse()
        large_numbers = { 100: "hundred", 1000: "thousand", 1000000: "million", 1000000000: "billion" }

        for num in divisors:
            fits_into = number / num
            if fits_into >= 1:
                rest = number % num
                speech = say(number // num) + " " + large_numbers.get(num)
                if rest > 0:
                    speech += " " + say(rest)

                break

    return speech
