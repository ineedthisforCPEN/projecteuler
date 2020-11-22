import argparse

from projecteuler import classes


# Problem-specific constants
PROBLEM_NAME = "Problem 006 - Sum square difference"
PROBLEM_DESCRIPTION = """
The sum of the squares of the first ten natural numbers is, $$1^2 + 2^2
+ ... + 10^2 = 385$$ The square of the sum of the first ten natural
numbers is, $$(1 + 2 + ... + 10)^2 = 55^2 = 3025$$ Hence the difference
between the sum of the squares of the first ten natural numbers and the
square of the sum is $3025 - 385 = 2640$. Find the difference between
the sum of the squares of the first one hundred natural numbers and the
square of the sum.
"""


class ProblemParser(argparse.ArgumentParser):
    def error(self, message):
        print(PROBLEM_NAME)
        self.print_help()
        print("\nError in argument list: " + message)
        self.exit()


class Problem006(classes.Problem):
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
        parser.add_argument("--number", "-n",
                            required=True,
                            type=int,
                            help="The upper range of numbers to test.")
        return parser
