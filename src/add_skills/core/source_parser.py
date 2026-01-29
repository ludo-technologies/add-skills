"""Source URL/path parser."""

import re
from pathlib import Path

from add_skills.exceptions import SourceParseError
from add_skills.models import SkillSource, SourceType

# Patterns for GitHub URLs
GITHUB_PATTERNS = [
    # Full URL: https://github.com/owner/repo
    re.compile(
        r"^https?://github\.com/(?P<owner>[^/]+)/(?P<repo>[^/]+?)(?:\.git)?(?:/tree/(?P<branch>[^/]+)(?P<subpath>/.*)?)?$"
    ),
    # SSH: git@github.com:owner/repo.git
    re.compile(
        r"^git@github\.com:(?P<owner>[^/]+)/(?P<repo>[^/]+?)(?:\.git)?$"
    ),
    # Short form: owner/repo
    re.compile(
        r"^(?P<owner>[a-zA-Z0-9][-a-zA-Z0-9]*)/(?P<repo>[a-zA-Z0-9][-a-zA-Z0-9._]*)(?:#(?P<branch>.+))?$"
    ),
]

# Patterns for GitLab URLs
GITLAB_PATTERNS = [
    # Full URL: https://gitlab.com/owner/repo
    re.compile(
        r"^https?://gitlab\.com/(?P<owner>[^/]+)/(?P<repo>[^/]+?)(?:\.git)?(?:/-/tree/(?P<branch>[^/]+)(?P<subpath>/.*)?)?$"
    ),
    # SSH: git@gitlab.com:owner/repo.git
    re.compile(
        r"^git@gitlab\.com:(?P<owner>[^/]+)/(?P<repo>[^/]+?)(?:\.git)?$"
    ),
]


def parse_source(source: str) -> SkillSource:
    """Parse a source string into a SkillSource.

    Args:
        source: A path, URL, or short form (owner/repo).

    Returns:
        SkillSource with parsed information.

    Raises:
        SourceParseError: If source format is invalid.
    """
    source = source.strip()

    # Check if it's a local path
    path = Path(source).expanduser()
    if path.exists() or source.startswith((".", "/", "~")):
        if not path.exists():
            raise SourceParseError(f"Local path does not exist: {source}")
        return SkillSource(
            source_type=SourceType.LOCAL,
            path=path.resolve(),
            original=source,
        )

    # Try GitHub patterns
    for pattern in GITHUB_PATTERNS:
        match = pattern.match(source)
        if match:
            groups = match.groupdict()
            return SkillSource(
                source_type=SourceType.GITHUB,
                owner=groups["owner"],
                repo=groups["repo"],
                branch=groups.get("branch"),
                subpath=groups.get("subpath"),
                original=source,
            )

    # Try GitLab patterns
    for pattern in GITLAB_PATTERNS:
        match = pattern.match(source)
        if match:
            groups = match.groupdict()
            return SkillSource(
                source_type=SourceType.GITLAB,
                owner=groups["owner"],
                repo=groups["repo"],
                branch=groups.get("branch"),
                subpath=groups.get("subpath"),
                original=source,
            )

    raise SourceParseError(
        f"Invalid source format: {source}. "
        "Expected: local path, owner/repo, or full GitHub/GitLab URL."
    )
