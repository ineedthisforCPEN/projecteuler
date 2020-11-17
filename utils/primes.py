"""primes.py

Utilities used for calculating and validating prime numbers.
"""


import math
import os.path


CACHED_PRIMES = {}
PROJECT_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__),
                                           "..",
                                           ".."))
PRIME_FILE = os.path.join(PROJECT_DIR, "resources", "primes.txt")


# No matter what, we want to try to load a list of known primes into our cache.
# This will speed up some performance at the cost of memory and some overhead
# when first loading the module.
with open(PRIME_FILE, "r") as prime_file:
    for prime in prime_file:
        prime = int(prime)
        index = prime // 1000

        if index not in CACHED_PRIMES:
            CACHED_PRIMES[index] = []
        CACHED_PRIMES[index].append(prime)


###############################################################################
# Prime Generation
###############################################################################
def prime_generator():
    """A generator that produces prime number. Makes use of caching for
    some performance benefits when calculating the first few primes.

    Yields:
        Yields the next prime number.
    """
    prime = 2

    # First, yield all of the cached primes
    for index in sorted(CACHED_PRIMES.keys()):
        for p in CACHED_PRIMES[index]:
            prime = p
            yield prime

    # Once the cache is exhausted, start calculating the remaining primes
    generator = _prime_generator_bruteforce(prime + 2)
    while True:
        yield(next(generator))


def _prime_generator_bruteforce(prime):
    """A generator that produces prime numbers using a bruteforce
    method.

    Assumption: prime > 2

    Parameters:
        prime   The number from which to start calculating primes

    Yields:
        Yields the next prime number
    """
    # Even numbers are not primes (assuming we start from prime > 2)
    if prime % 2 == 0:
        prime += 1

    while True:
        while not is_prime(prime):
            prime += 2

        index = prime // 1000
        if index not in CACHED_PRIMES:
            CACHED_PRIMES[index] = []
        CACHED_PRIMES[index].append(prime)
        yield prime


###############################################################################
# Prime Validation
###############################################################################
def is_prime(prime):
    """Checks if the input number is a prime number.

    Parameters:
        prime   The number whose primality to check

    Returns:
        True if "prime" is a prime number, False otherwise.
    """
    # Check the cache first
    index = prime // 1000
    if index in CACHED_PRIMES:
        return prime in CACHED_PRIMES[index]

    if _is_prime_bruteforce(prime):
        CACHED_PRIMES[index] = prime
        return True
    return False


def _is_prime_bruteforce(prime):
    """Check if a number is prime using a bruteforce method.

    Assumption: prime > 2

    Parameters:
        prime   The number whose primality to check

    Returns:
        True if "prime" is a prime number, False otherwise.
    """
    # Easiest check to make
    if prime % 2 == 0:
        return False

    # This prime isn't cached so we need to check.
    divisor = math.ceil(math.sqrt(prime))
    while divisor // 1000 not in CACHED_PRIMES:
        # The divisor is not cached. We have to use the less inteligent
        # bruteforce method to check if this is a prime
        if prime % divisor == 0:
            return False
        divisor -= 2

    index = divisor // 1000
    while index >= 0:
        primes = CACHED_PRIMES.get(index, [])
        for divisor in reversed(primes):
            if prime % divisor == 0:
                return False
        index -= 1

    # It *is* a prime!
    return True


if __name__ == "__main__":
    maxprime = max(CACHED_PRIMES[max(CACHED_PRIMES.keys())])
    print(maxprime)
