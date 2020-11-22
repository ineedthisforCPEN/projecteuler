"""primes.py

Utilities used for calculating and validating prime numbers.
"""


import enum
import math
import os.path


CACHE_INDEX_GRANULATIRY = 1000
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
        index = prime // CACHE_INDEX_GRANULATIRY

        if index not in CACHED_PRIMES:
            CACHED_PRIMES[index] = []
        CACHED_PRIMES[index].append(prime)


###############################################################################
# Utilities
###############################################################################
def _max_prime():
    max_index = max(CACHED_PRIMES)
    return CACHED_PRIMES[max_index][-1]


###############################################################################
# Prime Generation
###############################################################################
class PrimeGenerator(enum.Enum):
    BRUTEFORCE = 1


def get_prime_generator(algorithm=PrimeGenerator.BRUTEFORCE):
    if algorithm == PrimeGenerator.BRUTEFORCE:
        return _prime_generator_bruteforce()
    else:
        # This else statement is redundant but leave it up. If there are any
        # new algorithms, we can easily just modify the line below to choose
        # the default algorithm without needing to change the structure of the
        # whole if-else logic.
        return _prime_generator_bruteforce()


def _prime_generator_cached():
    """Pulled all cached primes. Always yields 2 first."""
    yield 2
    for index in sorted(CACHED_PRIMES):
        for prime in CACHED_PRIMES[index]:
            yield prime


def _prime_generator_bruteforce():
    """Bruteforce method for generating primes."""
    is_prime = get_prime_verifier()

    generator = _prime_generator_cached()
    for prime in generator:
        yield prime

    prime += 2
    while True:
        while not is_prime(prime):
            prime += 2

        # If it's a prime, cache it! This will make some of the prime
        # verification functions run quicker.
        index = prime // CACHE_INDEX_GRANULATIRY
        if index not in CACHED_PRIMES:
            CACHED_PRIMES[index] = []
        CACHED_PRIMES[index].append(prime)
        yield prime


###############################################################################
# Prime Validation
###############################################################################
class PrimeVerifier(enum.Enum):
    BRUTEFORCE = 1


def get_prime_verifier(algorithm=PrimeVerifier.BRUTEFORCE):
    if algorithm == PrimeVerifier.BRUTEFORCE:
        return _is_prime_bruteforce
    else:
        # This else statement is redundant but leave it up. If there are any
        # new algorithms, we can easily just modify the line below to choose
        # the default algorithm without needing to change the structure of the
        # whole if-else logic.
        return _is_prime_bruteforce


def _is_prime_bruteforce(prime):
    """Check if a number is prime using brute force and some caching.
    Our brute force method is a little smarter than the standard method,
    as we rule some factors out due to the following principles:

    1) We already have a list of cached primes. If our supposed prime is
    cached, we know it's a prime. If it is not cached, but is smaller
    than our largest cached prime, we know that it is not a prime number
    because we assume the cache contains all prime numbers from 2 to the
    largest number stored in the cache.

    2) We do not need to check for factors that are even. We can easily
    eliminate even numbers in the beginning, so checking even factors
    later is redundant.

    3) Every number n has two divisors a and b such that a*b = n and
    a <= b. In the case a == b, we see that a = b = sqrt(n). With this,
    we know there are two sets of factors: those in [1, sqrt(n)) and
    those in (sqrt(n), n]. Because the range of all numbers in
    [1, sqrt(n)] is much smaller than the range of numbers in
    (sqrt(n), n], we will limit our factor search in [1, sqrt(n)), and
    then finally test sqrt(n).

    Assumption: prime > 2

    Parameters:
        prime   The number whose primality to check

    Returns:
        True if "prime" is a prime number, False otherwise.
    """
    # Easiest prime to check
    if prime % 2 == 0:
        return False

    # Check if the prime is cached:
    index = prime // CACHE_INDEX_GRANULATIRY
    if index in CACHED_PRIMES:
        if prime in CACHED_PRIMES[index]:
            return True

    # If the number is not cached, it could still be a prime if it is
    # larger than the largest prime we currently have cached.
    largest_prime = _max_prime()
    if prime < largest_prime:
        return False

    # We've checked the cache with no conclusive results. Now it's time
    # to brute force our prime verification:
    factor = largest_prime + 2
    while factor < math.ciel(math.sqrt(prime)):
        if prime % factor == 0:
            return False
        factor += 2
    return True


if __name__ == "__main__":
    maxprime = max(CACHED_PRIMES[max(CACHED_PRIMES)])
    print(maxprime)
