# Version-specific constants - EDIT THESE VALUES
VERSION_NAME = "Version001 - Bruteforce"
VERSION_DESCRIPTION = """
Manually calculate the sum of squares and the square of the sum.
"""


def solution(resources, args):
    """Problem 6 - Version 1

    Manually calculate the sum of squares and the square of the sum.

    Parameters:
        args.number     The upper limit of the range of numbers to use
                        for the calculation (i.e. 1 to args.number)

    Return:
        (1^2 + 2^2 + ... + n^2) - (1 + 2 + ... + n)^2
    """
    sum_of_square = sum([i*i for i in range(1, args.number + 1)])
    square_of_sum = sum(range(1, args.number + 1)) ** 2
    return square_of_sum - sum_of_square


if __name__ == "__main__":
    errmsg = "Cannot run {} as a standalone script"
    raise RuntimeError(errmsg.format(VERSION_NAME))
