import argparse

from projecteuler import classes
from utils.resources import load_problem_resources


# Problem-specific constants
PROBLEM_NAME = "Problem 005 - Smallest multiple"
PROBLEM_DESCRIPTION = """
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder. What is the smallest positive number
that is evenly divisible by all of the numbers from 1 to 20?
"""


class ProblemParser(argparse.ArgumentParser):
    def error(self, message):
        print(PROBLEM_NAME)
        self.print_help()
        print("\nError in argument list: " + message)
        self.exit()


class Problem005(classes.Problem):
    def __init__(self, args):
        self.parser = self.create_parser()
        self.args = self.parser.parse_args(args)
        self.resources = load_problem_resources(int("005"))

        self.problem_name = PROBLEM_NAME
        self.problem_desc = PROBLEM_DESCRIPTION
        self.problem_versions = self.get_implemented_versions(__file__)

    def create_parser(self):
        # THIS SECTION SHOULD BE MODIFIED
        # ADD ANY ARGUMENTS REQUIRED TO RUN THIS PROBLEM'S SOLUTION
        parser = ProblemParser(description=PROBLEM_DESCRIPTION)
        parser.add_argument("--number", "-n",
                            required=True,
                            type=int,
                            help="The upper range of numbers (1 - n) for " +
                                 "which to find the smallest number that " +
                                 "is divisible by all of these numbers.")
        return parser
