import enum


###############################################################################
# INTEGER PALINDROME
###############################################################################
class PalindromeAlgorithm(enum.Enum):
    INTCOMPARE = 1
    STRCOMPARE = 2


def get_integer_palindrome_function(algorithm=PalindromeAlgorithm.STRCOMPARE):
    if algorithm == PalindromeAlgorithm.INTCOMPARE:
        return _is_palindrome_intcomp
    elif algorithm == PalindromeAlgorithm.STRCOMPARE:
        return _is_palindrome_strcomp
    else:
        # This else statement is redundant but leave it up. If there are any
        # new algorithms, we can easily just modify the line below to choose
        # the default algorithm without needing to change the structure of the
        # whole if-else logic.
        return _is_palindrome_strcomp


def _is_palindrome_intcomp(n):
    """Integer palindrome algorithm using integer comparison."""
    copy = n
    rev = 0

    while copy > 0:
        rev = 10*rev + (copy % 10)
        copy //= 10

    return rev == n


def _is_palindrome_strcomp(n):
    """Integer palindrome algorithm using string comparison."""
    return str(n) == str(n)[::-1]
