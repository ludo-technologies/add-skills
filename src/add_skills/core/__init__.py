"""Core functionality for add-skills."""

from .agents import AGENTS, get_agent, get_all_agents
from .git import clone_repo
from .installer import install_skill
from .skills import discover_skills, parse_skill
from .source_parser import parse_source

__all__ = [
    "AGENTS",
    "clone_repo",
    "discover_skills",
    "get_agent",
    "get_all_agents",
    "install_skill",
    "parse_skill",
    "parse_source",
]
