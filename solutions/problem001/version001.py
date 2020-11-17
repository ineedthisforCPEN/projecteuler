# Version-specific constants - EDIT THESE VALUES
VERSION_NAME = "Version001 - Brute Force, Iterative"
VERSION_DESCRIPTION = """
Brute force, iterate through all integers
"""


def solution(args):
    """Problem 1 - Version 1
    Iterate through every intger from 1 through n to calculate the sum
    of numbers divisible by 3 and 5.

    Parameters:
        args.number     The upper limit of the range of numbers over
                        which the sum will be taken

    Return:
        Sum of all numbers in range [1, args.number) that are divisible
        by 3 or 5.
    """
    retval = 0
    for n in range(1, args.number):
        if n % 3 == 0 or n % 5 == 0:
            retval += n
    return retval


if __name__ == "__main__":
    errmsg = "Cannot run {} as a standalone script"
    raise RuntimeError(errmsg.format(VERSION_NAME))
