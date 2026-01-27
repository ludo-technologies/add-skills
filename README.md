# add-skills

A CLI tool for managing AI coding agent skills. Install skills from local paths or GitHub/GitLab repositories.

## Installation

```bash
# No installation required (recommended)
uvx add-skills vercel-labs/skills

# Or install globally
uv pip install add-skills
pip install add-skills
```

## Usage

```bash
# Add skills from GitHub (short form)
uvx add-skills vercel-labs/skills

# Add skills from a local directory
uvx add-skills ./my-skills

# Add skills from full GitHub URL
uvx add-skills https://github.com/owner/repo

# List available skills without installing
uvx add-skills vercel-labs/skills --list

# Install globally (default: local to project)
uvx add-skills vercel-labs/skills --global

# Install for a specific agent
uvx add-skills vercel-labs/skills --global --agent cursor

# Skip confirmation prompt
uvx add-skills vercel-labs/skills --yes

# Install a specific skill by name
uvx add-skills vercel-labs/skills --skill find-skills
```

## Options

| Option | Short | Description |
|--------|-------|-------------|
| `--global` | `-g` | Install globally instead of locally to project |
| `--agent` | `-a` | Target agent (default: `claude-code`) |
| `--skill` | `-s` | Install specific skill by name |
| `--list` | `-l` | List available skills without installing |
| `--yes` | `-y` | Skip confirmation prompt |

## Supported Agents

amp, antigravity, claude-code, clawdbot, cline, codebuddy, codex, command-code, continue, crush, cursor, droid, gemini-cli, github-copilot, goose, kilo, kiro-cli, mcpjam, mux, neovate, opencode, openhands, pi, qoder, qwen-code, roo, trae, windsurf, zencoder

## Creating Skills

Create a `SKILL.md` file in your skill directory:

```markdown
---
name: my-skill
description: A brief description of what this skill does
globs:
  - "**/*.ts"
  - "**/*.tsx"
---

# My Skill

Instructions for the AI agent...
```

## How It Works

1. Parses the source (local path, `owner/repo`, or full URL)
2. For remote sources, performs a shallow clone
3. Discovers all `SKILL.md` files in the source
4. Creates symlinks in the target agent's skills directory

**Installation paths (example for claude-code):**
- Local: `.claude/skills/<skill-name>`
- Global: `~/.claude/skills/<skill-name>`

## License

MIT
