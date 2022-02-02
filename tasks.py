"""
Invoke tasks.
"""

from invoke import task


@task
def requirements(c):
    """
    Sync requirements from poetry to requirements.txt.
    """
    c.run("nox --session requirements")


@task(pre=[requirements])
def test(c):
    """
    Test notebook run and clean output afterwards.
    """
    c.run("nox --session test")


@task
def pre_commit(c):
    """
    Pre-commit check all files.
    """
    c.run("nox --session pre_commit")


@task(pre=[pre_commit, requirements, test])
def make(_):
    """
    Make all.
    """
