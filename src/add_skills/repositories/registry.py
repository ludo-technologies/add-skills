"""Registry fetching from remote."""

import json
import urllib.request
from urllib.error import HTTPError, URLError

from add_skills.exceptions import RegistryFetchError, RegistryParseError
from add_skills.models import RegistryEntry

REGISTRY_URL = "https://raw.githubusercontent.com/ludo-technologies/add-skills/main/registry.json"
TIMEOUT_SECONDS = 10


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
    for i, entry in enumerate(entries):
        if not isinstance(entry, dict):
            raise RegistryParseError(
                f"Entry {i} must be an object, got {type(entry).__name__}"
            )

        missing = [key for key in ("name", "repo") if key not in entry]
        if missing:
            raise RegistryParseError(
                f"Entry {i} missing required fields: {', '.join(missing)}"
            )

        result.append(
            RegistryEntry(
                name=entry["name"],
                repo=entry["repo"],
                description=entry.get("description", ""),
                tags=entry.get("tags", []),
            )
        )

    return result
