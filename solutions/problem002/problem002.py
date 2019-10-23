import argparse

from projecteuler import classes


# Problem-specific constants
PROBLEM_NAME = "Problem 002 - Even Fibonacci numbers"
PROBLEM_DESCRIPTION = \
"""Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will
be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... By considering the terms in
the Fibonacci sequence whose values do not exceed four million, find the
sum of the even-valued terms.
"""


class ProblemParser(argparse.ArgumentParser):
    def error(self, message):
        print(PROBLEM_NAME)
        self.print_help()
        print("\nError in argument list: " + message)
        self.exit()


class Problem002(classes.Problem):
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
        parser.add_argument("--number", "-n", type=int, required=True,
                            help="The upper limit to the number that " + \
                                 "will be processed")
        return parser