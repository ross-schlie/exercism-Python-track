"""exercism protein translation module."""


def proteins(strand):
    """
    Translate RNA sequences into proteins.

    :param strand string - The RNA to translate.
    :return list - The protein the RNA translated into.
    """

    # Some unit tests seem to be funky because of the order ...
    # proteins = set()
    proteins = []
    stop_codons = ["UAA", "UAG", "UGA"]
    protein_map = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan"
    }

    for index in range(0, len(strand), 3):
        codon = strand[index:index + 3]
        if codon in stop_codons:
            break

        # proteins.add(protein_map.get(codon))
        protein = protein_map.get(codon)
        if proteins.count(protein) == 0:
            proteins.append(protein)

    # proteins = list(proteins)
    # proteins.sort()
    return proteins

