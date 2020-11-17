import importlib
import os
import os.path

from projecteuler import constants as const


class Problem:
    """Abstract class use for all problem implementations. Provides
    some basic, necessary functionality, but leave problem-specific
    definitions up to the inheriting classes.

    Note: create_parser method must be implemented in the inheriting
    classes.
    """
    def __init__(self, args):
        self.parser = None
        self.args = None

        self.problem_name = ""
        self.problem_summary = ""
        self.problem_desc = ""
        self.problem_versions = {}

    def create_parser(self):
        """Create a custom argument parser for each problem. Each
        problem implementation must implement its own create_parser
        method.

        Parameters:
            None

        Return:
            None
        """
        raise NotImplementedError()

    def get_implemented_versions(self, context=__file__):
        """Get all implemented versions of the problem

        Parameters:
            None

        Return:
            A map of each version of the solution and the function that
            implements this solution.
        """
        problem_dir = os.path.abspath(os.path.dirname(context))
        problem_name = os.path.split(problem_dir)[-1]
        files = next(os.walk(problem_dir))[-1]
        files = \
            [f for f in files if const.RE_VERSION_FILE.match(f) is not None]

        versions = {}
        for version in files:
            # Get only the version name of the file
            version_name = os.path.basename(version)
            version_name = os.path.splitext(version_name)[0]

            # Import the implemented solution
            import_path = "solutions.{}.{}".format(problem_name, version_name)
            imported = importlib.import_module(import_path)
            solution = getattr(imported, "solution")

            # Now map the implemented solution (function) to the version name
            versions[version_name] = solution

        return versions

    def is_version_implemented(self, version):
        return version in self.problem_versions

    def run_solution(self, version):
        """Run the specified solution for this problem.

        Parameters:
            version     The version of the solution to run

        Return:
            The return value of the implemented solution that is run.
        """
        return self.problem_versions[version](self.args)
