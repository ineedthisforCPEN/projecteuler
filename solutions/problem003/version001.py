import utils.primes as primes


# Version-specific constants - EDIT THESE VALUES
VERSION_NAME = "Version001 - Using projecteuler utilities"
VERSION_DESCRIPTION = """
Find the largest prime factor with the use of this project's prime
number utilities.
"""


def solution(args):
    """Problem 3 - Version 1
    Find the largest prime factor with the use of this project's prime
    number utilities.

    Parameters:
        args.number     The number whose largest prime factor to find

    Return:
        Return the largest prime factor of args.number.
    """
    largest_prime_factor = 1
    number = args.number
    prime_generator = primes.prime_generator()

    while number > 1:
        prime = next(prime_generator)
        if number % prime == 0:
            number /= prime
            largest_prime_factor = prime

    if largest_prime_factor == 1:
        largest_prime_factor = args.number

    return largest_prime_factor


if __name__ == "__main__":
    errmsg = "Cannot run {} as a standalone script"
    raise RuntimeError(errmsg.format(VERSION_NAME))
