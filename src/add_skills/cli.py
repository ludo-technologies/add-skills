"""CLI application for add-skills."""

import sys

import typer
from rich.console import Console

from add_skills.commands import add_skills, find


def _create_console() -> Console:
    """Factory for creating Console instance. Override in tests."""
    return Console()


# Separate app for the "find" subcommand
find_app = typer.Typer(add_completion=False)


@find_app.callback(invoke_without_command=True)
def find_callback(
    ctx: typer.Context,
    keyword: str | None = typer.Argument(None),
) -> None:
    """Search for Skills in the curated registry."""
    ctx.obj = _create_console()
    find(ctx, keyword)


# Main app for adding skills
main_app = typer.Typer(add_completion=False)


@main_app.command(
    help="Install Skills from a source.\n\n"
    "Examples:\n"
    "  add-skills vercel-labs/skills\n"
    "  add-skills ./my-skills --list\n"
    "  add-skills owner/repo -g -a cursor",
)
def add_command(
    ctx: typer.Context,
    source: str = typer.Argument(..., help="Source (local path, owner/repo, or URL)"),
    global_install: bool = typer.Option(False, "--global", "-g", help="Install globally"),
    agent: str = typer.Option("claude-code", "--agent", "-a", help="Target agent"),
    skill_name: str | None = typer.Option(None, "--skill", "-s", help="Install specific skill"),
    list_only: bool = typer.Option(False, "--list", "-l", help="List without installing"),
    yes: bool = typer.Option(False, "--yes", "-y", help="Skip confirmation"),
) -> None:
    ctx.obj = _create_console()
    add_skills(ctx, source, global_install, agent, skill_name, list_only, yes)


# Subcommand registry - add new commands here
SUBCOMMANDS: dict[str, typer.Typer] = {
    "find": find_app,
}


def run() -> None:
    """Run the CLI application."""
    args = sys.argv[1:]

    # Check for subcommands
    if args and args[0] in SUBCOMMANDS:
        SUBCOMMANDS[args[0]](args[1:], standalone_mode=True)
        return

    # Default: add skills (typer handles --help and no-args)
    main_app()
