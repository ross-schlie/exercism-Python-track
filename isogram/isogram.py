'''
Introduction
Determine if a word or phrase is an isogram.

An isogram (also known as a "nonpattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.

Examples of isograms:

lumberjacks
background
downstream
six-year-old
The word isograms, however, is not an isogram, because the s repeats.
'''

# Check if the text passed in is an isogram by first filtering for alpha
# filter + list will convert the string to a list 
# finally compare the length of the filtered list to a set created from said list
# * string is lowercased while filtering to prevent issues of case when comparing
def is_isogram(string):
    text = list(filter(lambda c: c.isalpha(), string.lower()))
    return len(text) == len(set(text))

# Testing code
# print(is_isogram('lumberjacks'))
# print(is_isogram('isograms'))
# print(is_isogram('six-year-old'))
# print(is_isogram('six year old'))