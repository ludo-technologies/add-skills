"""Core functionality for add-skills.

This module re-exports from repositories and services for backward compatibility.
"""

from ..repositories import clone_repo, discover_skills, fetch_registry, parse_skill
from ..services import install_skill, search_registry
from .agents import AGENTS, get_agent, get_all_agents
from .source_parser import parse_source

__all__ = [
    "AGENTS",
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
