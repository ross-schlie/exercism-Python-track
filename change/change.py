"""exercism change module."""


def find_fewest_coins(coins, target):
    """
    Find the smalles/shortest combination of coins to make change.

    :param coins list - Possible coin denominations to use.
    :param target int - Amount the combination of coins should add up to.
    :return list - List of coin denominations

    Raises ValueError when target is a negative number
    Raises ValueError when no combination is possible
    """

    if target < 0:
        raise ValueError("Cannot return negative amount.")

    coins.sort(reverse=True)
    coin_change = get_coin_combinations(coins, target)
    exact_change = get_shortest(coin_change, target)

    if sum(exact_change) != target:
        raise ValueError("Cannot give exact change.")

    exact_change.sort()
    return exact_change

def get_coin_combinations(coins, target):
    """
    Build a list of combinations for change to provide.

    :param coin_change list - Possible coin denominations to use.
    :param target int - Amount the combination of coins should add up to.
    :return list - List of tuples cointaining coin denominations, count and remainder.
    """

    exact_change = []
    for denomination in coins:
        if target / denomination >= 1:
            denomination_coins = target // denomination
            remainder = target % denomination
            sub = []
            if remainder > 0:
                sub = get_coin_combinations(coins, remainder)
                # skip if unable to find a combination for remainder
                if len(sub) == 0:
                    continue

            exact_change.append((denomination, denomination_coins, sub))

    # When the above fails, and the target is an odd number
    # build combinations with odd numbers as a base.
    if len(exact_change) == 0 and target % 2 == 1:
        exact_change = get_odd_based_combinations(coins, target)

    return exact_change

def get_shortest(coin_change, target):
    """
    Given a coin combination, find the combination with smallest number of coins.

    :param coin_change list - List of tuples cointaining coin denominations, count and remainder.
    :param target int - Amount the combination of coins should add up to.
    :return list - List containing fewest number of coins from the combinations.
    """

    change_to_give = []
    number_of_coins = target + 1
    for results in coin_change:
        denomination = results[0]
        denomination_coins = results[1]
        remainder = results[2]

        remainder_coin_count = 0
        remainder_coins = []
        if len(remainder) > 0:
            remainder_coins = get_shortest(remainder, target)
            remainder_coin_count = len(remainder_coins)

        if denomination_coins + remainder_coin_count < number_of_coins:
            number_of_coins = denomination_coins + remainder_coin_count
            change_to_give = [denomination] * denomination_coins
            change_to_give.extend(remainder_coins)

    return change_to_give

def get_odd_based_combinations(coins, target):
    """
    Build a list of combinations for change to provide based on odd numbered coins.

    :param coins list - Possible coin denominations to use.
    :param target int - Amount the combination of coins should add up to.
    :return list - List of tuples cointaining coin denominations, count and remainder.

    Called when no coin change combinations are found normally.
    """

    exact_change = []
    salts = odd_coins(coins)

    for salt in salts:
        if salt < target:
            salt_multiples = 1
            salt_product = salt * salt_multiples
            while salt_product < target:
                salted_change = get_coin_combinations(coins, target - salt_product)
                if len(salted_change) > 0:
                    exact_change.extend([(salt, salt_multiples, salted_change)])

                salt_multiples += 1
                salt_product = salt * salt_multiples

    return exact_change

def odd_coins(coins):
    """
    Filter the coin denominations and retrieve only odd-numbered ones.

    :param coins list - Possible coin denominations to use.
    :return list - The odd coin denominations.
    """
    odd_ones = []
    for denomination in coins:
        if denomination % 2 == 1:
            odd_ones.append(denomination)

    return odd_ones
