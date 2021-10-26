"""exercism sieve of eratosthenes module."""


def primes(limit):
    """
    Use the Sieve of Eratosthenes to find all the primes from 2 up to a given number.

    A simple, ancient algorithm for finding all prime numbers up to any given limit.
    It does so by iteratively marking as composite (i.e. not prime) the multiples of each prime,
    starting with the multiples of 2. It does not use any division or remainder operation.

    The algorithm consists of repeating the following over and over:
    - take the next available unmarked number in your list (it is prime)
    - mark all the multiples of that number (they are not prime)
    Repeat until you have processed each number in your range.

    :param limit int - the limit to find primes up to.
    :return list - list of prime numbers.
    """
    not_prime = set()
    primes = []
    for number in range(2, limit + 1):
        # skip all numbers that have been marked as not prime
        if number in not_prime:
            continue

        primes.append(number)

        multiplier = 1
        multiple = number
        while multiple < limit:
            multiplier += 1
            multiple = number * multiplier
            not_prime.add(multiple)

    return primes
