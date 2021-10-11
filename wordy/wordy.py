"""exercism wordy module."""


def answer(question:str):
    """
    Answer a mathematical word problem.

    :param question str - The question
    :return int - The answer

    >>> answer("What is 25 divided by 5?")
    5

    Handle a set of operations, in sequence.

    Since these are verbal word problems, evaluate the expression
     from left-to-right, ignoring the typical order of operations.

    >>> answer("What is 3 plus 2 multiplied by 3?")
    15

    raises ValueError when:
    - Unsupported operations ("What is 52 cubed?")
    - Non-math questions ("Who is the President of the United States")
    - Word problems with invalid syntax ("What is 1 plus plus 2?")
    """

    result = None
    operations = ["plus", "minus", "multiplied", "divided", "raised"]
    ignore = ["What", "is", "to", "the", "by"]
    operation = None
    parameters = question.replace("?", "").split(" ")
    for argument in parameters:
        numeric = is_numeric(argument)
        if numeric and operation is None and result is None:
            result = int(argument)
        elif numeric and operation is None:
            raise ValueError("Second number encountered butno operation specified.")
        elif numeric:
            # This means weare performing some operation
            if operation == "plus":
                result = result + int(argument)
            elif operation == "minus":
                result = result - int(argument)
            elif operation == "multiplied":
                result = result * int(argument)
            elif operation == "divided":
                result = result / int(argument)
            else: # raised
                result = result ** int(argument)

            # reset operation
            operation = None
        elif argument in operations:
            if result is None or operation is not None:
                raise ValueError("Invalid question.")

            operation = argument
        else:
            if argument not in ignore:
                raise ValueError("Invalid operation.")

    if result is None or operation is not None:
        raise ValueError("Invalid question.")

    return result

def is_numeric(number:str):
    """
    Check to see if a value is "numeric"

    :param number str - String to check for numericy
    :return bool - True if it can be cast to float, otherwise false
    """
    # argument.isnumeric()
    # number[0] == "-"
    try:
        float(number)
        return True
    except ValueError:
        # not numeric
        return False