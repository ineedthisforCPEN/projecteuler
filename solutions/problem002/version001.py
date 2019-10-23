# Version-specific constants - EDIT THESE VALUES
VERSION_NAME = "Version001 - Brute Force"
VERSION_DESCRIPTION = \
"""Calculate each Fibonacci number and sum only the even ones.
"""


def solution(args):
    """Problem 2 - Version 1
    Calculate each Fibonacci number and sum only the even ones.

    Parameters:
        args.number     The upper limit of the range of numbers over
                        which the sum will be taken

    Return:
        The sum of the even Fibonacci numbers that are less than
        args.number.
    """
    retval = 0
    fib1 = 0
    fib2 = 1

    while fib2 < args.number:
        if fib2 % 2 == 0:
            retval += fib2
        fib1, fib2 = fib2, fib1 + fib2
    return retval


if __name__ == "__main__":
    errmsg = "Cannot run {} as a standalone script"
    raise RuntimeError(errmsg.format(VERSION_NAME))