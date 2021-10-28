"""exercism allergies module."""


ALLERGY_BITS = [1, 2, 4, 8, 16, 32, 64, 128]
ALLERGY_DESC = ['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats']

class Allergies:

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        index = ALLERGY_DESC.index(item)
        return ALLERGY_BITS[index] & self.score == ALLERGY_BITS[index]

    @property
    def lst(self):
        allergic = []
        for index, item in enumerate(ALLERGY_BITS):
            if item & self.score:
                allergic.append(ALLERGY_DESC[index])

        return allergic

