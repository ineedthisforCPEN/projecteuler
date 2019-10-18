import argparse
import re


###############################################################################
# Utilities
###############################################################################
def convert_range_string(range_string):
    """Convert a range string into a list containing all values in the
    values represented by the range string.

    Parameters:
        range_string    The range string to convert into a list

    Return:
        A list of all the values contained in the range string.
    """
    re_valid_range_string = re.compile(r"^(\d+)(\.\.(\d+))?$")
    numeric_list = []

    range_list = range_string.split(",")
    for r in range_list:
        matches = re_valid_range_string.match(r)
        if matches is None:
            errmsg = "Malformed range string {} - must be of the form " + \
                     "x[..y] and can be comma separated"
            raise ValueError(errmsg.format(range_string))

        start, _, end = matches.groups()
        if end is None:
            end = start

        start = int(start)
        end = int(end) + 1

        numeric_list += list(range(start, end))

    return numeric_list


###############################################################################
# Argument Parsing and Main Function
###############################################################################
def argparse_setup():
    """Initialize argument parser."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", "-c", default=1, type=int,
                        help="The number of times to run the solution - " + \
                             "only applied when the --time flag is set")
    parser.add_argument("--problem", "-p", default=0, type=int,
                        help="Which Euler problem to run")
    parser.add_argument("--time", "-t", action="store_true",
                        help="Times the solution to measure its performance")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Prints more detailed information to stdout")
    parser.add_argument("--version", "-V", default="0", type=str,
                        help="Which versions of the solution to run " + \
                             "(e.g. '1', '1..3', '1..3,5..7')")
    args = parser.parse_args()
    return args


def argparse_format(args):
    """Format arguments so they can be processed more easily by the
    interface. The args parameter is modified in place.

    Parameters:
        args    The arguments to format

    Return:
        None. The args parameter is modified in place.
    """
    args.version = convert_range_string(args.version)
    return args


def main():
    args = argparse_setup()
    argparse_format(args)


if __name__ == "__main__":
    main()