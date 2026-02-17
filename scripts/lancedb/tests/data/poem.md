### Install pre‑commit hooks

Source: https://python-poetry.org/docs/main/contributing

Installs the pre‑commit hooks defined in the repository. This one‑time setup enables automatic linting and formatting on each commit.

```bash
poetry run pre-commit install
```

--------------------------------

### Install Poetry Plugin with pipx

Source: https://python-poetry.org/docs/plugins

Shows commands to install and uninstall Poetry plugins using pipx. Includes version-specific syntax for different pipx releases.

```bash
pipx inject poetry poetry-plugin
```

```bash
pipx uninject poetry poetry-plugin          # For pipx versions >= 1.2.0

pipx runpip poetry uninstall poetry-plugin  # For pipx versions  < 1.2.0
```

--------------------------------

### Manual Poetry Installation with venv and pip - Bash

Source: https://python-poetry.org/docs/1

Performs manual installation by creating a virtual environment and installing Poetry via pip. Unix-only advanced method; omits git examples. Requires Python 3 and venv module; updates pip and setuptools first. Binary available at $VENV_PATH/bin/poetry; uninstall by deleting $VENV_PATH.

```bash
python3 -m venv $VENV_PATH
$VENV_PATH/bin/pip install -U pip setuptools
$VENV_PATH/bin/pip install poetry
```

--------------------------------

### Install Project Dependencies

Source: https://python-poetry.org/docs/main/basic-usage

Installs all defined dependencies for the project. Behavior differs based on operating mode - in package mode installs the project in editable mode, in non-package mode only installs dependencies. May trigger environment creation if none exists.

```bash
poetry install
```

--------------------------------

### Install and Activate Python for Project (pyenv)

Source: https://python-poetry.org/docs/1.8/managing-environments

Demonstrates a common workflow using `pyenv` to install a specific Python version, set it as the local version for the current project, and then install project dependencies using Poetry.

```bash
pyenv install 3.9.8
pyenv local 3.9.8  # Activate Python 3.9 for the current project
poetry install
```

--------------------------------

### Install Poetry project dependencies

Source: https://python-poetry.org/docs/main/contributing

Installs all project dependencies using Poetry. Run this after cloning the repository to set up the virtual environment. No additional inputs are required.

```bash
poetry install
poetry run pytest
```

--------------------------------

### Basic Poetry Installation in Docker (Python)

Source: https://python-poetry.org/docs/1.8/faq

Demonstrates a basic Dockerfile setup for a Python project using Poetry. This approach may lead to Docker cache invalidation when source files change.

```dockerfile
FROM python
COPY pyproject.toml poetry.lock .
COPY src/ ./src
RUN pip install poetry && poetry install --only main
```

--------------------------------

### Install Poetry in CI with Official Installer (Shell)

Source: https://python-poetry.org/docs/index

Uses official installer script with POETRY_HOME for CI pipelines. Controls installation path and version. Requires python3 and installer script. Outputs: Poetry at specified home path.

```shell
export POETRY_HOME=/opt/poetry
python3 install-poetry.py --version 2.0.0
$POETRY_HOME/bin/poetry --version
```

--------------------------------

### Installing Poetry with Pipx

Source: https://python-poetry.org/docs/index

Pipx installs Poetry globally in an isolated virtual environment, managing dependencies and allowing easy upgrades or uninstalls. Basic installation uses the standard command; advanced options support specific versions, parallel installations with suffixes, and git-based sources. Requires pipx pre-installed; outputs a runnable 'poetry' binary.

```bash
pipx install poetry
```

```bash
pipx install poetry==1.8.4
```

```bash
pipx install --suffix=@1.8.4 poetry==1.8.4
poetry@1.8.4 --version
```

```bash
pipx install --suffix=@preview --pip-args=--pre poetry
poetry@preview --version
```

```bash
pipx install --suffix @main git+https://github.com/python-poetry/poetry.git@main
pipx install --suffix @pr1234 git+https://github.com/python-poetry/poetry.git@refs/pull/1234/head
```

--------------------------------

### Optimized Poetry Installation in Docker (Python)

Source: https://python-poetry.org/docs/1.8/faq

Shows an optimized Dockerfile setup that separates dependency installation from source code copying to maintain better Docker cache efficiency. Uses --no-root and --no-directory flags.

```dockerfile
FROM python
COPY pyproject.toml poetry.lock .
RUN pip install poetry && poetry install --only main --no-root --no-directory
COPY src/ ./src
RUN poetry install --only main
```

--------------------------------

### Install Poetry with Official Installer on Windows Powershell

Source: https://python-poetry.org/docs/1

Downloads and executes the installer via Invoke-WebRequest in Powershell. Uses 'py' launcher or 'python' for Microsoft Store installations. Creates isolated environment similar to Unix methods.

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

--------------------------------

### Installer Configuration API

Source: https://python-poetry.org/docs/configuration

Configuration options for controlling Poetry's package installation behavior including binary distribution preferences and parallel execution.

