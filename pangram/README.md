# Pangram

Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan gramma,
"every letter") is a sentence using every letter of the alphabet at least once.
The best known English pangram is:
> The quick brown fox jumps over the lazy dog.

The alphabet used consists of ASCII letters `a` to `z`, inclusive, and is case
insensitive. Input will not contain non-ASCII symbols.

## Running the tests

To run the tests, run `pytest pangram_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest pangram_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Source

https://exercism.io/tracks/python Pangram
Wikipedia [https://en.wikipedia.org/wiki/Pangram](https://en.wikipedia.org/wiki/Pangram)
