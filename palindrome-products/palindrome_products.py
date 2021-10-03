"""exercism palindrome products module."""

def is_palindrome(product):
    product_list = list(str(product))
    max = len(product_list)
    if max == 1:
        return True

    pivot =  max // 2
    for i in range(0, pivot):
        if product_list[i] != product_list[-i -1]:
            return False

    return True

def get_palindromes(min_factor, max_factor, findMax=False):
    palindromes = []
    products = {}
    factor_range_a = range(min_factor, max_factor + 1)

    if findMax:
        factor_range_a = reversed(factor_range_a)

    for a in factor_range_a:
        factor_range_b = range(min_factor, max_factor)
        if findMax:
            factor_range_b = reversed(factor_range_b)

        for b in factor_range_b:
            product = a * b
            if is_palindrome(product):
                factors = products.get(product)
                if factors is None:
                    factors = [(a, b)]
                else:
                    if factors.count((b, a)) == 0:
                        factors.append((a, b))

                products[product] = factors
                palindromes.append(product)

            if len(palindromes) > 10:
                break

        if len(palindromes) > 10:
            break

    return palindromes, products

def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("Max factor is smaller than Min factor.")

    palindromes, products = get_palindromes(min_factor, max_factor, True)
    palindromes.sort(reverse=True)
    if len(palindromes) > 0:
        return palindromes[0], products[palindromes[0]]

    return None, []


def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("Max factor is smaller than Min factor.")

    palindromes, products = get_palindromes(min_factor, max_factor)
    palindromes.sort()
    if len(palindromes) > 0:
        return palindromes[0], products[palindromes[0]]

    return None, []
