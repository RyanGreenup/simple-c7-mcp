"""User management service."""

from typing import TypedDict


class UserResult(TypedDict):
    """Result of user creation."""

    name: str
    created: bool


def list_users() -> list[str]:
    """List all users.

    Returns:
        A list of usernames.
    """
    return ["alice", "bob", "charlie"]


def create_user(name: str) -> UserResult:
    """Create a new user.

    Args:
        name: The username to create.

    Returns:
        A dict with user info and creation status.
    """
    return {"name": name, "created": True}
