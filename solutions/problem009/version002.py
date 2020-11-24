# Version-specific constants - EDIT THESE VALUES
VERSION_NAME = "Version002 - Hardcode shortcut"
VERSION_DESCRIPTION = """
Shortcut the bruteforce method by checking if the sum a + b + c is
divisible by one of the 16 known primitive pythagorean triples where
a, b, c < 100.

If no primitive triple matches to the sum, fall back on the bruteforce
method.
"""


def _bruteforce(triple_sum):
    """Run through all possible combinations of a, b, c such that
    a^2 + b^2 = c^2 and a + b + c = triple_sum.

    Parameters:
        triple_sum  The sum a + b + c

    Return:
        The triplet (a, b, c). None if the triple does not exist.
    """
    # The largest possible value of a occurs when all values of a, b, c are as
    # close to triple_sum // 3 as possible
    max_a = (triple_sum // 3) - 1

    # The largest possible value of b occurs when a is the lowest value, and
    # b and c are as close to (triple_sum - 1) // 2 as possible
    max_b = (triple_sum - 1) // 2

    # Add 1 to the maximum because they will be used in the range() function.
    max_a += 1
    max_b += 1

    for a in range(1, max_a):
        for b in range(2, max_b):
            c = triple_sum - a - b
            if a**2 + b**2 == c**2:
                return (a, b, c)

    # There's a chance that there is no triplet. If that's the case, return
    # None.
    return None


def solution(resources, args):
    """Problem 9 - Version 2

    Shortcut the bruteforce method by checking if the sum a + b + c
    is divisible by one of the 16 known primitive pythagorean triples
    where a, b, c < 300.

    If no primitive triple matches to the sum, fall back on the
    bruteforce method.

    Parameters:
        args.number     The sum a + b + c

    Return:
        The triplet (a, b, c). None if the triple does not exist.
    """
    # All 47 primitives where a, b, c < 300 are stored here as
    # [a, b, c, a + b + c]
    primitives = [
        [3, 4, 5, 12], [5, 12, 13, 30], [8, 15, 17, 40],
        [7, 24, 25, 56], [20, 21, 29, 70], [12, 35, 37, 84],
        [9, 40, 41, 90], [28, 45, 53, 126], [11, 60, 61, 132],
        [16, 63, 65, 144], [33, 56, 65, 154], [48, 55, 73, 176],
        [13, 84, 85, 182], [36, 77, 85, 198], [39, 80, 89, 208],
        [65, 72, 97, 234], [20, 99, 101, 220], [60, 91, 109, 260],
        [15, 112, 113, 240], [44, 117, 125, 286], [88, 105, 137, 330],
        [17, 144, 145, 306], [24, 143, 145, 312], [51, 140, 149, 340],
        [85, 132, 157, 374], [119, 120, 169, 408], [52, 165, 173, 390],
        [19, 180, 181, 380], [57, 176, 185, 418], [104, 153, 185, 442],
        [95, 168, 193, 456], [28, 195, 197, 420], [84, 187, 205, 476],
        [133, 156, 205, 494], [21, 220, 221, 462], [140, 171, 221, 532],
        [60, 221, 229, 510], [105, 208, 233, 546], [120, 209, 241, 570],
        [32, 255, 257, 544], [23, 264, 265, 552], [96, 247, 265, 608],
        [69, 260, 269, 598], [115, 252, 277, 644], [160, 231, 281, 672],
        [161, 240, 289, 690], [68, 285, 293, 646],
    ]

    for primitive in primitives:
        if args.number % primitive[-1] == 0:
            multiplier = args.number // primitive[-1]
            return tuple(i * multiplier for i in primitive[:3])

    return _bruteforce(args.number)


if __name__ == "__main__":
    errmsg = "Cannot run {} as a standalone script"
    raise RuntimeError(errmsg.format(VERSION_NAME))
