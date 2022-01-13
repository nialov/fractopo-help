"""
Nox test suite.
"""


from pathlib import Path

import nox

# DOCS_APIDOC_DIR_PATH = Path("docs_src/apidoc")
# DOCS_DIR_PATH = Path("docs")
# pipfile_lock = "Pipfile.lock"
NOTEBOOKS_NAME = (
    "network.ipynb",
    "network_no_topology.ipynb",
    "command_line_help.ipynb",
)
TASKS_NAME = "tasks.py"
NOXFILE_NAME = "noxfile.py"
REQUIREMENTS_TXT = "requirements.txt"


@nox.session(python="3.8")
def format(session):
    """
    Format python files, notebooks and docs_src.
    """
    session.install("black", "black-nb", "isort")
    # Format python files
    session.run("black", TASKS_NAME, NOXFILE_NAME)
    # Format python file imports
    session.run(
        "isort",
        TASKS_NAME,
        NOXFILE_NAME,
    )
    # Format notebooks
    session.run("black-nb", *NOTEBOOKS_NAME)


@nox.session(python="3.8")
def lint(session):
    """
    Lint python files, notebooks and docs_src.
    """
    session.install("rstcheck", "sphinx", "black", "black-nb", "isort", "pylama")

    # Lint python files with black (all should be formatted.)
    session.run("black", "--check", TASKS_NAME, NOXFILE_NAME)
    session.run(
        "isort",
        "--check-only",
        TASKS_NAME,
        NOXFILE_NAME,
    )
    # Lint notebooks with black-nb (all should be formatted.)
    session.run("black-nb", "--check", *NOTEBOOKS_NAME)


@nox.session(python="3.8")
def requirements(session):
    """
    Sync requirements from poetry to requirements.txt.
    """
    session.install("poetry")
    session.run(
        "poetry",
        "export",
        "--without-hashes",
        "-o",
        REQUIREMENTS_TXT,
    )


@nox.session(python="3.8")
def test(session: nox.Session):
    """
    Test installation of fractopo and notebook run.
    """
    session.install("-r", REQUIREMENTS_TXT)
    session.run("fractopo", "tracevalidate", "--help")
    session.run("fractopo", "network", "--help")
    for notebook in NOTEBOOKS_NAME:
        assert Path(notebook).exists()
        session.run("ipython", notebook)
        cmd = (
            "jupyter",
            "nbconvert",
            ("--clear-output" if "command_line_help" not in notebook else "--execute"),
            "--inplace",
            notebook,
        )
        session.run(*cmd)
