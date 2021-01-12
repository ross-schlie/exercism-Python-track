'''
Introduction
To try and encourage more sales of different books from a popular 5 book series, 
a bookshop has decided to offer discounts on multiple book purchases.

One copy of any of the five books costs $8.

If, however, you buy two different books, you get a 5% discount on those two books.

If you buy 3 different books, you get a 10% discount.

If you buy 4 different books, you get a 20% discount.

If you buy all 5, you get a 25% discount.

Note: that if you buy four books, of which 3 are different titles, 
you get a 10% discount on the 3 that form part of a set, but the fourth book still costs $8.

Your mission is to write a piece of code to calculate the price of any conceivable shopping basket 
(containing only books of the same series), giving as big a discount as possible.

For example, how much does this basket of books cost?

2 copies of the first book
2 copies of the second book
2 copies of the third book
1 copy of the fourth book
1 copy of the fifth book
One way of grouping these 8 books is:

1 group of 5 --> 25% discount (1st,2nd,3rd,4th,5th)
+1 group of 3 --> 10% discount (1st,2nd,3rd)
This would give a total of:

5 books at a 25% discount
+3 books at a 10% discount
Resulting in:

5 x (8 - 2.00) == 5 x 6.00 == $30.00
+3 x (8 - 0.80) == 3 x 7.20 == $21.60
For a total of $51.60

However, a different way to group these 8 books is:

1 group of 4 books --> 20% discount (1st,2nd,3rd,4th)
+1 group of 4 books --> 20% discount (1st,2nd,3rd,5th)
This would give a total of:

4 books at a 20% discount
+4 books at a 20% discount
Resulting in:

4 x (8 - 1.60) == 4 x 6.40 == $25.60
+4 x (8 - 1.60) == 4 x 6.40 == $25.60
For a total of $51.20

And $51.20 is the price with the biggest discount.
'''

from collections import Counter
from itertools import filterfalse

BASEPRICE = 800
DISCOUNTS = { 2: 0.05, 3: 0.10, 4: 0.20, 5: 0.25 }

def total(basket):
    '''
    Calculate and return the cost of the 'books' in the basket, while applying the highest discount possible
    BASEPRICE for book base price
    DISCOUNTS for each unique combination of books

    Parameters: 
    arg1 (basket) list: A list of 'books' that are being 'sold'. Highly likely to contain duplicates
  
    Returns: 
    int: The price of the books being sold after discounting

    :Example: empty basket will return 0
    :Example: single book in basket will return 800
    :Example: 5 unique books will return  3000 | ((800 * 5) = 4000) - ((4000 * 25%) = 1000) = 3000
    :Example: 2 unique books and 1 duplicate will return 2320 | (800 * 3) = ((3 * 800) = 2400) - (((2 * 800) = 1600) * 5% = 80)
    '''
    if len(basket) == 0:
        return 0

    subtotal = BASEPRICE * len(basket)
    best_discount_combination = highest_discount(basket)
    discounts_available = DISCOUNTS.keys()
    for bookset in best_discount_combination:
        numbooks = len(bookset)
        if numbooks in discounts_available:
            subtotal -= int(DISCOUNTS[numbooks] * (BASEPRICE * numbooks))

    return subtotal

def highest_discount(basket):
    '''
    Based on the combination of discounts, try to find which combination will get the highest discount
    * This currently fails for test case where 2 groups of 4 and 1 group of 5 would 
        get a bigger discount than 2 groups of 5 and 1 group of 3

    Parameters: 
    arg1 (basket) list: A list of 'books' that are being 'sold'. Highly likely to contain duplicates

    Returns: 
    list: A list containg lists (groups) of books. This is supposed to be the grouping with the largest discount
    '''
    highestdis = 0
    bookgroups = []
    for maxbooks in DISCOUNTS.keys():
         discount, booksets= total_discount(basket.copy(), maxbooks)
         if discount > highestdis:
             highestdis = discount
             bookgroups = booksets
         
    return bookgroups

def total_discount(basket, maxbooks):
    '''
    Calculate the total discount for the users basket of books based on a maximum number of books in a group

    Parameters: 
    arg1 (basket) list: A list of 'books' that are being 'sold'. Highly likely to contain duplicates
    agr2 (maxbooks) int: The maximum number of unique books in a 'group' for discounting purposes

    Returns: 
    int: the amount to be discounted for this grouping of the basket
    list: A list containg lists (groups) of books. This is supposed to be the grouping with the largest discount
    '''
    basketgrp = []
    basket = sorted(basket, key = basket.count, reverse=True)
    while len(basket) > 0:
        uniquebooklist = list(unique_everseen(basket, length=maxbooks-1))
        basketgrp.append(uniquebooklist)
        for book in uniquebooklist:
            basket.remove(book)

    discounttotal = 0
    discounts_available = DISCOUNTS.keys()
    for grp in basketgrp:
        booksingrp = len(grp)
        if booksingrp in discounts_available:
            discounttotal += DISCOUNTS[booksingrp] * (BASEPRICE * booksingrp)

    return int(discounttotal), basketgrp

# from https://docs.python.org/3/library/itertools.html
# more-itertools
# modified to stop at given lenght
def unique_everseen(iterable, key=None, length=1):
    "List unique elements, preserving order. Remember all elements ever seen."
    # unique_everseen('AAAABBBCCDAABBB') --> A B C D
    # unique_everseen('ABBCcAD', str.lower) --> A B C D
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in filterfalse(seen.__contains__, iterable):
            if(len(seen) > length):
                return

            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element