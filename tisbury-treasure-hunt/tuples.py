"""exercism tisbury treasure hunt (tuples) module."""


def get_coordinate(record):
    """
    Retrieve coordinates from record.

    :param record: tuple - a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return record[1]


def convert_coordinate(coordinate):
    """
    Parse coordinate.

    :param coordinate: str - a string map coordinate
    :return:  tuple - the string coordinate seperated into its individual components.
    """

    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """
    Compare records to see if coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: bool - True if coordinates match, False otherwise.
    """

    azura_tuple = tuple(azara_record[1])
    return azura_tuple == rui_record[1]


def create_record(azara_record, rui_record):
    """
    Build a combined record for matching coordinates.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return:  tuple - combined record, or "not a match" if the records are incompatible.
    """

    azura_tuple = tuple(azara_record[1])
    if azura_tuple == rui_record[1]:
        return azara_record + rui_record

    return "not a match"


def clean_up(combined_record_group):
    """
    Create a clean report of a record group.

    :param combined_record_group: tuple of tuples - everything from both participants.
    :return: string of tuples separated by newlines - everything "cleaned". Excess coordinates and information removed.
    """

    record = ''
    for record_group in combined_record_group:
        record_group_copy = tuple([record_group[0], record_group[2], record_group[3], record_group[4]])
        record += str(record_group_copy) + '\n'

    return record
