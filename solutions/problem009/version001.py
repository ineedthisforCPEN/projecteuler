# Version-specific constants - EDIT THESE VALUES
VERSION_NAME = "Version001 - Bruteforce"
VERSION_DESCRIPTION = """
Run through all possible combinations of a, b, c such that
a^2 + b^2 = c^2 and the sum a, b, c is the given value.
"""


def solution(resources, args):
    """Problem 9 - Version 1

    Run through all possible combinations of a, b, c such that
    a^2 + b^2 = c^2 and a + b + c = args.number.

    Parameters:
        args.number     The sum a + b + c

    Return:
        The triplet (a, b, c). None if the triple does not exist.
    """
    # The largest possible value of a occurs when all values of a, b, c are as
    # close to args.numbers // 3 as possible
    max_a = (args.number // 3) - 1

    # The largest possible value of b occurs when a is the lowest value, and
    # b and c are as close to (args.number - 1) // 2 as possible
    max_b = (args.number - 1) // 2

    # Add 1 to the maximum because they will be used in the range() function.
    max_a += 1
    max_b += 1

    for a in range(1, max_a):
        for b in range(2, max_b):
            c = args.number - a - b
            if a**2 + b**2 == c**2:
                return (a, b, c)

    # There's a chance that there is no triplet. If that's the case, return
    # None.
    return None


if __name__ == "__main__":
    errmsg = "Cannot run {} as a standalone script"
    raise RuntimeError(errmsg.format(VERSION_NAME))
