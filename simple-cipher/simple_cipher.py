"""exercism simple cipher module."""

import string
import secrets

ALPHA = string.ascii_lowercase

class Cipher:
    def __init__(self, key=None):
        if key is not None:
            self.key = key.lower()
        else:
            self.key = ''.join(secrets.choice(ALPHA) for i in range(100))

    def encode(self, text):
        text = list(text)
        for index, char in enumerate(text):
            current = ALPHA.index(char)
            shift = ALPHA.index(self.key[index % len(self.key)])
            text[index] = ALPHA[(current + shift) % len(ALPHA)]

        return "".join(text)

    def decode(self, text):
        text = list(text)
        for index, char in enumerate(text):
            current = ALPHA.index(char)
            shift = ALPHA.index(self.key[index % len(self.key)])
            decoded = current - shift
            if decoded < 0:
                decoded += len(ALPHA)
            text[index] = ALPHA[decoded]

        return "".join(text)
