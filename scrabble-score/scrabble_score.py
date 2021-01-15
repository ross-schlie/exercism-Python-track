'''
Introduction
Given a word, compute the scrabble score for that word.

Letter Values
You'll need these:

Letter                           Value
A, E, I, O, U, L, N, R, S, T       1
D, G                               2
B, C, M, P                         3
F, H, V, W, Y                      4
K                                  5
J, X                               8
Q, Z                               10
Examples
"cabbage" should be scored as worth 14 points:

3 points for C
1 point for A, twice
3 points for B, twice
2 points for G
1 point for E
And to total:

3 + 2*1 + 2*3 + 2 + 1
= 3 + 2 + 6 + 3
= 5 + 9
= 14
Extensions
You can play a double or a triple letter.
You can play a double or a triple word.
'''

def scrabble_scorecard():
    '''
    Build out a dictionary with the scrabble's scoring for each letter
    * Updated with much cooler dict creation from hnlee's solution

    :return: The dictionary containing each letter that can get a score and how many points for them
    :rtype: dict
    '''
    return dict([(x, 1) for x in 'AEIOULNRST'] +
              [(x, 2) for x in 'DG'] +
              [(x, 3) for x in 'BCMP'] +
              [(x, 4) for x in 'FHVWY'] +
              [(x, 5) for x in 'K'] +
              [(x, 8) for x in 'JX'] + 
              [(x, 10) for x in 'QZ'])

def score(word):
    '''
    For each letter in a word, get the corresponding points
    return the sum of the points

    :return: The sum of the score for the word
    :rtype: int
    '''
    scorecard = scrabble_scorecard()
    scores = []
    word = word.upper()
    for c in word:
        scores.append(scorecard.get(c, 0))

    return sum(scores)

class ScrabbleScore:

    def __init__(self, word, scorecard, double_letters, triple_letters, double_word, triple_word):
        """
        todo

        :param word: the word to score 
        :param scorecard: dict built by scrabble_scorecard 
        :param double_letters: list of letters than should get double points
        :param triple_letters: list of letters than should get triple points
        :param double_word: if the word is a double word or not
        :param triple_word: if the word is a triple word or not

        :type word: string
        :type scorecard: dict
        :type double_letters: list
        :type triple_letters: list
        :type double_word: boolean
        :type triple_word: boolean

        :Example: word: 'quirk'
        :Example: double_letters: ['A', 'Y']
        :Example: triple_letters: ['B']

        see also scrabble_score_test_extension.py for unit tests
        """

        self.word = word.upper()
        self.scorecard = scorecard
        self.double_letters = double_letters
        self.triple_letters = triple_letters
        self.is_double_word = double_word
        self.is_triple_word = triple_word

    def modify_score_double_letter(self):
        '''
        Since score already calculate the base amount of points for each letter, don't double it
        :return: The additional points for any double letters
        :rtype: int
        '''
        bonuscore = 0
        for c in self.double_letters:
            bonuscore += self.scorecard.get(c.upper(), 0)
        return bonuscore

    def modify_score_triple_letter(self):
        '''
        Since score already calculate the base amount of points for each letter, don't triple it
        But do double it
        :return: The additional points for any triple letters
        :rtype: int
        '''
        bonuscore = 0
        for c in self.triple_letters:
            bonuscore += self.scorecard.get(c.upper(), 0) * 2
        return bonuscore

    def score(self):
        '''
        For each letter in a word, get the corresponding points
        Detect any double or triple letters to adjust score @ modify_score_double_letter
        Detect double or triple word to adjust score @ modify_score_triple_letter
        return the sum of the points

        :return: The sum of the score for the word
        :rtype: int
        '''
        score = 0
        scores = []
        for c in self.word:
            scores.append(self.scorecard.get(c, 0))

        # base score
        score = sum(scores)
        # modify_score_double_letter
        score += self.modify_score_double_letter()
        # modify_score_triple_letter
        score += self.modify_score_triple_letter()

        if self.is_double_word:
            score = score * 2

        if self.is_triple_word:
            score = score * 3

        return score

# Test code
# points = score("") # 0
# points = score("quirky") # 22
# print(points)

# scrabblescore = ScrabbleScore("quirky", scrabble_scorecard(), ['A', 'Y'], ['B'], False, True).score() # 22 base + (double for Y is extra 4) * 3 = 78
# scrabblescore = ScrabbleScore("sass", scrabble_scorecard(), ['S', 'S'], [], False, False).score() # 4 base + (double for s twice is extra 2) = 6
# scrabblescore = ScrabbleScore("sassy", scrabble_scorecard(), ['S', 'S'], [], True, False).score() # 8 base + (double for s twice is extra 2) * 2 = 20
# print(scrabblescore)