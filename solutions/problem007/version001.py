import utils.primes as primes


# Version-specific constants - EDIT THESE VALUES
VERSION_NAME = "Version001 - Using projecteuler utilities"
VERSION_DESCRIPTION = """
Find the nth prime number using this project's prime number utilities.
"""


def solution(args):
    """Problem 7 - Version 1

    Find the nth prime number using this project's prime number
    utilities.

    Parameters:
        args.n  Which prime number to find

    Return:
        Returh the nth prime number.
    """
    prime_generator = primes.get_prime_generator()
    prime = 1
    for _ in range(args.n):
        prime = next(prime_generator)

    return prime


if __name__ == "__main__":
    errmsg = "Cannot run {} as a standalone script"
    raise RuntimeError(errmsg.format(VERSION_NAME))
