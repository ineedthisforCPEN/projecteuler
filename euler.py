import argparse
import bisect
import importlib
import os
import os.path
import statistics
import sys
import time

import constants as const
import utils.arguments as utils_args


PROJECT_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), ".."))


###############################################################################
# Utilities
###############################################################################
def format_timing(timing):
    """Format a timing to  have the format 'X XXX XXX XXX.YYYYYY'.

    Parameters:
        timing  The timing (in seconds) to format

    Return:
        The formatted timing.
    """
    rounded = round(timing, 6)
    formatted = "{:,.6F}".format(rounded)
    formatted = formatted.replace(",", " ")
    return "{:>20}".format(formatted)


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

    import_path = "solutions.{p}.{p}".format(p=problem_name)
    try:
        imported = importlib.import_module(import_path)
    except ModuleNotFoundError:
        errmsg = "Problem {} not implemented"
        errmsg = errmsg.format(const.PROBLEM_NUMBER.format(problem))
        raise NotImplementedError(errmsg)
    return getattr(imported, problem_class)


def get_problem_name(problem):
    """Read the problem file and return its name.

    This function does NOT handle exceptions - the problem must be
    implemented when you call this function.

    Parameters:
        problem     The problem whose name to return

    Return:
        The name of the specified problem.
    """
    import_path = "solutions.{p}.{p}".format(p=problem)
    imported = importlib.import_module(import_path)
    return getattr(imported, "PROBLEM_NAME")


def get_version_name(problem, version):
    """Read the version file and return its name.

    This function does NOT handle exceptions - the version and problem
    must be implemented when you call this function.

    Parameters:
        problem     The problem associated with the version
        version     The version whose name to return

    Return:
        The name of the specified version.
    """
    import_path = "solutions.{p}.{v}".format(p=problem, v=version)
    imported = importlib.import_module(import_path)
    return getattr(imported, "VERSION_NAME")


###############################################################################
# Argument Parsing
###############################################################################
def argparse_setup():
    """Initialize the argument parser.

    Parameters:
        None

    Return:
        None
    """
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # Subparser for implementation listing
    info_parser = subparsers.add_parser("info",
                                        help="List implementation details")
    info_parser.add_argument("--problems", "-p", type=str,
                             help="Problems to list")
    info_parser.add_argument("--verbose", "-v", action="store_true",
                             help="Show details for all implementations")
    info_parser.set_defaults(which="info")

    # Subparser for problem execution
    run_parser = subparsers.add_parser("run",
                                       help="Execute given implementations")
    run_parser.add_argument("--problem", "-p", type=int, required=True,
                            help="Which Euler problem to run")
    run_parser.add_argument("--versions", "-v", type=str,
                            help="Which implementation(s) to run " +
                                 "(e.g. '1', '1..3', '1..3,5..7'")
    run_parser.set_defaults(which="run")

    # Subparser for testing
    test_parser = subparsers.add_parser("perf",
                                        help="Check problem implementation " +
                                             "performance")
    test_parser.add_argument("--count", "-c", type=int, default=3,
                             help="Number of times to run the solution")
    test_parser.add_argument("--problem", "-p", type=int, required=True,
                             help="Which Euler problem to run")
    test_parser.add_argument("--versions", "-v", type=str,
                             help="Which impementation(s) to run " +
                                  "(e.g. '1', '1..3', '1..3,5..7'")
    test_parser.set_defaults(which="perf")

    args, unknown = parser.parse_known_args()
    if (len(vars(args))) == 0:
        # No arguments passed. Print help string and exit.
        parser.print_help()
        sys.exit(1)

    return (args, unknown)


def argparse_format(args):
    """Format arguments so they can be processed more easily by the
    interface. The args parameter is modified in place.

    Parameters:
        args    The arguments to format

    Return:
        None. The args parameter is modified in place.
    """
    argvars = vars(args)

    if "count" in argvars:
        args.count = max(1, args.count)
    if "problems" in argvars and argvars["problems"] is not None:
        args.problems = utils_args.extended_range_string_to_list(args.problems)
    if "versions" in argvars and argvars["versions"] is not None:
        args.versions = utils_args.extended_range_string_to_list(args.versions)

    return args


