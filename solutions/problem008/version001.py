import functools
import operator


# Version-specific constants - EDIT THESE VALUES
VERSION_NAME = "Version001 - Bruteforce"
VERSION_DESCRIPTION = """
Go through the entire 1000-digit number and calculate the product of
each digit in the specified numbers of digits, then find the maximum.
"""


def solution(resources, args):
    """Problem 8 - Version 1

    Go through the entire 1000-digit number and calculate the product of
    each digit in the specified numbers of digits, then find the
    maximum.

    Parameters:
        resources       The 1000-digit number
        args.digits     The number of digits whose product to calculate

    Return:
        The maximum product of a given number of digits in the
        1000-digit number.
    """
    max_product = 0

    for index in range(len(resources) - args.digits + 1):
        subinteger = resources[index:index + args.digits]
        factors = [int(digit) for digit in subinteger]
        product = functools.reduce(operator.mul, factors)
        max_product = max(product, max_product)

    return max_product


if __name__ == "__main__":
    errmsg = "Cannot run {} as a standalone script"
    raise RuntimeError(errmsg.format(VERSION_NAME))
