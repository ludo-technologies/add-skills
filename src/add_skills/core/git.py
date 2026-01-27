"""Git operations for cloning repositories."""

import tempfile
from pathlib import Path

from git import Repo

from ..models import SkillSource


def clone_repo(source: SkillSource, target_dir: Path | None = None) -> Path:
    """Clone a repository.

    Args:
        source: The skill source to clone.
        target_dir: Optional target directory. If None, uses a temp directory.

    Returns:
        Path to the cloned repository.

    Raises:
        ValueError: If source is not a remote repository.
        git.GitCommandError: If clone fails.
    """
    if source.clone_url is None:
        raise ValueError("Cannot clone a local source")

    if target_dir is None:
        target_dir = Path(tempfile.mkdtemp(prefix="add-skills-"))

    # Shallow clone for faster download
    clone_kwargs = {
        "depth": 1,
        "single_branch": True,
    }

    if source.branch:
        clone_kwargs["branch"] = source.branch

    Repo.clone_from(source.clone_url, target_dir, **clone_kwargs)

    # If there's a subpath, return that directory
    if source.subpath:
        subpath = target_dir / source.subpath.lstrip("/")
        if not subpath.exists():
            raise ValueError(f"Subpath not found in repository: {source.subpath}")
        return subpath

    return target_dir
