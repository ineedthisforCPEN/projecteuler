# Version-specific constants - EDIT THESE VALUES
VERSION_NAME = "Version003 - Brute Force, Even Smarter Iteration"
VERSION_DESCRIPTION = """
A slightly more formulaic approach, but still iterative.
"""


def solution(resources, args):
    """Problem 1 - Version 3
    Use a formula to determine the additional sum 15 integers at a
    time, then use the iterative approach for any remaining integers
    in the range.

    Parameters:
        args.number     The upper limit of the range of numbers over
                        which the sum will be taken

    Return:
        Sum of all numbers in range [1, args.number) that are divisible
        by 3 or 5.
    """
    retval = 0
    repeats = [3, 5, 6, 9, 10, 12, 15]

    i = 0
    n = args.number - 1

    while n > 15:
        retval += sum(repeats)
        retval += 15*len(repeats)*i
        n -= 15
        i += 1
    while n >= 3:
        if n % 3 == 0 or n % 5 == 0:
            retval += 15*i + n
        n -= 1
    return retval


if __name__ == "__main__":
    errmsg = "Cannot run {} as a standalone script"
    raise RuntimeError(errmsg.format(VERSION_NAME))
