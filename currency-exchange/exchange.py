"""exercism currency exchange module."""

def exchange_money(budget, exchange_rate):
    """
    Estimated value of the foreign currency you can receive

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - estimated value of the foreign currency you can receive

    This function should return the estimated value of the foreign currency you
    can receive based on your budget and the current exchange rate.
    """

    return float(budget / exchange_rate)


def get_change(budget, exchanging_value):
    """
    The amount left of your starting currency after exchanging exchanging_value.

    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging
    """

    return float(budget - exchanging_value)


def get_value_of_bills(denomination, number_of_bills):
    """
    The total value of bills you now have.

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have
    """

    return denomination * number_of_bills


def get_number_of_bills(budget, denomination):
    """
    The number of bills after exchanging all your money.

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money
    """

    return budget // denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    The maximum value you can get considering the budget, exchange_rate, spread, & denomination.

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get
    """

    exchange_fee = exchange_rate * (spread / 100)
    foreign_currency = exchange_money(budget, exchange_rate + exchange_fee)
    exchanged_bills = get_number_of_bills(foreign_currency, denomination)
    return int(get_value_of_bills(denomination, exchanged_bills))


def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    The unexchangeable value considering the budget, exchange_rate, spread, & denomination.

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - unexchangeable value
    """

    exchange_fee = exchange_rate * (spread / 100)
    foreign_currency = exchange_money(budget, exchange_rate + exchange_fee)
    exchanged_bills = get_number_of_bills(foreign_currency, denomination)
    result = get_value_of_bills(denomination, exchanged_bills)
    return int(foreign_currency - result)