```APIDOC
## Installer Configuration Options

### Description
Configuration parameters that control how Poetry installs packages, including binary distribution preferences, parallel execution, and build settings.

### Endpoint
Configuration options accessed via `poetry config` command or environment variables

### Parameters
#### installer.no-binary
- **Type** (string | boolean) - Optional - Disallow binary distributions for packages
- **Default**: `false`
- **Environment Variable**: `POETRY_INSTALLER_NO_BINARY`

#### installer.only-binary
- **Type** (string | boolean) - Optional - Enforce binary distributions for packages
- **Default**: `false`
- **Environment Variable**: `POETRY_INSTALLER_ONLY_BINARY`

#### installer.parallel
- **Type** (boolean) - Optional - Use parallel execution for installation
- **Default**: `true`
- **Environment Variable**: `POETRY_INSTALLER_PARALLEL`

#### installer.re-resolve
- **Type** (boolean) - Optional - Control dependency re-resolution behavior
- **Default**: `true`
- **Environment Variable**: `POETRY_INSTALLER_RE_RESOLVE`

#### python.installation-dir
- **Type** (string) - Optional - Directory for Poetry-managed Python versions
- **Default**: `{data-dir}/python`
- **Environment Variable**: `POETRY_PYTHON_INSTALLATION_DIR`

#### requests.max-retries
- **Type** (int) - Optional - Maximum number of retries for unstable network
- **Default**: `0`
- **Environment Variable**: `POETRY_REQUESTS_MAX_RETRIES`

### Configuration Values
#### installer.no-binary Values
- `:all:` or `true` - Disallow binary distributions for all packages
- `:none:` or `false` - Allow binary distributions for all packages
- `package[,package,..]` - Disallow binary distributions for specified packages only

### Examples
Set no-binary configuration locally:
```
poetry config --local installer.no-binary :all:
```

Set via environment variable for CI:
```
export POETRY_INSTALLER_NO_BINARY=:all:
```

Configure build settings for a package:
```
poetry config --local installer.build-config-settings.grpcio \
  '{"CC": "gcc", "--global-option": ["--some-global-option"], "--build-option": ["--build-option1", "--build-option2"]}'
```
```

--------------------------------

### Install Poetry using pipx

Source: https://python-poetry.org/docs/1

Installs Poetry globally via pipx, which manages virtual environments for CLI apps. Requires pre-installed pipx; supports basic installation and version specification. Outputs the 'poetry' command for use.

```bash
pipx install poetry
```

```bash
pipx install poetry==1.2.0
```

--------------------------------

### Example pyproject.toml for Cython Extension TOML

Source: https://python-poetry.org/docs/main/building-extension-modules

Full example of pyproject.toml configuration for building a Cython-based native extension. Includes build-system requirements with cython and setuptools, package settings using src layout, and includes for binary outputs in wheels. Build inputs are handled separately for source distributions.

```toml
[build-system]
requires = ["poetry-core", "cython", "setuptools"]
build-backend = "poetry.core.masonry.api"

[tool.poetry]
...
packages = [
    { include = "package", from = "src"},
]
include = [
    { path = "src/package/**/*.so", format = "wheel" },
]

```

--------------------------------

### Verify Poetry Installation - Bash

Source: https://python-poetry.org/docs/1

Checks the installed version of Poetry after setup. Requires Poetry to be in PATH. Outputs version information like 'Poetry (version 1.2.0)' if successful.

```bash
poetry --version
```

--------------------------------

### Install Poetry Using Official Curl Installer - Bash

Source: https://python-poetry.org/docs/1

Installs Poetry by executing the official installer script via curl and Python. Supports version pinning, git repository installation, and uninstallation options. Requires curl and Python 3; installs to platform-specific directories like $HOME/.local/bin on Unix. Limitations include potential issues on Windows for updates.

```bash
curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.2.0 python3 -
```

```bash
curl -sSL https://install.python-poetry.org | python3 - --git https://github.com/python-poetry/poetry.git@main
```

```bash
curl -sSL https://install.python-poetry.org | python3 - --uninstall
```

```bash
curl -sSL https://install.python-poetry.org | POETRY_UNINSTALL=1 python3 -
```

--------------------------------

### Install Poetry Plugin with pip

Source: https://python-poetry.org/docs/plugins

Demonstrates how to install and uninstall Poetry plugins using pip in Poetry's virtual environment. Requires POETRY_HOME environment variable.

```bash
$POETRY_HOME/bin/pip install --user poetry-plugin
```

```bash
$POETRY_HOME/bin/pip uninstall poetry-plugin
```

--------------------------------

### Install Poetry with Official Installer on Linux/macOS

Source: https://python-poetry.org/docs/1

Uses curl to download and execute the installer script, creating an isolated virtual environment. Defaults to user-specific paths; supports Python 3 explicitly. Avoids ambiguity with python2 by using python3.

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

```bash
curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -
```

```bash
curl -sSL https://install.python-poetry.org | python3 - --preview
```

```bash
curl -sSL https://install.python-poetry.org | POETRY_PREVIEW=1 python3 -
```

```bash
curl -sSL https://install.python-poetry.org | python3 - --version 1.2.0
```

--------------------------------

### Configure tox to use Poetry for full installation in editable mode

Source: https://python-poetry.org/docs/1.8/faq

Defines a tox environment that skips tox's own install step and lets Poetry install the package and its dependencies in editable mode before running tests. Uses `skip_install = true` and `commands_pre = poetry install`. Ensures tests run against local source files.

```ini
[tox]

[testenv]
skip_install = true
allowlist_externals = poetry
commands_pre =
    poetry install
commands =
    poetry run pytest tests/ --import-mode importlib

```

--------------------------------

### Install extras with Poetry

Source: https://python-poetry.org/docs/main/pyproject

Commands to install packages with specific extras or all extras. Extras must be defined in the project's configuration.

```bash
poetry install --extras "mysql pgsql"
```

```bash
poetry install -E mysql -E pgsql
```

```bash
poetry install --all-extras
```

```bash
pip install awesome[databases]
```

--------------------------------

### Install Optional Dependency Group (CLI)

Source: https://python-poetry.org/docs/managing-dependencies

This command demonstrates how to install optional dependency groups along with the default dependencies using the 'poetry install --with' command, specifying the 'docs' group.

```bash
poetry install --with docs

```

--------------------------------

### Complete Cython extension configuration example

Source: https://python-poetry.org/docs/building-extension-modules

Full example of a pyproject.toml configuration for a Cython extension project. This includes build system requirements, package definition, and file inclusion rules. The configuration sets up poetry-core build backend, defines package structure, and ensures proper file distribution for both wheel and source formats.

