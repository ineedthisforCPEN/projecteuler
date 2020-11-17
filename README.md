# projecteuler

Solving [Project Euler](https://projecteuler.net/) problems using Python.

The goal is to provide a flexible and scalable interface that allows users to
run different "versions" (e.g. a brute force version or a smarter version) of
each problem's solution. Eventually, I plan on adding some C code to improve
the performance of some (or all) of the solutions.

## Usage

General usage information can found from the command line.

`python euler.py [case] -h`

There are three different use cases.

### Listing Solution Implementations

List all problems where a solution has been implemented.\
`python euler.py info [--problems PROBLEMS] [--verbose]`

The optional `--problems` parameter allows users to specify a range of problems
to check and see if the solutions have been implemented. If a solution has not
been implemented, or it has been implemented poorly, a warning will be shown.
If this parameter is not provided, all implementations will be listed.

If the `--verbose` flag is set, then all of the different solution versions
will be listed as well.

### Running a Solution

Execute a solution to a given problem.\
`python euler.py run --problem PROBLEM [--versions VERSIONS] PARAMETERS`

The `--problems` parameter specifies which Euler Project problem to solve.

The optional `--versions` parameter specifies which solution versions to run.
If no versions are specified, then all implemented versions will be run. If a
version number that does not exist is passed, a warning will be shown to
indicate that it has not been implemented.

The remaining `PARAMETERS` will be passed to the solution as arguments. Each
solution will have a unique argument parser. To see what parameters are
required for the solution, enter the following command

`python euler.py run --problem PROBLEM -h`

### Profiling a Solution Implementation

Profile a solution to a given problem to determine its performance and resource
usage.\
`python euler.py test [--count COUNT] --problem PROBLEM [--versions VERSIONS] PARAMETERS`

The only difference between this and solution execution is the `--count`
parameter which allows users to specify how many times the solution should be
executed during profiling. The default number of iterations is 3.

### Examples

List all implemented solutions\
`python euler.py info`

List all implemented solutions and all the implemented solution versions\
`python euler.py info --verbose`

List solutions 1 through 10 and check if they are implemented\
`python euler.py info --problems 1..10`

Run version 1 of the solution for
[Problem 1](https://projecteuler.net/problem=1)\
`python euler.py run --problem 1 --versions 1 -n 1000`

Run all solutions for [Problem 1](https://projecteuler.net/problem=1)\
`python euler.py run --problem 1 -n 1000`

Profile versions 1 and 2 of the solution for
[Problem 1](https://projecteuler.net/problem=1)\
`python euler.py test --problem 1 --versions 1,2 -n 1000`

Profile all solutions for [Problem 1](https://projecteuler.net/problem=1)\
`python euler.py test --problem 1 -n 1000`

Profile all solutions for [Problem 1](https://projecteuler.net/problem=1)
running each solution 5 times\
`python euler.py test --count 5 --problem 1 -n 1000`

## Adding Problem Files

To add a problem file, use the tool `generate_problem.py` from the `tools`
directory.

`python generate_problem.py [--force] PROBLEM_NUMBER`

This generates the problem file for `PROBLEM_NUMBER`. The tools searches for
the problem number in [Project Euler](https://projecteuler.net/), scrapes
problem information from the webpage if found, then generates a problem file
using a problem file template and the scraped information.

By default, `generate_problem.py` fails if the problem file to generate already
exists, as we don't want to accidentally overwrite an existing problem file. To
overwrite the existing problem file, use the `--force` flag.

## Adding Version Files

To add a version file, use the tool `generate_version.py` from the `tools`
directory.

`python generate_version.py [--force] PROBLEM_NUMBER VERSION_RANGE`

This tries to generate all version in `VERSION_RANGE` of the solution for
problem `PROBLEM_NUMBER`. The tool generates a version file using this
information and the version template. A version range must be either a single
number or formatted as `start..end` which represents a range of number from
`start` to `end` inclusive (i.e. 1..4 -> 1,2,3,4).

Note that `generate_version.py` will not skip versions. This means that if
version 1 of the solution is not implemented, it will fail to create version 2
of the solution.

By default, `generate_version.py` fails if the version file to generate already
exists, as we don't want to accidentally overwrite an existing problem file. To
overwrite the existing version file, use the `--force` flag.
