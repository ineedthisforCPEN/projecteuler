import argparse

from projecteuler import classes


# Problem-specific constants
PROBLEM_NAME = "Problem 007 - 10001st prime"
PROBLEM_DESCRIPTION = """
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6th prime is 13. What is the 10 001st prime number?
"""


class ProblemParser(argparse.ArgumentParser):
    def error(self, message):
        print(PROBLEM_NAME)
        self.print_help()
        print("\nError in argument list: " + message)
        self.exit()


class Problem007(classes.Problem):
    def __init__(self, args):
        self.parser = self.create_parser()
        self.args = self.parser.parse_args(args)

        self.problem_name = PROBLEM_NAME
        self.problem_desc = PROBLEM_DESCRIPTION
        self.problem_versions = self.get_implemented_versions(__file__)

    def create_parser(self):
        # THIS SECTION SHOULD BE MODIFIED
        # ADD ANY ARGUMENTS REQUIRED TO RUN THIS PROBLEM'S SOLUTION
        parser = ProblemParser(description=PROBLEM_DESCRIPTION)
        parser.add_argument("--n", "-n", type=int, required=True,
                            help="The nth prime number to find.")
        return parser
