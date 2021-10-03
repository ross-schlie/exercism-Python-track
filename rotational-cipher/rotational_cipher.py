"""exercism rotational cipher module."""


def rotate(text, key):
    """
    Caesar cipher the provided text with the provided key.

    :param text string - Text to cipher.
    :param key string - The key to use in the cipher.
    :return text - ciphered text
    """
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for index, char in enumerate(text):
        if char.isalpha():
            cindex = alpha.index(char.lower()) + key
            if cindex >= 26:
                cindex = cindex % 26

            if char.islower():
                out = out + alpha[cindex]
            else:
                out = out + alpha[cindex].upper()
        else:
            out = out + char

    return out
