"""Registry fetching and searching functionality."""

import json
import urllib.request
from urllib.error import HTTPError, URLError

from ..models import RegistryEntry

REGISTRY_URL = "https://raw.githubusercontent.com/ludo-technologies/add-skills/main/registry.json"
TIMEOUT_SECONDS = 10


class RegistryFetchError(Exception):
    """Failed to fetch registry from remote."""

    pass


class RegistryParseError(Exception):
    """Failed to parse registry JSON."""

    pass


def fetch_registry(url: str = REGISTRY_URL) -> list[RegistryEntry]:
    """Fetch the skill registry from the remote URL.

    Args:
        url: The URL to fetch the registry from.

    Returns:
        A list of RegistryEntry objects.

    Raises:
        RegistryFetchError: If the registry cannot be fetched.
        RegistryParseError: If the registry JSON is invalid.
    """
    try:
        with urllib.request.urlopen(url, timeout=TIMEOUT_SECONDS) as response:
            data = response.read().decode("utf-8")
    except HTTPError as e:
        raise RegistryFetchError(f"HTTP error {e.code}: {e.reason}") from e
    except URLError as e:
        raise RegistryFetchError(f"Failed to connect: {e.reason}") from e
    except TimeoutError as e:
        raise RegistryFetchError("Request timed out") from e

    try:
        entries = json.loads(data)
    except json.JSONDecodeError as e:
        raise RegistryParseError(f"Invalid JSON: {e}") from e

    if not isinstance(entries, list):
        raise RegistryParseError("Registry must be a JSON array")

    result = []
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        try:
            result.append(
                RegistryEntry(
                    name=entry["name"],
                    repo=entry["repo"],
                    description=entry.get("description", ""),
                    tags=entry.get("tags", []),
                )
            )
        except KeyError:
            continue

    return result


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
