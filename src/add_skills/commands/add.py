"""Add command implementation."""

import shutil
import tempfile
from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from add_skills.cli_utils import exit_with_error
from add_skills.core import get_agent
from add_skills.core.source_parser import parse_source
from add_skills.exceptions import InstallError, SourceParseError
from add_skills.models import InstallScope, SourceType
from add_skills.repositories import clone_repo, discover_skills
from add_skills.services import install_skill


def add_skills(
    ctx: typer.Context,
    source: str,
    global_install: bool = False,
    agent: str = "claude-code",
    skill_name: str | None = None,
    list_only: bool = False,
    yes: bool = False,
) -> None:
    """Install Skills from a source."""
    console: Console = ctx.obj

    # Validate agent
    try:
        agent_config = get_agent(agent)
    except KeyError as e:
        exit_with_error(console, str(e))

    # Parse source
    try:
        skill_source = parse_source(source)
    except SourceParseError as e:
        exit_with_error(console, str(e))

    # Get skill directory
    skill_dir: Path
    temp_dir: Path | None = None

    try:
        if skill_source.source_type == SourceType.LOCAL:
            if skill_source.path is None:
                exit_with_error(console, "Local source path is None")
            skill_dir = skill_source.path
        else:
            # Clone remote repository
            console.print(f"Cloning [cyan]{source}[/cyan]...")
            temp_dir = Path(tempfile.mkdtemp(prefix="add-skills-"))
            try:
                skill_dir = clone_repo(skill_source, temp_dir)
            except Exception as e:
                exit_with_error(console, f"cloning repository: {e}")

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
        _display_skills(console, skills)

        if list_only:
            raise typer.Exit(code=0)

        # Confirm installation
        scope = InstallScope.GLOBAL if global_install else InstallScope.LOCAL
        scope_label = "globally" if global_install else "locally"

        if not yes:
            console.print()
            confirm = typer.confirm(
                f"Install {len(skills)} skill(s) {scope_label} for {agent_config.display_name}?"
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


def _display_skills(console: Console, skills: list) -> None:
    """Display skills in a table."""
    table = Table(title="Available Skills")
    table.add_column("Name", style="cyan")
    table.add_column("Description")
    table.add_column("Globs", style="dim")

    for skill in skills:
        globs = ", ".join(skill.globs) if skill.globs else "-"
        table.add_row(skill.name, skill.description or "-", globs)

    console.print(table)