```toml
[build-system]
requires = ["poetry-core", "cython", "setuptools"]
build-backend = "poetry.core.masonry.api"

[tool.poetry]
...
packages = [
    { include = "package", from = "src"},
]
include = [
    { path = "src/package/**/*.so", format = "wheel" },
]
```

--------------------------------

### Install Poetry Dependencies and Run Tests - Bash

Source: https://python-poetry.org/docs/1.8/contributing

This Bash script installs project dependencies using Poetry and runs the test suite to verify the local setup. It requires Poetry to be pre-installed in a Python 3.8+ environment and access to the forked repository. Outputs include test results indicating pass/fail status, but success depends on a clean codebase without conflicts.

```bash
poetry install
poetry run pytest

```

--------------------------------

### Scripts Configuration - Poetry

Source: https://python-poetry.org/docs/1.8/pyproject

Creates console script entry points that execute specific functions when the package is installed. Scripts map command names to Python functions and require running poetry install to activate in the virtual environment.

```toml
[tool.poetry.scripts]
my_package_cli = 'my_package.console:run'
```

--------------------------------

### Configure pre-commit hooks with Poetry

Source: https://python-poetry.org/docs/pre-commit-hooks

Example configuration for pre-commit hooks in .pre-commit-config.yaml. This minimal setup includes the core Poetry hooks for checking configuration, locking dependencies, exporting requirements, and installing packages. The rev field must be filled with the specific Poetry version to use.

```yaml
repos:
-   repo: https://github.com/python-poetry/poetry
    rev: ''  # add version here
    hooks:
    -   id: poetry-check
    -   id: poetry-lock
    -   id: poetry-export
    -   id: poetry-install
```

--------------------------------

### Meson Build Script (Python)

Source: https://python-poetry.org/docs/main/building-extension-modules

This script demonstrates building a project using Meson. It sets up a build directory, runs Meson to configure and compile the project, and then installs it. Requires Meson.

```Python
from __future__ import annotations

import subprocess

from pathlib import Path

def meson(*args):
    subprocess.call(["meson", *args])

def build():
    build_dir = Path(__file__).parent.joinpath("build")
    build_dir.mkdir(parents=True, exist_ok=True)

    meson("setup", build_dir.as_posix())
    meson("compile", "-C", build_dir.as_posix())
    meson("install", "-C", build_dir.as_posix())


if __name__ == "__main__":
    build()
```

--------------------------------

### Advanced pipx Installation for Poetry Versions

Source: https://python-poetry.org/docs/1

Enables parallel installations of Poetry versions or prereleases using suffixes for testing. Accepts pip requirement specs like git sources for development branches or pull requests. Each installation creates a unique binary name.

```bash
pipx install --suffix=@1.2.0 poetry==1.2.0
poetry@1.2.0 --version
```

```bash
pipx install --suffix=@preview --pip-args=--pre poetry
poetry@preview --version
```

```bash
pipx install --suffix @main git+https://github.com/python-poetry/poetry.git@main
```

```bash
pipx install --suffix @pr1234 git+https://github.com/python-poetry/poetry.git@refs/pull/1234/head
```

--------------------------------

### Install Poetry via official installer (Unix)

Source: https://python-poetry.org/docs/main

Downloads and runs the official Poetry installer script in a single pipe. Works on Linux, macOS, and WSL using Python 3. Requires curl and a Python interpreter.

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

--------------------------------

### Install Poetry plugin with pip in Poetry's virtual environment (Shell)

Source: https://python-poetry.org/docs/main/plugins

Installs a plugin using the pip binary located in Poetry's virtual environment. Uses the $POETRY_HOME environment variable to reference the correct pip executable.

```shell
$POETRY_HOME/bin/pip install --user poetry-plugin
```

--------------------------------

### Install and Manage Poetry Plugins via Command Line

Source: https://python-poetry.org/docs/1.8/plugins

Commands for adding, removing, and listing Poetry plugins using pipx, pip, or Poetry self commands. Requires Poetry installation and appropriate environment variables like $POETRY_HOME; supports package specifications similar to poetry add. Limitations include potential issues on Windows with self commands and compatibility checks only in self add.

```Bash
pipx inject poetry poetry-plugin
```

```Bash
pipx uninject poetry poetry-plugin          # For pipx versions >= 1.2.0

pipx runpip poetry uninstall poetry-plugin  # For pipx versions  < 1.2.0
```

```Bash
$POETRY_HOME/bin/pip install --user poetry-plugin
```

```Bash
$POETRY_HOME/bin/pip uninstall poetry-plugin
```

```Bash
poetry self add poetry-plugin
```

```Bash
poetry self remove poetry-plugin
```

```Bash
poetry self show plugins
```

--------------------------------

### Installing Poetry with Official Installer

Source: https://python-poetry.org/docs/index

The official installer sets up Poetry in a dedicated virtual environment, supporting Linux, macOS, Windows via curl or PowerShell. Advanced usage allows custom home directories, preview versions, specific releases, or git sources through environment variables or flags. Outputs Poetry binary; may require adding to PATH manually.

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

```bash
curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -
```

```bash
curl -sSL https://install.python-poetry.org | python3 - --preview
```

```bash
curl -sSL https://install.python-poetry.org | POETRY_PREVIEW=1 python3 -
```

```bash
curl -sSL https://install.python-poetry.org | python3 - --version 1.8.4
```

```bash
curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.8.4 python3 -
```

```bash
curl -sSL https://install.python-poetry.org | python3 - --git https://github.com/python-poetry/poetry.git@main
```

--------------------------------

### List installed Poetry plugins (Shell)

Source: https://python-poetry.org/docs/main/plugins

Displays all plugins currently installed in the Poetry environment.

