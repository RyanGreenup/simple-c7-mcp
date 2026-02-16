### Example Installation Command for Custom CLI

Source: https://docs.deno.com/runtime/reference/cli/install

Provides an example of how to instruct users on installing a custom CLI tool using 'deno install', including specifying a custom executable name.

```bash
# Install using deno install

$ deno install -n awesome_cli https://example.com/awesome/cli.ts

```

--------------------------------

### Test Deno Installation

Source: https://docs.deno.com/runtime/getting_started/installation

Verifies that Deno has been installed correctly by checking its version and displaying help information.

```bash
deno --version
deno help
```

--------------------------------

### Upgrade Deno Installation

Source: https://docs.deno.com/runtime/getting_started/installation

Updates an existing Deno installation to the latest stable version. Also shows how to upgrade using Winget and how to install a specific version.

```bash
deno upgrade
winget upgrade DenoLand.Deno
den o upgrade --version 1.0.1
```

--------------------------------

### Deno CI Pipeline Setup (GitHub Actions)

Source: https://docs.deno.com/runtime/reference/continuous_integration

This snippet shows the basic setup for a Deno CI pipeline using GitHub Actions. It checks out the repository and installs a specified Deno version. This is a foundational step for any Deno CI process.

```yaml
name: Build

on: push

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: denoland/setup-deno@v2
        with:
          deno-version: v2.x # Run with latest stable Deno.

```

--------------------------------

### Build and Install Deno from Source

Source: https://docs.deno.com/runtime/getting_started/installation

Builds and installs Deno from its source code using Cargo, the Rust package manager. Assumes Rust and Cargo are already installed.

```bash
cargo install deno --locked
```

--------------------------------

### Install Deno using PowerShell (Windows)

Source: https://docs.deno.com/runtime/getting_started/installation

Installs Deno on Windows using a PowerShell command to download and execute an installation script. Recommended for better performance.

```powershell
irm https://deno.land/install.ps1 | iex
```

--------------------------------

### Install Deno using Shell Script

Source: https://docs.deno.com/runtime/getting_started/installation

Installs Deno using a curl command to download and execute an installation script. This is the recommended method for better performance compared to npm installation.

```shell
curl -fsSL https://deno.land/install.sh | sh
```

--------------------------------

### Install Deno using Nix

Source: https://docs.deno.com/runtime/getting_started/installation

Installs Deno using the Nix package manager, providing a reproducible environment.

```bash
nix-shell -p deno
```

--------------------------------

### Install Deno using Winget (Windows)

Source: https://docs.deno.com/runtime/getting_started/installation

Installs Deno on Windows using the Winget package manager.

```powershell
winget install DenoLand.Deno
```

--------------------------------

### Install Global Deno Package or Script

Source: https://docs.deno.com/runtime/reference/cli/install

Installs a specified package or script as a globally available binary. Creates a shell script that invokes 'deno' with given flags. Executable name is inferred from URL or can be set with --name. Installation root can be set with --root or DENO_INSTALL_ROOT. Permissions must be specified.

```bash
$ deno install --global --allow-net --allow-read jsr:@std/http/file-server
Download jsr:@std/http/file-server...

✅ Successfully installed file-server.
/Users/deno/.deno/bin/file-server

```

```bash
deno install -g -N -R -n serve jsr:@std/http/file-server

```

```bash
deno install -g -N -R --root /usr/local/bin jsr:@std/http/file-server

```

```bash
echo 'export PATH="$HOME/.deno/bin:$PATH"' >> ~/.bashrc

```

```bash
deno install -g -N -R jsr:@std/http/file-server -- -p 8080

```

--------------------------------

### Install Deno using Scoop (Windows)

Source: https://docs.deno.com/runtime/getting_started/installation

Installs Deno on Windows using the Scoop package manager.

```bash
scoop install deno
```

--------------------------------

### Install Deno using npm

Source: https://docs.deno.com/runtime/getting_started/installation

Installs Deno globally using the npm package manager. Note that this method may affect Deno's startup time.

```bash
npm install -g deno
```

--------------------------------

### Basic CLI Bundle Example

Source: https://docs.deno.com/runtime/reference/bundling

This example demonstrates the basic usage of the `deno bundle` command to create a single JavaScript file from a TypeScript entrypoint. It shows how to redirect the output to a file and how to execute the bundled file.

```typescript
import chalk from "npm:chalk";

console.log(chalk.red("Hello from `deno bundle`!"));

```

```shell
$ deno bundle main.ts > bundle.js

# Or with an explicit output file:

$ deno bundle -o bundle.js main.ts

```

```shell
$ deno bundle.js
Hello from `deno bundle`!

```

--------------------------------

### Deno OpenTelemetry API Import Example

Source: https://docs.deno.com/runtime/fundamentals/open_telemetry

Demonstrates how to import modules from the installed OpenTelemetry API package in Deno. It shows direct import from the registry or from a locally installed package.

```typescript
// Import directly from registry
import { metrics, trace } from "npm:@opentelemetry/api@1";

// Or import from a locally installed package
// import { metrics, trace } from "@opentelemetry/api";

const meter = metrics.getMeter("my-app", "1.0.0");
const tracer = trace.getTracer("my-app", "1.0.0");

console.log(meter);
console.log(tracer);
```

--------------------------------

### Create and Run a Vite App with Deno

Source: https://docs.deno.com/runtime/fundamentals/web_dev

This snippet shows the steps to create a new Vite application, a modern build tool, and prepare it for use with Deno. It involves using `create-vite` and then running `deno install` and `deno task dev` to set up and start the development server.

```bash
deno run -A npm:create-vite@latest
cd my-vite-app
deno install
deno task dev
```

--------------------------------

### Deno Deploy Cloud Integration Examples

