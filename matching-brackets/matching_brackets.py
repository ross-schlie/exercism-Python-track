"""exercism matching brackets module."""


def is_paired(input_string:str):
    """
    Determine that any and all pairs are matched and nested correctly.

    :param input_string str - The input to check
    :return bool - If they are matched and nested or not.
    """

    stack = []
    for char in input_string:
        if char in ['[', '{', '(']:
            stack.append(char)
        elif char in [']', '}', ')']:
            # Closing bracket with no open brackets.
            if len(stack) == 0:
                return False

            element = stack.pop()
            if element == '[' and char == ']':
                continue
            elif element == '{' and char == '}':
                continue
            elif element == '(' and char == ')':
                continue

            return False

    return len(stack) == 0
