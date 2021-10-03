"""exercism sublist module."""

"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = -5
SUPERLIST = 5
EQUAL = 0
UNEQUAL = 1

def is_sublist_equal(list_one, list_two):
    """
    Compare the values of two lists of equal length.

    :param list_one: list - A list
    :param list_two: list - A different list
    :return EQUAL or UNEQUAL - If all values match, or not.

    >>> is_sublist_equal([0], [0])
    EQUAL

    >>> is_sublist_equal([1], [0])
    UNEQUAL

    Iterate over values in each list and compare them
    Assumes lists are of equal sizes
    """
    for index, value in enumerate(list_one):
        if value != list_two[index]:
            return UNEQUAL

    # Otherwise, all values matched, so it's equal
    return EQUAL

def trim_and_compare_list(shorter_list, longer_list):
    """
    Pop values from a longer list to try and make it comparable to a shorter list.

    :param shorter_list: list - A list
    :param longer_list: list - A longer list
    :return EQUAL or UNEQUAL - returns UNEQUAL if unable to shorten them to equal lengths
        If they are shortened to the same size, returns the comparison from is_sublist_equal

    >>> trim_and_compare_list([0], [0, 1])
    EQUAL

    >>> trim_and_compare_list([1], [0, 2])
    UNEQUAL

    Drop elements from the back of the longer_list or from the front (via reverse())
    """

    unequal = True
    reversed = False
    while(unequal):
        if len(shorter_list) == 0 or len(longer_list) == 0:
            break

        if shorter_list[-1] != longer_list[-1]:
            longer_list.pop()
            reversed = False

            if len(shorter_list) == len(longer_list):
                unequal = False
        else:
            if reversed:
                for index, val in enumerate(shorter_list):
                    if shorter_list[index] != longer_list[index]:
                        shorter_list.reverse()
                        longer_list.reverse()
                        longer_list.pop()
                        reversed = True
                        continue
                    elif shorter_list[-index] != longer_list[-index]:
                        longer_list.pop()
                        continue

                continue
                #break

            shorter_list.reverse()
            longer_list.reverse()
            reversed = True

    if len(shorter_list) != len(longer_list):
        return UNEQUAL

    return is_sublist_equal(shorter_list, longer_list)

def sublist(list_one, list_two):
    """
    Determine the relationship between 2 lists.

    :param list_one: list - A list
    :param list_two: list - A different list
    :return ENUM [SUBLIST, SUPERLIST, EQUAL, UNEQUAL] or None - How one list compares to another

    Determine if the first list is contained within the second list,
    if the second list is contained within the first list,
    if both lists are contained within each other or if none of these are true.

    Specifically, a list A is a sublist of list B if by dropping 0 or more elements
    from the front of B and 0 or more elements from the back of B
    you get a list that's completely equal to A.
    """

    if len(list_one) == len(list_two):
        return is_sublist_equal(list_one, list_two)
    elif len(list_one) < len(list_two):
        if len(list_one) == 0:
            return SUBLIST

        if trim_and_compare_list(list_one, list_two) == EQUAL:
            return SUBLIST

        return UNEQUAL
    elif len(list_one) > len(list_two):
        if len(list_two) == 0:
            return SUPERLIST

        if trim_and_compare_list(list_two, list_one) == EQUAL:
            return SUPERLIST

        return UNEQUAL

    return None
