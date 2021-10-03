"""exercism isogram module."""

# Check if the text passed in is an isogram by
def is_isogram(string):
    """
    Check if the text passed in is an isogram.

    :param string string - Text to check
    :return bool - Isogram, or not.

    - Filter for alpha
        filter + list will convert the string to a list
    - Count occurences of each charater
        if theres more than 1 then it's not a isogram
    * string is lowercased while filtering to facilitate comparion (count)
    """
    text = list(filter(lambda c: c.isalpha(), string.lower()))
    for c in text:
        if text.count(c) > 1:
            return False

    return True
