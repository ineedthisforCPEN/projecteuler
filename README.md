# projecteuler

Solving [Project Euler](https://projecteuler.net/) problems using Python.

The goal is to provide a flexible and scalable interface that allows users to run different "versions" (e.g. a brute
force version or a smarter version) of each problem's solution. Eventually, I plan on adding some C code to improve the
performance of some (or all) of the solutions.

## Usage

`python projecteuler.py [options] --problem PROBLEM --version VERSION`

### Examples

`python projecteuler.py --problem 1 --version 1..3,5,8..10`
Run solutions to problem 1. Will run solution versions 1, 2, 3, 5, 8, 9, 10

`python projecteuler.py --time --problem 2 --version 3`
Run the version 3 of the solution to problem 2 and time the result

`python projecteuler.py --time --count 3 --problem 2 --version 3`
Same as example above, but run and time 3 iterations

### Required Arguments

`-p, --problem` The problem whose solution to run.
`-v, --version` A list of versions of the solution to run.

### Options

`--count`   The number of times to run the specified solution(s). This is only applicable when `--time` flag is set
`--time`    When set, times every solution

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

`python generate_version.py [--force] PROBLEM_NUMBER VERSION_NUMBER`

This generates version `VERSION_NUMBER` of the solution for problem `PROBLEM_NUMBER`. The tool generates a version file
using this information and the version template.

Note that `generate_version.py` will not skip versions. This means that if version 1 of the solution is not implemented,
it will fail to create version2 of the solution.

By default, `generate_version.py` fails if the version file to generate already exists, as we don't want to accidentally
overwrite an existing problem file. To overwrite the existing version file, use the `--force` flag.