```shell
poetry self show plugins
```

--------------------------------

### Configuring pyproject.toml for Poetry Project Metadata

Source: https://python-poetry.org/docs/basic-usage

The pyproject.toml file defines project metadata such as name, version, authors, and dependencies using TOML format. It integrates with Poetry's build system and replaces traditional setup files. Inputs include project details; outputs a configuration file readable by Poetry for installation and building. Limitations: Requires Poetry-core for build backend; Python version must be manually available on the system.

```toml
[project]
name = "poetry-demo"
version = "0.1.0"
description = ""
authors = [
    {name = "Sébastien Eustace", email = "sebastien@eustace.io"}
]
readme = "README.md"
requires-python = ">=3.9"
dependencies = [
]

[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"
```

--------------------------------

### Get Revision by Tag from Git

Source: https://python-poetry.org/docs/dependency-specification

This demonstrates specifying a dependency from a Git repository using a tag. Requires a Git URL and tag name as input, and installs the package specified by the tag.

```INI
[project]
# ...
dependencies = [
    "git+https://github.com/numpy/numpy.git@v0.13.2"
]
```

--------------------------------

### Configure Poetry hooks for monorepo setup

Source: https://python-poetry.org/docs/pre-commit-hooks

Example configuration for using Poetry pre-commit hooks in monorepo setups or when pyproject.toml is not in the root directory. The -C argument specifies the subdirectory containing the project files. The poetry-export hook is configured to output to a specific requirements.txt location.

```yaml
repos:
-   repo: https://github.com/python-poetry/poetry
    rev: ''  # add version here
    hooks:
    -   id: poetry-check
        args: ["-C", "./subdirectory"]
    -   id: poetry-lock
        args: ["-C", "./subdirectory"]
    -   id: poetry-export
        args: ["-C", "./subdirectory", "-f", "requirements.txt", "-o", "./subdirectory/requirements.txt"]
    -   id: poetry-install
        args: ["-C", "./subdirectory"]
```

--------------------------------

### Configure Poetry build script for Meson builds

Source: https://python-poetry.org/docs/building-extension-modules

Configures a Poetry project to use Meson as the build system through a custom build script. The script calls Meson commands to setup, compile, and install the project. Requires meson build dependency in pyproject.toml.

```toml
[tool.poetry.build]
script = "build-extension.py"

[build-system]
requires = ["poetry-core", "meson"]
build-backend = "poetry.core.masonry.api"

```

```python
from __future__ import annotations

import subprocess

from pathlib import Path


def meson(*args):
    subprocess.call(["meson", *args])


def build():
    build_dir = Path(__file__).parent.joinpath("build")
    build_dir.mkdir(parents=True, exist_ok=True)

    meson("setup", build_dir.as_posix())
    meson("compile", "-C", build_dir.as_posix())
    meson("install", "-C", build_dir.as_posix())


if __name__ == "__main__":
    build()

```

--------------------------------

### Install Poetry plugin using pipx (Shell)

Source: https://python-poetry.org/docs/main/plugins

Adds a Poetry plugin to an existing Poetry installation managed by pipx. Uses the pipx inject command to install the plugin package into Poetry's environment.

```shell
pipx inject poetry poetry-plugin
```

--------------------------------

### Install Poetry in CI with Pipx (Shell)

Source: https://python-poetry.org/docs/index

Installs Poetry using pipx for CI environments, ensuring version pinning. Requires pipx. Inputs: Version number. Outputs: Poetry installed via pipx.

```shell
pipx install poetry==2.0.0
```

--------------------------------

### Tox configuration for editable install with Poetry

Source: https://python-poetry.org/docs/main/faq

Tox configuration that skips pip install and uses Poetry to install dependencies in editable mode.

```ini
[tox]

[testenv]
skip_install = true
allowlist_externals = poetry
commands_pre =
    poetry install
commands =
    poetry run pytest tests/ --import-mode importlib
```

--------------------------------

### Install Project Dependencies with Poetry

Source: https://python-poetry.org/docs/1.8/cli

Installs dependencies defined in pyproject.toml and poetry.lock. Uses lock file versions if present, otherwise resolves and creates one. Supports excluding ('--without') or including ('--with', '--only') dependency groups, installing extras, and skipping root package installation.

```shell
poetry install

```

```shell
poetry install --without test,docs

```

```shell
poetry install --with test,docs

```

```shell
poetry install --only test,docs

```

```shell
poetry install --only-root

```

```shell
poetry install --sync

```

```shell
poetry install --without dev --sync

```

```shell
poetry install --with docs --sync

```

```shell
poetry install --only dev --sync

```

```shell
poetry install --extras "mysql pgsql"

```

```shell
poetry install -E mysql -E pgsql

```

```shell
poetry install --all-extras

```

```shell
poetry install --no-root

```

```shell
poetry install --no-directory

```

```shell
poetry install --compile

```

--------------------------------

### Manage Poetry installation with self subcommands

Source: https://python-poetry.org/docs/cli

Covers the `self` namespace commands for managing Poetry's own runtime environment, including adding plugins, installing dependencies, locking, removing packages, and displaying installed add-ons. These commands operate on Poetry's internal virtualenv and share options like `--dry-run`.

```Shell
poetry self add poetry-plugin-export
```

```Shell
poetry self add poetry-core@latest
```

```Shell
poetry self add artifacts-keyring
```

```Shell
poetry self install
```

```Shell
poetry self lock
```

```Shell
poetry self remove poetry-plugin-export
```

```Shell
poetry self show
```

```Shell
poetry self show plugins
```

--------------------------------

### Configure build system for Poetry library

Source: https://python-poetry.org/docs/libraries

Specify the PEP 517 build backend and its requirements in the project's pyproject.toml. This enables Poetry to build source and wheel distributions. The configuration must be placed under the [build-system] table.

