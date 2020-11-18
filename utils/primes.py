"""primes.py

Utilities used for calculating and validating prime numbers.
"""


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
# Prime Generation
###############################################################################
def prime_generator():
    """A generator that produces prime number. Makes use of caching for
    some performance benefits when calculating the first few primes.

    Yields:
        Yields the next prime number.
    """
    yield 2

    # First, yield all of the cached primes
    prime = 3
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
        Yields the next prime number.
    """
    # Even numbers are not primes (assuming we start from prime > 2)
    if prime % 2 == 0:
        prime += 1

    while True:
        while not is_prime(prime):
            prime += 2

        index = prime // CACHE_INDEX_GRANULATIRY
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
    index = prime // CACHE_INDEX_GRANULATIRY
    if index in CACHED_PRIMES:
        return prime in CACHED_PRIMES[index]

    if _is_prime_smarter_bruteforce(prime):
        if index not in CACHED_PRIMES:
            CACHED_PRIMES[index] = []
        CACHED_PRIMES[index].append(prime)
        return True
    return False


def _is_prime_smarter_bruteforce(prime):
    """Check if a number is prime using a modified bruteforce method.
    Every number n has two divisors a and b such that:
        a * b = n
        a <= b

    In the case where a == b, we know that:
        a = b = sqrt(n)

    We know that every number is made up of prime factors. So in order
    to determine if a number is prime, we can check all know prime
    numbers below sqrt(n) and if any can divide our supposed prime, we
    know that it is not, in fact, a prime. Because we will know more
    prime numbers smaller that sqrt(n) than prime numbers larger than
    sqrt(n), we conduct our search for a divisor in the range
    [3,sqrt(n)].

    If our first divisor, the odd number closest to sqrt(n), is not in
    our list of know primes, then we must use our bruteforce method to
    determine if there are any divisors for the supposed prime between
    the first divisor and the largest know prime. We can do this by
    iterating over all odd numbers between these two values, and
    checking if they are divisors of the supposed prime.

    Assumption: prime > 2

    Parameters:
        prime   The number whose primality to check

    Returns:
        True if "prime" is a prime number, False otherwise.
    """
    # Easiest check to make
    if prime % 2 == 0:
        return False

    # Calculate our starting # point: the odd number closes to the square root
    # of our supposed prime.
    divisor = math.ceil(math.sqrt(prime)) - (1 - prime % 2)

    # Run the bruteforce method if our divisor is not a cached prime.
    while divisor // CACHE_INDEX_GRANULATIRY not in CACHED_PRIMES and divisor > 1:
        if prime % divisor == 0:
            return False
        divisor -= 2

    # Now our divisor is approaching the cached primes. However, it might not
    # be a cached prime. Check all possible divisors until we reach our first
    # cached prime.
    #
    # NOTE: If there are no cached primes, largest_prime will be 1. This allows
    # us to run the full bruteforce method if there are no cached primes.
    index = divisor // CACHE_INDEX_GRANULATIRY
    largest_prime = CACHED_PRIMES.get(index, [1])[-1]

    while divisor > largest_prime:
        if prime % divisor == 0:
            return False
        divisor -= 2

    # Now our divisor is (or could be) a known prime. Go through each known
    # prime to determine if any of them are divisors of the supposed prime.
    index = divisor // CACHE_INDEX_GRANULATIRY
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
