"""
Nox test suite.
"""

from pathlib import Path

import nox

docs_apidoc_dir_path = Path("docs_src/apidoc")
docs_dir_path = Path("docs")
pipfile_lock = "Pipfile.lock"
notebooks_name = "network.ipynb"
tasks_name = "tasks.py"
noxfile_name = "noxfile.py"


@nox.session(python="3.8")
def format(session):
    """
    Format python files, notebooks and docs_src.
    """
    session.install("black", "black-nb", "isort")
    # Format python files
    session.run("black", tasks_name, noxfile_name)
    # Format python file imports
    session.run(
        "isort",
        tasks_name,
        noxfile_name,
    )
    # Format notebooks
    session.run("black-nb", notebooks_name)


@nox.session(python="3.8")
def lint(session):
    """
    Lint python files, notebooks and docs_src.
    """
    session.install("rstcheck", "sphinx", "black", "black-nb", "isort", "pylama")

    # Lint python files with black (all should be formatted.)
    session.run("black", "--check", tasks_name, noxfile_name)
    session.run(
        "isort",
        "--check-only",
        tasks_name,
        noxfile_name,
    )
    # Lint notebooks with black-nb (all should be formatted.)
    session.run("black-nb", "--check", notebooks_name)