```toml
[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"

```

--------------------------------

### Define optional dependencies with extras

Source: https://python-poetry.org/docs/dependency-specification

Shows how to define optional dependencies that are installed only when specific extras are requested during installation.

```Python
[project.optional-dependencies]
paths = [
    "pathlib2 (>=2.2,<3.0) ; sys_platform == 'win32'"
]
```

--------------------------------

### Manage Poetry Plugins with self Commands

Source: https://python-poetry.org/docs/plugins

Shows Poetry's self commands for adding, removing, and listing plugins. Includes warnings about Windows compatibility issues.

```bash
poetry self add poetry-plugin
```

```bash
poetry self remove poetry-plugin
```

```bash
poetry self show plugins
```

--------------------------------

### Install Poetry using pipx

Source: https://python-poetry.org/docs/main

Installs the latest Poetry release globally via pipx, which isolates the CLI in its own virtual environment. Requires pipx to be pre‑installed. The command creates a `poetry` executable accessible from the PATH.

```bash
pipx install poetry
```

--------------------------------

### Install optional dependency group

Source: https://python-poetry.org/docs/1.8/managing-dependencies

Command to install optional dependency groups in addition to default dependencies. The --with option specifies which optional groups to include. This allows selective installation of environment-specific dependencies.

```bash
poetry install --with docs
```

--------------------------------

### Basic Tox Configuration with pytest

Source: https://python-poetry.org/docs/faq

Simple tox configuration for testing using pytest. Creates isolated environment, installs pytest as dependency, and runs tests using importlib mode. Dependencies are resolved by pip during sdist installation.

```ini
[tox]

[testenv]
deps =
    pytest
commands =
    pytest tests/ --import-mode importlib

```

--------------------------------

### Get Revision by Commit Hash from Git

Source: https://python-poetry.org/docs/dependency-specification

This shows how to specify a dependency from a Git repository using a specific commit hash. Requires a Git URL and commit hash as input, and installs a specific version of the package.

```INI
[project]
# ...
dependencies = [
    "git+https://github.com/pallets/flask.git@38eb5d3b"
]
```

--------------------------------

### Tox configuration with Poetry for dependency resolution

Source: https://python-poetry.org/docs/main/faq

Tox configuration that uses Poetry to install locked dependencies after initial pip installation.

```ini
[tox]

[testenv]
allowlist_externals = poetry
commands_pre =
    poetry install --no-root --sync
commands =
    poetry run pytest tests/ --import-mode importlib
```

--------------------------------

### Delete virtual environments using Poetry

Source: https://python-poetry.org/docs/main/managing-environments

Provides command-line examples for removing Poetry-managed virtual environments. Supports deleting by full path, Python version, multiple versions at once, or all environments with the `--all` flag. Also shows the simple command for in-project environments. Requires Poetry installed and appropriate permissions.

```shell
poetry env remove /full/path/to/python
poetry env remove python3.7
poetry env remove 3.7
poetry env remove test-O3eWbxRl-py3.7

poetry env remove python3.6 python3.7 python3.8

poetry env remove --all

poetry env remove
```

--------------------------------

### Configure pyproject.toml for Poetry Project

Source: https://python-poetry.org/docs/1.8/basic-usage

Shows the default pyproject.toml configuration generated by Poetry for a new project. Includes project metadata, dependencies section, and build system requirements. The TOML file orchestrates the project and its dependencies using Poetry's configuration format.

```toml
[tool.poetry]
name = "poetry-demo"
version = "0.1.0"
description = ""
authors = ["Sébastien Eustace <sebastien@eustace.io>"]
readme = "README.md"
packages = [{include = "poetry_demo"}]

[tool.poetry.dependencies]
python = "^3.7"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

--------------------------------

### Get Latest Revision from Git Branch

Source: https://python-poetry.org/docs/dependency-specification

This demonstrates how to specify a dependency from a Git repository, fetching the latest revision from the 'next' branch. The input is a Git URL and branch name, and the output is the package installed from that branch.

```INI
[project]
# ...
dependencies = [
    "git+https://github.com/kennethreitz/requests.git@next"
]
```

--------------------------------

### Build library package with Poetry

Source: https://python-poetry.org/docs/libraries

Run the Poetry build command to create both a source distribution (sdist) and a wheel. The command works in an isolated environment and respects the build-system configuration defined in pyproject.toml.

```bash
poetry build

```

--------------------------------

### Specify Python Version Constraint in pyproject.toml

Source: https://python-poetry.org/docs/1.8/basic-usage

Demonstrates how to specify Python version constraints in pyproject.toml dependencies section. Uses caret notation (^3.7.0) to allow any Python 3 version greater than 3.7.0. Poetry requires explicit Python version specification and does not install interpreters automatically.

```toml
[tool.poetry.dependencies]
python = "^3.7.0"
```

--------------------------------

### Configure poetry-export hook with verbose output

Source: https://python-poetry.org/docs/pre-commit-hooks

Example configuration for the poetry-export hook with verbose output enabled. The verbose option outputs the export process to the console during pre-commit execution. This hook requires the Export Poetry Plugin to be installed.

```yaml
hooks:
-   id: poetry-export
    args: ["-f", "requirements.txt"]
    verbose: true
