# Introduction
# Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors. A factor is a number that evenly divides into another number, leaving no remainder. The simplest way to test if a one number is a factor of another is to use the modulo operation.

# The rules of raindrops are that if a given number:

# has 3 as a factor, add 'Pling' to the result.
# has 5 as a factor, add 'Plang' to the result.
# has 7 as a factor, add 'Plong' to the result.
# does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number.
# Examples
# 28 has 7 as a factor, but not 3 or 5, so the result would be "Plong".
# 30 has both 3 and 5 as factors, but not 7, so the result would be "PlingPlang".
# 34 is not factored by 3, 5, or 7, so the result would be "34".

def convert(number):
    rain = ''
    if number % 3 == 0:
        rain += 'Pling'

    if number % 5 == 0:
        rain += 'Plang' 

    if number % 7 == 0:
        rain += 'Plong'

    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        # Instructions says "does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number."
        # however the unit test tests for 52 and fails if it results in 7... 
        # The example also uses 34 and reuslts in 34 so this is commented out.

        # numberstr = format(number)
        # sum = 0
        # for i in range(0, len(numberstr)):
        #     sum += int(numberstr[i])

        # rain = format(sum)
        rain = format(number)

    return rain

# Self test code...
# x = convert(52)
# print(x)