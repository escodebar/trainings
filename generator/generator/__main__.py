from jinja2 import Environment, FileSystemLoader
from jinja2 import environmentfilter
from pathlib import Path
import argparse
import functools
import os
import re
import subprocess
import tempfile


TMPDIR = tempfile.mkdtemp()
REPODIR = Path(TMPDIR) / "repo"
REPODIR.mkdir(mode=0o755)
REPODIR = str(REPODIR)
DOTGITDIR = f"{REPODIR}/.git"
STORAGE = {}


print(REPODIR)


def last_commit_full():
    return run("git rev-parse HEAD").strip()


def last_commit():
    return run("git rev-parse --short HEAD").strip()


def last_tree():
    tree_hash_long = shell("git cat-file -p HEAD | grep 'tree' | cut -d' ' -f2")
    return run(f"git rev-parse --short {tree_hash_long}").strip()


def split_in_parts(command):
    strings = re.findall(r'((?P<quote>[\'"])(.+?)(?P=quote))', command)

    if not strings:
        return command.split(" ")

    strings = [string[0] for string in strings if len(string) > 1]

    replacements = {}
    for index, string in enumerate(strings):
        command = command.replace(string, f"____{index}____")
        replacements[f"____{index}____"] = string.strip('"').strip("'")

    return [replacements.get(part, part) for part in command.split(" ")]


def run(command, gitception=False, input=None, store=None):
    working_directory = DOTGITDIR if gitception else REPODIR

    if input is not None:
        input = input.encode()

    process = subprocess.run(
        split_in_parts(command), capture_output=True, cwd=working_directory, input=input
    )

    output = process.stdout.decode().strip().replace(REPODIR, "~/working/directory")

    error = process.stderr.decode().strip().replace(REPODIR, "~/working/directory")

    if not len(output) and len(error):
        output = error

    if store is not None:
        STORAGE[store] = output
        return ""

    return output


def commit_hash(ref, gitception=False):
    return run(f"git rev-parse --short {ref}", gitception=gitception).strip()


@environmentfilter
def commit_hash_filter(environment, ref, gitception=False):
    return commit_hash(ref, gitception=gitception)


def commit_title(ref, gitception=False):
    return run(
        f"git log {ref} -n 1 --oneline --pretty=format:%s", gitception=gitception
    )


@environmentfilter
def commit_title_filter(environment, ref, gitception=False):
    return commit_title(ref, gitception=gitception)


@environmentfilter
def run_filter(
    environment, command, gitception=False, input=None, store=None, quiet=False
):
    if "LAST_COMMIT_FULL" in command:
        command = command.replace("LAST_COMMIT_FULL", last_commit_full())

    if "LAST_COMMIT" in command:
        command = command.replace("LAST_COMMIT", last_commit())

    if "LAST_TREE" in command:
        command = command.replace("LAST_TREE", last_tree())

    output = run(command, gitception=gitception, input=input, store=store)

    if quiet:
        return command

    return "\n".join([command, output])


def shell(command):
    process = subprocess.run(command, capture_output=True, cwd=REPODIR, shell=True)
    stdout = process.stdout.decode().strip()

    return stdout


@environmentfilter
def shell_filter(environment, command):
    shell(command)
    return command


def multirun(commands, gitception=False):
    _run = functools.partial(run, gitception=gitception)
    _commands = commands.strip().split(" && ")
    outputs = map(_run, _commands)
    return list(outputs)[-1]


@environmentfilter
def multirun_filter(environment, commands, gitception=False, quiet=False):
    output = multirun(commands, gitception=gitception)

    if quiet:
        return commands

    return "\n".join([commands, output])


@environmentfilter
def store_filter(environment, store):
    return STORAGE.get(store, "")


def lines(text, *args):
    return "\n".join(text.split("\n")[slice(*args)])


@environmentfilter
def lines_filter(environment, text, *args):
    return lines(text, *args)


def gitception_generator():
    counter = 0
    while True:
        counter += 1

        transform = ""

        if counter % 2:
            transform = "-flipped"

        yield f'<!-- .slide: data-background="./gitception{transform}.jpg" -->'


gitception = gitception_generator()


@environmentfilter
def gitception_filter(environment, *args):
    return next(gitception)


def create_environment():
    cwd = os.getcwd()
    loader = FileSystemLoader(searchpath=cwd)
    environment = Environment(loader=loader)
    environment.filters["commit_hash"] = commit_hash_filter
    environment.filters["commit_title"] = commit_title_filter
    environment.filters["lines"] = lines_filter
    environment.filters["multirun"] = multirun_filter
    environment.filters["run"] = run_filter
    environment.filters["shell"] = shell_filter
    environment.filters["store"] = store_filter
    environment.filters["gitception"] = gitception_filter
    return environment


def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate slides")
    parser.add_argument("--input", type=str)
    parser.add_argument("--output", type=str)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    env = create_environment()
    template = env.get_template(args.input)

    if os.path.exists(args.output):
        os.remove(args.output)

    with open(args.output, "w") as output:
        output.write(template.render())