Source: https://docs.deno.com/runtime/reference/cli/deploy

Provides examples for setting up cloud integrations, specifically AWS and GCP, within Deno Deploy applications. These commands facilitate connecting external cloud services.

```bash
# Set up AWS integration
deno deploy setup-aws --org my-company --app my-api

# Set up GCP integration
deno deploy setup-gcp --org my-company --app my-api

```

--------------------------------

### Runtime API Bundle Example

Source: https://docs.deno.com/runtime/reference/bundling

This example shows how to use the `Deno.bundle()` runtime API to programmatically bundle your code. It demonstrates basic usage with specified entrypoints, output directory, platform, and minification.

```typescript
const result = await Deno.bundle({
  entrypoints: ["./index.tsx"],
  outputDir: "dist",
  platform: "browser",
  minify: true,
});
console.log(result);

```

--------------------------------

### Uninstall Deno Dependency or Binary

Source: https://docs.deno.com/runtime/reference/cli/install

Illustrates how to use the 'deno uninstall' command to remove installed dependencies or globally available binary scripts. It shows examples for uninstalling by package name and by global executable name.

```bash
$ deno uninstall express
Removed express

```

```bash
$ deno uninstall -g file-server
deleted /Users/deno/.deno/bin/file-server
✅ Successfully uninstalled file-server

```

--------------------------------

### Install Deno using Homebrew

Source: https://docs.deno.com/runtime/getting_started/installation

Installs Deno on macOS using the Homebrew package manager.

```bash
brew install deno
```

--------------------------------

### Example deno.json Configuration File

Source: https://docs.deno.com/runtime/fundamentals/configuration

A comprehensive example of a deno.json file, showcasing configurations for TypeScript compiler options, linter, formatter, permissions, tasks, and imports. This serves as a template for project setup.

```json
{
  "compilerOptions": {
    "allowJs": true,
    "lib": ["deno.window"],
    "strict": true
  },
  "permissions": {
    "default": {
      "read": ["./src/testdata/"]
    }
  },
  "lint": {
    "include": ["src/"]
    "exclude": ["src/testdata/", "src/fixtures/**/*.ts"]
    "rules": {
      "tags": ["recommended"],
      "include": ["ban-untagged-todo"],
      "exclude": ["no-unused-vars"]
    }
  },
  "fmt": {
    "useTabs": true,
    "lineWidth": 80,
    "indentWidth": 4,
    "semiColons": false,
    "singleQuote": true,
    "proseWrap": "preserve",
    "include": ["src/"]
    "exclude": ["src/testdata/", "src/fixtures/**/*.ts"]
  },
  "lock": false,
  "nodeModulesDir": "auto",
  "unstable": ["webgpu"],
  "test": {
    "include": ["src/"]
    "exclude": ["src/testdata/", "src/fixtures/**/*.ts"]
  },
  "tasks": {
    "start": "deno run --allow-read main.ts"
  },
  "imports": {
    "oak": "jsr:@oak/oak"
  },
  "exclude": [
    "dist/"
  ]
}
```

--------------------------------

### Deno fmt: Help Command Example

Source: https://docs.deno.com/runtime/reference/cli/fmt

Displays how to access the help documentation for the `deno fmt` command to view all available CLI options.

```bash
deno fmt --help
```

--------------------------------

### Deno.serve - Hello World Server

Source: https://docs.deno.com/runtime/fundamentals/http_server

This example demonstrates the simplest way to create an HTTP server using Deno.serve that responds with 'Hello, World!' to every request.

```APIDOC
## Deno.serve - Hello World Server

### Description
Creates a basic HTTP server that always responds with 'Hello, World!'.

### Method
GET, POST, PUT, DELETE, etc. (Handles all HTTP methods)

### Endpoint
/

### Parameters
None

### Request Example
(No specific request body for this simple example)

### Response
#### Success Response (200)
- **response** (Response) - A Response object with the body 'Hello, World!'

#### Response Example
```
Hello, World!
```
```

--------------------------------

### Install Deno using Chocolatey (Windows)

Source: https://docs.deno.com/runtime/getting_started/installation

Installs Deno on Windows using the Chocolatey package manager.

```powershell
choco install deno
```

--------------------------------

### Install Deno using asdf version manager

Source: https://docs.deno.com/runtime/getting_started/installation

Manages Deno versions using the asdf version manager. Involves adding the plugin, installing a specific version (latest in this case), and setting it globally or locally.

```bash
asdf plugin add deno https://github.com/asdf-community/asdf-deno.git
asdf install deno latest
asdf set -u deno latest
asdf set deno latest
```

--------------------------------

### Replace new Deno.FsFile() with Deno.openSync() or Deno.open()

Source: https://docs.deno.com/runtime/reference/migration_guide

This example shows how to migrate from using the constructor `new Deno.FsFile()` to using the recommended `Deno.openSync()` or `Deno.open()` functions for opening files. This ensures compatibility with modern Deno APIs.

```typescript
using file = await Deno.open("/foo/bar.txt");
```

--------------------------------

### Create and Run a Docusaurus Site with Deno

Source: https://docs.deno.com/runtime/fundamentals/web_dev

This snippet shows how to create a new Docusaurus project, a static site generator optimized for documentation, using Deno. It employs `create-docusaurus` for project setup. The `deno task start` command initiates the development server.

```bash
deno run -A npm:create-docusaurus@latest my-website classic
cd my-website
deno task start
```

--------------------------------

### Uninstall Dependency with deno uninstall and --root flag

Source: https://docs.deno.com/runtime/reference/cli/uninstall

This example demonstrates uninstalling a globally installed script ('serve') while specifying a custom installation root directory (`/usr/local`) using the `--root` flag. This allows for managing installations in non-default locations.

```bash
deno uninstall --global --root /usr/local serve
```

