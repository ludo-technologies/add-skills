"""CLI application for add-skills."""

import typer

from .commands import add

app = typer.Typer(
    name="add-skills",
    help="Manage Claude Code skills",
    no_args_is_help=True,
)


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context) -> None:
    """Manage Claude Code skills."""
    pass


# Register commands
app.command(name="add")(add)


def run() -> None:
    """Run the CLI application."""
    app()
