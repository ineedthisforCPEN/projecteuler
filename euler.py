import argparse
import importlib
import re
import os
import os.path


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


def get_import_paths(problem, versions):
    """Return a list of import paths for each solution of the specified
    problem. This list can be used to import (and run) each version of
    the solution.

    Parameters:
        problem     The problem whose solutions' import paths will be
                    returned

        versions    The version of the solutions whose import paths to
                    return'

    Return:
        A list containint the import paths of each implemented solution
        to the specified problem.
    """
    # Verify that the requested problem has been implemented
    problem_name = "problem{:03}".format(problem)
    problem_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                "solutions",
                                problem_name)
    if not os.path.exists(problem_dir):
        errmsg = "Solution to problem {:03} not implemented"
        raise NotImplementedError(errmsg.format(problem))

    # Get all available solution versions for the given problem
    version_files = next(os.walk(problem_dir))[-1]
    version_files = [os.path.splitext(f)[0] for f in version_files]
    if len(version_files) == 0:
        # No versions of the solution are implemented. The solution to this
        # problem is not implemented.
        errmsg = "Solution to problem {:03} not implemented"
        raise NotImplementedError(errmsg.format(problem))

    # Filter out any requested versions that have not been implemented, and
    # convert all implemented versions into the equivalent import path for
    # each version (i.e. solutions.problemXXX.verisionYYY)
    implemented_versions = []
    for version in versions:
        version_string = "version{:03}".format(version)
        if version_string in version_files:
            import_path = "solutions.{}.{}".format(problem_name,
                                                   version_string)
            implemented_versions.append(import_path)
        else:
            warnstr = "Problem {:03} Version {:03} not implemented - skipping"
            print(warnstr.format(problem, version))

    return implemented_versions


def run_solution(import_path):
    """Runs the solution implemented in the file specified by the
    import path.

    Parameters:
        import_path     The import path to the file that implements a
                        solution to a particular problem

    Return:
        The return value of the executed solution
    """
    imported = importlib.import_module(import_path)
    solution = getattr(imported, "solution")
    return solution()


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
    def run(problem, versions):
        try:
            return get_import_paths(problem, versions)
        except Exception as e:
            print(e)
            return None

    args = argparse_setup()
    argparse_format(args)

    import_paths = get_import_paths(args.problem, args.version)
    for import_path in import_paths:
        run_solution(import_path)


if __name__ == "__main__":
    main()