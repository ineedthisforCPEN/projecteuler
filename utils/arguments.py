"""arguments.py

Utilities used for processing command line arguments.
"""


import re


def extended_range_string_to_list(range_string):
    """Convert a range string into a list containing all values in the
    values represented by the range string.

    Parameters:
        range_string    The range string to convert into a list

    Return:
        A list of all the values contained in the range string.

    Examples:
        "1"         -> [1]
        "1..3"      -> [1,2,3]
        "1..3,5"    -> [1,2,3,5]
        "1..3,5..7" -> [1,2,3,5,6,7]
        "4..6,1..3" -> [1,2,3,4,5,6]
    """
    numeric_list = []
    for r in range_string.split(","):
        numeric_list += range_string_to_list(r)

    # Return a sorted list for easier processing
    return sorted(numeric_list)


def range_string_to_list(range_string):
    """Convert a range string into a list containing all values in the
    values represented by the range string.

    Parameters:
        range_string    The range string to convert into a list

    Return:
        A list of all the values contained in the range string.

    Examples:
        "1"         -> [1]
        "1..3"      -> [1,2,3]
    """
    re_valid_range_string = re.compile(r"^(\d+)(\.\.(\d+))?$")
    matches = re_valid_range_string.match(range_string.strip())

    if matches is None:
        errmsg = "Malformed range string {} - must be of the form " + \
                    "x[..y] and can be comma separated"
        raise ValueError(errmsg.format(range_string))

    start, _, end = matches.groups()
    if end is None:
        end = start

    # The ending value of the range_string's range is inclusive unlike
    # Python's range. Add 1 to end to adjust for this.
    return list(range(int(start), int(end) + 1))