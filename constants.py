import re


# Formatting constants
PROBLEM_DIGITS = 3
VERSION_DIGITS = 3


# String and format string constants
PROBLEM_NUMBER = "{{:0{}}}".format(PROBLEM_DIGITS)
VERSION_NUMBER = "{{:0{}}}".format(VERSION_DIGITS)

PROBLEM_NAME = "problem" + PROBLEM_NUMBER
VERSION_NAME = "version" + VERSION_NUMBER

PROBLEM_FILE = PROBLEM_NAME + ".py"
VERSION_FILE = VERSION_NAME + ".py"


# Regular expressions constants
RE_PROBLEM_RAW = r"problem\d{{{}}}".format(PROBLEM_DIGITS)
RE_VERSION_RAW = r"version\d{{{}}}".format(VERSION_DIGITS)

RE_PROBLEM = re.compile(RE_PROBLEM_RAW)
RE_VERSION = re.compile(RE_VERSION_RAW)

RE_PROBLEM_FILE = re.compile(RE_PROBLEM_RAW + r".py")
RE_VERSION_FILE = re.compile(RE_VERSION_RAW + r".py")
