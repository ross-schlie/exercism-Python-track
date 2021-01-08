'''
Introduction
Output the lyrics to 'The Twelve Days of Christmas'.

On the first day of Christmas my true love gave to me: 
a Partridge in a Pear Tree.

On the second day of Christmas my true love gave to me: 
two Turtle Doves, and a Partridge in a Pear Tree.

On the third day of Christmas my true love gave to me: 
three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

On the fourth day of Christmas my true love gave to me: 
four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

On the fifth day of Christmas my true love gave to me: 
five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

On the sixth day of Christmas my true love gave to me: 
six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, 
and a Partridge in a Pear Tree.

On the seventh day of Christmas my true love gave to me: 
seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, 
two Turtle Doves, and a Partridge in a Pear Tree.

On the eighth day of Christmas my true love gave to me: 
eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, 
three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

On the ninth day of Christmas my true love gave to me: 
nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, 
four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

On the tenth day of Christmas my true love gave to me: 
ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, 
five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

On the eleventh day of Christmas my true love gave to me: 
eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, 
six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

On the twelfth day of Christmas my true love gave to me: 
twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, 
seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, 
and a Partridge in a Pear Tree.
'''

# Sing!!
# - a dictionary for first -> twelfth
# - another dictionary for the individual 'gift' verses
# - Build the 'verse'
# - if multiple verses were requested, recurse for each individual 'next' verse
def recite(start_verse, end_verse):
    nth = {
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

    verses = {
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

    verse = 'On the ' + nth[start_verse] + ' day of Christmas my true love gave to me: '
    for i in range(start_verse, 0, -1):
        verse += verses[i]
        if i > 1:
            verse += ', '
        
        if i == 2 and start_verse > 1:
            verse += 'and '

    verse += '.'
    song = [verse]
    if start_verse != end_verse:
        for i in range(start_verse + 1, end_verse + 1):
            song.append(recite(i, i)[0])

    return song

# Test
# print(recite(4, 7))