"""exercism word count module."""


# from collections import Counter
import re

def count_words(sentence):
    """Count the words in a given sentence.

    Parameters
    ----------
    arg1 : string
        Sentence to count words of.

    Returns
    ------
    dictioary
        Containing the unique words and their count.

    >>> count_words("word")
    {"word": 1}

    >>> count_words("one fish two fish red fish blue fish")
    {"one": 1, "fish": 4, "two": 1, "red": 1, "blue": 1}

    # Started out thinking of using filter and the lowercasing
    # + replacing punctuation and splitting the string
    # but realized using regex would be simpler
    """
    # punctuation = list(filter(lambda c: c.isalpha() != True, sentence))
    # print(punctuation)
    # words = sentence.lower().replace(punctuation, ' ').split()

    # \w+'?-?\w+ should match 'words' having contractions/hyphenations
    # and normal words longer than 1 characters
    # and |\w+ means it should also find single character 'words'

    # using .replace for underscores is cheap?
    words = re.findall(r"\w+-?'?\w+|\w+", sentence.lower().replace('_', ' '))
    uniquewords = set(words)
    countedwords = {}
    # c = Counter()
    for w in uniquewords:
        # c[w] = words.count(w)
        countedwords[w] = words.count(w)

    return countedwords
