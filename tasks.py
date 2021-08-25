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
def format(c):
    """
    Format everything.
    """
    c.run("nox --session format")


@task(pre=[format])
def lint(c):
    """
    Lint everything.
    """
    c.run("nox --session lint")


@task(pre=[format, lint, test])
def make(_):
    """
    Make all.
    """
