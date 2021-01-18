def distance(strand_a, strand_b):
    """Compare two strings (of equal length) and count the differences.
    
    Parameters
    ----------
    arg1 : string
        The first dna strand to compare
    
    arg2 : string
        The first dna for comparison
  
    Returns
    ------ 
    int
        The 'distance' or number of differences between 2 strands of dna

    Raises a ValueError when lengths differ

    >>> distance("", "")
    0

    >>> distance("A", "A")
    0

    >>> distance("G", "T")
    1

    >>> distance("AATG", "AAA")
    ValueError

    """
    if len(strand_a) != len(strand_b):
        raise ValueError("The Hamming distance is only defined for "
                        "sequences of equal length, so an attempt to "
                        "calculate it between sequences of different lengths "
                        "should not work.")
    
    dna_compared = zip(strand_a, strand_b)
    num_differences = 0
    for sequence in dna_compared:
        if sequence[0] != sequence[1]:
            num_differences += 1

    return num_differences
