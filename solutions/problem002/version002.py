# Version-specific constants - EDIT THESE VALUES
VERSION_NAME = "Version002 - Brute Force, but Skip Some"
VERSION_DESCRIPTION = """
Calculate each Fibonacci number and sum only the even ones. Skip the
even check to reduce branching.

We can skip the even check because we know every third Fibonacci number
is even, so we calculate three Fibonacci numbers and, if the third one
is less than our limit, add it to the sum.
"""


def solution(resources, args):
    """Problem 2 - Version 2
    Calculate each Fibonacci number and sum only the even ones. Skip
    the even check to reduce branching.

    Parameters:
        args.number     The upper limit of the range of numbers over
                        which the sum will be taken

    Return:
        The sum of the even Fibonacci numbers that are less than
        args.number.
    """
    retval = 0
    fib1 = 2
    fib2 = 3

    while fib1 < args.number:
        retval += fib1
        fib1, fib2 = fib2, fib1 + fib2
        fib1, fib2 = fib2, fib1 + fib2
        fib1, fib2 = fib2, fib1 + fib2
    return retval


if __name__ == "__main__":
    errmsg = "Cannot run {} as a standalone script"
    raise RuntimeError(errmsg.format(VERSION_NAME))