--------------------------------

### Create and Run a Next.js App with Deno

Source: https://docs.deno.com/runtime/fundamentals/web_dev

This snippet shows how to initialize a new Next.js application using `create-next-app` and run it with Deno. It leverages Deno's ability to execute npm packages directly. Ensure you have Deno installed. The command `deno task dev` starts the development server, typically accessible at http://localhost:3000.

```bash
deno run -A npm:create-next-app@latest my-next-app
cd my-next-app
deno task dev
```

--------------------------------

### Deno fmt: Basic Usage and File Examples

Source: https://docs.deno.com/runtime/reference/cli/fmt

Demonstrates the basic command-line usage of `deno fmt` for formatting specified files and piping input/output.

```bash
deno fmt [OPTIONS] [files]...
deno fmt myfile1.ts myfile2.ts
cat file.ts | deno fmt -
deno fmt --check
```

--------------------------------

### Install Dependencies from Entrypoint Files with Deno

Source: https://docs.deno.com/runtime/reference/cli/install

Installs all dependencies used in the provided entrypoint files and their transitive dependencies. This is useful for caching dependencies before deployment, especially for packages from JSR, npm, http, or https specifiers. Optionally, a local node_modules directory can be created using the `--node-modules-dir=auto` flag.

```javascript
import * as colors from "jsr:@std/fmt/colors";
import express from "npm:express";

```

```bash
$ deno install -e main.js
Download jsr:@std/fmt
Download npm:express

```

--------------------------------

### Install Deno using vfox version manager

Source: https://docs.deno.com/runtime/getting_started/installation

Manages Deno versions using the vfox version manager. Involves adding the tool, installing a specific version (latest in this case), and setting it globally.

```bash
vfox add deno
vfox install deno@latest
vfox use --global deno
```

--------------------------------

### Get Help for Deno Bench Command

Source: https://docs.deno.com/runtime/reference/cli/bench

This command displays the help information for the `deno bench` command, listing all available runtime options and usage details.

```bash
deno help bench

```

--------------------------------

### Install Deno Jupyter Kernel

Source: https://docs.deno.com/runtime/reference/cli/jupyter

Provides instructions on how to install the Deno Jupyter kernel. Running `deno jupyter --install` forces the installation, assuming the `jupyter` command is available in the system's PATH.

```bash
deno jupyter --install
```

--------------------------------

### Replace Deno.UnixConn.prototype.rid Access

Source: https://docs.deno.com/runtime/reference/migration_guide

Illustrates the transition for Unix connections, implicitly suggesting the use of instance methods over direct .rid access, although a specific replacement example isn't fully provided in the source text beyond the context.

```typescript
using unixConn = await Deno.connect({ path: "/foo/bar.sock", transport: "unix" });

// Assuming similar pattern to other Conn types, instance methods replace .rid access.
```

--------------------------------

### Basic Documentation Example Syntax

Source: https://docs.deno.com/runtime/reference/documentation

Demonstrates the fundamental structure for including code examples within Deno documentation using triple backticks and a language identifier.

```markdown
/**
 * # Examples
 *
 * ```ts
 * const x = 42;
 * ```
 */
```

--------------------------------

### Replace 'deno cache' with 'deno install --entrypoint'

Source: https://docs.deno.com/runtime/reference/migration_guide

The 'deno cache' command is now merged into 'deno install' using the '--entrypoint' option. This change simplifies the process of installing and caching scripts.

```bash
- deno cache main.ts
+ deno install --entrypoint main.ts

```

--------------------------------

### Deno Package Configuration Example

Source: https://docs.deno.com/runtime/reference/cli/publish

An example of a deno.json or jsr.json file specifying the required 'name', 'version', and 'exports' fields for publishing a Deno package. The 'name' must be unique, 'version' must follow semver, and 'exports' must point to the package's entry point.

```json
{
  "name": "@scope_name/package_name",
  "version": "1.0.0",
  "exports": "./main.ts"
}
```

--------------------------------

### Uninstall Global Script with deno uninstall

Source: https://docs.deno.com/runtime/reference/cli/uninstall

This example demonstrates how to uninstall a globally installed executable script named 'serve' using the `deno uninstall --global` command. This removes the script from the installation root's bin directory.

```bash
deno uninstall --global serve
```

--------------------------------

### Basic Deno Dockerfile

Source: https://docs.deno.com/runtime/reference/docker

A foundational Dockerfile for running a Deno application. It sets up the working directory, copies the source code, installs dependencies using `deno install`, and defines the command to run the application. Assumes `main.ts` is the entry point.

```Dockerfile
FROM denoland/deno:latest

# Create working directory
WORKDIR /app

# Copy source
COPY . .

# Install dependencies (use just `deno install` if deno.json has imports)
RUN deno install --entrypoint main.ts

# Run the app
CMD ["deno", "run", "--allow-net", "main.ts"]

```

--------------------------------

### Replace Deno.serveHttp with Deno.serve

Source: https://docs.deno.com/runtime/reference/migration_guide

This snippet demonstrates replacing the older `Deno.serveHttp` API with the unified `Deno.serve` API for handling HTTP requests. It simplifies the server setup process.

```typescript
Deno.serve({ port: 80 }, () => new Response("Hello World"));
```

--------------------------------

### Replace Deno.writeAllSync with std/io/write-all

Source: https://docs.deno.com/runtime/reference/migration_guide

This example demonstrates migrating from the deprecated Deno.writeAllSync function to the writeAllSync function from the Deno standard library's io module. This ensures continued compatibility and access to the latest features.

```typescript
import { writeAllSync } from "jsr:@std/io/write-all";

const data = new TextEncoder().encode("Hello, world!");

writeAllSync(Deno.stdout, data);
```

