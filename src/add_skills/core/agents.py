"""Agent configurations for various AI tools."""

from pathlib import Path

from ..models import AgentConfig

# Agent configurations for supported tools
AGENTS: dict[str, AgentConfig] = {
    # Claude Code
    "claude": AgentConfig(
        name="claude",
        skills_dir=Path("~/.claude/skills"),
        description="Claude Code (Anthropic)",
    ),
    # Cursor
    "cursor": AgentConfig(
        name="cursor",
        skills_dir=Path("~/.cursor/skills"),
        description="Cursor Editor",
    ),
    # Windsurf
    "windsurf": AgentConfig(
        name="windsurf",
        skills_dir=Path("~/.windsurf/skills"),
        description="Windsurf Editor",
    ),
    # Cline
    "cline": AgentConfig(
        name="cline",
        skills_dir=Path("~/.cline/skills"),
        description="Cline (VS Code Extension)",
    ),
    # Roo Code
    "roo": AgentConfig(
        name="roo",
        skills_dir=Path("~/.roo/skills"),
        description="Roo Code",
    ),
    # Continue
    "continue": AgentConfig(
        name="continue",
        skills_dir=Path("~/.continue/skills"),
        description="Continue (VS Code/JetBrains)",
    ),
    # Aider
    "aider": AgentConfig(
        name="aider",
        skills_dir=Path("~/.aider/skills"),
        description="Aider",
    ),
    # GitHub Copilot
    "copilot": AgentConfig(
        name="copilot",
        skills_dir=Path("~/.copilot/skills"),
        description="GitHub Copilot",
    ),
    # Amazon Q Developer
    "amazon-q": AgentConfig(
        name="amazon-q",
        skills_dir=Path("~/.amazon-q/skills"),
        description="Amazon Q Developer",
    ),
    # Tabnine
    "tabnine": AgentConfig(
        name="tabnine",
        skills_dir=Path("~/.tabnine/skills"),
        description="Tabnine",
    ),
    # Sourcegraph Cody
    "cody": AgentConfig(
        name="cody",
        skills_dir=Path("~/.cody/skills"),
        description="Sourcegraph Cody",
    ),
    # Replit
    "replit": AgentConfig(
        name="replit",
        skills_dir=Path("~/.replit/skills"),
        description="Replit AI",
    ),
    # JetBrains AI
    "jetbrains": AgentConfig(
        name="jetbrains",
        skills_dir=Path("~/.jetbrains/skills"),
        description="JetBrains AI Assistant",
    ),
    # Codium
    "codium": AgentConfig(
        name="codium",
        skills_dir=Path("~/.codium/skills"),
        description="Codium AI",
    ),
    # Supermaven
    "supermaven": AgentConfig(
        name="supermaven",
        skills_dir=Path("~/.supermaven/skills"),
        description="Supermaven",
    ),
    # Codeium
    "codeium": AgentConfig(
        name="codeium",
        skills_dir=Path("~/.codeium/skills"),
        description="Codeium",
    ),
    # Devin
    "devin": AgentConfig(
        name="devin",
        skills_dir=Path("~/.devin/skills"),
        description="Devin (Cognition)",
    ),
    # OpenHands
    "openhands": AgentConfig(
        name="openhands",
        skills_dir=Path("~/.openhands/skills"),
        description="OpenHands",
    ),
    # SWE-agent
    "swe-agent": AgentConfig(
        name="swe-agent",
        skills_dir=Path("~/.swe-agent/skills"),
        description="SWE-agent",
    ),
    # AutoGPT
    "autogpt": AgentConfig(
        name="autogpt",
        skills_dir=Path("~/.autogpt/skills"),
        description="AutoGPT",
    ),
    # GPT Engineer
    "gpt-engineer": AgentConfig(
        name="gpt-engineer",
        skills_dir=Path("~/.gpt-engineer/skills"),
        description="GPT Engineer",
    ),
    # Mentat
    "mentat": AgentConfig(
        name="mentat",
        skills_dir=Path("~/.mentat/skills"),
        description="Mentat",
    ),
    # Sweep
    "sweep": AgentConfig(
        name="sweep",
        skills_dir=Path("~/.sweep/skills"),
        description="Sweep AI",
    ),
    # Codegen
    "codegen": AgentConfig(
        name="codegen",
        skills_dir=Path("~/.codegen/skills"),
        description="Codegen",
    ),
    # Aide
    "aide": AgentConfig(
        name="aide",
        skills_dir=Path("~/.aide/skills"),
        description="Aide",
    ),
    # Pear
    "pear": AgentConfig(
        name="pear",
        skills_dir=Path("~/.pear/skills"),
        description="PearAI",
    ),
    # Void
    "void": AgentConfig(
        name="void",
        skills_dir=Path("~/.void/skills"),
        description="Void Editor",
    ),
    # Zed
    "zed": AgentConfig(
        name="zed",
        skills_dir=Path("~/.zed/skills"),
        description="Zed Editor AI",
    ),
    # Qodo
    "qodo": AgentConfig(
        name="qodo",
        skills_dir=Path("~/.qodo/skills"),
        description="Qodo (formerly Codium)",
    ),
    # Trae
    "trae": AgentConfig(
        name="trae",
        skills_dir=Path("~/.trae/skills"),
        description="Trae AI",
    ),
    # Kilo Code
    "kilo": AgentConfig(
        name="kilo",
        skills_dir=Path("~/.kilo/skills"),
        description="Kilo Code",
    ),
    # Augment
    "augment": AgentConfig(
        name="augment",
        skills_dir=Path("~/.augment/skills"),
        description="Augment Code",
    ),
}

# Default agent
DEFAULT_AGENT = "claude"


def get_agent(name: str) -> AgentConfig:
    """Get agent configuration by name.

    Args:
        name: Agent name.

    Returns:
        AgentConfig for the specified agent.

    Raises:
        KeyError: If agent not found.
    """
    if name not in AGENTS:
        raise KeyError(f"Unknown agent: {name}. Available: {', '.join(AGENTS.keys())}")
    return AGENTS[name]


def get_all_agents() -> list[AgentConfig]:
    """Get all agent configurations.

    Returns:
        List of all AgentConfig objects.
    """
    return list(AGENTS.values())
