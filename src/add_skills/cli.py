"""CLI application for add-skills."""

import sys
from typing import Optional

import typer
from rich.console import Console

from add_skills.commands import add_skills, find
from add_skills.core import AGENTS

# Separate app for the "find" subcommand
find_app = typer.Typer()


@find_app.command()
def find_command(
    ctx: typer.Context,
    keyword: Optional[str] = typer.Argument(None),
) -> None:
    """Search for Skills in the curated registry."""
    ctx.obj = Console()
    find(ctx, keyword)


# Main app for adding skills
main_app = typer.Typer()


@main_app.command()
def add_command(
    ctx: typer.Context,
    source: str = typer.Argument(..., help="Source (local path, owner/repo, or URL)"),
    global_install: bool = typer.Option(False, "--global", "-g", help="Install globally"),
    agent: str = typer.Option("claude-code", "--agent", "-a", help="Target agent"),
    skill_name: Optional[str] = typer.Option(None, "--skill", "-s", help="Install specific skill"),
    list_only: bool = typer.Option(False, "--list", "-l", help="List without installing"),
    yes: bool = typer.Option(False, "--yes", "-y", help="Skip confirmation"),
) -> None:
    """Install Skills from a source."""
    ctx.obj = Console()
    add_skills(ctx, source, global_install, agent, skill_name, list_only, yes)


def _show_help() -> None:
    """Show help message."""
    console = Console()
    agents_str = ", ".join(list(AGENTS.keys())[:5]) + ", ..."
    console.print(
        "[bold]Usage:[/bold] add-skills [OPTIONS] SOURCE\n"
        "       add-skills find [KEYWORD]\n\n"
        "A tool for managing AI agent Skills.\n\n"
        "[bold]Examples:[/bold]\n"
        "  add-skills vercel-labs/skills\n"
        "  add-skills ./my-skills --list\n"
        "  add-skills owner/repo -g -a cursor\n"
        "  add-skills find python\n\n"
        "[bold]Options:[/bold]\n"
        "  -g, --global    Install globally\n"
        "  -a, --agent     Target agent (" + agents_str + ")\n"
        "  -s, --skill     Install specific skill by name\n"
        "  -l, --list      List available Skills without installing\n"
        "  -y, --yes       Skip confirmation prompt\n"
        "  --help          Show this message"
    )


def run() -> None:
    """Run the CLI application."""
    args = sys.argv[1:]

    # No args -> show help
    if not args:
        _show_help()
        return

    # Help flag
    if args[0] in ("--help", "-h"):
        _show_help()
        return

    # "find" subcommand
    if args[0] == "find":
        sys.argv = [sys.argv[0]] + args[1:]  # Remove "find" from args
        find_app()
        return

    # Default: add skills
    main_app()
