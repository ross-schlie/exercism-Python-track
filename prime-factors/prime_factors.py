"""exercism prime factors module."""

def factors(value):
    if value in [2, 3]:
        return [value]

    primes = []
    potential = range(2, value)
    while value > 1:
        for factor in potential:
            if value % factor == 0:
                primes.append(factor)
                value = value / factor
                break;

            if value <= 1:
                break;

    primes.sort()
    return primes
