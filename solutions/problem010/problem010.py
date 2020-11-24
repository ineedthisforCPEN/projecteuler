import argparse

from projecteuler import classes
from utils.resources import load_problem_resources


# Problem-specific constants
PROBLEM_NAME = "Problem 010 - Summation of primes"
PROBLEM_DESCRIPTION = """
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of
all the primes below two million.
"""


class ProblemParser(argparse.ArgumentParser):
    def error(self, message):
        print(PROBLEM_NAME)
        self.print_help()
        print("\nError in argument list: " + message)
        self.exit()


class Problem010(classes.Problem):
    def __init__(self, args):
        self.parser = self.create_parser()
        self.args = self.parser.parse_args(args)
        self.resources = load_problem_resources(int("010"))

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
                            help="The upper limit of primes to sum.")
        return parser
