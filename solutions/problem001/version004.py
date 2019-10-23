import math


# Version-specific constants - EDIT THESE VALUES
VERSION_NAME = "Formulaic Approach"
VERSION_DESCRIPTION = \
"""A formulaic approach - worst-case constant time.

This works once we notice that the all numbers that are divisible by
3 and those that are divisible by 5 only overlap when the numbers are
divisible by 15. All other numbers in these sequences do not overlap.

This means that if we just sum the numbers divisible by 3 and those
divisible by 5, we will not get the right answer.

Notice that numbers divisible by 15 apear twice in this sum, which is
why we get the wrong answer. To get the correct answer, simply subtract
all numbers divisible by 15.

Here is an example using the range [1,20]

sum_div_3 = 3 + 6 + 9 + 10 + 12 + 15 + 18
sum_div_5 = 5 + 10 + 15 + 20
sum_div_15 = 15

sum = sum_div_3 + sum_div_5 - sum_div_15
    = 3    +6 +9     +12 +15 +18        (+sum_div_3)
        +5       +10     +15     +20    (+sum_div_5)
                         -15            (-sum_div_15)
    = 3 +5 +6 +9 +10 +12 +15 +18 +20

Here, we see that our sum does not have any repeating numbers, meaning
we get the correct answer.
"""


def arithmetic_series_sum(a_1, a_n, d):
    """Calculate the sum of an arithmetic series.

    Parameters:
        a_n     The last element of the series
        d       The difference between elements

    Return:
        The sum of the arithmetic series.
    """
    n = ((a_n - a_1)//d + 1)
    return n*(a_1 + a_n)//2


def solution(args):
    """Problem 1 - Version 4
    Use a formula to determine the the sum.

    Parameters:
        args.number     The upper limit of the range of numbers over
                        which the sum will be taken

    Return:
        Sum of all numbers in range [1, args.number) that are divisible
        by 3 or 5.
    """
    n = args.number - 1
    sum_div_by_3  = arithmetic_series_sum(0, n - (n %  3),  3)
    sum_div_by_5  = arithmetic_series_sum(0, n - (n %  5),  5)
    sum_div_by_15 = arithmetic_series_sum(0, n - (n % 15), 15) if n >= 15 else 0
    return sum_div_by_3 + sum_div_by_5 - sum_div_by_15


if __name__ == "__main__":
    errmsg = "Cannot run {} as a standalone script"
    raise RuntimeError(errmsg.format(VERSION_NAME))