--------------------------------

### Deno Unit Test Example

Source: https://docs.deno.com/runtime/contributing/style_guide

This snippet provides an example of an explicit unit test in Deno. It demonstrates importing assertion functions and the module under test, followed by a `Deno.test` block with a descriptive name and an assertion.

```typescript
import { assertEquals } from "@std/assert";
import { foo } from "./mod.ts";

Deno.test("foo() returns bar object", function () {
  assertEquals(foo(), { bar: "bar" });
});
```

--------------------------------

### Deno Executable Script Entrypoint with import.meta.main

Source: https://docs.deno.com/runtime/reference/cli/install

Example of how to define an entry point for an executable Deno script using the 'import.meta.main' idiom. This ensures the main logic runs only when the script is executed directly.

```typescript
// https://example.com/awesome/cli.ts
async function myAwesomeCli(): Promise<void> {
  // -- snip --
}

if (import.meta.main) {
  myAwesomeCli();
}

```

--------------------------------

### Verify Deno Installation

Source: https://docs.deno.com/runtime/index

Checks if the Deno runtime has been successfully installed and is available in the system's PATH by printing the installed version. This command should be run after installation.

```shell
deno --version

```

--------------------------------

### Function Arguments: Using Options Object for Many Arguments (TypeScript)

Source: https://docs.deno.com/runtime/contributing/style_guide

Demonstrates how to handle functions with a large number of arguments by consolidating them into a single options object. The 'BAD' example has too many distinct arguments. The 'BETTER' example uses an `PWrite` interface to group all parameters into a single object argument, improving readability and maintainability.

```typescript
// BAD: too many arguments. (#1)
export function pwrite(
  fd: number,
  buffer: ArrayBuffer,
  offset: number,
  length: number,
  position: number,
) {}

// BETTER.
export interface PWrite {
  fd: number;
  buffer: ArrayBuffer;
  offset: number;
  length: number;
  position: number;
}
export function pwrite(options: PWrite) {}


```

--------------------------------

### CLI Bundle with HTML Entrypoint

Source: https://docs.deno.com/runtime/reference/bundling

This example demonstrates using an HTML file as the entrypoint for `deno bundle`. It shows the command to bundle an HTML file and the resulting output, which includes updated script and stylesheet references with cache-busting hashes.

```typescript
import { render } from "npm:preact";
import "./styles.css";

const app = (
  <div>
    <p>Hello World!</p>
  </div>
);

render(app, document.body);

```

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Example</title>
    <script src="./index.tsx" type="module"></script>
  </head>
</html>

```

```shell
deno bundle --outdir dist index.html

```

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Example</title>
    <script src="./index-2TFDJWLF.js" type="module" crossorigin></script>
    <link rel="stylesheet" crossorigin href="./index-EWSJYQGA.css">
  </head>
</html>

```

--------------------------------

### JSX Import Source Pragma Example

Source: https://docs.deno.com/runtime/reference/jsx

Demonstrates how to use the `@jsxImportSource` pragma in a file to specify the JSX import source, overriding project-level configurations. This example shows how to use Preact from esm.sh.

```javascript
/** @jsxImportSource https://esm.sh/preact */

export function App() {
  return (
    <div>
      <h1>Hello, world!</h1>
    </div>
  );
}
```

--------------------------------

### Define Baseline and Compare Timings in Deno

Source: https://docs.deno.com/runtime/reference/cli/bench

This example shows how to set up a baseline benchmark case using `baseline: true` and compare its performance against other cases within the same group ('timing'). It uses `Date.now()` as the baseline and `performance.now()` for comparison.

```typescript
// time_bench.ts
Deno.bench("Date.now()", { group: "timing", baseline: true }, () => {
  Date.now();
});

Deno.bench("performance.now()", { group: "timing" }, () => {
  performance.now();
});

```

--------------------------------

### Quiet Installation with Deno

Source: https://docs.deno.com/runtime/reference/cli/install

Shows the usage of the '--quiet' flag with 'deno install' to suppress diagnostic and progress output during installation. This is useful for cleaner output in automated environments.

```bash
$ deno install --quiet jsr:@std/http/file-server

```

--------------------------------

### Debug with Chrome DevTools (--inspect-brk)

Source: https://docs.deno.com/runtime/fundamentals/debugging

This example demonstrates debugging a Deno program using Chrome DevTools with the --inspect-brk flag. It starts a file server and shows how to connect to the debugger, set breakpoints, and inspect requests.

```bash
$ deno run --inspect-brk -RN jsr:@std/http/file-server
Debugger listening on ws://127.0.0.1:9229/ws/1e82c406-85a9-44ab-86b6-7341583480b1
...

```

```bash
curl http://0.0.0.0:4507/

```

--------------------------------

### Initialize a Web Server Project

Source: https://docs.deno.com/runtime/reference/cli/init

Initializes a Deno project suitable for running a web server with 'deno serve'. It configures the 'deno.json' file with tasks for running and developing the server, including hot-reloading capabilities.

```bash
$ deno init --serve
✅ Project initialized

Run these commands to get started

  # Run the server
  deno serve -R main.ts

  # Run the server and watch for file changes
  deno task dev

  # Run the tests
  deno -R test

$ deno task dev
Task dev deno serve --watch -R main.ts
Watcher Process started.
deno serve: Listening on http://0.0.0.0:8000/

```

```json
{
  "tasks": {
    "dev": "deno serve --watch -R main.ts"
  },
  "imports": {
    "@std/assert": "jsr:@std/assert@1",
    "@std/http": "jsr:@std/http@1"
  }
}
```

--------------------------------

### Deno OpenTelemetry API Installation

Source: https://docs.deno.com/runtime/fundamentals/open_telemetry

