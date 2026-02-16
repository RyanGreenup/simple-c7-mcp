"""CLI integration tests.

These tests verify the CLI commands work end-to-end via CliRunner.
"""

from typer.testing import CliRunner

from lance_db_example.cli import app

runner = CliRunner()


def test_hello_default():
    """Test hello command with default name."""
    result = runner.invoke(app, ["hello"])
    assert result.exit_code == 0
    assert "Hello, World!" in result.stdout


def test_hello_with_name():
    """Test hello command with custom name."""
    result = runner.invoke(app, ["hello", "John"])
    assert result.exit_code == 0
    assert "Hello, John!" in result.stdout


def test_users_list():
    """Test users list command."""
    result = runner.invoke(app, ["users", "list"])
    assert result.exit_code == 0
    assert "alice" in result.stdout
    assert "bob" in result.stdout


def test_users_create():
    """Test users create command."""
    result = runner.invoke(app, ["users", "create", "John"])
    assert result.exit_code == 0
    assert "Created user: John" in result.stdout
