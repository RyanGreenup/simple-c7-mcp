### Open Local Rust Documentation

Source: https://doc.rust-lang.org/book/ch01-01-installation

This command opens the locally installed Rust documentation in the default web browser. It provides offline access to API documentation and guides.

```shell
rustup doc
```

--------------------------------

### Create Rust Project and Add Dependencies with Cargo

Source: https://doc.rust-lang.org/book/ch01-01-installation

This snippet demonstrates the basic workflow for setting up a new Rust project and adding external crates using Cargo. It first creates a new project directory, then navigates into it, and finally adds specified package versions. These commands cache the dependencies locally, enabling offline usage.

```bash
cargo new get-dependencies
cd get-dependencies
cargo add rand@0.8.5 trpl@0.2.0
```

--------------------------------

### Install Rust using rustup (Linux/macOS)

Source: https://doc.rust-lang.org/book/ch01-01-installation

This command downloads and executes a script to install the rustup tool and the latest stable version of the Rust compiler on Linux and macOS systems. It requires an internet connection and may prompt for a password.

```shell
curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh
```

--------------------------------

### Verify Rust Installation

Source: https://doc.rust-lang.org/book/ch01-01-installation

This command checks if Rust is installed correctly by displaying the version of the Rust compiler. Successful execution will show the compiler version, commit hash, and commit date.

```shell
rustc --version
```

--------------------------------

### Rust Documentation Comment Example

Source: https://doc.rust-lang.org/book/ch14-02-publishing-to-crates-io

Demonstrates how to write documentation comments in Rust for a function. These comments are used to generate HTML documentation and can include examples that are run as tests. The `///` syntax is used for documentation comments, and Markdown is supported for formatting. The `# Examples` heading is commonly used to introduce code examples.

```rust
/// Adds one to the given number.
///
/// # Examples
///
/// ```
/// let arg = 5;
/// let answer = my_crate::add_one(arg);
///
/// assert_eq!(6, answer);
/// ```
pub fn add_one(x: i32) -> i32 {
    x + 1
}
```

--------------------------------

### Install Rust Binary Crate with Cargo

Source: https://doc.rust-lang.org/book/ch14-04-installing-binaries

Installs a binary Rust crate from crates.io using the 'cargo install' command. This command downloads, compiles, and installs executable Rust programs. Ensure the installation directory (~/.cargo/bin by default) is in your system's PATH to run the installed binaries.

```shell
$ cargo install ripgrep
    Updating crates.io index
  Downloaded ripgrep v14.1.1
  Downloaded 1 crate (213.6 KB) in 0.40s
  Installing ripgrep v14.1.1
--snip--
   Compiling grep v0.3.2
    Finished `release` profile [optimized + debuginfo] target(s) in 6.73s
  Installing ~/.cargo/bin/rg
   Installed package `ripgrep v14.1.1` (executable `rg`)

```

--------------------------------

### Install C compiler on macOS

Source: https://doc.rust-lang.org/book/ch01-01-installation

This command installs the Xcode command line tools on macOS, which include a C compiler and linker necessary for some Rust operations and dependencies.

```shell
xcode-select --install
```

--------------------------------

### Initial Cargo.toml Package Name Setup

Source: https://doc.rust-lang.org/book/ch14-02-publishing-to-crates-io

The initial setup of the `[package]` section in `Cargo.toml` showing only the required `name` field. Additional metadata is needed for successful publishing.

```toml
[package]
name = "guessing_game"

```

--------------------------------

### Update Rust Installation

Source: https://doc.rust-lang.org/book/ch01-01-installation

This command updates the Rust installation to the latest stable version using the rustup tool. It fetches and installs any new releases and associated components.

```shell
rustup update
```

--------------------------------

### Rust: Example of `cargo run` with no matches

Source: https://doc.rust-lang.org/book/ch12-04-testing-the-librarys-functionality

This example demonstrates running the Minigrep program with `cargo run` and a query (`monomorphization`) that does not exist in `poem.txt`. The output is empty, indicating no lines matched the query.

```text
__
$ cargo run -- monomorphization poem.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep monomorphization poem.txt`


```

--------------------------------

### Rust: Initial main function setup for I/O Project

