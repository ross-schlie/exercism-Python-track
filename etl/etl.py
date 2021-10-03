"""exercism etl module."""


def transform(legacy_data):
    """
    Transform legacy data.
    """
    data = {}
    while len(legacy_data) > 0:
        item = legacy_data.popitem()
        for char in item[1]:
            data[char.lower()] = item[0]

    return data
