"""exercism rna-transcription module."""


def to_rna(dna_strand):
    """Convert a strand of DNA to RNA

    Parameters
    ----------
    arg1 : string
        DNA strand (string of nucleotides)

    Returns
    ------
    string
        RNA strand (string of nucleotides)

    >>> to_rna("T")
    "A"

    >>> to_rna("ACGTGGTCTTAA")
    "UGCACCAGAAUU"
    """

    nucleotides = ['G', 'C', 'T', 'A']
    nucleotide_complements = ['C', 'G', 'A', 'U']
    replacedstrand = []
    for nucleotide in list(dna_strand):
        if nucleotide in nucleotides:
            replacedstrand.append(
                nucleotide_complements[nucleotides.index(nucleotide)])
        else:
            replacedstrand.append(nucleotide)

    return "".join(replacedstrand)
