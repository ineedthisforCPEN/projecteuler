import argparse

from projecteuler import classes
from projecteuler.utils import factories
from utils.resources import load_problem_resources


# Problem-specific constants
PROBLEM_NAME = "Problem 004 - Largest palindrome product"
PROBLEM_DESCRIPTION = """
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 x 99. Find the
largest palindrome made from the product of two 3-digit numbers.
"""


class ProblemParser(argparse.ArgumentParser):
    def error(self, message):
        print(PROBLEM_NAME)
        self.print_help()
        print("\nError in argument list: " + message)
        self.exit()


class Problem004(classes.Problem):
    def __init__(self, args):
        self.parser = self.create_parser()
        self.args = self.parser.parse_args(args)
        self.resources = load_problem_resources(int("004"))

        self.problem_name = PROBLEM_NAME
        self.problem_desc = PROBLEM_DESCRIPTION
        self.problem_versions = self.get_implemented_versions(__file__)

    def create_parser(self):
        # THIS SECTION SHOULD BE MODIFIED
        # ADD ANY ARGUMENTS REQUIRED TO RUN THIS PROBLEM'S SOLUTION
        restricted_int = factories.restricted_integer_factory(lower=1)

        parser = ProblemParser(description=PROBLEM_DESCRIPTION)
        parser.add_argument("--digits", "-n",
                            type=restricted_int,
                            required=True,
                            help="The number of digits for the palindrome " +
                                 "factors")
        return parser
