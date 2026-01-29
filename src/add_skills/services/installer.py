"""Skill installation logic."""

import shutil
from pathlib import Path

from ..exceptions import InstallError
from ..models import AgentConfig, InstallScope, Skill


def get_install_path(
    skill: Skill,
    agent: AgentConfig,
    scope: InstallScope,
    project_dir: Path | None = None,
) -> Path:
    """Get the installation path for a skill.

    Args:
        skill: The skill to install.
        agent: Target agent configuration.
        scope: Installation scope (local or global).
        project_dir: Project directory for local scope.

    Returns:
        Path where the skill should be installed.

    Raises:
        ValueError: If project_dir is required but not provided.
    """
    if scope == InstallScope.LOCAL:
        if project_dir is None:
            project_dir = Path.cwd()
        base_dir = project_dir / agent.project_skills_dir
    else:
        base_dir = agent.global_skills_path

    return base_dir / skill.name


def install_skill(
    skill: Skill,
    agent: AgentConfig,
    scope: InstallScope,
    project_dir: Path | None = None,
) -> Path:
    """Install a skill for an agent.

    Copies the skill directory to the agent's skills directory.

    Args:
        skill: The skill to install.
        agent: Target agent configuration.
        scope: Installation scope (local or global).
        project_dir: Project directory for local scope.

    Returns:
        Path to the installed skill.

    Raises:
        InstallError: If installation fails.
    """
    install_path = get_install_path(skill, agent, scope, project_dir)

    # Create parent directory if needed
    install_path.parent.mkdir(parents=True, exist_ok=True)

    # Check if already installed
    if install_path.exists() or install_path.is_symlink():
        raise InstallError(
            f"Skill already exists at {install_path}. "
            "Remove it first or use a different name."
        )

    # Copy skill directory
    try:
        if skill.path.is_dir():
            shutil.copytree(skill.path, install_path)
        else:
            shutil.copy2(skill.path, install_path)
    except OSError as e:
        raise InstallError(f"Failed to copy skill: {e}") from e

    return install_path


def uninstall_skill(
    skill_name: str,
    agent: AgentConfig,
    scope: InstallScope,
    project_dir: Path | None = None,
) -> bool:
    """Uninstall a skill.

    Args:
        skill_name: Name of the skill to uninstall.
        agent: Target agent configuration.
        scope: Installation scope.
        project_dir: Project directory for local scope.

    Returns:
        True if uninstalled, False if not found.

    Raises:
        InstallError: If uninstallation fails.
    """
    if scope == InstallScope.LOCAL:
        if project_dir is None:
            project_dir = Path.cwd()
        install_path = project_dir / agent.project_skills_dir / skill_name
    else:
        install_path = agent.global_skills_path / skill_name

    if not install_path.exists() and not install_path.is_symlink():
        return False

    try:
        if install_path.is_symlink():
            install_path.unlink()
        elif install_path.is_dir():
            shutil.rmtree(install_path)
        else:
            install_path.unlink()
    except OSError as e:
        raise InstallError(f"Failed to remove skill: {e}") from e

    return True
