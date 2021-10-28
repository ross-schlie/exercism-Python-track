"""exercism isbn verifier module."""



def is_valid(isbn):
    """Check if the provided value is a valid ISBN."""
    if len(isbn) == 0:
        return False

    isbn = list(isbn.replace('-', ''))
    control = isbn.pop(len(isbn) - 1)
    if not control.isnumeric() and control != 'X':
        return False

    isbn = "".join(isbn)
    if not isbn.isnumeric() or len(isbn) != 9:
        return False

    """
    (
    x1 * 10 +
    x2 * 9 +
    x3 * 8 +
    x4 * 7 +
    x5 * 6 +
    x6 * 5 +
    x7 * 4 +
    x8 * 3 +
    x9 * 2 +
    x10 * 1
    )
    mod 11 == 0
    """

    isbn_sum = 0
    for i in range(0, 9):
        isbn_sum += int(isbn[i]) * (10 - i)

    if control == 'X':
        isbn_sum += 10
    else:
        isbn_sum += int(control)

    return isbn_sum % 11 == 0