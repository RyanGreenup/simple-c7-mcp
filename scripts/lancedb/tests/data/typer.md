# Typer - CLI Application Framework

## Introduction

Typer is a Python library for building command-line interface (CLI) applications with minimal code using Python type hints. Built on top of Click, it provides an intuitive way to create CLI tools by leveraging modern Python type annotations to automatically generate help text, parse arguments, validate inputs, and provide shell completion. The library follows the same design philosophy as FastAPI, making it the "FastAPI of CLIs" by prioritizing developer experience and reducing boilerplate code.

The framework supports everything from simple single-command scripts to complex multi-command applications with subcommands, argument validation, interactive prompts, progress bars, and rich terminal output. It automatically converts Python function signatures into CLI interfaces, handling type conversion, default values, and validation without requiring extensive configuration. Typer also includes a command-line tool that can run plain Python scripts as CLI applications, even if they don't explicitly use Typer internally.

## API Reference and Examples

### Running a simple function as CLI

Convert any Python function into a CLI application using `typer.run()`.

```python
import typer

def main(name: str, age: int = 0, formal: bool = False):
    """Greet a person by name."""
    if formal:
        greeting = f"Good day, {name}."
    else:
        greeting = f"Hello {name}!"

    if age:
        greeting += f" You are {age} years old."

    print(greeting)

if __name__ == "__main__":
    typer.run(main)
```

```bash
# Run with required argument
$ python app.py Alice
Hello Alice!

# Run with options
$ python app.py Bob --age 30 --formal
Good day, Bob. You are 30 years old.

# Get automatic help
$ python app.py --help
Usage: app.py [OPTIONS] NAME

  Greet a person by name.

Arguments:
  NAME  [required]

Options:
  --age INTEGER           [default: 0]
  --formal / --no-formal  [default: no-formal]
  --help                  Show this message and exit.
```

### Creating multi-command applications

Build applications with multiple subcommands using the Typer app decorator pattern.

```python
import typer

app = typer.Typer()

@app.command()
def create(username: str, email: str, admin: bool = False):
    """Create a new user account."""
    role = "admin" if admin else "user"
    print(f"Creating user: {username}")
    print(f"Email: {email}")
    print(f"Role: {role}")
    # Database logic here
    print("✓ User created successfully")

@app.command()
def delete(username: str, force: bool = typer.Option(False, "--force", "-f")):
    """Delete an existing user account."""
    if not force:
        confirm = typer.confirm(f"Are you sure you want to delete {username}?")
        if not confirm:
            print("Cancelled")
            raise typer.Abort()

    print(f"Deleting user: {username}")
    # Database logic here
    print("✓ User deleted")

@app.command()
def list():
    """List all users."""
    users = ["alice", "bob", "charlie"]
    print("Current users:")
    for user in users:
        print(f"  • {user}")

if __name__ == "__main__":
    app()
```

```bash
# List available commands
$ python app.py --help
Usage: app.py [OPTIONS] COMMAND [ARGS]...

Commands:
  create  Create a new user account.
  delete  Delete an existing user account.
  list    List all users.

# Run specific commands
$ python app.py create alice alice@example.com --admin
Creating user: alice
Email: alice@example.com
Role: admin
✓ User created successfully

$ python app.py delete bob --force
Deleting user: bob
✓ User deleted
```

### Using arguments and options with validation

Define CLI parameters using Argument and Option with validation and custom behavior.

```python
from typing import Optional
from pathlib import Path
import typer

app = typer.Typer()

def validate_email(email: str) -> str:
    """Validate email format."""
    if "@" not in email:
        raise typer.BadParameter("Invalid email format")
    return email

@app.command()
def register(
    username: str = typer.Argument(..., help="Username (3-20 characters)"),
    email: str = typer.Option(..., "--email", "-e", callback=validate_email),
    password: str = typer.Option(..., prompt=True, hide_input=True, confirmation_prompt=True),
    age: Optional[int] = typer.Option(None, min=13, max=120),
    config: Optional[Path] = typer.Option(None, exists=True, file_okay=True, dir_okay=False, readable=True)
):
    """Register a new user with validation."""
    if len(username) < 3 or len(username) > 20:
        typer.echo("Username must be 3-20 characters", err=True)
        raise typer.Exit(code=1)

    print(f"Registering user: {username}")
    print(f"Email: {email}")
    if age:
        print(f"Age: {age}")
    if config:
        print(f"Loading config from: {config}")
    print("✓ Registration complete")

if __name__ == "__main__":
    app()
```

