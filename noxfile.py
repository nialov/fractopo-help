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


@nox.session(python="3.8", reuse_venv=True)
def pre_commit(session):
    """
    Format python files and notebooks.
    """
    session.install("pre-commit")
    # Format python files
    session.run("pre-commit", "run", "--all-files")


@nox.session(python="3.8", reuse_venv=True)
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


@nox.session(python="3.8", reuse_venv=True)
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
