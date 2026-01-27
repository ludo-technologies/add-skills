"""CLI application for add-skills."""

import typer

from .commands.add import add


def run() -> None:
    """Run the CLI application."""
    typer.run(add)
