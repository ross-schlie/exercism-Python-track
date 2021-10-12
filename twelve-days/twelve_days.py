"""exercism twelve-days module."""


NTH = {
        1: "first",
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth",
        9: "ninth",
        10: "tenth",
        11: "eleventh",
        12: "twelfth"
}
"""Ordinals for days of Xmas"""

VERSES = {
        12: 'twelve Drummers Drumming',
        11: 'eleven Pipers Piping',
        10: 'ten Lords-a-Leaping',
        9: 'nine Ladies Dancing',
        8: 'eight Maids-a-Milking',
        7: 'seven Swans-a-Swimming',
        6: 'six Geese-a-Laying',
        5: 'five Gold Rings',
        4: 'four Calling Birds',
        3: 'three French Hens',
        2: 'two Turtle Doves',
        1: 'a Partridge in a Pear Tree'
}
"""Verses possible to sing"""

def recite(start_verse, end_verse):
    """Recite the verses of Twelve days of Xmas

    This function recurses for each verse in between start and end

    Parameters
    ----------
    arg1 : int
        The first verse to sing

    arg2 : int
        The last verse to sing

    Returns
    ------
    string
        A string containing the verses to be sung.

    """

    song = 'On the ' \
            + NTH[start_verse] \
            + ' day of Christmas my true love gave to me: '
    for verse in range(start_verse, 0, -1):
        song += VERSES[verse]
        if verse > 1:
            song += ', '

        if verse == 2 and start_verse > 1:
            song += 'and '

    song += '.'
    song = [song]
    # Recurse for other verses
    if start_verse != end_verse:
        for i in range(start_verse + 1, end_verse + 1):
            song.append(recite(i, i)[0])

    return song
