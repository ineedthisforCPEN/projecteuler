# projecteuler

Solving [Project Euler](https://projecteuler.net/) problems using Python.

The goal is to provide a flexible and scalable interface that allows users to run different "versions" (e.g. a brute
force version or a smarter version) of each problem's solution. Eventually, I plan on adding some C code to improve the
performance of some (or all) of the solutions.

## Usage

`python euler.py [options] --problem PROBLEM --version VERSION`

### Examples

`python euler.py --list`\
Lists all implemented problems

`python euler.py --list --problem 1`\
Lists all implementated versions of the solution to problem 1

`python euler.py --problem 1 --version 1..3,5,8..10`\
Run solutions to problem 1. Will run solution versions 1, 2, 3, 5, 8, 9, 10

`python euler.py --time --problem 2 --version 3`\
Run the version 3 of the solution to problem 2 and time the result

`python euler.py --time --count 3 --problem 2 --version 3`\
Same as example above, but run and time 3 iterations

### Required Arguments

Though there are cases where `projecteuler` can run without these arguments, they are required to actually execute the
solution code.

`-p, --problem` The problem whose solution to run.

`-v, --version` A list of versions of the solution to run.

### Options

`--count`   The number of times to run the specified solution(s). This is only applicable when `--time` flag is set

`--list`    List the implemented problems. If the `--problem` argument is given, list the implemented solution versions

`--time`    When set, times every run of every solution version

## Adding Problem Files

To add a problem file, use the tool `generate_problem.py` from the `tools` directory.

`python generate_problem.py [--force] PROBLEM_NUMBER`

This generates the problem file for `PROBLEM_NUMBER`. The tools searches for the problem number in
[Project Euler](https://projecteuler.net/), scrapes problem information from the webpage if found, then generates a
problem file using a problem file template and the scraped information.

By default, `generate_problem.py` fails if the problem file to generate already exists, as we don't want to accidentally
overwrite an existing problem file. To overwrite the existing problem file, use the `--force` flag.

## Adding Version Files

To add a version file, use the tool `generate_version.py` from the `tools` directory.

`python generate_version.py [--force] PROBLEM_NUMBER VERSION_RANGE`

This tries to generate all version in `VERSION_RANGE` of the solution for problem `PROBLEM_NUMBER`. The tool generates a
version file using this information and the version template. A version range must be either a single number or
formatted as `start..end` which represents a range of number from `start` to `end` inclusive (i.e. 1..4 -> 1,2,3,4).

Note that `generate_version.py` will not skip versions. This means that if version 1 of the solution is not implemented,
it will fail to create version 2 of the solution.

By default, `generate_version.py` fails if the version file to generate already exists, as we don't want to accidentally
overwrite an existing problem file. To overwrite the existing version file, use the `--force` flag.
