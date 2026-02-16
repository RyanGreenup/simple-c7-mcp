### Example Installation and PATH configuration for Just

Source: https://just.systems/man/en/pre-built-binaries

This example demonstrates how to install 'just' to a local 'bin' directory, create the directory if it doesn't exist, and add the directory to the system's PATH environment variable for easy execution. This is typically added to shell initialization files like .bashrc or .zshrc.

```shell
# create ~/bin
mkdir -p ~/bin

# download and extract just to ~/bin/just
curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to ~/bin

# add `~/bin` to the paths that your shell searches for executables
# this line should be added to your shells initialization file,
# e.g. `~/.bashrc` or `~/.zshrc`
export PATH="$PATH:$HOME/bin"

# just should now be executable
just --help
```

--------------------------------

### Install 'just' using extractions/setup-just Action

Source: https://just.systems/man/en/github-actions

Installs the 'just' command-line tool on GitHub Actions using the extractions/setup-just action. Allows specifying a 'just-version' for a particular semver range, defaulting to the latest version if not provided. This action simplifies the setup process for using 'just' in CI/CD pipelines.

```yaml
- uses: extractions/setup-just@v3
  with:
    just-version: 1.5.0  # optional semver specification, otherwise latest
```

--------------------------------

### Example Just Installation to ~/bin

Source: https://just.systems/man/en/print

Demonstrates installing 'just' to the '~/bin' directory, creating the directory if it doesn't exist, and adding '~/bin' to the system's PATH environment variable for global accessibility. This ensures the 'just' command can be executed from any terminal session after restarting the shell or sourcing the initialization file.

```shell
# create ~/bin
mkdir -p ~/bin

# download and extract just to ~/bin/just
curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to ~/bin

# add `~/bin` to the paths that your shell searches for executables
# this line should be added to your shells initialization file,
# e.g. `.bashrc` or `.zshrc`
export PATH="$PATH:$HOME/bin"

# just should now be executable
just --help
```

--------------------------------

### Run Multiple Recipes - Make and Python

Source: https://just.systems/man/en/invoking-multiple-recipes

