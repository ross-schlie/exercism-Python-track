"""exercism scrabble score module."""


SCORECARD = dict([(x, 1) for x in 'AEIOULNRST']
              + [(x, 2) for x in 'DG']
              + [(x, 3) for x in 'BCMP']
              + [(x, 4) for x in 'FHVWY']
              + [(x, 5) for x in 'K']
              + [(x, 8) for x in 'JX']
              + [(x, 10) for x in 'QZ'])
"""
Dictionary with the scrabble's scoring for each letter.

Updated with much cooler dict creation from hnlee's solution
"""

def score(word):
    """Given a word, (scrabble) score it based on the rules and scorecard.

    For each letter in a word, get the corresponding points and sum them.

    Parameters
    ----------
    arg1 : string
        A word to score.

    Returns
    ------
    int
        The sum of the score for the word.

    """

    scores = []
    word = word.upper()
    for c in word:
        scores.append(SCORECARD.get(c, 0))

    return sum(scores)

class ScrabbleScore:

    SCORECARD = dict([(x, 1) for x in 'AEIOULNRST']
              + [(x, 2) for x in 'DG']
              + [(x, 3) for x in 'BCMP']
              + [(x, 4) for x in 'FHVWY']
              + [(x, 5) for x in 'K']
              + [(x, 8) for x in 'JX']
              + [(x, 10) for x in 'QZ'])

    def __init__(self):
        """Score a given scrable word

        Scrabble scoring for a word based on SCORECARD while taking into
        account double/tripple letters and words.

        >>> ScrabbleScore().score('quirk', ['A', 'Y'], ['B'], False, False)
        30

        See scrabble_score_test_extension.py for unit tests
        """
        pass

    def _modify_score_double_letter(self, double_letters):
        # Since score already calculate the base amount of points
        # for each letter, don't double it, just add them
        bonuscore = 0
        for c in double_letters:
            bonuscore += self.SCORECARD.get(c.upper(), 0)
        return bonuscore

    def _modify_score_triple_letter(self, triple_letters):
        # Since score already calculate the base amount of points
        # for each letter, don't triple it, do double it
        bonuscore = 0
        for c in triple_letters:
            bonuscore += self.SCORECARD.get(c.upper(), 0) * 2
        return bonuscore

    def score(self, word, double_letters, triple_letters,
            double_word, triple_word):
        """Score a given scrable word!

        Scrabble scoring for a word based on SCORECARD while taking into
        account double/tripple letters and words.

        For each letter in a word, get the corresponding points
        Detect any double or triple letters to adjust score
        _modify_score_double_letter
        _modify_score_triple_letter
        Detect double or triple word to adjust score

        Parameters
        ----------
        arg1 : string
            A word to score.

        arg2 : list
            Letters than should get double points.

        arg3 : bool
            Letters than should get triple points.

        arg4 : bool
            Word is worth double points, or not.

        arg5 : bool
            Word is worth triple points, or not.

        Returns
        ------
        int
            The sum of the score for the word.

        >>> ScrabbleScore().score('quirk', ['A', 'Y'], ['B'], False, False)
        30

        See scrabble_score_test_extension.py for unit tests
        """

        score = 0
        scores = []
        for c in word.upper():
            scores.append(self.SCORECARD.get(c, 0))

        score = sum(scores)
        score += self._modify_score_double_letter(double_letters)
        score += self._modify_score_triple_letter(triple_letters)

        if double_word:
            score = score * 2

        if triple_word:
            score = score * 3

        return score
