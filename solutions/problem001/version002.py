# Version-specific constants - EDIT THESE VALUES
VERSION_NAME = "Version002 - Brute Force, Smarter Iteration"
VERSION_DESCRIPTION = """
Brute force, iterate through all integers that are divisible by 3
or 5, skipping those that are not.
"""


def solution(args):
    """Problem 1 - Version 2
    Iterate through every integer that is divisible by 3 and 5,
    skipping those that are not, and sum those values.

    Parameters:
        args.number     The upper limit of the range of numbers over
                        which the sum will be taken

    Return:
        Sum of all numbers in range [1, args.number) that are divisible
        by 3 or 5.
    """
    retval = 0
    index = 0   # Used to traverse the increments list
    number = 3  # The first number that will be summed
    increments = [2, 1, 3, 1, 2, 3, 3]

    while number < args.number:
        retval += number
        number += increments[index]
        index = (index + 1) % len(increments)
    return retval


if __name__ == "__main__":
    errmsg = "Cannot run {} as a standalone script"
    raise RuntimeError(errmsg.format(VERSION_NAME))
