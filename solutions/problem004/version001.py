# Version-specific constants - EDIT THESE VALUES
VERSION_NAME = "Version001 - Bruteforce bottom-up (stringpal)"
VERSION_DESCRIPTION = """
Try all possible combinations of n-digit numbers to find the combination
that will create the largest palindrome.

The palindrome check is done via string conversion.
"""


def _ispalindrome(number):
    return str(number) == str(number)[::-1]


def solution(args):
    """Problem 4 - Version 1
    Try all possible combinations of n-digit numbers to find the
    combination that will create the largest palindrome.

    The palindrome check is done via string conversion.

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

    maxnum = 0
    pair = [0, 0]

    for factor1 in range(minfactor, maxfactor):
        for factor2 in range(factor1, maxfactor):
            num = factor1 * factor2
            if _ispalindrome(num) and num > maxnum:
                maxnum = num
                pair = [factor1, factor2]

    return pair


if __name__ == "__main__":
    errmsg = "Cannot run {} as a standalone script"
    raise RuntimeError(errmsg.format(VERSION_NAME))
