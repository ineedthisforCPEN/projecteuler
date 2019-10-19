import argparse
import importlib
import re
import os
import os.path
import sys

import constants as const


###############################################################################
# Utilities
###############################################################################
def convert_range_string_to_list(range_string):
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
    re_valid_range_string = re.compile(r"^(\d+)(\.\.(\d+))?$")
    numeric_list = []

    range_list = range_string.split(",")
    for r in range_list:
        matches = re_valid_range_string.match(r.strip())
        if matches is None:
            errmsg = "Malformed range string {} - must be of the form " + \
                     "x[..y] and can be comma separated"
            raise ValueError(errmsg.format(range_string))

        start, _, end = matches.groups()
        if end is None:
            end = start

        # The ending value of the range_string's range is inclusive unlike
        # Python's range. Add 1 to end to adjust for this.
        start = int(start)
        end = int(end) + 1

        numeric_list += list(range(start, end))

    # Return a sorted list for easier processing
    return sorted(numeric_list)


def get_problem_class(problem):
    """Import and return the specified problem and its implemented
    solutions.

    Parameters:
        problem     The problem to import

    Return:
        The Problem class that provides problem details and implemented
        solutions.
    """
    problem_name = const.PROBLEM_NAME.format(problem)
    problem_class = problem_name[0].upper() + problem_name[1:]

    import_path = "solutions.{}.{}".format(problem_name, problem_name)
    try:
        imported = importlib.import_module(import_path)
    except ModuleNotFoundError:
        errmsg = "Problem {} not implemented"
        errmsg = errmsg.format(const.PROBLEM_NUMBER.format(problem))
        raise NotImplementedError(errmsg)
    return getattr(imported, problem_class)


###############################################################################
# Argument Parsing and Main Function
###############################################################################
def argparse_setup():
    """Initialize the argument parser.

    Parameters:
        None

    Return:
        None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", "-c", default=1, type=int,
                        help="The number of times to run the solution - " + \
                             "only applied when the --time flag is set")
    parser.add_argument("--problem", "-p", default=0, type=int,
                        help="Which Euler problem to run")
    parser.add_argument("--time", "-t", action="store_true",
                        help="Times the solution to measure its performance")
    parser.add_argument("--versions", "-v", default="0", type=str,
                        help="Which versions of the solution to run " + \
                             "(e.g. '1', '1..3', '1..3,5..7')")
    args, unknown = parser.parse_known_args()
    return (args, unknown)


def argparse_format(args):
    """Format arguments so they can be processed more easily by the
    interface. The args parameter is modified in place.

    Parameters:
        args    The arguments to format

    Return:
        None. The args parameter is modified in place.
    """
    args.versions = convert_range_string_to_list(args.versions)
    return args


def main():
    # Get and format command line arguments
    args, problem_args = argparse_setup()
    argparse_format(args)

    # Find the appropriate problem (if it exists) and pass the unhandled
    # command line arguments into the problme class
    problem = get_problem_class(args.problem)(problem_args)
    for version in args.versions:
        if not problem.is_version_implemented(version):
            # Specified version is not implemented. Let the user know, then
            # ignore this version and continue trying to run the remaining
            # versions.
            warnstr = "Problem {p} Version {v} not implemented - skipping"
            warnstr = warnstr.format(p=const.PROBLEM_NUMBER.format(args.problem),
                                     v=const.VERSION_NUMBER.format(version))
            print(warnstr)
            continue

        # This version of the solution exists. Run it and show the results.
        retval = problem.run_solution(version)
        infostr = "Problem {p} Version {v} - returned {r}"
        infostr = infostr.format(p=const.PROBLEM_NUMBER.format(args.problem),
                                 v=const.VERSION_NUMBER.format(version),
                                 r=retval)
        print(infostr)


if __name__ == "__main__":
    # Add projecteuler to system path so that utilities and constants can be
    # imported from any file.
    current_dir = os.path.dirname(os.path.realpath(__file__))
    root_dir = os.path.abspath(os.path.join(current_dir, ".."))
    if root_dir not in sys.path:
        sys.path.append(root_dir)

    main()