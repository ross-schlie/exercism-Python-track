# Matrix

Given a string representing a matrix of numbers, return the rows and columns of
that matrix.

So given a string with embedded newlines like:

```text
9 8 7
5 3 2
6 6 7
```

representing this matrix:

```text
    1  2  3
  |---------
1 | 9  8  7
2 | 5  3  2
3 | 6  6  7
```

your code should be able to spit out:

- A list of the rows, reading each row left-to-right while moving
  top-to-bottom across the rows,
- A list of the columns, reading each column top-to-bottom while moving
  from left-to-right.

The rows for our example matrix:

- 9, 8, 7
- 5, 3, 2
- 6, 6, 7

And its columns:

- 9, 5, 6
- 8, 3, 6
- 7, 2, 7

In this exercise you're going to create a **class**.  _Don't worry, it's not as complicated as you think!_ 

-   [**A First Look at Classes**](https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes) from the Python 3 documentation. 
-   [**How to Define a Class in Python**](https://realpython.com/python3-object-oriented-programming/#how-to-define-a-class-in-python) from the Real Python website.  
-   [**Data Structures in Python**](https://docs.python.org/3/tutorial/datastructures.html) from the Python 3 documentation.

## Running the tests

To run the tests, run `pytest matrix_test.py`

Alternatively, you can tell Python to run the pytest module:
`python -m pytest matrix_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Source

https://exercism.io/tracks/python Matrix
Warmup to the `saddle-points` warmup. [http://jumpstartlab.com](http://jumpstartlab.com)
