import argparse
import os
import os.path
import sys


PROJECT_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__),
                                           "..",
                                           ".."))


def argument_parser():
    """Get and process arguments and handle exceptions

    Parameters:
        None

    Return:
        Returns the processed argument object.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("problem", type=int)
    parser.add_argument("version", type=str)
    parser.add_argument("--force", "-f", action="store_true")
    args = parser.parse_args()

    problem_dir = os.path.join(PROJECT_DIR,
                               "solutions",
                               const.PROBLEM_NAME.format(args.problem))
    problem_file = os.path.join(problem_dir,
                                const.PROBLEM_FILE.format(args.problem))

    # Process and handle errors for problem argument
    if args.problem < 1:
        errmsg = "Invalid problem number {} - must be positive integer"
        raise ValueError(errmsg.format(args.problem))
    if not os.path.exists(problem_file):
        errmsg = "Problem file \"{f}\" does not exist - please generate " + \
                 "it using generate_problem.py"
        errmsg = errmsg.format(f=const.PROBLEM_FILE.format(args.problem),
                               n=args.problem)
        raise NotImplementedError(errmsg)

    # Process the version argument
    versions = utils_args.range_string_to_list(args.version)
    prev_version_file = os.path.join(problem_dir,
                                     const.VERSION_FILE.format(versions[0]-1))

    # Process and handle errors for version argument
    overlap = False
    if versions[0] < 1:
        raise ValueError("All version numbers must be greater than 0")
    if versions[0] > 1 and not os.path.exists(prev_version_file):
        errmsg = "Invalid version range - cannot implement version " + \
                 "{n} before implementing version {p}"
        raise ValueError(errmsg.format(n=versions[0], p=versions[0]-1))
    for version in versions:
        version_file = os.path.join(problem_dir,
                                    const.VERSION_FILE.format(version))
        if not args.force and os.path.exists(version_file):
            overlap = True
            warnstr = "Version {} already implemented".format(version)
            print("WARNING: {}".format(warnstr))
    if overlap:
        errmsg = "Some of the versions specified already exist. If you " + \
                 "wish to continue (and overwrite the existing files) " + \
                 "please use the --force flag"
        raise ValueError(errmsg)

    return (args.problem, versions)


def create_version_from_template(problem, version):
    """Create a new version file from the problem and version number.

    Parameter:
        problem     The problem number
        version     The version number

    Return:
        None.
    """
    version_dir_name = os.path.join(PROJECT_DIR,
                                    "solutions",
                                    const.PROBLEM_NAME.format(problem))
    version_file_name = os.path.join(version_dir_name,
                                     const.VERSION_FILE.format(version))
    template_file_name = os.path.join(PROJECT_DIR,
                                      "templates",
                                      "version.template")

    # Get the template and fill it in with relevant information. Wrap
    # all longer string to 72 characters as outlined in PEP8.
    generated_version = ""
    with open(template_file_name, "r") as template_file:
        template = template_file.read()
        version_name = const.VERSION_NAME.format(version).capitalize()

        generated_version = template.format(
                version_name=version_name,
                version_number=version,
                problem_number=problem)

    # Create a new file and write the formatted problem template
    with open(version_file_name, "w") as version_file:
        version_file.write(generated_version)


def main():
    problem, versions = argument_parser()
    for version in versions:
        create_version_from_template(problem, version)
        print("Generated version file for version {}".format(version))


if __name__ == "__main__":
    # Add projecteuler to system path to make use of constants and templates
    import_dir = os.path.abspath(os.path.join(PROJECT_DIR, ".."))
    if import_dir not in sys.path:
        sys.path.append(import_dir)

    import projecteuler.constants as const
    import projecteuler.utils.arguments as utils_args
    main()
