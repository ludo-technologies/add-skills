"""Agent configurations for various AI tools."""

from pathlib import Path

from add_skills.models import AgentConfig

# Agent configurations matching vercel-labs/skills
AGENTS: dict[str, AgentConfig] = {
    "amp": AgentConfig(
        name="amp",
        display_name="Amp",
        project_skills_dir=".agents/skills",
        global_skills_dir=Path("~/.config/agents/skills"),
    ),
    "antigravity": AgentConfig(
        name="antigravity",
        display_name="Antigravity",
        project_skills_dir=".agent/skills",
        global_skills_dir=Path("~/.gemini/antigravity/global_skills"),
    ),
    "claude-code": AgentConfig(
        name="claude-code",
        display_name="Claude Code",
        project_skills_dir=".claude/skills",
        global_skills_dir=Path("~/.claude/skills"),
    ),
    "clawdbot": AgentConfig(
        name="clawdbot",
        display_name="Clawdbot",
        project_skills_dir="skills",
        global_skills_dir=Path("~/.clawdbot/skills"),
    ),
    "cline": AgentConfig(
        name="cline",
        display_name="Cline",
        project_skills_dir=".cline/skills",
        global_skills_dir=Path("~/.cline/skills"),
    ),
    "codebuddy": AgentConfig(
        name="codebuddy",
        display_name="CodeBuddy",
        project_skills_dir=".codebuddy/skills",
        global_skills_dir=Path("~/.codebuddy/skills"),
    ),
    "codex": AgentConfig(
        name="codex",
        display_name="Codex",
        project_skills_dir=".codex/skills",
        global_skills_dir=Path("~/.codex/skills"),
    ),
    "command-code": AgentConfig(
        name="command-code",
        display_name="Command Code",
        project_skills_dir=".commandcode/skills",
        global_skills_dir=Path("~/.commandcode/skills"),
    ),
    "continue": AgentConfig(
        name="continue",
        display_name="Continue",
        project_skills_dir=".continue/skills",
        global_skills_dir=Path("~/.continue/skills"),
    ),
    "crush": AgentConfig(
        name="crush",
        display_name="Crush",
        project_skills_dir=".crush/skills",
        global_skills_dir=Path("~/.config/crush/skills"),
    ),
    "cursor": AgentConfig(
        name="cursor",
        display_name="Cursor",
        project_skills_dir=".cursor/skills",
        global_skills_dir=Path("~/.cursor/skills"),
    ),
    "droid": AgentConfig(
        name="droid",
        display_name="Droid",
        project_skills_dir=".factory/skills",
        global_skills_dir=Path("~/.factory/skills"),
    ),
    "gemini-cli": AgentConfig(
        name="gemini-cli",
        display_name="Gemini CLI",
        project_skills_dir=".gemini/skills",
        global_skills_dir=Path("~/.gemini/skills"),
    ),
    "github-copilot": AgentConfig(
        name="github-copilot",
        display_name="GitHub Copilot",
        project_skills_dir=".github/skills",
        global_skills_dir=Path("~/.copilot/skills"),
    ),
    "goose": AgentConfig(
        name="goose",
        display_name="Goose",
        project_skills_dir=".goose/skills",
        global_skills_dir=Path("~/.config/goose/skills"),
    ),
    "kilo": AgentConfig(
        name="kilo",
        display_name="Kilo Code",
        project_skills_dir=".kilocode/skills",
        global_skills_dir=Path("~/.kilocode/skills"),
    ),
    "kiro-cli": AgentConfig(
        name="kiro-cli",
        display_name="Kiro CLI",
        project_skills_dir=".kiro/skills",
        global_skills_dir=Path("~/.kiro/skills"),
    ),
    "mcpjam": AgentConfig(
        name="mcpjam",
        display_name="MCPJam",
        project_skills_dir=".mcpjam/skills",
        global_skills_dir=Path("~/.mcpjam/skills"),
    ),
    "mux": AgentConfig(
        name="mux",
        display_name="Mux",
        project_skills_dir=".mux/skills",
        global_skills_dir=Path("~/.mux/skills"),
    ),
    "opencode": AgentConfig(
        name="opencode",
        display_name="OpenCode",
        project_skills_dir=".opencode/skills",
        global_skills_dir=Path("~/.config/opencode/skills"),
    ),
    "openhands": AgentConfig(
        name="openhands",
        display_name="OpenHands",
        project_skills_dir=".openhands/skills",
        global_skills_dir=Path("~/.openhands/skills"),
    ),
    "pi": AgentConfig(
        name="pi",
        display_name="Pi",
        project_skills_dir=".pi/skills",
        global_skills_dir=Path("~/.pi/agent/skills"),
    ),
    "qoder": AgentConfig(
        name="qoder",
        display_name="Qoder",
        project_skills_dir=".qoder/skills",
        global_skills_dir=Path("~/.qoder/skills"),
    ),
    "qwen-code": AgentConfig(
        name="qwen-code",
        display_name="Qwen Code",
        project_skills_dir=".qwen/skills",
        global_skills_dir=Path("~/.qwen/skills"),
    ),
    "roo": AgentConfig(
        name="roo",
        display_name="Roo Code",
        project_skills_dir=".roo/skills",
        global_skills_dir=Path("~/.roo/skills"),
    ),
    "trae": AgentConfig(
        name="trae",
        display_name="Trae",
        project_skills_dir=".trae/skills",
        global_skills_dir=Path("~/.trae/skills"),
    ),
    "windsurf": AgentConfig(
        name="windsurf",
        display_name="Windsurf",
        project_skills_dir=".windsurf/skills",
        global_skills_dir=Path("~/.codeium/windsurf/skills"),
    ),
    "zencoder": AgentConfig(
        name="zencoder",
        display_name="Zencoder",
        project_skills_dir=".zencoder/skills",
        global_skills_dir=Path("~/.zencoder/skills"),
    ),
    "neovate": AgentConfig(
        name="neovate",
        display_name="Neovate",
        project_skills_dir=".neovate/skills",
        global_skills_dir=Path("~/.neovate/skills"),
    ),
}

# Default agent
DEFAULT_AGENT = "claude-code"


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
