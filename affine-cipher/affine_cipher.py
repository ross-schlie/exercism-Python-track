"""exercism affine cipher module."""

from math import gcd as bltin_gcd
import string

def encode(plain_text, a, b):
    """
    Encode text with the affine cipher.

    :param plain_text string - The text to encode.
    :param a int - key used in ciphering.
    :param b int - key used in ciphering.
    :return string - Encoded text.
    """

    alpha = string.ascii_lowercase
    m = len(alpha)

    if bltin_gcd(a, m) != 1:
        raise ValueError("Error: a and m must be coprime.")

    out = ''
    char_count = 0
    for index, char in enumerate(plain_text):
        if char_count == 5:
            out = out + ' '
            char_count = 0

        if char.isalpha():
            # E(x) = (ax + b) mod m
            # where x is the letter's index from 0 - length of alphabet - 1
            x = alpha.index(char.lower())
            cipheredchar = (a * x + b) % m
            out = out + alpha[cipheredchar]
            char_count += 1
        elif char.isnumeric():
            out = out + char
            char_count += 1

    return out.rstrip()


def decode(ciphered_text, a, b):
    """
    Decode text with the affine cipher.

    :param ciphered_text string - The text to decode.
    :param a int - key used in ciphering.
    :param b int - key used in ciphering.
    :return string - Decoded text.
    """

    alpha = string.ascii_lowercase
    m = len(alpha)

    if bltin_gcd(a, m) != 1:
        raise ValueError("Error: a and m must be coprime.")

    out = ''
    for index, char in enumerate(ciphered_text):
        if char.isspace():
            continue

        if char.isnumeric():
            out = out + char
        else:
            # D(y) = a^-1(y - b) mod m
            # where y is the numeric value of an encrypted letter
            y = alpha.index(char)
            a_mmi = mmi(a, m)
            decoded_char = a_mmi * (y - b) % m
            out = out + alpha[decoded_char]

    return out

def mmi(a, m):
    """
    Find the modular multiplicative inverse of a.

    :param a int - key used in ciphering.
    :param m int - the number of letters in the alphabet.
    :return int - The MMI
    """
    #an mod m = 1
    result = a
    n = 1
    while result != 1:
        n += 1
        result = a * n % m
        while result > m:
            result = result % m

    return n
