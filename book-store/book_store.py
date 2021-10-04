"""exercism book store module."""



BASEPRICE = 800
DISCOUNTS = { 2: 0.05, 3: 0.10, 4: 0.20, 5: 0.25 }
"""The bookstores discounts for books.

2 unique books get 5% discount.
3 unique books get a 10% discount.
4 unique books get a 20% discount.
5 unique books get a 25% discount.
"""

def total(basket):
    """Calculate the cost of the 'books' in the basket after discount.

    :param basket list - Books that are being sold. May contain multiple copies of a book
    :return int - The price of the books after highest possible discount

    >>> total([])
    0

    >>> total(['A'])
    800
    # BASEPRICE = 800

    >>> total(['A', 'B', 'C', 'D', 'E'])
    3000
    # BASEPRICE = 800
    # * 5 = 4000
    # - 25% = 3000

    >>> total(['A', 'B', 'A'])
    2320
    # BASEPRICE = 800
    # * 3 = 2400
    # - 5% of 1600 = 2320

    """
    if not basket:
        return 0

    subtotal = BASEPRICE * len(basket)
    if len(basket) < 2:
        return subtotal

    basket.sort()
    possible_baskets = unique_book_combinations(basket)

    discounts = []
    for basket in possible_baskets:
        discount_applied = 0
        for group in basket:
            number_of_books = len(group)
            if number_of_books >= 2:
                discount_applied += BASEPRICE * number_of_books * DISCOUNTS.get(number_of_books)

        discounts.append(discount_applied)

    total = subtotal
    if len(discounts) > 0:
        discounts.sort()
        total -= discounts[-1]

    return total

def unique_book_combinations(books:list):
    """
    Find combinations of unique books in groups of 1-5

    :param books list - The books in the cart to sort into different groups.
    :return list - list of combinations of up to 5 books.
    """
    combinations = []

    for offset, book in enumerate(books):
        for num_books_in_other_groups in [5, 4, 3, 2]:
            for num_books_in_group in [5, 4, 3, 2]:
                basket = make_unique_group(books, offset, num_books_in_group, num_books_in_other_groups)
                if basket not in combinations:
                    combinations.append(basket)

    return combinations

def make_unique_group(books, offset, first_group_size, other_group_size):
    """
    Recursive method to create groups of unique books

    :param books list - The books to sort and group.
    :param offset int - Index of book to exclude from first group.
    :param first_group_size int - Max size of first group of books
    :param other_group_size int - Max size of other groups of books
    :return list - The 'shopping cart' of books as it were,
        seperating the books into groups in order to calculate the discount
    """
    if len(books) == len(set(books)) and len(books) <= first_group_size:
        return [books]

    basket = []
    group = []
    the_rest = []
    for index, book in enumerate(books):
        if index == offset:
            the_rest.append(book)
            continue

        if len(group) == first_group_size:
            the_rest = the_rest + books[index::]
            break

        if book in group:
            the_rest.append(book)
        else:
            group.append(book)

    basket.append(group)
    if len(the_rest) > other_group_size or len(the_rest) != len(set(the_rest)):
        rest_groups = make_unique_group(the_rest, offset, other_group_size, other_group_size)
        for remaining_book_group in rest_groups:
            basket.append(remaining_book_group)
    else:
        basket.append(the_rest)

    return basket
