# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.0.4] - 2026-01-28

### Changed

- Copy skills instead of creating symlinks for better compatibility

### Fixed

- Use SPDX license expression in pyproject.toml

## [0.0.3] - 2025-01-28

### Added

- Initial release
- CLI tool for managing AI coding agent skills
- Support for installing skills from local paths or GitHub/GitLab repositories
- `--global` option for system-wide installation
- `--agent` option to target specific AI agents
- `--skill` option to install specific skills by name
- `--list` option to preview available skills
- `--yes` option to skip confirmation prompts
- Support for 30+ AI coding agents

[Unreleased]: https://github.com/ludo-technologies/add-skills/compare/v0.0.4...HEAD
[0.0.4]: https://github.com/ludo-technologies/add-skills/compare/v0.0.3...v0.0.4
[0.0.3]: https://github.com/ludo-technologies/add-skills/releases/tag/v0.0.3
