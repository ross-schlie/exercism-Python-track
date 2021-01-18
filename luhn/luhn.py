class Luhn:

    def __init__(self, card_num):
        """Given a number, is a Luhn number?"""
        self._valid = False
        self._number = card_num

    def valid(self):
        """Check if the provided number conforms to a Luhn number."""
        # reset in case valid is called multiple times
        self._valid = False
        self._check()
        return self._valid

    def _simple_check(self, num):
        if num.isdecimal() == False:
            return False
        
        if len(num) <= 1:
            return False

        return True

    def _check(self):
        num = self._number.replace(' ', '')
        if not self._simple_check(num):
            return
        
        totalsum = 0
        numbers = list(num)
        # If the number is odd, this will be 1, otherwise 0.
        divisor_remainder = len(numbers) % 2
        for index in range(len(numbers)):
            if index % 2 == divisor_remainder:
                even_number_doubled = int(numbers[index]) * 2
                if even_number_doubled > 9:
                    even_number_doubled -= 9
                
                totalsum += even_number_doubled
            else:
                totalsum += int(numbers[index])
            
        # If the sum is evenly divisible by 10, then the number is valid
        if totalsum % 10 == 0:
            self._valid = True