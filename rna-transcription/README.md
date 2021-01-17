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


## Running the tests

To run the tests, run `pytest rna_transcription_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest rna_transcription_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Source

https://exercism.io/tracks/python RNA Transcription
Hyperphysics [http://hyperphysics.phy-astr.gsu.edu/hbase/Organic/transcription.html](http://hyperphysics.phy-astr.gsu.edu/hbase/Organic/transcription.html)
