"""Unit tests for services.

These tests verify the business logic in isolation, without CLI overhead.
"""

from lance_db_example.services.greeting import greet
from lance_db_example.services.users import create_user, list_users


class TestGreetingService:
    """Tests for the greeting service."""

    def test_greet_default(self):
        """Test greeting with default name."""
        assert greet() == "Hello, World!"

    def test_greet_custom_name(self):
        """Test greeting with custom name."""
        assert greet("Alice") == "Hello, Alice!"

    def test_greet_empty_string(self):
        """Test greeting with empty string."""
        assert greet("") == "Hello, !"


class TestUsersService:
    """Tests for the users service."""

    def test_list_users_returns_list(self):
        """Test that list_users returns a list."""
        users = list_users()
        assert isinstance(users, list)
        assert len(users) > 0

    def test_list_users_contains_expected_users(self):
        """Test that list_users contains expected users."""
        users = list_users()
        assert "alice" in users
        assert "bob" in users

    def test_create_user_returns_dict(self):
        """Test that create_user returns a dict with expected keys."""
        result = create_user("newuser")
        assert isinstance(result, dict)
        assert "name" in result
        assert "created" in result

    def test_create_user_sets_name(self):
        """Test that create_user sets the correct name."""
        result = create_user("testuser")
        assert result["name"] == "testuser"
        assert result["created"] is True
