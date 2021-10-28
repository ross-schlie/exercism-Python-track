"""exercism diamond module."""


ALPHABET = "abcdefghijklmnopqrstuvwxyz".upper()

def rows(letter):
    """
    Given a letter, it returns a diamond starting with 'A',
    with the supplied letter at the widest point.

    :param letter string - The supplied letter.
    :return string - The Diamond.

    >>> rows('A')
    A

    >>> rows('C')
    ·A··
    ·B·B·
    C···C
    ·B·B·
    ··A··
    """

    diamond = []

    letter_index = ALPHABET.index(letter)
    spaces = letter_index
    space_between = 0
    for i in range(0, letter_index + 1):
        diamond.append(row_text(i, spaces, space_between))
        spaces -= 1
        if i == 0:
            space_between += 1
        else:
            space_between += 2

    spaces += 1
    space_between -= 2
    for i in range(1, letter_index + 1):
        spaces += 1
        if letter_index - i == 1:
            space_between = 1
        else:
            space_between -= 2
        diamond.append(row_text(letter_index - i, spaces, space_between))

    return diamond

def row_text(index, spaces, space_between):
    """Build a text for the diamon for a specied letter (index)."""
    text = " " * spaces + ALPHABET[index]
    if index > 0:
        text += " " * space_between + ALPHABET[index]

    text += " " * spaces
    return text
