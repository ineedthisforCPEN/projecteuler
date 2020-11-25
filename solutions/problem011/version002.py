import numpy
import multiprocessing


# Version-specific constants - EDIT THESE VALUES
VERSION_NAME = "Version002 - Bruteforce (multithreaded)"
VERSION_DESCRIPTION = """
Go through all possible 4-adjacent values (vertical, horizontal, and
diagonal) in the 20 x 20 matrix and find the maximum product.

Each type of quadruple (vertical, horizontal, and the diagonals) will
have its own thread/process.
"""


def _thread_diagonal_tlbr(matrix, return_dict):
    """Thread for '\' diagonals quadruples."""
    quadruple = None
    product = 0

    for row in range(16):
        for col in range(16):
            array = numpy.array([
                matrix[row + 0, col + 0],
                matrix[row + 1, col + 1],
                matrix[row + 2, col + 2],
                matrix[row + 3, col + 3],
            ])
            if numpy.prod(array) > product:
                product = numpy.prod(array)
                quadruple = tuple(array)

    return_dict[product] = quadruple


def _thread_diagonal_trbl(matrix, return_dict):
    """Thread for '/' diagonals quadruples."""
    quadruple = None
    product = 0

    for row in range(16):
        for col in range(16):
            array = numpy.array([
                matrix[row + 0, col + 3],
                matrix[row + 1, col + 2],
                matrix[row + 2, col + 1],
                matrix[row + 3, col + 0],
            ])
            if numpy.prod(array) > product:
                product = numpy.prod(array)
                quadruple = tuple(array)

    return_dict[product] = quadruple


def _thread_horizontal(matrix, return_dict):
    """Thread for horizontal quadruples."""
    quadruple = None
    product = 0

    for row in range(20):
        for col in range(16):
            array = numpy.array([
                matrix[row, col + 0],
                matrix[row, col + 1],
                matrix[row, col + 2],
                matrix[row, col + 3],
            ])
            if numpy.prod(array) > product:
                product = numpy.prod(array)
                quadruple = tuple(array)

    return_dict[product] = quadruple


def _thread_vertical(matrix, return_dict):
    """Thread for vertical quadruples."""
    quadruple = None
    product = 0

    for col in range(20):
        for row in range(16):
            array = numpy.array([
                matrix[row + 0, col],
                matrix[row + 1, col],
                matrix[row + 2, col],
                matrix[row + 3, col],
            ])
            if numpy.prod(array) > product:
                product = numpy.prod(array)
                quadruple = tuple(array)

    return_dict[product] = quadruple


def solution(resources, args):
    """Problem 11 - Version 2

    Go through all possible 4-adjacent values (vertical, horizontal, and
    diagonal) in the 20 x 20 matrix and find the maximum product.

    Each type of quadruple (vertical, horizontal, and the diagonals)
    will have its own thread/process.

    Parameters:
        resources   The 20 x 20 matrix (numpy.array)

    Return:
        The quadruple (a, b, c, d) such that a x b x c x d is the
        largest product of all possible quadruples in the matrix.
    """
    return_dict = multiprocessing.Manager().dict()
    pdiag1 = multiprocessing.Process(target=_thread_diagonal_tlbr,
                                     args=(resources, return_dict))
    pdiag2 = multiprocessing.Process(target=_thread_diagonal_trbl,
                                     args=(resources, return_dict))
    phorz = multiprocessing.Process(target=_thread_horizontal,
                                    args=(resources, return_dict))
    pvert = multiprocessing.Process(target=_thread_vertical,
                                    args=(resources, return_dict))

    pdiag1.start()
    pdiag2.start()
    phorz.start()
    pvert.start()

    pdiag1.join()
    pdiag2.join()
    phorz.join()
    pvert.join()

    return return_dict[max(return_dict)]


if __name__ == "__main__":
    errmsg = "Cannot run {} as a standalone script"
    raise RuntimeError(errmsg.format(VERSION_NAME))
