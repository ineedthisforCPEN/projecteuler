import argparse
import html.parser
import os
import os.path
import sys
import textwrap
import urllib.request


PROJECT_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), "..", ".."))


class ProblemParser(html.parser.HTMLParser):
    """Custom HTML parser to determine the problem name and description
    of the problem given its HTML code.

    Assumptions made:
        There is only one section with <h2> tags and those tags contain
        the problem name.

        All data in a <div> tag with an attribute whose value is
        "problem" is the problem description.
    """
    def __init__(self):
        super().__init__()

        self.start_tag = ""
        self.div_problem_desc = False
        self.div_problem_name = False

        self.problem_name = "Problem {} - ".format(const.PROBLEM_NUMBER)
        self.problem_desc = ""

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "h2":
            self.div_problem_name = True
        if tag.lower() == "div":
            for _, value in attrs:
                if value.lower() == "problem":
                    self.div_problem_desc = True
                    break

    def handle_data(self, data):
        if self.div_problem_name:
            self.problem_name += data
        elif self.div_problem_desc:
            self.problem_desc += data

    def handle_endtag(self, tag):
        if tag.lower() in ["div", "h2"]:
            self.div_problem_desc = False
            self.div_problem_name = False


def argument_parser():
    """Get and process arguments and handle exceptions

    Parameters:
        None

    Return:
        Returns the processed argument object.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("problem", type=int)
    parser.add_argument("--force", "-f", action="store_true")
    args = parser.parse_args()

    problem_file = os.path.join(PROJECT_DIR,
                                "solutions",
                                const.PROBLEM_NAME.format(args.problem),
                                const.PROBLEM_FILE.format(args.problem))

    if args.problem < 1:
        errmsg = "Invalid problem number {} - must be positive integer"
        errmsg = errmsg.format(args.problem)
        raise ValueError(errmsg)
    if not args.force and os.path.exists(problem_file):
        errmsg = "Problem {} is already implemented. If you wish to " + \
                 "continue, please use the -f (or --force) flag when " + \
                 "running generate_problem"
        errmsg = errmsg.format(args.problem)
        raise ValueError(errmsg)

    return args.problem


def cleanup_on_exception(problem):
    """Clean up any created files and directories if the problem
    specified in the command line does not exist on projecteuler.net.

    Parameters:
        problem     The problem number whose files to clean up

    Return:
        None.
    """
    problem_dir = os.path.join(PROJECT_DIR,
                               "solutions",
                               const.PROBLEM_NAME.format(problem))
    problem_file = os.path.join(problem_dir,
                                const.PROBLEM_FILE.format(problem))

    if os.path.exists(problem_file):
        os.remove(problem_file)
    if os.path.exists(problem_dir):
        os.rmdir(problem_dir)


def create_problem_from_template(parser, problem):
    """Create a new problem file from the gathered information.

    Parameter:
        parser      The parser object contiaining problem information
        problem     The problem number

    Return:
        None.
    """
    problem_dir_name = os.path.join(PROJECT_DIR,
                                    "solutions",
                                    const.PROBLEM_NAME.format(problem))
    problem_file_name = os.path.join(problem_dir_name,
                                     const.PROBLEM_FILE.format(problem))
    template_file_name = os.path.join(PROJECT_DIR,
                                      "templates",
                                      "problem.template")

    # Get the template and fill it in with the data parsed from the HTML file.
    # Wrap all longer string to 72 characters as outlined in PEP8.
    generated_problem = ""
    with open(template_file_name, "r") as template_file:
        template = template_file.read()

        problem_name = parser.problem_name.strip()
        problem_desc = parser.problem_desc.strip().replace("\n"," ")
        problem_desc = "\n".join(textwrap.wrap(problem_desc, 72))
        problem_summary = problem_desc[:65] + "..."

        generated_problem = template.format(
                problem_number=problem,
                problem_name=problem_name,
                problem_summary=problem_summary,
                problem_description=problem_desc)

    # Create a new file and write the formatted problem template
    if not os.path.exists(problem_dir_name):
        os.mkdir(problem_dir_name)
    with open(problem_file_name, "w") as problem_file:
        problem_file.write(generated_problem)


def parse_html(problem):
    """Find the problem definition from projecteuler.net, then scrape
    the HTML to extract the problem name and description.

    Parameters:
        problem     The problem number to read and scrape

    Return:
        The parser object that stores the information scraped from the
        HTML.
    """
    url = "https://projecteuler.net/problem=" + str(problem)

    print("Trying URL {}".format(url))
    open_url = urllib.request.urlopen(url)
    print("HTTP Status Code: {}".format(open_url.status))
    print("Received data from {}".format(open_url.url))

    if open_url.url != url:
        cleanup_on_exception(problem)
        errmsg = "Problem {} does not exist on projecteuler.net"
        errmsg = errmsg.format(problem)
        raise NotImplementedError(errmsg)

    # Read, parse, and extract particular data from the HTTP content
    # content = open_url.read().decode("utf-8")
    parser = ProblemParser()
    parser.problem_name = parser.problem_name.format(problem)
    parser.feed(open_url.fp.read().decode("utf-8"))
    return parser


def main():
    problem = argument_parser()
    parser = parse_html(problem)
    create_problem_from_template(parser, problem)
    print("Generated problem file for problem {}".format(problem))


if __name__ == "__main__":
    # Add projecteuler to system path to make use of constants and templates
    import_dir = os.path.abspath(os.path.join(PROJECT_DIR, ".."))
    if import_dir not in sys.path:
        sys.path.append(import_dir)

    import projecteuler.constants as const
    main()