```

--------------------------------

### Install Poetry from Git with pipx

Source: https://python-poetry.org/docs/main

Installs Poetry directly from a Git repository using pipx, which can target a branch, tag, or pull‑request reference. Allows testing unreleased changes. The Git URL follows the standard `git+` syntax.

```bash
pipx install --suffix @main git+https://github.com/python-poetry/poetry.git@main
```

```bash
pipx install --suffix @pr1234 git+https://github.com/python-poetry/poetry.git@refs/pull/1234/head
```

--------------------------------

### Apply Environment Markers to Dependencies

Source: https://python-poetry.org/docs/1.8/dependency-specification

Illustrates the use of environment markers via the `markers` property to define complex installation conditions for dependencies. This allows for conditional installation based on system properties or Python versions.

```toml
[tool.poetry.dependencies]
pathlib2 = { version = "^2.2", markers = "python_version <= '3.4' or sys_platform == 'win32'" }
```

--------------------------------

### Use environment markers for complex conditions

Source: https://python-poetry.org/docs/dependency-specification

Demonstrates how to use environment markers for more complex dependency installation conditions, including platform-specific dependencies.

```Python
[project]
dependencies = [
    "pathlib2 (>=2.2,<3.0) ; python_version <= '3.4' or sys_platform == 'win32'"
]
```

```TOML
[tool.poetry.dependencies]
pathlib2 = { version = "^2.2", markers = "python_version <= '3.4' or sys_platform == 'win32'" }
```

--------------------------------

### Configure tox to run Poetry with dependency synchronization

Source: https://python-poetry.org/docs/1.8/faq

Sets up a tox test environment that allows external Poetry commands, installs dependencies without creating a project package, and runs pytest. Uses `allowlist_externals = poetry` and `commands_pre` with `poetry install --no-root --sync`. Suitable for projects using Poetry to manage locked dependencies inside tox.

```ini
[tox]

[testenv]
allowlist_externals = poetry
commands_pre =
    poetry install --no-root --sync
commands =
    poetry run pytest tests/ --import-mode importlib

```

--------------------------------

### Install only project root

Source: https://python-poetry.org/docs/main/managing-dependencies

Installs only the project root package without any dependencies. Useful for development scenarios where you want to work with the local package directly.

```bash
poetry install --only-root

```

--------------------------------

### Check Poetry Version and Update

Source: https://python-poetry.org/docs/main

Commands to verify Poetry installation and update to the latest, preview, or specific version. Essential for validating successful installation and keeping Poetry current.

```bash
poetry --version
```

```bash
poetry self update
```

```bash
poetry self update --preview
```

```bash
poetry self update 1.8.4
```

--------------------------------

### Install Pre-Commit Hooks - Bash

Source: https://python-poetry.org/docs/1.8/contributing

This Bash command installs pre-commit hooks to automate linting and style checks on commits. It uses Poetry to run pre-commit, requiring pre-commit to be listed as a dependency. Executes one-time in the local repository; no specific inputs or outputs, but it sets up automatic checks. Limitations are that it must be run after cloning and before committing to prevent failing commits.

```bash
poetry run pre-commit install

```

--------------------------------

### Install Poetry in CI with Manual Pip (Shell)

Source: https://python-poetry.org/docs/index

Manual pip installation in venv for CI control. Recommends isolating Poetry from project environments. Requires python3 and venv. Inputs: POETRY_HOME path. Outputs: Poetry version check.

```shell
export POETRY_HOME=/opt/poetry
python3 -m venv $POETRY_HOME
$POETRY_HOME/bin/pip install poetry==2.0.0
$POETRY_HOME/bin/poetry --version
```

--------------------------------

### Adding Simple API Repository

Source: https://python-poetry.org/docs/main/repositories

Poetry can fetch and install package dependencies from public or private custom repositories that implement the simple repository API (PEP 503). Configure these sources using the `poetry source add` command.

```APIDOC
## Adding Simple API Repository

### Description
Poetry can fetch and install package dependencies from public or private custom repositories that implement the simple repository API (PEP 503). Configure these sources using the `poetry source add` command. Note the trailing `/simple/` is important for PEP 503 compliant sources. Poetry also supports PEP 658 for reducing dependency resolution time.

### Method
Command Line Interface

### Endpoint
Not Applicable (Local configuration)

### Parameters
#### Command Arguments
- **name** (string) - Required - The name of the repository.
- **url** (string) - Required - The URL of the repository (must end with `/simple/`).

### Request Example
```bash
poetry source add testpypi https://test.pypi.org/simple/
```

### Warning
When using sources that distribute large wheels without file checksums, Poetry may download each candidate wheel to generate the checksum, potentially leading to long dependency resolution times.
```

--------------------------------

### Install Poetry in CI with pipx - Bash

Source: https://python-poetry.org/docs/1

Installs a pinned version of Poetry using pipx for reproducible CI environments. Prioritizes stability over latest features. Requires pipx; suitable for pipelines with version control for upgrades after validation.

```bash
pipx install poetry==1.2.0
```

--------------------------------

### Add Dependencies Using Poetry CLI

Source: https://python-poetry.org/docs/main/basic-usage

Command-line approach to add dependencies to the project. Automatically finds suitable version constraints and installs the package with its sub-dependencies. This modifies the pyproject.toml file automatically.

```bash
$ poetry add pendulum
```

--------------------------------

### Specify Project Plugins in pyproject.toml

Source: https://python-poetry.org/docs/plugins

Illustrates how to declare required plugins for a project in pyproject.toml. Uses the same syntax as dependency specifications.

```toml
[tool.poetry.requires-plugins]
my-application-plugin = ">1.0"
```

--------------------------------

### Docker Cache Invalidation with Poetry Install

Source: https://python-poetry.org/docs/main/faq

Illustrates a common Dockerfile pattern that leads to cache invalidation when using `poetry install`. It provides an alternative two-step approach to install dependencies separately from copying source code, optimizing Docker build cache.

```dockerfile
FROM python
COPY pyproject.toml poetry.lock .
COPY src/ ./src
RUN pip install poetry && poetry install --only main

```

```dockerfile
FROM python
COPY pyproject.toml poetry.lock .
RUN pip install poetry && poetry install --only main --no-root --no-directory
COPY src/ ./src
RUN poetry install --only main

