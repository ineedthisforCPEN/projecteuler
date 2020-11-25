import argparse

from projecteuler import classes
from utils.resources import load_problem_resources


# Problem-specific constants
PROBLEM_NAME = "Problem 011 - Largest product in a grid"
PROBLEM_DESCRIPTION = """
The resource file for the problem contains a 20x20 grid. What four
adjascent numbers (vertically, horizontally, or diagonally) create the
largest product?
"""


class ProblemParser(argparse.ArgumentParser):
    def error(self, message):
        print(PROBLEM_NAME)
        self.print_help()
        print("\nError in argument list: " + message)
        self.exit()


class Problem011(classes.Problem):
    def __init__(self, args):
        self.parser = self.create_parser()
        self.args = self.parser.parse_args(args)
        self.resources = load_problem_resources(int("011"))

        self.problem_name = PROBLEM_NAME
        self.problem_desc = PROBLEM_DESCRIPTION
        self.problem_versions = self.get_implemented_versions(__file__)

    def create_parser(self):
        # THIS SECTION SHOULD BE MODIFIED
        # ADD ANY ARGUMENTS REQUIRED TO RUN THIS PROBLEM'S SOLUTION
        parser = ProblemParser(description=PROBLEM_DESCRIPTION)
        return parser