Installs version 1.x of the OpenTelemetry API package for Deno. This package is used for creating custom metrics and traces within the Deno runtime.

```bash
deno add npm:@opentelemetry/api@1
```

--------------------------------

### Install Deno Runtime (macOS/Linux)

Source: https://docs.deno.com/runtime/index

Installs the Deno runtime on macOS and Linux systems using a curl command to download and execute an installation script. Ensure you have curl and shell access.

```shell
curl -fsSL https://deno.land/install.sh | sh

```

--------------------------------

### Create a Tracer and Start an Active Span in Deno

Source: https://docs.deno.com/runtime/fundamentals/open_telemetry

Initializes a tracer and demonstrates how to create an active span using `tracer.startActiveSpan`. Includes error handling and ensures the span is always ended.

```typescript
import { trace } from "npm:@opentelemetry/api@1";

const tracer = trace.getTracer("my-app", "1.0.0");

function myFunction() {
  return tracer.startActiveSpan("myFunction", (span) => {
    try {
      // do myFunction's work
    } catch (error) {
      span.recordException(error);
      span.setStatus({
        code: trace.SpanStatusCode.ERROR,
        message: (error as Error).message,
      });
      throw error;
    } finally {
      span.end();
    }
  });
}
```

--------------------------------

### Deno Resource Sanitizer Example

Source: https://docs.deno.com/runtime/fundamentals/testing

Demonstrates how to manage and close I/O resources like file handles and network connections in Deno to prevent leaks. It shows the manual closing of resources and how the resource sanitizer, enabled by default, ensures these are closed. The example also shows how to disable this sanitizer using `sanitizeResources: false`.

```typescript
const file = await Deno.open("hello.txt");
// Do something with the file
file.close(); // <- Always close the file when you are done with it

```

```typescript
const conn = await Deno.connect({ hostname: "example.com", port: 80 });
// Do something with the connection
conn.close(); // <- Always close the connection when you are done with it

```

```typescript
const response = await fetch("https://example.com");
// Do something with the response
await response.body?.cancel(); // <- Always cancel the body when you are done with it, if you didn't consume it otherwise

```

```typescript
Deno.test({
  name: "leaky resource test",
  async fn() {
    await Deno.open("hello.txt");
  },
  sanitizeResources: false,
});

```

--------------------------------

### Basic Test Execution Examples

Source: https://docs.deno.com/runtime/reference/cli/test

Demonstrates basic commands for running Deno tests, including running all tests, specifying test files, using glob patterns, skipping type-checking, and running tests in watch mode.

```bash
deno test
den
o test src/fetch_test.ts src/signal_test.ts
den
o test src/*.test.ts
den
o test --no-check
den
o test --watch
```

--------------------------------

### Install Deno using MacPorts

Source: https://docs.deno.com/runtime/getting_started/installation

Installs Deno on macOS using the MacPorts package manager. Requires root privileges.

```bash
sudo port install deno
```

--------------------------------

### Install Deno Runtime (Windows PowerShell)

Source: https://docs.deno.com/runtime/index

Installs the Deno runtime on Windows systems using PowerShell to download and execute an installation script. This command requires PowerShell to be available.

```powershell
irm https://deno.land/install.ps1 | iex

```

--------------------------------

### Initialize a Basic Deno Project

Source: https://docs.deno.com/runtime/reference/cli/init

Initializes a standard Deno project with main.ts, main_test.ts, and deno.json. It provides example code for a simple function and its test. The command can take a directory name as an argument to initialize the project in a specific location.

```bash
$ deno init
✅ Project initialized
Run these commands to get started

  // Run the program
  deno run main.ts

  // Run the program and watch for file changes
  deno task dev

  // Run the tests
  deno test

$ deno run main.ts
Add 2 + 3 = 5

$ deno test
Check file:///dev/main_test.ts
running 1 test from main_test.ts
addTest ... ok (6ms)

ok | 1 passed | 0 failed (29ms)

$ deno init my_deno_project
✅ Project initialized

Run these commands to get started

  cd my_deno_project

  // Run the program
  deno run main.ts

  // Run the program and watch for file changes
  deno task dev

  // Run the tests
  deno test

```

--------------------------------

### Deno.run() Migration

Source: https://docs.deno.com/runtime/reference/migration_guide

Replaces `Deno.run()` with the `Deno.Command` API for spawning and managing child processes.

```APIDOC
## Deno.run()

### Description
Use `new Deno.Command()` instead of `Deno.run()` for spawning and interacting with child processes.

### Method
Process Spawning and Management

### Endpoint
N/A (Internal API)

### Parameters
N/A

### Request Example
```javascript
// Deprecated usage
// const process = Deno.run({ cmd: [ "echo", "hello world" ], stdout: "piped" });
// const [{ success }, stdout] = await Promise.all([
//   process.status(),
//   process.output(),
// ]);
// process.close();

// Recommended usage
const command = new Deno.Command("echo", {
  args: ["hello world"]
});
const { success, stdout } = await command.output();
console.log(success);
console.log(new TextDecoder().decode(stdout));
```

### Response
#### Success Response (200)
- `boolean` - `success`: Indicates if the command executed successfully.
- `Uint8Array` - `stdout`: The standard output of the command.

#### Response Example
```json
{
  "success": true,
  "stdout": "aGVsbG8gd29ybGQ="
}
```
```

--------------------------------

### JSX Precompile Transform Input and Output Example

Source: https://docs.deno.com/runtime/reference/jsx

This example illustrates the input JSX and the resulting JavaScript code after applying Deno's JSX precompile transform. It demonstrates how JSX is converted into efficient HTML string generation for server-side rendering.