Source: https://doc.rust-lang.org/book/ch13-03-improving-our-io-project

This Rust code snippet shows the initial setup of the `main` function in an I/O project. It collects command-line arguments into a vector of strings and attempts to build a `Config` struct. Error handling is included using `unwrap_or_else` to print problems and exit the process.

```rust
use std::env;
use std::process;

fn main() {
    let args: Vec<String> = env::args().collect();

    let config = Config::build(&args).unwrap_or_else(|err| {
        eprintln!("Problem parsing arguments: {err}");
        process::exit(1);
    });

    // ... rest of the main function
}

// Assuming Config struct and its build method are defined elsewhere

```

--------------------------------

### Blog Post Workflow Example Usage (Rust)

Source: https://doc.rust-lang.org/book/ch18-03-oo-design-patterns

Demonstrates the intended usage of a blog post API, showcasing the expected behavior for creating a draft, requesting a review, and publishing a post. It includes assertions to verify content availability at different stages. This code snippet is part of a larger example demonstrating the State pattern.

```rust
let mut post = Post::new();

post.add_text("I've learned so much about the Rust programming language. I can't wait to share them with you!");
assert_eq!("", post.content());

post.request_review();
assert_eq!("", post.content());

post.approve();
assert_eq!("I've learned so much about the Rust programming language. I can't wait to share them with you!", post.content());
```

--------------------------------

### Rust Helper Function for Integration Tests (common.rs)

Source: https://doc.rust-lang.org/book/ch11-03-test-organization

Defines a public `setup` function intended for use in integration tests. This code snippet is an example of a helper function placed in a separate file within the tests directory. It highlights the initial approach which can lead to unintended separate compilation of test files.

```rust
pub fn setup() {
    // setup code specific to your library's tests would go here
}
```

--------------------------------

### Uninstall Rust and rustup

Source: https://doc.rust-lang.org/book/ch01-01-installation

This command removes Rust and the rustup tool from the system. It cleans up the installation and associated configurations.

```shell
rustup self uninstall
```

--------------------------------

### Check PATH environment variable (Windows CMD)

Source: https://doc.rust-lang.org/book/ch01-01-installation

This command displays the current value of the system's PATH environment variable in the Windows Command Prompt. It's used to verify if Rust's bin directory is included.

```batch
> echo %PATH%
```

--------------------------------

### List Installed Rust Toolchains

Source: https://doc.rust-lang.org/book/appendix-07-nightly-rust

This command lists all the Rust toolchains (releases and associated components) currently installed on your system. It shows the default toolchain and available options like stable, beta, and nightly.

```shell
rustup toolchain list
```

--------------------------------

### Rust: Access and Store Command Line Arguments

Source: https://doc.rust-lang.org/book/ch12-01-accepting-command-line-arguments

This Rust code snippet demonstrates how to access command-line arguments provided to a program. It specifically shows how to retrieve the program's name, the search query, and the file path from the arguments vector and store them in separate variables. It uses `std::env::args` to get the arguments and assumes the first two user-provided arguments are the query and file path, respectively.

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    let query = &args[1];
    let file_path = &args[2];

    println!("Searching for {}", query);
    println!("In file {}", file_path);
}
```

--------------------------------

### Check PATH environment variable (Linux/macOS)

Source: https://doc.rust-lang.org/book/ch01-01-installation

This command displays the current value of the system's PATH environment variable on Linux and macOS. It's used to verify if Rust's bin directory is included.

```shell
$ echo $PATH
```

--------------------------------

### Create New Rust Project with Cargo

Source: https://doc.rust-lang.org/book/ch12-01-accepting-command-line-arguments

This command creates a new binary application project named 'minigrep'. It initializes the project structure and a basic main.rs file. The output confirms the project creation and prompts the user to navigate into the project directory.

```shell
$
cargo new minigrep
     Created binary (application) `minigrep` project
$
cd minigrep

