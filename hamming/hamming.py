"""exercism hamming module."""

def distance(strand_a, strand_b):
    """
    Compare two strings and count the differences.

    :param strand_a string - String representing a strand of DNA.
    :param strand_b string - String representing a different strand of DNA.
    :return int - number of differences between 2 strands.
    """

    if len(strand_a) != len(strand_b):
        raise ValueError("The Hamming distance is only defined for sequences of equal length, "
            " so an attempt to calculate it between sequences of different lengths should not work.")

    dna_compared = zip(strand_a, strand_b)
    num_differences = 0
    for sequence in dna_compared:
        if sequence[0] != sequence[1]:
            num_differences += 1

    return num_differences