```javascript
// input
const jsx = (
  <div className="foo">
    <MyComponent value={2} />
  </div>
);

// output:
import {
  jsx as _jsx,
  jsxTemplate as _jsxTemplate,
} from "npm:preact/jsx-runtime";
const $$_tpl_1 = [
  '<div class="foo">',
  "</div>",
];
function MyComponent() {
  return null;
}
const jsx = _jsxTemplate(
  $$_tpl_1,
  _jsx(MyComponent, {
    value: 2,
  }),
);
```

--------------------------------

### Create and Run a Hono App with Deno

Source: https://docs.deno.com/runtime/fundamentals/web_dev

This snippet details the steps to create a new Hono application, a lightweight web framework, and run it using Deno. It uses `create-hono` for project initialization. The `deno task start` command launches the development server, typically accessible at http://localhost:8000.

```bash
deno run -A npm:create-hono@latest
cd my-hono-app
deno task start
```

--------------------------------

### Hashing a File with BLAKE3

Source: https://docs.deno.com/runtime/reference/std/crypto

Example of reading a file and computing its BLAKE3 hash.

```typescript
import { crypto } from "@std/crypto/crypto";

const file = await Deno.readFile("./README.md");
const buf = await crypto.subtle.digest("BLAKE3", file);
console.log(new Uint8Array(buf));

```

--------------------------------

### Web Storage API (localStorage) Operations in Deno

Source: https://docs.deno.com/runtime/reference/web_platform_apis

Provides examples of basic operations for the Web Storage API's localStorage object in Deno. It demonstrates how to set, get, remove, and clear items, with persistence rules depending on command-line flags like --location or --config.

```typescript
// Set an item in localStorage
localStorage.setItem("myDemo", "Deno App");

// Read an item from localStorage
const cat = localStorage.getItem("myDemo");

// Remove an item from localStorage
localStorage.removeItem("myDemo");

// Remove all items from localStorage
localStorage.clear();

```

--------------------------------

### Update nodeModulesDir Configuration Option

Source: https://docs.deno.com/runtime/reference/migration_guide

This example demonstrates the change in the `nodeModulesDir` configuration option from Deno 1.x to Deno 2.x. The boolean values `false` and `true` are replaced with string options like `"none"`, `"auto"`, and `"manual"` to provide more granular control over Node module directory behavior.

```json
- "nodeModulesDir": false | true
+ "nodeModulesDir": "none" | "auto" | "manual"
```

--------------------------------

### Glob expansion examples

Source: https://docs.deno.com/runtime/reference/cli/task

Demonstrates the use of glob patterns in Deno for matching files. Supported characters include `*`, `?`, and `[`/`]`. This feature allows for cross-platform file matching.

```shell
# match .ts files in the current and descendant directories
echo **/*.ts
# match .ts files in the current directory
echo *.ts
# match files that start with "data", have a single number, then end with .csv
echo data[0-9].csv

```

--------------------------------

### Output of Example Documentation (CLI)

Source: https://docs.deno.com/runtime/reference/cli/doc

The expected output when running 'deno doc' on the provided 'add.ts' file. It shows the parsed JSDoc comment and function signature.

```bash
deno doc add.ts
function add(x: number, y: number): number
  Adds x and y. @param {number} x @param {number} y @returns {number} Sum of x and y

```

--------------------------------

### Download Deno Upgrade to Specific Output Path

Source: https://docs.deno.com/runtime/reference/cli/upgrade

Downloads and installs the updated Deno executable to a specified file path instead of replacing the current one. Useful for managing multiple Deno versions or custom installations.

```bash
deno upgrade --output $HOME/my_deno
```

--------------------------------

### Deno Compile - Example with Permissions

Source: https://docs.deno.com/runtime/reference/cli/compile

An example of 'deno compile' specifying read and network permissions using --allow-read and --allow-net. This ensures the compiled executable will have these capabilities at runtime.

```bash
deno compile --allow-read --allow-net jsr:@std/http/file-server
```

--------------------------------

### Run Deno Benchmarks from Command Line

Source: https://docs.deno.com/runtime/reference/cli/bench

These commands illustrate how to execute Deno benchmarks. You can run all benchmarks in the current directory, a specific directory, or a single benchmark file. The `deno bench` command supports recursive searching and directory targeting.

```bash
# Run all benches in the current directory and all sub-directories
den
o bench

# Run all benches in the util directory
den
o bench util/

# Run just my_bench.ts
den
o bench my_bench.ts

```

--------------------------------

### Create and Run an Astro Site with Deno

Source: https://docs.deno.com/runtime/fundamentals/web_dev

This snippet illustrates setting up a new Astro project, a static site generator, and running it using Deno. It utilizes `create-astro` for project initialization. The `deno task dev` command starts the development server, typically found at http://localhost:4321.

```bash
deno run -A npm:create-astro my-astro-site
cd my-astro-site
deno task dev
```

--------------------------------

### Install Packages with Deno

Source: https://docs.deno.com/runtime/reference/cli/install

Installs specified packages from JSR or npm registries. If a package.json exists, npm packages are added to its dependencies. Otherwise, all packages are added to deno.json. This command also serves as an alias for `deno add`.

```bash
$ deno install jsr:@std/testing npm:express
```

--------------------------------

### Cache Dependencies Immediately with Deno Install

Source: https://docs.deno.com/runtime/fundamentals/modules

Immediately caches project dependencies into the 'vendor' directory without running the application, using the 'deno install' command with an entrypoint.

```shell
deno install --entrypoint main.ts
```

--------------------------------

### Run Deno Jupyter Kernel

Source: https://docs.deno.com/runtime/reference/cli/jupyter

Explains how to start the Deno Jupyter kernel by running the `deno jupyter` command. Note that currently, all code executed within the kernel runs with the `--allow-all` flag as a temporary limitation.

```bash
deno jupyter
```

--------------------------------

### Memoize Fibonacci with LRU Cache Example - TypeScript

