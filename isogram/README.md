# Isogram

Determine if a word or phrase is an isogram.

An isogram (also known as a "nonpattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.

Examples of isograms:

- lumberjacks
- background
- downstream
- six-year-old

The word *isograms*, however, is not an isogram, because the s repeats.

## Running the tests

To run the tests, run `pytest isogram_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest isogram_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Source

https://exercism.io/tracks/python Isogram
Wikipedia [https://en.wikipedia.org/wiki/Isogram](https://en.wikipedia.org/wiki/Isogram)
