import numpy


# Version-specific constants - EDIT THESE VALUES
VERSION_NAME = "Version001 - Bruteforce"
VERSION_DESCRIPTION = """
Go through all possible 4-adjacent values (vertical, horizontal, and
diagonal) in the 20 x 20 matrix and find the maximum product.
"""


def solution(resources, args):
    """Problem 11 - Version 1

    Go through all possible 4-adjacent values (vertical, horizontal, and
    diagonal) in the 20 x 20 matrix and find the maximum product.

    Parameters:
        resources   The 20 x 20 matrix (numpy.array)

    Return:
        The quadruple (a, b, c, d) such that a x b x c x d is the
        largest product of all possible quadruples in the matrix.
    """
    quadruple = None
    product = 0

    # Check all horizontal adjacent values.
    for row in range(20):
        for col in range(16):
            array = resources[row:row + 1, col:col + 4]
            if numpy.prod(array) > product:
                product = numpy.prod(array)
                quadruple = tuple(array)

    # Check all vertical adjacent values.
    for col in range(20):
        for row in range(16):
            array = resources[row:row + 4, col:col + 1]
            if numpy.prod(array) > product:
                product = numpy.prod(array)
                quadruple = tuple(array)

    # Check all \ diagonal adjacent values.
    for row in range(16):
        for col in range(16):
            array = numpy.array([
                resources[row + 0, col + 0],
                resources[row + 1, col + 1],
                resources[row + 2, col + 2],
                resources[row + 3, col + 3],
            ])
            if numpy.prod(array) > product:
                product = numpy.prod(array)
                quadruple = tuple(array)

    # Check all / diagonal adjacent values.
    for row in range(16):
        for col in range(16):
            array = numpy.array([
                resources[row + 0, col + 3],
                resources[row + 1, col + 2],
                resources[row + 2, col + 1],
                resources[row + 3, col + 0],
            ])
            if numpy.prod(array) > product:
                product = numpy.prod(array)
                quadruple = tuple(array)

    return quadruple


if __name__ == "__main__":
    errmsg = "Cannot run {} as a standalone script"
    raise RuntimeError(errmsg.format(VERSION_NAME))