Source: https://docs.deno.com/runtime/reference/std/cache

Provides a basic example of memoizing a Fibonacci function using an LRU cache. This snippet demonstrates the setup of the cache and the memoized function without explicit imports for verification, focusing on the core logic.

```typescript
import { LruCache, memoize } from "@std/cache";

const cache = new LruCache<string, number>(500);
const fib = memoize(
  (n: number): number => n <= 1 ? n : fib(n - 1) + fib(n - 2),
  { cache },
);

```

--------------------------------

### Compile Rust to WebAssembly for Deno

Source: https://docs.deno.com/runtime/reference/wasm

Shows an example of a Rust program that compiles to WebAssembly, exporting a 'main' function that returns the value 42. This demonstrates the source code that would generate the Wasm binary used in other examples.

```rust
#[unsafe(no_mangle)]
pub fn main() -> u32 { // u32 stands for an unsigned integer using 32 bits of memory.
  42
}

```

--------------------------------

### Example Deno Lint Plugin Structure and Rule

Source: https://docs.deno.com/runtime/reference/lint_plugins

An example of a Deno lint plugin. It defines a plugin object with a name and a 'rules' property. Each rule has a 'create' method that returns an AST visitor. This example demonstrates reporting an error for identifiers named '_a' and providing a fix to rename them to '_b'.

```typescript
const plugin: Deno.lint.Plugin = {
  // The name of your plugin. Will be shown in error output
  name: "my-plugin",
  // Object with rules. The property name is the rule name and
  // will be shown in the error output as well.
  rules: {
    "my-rule": {
      // Inside the `create(context)` method is where you'll put your logic.
      // It's called when a file is being linted.
      create(context) {
        // Return an AST visitor object
        return {
          // Here in this example we forbid any identifiers being named `_a`
          Identifier(node) {
            if (node.name === "_a") {
              // Report a lint error with a custom message
              context.report({
                node,
                message: "should be _b",
                // Optional: Provide a fix, which can be applied when
                // the user runs `deno lint --fix`
                fix(fixer) {
                  return fixer.replaceText(node, "_b");
                },
              });
            }
          },
        };
      },
    },
  },
};
export default plugin;

```

--------------------------------

### Function Arguments: Consolidating Optional Parameters (TypeScript)

Source: https://docs.deno.com/runtime/contributing/style_guide

Shows how to refactor functions with multiple optional parameters into a single options object. The 'BAD' example has too many arguments and optional parameters. The 'GOOD' example consolidates these into a `RenameOptions` interface, simplifying the function signature and adhering to rule #2.

```typescript
// BAD: more than 3 arguments (#1), multiple optional parameters (#2).
export function renameSync(
  oldname: string,
  newname: string,
  replaceExisting?: boolean,
  followLinks?: boolean,
) {}

// GOOD.
interface RenameOptions {
  replaceExisting?: boolean;
  followLinks?: boolean;
}
export function renameSync(
  oldname: string,
  newname: string,
  options: RenameOptions = {},
) {}


```

--------------------------------

### Deno: Create a Minimal HTTP Server

Source: https://docs.deno.com/runtime/reference/std/http

This example demonstrates how to create a very basic HTTP server in Deno using the `serve` function from `@std/http`. It listens on port 8000 and responds with 'Hello' to all incoming requests. No external dependencies beyond the standard library are required.

```typescript
import { serve } from "@std/http";

serve((_req) => new Response("Hello"), { port: 8000 });

```

--------------------------------

### Deno Configuration - Including Specific Test Files

Source: https://docs.deno.com/runtime/fundamentals/testing

Provides an example of a Deno configuration file (`deno.json` or `deno.jsonc`) specifying an `include` array to limit test execution to only the listed files.

```json
{
  "test": {
    "include": [
      "src/fetch_test.ts",
      "src/signal_test.ts"
    ]
  }
}

```

--------------------------------

### Deno: Implement Conditional GET with ETag

Source: https://docs.deno.com/runtime/reference/std/http

This example shows how to implement conditional GET requests using ETags to enable client-side caching and reduce bandwidth. It uses `eTag` to generate an ETag for the response body and `ifNoneMatch` to check if the client's `If-None-Match` header matches the ETag. If they match, it returns a 304 Not Modified status.

```typescript
import { serve } from "@std/http";
import { eTag, ifNoneMatch } from "@std/http/etag";

const body = JSON.stringify({ message: "Hello, cached world" });
const etag = eTag(body);

serve((req) => {
  const inm = req.headers.get("if-none-match");
  // ifNoneMatch returns false when the tag matches -> respond 304
  if (!ifNoneMatch(inm, etag)) {
    return new Response(null, { status: 304, headers: { ETag: etag } });
  }
  return new Response(body, {
    headers: { "content-type": "application/json; charset=utf-8", ETag: etag },
  });
});

```

--------------------------------

### Deno: Manage Cookies (Set, Read, Delete)

Source: https://docs.deno.com/runtime/reference/std/http

This example illustrates how to manage cookies in a Deno HTTP server. It shows how to set a cookie using `setCookie`, read cookies using `getCookies`, and delete a cookie using `deleteCookie`. The example handles different routes for login, retrieving user information, and logging out.

```typescript
import { serve } from "@std/http";
import { deleteCookie, getCookies, setCookie } from "@std/http/cookie";

serve(async (req) => {
  const url = new URL(req.url);
  const headers = new Headers();

  if (url.pathname === "/login" && req.method === "POST") {
    // In practice, validate credentials first
    setCookie(headers, {
      name: "sid",
      value: crypto.randomUUID(),
      httpOnly: true,
      secure: true,
      sameSite: "Lax",
      path: "/",
      maxAge: 60 * 60, // 1 hour
    });
    return new Response("ok", { headers });
  }

  if (url.pathname === "/me") {
    const cookies = getCookies(req.headers);
    const sid = cookies["sid"] ?? "(none)";
    return Response.json({ sid });
  }

  if (url.pathname === "/logout") {
    deleteCookie(headers, "sid", { path: "/" });
    return new Response("bye", { headers });
  }

  return new Response("not found", { status: 404 });
});

```

