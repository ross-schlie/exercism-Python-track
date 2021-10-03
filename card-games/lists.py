"""exercism card games (lists) module."""

def get_rounds(number):
    """
    Get list of current and next rounds

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    """
    List of poker rounds across tables

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """
    Find prior rounds

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """

    return rounds.count(number) > 0


def card_average(hand):
    """
    Find the average value of a hand

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """
    Find if the median or approximate average is the same as the average

    :param hand: list - cards in hand.
    :return: bool - is approximate average the same as true average?
    """

    hand_size = len(hand)
    average = card_average(hand)
    median_index = hand_size // 2
    median = hand[median_index]
    approx = (hand[0] + hand[hand_size - 1]) / 2
    return average in [median, approx]


def average_even_is_average_odd(hand):
    """
    Find if the average of odd cards in a hand is the same as the average of even cards

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    return card_average(hand[0::2]) == card_average(hand[1::2])


def maybe_double_last(hand):
    """
    Find if the value of a 'bonus round' hand

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    JACK_VALUE = 11
    while hand.count(JACK_VALUE) > 0:
        index = hand.index(JACK_VALUE)
        hand[index] = JACK_VALUE * 2

    return hand
