"""Skill installation logic."""

from pathlib import Path

from ..models import AgentConfig, InstallScope, Skill


class InstallError(Exception):
    """Installation error."""

    pass


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

    Creates a symlink to the skill in the agent's skills directory.

    Args:
        skill: The skill to install.
        agent: Target agent configuration.
        scope: Installation scope (local or global).
        project_dir: Project directory for local scope.

    Returns:
        Path to the installed skill (symlink location).

    Raises:
        InstallError: If installation fails (FailFast - no fallback).
    """
    install_path = get_install_path(skill, agent, scope, project_dir)

    # Create parent directory if needed
    install_path.parent.mkdir(parents=True, exist_ok=True)

    # Check if already installed
    if install_path.exists() or install_path.is_symlink():
        if install_path.is_symlink() and install_path.resolve() == skill.path:
            # Already correctly linked
            return install_path
        raise InstallError(
            f"Skill already exists at {install_path}. "
            "Remove it first or use a different name."
        )

    # Create symlink (FailFast - no fallback to copy)
    try:
        install_path.symlink_to(skill.path)
    except OSError as e:
        raise InstallError(f"Failed to create symlink: {e}") from e

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
        else:
            # If it's a directory (not a symlink), refuse to delete
            raise InstallError(
                f"Skill at {install_path} is not a symlink. "
                "Manual removal required for safety."
            )
    except OSError as e:
        raise InstallError(f"Failed to remove skill: {e}") from e

    return True
