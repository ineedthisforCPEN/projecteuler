import collections
import math
import utils.primes as primes


# Version-specific constants - EDIT THESE VALUES
VERSION_NAME = "Version002 - Prime factorization"
VERSION_DESCRIPTION = """
Determine the smallest number divisible by all the numbers in the given
range using prime factors of each of the numbers in the given range.
"""


def _get_prime_factors(n):
    prime_generator = primes.get_prime_generator()
    prime = next(prime_generator)
    max_divisor = math.ceil(math.sqrt(n))

    prime_factors = []
    while prime <= max_divisor:
        while n % prime == 0:
            prime_factors.append(prime)
            n //= prime
        prime = next(prime_generator)

    if len(prime_factors) == 0:
        return collections.Counter([n])
    return collections.Counter(prime_factors)


def solution(resources, args):
    """Problem 5 - Version 2

    Determine the smallest number divisible by all the numbers in the
    given range using prime factors of each of the numbers in the given
    range.

    Parameters:
        args.number     The upper range of numbers (1 - args.numbers)
                        for which to find the smallest number that is
                        divisible by all of these numbers.

    Return:
        The smallest number that is divisible by all numbers in the
        range 1 to args.number.
    """
    prime_factors = collections.defaultdict(int)
    for i in range(1, args.number + 1):
        factors = _get_prime_factors(i)
        for factor in factors:
            prime_factors[factor] = max(factors[factor], prime_factors[factor])

    retval = 1
    for factor in prime_factors:
        retval = retval * (factor ** prime_factors[factor])
    return retval


if __name__ == "__main__":
    errmsg = "Cannot run {} as a standalone script"
    raise RuntimeError(errmsg.format(VERSION_NAME))
