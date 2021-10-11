"""exercism phone number module."""


class PhoneNumber:

    def __init__(self, number:str):
        chars_to_strip = [".", " ", "-", "(", ")", "+"]
        for subsitutiion in chars_to_strip:
            number = number.replace(subsitutiion, "")

        if number.startswith("1"):
            number = number[1::]

        self.number = number
        self.area_code = number[0:3]
        self.__validate()

    def __validate(self):
        """
        Validate that the provided number conforms to rules for North American Numbering Plan.

        (NXX)-NXX-XXXX
        where N is any digit from 2 through 9 and X is any digit from 0 through 9.
        """
        if self.number.isalpha():
            raise ValueError("Invalid phone number.")

        number_length = len(self.number)
        if self.number.startswith("0"):
            raise ValueError("Invalid phone number.")
        elif self.number.startswith("1"):
            raise ValueError("Invalid phone number.")
        elif number_length == 10 and self.number[3] in ["0", "1"]:
            raise ValueError("Invalid phone number.")

        if number_length not in [7, 10]:
            raise ValueError("Invalid phone number.")

    def pretty(self):
        """
        Output 'pretty' formatted phone number.
        """
        pretty_number = ""
        pretty_number += "(" + self.number[0:3] + ")-"
        if len(self.number) == 10:
            pretty_number += self.number[3:6] + "-" + self.number[6:10]
        else:
            pretty_number += self.number[3:7]

        return pretty_number