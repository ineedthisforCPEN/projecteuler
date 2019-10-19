import re


# Formatting constants
MIN_PROBLEM_DIGITS = 3
MAX_PROBLEM_DIGITS = 3

MIN_VERSION_DIGITS = 3
MAX_VERSION_DIGITS = 3

# Regular expressions constants
RE_PROBLEM_RAW = r"problem\d{{{min},{max}}}".format(min=MIN_PROBLEM_DIGITS,
                                                    max=MAX_PROBLEM_DIGITS)
RE_VERSION_RAW = r"version\d{{{min},{max}}}".format(min=MIN_VERSION_DIGITS,
                                                    max=MAX_VERSION_DIGITS)

RE_PROBLEM = re.compile(RE_PROBLEM_RAW)
RE_VERSION = re.compile(RE_VERSION_RAW)

RE_PROBLEM_FILE = re.compile(RE_PROBLEM_RAW + r".py")
RE_VERSION_FILE = re.compile(RE_VERSION_RAW + r".py")