```bash
# Interactive password prompt
$ python app.py register john_doe --email john@example.com --age 25
Password:
Repeat for confirmation:
Registering user: john_doe
Email: john@example.com
Age: 25
✓ Registration complete

# Validation errors
$ python app.py register alice --email invalid
Error: Invalid value for '--email' / '-e': Invalid email format

$ python app.py register bob --email bob@example.com --age 150
Error: Invalid value for '--age': 150 is larger than the maximum valid value 120.
```

### Enum choices for restricted options

Use Python Enums to provide fixed choice options with auto-completion.

```python
from enum import Enum
import typer

class Environment(str, Enum):
    development = "dev"
    staging = "staging"
    production = "prod"

class LogLevel(str, Enum):
    debug = "DEBUG"
    info = "INFO"
    warning = "WARNING"
    error = "ERROR"

app = typer.Typer()

@app.command()
def deploy(
    env: Environment = typer.Argument(Environment.development),
    log_level: LogLevel = typer.Option(LogLevel.info, "--log-level", "-l"),
    dry_run: bool = False
):
    """Deploy application to specified environment."""
    print(f"Environment: {env.value}")
    print(f"Log Level: {log_level.value}")

    if dry_run:
        print("[DRY RUN] Would deploy application")
    else:
        print(f"Deploying to {env.value}...")
        print("✓ Deployment complete")

if __name__ == "__main__":
    app()
```

```bash
# Use enum values
$ python app.py deploy prod --log-level ERROR
Environment: prod
Log Level: ERROR
Deploying to prod...
✓ Deployment complete

# Get choices in help
$ python app.py deploy --help
Usage: app.py deploy [OPTIONS] [ENV]:[dev|staging|prod]

Arguments:
  [ENV]:[dev|staging|prod]  [default: dev]

Options:
  -l, --log-level [DEBUG|INFO|WARNING|ERROR]  [default: INFO]
  --dry-run / --no-dry-run                    [default: no-dry-run]

# Invalid choice shows available options
$ python app.py deploy invalid
Error: Invalid value for '[ENV]': 'invalid' is not one of 'dev', 'staging', 'prod'.
```

### Nested subcommands and command groups

Create hierarchical command structures with subcommands organized into groups.

```python
import typer

# Create sub-apps
app = typer.Typer()
db_app = typer.Typer()
cache_app = typer.Typer()

# Database commands
@db_app.command("migrate")
def db_migrate(revision: str = "head"):
    """Run database migrations."""
    print(f"Running migrations to: {revision}")
    print("✓ Database migrated")

@db_app.command("seed")
def db_seed():
    """Seed database with test data."""
    print("Seeding database...")
    print("✓ Database seeded")

# Cache commands
@cache_app.command("clear")
def cache_clear():
    """Clear application cache."""
    print("Clearing cache...")
    print("✓ Cache cleared")

@cache_app.command("stats")
def cache_stats():
    """Show cache statistics."""
    print("Cache Statistics:")
    print("  Hit rate: 87.3%")
    print("  Size: 245 MB")

# Main app commands
@app.command()
def serve(port: int = 8000):
    """Start the application server."""
    print(f"Starting server on port {port}...")
    print("Server running at http://localhost:{port}")

# Register sub-apps
app.add_typer(db_app, name="db", help="Database operations")
app.add_typer(cache_app, name="cache", help="Cache management")

if __name__ == "__main__":
    app()
```

```bash
# Show top-level commands
$ python app.py --help
Commands:
  cache  Cache management
  db     Database operations
  serve  Start the application server.

# Access nested commands
$ python app.py db migrate
Running migrations to: head
✓ Database migrated

$ python app.py cache clear
Clearing cache...
✓ Cache cleared

$ python app.py serve --port 3000
Starting server on port 3000...
Server running at http://localhost:3000
```

