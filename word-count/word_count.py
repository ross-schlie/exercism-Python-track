'''
Introduction
Given a phrase, count the occurrences of each word in that phrase.

For the purposes of this exercise you can expect that a word will always be one of:

A number composed of one or more ASCII digits (ie "0" or "1234") OR
A simple word composed of one or more ASCII letters (ie "a" or "they") OR
A contraction of two simple words joined by a single apostrophe (ie "it's" or "they're")
When counting words you can assume the following rules:

The count is case insensitive (ie "You", "you", and "YOU" are 3 uses of the same word)
The count is unordered; the tests will ignore how words and counts are ordered
Other than the apostrophe in a contraction all forms of punctuation are ignored
The words can be separated by any form of whitespace (ie "\t", "\n", " ")
For example, for the phrase "That's the password: 'PASSWORD 123'!", cried the Special Agent.\nSo I fled. the count would be:

that's: 1
the: 2
password: 2
123: 1
cried: 1
special: 1
agent: 1
so: 1
i: 1
fled: 1
'''

import re

# Started out thinking of using filter and the lowercasing + replacing punctuation and splitting the string
# But realized using regex would be simpler
def count_words(sentence):
    # punctuation = list(filter(lambda c: c.isalpha() != True, sentence))
    # print(punctuation)
    # words = sentence.lower().replace(punctuation, ' ').split()
    
    # \w+'?-?\w+ should match 'words' having contractions/hyphenations and normal words longer than 1 characters
    # and |\w+ means it should also find single character 'words'
    # using .replace for underscores is cheap?
    words = re.findall(r"\w+-?'?\w+|\w+", sentence.lower().replace('_', ' '))
    uniquewords = set(words)
    countedwords = {}
    for w in uniquewords:
        countedwords[w] = words.count(w)

    return countedwords

# testing code
# wordcount = count_words("password, that's the password a six-year would think of.")
# print(wordcount)