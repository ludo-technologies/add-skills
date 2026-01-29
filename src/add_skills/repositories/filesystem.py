"""Filesystem operations for skill discovery."""

from pathlib import Path

import frontmatter

from ..models import Skill

SKILL_FILENAME = "SKILL.md"


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
        post = frontmatter.load(skill_file)
    except Exception:
        return None

    # Extract metadata from frontmatter
    name = post.get("name", skill_dir.name)
    description = post.get("description", "")
    globs = post.get("globs", [])
    agents = post.get("agents", [])

    # Ensure globs is a list
    if isinstance(globs, str):
        globs = [globs]

    # Ensure agents is a list
    if isinstance(agents, str):
        agents = [agents]

    return Skill(
        name=name,
        path=skill_dir.resolve(),
        description=description,
        globs=globs,
        agents=agents,
        metadata=dict(post.metadata),
    )
