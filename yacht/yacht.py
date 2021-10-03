"""exercism yatch module."""


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


# Score categories.
# Change the values as you see fit.
YACHT = 50
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 23
FOUR_OF_A_KIND = 40
LITTLE_STRAIGHT = 10
BIG_STRAIGHT = 20
CHOICE = 33

def single(value, dice):
    """
    Score the dice based on a single value (1-6).
    """
    points = 0
    for die in dice:
        if die == value:
            points += value

    return points

def full_house(dice):
    """
    Score the dice based on rules for FULL_HOUSE.
    """
    points = 0
    dice.sort()
    first = dice[0]
    last = dice[-1]
    num_first = dice.count(first)
    num_last = dice.count(last)
    if num_first >= 2 and num_last >= 2 and num_first + num_last == len(dice):
        points = sum(dice)

    return points

def straight(start, dice):
    """
    Score the dice based on rules for LITTLE_STRAIGHT or BIG_STRAIGHT.
    """
    dice.sort()
    for die in dice:
        if die != start:
            return 0

        start += 1

    return 30

def four_of_a_kind(dice):
    """
    Score the dice based on rules for FOUR_OF_A_KIND
    """
    points = 0
    dice.sort()
    middle_value = dice[2]
    die_count = 0
    if dice.count(middle_value) >= 4:
        for die in dice:
            if die == middle_value and die_count < 4:
                points += die
                die_count += 1

    return points

def yatch(dice):
    """
    Score the dice based on rules for YACHT.
    """
    points = 0
    if dice.count(dice[0]) == len(dice):
        points = 50

    return points

def score(dice, category):
    """
    Score the game of yatch based on category.

    :param dice list - A list containing the value of each roll of a die (5 dice)
    :param category int - ENUM category matching: YACHT, CHOICE, FOUR_OF_A_KIND
        ONES, TWOS, THREES, FOURS, FIVES, SIXES, FULL_HOUSE, LITTLE_STRAIGHT, BIG_STRAIGHT
    :return int - points scored based on category
    """
    points = 0
    if category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]:
        points = single(category, dice)
    elif category == FULL_HOUSE:
        points = full_house(dice)
    elif category == LITTLE_STRAIGHT:
        points = straight(1, dice)
    elif category == BIG_STRAIGHT:
        points = straight(2, dice)
    elif category == FOUR_OF_A_KIND:
        points = four_of_a_kind(dice)
    elif category == YACHT:
        points = yatch(dice)
    elif category == CHOICE:
        points = sum(dice)

    return points
