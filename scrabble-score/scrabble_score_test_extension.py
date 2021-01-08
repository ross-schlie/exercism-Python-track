import unittest

from scrabble_score import scrabble_scorecard, ScrabbleScore

# Tests adapted from `problem-specifications//canonical-data.json`


class ScrabbleScoreTest(unittest.TestCase):

    '''
    Copied from scrabble_score_test.py and modified to use ScrabbleScore.score()
    '''

    def test_lowercase_letter(self):
        score = ScrabbleScore("a", scrabble_scorecard(), [], [], False, False).score()
        self.assertEqual(score, 1)

    def test_uppercase_letter(self):
        score = ScrabbleScore("A", scrabble_scorecard(), [], [], False, False).score()
        self.assertEqual(score, 1)

    def test_valuable_letter(self):
        score = ScrabbleScore("f", scrabble_scorecard(), [], [], False, False).score()
        self.assertEqual(score, 4)

    def test_short_word(self):
        score = ScrabbleScore("at", scrabble_scorecard(), [], [], False, False).score()
        self.assertEqual(score, 2)

    def test_short_valuable_word(self):
        score = ScrabbleScore("zoo", scrabble_scorecard(), [], [], False, False).score()
        self.assertEqual(score, 12)

    def test_medium_word(self):
        score = ScrabbleScore("street", scrabble_scorecard(), [], [], False, False).score()
        self.assertEqual(score, 6)

    def test_medium_valuable_word(self):
        score = ScrabbleScore("quirky", scrabble_scorecard(), [], [], False, False).score()
        self.assertEqual(score, 22)

    def test_long_mixed_case_word(self):
        score = ScrabbleScore("OxyphenButazone", scrabble_scorecard(), [], [], False, False).score()
        self.assertEqual(score, 41)

    def test_english_like_word(self):
        score = ScrabbleScore("pinata", scrabble_scorecard(), [], [], False, False).score()
        self.assertEqual(score, 8)

    def test_empty_input(self):
        score = ScrabbleScore("", scrabble_scorecard(), [], [], False, False).score()
        self.assertEqual(score, 0)

    def test_entire_alphabet_available(self):
        score = ScrabbleScore("abcdefghijklmnopqrstuvwxyz", scrabble_scorecard(), [], [], False, False).score()
        self.assertEqual(score, 87)

    '''
    New unit tests based on those above, but modified to test double/triple letters/words
    '''

    def test_lowercase_letter_doubled(self):
        score = ScrabbleScore("a", scrabble_scorecard(), ['a'], [], False, False).score()
        self.assertEqual(score, 2)

    def test_uppercase_letter_tripled(self):
        score = ScrabbleScore("A", scrabble_scorecard(), ['a'], [], False, False).score()
        self.assertEqual(score, 2)

    def test_valuable_letter_double_all(self):
        score = ScrabbleScore("f", scrabble_scorecard(), ['F'], [], True, False).score()
        self.assertEqual(score, 16)

    def test_short_word_tripled(self):
        score = ScrabbleScore("at", scrabble_scorecard(), [], [], False, True).score()
        self.assertEqual(score, 6) # 2 * 3

    def test_short_valuable_word_doublel_triplew(self):
        score = ScrabbleScore("zoo", scrabble_scorecard(), ['Z'], [], False, True).score()
        self.assertEqual(score, 66) # (z = 10) * 3 + 2(o = 1) * 3 = 66

    def test_medium_word_doubled_letters(self):
        score = ScrabbleScore("street", scrabble_scorecard(), ['s', 't'], [], False, False).score()
        self.assertEqual(score, 8) # 6 + 1 (doubled s) + 1 (double t) = 8

    def test_medium_valuable_word_tripledy(self):
        score = ScrabbleScore("quirky", scrabble_scorecard(), [], ['Y'], False, False).score()
        self.assertEqual(score, 30) # quirky = 22 + (y = 4, so 8 bonus points) = 30 

    def test_english_like_word(self):
        score = ScrabbleScore("pinata", scrabble_scorecard(), ['a'], ['p'], True, False).score()
        self.assertEqual(score, 30) # pinata = 8 + 1 (double a) + 6 (tripled p) * 2 = 15 * 2 = 30

if __name__ == "__main__":
    unittest.main()
