def is_isogram(string):
    """Check the text passed in and decide if it is an isogram.
    
    First performs filtering for alphabestical characters.
    The string is lowercased while filtering to prevent issues of case 
    when comparing.
    Convert the string to a list.
    Finally compare the length of the filtered list to 
    a set created from said list.

    """
    text = list(filter(lambda c: c.isalpha(), string.lower()))
    return len(text) == len(set(text))
