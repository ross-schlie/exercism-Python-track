"""exercism flatten array module."""


def flatten(iterable):
    output = []
    for item in iterable:
        if type(item) is list:
            output = output + flatten(item)
        elif item is None:
            continue
        else:
            output.append(item)

    return output

