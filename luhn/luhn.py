'''
Introduction
Given a number determine whether or not it is valid per the Luhn formula.

The Luhn algorithm is a simple checksum formula used to validate a variety of identification numbers, 
such as credit card numbers and Canadian Social Insurance Numbers.

The task is to check if a given string is valid.

Validating a Number
Strings of length 1 or less are not valid. Spaces are allowed in the input, but they should be stripped before checking. 
All other non-digit characters are disallowed.

Example 1: valid credit card number
4539 1488 0343 6467
The first step of the Luhn algorithm is to double every second digit, starting from the right. We will be doubling

4_3_ 1_8_ 0_4_ 6_6_
If doubling the number results in a number greater than 9 then subtract 9 from the product. The results of our doubling:

8569 2478 0383 3437
Then sum all of the digits:

8+5+6+9+2+4+7+8+0+3+8+3+3+4+3+7 = 80
If the sum is evenly divisible by 10, then the number is valid. This number is valid!

Example 2: invalid credit card number
8273 1232 7352 0569
Double the second digits, starting from the right

7253 2262 5312 0539
Sum the digits

7+2+5+3+2+2+6+2+5+3+1+2+0+5+3+9 = 57
57 is not evenly divisible by 10, so this number is not valid.
'''

class Luhn:

    def __init__(self, card_num):
        self.__valid = False
        self.__number = card_num

    def valid(self):
        # reset in case valid is called multiple times
        self.__valid = False
        self.__check()
        return self.__valid

    def __check(self):
        num = self.__number.replace(' ', '')
        if num.isdecimal() == False:
            return False
        
        if len(num) <= 1:
            return False
        
        # print(num)
        totalsum = 0
        numbers = list(num)
        # If the number is odd, this will be 1, otherwise 0. This helps with
        # every second digit, starting from the right being doubled
        divisorremainder = len(numbers) % 2
        for i in range(len(numbers)):
            # print(numbers[i])
            if i % 2 == divisorremainder:
                evenumdbld = int(numbers[i]) * 2
                # print(evenumdbld)
                if evenumdbld > 9:
                    evenumdbld -= 9
                
                totalsum += evenumdbld
            else:
                oddnum = int(numbers[i])
                # print(oddnum)
                totalsum += oddnum
            
        # print(totalsum)
        # If the sum is evenly divisible by 10, then the number is valid
        if totalsum % 10 == 0:
            self.__valid = True

        return


# cardnum = '4539 1488 0343 6467'
# luhncheck = Luhn(cardnum)
# print(luhncheck.valid())
# cardnum = ' 0'
# luhncheck = Luhn(cardnum)
# print(luhncheck.valid())
# number = Luhn("055 444 285")
# print(number.valid())
# print(number.valid())