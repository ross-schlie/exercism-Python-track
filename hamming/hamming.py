'''
Introduction
Calculate the Hamming Distance between two DNA strands.

Your body is made up of cells that contain DNA. Those cells regularly wear out and need replacing, which they achieve by dividing into daughter cells. 
In fact, the average human body experiences about 10 quadrillion cell divisions in a lifetime!

When cells divide, their DNA replicates too. Sometimes during this process mistakes happen and single pieces of DNA get encoded with the incorrect information. 
If we compare two strands of DNA and count the differences between them we can see how many mistakes occurred. This is known as the "Hamming Distance".

We read DNA using the letters C,A,G and T. Two strands might look like this:

GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
^ ^ ^  ^ ^    ^^
They have 7 differences, and therefore the Hamming Distance is 7.

The Hamming Distance is useful for lots of things in science, not just biology, so it's a nice phrase to be familiar with :)

Implementation notes
The Hamming distance is only defined for sequences of equal length, so an attempt to calculate it between sequences of different lengths should not work. 
The general handling of this situation (e.g., raising an exception vs returning a special value) may differ between languages.
'''

# Compare two strings and count the differences
# - Raises a ValueError when lengths differ
def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("The Hamming distance is only defined for sequences of equal length, "
            " so an attempt to calculate it between sequences of different lengths should not work.")
    
    dna_compared = zip(strand_a, strand_b)
    num_differences = 0
    for sequence in dna_compared:
        if sequence[0] != sequence[1]:
            num_differences += 1

    return num_differences

# Testing code
# strand_a = 'GAGCCTACTAACGGGAT'
# strand_b = 'CATCGTAATGACGGCCT'
# num_differences = distance(strand_a, strand_b)
# print(num_differences)