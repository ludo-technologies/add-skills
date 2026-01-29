"""CLI application for add-skills."""

import typer
from rich.console import Console

from add_skills.commands import add, find

app = typer.Typer(name="add-skills", no_args_is_help=True)


@app.callback()
def main(ctx: typer.Context) -> None:
    """A tool for managing AI agent Skills."""
    ctx.obj = Console()


app.command()(add)
app.command()(find)


def run() -> None:
    """Run the CLI application."""
    app()
