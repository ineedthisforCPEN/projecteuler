import numpy


# Version-specific constants - EDIT THESE VALUES
VERSION_NAME = "Version003 - Brute force matrix math"
VERSION_DESCRIPTION = """
Calculate each Fibonacci number using matrix math and sum only the even
ones. Skip the even check to reduce branching.

We can skip the even check because we know every third Fibonacci number
(starting from the very first one: 0) is even. So instead of having to
check whether a generated Fibonacci number is even, we can start at 0,
then generate the next 3 Fibonacci numbers to determine the next even
Fibonacci number.

The matrix math required to calculate the next Fibonacci number is as
follows:

[ F_n+2 ] = [ 1  1 ][ F_n+1 ]
[ F_n+1 ]   [ 1  0 ][  F_n  ]

Or, as shorthand, with F_n being the vertical vector [F_n+1, F_n]:

F_n+1 = AF_n

So if we want to find the third Fibonacci number:

F_n+3 = (A^3)(F_n)

So by using A^3 (the variable A3 in the solution), we can reduce the
number of calculations required.
"""


def solution(resources, args):
    """Problem 2 - Version 3
    Calculate each Fibonacci number using matrix math and sum only the
    even ones. Skip the even check to reduce branching.

    Parameters:
        args.number     The upper limit of the range of numbers over
                        which the sum will be taken

    Return:
        The sum of the even Fibonacci numbers that are less than
        args.number.
    """
    # Note that we start with the Fibonacci numbers 2 and 3. The first
    # Fibonacci number is 0, so it would not increase the sum.
    retval = 0
    A3 = numpy.array([[3, 2], [2, 1]])
    F = numpy.array([3, 2]).reshape(2, 1)

    while F[1] < args.number:
        retval += F[1]
        F = A3.dot(F)

    return retval[0]


if __name__ == "__main__":
    errmsg = "Cannot run {} as a standalone script"
    raise RuntimeError(errmsg.format(VERSION_NAME))
