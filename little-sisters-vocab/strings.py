"""exercism little sisters vocabulary (strings) module."""

def add_prefix_un(word):
    """
    Make negative, or "not" words by adding un to them

    :param word: str of a root word
    :return:  str of root word with un prefix

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """

    return 'un' + word


def make_word_groups(vocab_words):
    """
    Add predixes to word groups

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    """

    prefix = vocab_words[0]
    words = prefix
    for word in vocab_words[1::]:
        words += ' :: ' + prefix + word

    return words


def remove_suffix_ness(word):
    """
    Remove a suffix from a word

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.
    """

    result = word
    if word.endswith('ness'):
        if word[-5] in ['a', 'e', 'i', 'o', 'u']:
            result = word[0:-5] + 'y'
        else:
            result = word[0:-4]

    return result


def noun_to_verb(sentence, index):
    """
    Extract and transform a word

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """

    verb = sentence.split(' ')[index]
    return verb.replace('.', '') + 'en'
