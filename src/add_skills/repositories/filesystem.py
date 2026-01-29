"""Filesystem operations for skill discovery."""

from pathlib import Path
from typing import Any

import frontmatter
import yaml

from add_skills.models import Skill

SKILL_FILENAME = "SKILL.md"


def _parse_string(value: Any, default: str = "") -> str:
    """Parse a value as string."""
    if value is None:
        return default
    return str(value)


def _parse_string_list(value: Any) -> list[str]:
    """Parse a value as list of strings."""
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [str(item) for item in value]
    return []


def discover_skills(directory: Path) -> list[Skill]:
    """Discover all skills in a directory.

    Args:
        directory: Directory to search for skills.

    Returns:
        List of discovered Skill objects.
    """
    skills = []
    directory = Path(directory).resolve()

    # Find all SKILL.md files
    for skill_file in directory.rglob(SKILL_FILENAME):
        skill = parse_skill(skill_file.parent)
        if skill:
            skills.append(skill)

    return sorted(skills, key=lambda s: s.name)


def parse_skill(skill_dir: Path) -> Skill | None:
    """Parse a skill from its directory.

    Args:
        skill_dir: Directory containing SKILL.md.

    Returns:
        Skill object or None if invalid.
    """
    skill_file = skill_dir / SKILL_FILENAME

    if not skill_file.exists():
        return None

    try:
        with open(skill_file, encoding="utf-8") as f:
            post = frontmatter.load(f)
    except (OSError, yaml.YAMLError):
        return None

    return Skill(
        name=_parse_string(post.get("name"), skill_dir.name),
        path=skill_dir.resolve(),
        description=_parse_string(post.get("description")),
        globs=_parse_string_list(post.get("globs")),
        agents=_parse_string_list(post.get("agents")),
        metadata=dict(post.metadata),
    )
