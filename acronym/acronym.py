'''
Introduction
Convert a phrase to its acronym.

Techies love their TLA (Three Letter Acronyms)!

Help generate some jargon by writing a program that converts a long name like Portable Network Graphics to its acronym (PNG).
'''
import re

def abbreviate(words):
    matches = re.findall(r"(\w)[\w']*", words.replace('_', ' '))
    return "".join(matches).upper()

# Test code
# print(abbreviate("He even left pie")) #HELP