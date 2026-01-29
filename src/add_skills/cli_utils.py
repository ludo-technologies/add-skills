"""CLI utility functions."""

from typing import NoReturn

import typer
from rich.console import Console


def exit_with_error(console: Console, message: str) -> NoReturn:
    """Print error message and exit with code 1."""
    console.print(f"[red]Error:[/red] {message}")
    raise typer.Exit(code=1)
