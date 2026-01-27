"""Add command implementation."""

import shutil
import tempfile
from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from ..core import (
    AGENTS,
    clone_repo,
    discover_skills,
    get_agent,
    install_skill,
    parse_source,
)
from ..core.installer import InstallError
from ..models import InstallScope, SourceType

console = Console()


def add(
    source: str = typer.Argument(
        ...,
        help="Source to add skills from (local path, owner/repo, or URL)",
    ),
    global_install: bool = typer.Option(
        False,
        "--global",
        "-g",
        help="Install globally (default: local to project)",
    ),
    agent: str = typer.Option(
        "claude",
        "--agent",
        "-a",
        help=f"Target agent ({', '.join(AGENTS.keys())})",
    ),
    skill_name: str = typer.Option(
        None,
        "--skill",
        "-s",
        help="Install specific skill by name",
    ),
    list_only: bool = typer.Option(
        False,
        "--list",
        "-l",
        help="List available skills without installing",
    ),
    yes: bool = typer.Option(
        False,
        "--yes",
        "-y",
        help="Skip confirmation prompt",
    ),
) -> None:
    """Install skills from a source.

    Examples:
        add-skills ./my-skills
        add-skills vercel-labs/skills
        add-skills https://github.com/owner/repo
        add-skills owner/repo -g -a cursor
    """
    # Validate agent
    try:
        agent_config = get_agent(agent)
    except KeyError as e:
        console.print(f"[red]Error:[/red] {e}")
        raise typer.Exit(code=1)

    # Parse source
    try:
        skill_source = parse_source(source)
    except ValueError as e:
        console.print(f"[red]Error:[/red] {e}")
        raise typer.Exit(code=1)

    # Get skill directory
    skill_dir: Path
    temp_dir: Path | None = None

    try:
        if skill_source.source_type == SourceType.LOCAL:
            skill_dir = skill_source.path
        else:
            # Clone remote repository
            console.print(f"Cloning [cyan]{source}[/cyan]...")
            temp_dir = Path(tempfile.mkdtemp(prefix="add-skills-"))
            try:
                skill_dir = clone_repo(skill_source, temp_dir)
            except Exception as e:
                console.print(f"[red]Error cloning repository:[/red] {e}")
                raise typer.Exit(code=1)

        # Discover skills
        skills = discover_skills(skill_dir)

        if not skills:
            console.print(f"[yellow]No skills found in {source}[/yellow]")
            raise typer.Exit(code=0)

        # Filter by skill name if specified
        if skill_name:
            skills = [s for s in skills if s.name == skill_name]
            if not skills:
                console.print(f"[red]Skill not found:[/red] {skill_name}")
                raise typer.Exit(code=1)

        # Display skills
        _display_skills(skills)

        if list_only:
            raise typer.Exit(code=0)

        # Confirm installation
        scope = InstallScope.GLOBAL if global_install else InstallScope.LOCAL
        scope_label = "globally" if global_install else "locally"

        if not yes:
            console.print()
            confirm = typer.confirm(
                f"Install {len(skills)} skill(s) {scope_label} for {agent_config.name}?"
            )
            if not confirm:
                console.print("[yellow]Installation cancelled.[/yellow]")
                raise typer.Exit(code=0)

        # Install skills
        console.print()
        installed_count = 0
        for skill in skills:
            try:
                install_path = install_skill(skill, agent_config, scope)
                console.print(
                    f"[green]Installed:[/green] {skill.name} -> {install_path}"
                )
                installed_count += 1
            except InstallError as e:
                console.print(f"[red]Failed:[/red] {skill.name} - {e}")

        console.print()
        console.print(
            f"[green]Done![/green] Installed {installed_count}/{len(skills)} skill(s)."
        )

    finally:
        # Cleanup temp directory
        if temp_dir and temp_dir.exists():
            shutil.rmtree(temp_dir, ignore_errors=True)


def _display_skills(skills: list) -> None:
    """Display skills in a table."""
    table = Table(title="Available Skills")
    table.add_column("Name", style="cyan")
    table.add_column("Description")
    table.add_column("Globs", style="dim")

    for skill in skills:
        globs = ", ".join(skill.globs) if skill.globs else "-"
        table.add_row(skill.name, skill.description or "-", globs)

    console.print(table)
