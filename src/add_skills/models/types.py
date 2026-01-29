"""Type definitions for add-skills."""

from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any


class SourceType(Enum):
    """Type of skill source."""

    LOCAL = "local"
    GITHUB = "github"
    GITLAB = "gitlab"


class InstallScope(Enum):
    """Installation scope."""

    LOCAL = "local"
    GLOBAL = "global"


@dataclass
class AgentConfig:
    """Configuration for an AI agent."""

    name: str
    display_name: str
    project_skills_dir: str  # Relative path for project-local installs
    global_skills_dir: Path  # Absolute path for global installs

    @property
    def global_skills_path(self) -> Path:
        """Return the expanded global skills directory path."""
        return self.global_skills_dir.expanduser()


@dataclass
class SkillSource:
    """Parsed source information."""

    source_type: SourceType
    path: Path | None = None
    owner: str | None = None
    repo: str | None = None
    branch: str | None = None
    subpath: str | None = None
    original: str = ""

    @property
    def clone_url(self) -> str | None:
        """Return the clone URL for remote sources."""
        if self.source_type == SourceType.GITHUB:
            return f"https://github.com/{self.owner}/{self.repo}.git"
        elif self.source_type == SourceType.GITLAB:
            return f"https://gitlab.com/{self.owner}/{self.repo}.git"
        return None


@dataclass
class Skill:
    """A skill definition."""

    name: str
    path: Path
    description: str = ""
    globs: list[str] = field(default_factory=list)
    agents: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def skill_file(self) -> Path:
        """Return the path to SKILL.md."""
        return self.path / "SKILL.md"


@dataclass
class RegistryEntry:
    """A skill entry in the curated registry."""

    name: str
    repo: str
    description: str
    tags: list[str] = field(default_factory=list)

    def matches(self, keyword: str) -> bool:
        """Check if this entry matches a search keyword."""
        keyword_lower = keyword.lower()
        return (
            keyword_lower in self.name.lower()
            or keyword_lower in self.description.lower()
            or any(keyword_lower in tag.lower() for tag in self.tags)
        )