```

--------------------------------

### Add Git Dependencies - Poetry

Source: https://python-poetry.org/docs/1.8/cli

Installs packages directly from Git repositories using HTTPS or SSH. Supports specific branches, tags, or revisions. Useful for installing development versions or private packages.

```shell
poetry add git+https://github.com/sdispater/pendulum.git

poetry add git+ssh://git@github.com/sdispater/pendulum.git

poetry add git+ssh://git@github.com:sdispater/pendulum.git

# Specific branch or tag
poetry add git+https://github.com/sdispater/pendulum.git#develop
poetry add git+https://github.com/sdispater/pendulum.git#2.0.5

poetry add git+ssh://git@github.com/sdispater/pendulum.git#develop
poetry add git+ssh://git@github.com/sdispater/pendulum.git#2.0.5

# Subdirectory
poetry add git+https://github.com/myorg/mypackage_with_subdirs.git@main#subdirectory=subdir
```

--------------------------------

### Install only runtime dependencies

Source: https://python-poetry.org/docs/main/managing-dependencies

Installs only the main runtime dependencies of the project, excluding all optional groups. Ideal for production deployments where only essential dependencies are needed.

```bash
poetry install --only main

```

--------------------------------

### Cython Extension Build Script (Python)

Source: https://python-poetry.org/docs/main/building-extension-modules

This script demonstrates building Cython extensions using setuptools. It compiles .pyx files, applies compile and link arguments, and copies the compiled extensions to the project's source directory. Requires Cython and setuptools.

```Python
from __future__ import annotations

import os
import shutil

from pathlib import Path

from Cython.Build import cythonize
from setuptools import Distribution
from setuptools import Extension
from setuptools.command.build_ext import build_ext

COMPILE_ARGS = ["-march=native", "-O3", "-msse", "-msse2", "-mfma", "-mfpmath=sse"]
LINK_ARGS = []
INCLUDE_DIRS = []
LIBRARIES = ["m"]

def build() -> None:
    extensions = [
        Extension(
            "*",
            ["src/package/*.pyx"],
            extra_compile_args=COMPILE_ARGS,
            extra_link_args=LINK_ARGS,
            include_dirs=INCLUDE_DIRS,
            libraries=LIBRARIES,
        )
    ]
    ext_modules = cythonize(
        extensions,
        include_path=INCLUDE_DIRS,
        compiler_directives={"binding": True, "language_level": 3},
    )

    distribution = Distribution({
        "name": "package",
        "ext_modules": ext_modules
    })

    cmd = build_ext(distribution)
    cmd.ensure_finalized()
    cmd.run()

    # Copy built extensions back to the project
    for output in cmd.get_outputs():
        output = Path(output)
        relative_extension = Path("src") / output.relative_to(cmd.build_lib)

        shutil.copyfile(output, relative_extension)
        mode = os.stat(relative_extension).st_mode
        mode |= (mode & 0o444) >> 2
        os.chmod(relative_extension, mode)


if __name__ == "__main__":
    build()