```

--------------------------------

### Check PATH environment variable (Windows PowerShell)

Source: https://doc.rust-lang.org/book/ch01-01-installation

This command displays the current value of the system's PATH environment variable in Windows PowerShell. It's used to verify if Rust's bin directory is included.

```powershell
> echo $env:Path
```

--------------------------------

### Check Cargo Installation

Source: https://doc.rust-lang.org/book/ch01-03-hello-cargo

Verify if Cargo, Rust's build system and package manager, is installed on your system. This command outputs the installed version of Cargo if it is available.

```bash
$ cargo --version
```

--------------------------------

### Rust: Example of `cargo test` output for Minigrep

Source: https://doc.rust-lang.org/book/ch12-04-testing-the-librarys-functionality

This is the output from running the `cargo test` command for the Minigrep project. It confirms that the tests, including the one for the `search` function, are passing.

```text
__
$ cargo test
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished `test` profile [unoptimized + debuginfo] target(s) in 1.22s
     Running unittests src/lib.rs (target/debug/deps/minigrep-9cd200e5fac0fc94)

running 1 test
test tests::one_result ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running unittests src/main.rs (target/debug/deps/minigrep-9cd200e5fac0fc94)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

   Doc-tests minigrep

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

```

--------------------------------

### Rust Integration Test Code Example

Source: https://doc.rust-lang.org/book/ch11-03-test-organization

Provides an example of an integration test file in Rust. It includes the necessary `use` statement to bring the library's functionality into scope and a test function.

```rust
use adder::add_two;

#[test]
fn it_adds_two() {
    assert_eq!(4, add_two(2));
}

```

--------------------------------

### Run Rust Program with Command-Line Arguments

Source: https://doc.rust-lang.org/book/ch12-01-accepting-command-line-arguments

This command demonstrates how to run the Rust program 'minigrep' with custom command-line arguments. The '--' separates arguments for 'cargo run' from arguments intended for the 'minigrep' program itself. Here, 'searchstring' and 'example-filename.txt' are passed to the program.

```shell
$
cargo run -- searchstring example-filename.txt

```

--------------------------------

### Rust: Example of `cargo run` with a single match

Source: https://doc.rust-lang.org/book/ch12-04-testing-the-librarys-functionality

This demonstrates running the Minigrep program using `cargo run` with the query `frog` and the file `poem.txt`. The output shows the single line from the poem that contains the word 'frog'.

```text
__
$ cargo run -- frog poem.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.38s
     Running `target/debug/minigrep frog poem.txt`
How public, like a frog

```

--------------------------------

### Shorthand for String Slices from Start in Rust

Source: https://doc.rust-lang.org/book/ch04-03-slices

Illustrates the shorthand syntax for creating string slices that start from the beginning of a String. It shows that `&s[0..2]` is equivalent to `&s[..2]`.

```rust
#![allow(unused)]
fn main() {
let s = String::from("hello");

let slice = &s[0..2];
let slice = &s[..2];
}
```

--------------------------------

### Rust Crate-Level Documentation with `//!`

Source: https://doc.rust-lang.org/book/ch14-02-publishing-to-crates-io

This example demonstrates how to use `//!` doc comments at the beginning of a Rust crate root file (`src/lib.rs`) to document the entire crate. These comments appear on the crate's main documentation page, providing an overview of its purpose. This is particularly useful for explaining the overall functionality and organization of the crate to users.

```rust
#!/usr/bin/env cargo
//! ```
//! This is the documentation for the `my_crate` crate.
//! It provides various utility functions, including `add_one`.
//! ```

//! Add documentation to the item that _contains_ the comments rather than to the items _following_ the comments.

// Note: In a real scenario, the code for the crate would follow these comments.
// For example:
// pub fn add_one(x: i32) -> i32 {
//     x + 1
// }

```

--------------------------------

### Install Rust Nightly Toolchain

Source: https://doc.rust-lang.org/book/appendix-07-nightly-rust

This command installs the nightly release channel of the Rust toolchain. This is necessary for using unstable features that are not yet available in stable releases.

```shell
rustup toolchain install nightly
```

--------------------------------

### Define Post Struct and Draft State in Rust

Source: https://doc.rust-lang.org/book/ch18-03-oo-design-patterns

Defines the public `Post` struct with a private `state` field holding a trait object and an associated public `new` function. It also introduces a private `State` trait and the initial `Draft` struct to manage post states, ensuring new posts start as drafts.

```rust
struct Post {
    state: Option<Box<dyn State>>,
    content: String
}

