'''
# Pangram

Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan gramma,
"every letter") is a sentence using every letter of the alphabet at least once.
The best known English pangram is:
> The quick brown fox jumps over the lazy dog.

The alphabet used consists of ASCII letters `a` to `z`, inclusive, and is case
insensitive. Input will not contain non-ASCII symbols.
'''

import string

def is_pangram(sentence):
    # filter(lambda c: sentence.lower().find(c) == -1, string.ascii_lowercase)
    for char in string.ascii_lowercase:
        if sentence.lower().find(char) == -1:
            return False

    return True

# print(is_pangram("hello"))
# print(is_pangram('"Five quacking Zephyrs jolt my wax bed."'))