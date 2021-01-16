'''
# RNA Transcription

Given a DNA strand, return its RNA complement (per RNA transcription).

Both DNA and RNA strands are a sequence of nucleotides.

The four nucleotides found in DNA are adenine (**A**), cytosine (**C**),
guanine (**G**) and thymine (**T**).

The four nucleotides found in RNA are adenine (**A**), cytosine (**C**),
guanine (**G**) and uracil (**U**).

Given a DNA strand, its transcribed RNA strand is formed by replacing
each nucleotide with its complement:

* `G` -> `C`
* `C` -> `G`
* `T` -> `A`
* `A` -> `U`
'''

def to_rna(dna_strand):
    nucleotides = ['G', 'C', 'T', 'A']
    nucleotidecomplements = ['C', 'G', 'A', 'U']
    replacedstrand = []
    for nucleotide in list(dna_strand):
        if nucleotide in nucleotides:
            replacedstrand.append(nucleotidecomplements[nucleotides.index(nucleotide)])
        else:
            replacedstrand.append(nucleotide)

    return "".join(replacedstrand)

# print(to_rna("ACGTGGTCTTAA")) #"UGCACCAGAAUU"