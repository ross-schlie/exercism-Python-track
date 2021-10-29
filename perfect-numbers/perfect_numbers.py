"""exercism perfect numbers module."""

def classify(number):
    """
    Implement a way to determine whether a given number is **perfect**, **abundant** or **deficient**.

    :param number int - The number to classify.
    :return string - The number's classification; one of: "deficient", "perfect" or "abundant".

    The aliquot sum is defined as the sum of the factors of a number not including the number itself.
    For example, the aliquot sum of 15 is (1 + 3 + 5) = 9
    - **Perfect**: aliquot sum = number
    - 6 is a perfect number because (1 + 2 + 3) = 6
    - 28 is a perfect number because (1 + 2 + 4 + 7 + 14) = 28
    - **Abundant**: aliquot sum > number
    - 12 is an abundant number because (1 + 2 + 3 + 4 + 6) = 16
    - 24 is an abundant number because (1 + 2 + 3 + 4 + 6 + 8 + 12) = 36
    - **Deficient**: aliquot sum < number
    - 8 is a deficient number because (1 + 2 + 4) = 7
    - Prime numbers are deficient
    """

    if number < 1:
        raise ValueError("Must be a positive integer.")

    classification = "deficient"

    # Prime numbers are deficient
    factors = get_factors(number)
    if len(factors) == 1:
        return classification

    factor_sum = sum(factors)
    if factor_sum == number:
        classification = "perfect"
    elif factor_sum > number:
        classification = "abundant"

    return classification

def get_factors(number):
    """Get the factors of a number."""
    factors = [1]
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            factors.append(i)

    return factors

