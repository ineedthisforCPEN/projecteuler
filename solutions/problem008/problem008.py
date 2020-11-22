import argparse

from projecteuler import classes
from utils.resources import load_problem_resources


# Problem-specific constants
PROBLEM_NAME = "Problem 008 - Largest product in a series"
PROBLEM_DESCRIPTION = """
The resource file for this problem contains a 1000-digit number. In this
1000-digit number, there are four adjacent digits that have the greatest
product; they are 9 x 9 x 8 x 9 = 5832. Find the thirteen adjacent
digits in the 1000-digit number that have the greatest product. What is
the value of this product?
"""


class ProblemParser(argparse.ArgumentParser):
    def error(self, message):
        print(PROBLEM_NAME)
        self.print_help()
        print("\nError in argument list: " + message)
        self.exit()


class Problem008(classes.Problem):
    def __init__(self, args):
        self.parser = self.create_parser()
        self.args = self.parser.parse_args(args)
        self.resources = load_problem_resources(int("008"))

        self.problem_name = PROBLEM_NAME
        self.problem_desc = PROBLEM_DESCRIPTION
        self.problem_versions = self.get_implemented_versions(__file__)

    def create_parser(self):
        # THIS SECTION SHOULD BE MODIFIED
        # ADD ANY ARGUMENTS REQUIRED TO RUN THIS PROBLEM'S SOLUTION
        parser = ProblemParser(description=PROBLEM_DESCRIPTION)
        parser.add_argument("--digits", "-n", type=int, required=True,
                            help="The number of digits whose max product " +
                                 "to find.")
        return parser
