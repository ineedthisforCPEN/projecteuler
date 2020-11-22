import multiprocessing

from utils.misc import get_integer_palindrome_function


# Version-specific constants - EDIT THESE VALUES
VERSION_NAME = "Version003 - Parallelized greedy"
VERSION_DESCRIPTION = """
A parallelized bottom-up greedy algorithm.
"""


_is_palindrome = get_integer_palindrome_function()


def _thread(range_min, range_max):
    """A single bruteforce thread. Finds a value x such that
    range_min <= x < range_max is the largest possible integer
    palindrome.

    This uses a greedy algorithm to optmimize the palindrome search.

    Parameters:
        range_min       The smallest factor to try in the search
        range_max       The largest factor to try in the search

    Return:
        The tuple (range_min, x, product).
        (range_min, 0, 0) if no palindrome was found.
    """
    for factor in reversed(range(range_min, range_max)):
        if _is_palindrome(factor * range_min):
            return (range_min, factor, factor * range_min)
    return (range_min, 0, 0)


def solution(resources, args):
    """Problem 4 - Version 3
    A parallelized bottom-up greedy algorithm.

    Parameters:
        args.digits     The number of digits in the factors used to
                        create the largest palindrome.

    Return:
        The pair of integers that, when multiplied, create the largest
        palindrome of all pairs of numbers with args.digits number of
        digits.
    """
    minfactor = 10 ** (args.digits - 1)
    maxfactor = 10 ** args.digits

    corecount = multiprocessing.cpu_count()
    args = [[i, maxfactor] for i in range(minfactor, maxfactor)]

    pool = multiprocessing.Pool(corecount)
    results = pool.starmap_async(_thread, args).get()
    pool.close()

    results.sort(key=lambda x: x[-1])
    (*pair, _) = results[-1]
    return pair


if __name__ == "__main__":
    errmsg = "Cannot run {} as a standalone script"
    raise RuntimeError(errmsg.format(VERSION_NAME))
