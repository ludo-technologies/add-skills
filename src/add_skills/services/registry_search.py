"""Registry search service."""

from add_skills.models import RegistryEntry


def search_registry(
    entries: list[RegistryEntry], keyword: str | None = None
) -> list[RegistryEntry]:
    """Search the registry for entries matching a keyword.

    Args:
        entries: List of registry entries to search.
        keyword: Optional keyword to filter by. If None, returns all entries.

    Returns:
        A list of matching RegistryEntry objects.
    """
    if keyword is None:
        return entries

    return [entry for entry in entries if entry.matches(keyword)]