impl Post {
    pub fn new() -> Post {
        Post {
            state: Some(Box::new(Draft {})),
            content: String::new(),
        }
    }
}

trait State {}

struct Draft {}

impl State for Draft {}

```

--------------------------------

### Rust Vector Element Access: Indexing vs. Get Method

Source: https://doc.rust-lang.org/book/ch08-01-vectors

Demonstrates accessing elements of a Rust vector using both direct indexing (`&v[index]`) and the `get()` method. Indexing returns a direct reference, while `get()` returns an `Option<&T>`, allowing for safe handling of out-of-bounds access via `match`. This highlights the trade-offs between immediate access and potential panics versus safer, albeit more verbose, access.

```rust
let v = vec![1, 2, 3, 4, 5];

// Using indexing
let first_indexed = &v[0];
println!("The first element (indexed) is: {}", first_indexed);

// Using get method
let third_get = v.get(2);
match third_get {
    Some(value) => println!("The third element (get) is: {}", value),
    None => println!("Index out of bounds.")
}

// Example of out-of-bounds access with get
let out_of_bounds_get = v.get(100);
match out_of_bounds_get {
    Some(value) => println!("Element at index 100 is: {}", value),
    None => println!("Index 100 is out of bounds.")
}
```

--------------------------------

### Rust: Example of `cargo run` with multiple matches

Source: https://doc.rust-lang.org/book/ch12-04-testing-the-librarys-functionality

This shows the output of running the Minigrep program with `cargo run` using the query `body` and `poem.txt`. The output correctly displays multiple lines from the poem that contain the word 'body'.

```text
__
$ cargo run -- body poem.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep body poem.txt`
I'm nobody! Who are you?
Are you nobody, too?
How dreary to be somebody!


```

--------------------------------

### Rust Project Structure Example

Source: https://doc.rust-lang.org/book/ch07-02-defining-modules-to-control-scope-and-privacy

This illustrates the directory structure for a Rust binary crate named 'backyard'. It shows the placement of the main crate file (src/main.rs), module files (src/garden.rs), and submodule files (src/garden/vegetables.rs).

```text
backyard
├── Cargo.lock
├── Cargo.toml
└── src
    ├── garden
    │   └── vegetables.rs
    ├── garden.rs
    └── main.rs


```

--------------------------------

### Rust Lifetime Annotation Syntax Examples

Source: https://doc.rust-lang.org/book/ch10-03-lifetime-syntax

This example demonstrates the basic syntax for lifetime annotations in Rust. It shows how to represent a reference without a lifetime parameter, a reference with an explicit lifetime parameter named `'a`, and a mutable reference with the same lifetime parameter.

```rust
&i32        // a reference
&'a i32     // a reference with an explicit lifetime
&'a mut i32 // a mutable reference with an explicit lifetime
```

--------------------------------

### Cargo Build Output Examples (dev vs. release)

Source: https://doc.rust-lang.org/book/ch14-01-release-profiles

Shows the typical output when building a Rust project using Cargo for the 'dev' and 'release' profiles. This illustrates the difference in compilation results, indicating optimization and debugging information availability.

```shell
$ cargo build
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.00s
$ cargo build --release
    Finished `release` profile [optimized] target(s) in 0.32s
```

--------------------------------

### Rust Single-Line Comment

Source: https://doc.rust-lang.org/book/ch03-04-comments

Demonstrates the basic single-line comment syntax in Rust, which starts with '//' and extends to the end of the line. This is useful for brief explanations or annotations.

```rust
#![allow(unused)]
fn main() {
// hello, world
}
```

--------------------------------

### Miri Execution Output Example

Source: https://doc.rust-lang.org/book/ch20-01-unsafe-rust

Example output from running Miri on a Rust project. Miri analyzes the runtime behavior of the code to identify potential issues like shared references to mutable data, providing warnings or detecting outright errors.

```shell
$ cargo +nightly miri run
   Compiling unsafe-example v0.1.0 (file:///projects/unsafe-example)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.01s
     Running `file:///home/.rustup/toolchains/nightly/bin/cargo-miri runner target/miri/debug/unsafe-example`
