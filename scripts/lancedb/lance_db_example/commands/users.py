"""User management commands."""

from lance_db_example import create_typer
from lance_db_example.services.users import create_user, list_users

app = create_typer()


@app.command()
def list():
    """List all users."""
    for user in list_users():
        print(user)


@app.command()
def create(name: str):
    """Create a new user."""
    result = create_user(name)
    print(f"Created user: {result['name']}")
