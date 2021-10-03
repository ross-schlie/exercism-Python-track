"""exercism sum of multiples module."""


def sum_of_multiples(limit, multiples):
    """
    Find the sum of all the unique multiples of particular numbers
        up to but not including that number.

    :param limit int - The highest resulting product of multiples.
    :param multiples list - The multiples to multiply and sum.
    :return int - The total or sum of multiples that meet the criteria.
    """

    total = 0
    if len(multiples) == 0:
        return total

    factor = 1
    products = {}

    limit_reached = False
    last_change_counter = 0
    while not limit_reached:
        last_total = total
        for index, number in enumerate(multiples):
            result = number * factor

            # skip results we already stored
            if products.get(result) is not None:
                continue

            products[result] = number
            if result < limit:
                total += result
            elif index == 0:
                # Cancle out if the smallest (index 0) multiple exceeds limit
                limit_reached = True

        factor += 1
        # cancel out if not increasing over time
        if last_change_counter > 10:
            break

        if last_total == total:
            last_change_counter += 1
        else:
            last_change_counter = 0

    return total