###############################################################################
# Main Function and Workload Delegation
###############################################################################
def workload_info(args, problem_args):
    print("\n[Project Euler Solution Implementations]\n")
    solutions_dir = os.path.join(PROJECT_DIR, "solutions")
    implemented = next(os.walk(solutions_dir))[1]
    missing_problems = False

    if args.problems is not None:
        problems = [const.PROBLEM_NAME.format(p) for p in args.problems]
    else:
        problems = implemented

    for problem in problems:
        if problem not in implemented:
            print(f"Problem {problem[-const.PROBLEM_DIGITS:]}" +
                  " - NOT IMPLEMENTED")
            continue

        problem_dir = os.path.join(solutions_dir, problem)
        problem_file = problem + ".py"
        files = next(os.walk(problem_dir))[-1]

        # Print problem information.
        if problem_file in files:
            print(get_problem_name(problem)[:65])
        else:
            print(f"Problem {problem[-const.PROBLEM_DIGITS:]}" +
                  " - NO PROBLEM FILE FOUND")
            missing_problems = True

        # If verbose, print version implementations.
        if args.verbose:
            for version in files:
                if const.RE_VERSION_FILE.match(version) is not None:
                    version_name = os.path.splitext(version)[0]
                    infostr = f"    {get_version_name(problem, version_name)}"
                    print(infostr[:65])

    if missing_problems:
        print("\nWARNING: Some problems are not implemented properly. " +
              "Please re-run the generate_problem tool again.")
    print("\n")


def workload_perf(args, problem_args):
    problem = get_problem_class(args.problem)(problem_args)
    print(get_problem_name(const.PROBLEM_NAME.format(args.problem)))

    if args.versions is not None:
        versions = [const.VERSION_NAME.format(v) for v in args.versions]
    else:
        versions = list(problem.problem_versions.keys())

    for version in versions:
        if not problem.is_version_implemented(version):
            print(f"  {version} - not implemented")
            continue

        problem_name = const.PROBLEM_NAME.format(args.problem)
        print(f"  {get_version_name(problem_name, version)}")
        # print(f"  {version} - running {args.count} iterations")

        timings = []
        for iteration in range(args.count):
            start_time = time.time()
            problem.run_solution(version)
            bisect.insort(timings, time.time() - start_time)

        minimum = timings[0]
        average = statistics.mean(timings)
        maximum = timings[-1]
        median = statistics.median(timings)
        stdev = statistics.stdev(timings)

        print(f"    total runtime   {format_timing(sum(timings))}  seconds")
        print(f"    min.  runtime   {format_timing(minimum)}  seconds")
        print(f"    avg.  runtime   {format_timing(average)}  seconds")
        print(f"    max.  runtime   {format_timing(maximum)}  seconds")
        print(f"    med.  runtime   {format_timing(median)}  seconds")
        print(f"    standard deviation                      {stdev:.3f}")


def workload_run(args, problem_args):
    problem = get_problem_class(args.problem)(problem_args)
    print(get_problem_name(const.PROBLEM_NAME.format(args.problem)))

    if args.versions is not None:
        versions = [const.VERSION_NAME.format(v) for v in args.versions]
    else:
        versions = list(problem.problem_versions.keys())

    for version in versions:
        if not problem.is_version_implemented(version):
            print(f"  {version} - not implemented")
            continue

        retval = problem.run_solution(version)
        print(f"  {version} - returned '{retval}'")


def main():
    # Get and format command line arguments
    args, problem_args = argparse_setup()
    argparse_format(args)

    # Determine what action to take depending on which subparser was chosen.
    # Each subparser has different command line arguments, so it must be
    # handled separately.
    if args.which == "info":
        workload_info(args, problem_args)
    elif args.which == "run":
        workload_run(args, problem_args)
    elif args.which == "perf":
        workload_perf(args, problem_args)
    return


if __name__ == "__main__":
    # Add projecteuler to system path so that utilities and constants can be
    # imported from any file.
    root_dir = os.path.join(PROJECT_DIR, "..")
    if root_dir not in sys.path:
        sys.path.append(root_dir)

    main()
