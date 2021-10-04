"""exercism hangman module."""


# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.__word = word
        self.masked_word = ["_"] * len(word)
        self.guessed_letters = {}
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING

    def guess(self, char):
        if self.status == STATUS_LOSE:
            raise ValueError("No guesses remain.")

        if self.status == STATUS_WIN:
            raise ValueError("Game already won.")

        if char in self.__word and self.guessed_letters.get(char) is None:
            for index, c in enumerate(self.__word):
                if c == char:
                    self.masked_word[index] = char

            if "".join(self.masked_word) == self.__word:
                self.status = STATUS_WIN

            self.guessed_letters[char] = True
        else:
            self.remaining_guesses -= 1
            if self.remaining_guesses < 0:
                self.status = STATUS_LOSE

    def get_masked_word(self):
        return "".join(self.masked_word)

    def get_status(self):
        return self.status