### Interactive prompts and confirmations

Collect user input interactively with prompts, confirmations, and hidden input.

```python
import typer

app = typer.Typer()

@app.command()
def setup():
    """Interactive setup wizard."""
    typer.echo("=== Application Setup ===\n")

    # Basic prompt
    username = typer.prompt("Enter username")

    # Prompt with default
    email = typer.prompt("Enter email", default=f"{username}@example.com")

    # Hidden input for password
    password = typer.prompt("Enter password", hide_input=True)

    # Confirmation prompt
    is_admin = typer.confirm("Grant admin privileges?", default=False)

    # Type conversion
    max_connections = typer.prompt("Max connections", type=int, default=10)

    typer.echo("\n--- Configuration Summary ---")
    typer.echo(f"Username: {username}")
    typer.echo(f"Email: {email}")
    typer.echo(f"Admin: {is_admin}")
    typer.echo(f"Max connections: {max_connections}")

    if typer.confirm("\nSave configuration?"):
        typer.echo("✓ Configuration saved")
    else:
        typer.echo("Setup cancelled")
        raise typer.Abort()

if __name__ == "__main__":
    app()
```

```bash
$ python app.py setup
=== Application Setup ===

Enter username: alice
Enter email [alice@example.com]:
Enter password:
Grant admin privileges? [y/N]: y
Max connections [10]: 20

--- Configuration Summary ---
Username: alice
Email: alice@example.com
Admin: True
Max connections: 20

Save configuration? [y/N]: y
✓ Configuration saved
```

### Progress bars and rich output

Display progress indicators and styled terminal output for long-running operations.

```python
import time
import typer
from rich.progress import track
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()

@app.command()
def process(count: int = 100):
    """Process items with progress bar."""
    items_processed = 0

    for i in track(range(count), description="Processing items"):
        # Simulate processing
        time.sleep(0.02)
        items_processed += 1

    console.print(f"[green]✓[/green] Processed {items_processed} items")

@app.command()
def report():
    """Generate a formatted report."""
    table = Table(title="User Statistics")

    table.add_column("User", style="cyan", no_wrap=True)
    table.add_column("Status", style="magenta")
    table.add_column("Requests", justify="right", style="green")

    table.add_row("Alice", "Active", "1,234")
    table.add_row("Bob", "Active", "856")
    table.add_row("Charlie", "Inactive", "23")

    console.print(table)
    console.print("\n[bold green]Report generated successfully[/bold green]")

if __name__ == "__main__":
    app()
```

```bash
$ python app.py process --count 50
Processing items ━━━━━━━━━━━━━━━━━━━━ 100% 0:00:01
✓ Processed 50 items

$ python app.py report
         User Statistics
┏━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┓
┃ User    ┃ Status   ┃ Requests ┃
┡━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━┩
│ Alice   │ Active   │    1,234 │
│ Bob     │ Active   │      856 │
│ Charlie │ Inactive │       23 │
└─────────┴──────────┴──────────┘

Report generated successfully
```

### Testing CLI applications

Test Typer applications using the built-in testing utilities based on Click's test runner.

```python
# app.py
from typing import Optional
import typer

app = typer.Typer()

@app.command()
def greet(name: str, city: Optional[str] = None, excited: bool = False):
    """Greet a person."""
    message = f"Hello {name}"
    if city:
        message += f" from {city}"
    if excited:
        message += "!"
    else:
        message += "."
    typer.echo(message)

if __name__ == "__main__":
    app()
```

```python
# test_app.py
from typer.testing import CliRunner
from app import app

runner = CliRunner()

def test_greet_basic():
    """Test basic greeting."""
    result = runner.invoke(app, ["Alice"])
    assert result.exit_code == 0
    assert "Hello Alice." in result.output

def test_greet_with_city():
    """Test greeting with city option."""
    result = runner.invoke(app, ["Bob", "--city", "Seattle"])
    assert result.exit_code == 0
    assert "Hello Bob from Seattle." in result.output

def test_greet_excited():
    """Test excited greeting."""
    result = runner.invoke(app, ["Charlie", "--excited"])
    assert result.exit_code == 0
    assert "Hello Charlie!" in result.output

def test_missing_argument():
    """Test error when required argument is missing."""
    result = runner.invoke(app, [])
    assert result.exit_code != 0
    assert "Missing argument" in result.output

def test_help():
    """Test help output."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Greet a person." in result.output
```

