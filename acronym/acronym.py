"""exercism acronym module."""

import re

def abbreviate(words):
    """
    Convert text to its acronym.

    :param words string - The text to create an acronym for.
    :return string - Acronym.
    """

    matches = re.findall(r"(\w)[\w']*", words.replace('_', ' '))
    return "".join(matches).upper()
