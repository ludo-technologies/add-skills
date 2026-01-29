"""CLI application for add-skills."""

import typer

from .commands import add, find

app = typer.Typer(name="add-skills", no_args_is_help=True)
app.command()(add)
app.command()(find)


def run() -> None:
    """Run the CLI application."""
    app()