--------------------------------

### Replace Deno.fstatSync() with Deno.FsFile.prototype.statSync()

Source: https://docs.deno.com/runtime/reference/migration_guide

Replaces the `Deno.fstatSync()` function with the `.statSync()` method on `Deno.FsFile` instances. This provides a direct, synchronous way to get file status information.

```typescript
  using file = Deno.openSync("/foo/bar.txt");

- const fileInfo = Deno.fstatSync(file.rid);
+ const fileInfo = file.statSync();

```

--------------------------------

### Include Files Starting with 'file:' or 'https:'

Source: https://docs.deno.com/runtime/reference/cli/coverage

This command customizes the coverage report to include files that start with either the 'file:' schema or the 'https:' schema. This expands coverage beyond the local filesystem.

```bash
deno coverage --include="^file:|https:"
```

--------------------------------

### Allowing Lifecycle Scripts for Node.js Addons

Source: https://docs.deno.com/runtime/reference/cli/install

Demonstrates how to use the '--allow-scripts' flag with 'deno install' to permit specific npm packages to run their lifecycle scripts, which is necessary for packages like 'npm:sqlite3'.

```bash
deno install --allow-scripts=npm:sqlite3

```

--------------------------------

### Deno Workspace Dependency Resolution Example

Source: https://docs.deno.com/runtime/fundamentals/workspaces

Illustrates the directory structure and deno.json configurations for a Deno workspace, showing how imports are resolved between workspace members.

```json
{
  "workspace": ["./project-a", "./project-b"]
}
```

```json
{
  "name": "@scope/project-a"
}
```

```typescript
imports from "@scope/project-b"
```

```json
{
  "name": "@scope/project-b"
}
```

--------------------------------

### Deno.ListenTlsOptions.keyFile

Source: https://docs.deno.com/runtime/reference/migration_guide

The `keyFile` option in `Deno.ListenTlsOptions` is deprecated. Use the `key` option instead, providing the key contents directly.

```APIDOC
## Deno.ListenTlsOptions.keyFile

### Description
Replaced by the `key` option in `Deno.ListenTlsOptions`.

### Method
N/A (Option Replacement)

### Endpoint
N/A

### Parameters
N/A

### Request Example
```javascript
// Old usage
// using listener = Deno.listenTls({
//   port: 443,
//   cert: Deno.readTextFile("./server.crt"),
//   keyFile: "./server.key",
// });

// New usage
using listener = Deno.listenTls({
  port: 443,
  cert: Deno.readTextFile("./server.crt"),
  key: Deno.readTextFileSync("./server.key"),
});
```

### Response
N/A
```

--------------------------------

### Start Deno Inspector Server (--inspect)

Source: https://docs.deno.com/runtime/fundamentals/debugging

Use the --inspect flag to start your Deno program with an inspector server. This allows client connections from tools supporting the V8 Inspector Protocol, such as Chrome DevTools. Note that code execution begins immediately.

```bash
deno run --inspect your_script.ts

```

--------------------------------

### Function Arguments: Distinguishing Options Object (TypeScript)

Source: https://docs.deno.com/runtime/contributing/style_guide

Illustrates how to distinguish a regular JavaScript Object used as an options parameter from other object types. The 'BAD' example uses a plain `Environment` object, while the 'GOOD' example wraps it in a specific `RunShellOptions` interface, preventing ambiguity. This adheres to rule #3 regarding the 'options' argument.

```typescript
export interface Environment {
  [key: string]: string;
}

// BAD: `env` could be a regular Object and is therefore indistinguishable
// from an options object. (#3)
export function runShellWithEnv(cmdline: string, env: Environment): string {}

// GOOD.
export interface RunShellOptions {
  env: Environment;
}
export function runShellWithEnv(
  cmdline: string,
  options: RunShellOptions,
): string {}


```

--------------------------------

### Deno Check Example: Local File Type Checking

Source: https://docs.deno.com/runtime/reference/cli/check

Illustrates a practical example of using 'deno check' on a local TypeScript file. This snippet also includes a simple TypeScript code block to be checked, demonstrating a type error.

```typescript
const x: string = 1 + 1n;

```

```bash
deno check example.ts

```

--------------------------------

### Create and Initialize OpenTelemetry Meter

Source: https://docs.deno.com/runtime/fundamentals/open_telemetry

Demonstrates how to import the metrics API and initialize a meter with a name and version. This is the first step in creating any metric instrument.

```typescript
import { metrics } from "npm:@opentelemetry/api@1";

const meter = metrics.getMeter("my-app", "1.0.0");

```

--------------------------------

### Function Arguments: Optional Parameters in Options Object (TypeScript)

Source: https://docs.deno.com/runtime/contributing/style_guide

Demonstrates the correct way to handle optional function parameters by placing them within an options object. This improves API flexibility and backward compatibility. It contrasts a 'BAD' example with optional parameters directly in the function signature and a 'GOOD' example using an interface for options.

```typescript
// BAD: optional parameters not part of options object. (#2)
export function resolve(
  hostname: string,
  family?: "ipv4" | "ipv6",
  timeout?: number,
): IPAddress[] {}


```

```typescript
// GOOD.
export interface ResolveOptions {
  family?: "ipv4" | "ipv6";
  timeout?: number;
}
export function resolve(
  hostname: string,
  options: ResolveOptions = {},
): IPAddress[] {}


```