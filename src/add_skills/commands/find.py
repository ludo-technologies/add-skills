"""Find command for searching skills in the registry."""

from typing import Optional

import typer
from rich.console import Console
from rich.table import Table

from ..core import RegistryFetchError, RegistryParseError, fetch_registry, search_registry


def find(
    keyword: Optional[str] = typer.Argument(
        None,
        help="Keyword to search for in skill names, descriptions, and tags.",
    ),
) -> None:
    """Search for skills in the curated registry.

    If no keyword is provided, lists all available skills.
    """
    console = Console()

    try:
        entries = fetch_registry()
    except RegistryFetchError as e:
        console.print(f"[red]Error fetching registry:[/red] {e}")
        raise typer.Exit(1)
    except RegistryParseError as e:
        console.print(f"[red]Error parsing registry:[/red] {e}")
        raise typer.Exit(1)

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
