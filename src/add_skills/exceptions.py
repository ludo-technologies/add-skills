"""Exception classes for add-skills."""


class AddSkillsError(Exception):
    """Base exception for add-skills."""

    pass


class InstallError(AddSkillsError):
    """Installation error."""

    pass


class RegistryFetchError(AddSkillsError):
    """Failed to fetch registry from remote."""

    pass


class RegistryParseError(AddSkillsError):
    """Failed to parse registry JSON."""

    pass


class GitError(AddSkillsError):
    """Git operation error."""

    pass


class SourceParseError(AddSkillsError):
    """Failed to parse source string."""

    pass
