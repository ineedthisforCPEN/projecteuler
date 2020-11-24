import utils.primes as primes


# Version-specific constants - EDIT THESE VALUES
VERSION_NAME = "Version001 - Using utilities"
VERSION_DESCRIPTION = """
Calculate the sum of all primes under a given number using the prime
utilities.
"""


def solution(resources, args):
    """Problem 10 - Version 1

    Calculate the sum of all primes under a given number using the prime
    utilities.

    Parameters:
        args.number     The upper limit of the prime numbers to sum

    Return:
        The sum of all prime numbers under args.number.
    """
    prime_generator = primes.get_prime_generator()
    prime = next(prime_generator)
    retval = 0

    while prime < args.number:
        retval += prime
        prime = next(prime_generator)

    return retval


if __name__ == "__main__":
    errmsg = "Cannot run {} as a standalone script"
    raise RuntimeError(errmsg.format(VERSION_NAME))
