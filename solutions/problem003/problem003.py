import argparse

from projecteuler import classes
from utils.resources import load_problem_resources


# Problem-specific constants
PROBLEM_NAME = "Problem 003 - Largest prime factor"
PROBLEM_DESCRIPTION = """
The prime factors of 13195 are 5, 7, 13 and 29. What is the largest
prime factor of the number 600851475143 ?
"""


class ProblemParser(argparse.ArgumentParser):
    def error(self, message):
        print(PROBLEM_NAME)
        self.print_help()
        print("\nError in argument list: " + message)
        self.exit()


class Problem003(classes.Problem):
    def __init__(self, args):
        self.parser = self.create_parser()
        self.args = self.parser.parse_args(args)
        self.resources = load_problem_resources(int("003"))

        self.problem_name = PROBLEM_NAME
        self.problem_desc = PROBLEM_DESCRIPTION
        self.problem_versions = self.get_implemented_versions(__file__)

    def create_parser(self):
        # THIS SECTION SHOULD BE MODIFIED
        # ADD ANY ARGUMENTS REQUIRED TO RUN THIS PROBLEM'S SOLUTION
        parser = ProblemParser(description=PROBLEM_DESCRIPTION)
        parser.add_argument("--number", "-n", type=int, required=True,
                            help="The number whose largest prime factor to " +
                                 "find")
        return parser
