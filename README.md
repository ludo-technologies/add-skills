# add-skills

A Python-based CLI for managing AI agent Skills. Install Skills from local paths or GitHub/GitLab repositories.

## Installation

No installation required (recommended)
```bash
uvx add-skills ludo-technologies/python-best-practices
```

Or install globally
```bash
uv tool install add-skills
pipx install add-skills
```

## Usage

```bash
# Add Skills from GitHub (short form)
uvx add-skills ludo-technologies/python-best-practices

# Add Skills from a local directory
uvx add-skills ./my-skills

# Add Skills from full GitHub URL
uvx add-skills https://github.com/owner/repo

# List available Skills without installing
uvx add-skills ludo-technologies/python-best-practices --list

# Install globally (default: local to project)
uvx add-skills ludo-technologies/python-best-practices --global

# Install for a specific agent
uvx add-skills ludo-technologies/python-best-practices --global --agent cursor

# Skip confirmation prompt
uvx add-skills ludo-technologies/python-best-practices --yes

# Install a specific Skill by name
uvx add-skills ludo-technologies/python-best-practices --skill coding-standards
```

## Options

| Option | Short | Description |
|--------|-------|-------------|
| `--global` | `-g` | Install globally instead of locally to project |
| `--agent` | `-a` | Target agent (default: `claude-code`) |
| `--skill` | `-s` | Install specific Skill by name |
| `--list` | `-l` | List available Skills without installing |
| `--yes` | `-y` | Skip confirmation prompt |

## Supported Agents

amp, antigravity, claude-code, clawdbot, cline, codebuddy, codex, command-code, continue, crush, cursor, droid, gemini-cli, github-copilot, goose, kilo, kiro-cli, mcpjam, mux, neovate, opencode, openhands, pi, qoder, qwen-code, roo, trae, windsurf, zencoder

## Creating Skills

Create a `SKILL.md` file in your Skill directory:

```markdown
---
name: my-skill
description: A brief description of what this skill does
---

# My Skill

Instructions for the AI agent...
```

## How It Works

1. Parses the source (local path, `owner/repo`, or full URL)
2. For remote sources, performs a shallow clone
3. Discovers all `SKILL.md` files in the source
4. Copies Skill files to the target agent's Skills directory

**Installation paths (example for claude-code):**
- Local: `.claude/skills/<skill-name>`
- Global: `~/.claude/skills/<skill-name>`

## License

MIT
