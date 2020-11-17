import argparse

from projecteuler import classes


# Problem-specific constants
PROBLEM_NAME = "Problem 001 - Multiples of 3 and 5"
PROBLEM_SUMMARY = """
If we list all the natural numbers below 10 that are multiples of...
"""
PROBLEM_DESCRIPTION = """
If we list all the natural numbers below 10 that are multiples of 3 or
5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum
of all the multiples of 3 or 5 below 1000.
"""


class ProblemParser(argparse.ArgumentParser):
    def error(self, message):
        print(PROBLEM_NAME)
        self.print_help()
        print("\nError in argument list: " + message)
        self.exit()


class Problem001(classes.Problem):
    def __init__(self, args):
        self.parser = self.create_parser()
        self.args = self.parser.parse_args(args)

        self.problem_name = PROBLEM_NAME
        self.problem_summary = PROBLEM_SUMMARY
        self.problem_desc = PROBLEM_DESCRIPTION
        self.problem_versions = self.get_implemented_versions(__file__)

    def create_parser(self):
        # THIS SECTION SHOULD BE MODIFIED
        # ADD ANY ARGUMENTS REQUIRED TO RUN THIS PROBLEM'S SOLUTION
        parser = ProblemParser(description=PROBLEM_DESCRIPTION)
        parser.add_argument("--number", "-n", type=int, required=True,
                            help="The upper limit to the number that " +
                                 "will be processed")
        return parser
