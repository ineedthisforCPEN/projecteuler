import argparse
import importlib
import re
import os
import os.path
import sys

import constants as const


PROJECT_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), ".."))


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


def list_implementations(args):
    """List all problem implementations or the implementations of a
    given problem's solution versions.

    Parameters:
        args    The command line arguments list

    Return:
        None.
    """
    if args.problem is None:
        implementations = list_problem_implementations()
        infostr = "Implemented problems:"
        warnstr = "No problem implementations found"
    else:
        implementations = list_version_implementations(args.problem)
        infostr = "Implemented versions of problem {} solution"
        infostr = infostr.format(args.problem)
        warnstr = "No version implementations found for problem {}"
        warnstr = warnstr.format(args.problem)

    if len(implementations) == 0:
        print(warnstr + "\n")
    else:
        print(infostr)
        for implementation in implementations:
            print("\t{}".format(implementation))
        print("\n")


def list_problem_implementations():
    """List all implemented problems.

    Parameters:
        None

    Return:
        Returns a string list of all implemented problems.
    """
    implementations = []
    solutions_dir = os.path.join(PROJECT_DIR, "solutions")
    problems = next(os.walk(solutions_dir))[1]
    problems = [p for p in problems if const.RE_PROBLEM.match(p) is not None]

    for problem in problems:
        problem_dir = os.path.join(solutions_dir, problem)
        problem_file = problem + ".py"

        files = next(os.walk(problem_dir))[-1]
        if problem_file in files:
            implementations.append(problem)
        else:
            warnstr = "WARNING: {p} does not contain {f} - the problem " + \
                      "is not properly implemented. Please re-run the " + \
                      "generate_problem tool again."
            print(warnstr.format(p=problem, f=problem_file))

    return implementations


def list_version_implementations(problem):
    """List all implemented versions of the given problem's solution.

    Parameters:
        problem     The problem whose solution versions to list

    Return:
        Returns a string list of all implemented solution versions.
    """
    implementations = []
    problem_dir = os.path.join(PROJECT_DIR,
                               "solutions",
                               const.PROBLEM_NAME.format(problem))

    if not os.path.exists(problem_dir):
        return implementations

    versions = next(os.walk(problem_dir))[-1]
    for version in versions:
        if const.RE_VERSION_FILE.match(version) is not None:
            implementations.append(version)

    return implementations


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

    # Required arguments
    parser.add_argument("--problem", "-p", type=int,
                        help="Which Euler problem to run")
    parser.add_argument("--versions", "-v", type=str,
                        help="Which versions of the solution to run " + \
                             "(e.g. '1', '1..3', '1..3,5..7')")

    # Options
    parser.add_argument("--count", default=1, type=int,
                        help="The number of times to run the solution - " + \
                             "only applied when the --time flag is set")
    parser.add_argument("--list", action="store_true",
                        help="List all problem or version implementations")
    parser.add_argument("--time", action="store_true",
                        help="Times the solution to measure its performance")

    args, unknown = parser.parse_known_args()

    # Process any arguments as required
    if not args.time:
        # Count argument only applicable when timing each solution's run
        args.count = 1

    return (args, unknown)


def argparse_format(args):
    """Format arguments so they can be processed more easily by the
    interface. The args parameter is modified in place.

    Parameters:
        args    The arguments to format

    Return:
        None. The args parameter is modified in place.
    """
    if args.versions is not None:
        args.versions = convert_range_string_to_list(args.versions)
    return args


def main():
    # Get and format command line arguments
    args, problem_args = argparse_setup()
    argparse_format(args)

    # Handle any special options that have priority
    if args.list:
        list_implementations(args)
        return

    # If any of the above options were not specified, then the "problem"
    # argument is mandatory. Perform the check here.
    if args.problem is None:
        raise TypeError("Missing required argument: 'problem'")

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
    root_dir = os.path.join(PROJECT_DIR, "..")
    if root_dir not in sys.path:
        sys.path.append(root_dir)

    main()