```bash
# Run tests with pytest
$ pytest test_app.py -v
test_app.py::test_greet_basic PASSED
test_app.py::test_greet_with_city PASSED
test_app.py::test_greet_excited PASSED
test_app.py::test_missing_argument PASSED
test_app.py::test_help PASSED

===== 5 passed in 0.12s =====
```

### File and path handling

Work with files and paths using built-in validation and type conversion.

```python
from pathlib import Path
from typing import Optional
import typer

app = typer.Typer()

@app.command()
def process_file(
    input_file: Path = typer.Argument(..., exists=True, file_okay=True, dir_okay=False, readable=True),
    output_file: Path = typer.Argument(..., file_okay=True, dir_okay=False, writable=True),
    backup: bool = True
):
    """Process a file and write results to output."""
    if not input_file.exists():
        typer.echo(f"Error: {input_file} does not exist", err=True)
        raise typer.Exit(code=1)

    # Create backup if requested
    if backup and output_file.exists():
        backup_path = output_file.with_suffix(output_file.suffix + ".bak")
        output_file.rename(backup_path)
        typer.echo(f"Created backup: {backup_path}")

    # Process file
    content = input_file.read_text()
    processed = content.upper()  # Example processing
    output_file.write_text(processed)

    typer.echo(f"Processed {input_file} -> {output_file}")
    typer.echo(f"Input size: {input_file.stat().st_size} bytes")
    typer.echo(f"Output size: {output_file.stat().st_size} bytes")

@app.command()
def analyze_dir(
    directory: Path = typer.Option(".", exists=True, file_okay=False, dir_okay=True),
    pattern: str = "*.py"
):
    """Analyze files in a directory."""
    files = list(directory.glob(pattern))
    typer.echo(f"Found {len(files)} files matching '{pattern}' in {directory}")

    total_size = 0
    for file in files:
        size = file.stat().st_size
        total_size += size
        typer.echo(f"  {file.name}: {size:,} bytes")

    typer.echo(f"\nTotal size: {total_size:,} bytes")

if __name__ == "__main__":
    app()
```

```bash
# Process a file
$ python app.py process-file input.txt output.txt
Created backup: output.txt.bak
Processed input.txt -> output.txt
Input size: 1234 bytes
Output size: 1234 bytes

# Analyze directory
$ python app.py analyze-dir --directory ./src --pattern "*.py"
Found 5 files matching '*.py' in ./src
  main.py: 2,543 bytes
  utils.py: 1,892 bytes
  config.py: 456 bytes
  models.py: 3,210 bytes
  tests.py: 1,678 bytes

Total size: 9,779 bytes

# File validation error
$ python app.py process-file nonexistent.txt output.txt
Error: Invalid value for 'INPUT_FILE': Path 'nonexistent.txt' does not exist.
```

## Summary and Integration

Typer excels at creating production-ready CLI applications with minimal boilerplate code, making it ideal for tools, scripts, automation tasks, and developer utilities. The main use cases include building admin tools for web applications, creating data processing pipelines with clear command-line interfaces, developing DevOps automation scripts, and building interactive terminal applications. Its type-hint-based design ensures that CLI interfaces stay in sync with code, reducing bugs and maintenance overhead while providing excellent IDE support with autocompletion.

Integration with existing Python projects is straightforward - simply wrap functions with `typer.run()` for single commands or use `@app.command()` decorators for multi-command applications. Typer works seamlessly with other libraries like Rich for enhanced terminal output, supports Click extensions, and can be tested using the familiar pytest framework with the built-in CliRunner. The library scales from simple scripts to complex applications with nested subcommands, making it suitable for both quick automation tasks and large enterprise CLI tools. Installation is simple (`pip install typer`) and includes automatic shell completion for Bash, Zsh, Fish, and PowerShell when properly configured.
