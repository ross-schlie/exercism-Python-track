import unittest

from scrabble_score import SCORECARD, ScrabbleScore

# Tests adapted from `problem-specifications//canonical-data.json`

class ScrabbleScoreTest(unittest.TestCase):

    '''
    Copied from scrabble_score_test.py and modified to use ScrabbleScore.score()
    '''

    def test_lowercase_letter(self):
        score = ScrabbleScore().score("a", [], [], False, False)
        self.assertEqual(score, 1)

    def test_uppercase_letter(self):
        score = ScrabbleScore().score("A", [], [], False, False)
        self.assertEqual(score, 1)

    def test_valuable_letter(self):
        score = ScrabbleScore().score("f", [], [], False, False)
        self.assertEqual(score, 4)

    def test_short_word(self):
        score = ScrabbleScore().score("at", [], [], False, False)
        self.assertEqual(score, 2)

    def test_short_valuable_word(self):
        score = ScrabbleScore().score("zoo", [], [], False, False)
        self.assertEqual(score, 12)

    def test_medium_word(self):
        score = ScrabbleScore().score("street", [], [], False, False)
        self.assertEqual(score, 6)

    def test_medium_valuable_word(self):
        score = ScrabbleScore().score("quirky", [], [], False, False)
        self.assertEqual(score, 22)

    def test_long_mixed_case_word(self):
        score = ScrabbleScore().score("OxyphenButazone", [], [], False, False)
        self.assertEqual(score, 41)

    def test_english_like_word(self):
        score = ScrabbleScore().score("pinata", [], [], False, False)
        self.assertEqual(score, 8)

    def test_empty_input(self):
        score = ScrabbleScore().score("", [], [], False, False)
        self.assertEqual(score, 0)

    def test_entire_alphabet_available(self):
        scrable_scorer = ScrabbleScore()
        score = scrable_scorer.score("abcdefghijklmnopqrstuvwxyz", [], [], 
            False, False)
        self.assertEqual(score, 87)

    '''
    New unit tests based on those above, but modified to test double/triple letters/words
    '''

    def test_lowercase_letter_doubled(self):
        score = ScrabbleScore().score("a", ['a'], [], False, False)
        self.assertEqual(score, 2)

    def test_uppercase_letter_tripled(self):
        score = ScrabbleScore().score("A", ['a'], [], False, False)
        self.assertEqual(score, 2)

    def test_valuable_letter_double_all(self):
        score = ScrabbleScore().score("f", ['F'], [], True, False)
        self.assertEqual(score, 16)

    def test_short_word_tripled(self):
        score = ScrabbleScore().score("at", [], [], False, True)
        self.assertEqual(score, 6) 
        # 2 * 3

    def test_short_valuable_word_doublel_triplew(self):
        score = ScrabbleScore().score("zoo", ['Z'], [], False, True)
        self.assertEqual(score, 66) 
        # (z = 10) * 3 + 2(o = 1) * 3 = 66

    def test_medium_word_doubled_letters(self):
        score = ScrabbleScore().score("street", ['s', 't'], [], False, False)
        self.assertEqual(score, 8) 
        # 6 + 1 (doubled s) + 1 (double t) = 8

    def test_medium_valuable_word_tripledy(self):
        score = ScrabbleScore().score("quirky", [], ['Y'], False, False)
        self.assertEqual(score, 30) 
        # quirky = 22 + (y = 4, so 8 bonus points) = 30 

    def test_english_like_word(self):
        score = ScrabbleScore().score("pinata", ['a'], ['p'], True, False)
        self.assertEqual(score, 30) 
        # pinata = 8 + 1 (double a) + 6 (tripled p) * 2 = 15 * 2 = 30

if __name__ == "__main__":
    unittest.main()
