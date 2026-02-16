"""Command-line interface entry point."""

from lance_db_example import create_typer
from lance_db_example.commands import users
from lance_db_example.commands.hello import hello

app = create_typer()
_ = app.command()(hello)
app.add_typer(users.app, name="users")

if __name__ == "__main__":
    app()
