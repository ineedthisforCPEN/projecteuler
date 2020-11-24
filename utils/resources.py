import collections
import numpy
import os.path

from projecteuler import constants as const


_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
_RESOURCE_DIR = os.path.abspath(os.path.join(_BASE_DIR,
                                             "..",
                                             "resources"))

_STRING_TO_TYPE_MAP = collections.defaultdict(lambda: _nonetypeclass, {
    "integer": int,
    "float": float,
    "matrix": numpy.array,
    "string": str,
})


def _nonetypeclass(*args, **kwargs):
    """Initializer function that returns Nonetype no matter what."""
    return None


def load_problem_resources(problem):
    """Load the resources for a specific problem.

    Parameters:
        problem     The problem number whose resources to load

    Return:
        Return problem's resources. Returns None if no resources were
        found or if the resources were not loaded as expected.
    """
    filename = os.path.join(_RESOURCE_DIR,
                            const.RESOURCE_FILE.format(problem))
    if not os.path.exists(filename):
        return None

    value = None
    with open(filename, "r") as openfile:
        lines = openfile.read().splitlines()
        typeclass = _STRING_TO_TYPE_MAP[lines[0]]

        if typeclass is numpy.array:
            value = numpy.array([
                [value for value in line.split(" ")] for line in lines[1:]
            ], dtype=int)
        else:
            value = typeclass("".join(lines[1:]))

    return value
