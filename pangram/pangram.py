"""exercism pangram module."""


import string

def is_pangram(sentence):
    """
    Is the given sentence a pangram?

    :param sentence str - The sentence to evaluate.
    :return bool - Whether the provided sentence is a pangram or not.
    """
    # filter(lambda c: sentence.lower().find(c) == -1, string.ascii_lowercase)
    for char in string.ascii_lowercase:
        if sentence.lower().find(char) == -1:
            return False

    return True