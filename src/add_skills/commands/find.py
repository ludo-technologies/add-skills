"""Find command for searching skills in the registry."""

from typing import NoReturn

import typer
from rich.console import Console
from rich.table import Table

from add_skills.exceptions import RegistryFetchError, RegistryParseError
from add_skills.repositories import fetch_registry
from add_skills.services import search_registry


def _exit_with_error(console: Console, message: str) -> NoReturn:
    """Print error message and exit with code 1."""
    console.print(f"[red]Error:[/red] {message}")
    raise typer.Exit(code=1)


def find(
    ctx: typer.Context,
    keyword: str | None = typer.Argument(
        None,
        help="Keyword to search for in skill names, descriptions, and tags.",
    ),
) -> None:
    """Search for skills in the curated registry.

    If no keyword is provided, lists all available skills.
    """
    console: Console = ctx.obj

    try:
        entries = fetch_registry()
    except RegistryFetchError as e:
        _exit_with_error(console, f"fetching registry: {e}")
    except RegistryParseError as e:
        _exit_with_error(console, f"parsing registry: {e}")

    results = search_registry(entries, keyword)

    if not results:
        if keyword:
            console.print(f"No skills found matching '{keyword}'.")
        else:
            console.print("No skills found in registry.")
        return

    table = Table(title="Available Skills" if not keyword else f"Skills matching '{keyword}'")
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Repository", style="green")
    table.add_column("Description")

    for entry in results:
        table.add_row(entry.name, entry.repo, entry.description)

    console.print(table)