Demonstrates how to invoke multiple recipes sequentially from the command line. This example shows running a 'build' recipe (using make) followed by a 'serve' recipe (using Python's http.server). Ensure 'make' and 'python3' are installed and configured.

```makefile
build:
  make web

serve:
  python3 -m http.server -d out 8000
```

```bash
$ just build serve
make web
python3 -m http.server -d out 8000
```

--------------------------------

### Install 'just' using taiki-e/install-action

Source: https://just.systems/man/en/github-actions

Installs the 'just' command-line tool on GitHub Actions using the taiki-e/install-action. This action provides a straightforward way to include 'just' in your workflow without needing to specify versions or configurations, typically installing the latest stable release.

```yaml
- uses: taiki-e/install-action@just
```

--------------------------------

### Install Just Programmer's Manual (Linux/MacOS/Windows)

Source: https://just.systems/man/en/pre-built-binaries

This command downloads and installs the latest release of 'just' to a specified destination directory. It requires curl and bash to be installed. Replace 'DEST' with your desired directory.

```shell
curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to DEST
```

--------------------------------

### Just Recipes: Shared Setup Dependency Runs Once

Source: https://just.systems/man/en/dependencies

Shows how a common setup dependency ('build') runs only once when multiple recipes ('test-foo', 'test-bar') depend on it. This ensures that the setup process is not duplicated.

```just
build:
  cc main.c

test-foo: build
  ./a.out --test foo

test-bar: build
  ./a.out --test bar
```

```shell
$ just test-foo test-bar
cc main.c
./a.out --test foo
./a.out --test bar
```

--------------------------------

### XDG Configuration Directory Example

Source: https://just.systems/man/en/functions

An example demonstrating how to construct an XDG compliant configuration directory path using environment variables and fallback to the home directory. This ensures compatibility with applications adhering to the XDG specification.

```just
xdg_config_dir := if env('XDG_CONFIG_HOME', '') =~ '^/' {
  env('XDG_CONFIG_HOME')
} else {
  home_directory() / '.config'
}
```

--------------------------------

### Execute Justfile Recipes in PowerShell

Source: https://just.systems/man/en/indentation

Examples of executing the 'list-space' and 'list-tab' Justfile recipes from a PowerShell prompt. These examples show the command-line invocation and the expected output, demonstrating the practical use of the defined recipes.

```powershell
PS > just list-space ~
Desktop
Documents
Downloads

PS > just list-tab ~
Desktop
Documents
Downloads
```

--------------------------------

### Listing Available Recipes with Module Docs

Source: https://just.systems/man/en/print

Example output of `just --list` command, showing how module doc comments are displayed alongside the available recipes.

```bash
$ just --list
Available recipes:
    foo ... # foo is a great module!

```

--------------------------------

### Listing and Showing Recipes with Just CLI

Source: https://just.systems/man/en/print

Provides examples of using `just` command-line options to list available recipes (`--list`) and display the content of a specific recipe (`--show`). This is useful for inspecting and debugging Justfiles.

```bash
$ just --list
Available recipes:
  js
  perl
  polyglot
  python
  ruby
$ just --show perl
perl:
  #!/usr/bin/env perl
  print "Larry Wall says Hi!\n";
$ just --show polyglot
polyglot: python js perl sh ruby
```

--------------------------------

### Importing a Justfile and Running Recipes

Source: https://just.systems/man/en/imports

Demonstrates how to include another Justfile using 'import' and how recipes defined in the imported file can be executed. The example shows that recipes from the imported file are available.

```just
import 'foo/bar.just'

a: b
  @echo A

```

```just
b:
  @echo B

```

```bash
$ just b
B
$ just a
B
A

```

--------------------------------

### Pass Arguments to Recipe

Source: https://just.systems/man/en/recipe-parameters

Illustrates how to pass arguments to a 'just' recipe from the command line. The example shows the command `just build my-awesome-project` and the resulting output, demonstrating that the `target` parameter was successfully substituted.

```bash
$ just build my-awesome-project
Building my-awesome-project…
cd my-awesome-project && make
```

--------------------------------

### Install vim-just Plugin with Vim's built-in package support

Source: https://just.systems/man/en/vim-and-neovim

This snippet demonstrates installing the `vim-just` plugin using Vim's native package management system. It clones the repository into the correct directory for Vim to recognize it.

```bash
mkdir -p ~/.vim/pack/vendor/start
cd ~/.vim/pack/vendor/start
git clone https://github.com/NoahTheDuke/vim-just.git
```

--------------------------------

### Justfile: Windows Shell Configuration

Source: https://just.systems/man/en/print

Illustrates how to configure the shell for Windows. It provides examples for using `powershell.exe` and `pwsh.exe` with the appropriate flags, and recommends the use of `windows-shell` for more flexibility.

```Justfile
set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

hello:
  Write-Host "Hello, world!"
```

```Justfile
set windows-powershell := true

hello:
  Write-Host "Hello, world!"
```

--------------------------------

### Basic Justfile Structure and Execution

Source: https://just.systems/man/en/print

Illustrates the fundamental structure of a `justfile` with simple recipes and comments. It shows how to define recipes and provides an example of running `just` with no arguments, which executes the first recipe.

```makefile
recipe-name:
  echo 'This is a recipe!'

# this is a comment
another-recipe:
  @echo 'This is another recipe.'

```

```bash
$ just
echo 'This is a recipe!'
This is a recipe!

```

--------------------------------

### Make Example: Stale Rule Output

Source: https://just.systems/man/en/print

This example shows the output of running 'make test' in the context of the 'stale rule' behavior. 'make' indicates that the target 'test' is up-to-date and does not execute the recipe.

```bash
$ make test
make: `test' is up to date.

```

--------------------------------

### Justfile: Environment Variables and Recipe Execution

Source: https://just.systems/man/en/settings

Demonstrates setting environment variables and executing a recipe. The `DATABASE_ADDRESS` and `SERVER_PORT` variables are defined and used within the `serve` recipe, which starts a server. The output of the recipe execution is also shown.

```justfile
DATABASE_ADDRESS=localhost:6379
SERVER_PORT=1337

serve:
  @echo "Starting server with database $DATABASE_ADDRESS on port $SERVER_PORT…"
  ./server --database $DATABASE_ADDRESS --port $SERVER_PORT
```

--------------------------------

### Display Recipe Usage Information

Source: https://just.systems/man/en/recipe-parameters

Introduces the `--usage` subcommand to print usage information for a recipe. The example shows the output of `just --usage foo`, detailing the recipe's arguments and options.

```bash
$ just --usage foo
Usage: just foo [OPTIONS] bar

Arguments:
  bar
```

--------------------------------

### Justfile: PowerShell with Positional Arguments

Source: https://just.systems/man/en/settings

Demonstrates how to handle positional arguments in PowerShell recipes using the `-CommandWithArgs` flag with `pwsh.exe` and accesses via `$args`. Includes an example `print-args` recipe.

```justfile
__
set shell := ['pwsh.exe', '-CommandWithArgs']
set positional-arguments

print-args a b c:
  Write-Output @($args[1..($args.Count - 1)])
```

--------------------------------

### Importing Justfile (foo.just)

Source: https://just.systems/man/en/print

Example of a justfile ('foo.just') that imports another justfile ('baz.just'). This showcases nested imports and how recipes from deeper imports can be accessed.

```yaml
# foo.just
import 'baz.just'
foo: baz

```

--------------------------------

### Install vim-just Plugin with vim-plug

Source: https://just.systems/man/en/vim-and-neovim

This snippet shows how to install the `vim-just` plugin using the vim-plug package manager. This plugin provides syntax highlighting for Justfiles in Vim.

```vim
call plug#begin()

Plug 'NoahTheDuke/vim-just'

call plug#end()
```

--------------------------------

### Variadic Parameter Example with Default Value

Source: https://just.systems/man/en/print

Shows how variadic parameters can have default values, which are overridden by command-line arguments.

```just
__
test +FLAGS='-q':
  cargo test {{FLAGS}}

```

--------------------------------

### Justfile Fallback Mechanism Example

Source: https://just.systems/man/en/fallback-to-parent-justfiles

Demonstrates the fallback mechanism in justfiles. When a recipe is not found, 'just' searches parent directories until it finds a justfile with fallback disabled or reaches the root. This example shows how 'just bar' resolves a recipe from a parent justfile.

```justfile
set fallback

foo:
	echo foo

```

```justfile
bar:
	echo bar

```

```shell
$ just bar
Trying ../justfile
echo bar
bar

```

--------------------------------

### Just Recipes: Single Execution of Recipes and Dependencies

Source: https://just.systems/man/en/dependencies

Illustrates that a recipe with the same arguments runs only once, even if listed multiple times or as a dependency. The example shows that 'a' runs once, and 'b' and 'c' run once each, despite 'a' being a dependency for both.

```just
a:
  @echo A

b: a
  @echo B

c: a
  @echo C
```

```shell
$ just a a a a a
A
$ just b c
A
B
C
```

--------------------------------

### Pass Arguments to Dependency

Source: https://just.systems/man/en/recipe-parameters

Explains how to pass arguments to a dependency within a 'just' recipe. The example shows a `default` recipe depending on `build`, and how `build` receives arguments. The output is not explicitly shown but implied by the recipe structure.

```just
default: (build "main")

build target:
  @echo 'Building {{target}}…'
  cd {{target}} && make
```

--------------------------------

### List Available Recipes (Sorted by Group)

Source: https://just.systems/man/en/groups

This example shows how to use the `just --list` command to display all available recipes, sorted alphabetically within their respective groups. Recipes not assigned to any group are listed separately. This helps in understanding the structure and available commands.

```bash
$ just --list
Available recipes:
    email-everyone # not in any group

    [lint]
    cpp-lint
    js-lint
    rust-lint

    [rust recipes]
    rust-lint
```

--------------------------------

### Importing Justfile (bar.just)

Source: https://just.systems/man/en/print

Example of another justfile ('bar.just') that also imports the same shared justfile ('baz.just'). This illustrates how multiple top-level justfiles can depend on a common set of recipes.

```yaml
# bar.just
import 'baz.just'
bar: baz

```

--------------------------------

### Example: Styling an Error Message

Source: https://just.systems/man/en/print

This example shows how to use the `style` function to format an error message in the terminal. It applies the 'error' style, prints 'OH NO', and then resets the style using `NORMAL`.

```just
scary:
  @echo '{{ style("error") }}OH NO{{ NORMAL }}'
```

--------------------------------

### Integration test setup for `just` binary in Rust

Source: https://just.systems/man/en/print

This illustrates the use of the `Test` struct for integration testing the `just` binary in Rust. It allows for configuring the `justfile`, command-line arguments, and environment variables, then asserting the output, standard error, and exit code.

```rust
// Example of an integration test using the Test struct
use just::Test;

#[test]
fn test_integration_run_script() {
    Test::new()
        .justfile("default: echo hello")
        .run("default")
        .stdout("hello\n")
        .code(0);
}

#[test]
fn test_integration_unindent_in_justfile() {
    Test::new()
        .justfile("task:\n    echo \"  indented string\n  \"")
        .run("task")
        .stdout("indented string\n")
        .code(0);
}

```

--------------------------------

### Justfile: Expressions and Operators

Source: https://just.systems/man/en/print

Demonstrates the use of expressions, operators, and function calls within Justfile. It shows examples of variable assignments, string concatenation, and command execution using backticks.

```Justfile
tmpdir  := `mktemp -d`
version := "0.2.7"
tardir  := tmpdir / "awesomesauce-" + version
tarball := tardir + ".tar.gz"
config  := quote(config_dir() / ".project-config")

publish:
  rm -f {{tarball}}
  mkdir {{tardir}}
  cp README.md *.c {{ config }} {{tardir}}
  tar zcvf {{tarball}} {{tardir}}
  scp {{tarball}} me@server.com:release/
  rm -rf {{tarball}} {{tardir}}
```

```Justfile
foobar := 'foo' + 'bar'
```

--------------------------------

### While Loops in Justfile Recipes

Source: https://just.systems/man/en/multi-line-constructs

Provides examples of implementing 'while' loops in Justfile recipes. It covers single-line loops, multi-line loops using escaped newlines, and multi-line loops with a shebang for consistent execution.

```just
while:
  while `server-is-dead`; do ping -c 1 server; done

```

```just
while:
  while `server-is-dead`; do \
    ping -c 1 server; \
  done

```

```just
while:
  #!/usr/bin/env sh
  while `server-is-dead`; do
    ping -c 1 server
  done

```

--------------------------------

### Executing Virtual Environment Binaries Directly

Source: https://just.systems/man/en/print

Provides a workaround for tools like Python's venv that require environment variable loading. This example shows how to execute virtual environment binaries directly by specifying their path.

```shell
[ -d foo ] || python3 -m venv foo

run: venv
  ./foo/bin/python3 main.py
```

--------------------------------

### Make Example: 'make' refuses to run recipe when target file exists

Source: https://just.systems/man/en/what-are-the-idiosyncrasies-of-make-that-just-avoids

This example demonstrates how 'make' assumes a recipe will produce a file matching the target name. If the file exists and there are no other dependencies, 'make' will not execute the recipe, considering it up-to-date. This behavior is undesirable when 'make' is used as a command runner.

```makefile
test:
  ./test
```

```shell
$ make test
make: `test' is up to date.
```

--------------------------------

### Get Concise Recipe Summary with `just --summary`

Source: https://just.systems/man/en/print

Provides a concise summary of all available recipes, listed on a single line. This is a more compact way to view available tasks compared to `just --list`.

```bash
$ just --summary
build test deploy lint

```

--------------------------------

### List Available Recipes as Default

Source: https://just.systems/man/en/the-default-recipe

If no single recipe makes sense as the default, this example shows how to add a 'default' recipe that lists all available recipes using the 'just --list' command.

```just
default:
  just --list
```

--------------------------------

### Dependency Deduplication in Justfile

Source: https://just.systems/man/en/print

Explains that a recipe with the same arguments runs only once per invocation, even if listed multiple times or as a dependency of multiple recipes. This ensures setup tasks run only once.

```shell
$ just a a a a a
A
```

```shell
$ just b c
A
B
C
```

```justfile
a:
  @echo A

b: a
  @echo B

c: a
  @echo C
```

```justfile
build:
  cc main.c

test-foo: build
  ./a.out --test foo

test-bar: build
  ./a.out --test bar
```

```shell
$ just test-foo test-bar
cc main.c
./a.out --test foo
./a.out --test bar
```

```justfile
build:
  cc main.c

test TEST: build
  ./a.out --test {{TEST}}
```

```shell
$ just test foo test bar
cc main.c
./a.out --test foo
./a.out --test bar
```

--------------------------------

### Re-run Recipe on File Change with Watchexec

Source: https://just.systems/man/en/print

This snippet demonstrates how to use `watchexec` to automatically re-run a Just recipe when any file in the project changes. Ensure `watchexec` is installed and configured to watch your project files.

```shell
watchexec just foo
```

--------------------------------

### List Recipe Groups

Source: https://just.systems/man/en/groups

This example illustrates the `just --groups` command, which lists all the unique recipe groups defined in the Justfile. The groups are listed alphabetically. This command helps in understanding the categorization of recipes.

```bash
$ just --groups
Recipe groups:
  lint
  rust recipes
```

--------------------------------

### Running Tests with `cargo-watch` in Rust

Source: https://just.systems/man/en/print

This snippet demonstrates how to use `cargo-watch` to automatically re-run tests when code changes. It's a recommended workflow for developing new features for the 'just' project. Ensure `cargo-watch` is installed via `cargo install cargo-watch`.

```shell
just watch test
```

--------------------------------

### Executable and Process Information

Source: https://just.systems/man/en/print

Functions to get information about the `just` executable and its process.

```APIDOC
## Executable and Process Information

### Description
Functions to get information about the `just` executable and its process.

### Functions

- **`just_executable()`**
  - Retrieves the absolute path to the `just` executable.

  **Example Usage:**
  ```just
  executable:
    @echo The executable is at: {{just_executable()}}
  ```
  **Example Output:**
  ```
  $ just
  The executable is at: /bin/just
  ```

- **`just_pid()`**
  - Retrieves the Process ID (PID) of the `just` executable.

  **Example Usage:**
  ```just
  pid:
    @echo The process ID is: {{ just_pid() }}
  ```
  **Example Output:**
  ```
  $ just
  The process ID is: 420
  ```

```

--------------------------------

### Justfile Example: Using Operators and Function Calls

Source: https://just.systems/man/en/expressions-and-substitutions

Demonstrates the usage of various operators like assignment, string concatenation, and path joining within a Justfile. It includes defining variables, creating directories, copying files, and publishing artifacts. Dependencies include standard shell utilities and Just's internal functions like `mktemp`, `config_dir`, and `quote`.

```justfile
tmpdir  := `mktemp -d`
version := "0.2.7"
tardir  := tmpdir / "awesomesauce-" + version
tarball := tardir + ".tar.gz"
config  := quote(config_dir() / ".project-config")

publish:
  rm -f {{tarball}}
  mkdir {{tardir}}
  cp README.md *.c {{ config }} {{tardir}}
  tar zcvf {{tarball}} {{tardir}}
  scp {{tarball}} me@server.com:release/
  rm -rf {{tarball}} {{tardir}}
```

--------------------------------

### Justfile: Export Variables

Source: https://just.systems/man/en/settings

The `set export` setting exports all just variables as environment variables. The example shows how a variable `a` can be used within a recipe.

```justfile
__
set dotenv-load

serve:
  @echo "Starting server with database $DATABASE_ADDRESS on port $SERVER_PORT…"
  ./server --database $DATABASE_ADDRESS --port $SERVER_PORT
```

--------------------------------

### Customize Just Recipe Alias Working Directory

Source: https://just.systems/man/en/print

This example demonstrates how to customize the working directory for the '.j' alias to the user's home directory instead of the current directory. This is useful for recipes that operate on files relative to the home directory.

```shell
alias .j='just --justfile ~/.user.justfile --working-directory ~'
```

--------------------------------

### Shell Command Execution in Recipes (Makefile/Just)

Source: https://just.systems/man/en/changing-the-working-directory-in-a-recipe

Demonstrates how shell commands are executed in recipes. By default, each line is a new shell, so directory changes are not persistent. Examples show workarounds using `cd` on the same line or employing shebang recipes for script-like behavior.

```makefile
foo:
  pwd    # This `pwd` will print the same directory…
  cd bar
  pwd    # …as this `pwd`!
```

```makefile
foo:
  cd bar && pwd
```

```makefile
foo:
  #!/usr/bin/env bash
  set -euxo pipefail
  cd bar
  pwd
```

--------------------------------

### For Loops in Justfile Recipes

Source: https://just.systems/man/en/multi-line-constructs

Illustrates different methods for creating 'for' loops in Justfile recipes. Examples include single-line loops, multi-line loops with escaped newlines, and multi-line loops using a shebang for predictable behavior.

```just
for:
  for file in `ls .`; do echo $file; done

```

```just
for:
  for file in `ls .`; do \
    echo $file; \
  done

```

```just
for:
  #!/usr/bin/env sh
  for file in `ls .`; do
    echo $file
  done

```

--------------------------------

### Get Just Executable Path

Source: https://just.systems/man/en/print

Retrieves the absolute path to the `just` executable. This can be used to reference the `just` binary itself within recipes.

```just
@echo The executable is at: {{just_executable()}}
```

--------------------------------

### Get Invocation Directory Path

Source: https://just.systems/man/en/print

Retrieves the absolute path to the directory where the `just` command was invoked. This is useful for referencing files relative to the user's starting point, before `just` changes the current directory. On Windows, it's converted to a Cygwin-compatible path.

```just
find {{invocation_directory()}} -name \*.rs -exec rustfmt {} \;
```

```just
cd {{invocation_directory()}}; ./some_script_that_needs_to_be_run_from_here
```

--------------------------------

### Justfile: Positional Arguments

Source: https://just.systems/man/en/settings

Explains the use of positional arguments in recipes.  When `positional-arguments` is set to `true`, recipe arguments can be accessed using `$0`, `$1`, etc.  The example shows using the arguments.

```justfile
__
set export

a := "hello"

@foo b:
  echo $a
  echo $b
```

```shell
$ just foo goodbye
hello
goodbye
```

--------------------------------

### Bash Shebang Recipe with `set -euxo pipefail`

Source: https://just.systems/man/en/print

Provides an example of a Bash shebang recipe that includes `set -euxo pipefail` for enhanced error handling and debugging, making it behave more like standard 'just' recipes.

```bash
#!/usr/bin/env bash
set -euxo pipefail
hello='Yo'
echo "$hello from Bash!"
```

--------------------------------

### Justfile: Positional Arguments with Bash, Iteration

Source: https://just.systems/man/en/settings

Shows how to pass and process positional arguments in a Justfile recipe using Bash. The example uses a Bash `while` loop to iterate through the arguments provided to the recipe.

```justfile
__
set positional-arguments

@test *args='':
  bash -c 'while (( "$#" )); do echo - $1; shift; done' -- "$@"
```

```shell
$ just test foo "bar baz"
- foo
- bar baz
```

--------------------------------

### Justfile: Setting the Shell

Source: https://just.systems/man/en/settings

Explains how to configure the shell used to execute recipe lines. The default shell is `sh -cu`. Examples show how to change the shell to Python, Bash, Zsh, Fish, NuShell, and PowerShell on Windows.

```justfile
__
# use python3 to execute recipe lines and backticks
set shell := ["python3", "-c"]

# use print to capture result of evaluation
foos := `print("foo" * 4)`

foo:
  print("Snake snake snake snake.")
  print("{{foos}}")
```

--------------------------------

### Concurrent Recipe Execution with GNU Parallel

Source: https://just.systems/man/en/parallelism

Shows how to use GNU `parallel` to execute recipe lines concurrently within a justfile. This example configures GNU parallel to use the number of available CPUs and runs four tasks, each with a sleep duration, demonstrating parallel task execution. The `--shebang`, `--ungroup`, and `--jobs` flags are used for robust parallel execution.

```justfile
parallel:
  #!/usr/bin/env -S parallel --shebang --ungroup --jobs {{ num_cpus() }}
  echo task 1 start; sleep 3; echo task 1 done
  echo task 2 start; sleep 3; echo task 2 done
  echo task 3 start; sleep 3; echo task 3 done
  echo task 4 start; sleep 3; echo task 4 done

```

--------------------------------

### Execute echo command

Source: https://just.systems/man/en/paths-on-windows

This snippet demonstrates how to execute an 'echo' command to display the absolute path of the current directory. It's a basic example of command execution within the Just system.

```just
ls:
    echo '{{absolute_path(".")}}'
```

--------------------------------

### Get System Architecture (Just)

Source: https://just.systems/man/en/print

The `arch()` function returns the instruction set architecture of the system. It can be used within recipe body substitutions to display system information.

```just
system-info:
  @echo "This is an {{arch()}} machine"
```

--------------------------------

### Long Option Parameters in Justfile

Source: https://just.systems/man/en/print

Explains how to make recipe parameters into long options using the `[arg(ARG, long=OPTION)]` attribute. The example shows 'bar' being passed via `--bar`.

```justfile
[arg("bar", long="bar")]
foo bar:
```

```shell
$ just foo --bar hello
bar=hello
```

```shell
$ just foo --bar=hello
bar=hello
```

```justfile
[arg("bar", long)]
foo bar:
```

--------------------------------

### Recipe Parameter with Default Value

Source: https://just.systems/man/en/recipe-parameters

Illustrates how to assign a default value to a recipe parameter. The `test` recipe has a `target` parameter and a `tests` parameter defaulting to 'all'. The example output shows the default value being used when no explicit argument is provided.

```just
default := 'all'

test target tests=default:
  @echo 'Testing {{target}}:{{tests}}…'
  ./test --tests {{tests}} {{target}}
```

--------------------------------

### Run the first recipe with 'just'

Source: https://just.systems/man/en/quick-start

Demonstrates how to execute the first defined recipe in a 'justfile' by running the 'just' command without any arguments. The output shows the command being executed and its result.

```bash
$ just
echo 'This is a recipe!'
This is a recipe!

```

--------------------------------

### Justfile: Positional Arguments with Bash/Zsh

Source: https://just.systems/man/en/print

Demonstrates how to pass arguments to recipes as positional arguments using `bash` or `zsh`. `$0` represents the recipe name, and `$1`, `$2`, etc., represent the arguments. The example shows how to iterate through arguments using a `while` loop within `bash`.

```Justfile
set positional-arguments

@foo bar:
  echo $0
  echo $1
```

```Bash
just foo hello
```

```Justfile
set positional-arguments

@test *args='':
  bash -c 'while (( "$#" )); do echo - $1; shift; done' -- "$@"
```

```Bash
just test foo "bar baz"
```

--------------------------------

### Basic Bash Shebang for 'echo' Command - Just Recipe

Source: https://just.systems/man/en/safer-bash-shebang-recipes

A simple bash shebang recipe that executes an 'echo' command. This example illustrates a basic script structure where the interpreter path might be translated on Windows.

```bash
#!/bin/sh
echo "Hello!"

```

--------------------------------

### Get System Information with arch() and os() Functions

Source: https://just.systems/man/en/functions

Demonstrates how to use the `arch()` and `os()` functions to retrieve the system's instruction set architecture and operating system, respectively. These functions are useful for conditional logic within 'justfile' recipes.

```just
system-info:
  @echo "This is an {{arch()}} machine".
```

--------------------------------

### Configuring Just to Use cmd.exe on Windows

Source: https://just.systems/man/en/print

Illustrates how to configure 'just' to use 'cmd.exe' as its shell on Windows. Similar to the PowerShell example, this involves setting the 'shell' directive to 'cmd.exe' with the '/c' argument. A sample recipe demonstrates using the 'dir' command in 'cmd.exe'.

```batch
# use cmd.exe instead of sh:
set shell := ["cmd.exe", "/c"]

list:
  dir
```

--------------------------------

### Default Values with Complex Expressions

Source: https://just.systems/man/en/recipe-parameters

Explains that default values can be arbitrary expressions. Expressions using `+`, `&&`, `||`, or `/` must be parenthesized. The example defines `arch` and uses it to construct default values for `triple` and `input` parameters.

```just
arch := "wasm"

test triple=(arch + "-unknown-unknown") input=(arch / "input.dat"):
  ./test {{triple}}
```

--------------------------------

### Run Python Scripts with uv using [script]

Source: https://just.systems/man/en/python-recipes-with-uv

Configures 'just' to use 'uv' for running Python scripts via the '[script]' attribute and 'script-interpreter' setting. Supports direct execution and dependency management. Requires 'uv' to be installed.

```justfile
set unstable

set script-interpreter := ['uv', 'run', '--script']

[script]
hello:
  print("Hello from Python!")

[script]
goodbye:
  # /// script
  # requires-python = ">=3.11"
  # dependencies=["sh"]
  # ///
  import sh
  print(sh.echo("Goodbye from Python!"), end='')

```

--------------------------------

### Create Shell Aliases for Just Recipes

Source: https://just.systems/man/en/print

This script iterates through recipes defined in a specified justfile and creates shell aliases for each. This allows recipes to be called directly as commands. It requires the 'just' command-line tool to be installed and accessible.

```shell
for recipe in `just --justfile ~/.user.justfile --summary`; do
  alias $recipe="just --justfile ~/.user.justfile --working-directory . $recipe"
done
```

--------------------------------

### Hide Private Recipes with Underscore Prefix (Justfile)

Source: https://just.systems/man/en/private-recipes

Example Justfile content showing a 'test' recipe and a '_test-helper' alias. The '_test-helper' is not listed by 'just --list' or 'just --summary' due to its leading underscore.

```justfile
test: _test-helper
  ./bin/test

_test-helper:
  ./bin/super-secret-test-helper-stuff

```

--------------------------------

### Just Recipes: Prior and Subsequent Dependencies

Source: https://just.systems/man/en/dependencies

Explains and demonstrates 'prior dependencies' (default, run before) and 'subsequent dependencies' (run after, prefixed with '&&'). Recipe 'b' has prior dependency 'a' and subsequent dependencies 'c' and 'd'. The output shows 'A', then 'B', then 'C' and 'D'.

```just
a:
  echo 'A!'

b: a && c d
  echo 'B!'

c:
  echo 'C!'

d:
  echo 'D!'
```

```shell
$ just b
echo 'A!'
A!
echo 'B!'
B!
echo 'C!'
C!
echo 'D!'
D!
```

--------------------------------

### Default Recipe Execution in Just

Source: https://just.systems/man/en/print

Explains how `just` determines which recipe to run when invoked without arguments. It prioritizes a recipe with the `[default]` attribute or, failing that, the first recipe in the `justfile`. Examples include a single default recipe and a default recipe that depends on multiple other recipes.

```makefile
test:
  cargo test

```

```makefile
default: lint build test

build:
  echo Building…

test:
  echo Testing…

lint:
  echo Linting…

```

```makefile
default:
  just --list

```

--------------------------------

### Define Recipes with Groups (Justfile Syntax)

Source: https://just.systems/man/en/groups

This snippet demonstrates how to define recipes within a Justfile, annotating them with group names using the `[group('group_name')]` syntax. Recipes can belong to multiple groups. It shows examples for JavaScript linting, Rust linting, C++ linting, and a general email recipe.

```justfile
[group('lint')]
js-lint:
    echo 'Running JS linter…'

[group('rust recipes')]
[group('lint')]
rust-lint:
    echo 'Running Rust linter…'

[group('lint')]
cpp-lint:
  echo 'Running C++ linter…'

# not in any group
email-everyone:
    echo 'Sending mass email…'
```

--------------------------------

### Basic Argument Handling with Justfile

Source: https://just.systems/man/en/avoiding-argument-splitting

Demonstrates a basic Justfile recipe that accepts an argument and uses it with the `touch` command. It highlights the potential issue of argument splitting when quotes are not preserved.

```justfile
foo argument:
  touch {{argument}}
```

--------------------------------

### Ensuring Code Quality with `just ci`

Source: https://just.systems/man/en/print

The `just ci` command is used to verify that all tests, linters, and checks pass before submitting code. This ensures code quality and adherence to project standards. This command requires mdBook and mdbook-linkcheck to be installed.

```shell
just ci
```

--------------------------------

### Make Example: Stale Rule Behavior

Source: https://just.systems/man/en/print

This code snippet demonstrates a scenario in 'make' where a recipe is not executed because 'make' believes the target file is up-to-date. This highlights 'make's build system-oriented behavior, which can be problematic for general command running.

```makefile
test:
  ./test

```

--------------------------------

### Get Just Process ID

Source: https://just.systems/man/en/print

Retrieves the process ID (PID) of the running `just` executable. This can be useful for logging or inter-process communication.

```just
@echo The process ID is: {{ just_pid() }}
```

--------------------------------

### Recipe Usage Information

Source: https://just.systems/man/en/print

Demonstrates how to obtain usage information for a recipe using the `--usage` subcommand, which displays available arguments and their descriptions.

```bash
__
$ just --usage foo
Usage: just foo [OPTIONS] bar

Arguments:
  bar

```

--------------------------------

### Run Default Recipe with Cargo Test

Source: https://just.systems/man/en/the-default-recipe

When 'just' is invoked without a recipe, it runs the recipe with the '[default]' attribute or the first recipe in the 'justfile'. This example shows how to set a 'test' recipe as the default using Cargo.

```just
test:
  cargo test
```

--------------------------------

### Configure Zsh for Homebrew Completion Scripts

Source: https://just.systems/man/en/shell-completion-scripts

This Zsh configuration snippet initializes Homebrew environment variables, updates the `fpath` to include Homebrew's Zsh site-functions directory, and optionally initializes Oh My Zsh or runs `compinit` manually. This allows Zsh to recognize completion scripts installed by Homebrew packages, including `just`.

```zsh
# Init Homebrew, which adds environment variables
eval "$(brew shellenv)"

fpath=($HOMEBREW_PREFIX/share/zsh/site-functions $fpath)

# Then choose one of these options:
# 1. If you're using Oh My Zsh, you can initialize it here
# source $ZSH/oh-my-zsh.sh

# 2. Otherwise, run compinit yourself
# autoload -U compinit
# compinit

```

--------------------------------

### View Just Man Page with Groff

Source: https://just.systems/man/en/print

This command shows how to view the Just man page in plain text format. It pipes the output of `just --man` to `groff` for rendering and then pipes the result to `less` for paginated viewing in the terminal. This requires `groff` to be installed on the system.

```shell
just --man | groff -mandoc -Tascii | less

```

--------------------------------

### Configuring Just to Use PowerShell on Windows

Source: https://just.systems/man/en/print

Shows how to configure 'just' to use PowerShell as its shell on Windows instead of the default 'sh'. This involves setting the 'shell' directive in the 'justfile' to 'powershell.exe' and providing the necessary arguments. It includes an example recipe that uses PowerShell's 'Write-Host' command.

```powershell
# use PowerShell instead of sh:
set shell := ["powershell.exe", "-c"]

hello:
  Write-Host "Hello, world!"
```

--------------------------------

### Run Multiple Recipes by Default with Dependencies

Source: https://just.systems/man/en/the-default-recipe

Demonstrates how to use dependencies to run multiple recipes sequentially by default. The 'default' recipe depends on 'lint', 'build', and 'test', ensuring they are executed in order.

```just
default: lint build test

build:
  echo Building…

test:
  echo Testing…

lint:
  echo Linting…
```

--------------------------------

### Get Just Executable Path

Source: https://just.systems/man/en/functions

Returns the absolute path to the `just` executable. This is useful for explicitly referencing the `just` binary in scripts or commands.

```justfile
__
executable:
  @echo The executable is at: {{just_executable()}}
```

--------------------------------

### Execute Shell Commands with shell() Function

Source: https://just.systems/man/en/functions

Illustrates the usage of the `shell(command, args...)` function to execute shell commands and capture their standard output. It shows how to pass arguments, use variables for commands, and handle cases where arguments are missing. The example also demonstrates setting a custom shell interpreter.

```just
# arguments can be variables or expressions
file := '/sys/class/power_supply/BAT0/status'
bat0stat := shell('cat $1', file)

# commands can be variables or expressions
command := 'wc -l'
output := shell(command + ' "$1"', 'main.c')

# arguments referenced by the shell command must be used
empty := shell('echo', 'foo')
full := shell('echo $1', 'foo')
error := shell('echo $1')
```

```just
# Using python as the shell. Since `python -c` sets `sys.argv[0]` to `'-c'`,
# the first "real" positional argument will be `sys.argv[2]`.
set shell := ["python3", "-c"]
olleh := shell('import sys; print(sys.argv[2][::-1])', 'hello')
```

--------------------------------

### Invert Recipe Meaning with '@' Prefix

Source: https://just.systems/man/en/quiet-recipes

Demonstrates how prefixing a recipe name with '@' in a Justfile inverts the meaning of '@' before each line. Normally, '@' echoes the command before execution. With '@' prefix on the recipe, only lines starting with '@' are echoed.

```makefile
@quiet:
  echo hello
  echo goodbye
  @# all done!

$ just quiet
hello
goodbye
# all done!
```

--------------------------------

### Get Just Process ID

Source: https://just.systems/man/en/functions

Retrieves the process ID (PID) of the running `just` executable. This can be helpful for process management or logging purposes.

```justfile
__
pid:
  @echo The process ID is: {{ just_pid() }}
```

--------------------------------

### Just List Command Output

Source: https://just.systems/man/en/documentation-comments

Demonstrates the output of the `just --list` command, showing available recipes and their associated documentation comments.

```bash
$ just --list
Available recipes:
    build # build stuff
    test # test stuff
```

--------------------------------

### Verify Just Programmer's Manual Release Integrity

Source: https://just.systems/man/en/pre-built-binaries

This command verifies the integrity of downloaded pre-built binary archives using the SHA256SUMS file. It requires the 'shasum' utility (available on most Unix-like systems) and the SHA256SUMS file to be present in the current directory.

```shell
shasum --algorithm 256 --ignore-missing --check SHA256SUMS
```

--------------------------------

### Get Justfile Path and Directory

Source: https://just.systems/man/en/print

Retrieves the path of the current `justfile` and its parent directory. This is useful for running commands or accessing scripts located relative to the `justfile` itself.

```just
{{justfile_directory()}}/scripts/some_script
```

--------------------------------

### Usage Information with Help Strings

Source: https://just.systems/man/en/recipe-parameters

Shows the output of `just --usage foo` after help strings have been added to arguments. The 'bar' argument now displays its associated help text 'hello' in the usage information.

```bash
$ just --usage foo
Usage: just foo bar

Arguments:
  bar hello
```

--------------------------------

### Hide Private Recipes with [private] Attribute (Justfile)

Source: https://just.systems/man/en/private-recipes

Example Justfile content using the '[private]' attribute to hide the 'foo' recipe and the 'b' alias, which is an alias for the 'bar' recipe. Only 'bar' is visible.

```justfile
[private]
foo:

[private]
alias b := bar

bar:

```

--------------------------------

### Variadic Parameter Expansion (One or More)

Source: https://just.systems/man/en/recipe-parameters

Demonstrates the expansion of a variadic parameter (`+FILES`) when multiple arguments are provided. The `just backup FAQ.md GRAMMAR.md` command results in `scp FAQ.md GRAMMAR.md me@server.com:`, showing the files listed.

```bash
$ just backup FAQ.md GRAMMAR.md
scp FAQ.md GRAMMAR.md me@server.com:
FAQ.md                  100% 1831     1.8KB/s   00:00
GRAMMAR.md              100% 1666     1.6KB/s   00:00
```

--------------------------------

### Customize User Justfile Alias with Working Directory (Shell Script)

Source: https://just.systems/man/en/global-and-user-justfiles

This example demonstrates customizing the single alias for a user justfile to execute recipes from a specific directory, such as the user's home directory, instead of the current working directory. This allows for consistent execution environments for user-defined tasks. Requires the 'just' command-line tool.

```shell
alias .j='just --justfile ~/.user.justfile --working-directory ~'

```

--------------------------------

### Running `unindent` function tests in Rust

Source: https://just.systems/man/en/print

This example shows how unit tests for the `unindent` function are typically written in Rust. These tests live alongside the code being tested and focus on isolating specific functionality, like handling edge cases in triple-quoted strings.

```rust
// Example of a unit test for the unindent function
#[test]
fn test_unindent_simple() {
    let input = "  hello\n    world\n  ";
    let expected = "hello\n  world\n";
    assert_eq!(unindent(input), expected);
}

#[test]
fn test_unindent_empty() {
    let input = "";
    let expected = "";
    assert_eq!(unindent(input), expected);
}

#[test]
fn test_unindent_no_indent() {
    let input = "hello\nworld";
    let expected = "hello\nworld";
    assert_eq!(unindent(input), expected);
}

```

--------------------------------

### Find Executable Paths with which() Function (Unstable)

Source: https://just.systems/man/en/functions

Illustrates the `which(name)` function, which searches the PATH for an executable and returns its full path or an empty string if not found. This function is currently unstable. The example shows retrieving the path for 'bosh'.

```just
set unstable

bosh := which("bosh")

@test:
    echo "bosh: '{{bosh}}'"
```

--------------------------------

### Convert Paths using cygpath.exe

Source: https://just.systems/man/en/paths-on-windows

This snippet shows how to use the `cygpath.exe` utility to convert file paths between Unix-style and Windows-style formats. It's useful for cross-platform compatibility when working with file paths.

```just
foo_unix := '/hello/world'
foo_windows := shell('cygpath --windows $1', foo_unix)

bar_windows := 'C:\hello\world'
bar_unix := shell('cygpath --unix $1', bar_windows)
```

--------------------------------

### Continue Execution After Failed Command (Shell)

Source: https://just.systems/man/en/ignoring-errors

This example demonstrates how to use the '-' prefix to continue script execution even if a command fails. The `cat foo` command is expected to fail because 'foo' does not exist, but the script proceeds to `echo 'Done!'`.

```shell
-cat foo
echo 'Done!'
```

```shell
$ just foo
cat foo
cat: foo: No such file or directory
echo 'Done!'
Done!
```

--------------------------------

### Indented Backticks for Command Execution

Source: https://just.systems/man/en/command-evaluation-using-backticks

This example shows how indented triple backticks (```) can be used to execute multi-line shell commands and store the de-indented output in a variable. The commands `echo foo` and `echo bar` are executed.

```Just
stuff := ```
    echo foo
    echo bar
  ```
```

--------------------------------

### Python Recipes with `uv` using `[script]`

Source: https://just.systems/man/en/print

Shows how to configure 'just' to run Python recipes using the `uv` package manager with the `[script]` attribute and `script-interpreter` setting.

```toml
set unstable

set script-interpreter := ['uv', 'run', '--script']

[script]
hello:
  print("Hello from Python!")

[script]
goodbye:
  # /// script
  # requires-python = ">=3.11"
  # dependencies=["sh"]
  # ///
  import sh
  print(sh.echo("Goodbye from Python!"), end='')
```

--------------------------------

### Quoting Substitutions with Spaces

Source: https://just.systems/man/en/recipe-parameters

Highlights the need for quoting substitutions (`{{...}}`) if they might contain spaces to prevent shell parsing issues. The example shows an incorrect command without quotes and the corrected version using single quotes around the URL.

```just
search QUERY:
  lynx 'https://www.google.com/?q={{QUERY}}'
```

--------------------------------

### Recipe with a Single Parameter

Source: https://just.systems/man/en/print

Demonstrates a simple recipe 'build' that accepts a 'target' parameter to specify the project to build. The parameter is used within the recipe's commands.

```just
__
build target:
  @echo 'Building {{target}}…'
  cd {{target}} && make

```

--------------------------------

### Find Executable Paths with require() Function

Source: https://just.systems/man/en/functions

Demonstrates the use of the `require(name)` function to find the full path of an executable in the system's PATH. If the executable is not found, the function halts with an error. An example shows retrieving the path for 'bash'.

```just
bash := require("bash")

@test:
    echo "bash: '{{bash}}'"
```