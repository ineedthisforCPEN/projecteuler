# Version-specific constants - EDIT THESE VALUES
VERSION_NAME = "Version001 - Bruteforce"
VERSION_DESCRIPTION = """
Bottom-up brute force approach.
"""


def solution(args):
    """Problem 5 - Version 1

    Bottom-up brute force approach.

    Some steps have been taken to improve brute force computation:

    1) The smallest number that can possibly be divisible by all numbers
    in the given range is the largest number in the range.

    2) The final value must be divisible by the largest number in the
    given range. So we only need to check values divisible by the
    largest number in the given range.

    Parameters:
        args.number     The upper range of numbers (1 - args.numbers)
                        for which to find the smallest number that is
                        divisible by all of these numbers.

    Return:
        The smallest number that is divisible by all numbers in the
        range 1 to args.number.
    """
    product = args.number
    while True:
        for factor in range(1, args.number + 1):
            if product % factor != 0:
                break
        else:
            return product

        product += args.number


if __name__ == "__main__":
    errmsg = "Cannot run {} as a standalone script"
    raise RuntimeError(errmsg.format(VERSION_NAME))
