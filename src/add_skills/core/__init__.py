"""Core functionality for add-skills."""

from .agents import AGENTS, get_agent, get_all_agents
from .git import clone_repo
from .installer import install_skill
from .registry import (
    RegistryFetchError,
    RegistryParseError,
    fetch_registry,
    search_registry,
)
from .skills import discover_skills, parse_skill
from .source_parser import parse_source

__all__ = [
    "AGENTS",
    "RegistryFetchError",
    "RegistryParseError",
    "clone_repo",
    "discover_skills",
    "fetch_registry",
    "get_agent",
    "get_all_agents",
    "install_skill",
    "parse_skill",
    "parse_source",
    "search_registry",
]
