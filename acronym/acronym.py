import re

def abbreviate(words):
    """Use regex to match the first letter of a word to make acronyms."""
    matches = re.findall(r"(\w)[\w']*", words.replace('_', ' '))
    return "".join(matches).upper()