```

--------------------------------

### Original Poetry Configuration in pyproject.toml

Source: https://python-poetry.org/docs/faq

This shows the traditional [tool.poetry] setup for project metadata, dependencies, and build system. It includes main dependencies, dev groups, scripts, and package inclusion. No external dependencies beyond Poetry itself; outputs a standard pyproject.toml for Poetry-managed projects. Limitations: Not PEP 621 compliant without migration.

```toml
[tool.poetry]
name = "foobar"
version = "0.1.0"
description = ""
authors = ["Baz Qux <baz.qux@example.com>"]
readme = "README.md"
packages = [{ include = "awesome", from = "src" }]
include = [{ path = "tests", format = "sdist" }]
homepage = "https://python-foobar.org/"
repository = "https://github.com/python-foobar/foobar"
documentation = "https://python-foobar.org/docs"
keywords = ["packaging", "dependency", "foobar"]
classifiers = [
    "Topic :: Software Development :: Build Tools",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

[tool.poetry.scripts]
foobar = "foobar.console.application:main"

[tool.poetry.dependencies]
python = "^3.13"
httpx = "^0.28.1"

[tool.poetry.group.dev.dependencies]
pre-commit = ">=2.10"

[tool.poetry.group.test.dependencies]
pytest = ">=8.0"

[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"

```

--------------------------------

### Declaring Optional Dependency Groups

Source: https://python-poetry.org/docs/main/managing-dependencies

Mark groups as optional with 'optional = true' for environment-specific needs like 'docs'. Install via 'poetry install --with <group>'. Dependencies resolve with others, ensuring compatibility. Mixes PEP 735 and legacy syntax.

```toml
[dependency-groups]
docs = [
    "mkdocs",
]

[tool.poetry.group.docs]
optional = true

```

```toml
[tool.poetry.group.docs]
optional = true

[tool.poetry.group.docs.dependencies]
mkdocs = "*"

```

```bash
poetry install --with docs

```

--------------------------------

### Define GUI scripts in Poetry

Source: https://python-poetry.org/docs/main/pyproject

Configures GUI scripts that will be installed with the package. Scripts execute GUI functions from specified modules. Requires running poetry install after adding or updating scripts.

```toml
[project.gui-scripts]
my_package_gui = 'my_package.gui:run'
```

--------------------------------

### Configure distribution files for extensions

Source: https://python-poetry.org/docs/building-extension-modules

Specifies which files to include in different distribution formats. This example shows including compiled .so files in wheels while including source .c files in the source distribution. This pattern ensures build outputs are packaged properly while preserving source materials for distribution.

```toml
[tool.poetry]
...
include = [
    { path = "package/**/*.so", format = "wheel" },
    # sources must be present in sdist, can be ignored if you only have *.pyx sources
    { path = "package/**/*.c", format = "sdist" },
]
```

--------------------------------

### Install only specific dependency groups

Source: https://python-poetry.org/docs/main/managing-dependencies

Installs only the specified dependency groups, ignoring default dependencies. Useful for isolated environments or specific deployment scenarios.

```bash
poetry install --only docs

```

--------------------------------

### Creating a New Poetry Project with poetry new

Source: https://python-poetry.org/docs/basic-usage

The 'poetry new' command initializes a new Python project directory with a standard structure including pyproject.toml, README.md, and source/tests folders. It sets up the project for dependency management using Poetry. No inputs beyond the project name are required; outputs a ready-to-use project scaffold. Limitations: Assumes standard package layout; custom locations need manual adjustment.

```bash
poetry new poetry-demo
```

--------------------------------

### Add Basic Packages - Poetry

Source: https://python-poetry.org/docs/1.8/cli

Installs packages from PyPI to your project and updates pyproject.toml. Supports multiple packages at once. If no version constraint is specified, Poetry automatically selects an appropriate version based on available packages.

```shell
poetry add requests pendulum
```

--------------------------------

### Install specific Poetry version with pipx

Source: https://python-poetry.org/docs/main

Installs a particular Poetry release (e.g., 1.8.4) using pipx, allowing precise version control. Useful when projects depend on a known Poetry version. The version is provided after `==`.

```bash
pipx install poetry==1.8.4
```

--------------------------------

### Define documentation URL in pyproject.toml

Source: https://python-poetry.org/docs/1.8/pyproject

Sets the URL to the project's documentation. Optional field that directs users to comprehensive guides and API references for the project.

```toml
documentation = "https://python-poetry.org/docs/"

```

--------------------------------

### Add build dependencies using Poetry CLI

Source: https://python-poetry.org/docs/building-extension-modules

Command to add build-time dependencies to a Poetry project. This example shows adding setuptools and cython to a dedicated 'build' dependency group, making them available during the build process while keeping them separate from runtime dependencies.

```bash
poetry add --group=build setuptools cython
```

--------------------------------

### Install dependencies excluding specific groups

Source: https://python-poetry.org/docs/main/managing-dependencies

Installs all non-optional dependencies except those in the specified groups. Useful for excluding test or documentation dependencies in production environments.

```bash
poetry install --without test,docs

```

--------------------------------

### Run test suite with coverage reporting

Source: https://python-poetry.org/docs/main/contributing

Executes the test suite while collecting coverage metrics for the src/poetry package. The command reports coverage in the terminal. Requires the coverage plugin installed.

```bash
poetry run pytest --cov=src/poetry --cov-report term
```

--------------------------------

### Define console scripts in Poetry

Source: https://python-poetry.org/docs/main/pyproject

Configures console scripts that will be installed with the package. Scripts execute functions from specified modules. Requires running poetry install after adding or updating scripts.

```toml
[project.scripts]
my_package_cli = 'my_package.console:run'
```

--------------------------------

### Install parallel Poetry versions with pipx suffix

Source: https://python-poetry.org/docs/main

Installs multiple Poetry versions side‑by‑side by assigning a unique suffix to each binary. The suffix creates distinct executable names (e.g., poetry@1.8.4). Suitable for testing prereleases or different project requirements.

```bash
pipx install --suffix=@1.8.4 poetry==1.8.4
```

```bash
pipx install --suffix=@preview --pip-args=--pre poetry
```

--------------------------------

### Add Package Extras - Poetry

Source: https://python-poetry.org/docs/1.8/cli

Installs packages with optional extras that provide additional functionality. Extras are specified in square brackets after the package name and constraint.

```shell
poetry add "requests[security,socks]"
poetry add "requests[security,socks]~=2.22.0"
poetry add "git+https://github.com/pallets/flask.git@1.1.1[dotenv,dev]"
```

--------------------------------

### Configure Poetry to not re-resolve for installation

Source: https://python-poetry.org/docs/dependency-specification

Command to configure Poetry to skip dependency resolution during installation, which may be necessary for certain dependency configurations.

```Bash
poetry config installer.re-resolve false
```

--------------------------------

### Setting Python Version Constraint in pyproject.toml

Source: https://python-poetry.org/docs/basic-usage

Specify supported Python versions in pyproject.toml using the requires-python field to ensure compatibility across dependency resolution. Poetry enforces this during installation but does not install Python itself. Inputs are version constraints like '>=3.9'; outputs a validated project configuration. Limitations: User must provide a compatible Python interpreter; does not handle interpreter installation.

```toml
[project]
requires-python = ">=3.9"
```

--------------------------------

### Extras Configuration - Poetry

Source: https://python-poetry.org/docs/1.8/pyproject

Defines optional dependencies that enhance package functionality without being required for core operations. Allows grouping of optional features and conditional dependency installation.

```toml
[tool.poetry]
name = "awesome"

[tool.poetry.dependencies]
mandatory = "^1.0"
```

--------------------------------

### Specify Optional Dependencies with Extra Markers in Standard TOML

Source: https://python-poetry.org/docs/main/dependency-specification

Optional dependencies can use extra markers for conditional installation based on selected extras. Standard format uses semicolon conditions in optional-dependencies. Requires package installation with --extras flag. Input is extra names and conditions; output is extra-specific package installation. Limitations: Poetry 2.0 feature, may require re-resolve config.

```toml
[project.optional-dependencies]
paths = [
    "pathlib2 (>=2.2,<3.0) ; sys_platform == 'win32'"
]

```

--------------------------------

### Publish Poetry library to repositories

Source: https://python-poetry.org/docs/libraries

Use `poetry publish` to upload the built package to PyPI or a private repository. The command requires proper credentials and can optionally build the package before publishing with the `--build` flag. For private repositories, specify the repository name with `-r`.

```bash
poetry publish

```

```bash
poetry publish -r my-repository

```