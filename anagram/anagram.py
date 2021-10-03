"""exercism anagram module."""


def find_anagrams(word, candidates):
    """
    Find an anagram of a word among the provided candidates.

    :param word string - the word to find an anagram of.
    :param candidates list - list containing candidates for anagram of the word.
    :return list - anagram(s) of the provided word.
    """

    word = word.lower()
    anagrams = []
    candidates_trimmed = []
    for candidate in candidates:
        # skip any candidates that are the same as the original
        if candidate.lower() == word:
            continue

        # skip any candidates that cannot be anagrams due to length
        if len(candidate) != len(word):
            continue

        # otherwise we can consider it
        candidates_trimmed.append(candidate)

    for candidate in candidates_trimmed:
        test_candidate = candidate.lower()
        matches = True
        # would it be more efficient to build a dictionary?
        for char in set(word):
            # compare the number of times a character occurs,
            # if they aren't the same, it's not anagram
            if word.count(char) != test_candidate.count(char):
                matches = False
                break

        # all chars must have matched counts, so it's an anagram
        if matches:
            anagrams.append(candidate)

    return anagrams
