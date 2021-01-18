import string

def is_pangram(sentence):
    """Is the given sentence a pangram?"""
    # filter(lambda c: sentence.lower().find(c) == -1, string.ascii_lowercase)
    for char in string.ascii_lowercase:
        if sentence.lower().find(char) == -1:
            return False

    return True