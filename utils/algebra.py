def arithmetic_sum(a_1, a_n, d):
    """Calculate the sum of an arithmetic series.

    Parameters:
        a_1     The first element of the series
        a_n     The last element of the series
        d       The difference between elements

    Return:
        The sum of the arithmetic series.
    """
    n = ((a_n - a_1)//d + 1)
    return n*(a_1 + a_n) // 2


def arithmetic_sum_n(a_1, d, n):
    """Calculate the sum of an arithmetic series.

    Parameters:
        a_1     The first element of the series
        d       The difference between elements
        n       The number of elements in the series to sum

    Return:
        The sum of n numbers in the arithmetic series.
    """
    a_n = a_1 + d*(n - 1)
    return n*(a_1 + a_n) // 2