COUNTER: 3
```

--------------------------------

### Cargo Configuration File

Source: https://doc.rust-lang.org/book/ch01-03-hello-cargo

Example content of a `Cargo.toml` file, which is used for configuring Rust projects managed by Cargo. It specifies package metadata like name, version, and edition, and lists project dependencies. The file uses the TOML format.

```toml
[package]
name = "hello_cargo"
version = "0.1.0"
edition = "2021"

[dependencies]
```

--------------------------------

### Rust Async/Await Compilation Example

Source: https://doc.rust-lang.org/book/ch17-05-traits-for-async

Illustrates how Rust's `await` keyword is conceptually compiled into code that repeatedly polls a future until it returns `Ready`. This example shows a basic polling loop for a hypothetical `page_title` future.

```rust
match page_title(url).poll() {
    Ready(page_title) => match page_title {
        Some(title) => println!("The title for {url} was {title}"),
        None => println!("{url} had no title")
    }
    Pending => {
        // But what goes here?
    }
}
```

--------------------------------

### Example of Rust Backtrace Output

Source: https://doc.rust-lang.org/book/ch09-01-unrecoverable-errors-with-panic

Illustrative output from running a Rust program with the `RUST_BACKTRACE=1` environment variable set. This shows the detailed backtrace generated when a panic occurs, aiding in debugging by listing the call stack.

```text
$ cargo run
   Compiling panic v0.1.0 (file:///projects/panic)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.25s
     Running `target/debug/panic`

thread 'main' panicked at src/main.rs:2:5: 
crash and burn
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

$ RUST_BACKTRACE=1 cargo run
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.01s
     Running `target/debug/panic`

thread 'main' panicked at src/main.rs:2:5:
crash and burn
stack backtrace:
  0: rustc 1.70.0 (90c541806 2023-05-31)
  1: core::panicking::panic_fmt
  ... (output truncated for brevity) ...
  9: panic::main

```

--------------------------------

### Create Project Directory (Linux/macOS/PowerShell)

Source: https://doc.rust-lang.org/book/ch01-02-hello-world

These commands create a 'projects' directory in your home directory, navigate into it, and then create a 'hello_world' directory for your project. This sets up the basic file structure for your Rust projects.

```bash
$ mkdir ~/projects
$ cd ~/projects
$ mkdir hello_world
$ cd hello_world
```

--------------------------------

### List Available Cargo Commands

Source: https://doc.rust-lang.org/book/ch14-05-extending-cargo

Shows how to list all available Cargo commands, including built-in commands and any custom subcommands installed in the system's PATH. This is useful for discovering available functionality.

```bash
cargo --list
```

--------------------------------

### Create Project Directory (Windows CMD)

Source: https://doc.rust-lang.org/book/ch01-02-hello-world

These commands are the Windows Command Prompt equivalents for creating a 'projects' directory, navigating into it, and then creating a 'hello_world' directory for your Rust project.

```cmd
> mkdir "%USERPROFILE%\projects"
> cd /d "%USERPROFILE%\projects"
> mkdir hello_world
> cd hello_world
```

--------------------------------

### Shell: Running a Cargo Project

Source: https://doc.rust-lang.org/book/ch21-01-single-threaded

This command compiles and runs a Rust project managed by Cargo. The output indicates that the server has started and successfully handled multiple incoming connections, printing 'Connection established!' for each.

```bash
$ cargo run
     Running `target/debug/hello`
Connection established!
Connection established!
Connection established!
```

--------------------------------

### Rust Macro Definition with println!

Source: https://doc.rust-lang.org/book/ch20-05-macros

Demonstrates the usage of the `println!` macro for outputting formatted strings. This is a common example of a declarative macro in Rust, used for simple output operations. It can handle a variable number of arguments.

```rust
println!("hello");
println!("hello {}", name);
```

--------------------------------

### Rust Multi-Line Comment

Source: https://doc.rust-lang.org/book/ch03-04-comments

Illustrates how to write comments that span multiple lines in Rust. Each line of the comment must start with '//'. This is suitable for more detailed explanations.

```rust
#![allow(unused)]
fn main() {
// So we're doing something complicated here, long enough that we need
// multiple lines of comments to do it! Whew! Hopefully, this comment will
// explain what's going on.
}
```