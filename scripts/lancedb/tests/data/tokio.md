### SetOnce Basic Usage Example

Source: https://docs.rs/tokio/latest/tokio/sync/struct.SetOnce

Demonstrates the basic usage of SetOnce for setting and getting a value, including waiting for the value to be set. It shows how to initialize a static SetOnce and access its value asynchronously.

```rust
use tokio::sync::{SetOnce, SetOnceError};

static ONCE: SetOnce<u32> = SetOnce::const_new();


// set the value inside a task somewhere...
tokio::spawn(async move { ONCE.set(20) });

// checking with .get doesn't block main thread
println!("{:?}", ONCE.get());

// wait until the value is set, blocks the thread
println!("{:?}", ONCE.wait().await);

Ok(())

```

--------------------------------

### OnceCell Initialization Example (Rust)

Source: https://docs.rs/tokio/latest/tokio/sync/struct.OnceCell

Demonstrates how to use `OnceCell` to initialize a value asynchronously using `get_or_init`. This is useful for global variables that need one-time asynchronous setup. It requires the `sync` feature flag.

```rust
use tokio::sync::OnceCell;

async fn some_computation() -> u32 {
    1 + 1
}

static ONCE: OnceCell<u32> = OnceCell::const_new();

// In an async context:
// let result = ONCE.get_or_init(some_computation).await;
// assert_eq!(*result, 2);
```

--------------------------------

### Tokio UdpSocket: Bind, Connect, Recv, Send Example

Source: https://docs.rs/tokio/latest/tokio/net/struct.UdpSocket

A basic example demonstrating how to bind a UdpSocket, connect to a remote address, receive data, and send data back using Tokio. This snippet shows fundamental asynchronous network operations.

```rust
use tokio::net::UdpSocket;
use std::net::SocketAddr;

// ... inside an async function ...
let sock = UdpSocket::bind("0.0.0.0:8080".parse::<SocketAddr>().unwrap()).await?;

let remote_addr = "127.0.0.1:59600".parse::<SocketAddr>().unwrap();
sock.connect(remote_addr).await?;
let mut buf = [0u8; 32];
// recv from remote_addr
let len = sock.recv(&mut buf).await?;
// send to remote_addr
let _len = sock.send(&buf[..len]).await?;
```

--------------------------------

### Unix Signal Listener Example

Source: https://docs.rs/tokio/latest/tokio/signal/unix/struct.Signal

Demonstrates how to create and use a `Signal` listener to asynchronously wait for and react to OS signals, specifically SIGHUP, on Unix-like systems. It utilizes `tokio::signal::unix::signal` to create the listener and `recv().await` to wait for signal events. This example requires the `signal` feature flag to be enabled.

```rust
use tokio::signal::unix::{signal, SignalKind};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // An infinite stream of hangup signals.
    let mut sig = signal(SignalKind::hangup())?;

    // Print whenever a HUP signal is received
    loop {
        sig.recv().await;
        println!("got signal HUP");
    }
}
```

--------------------------------

### Spawn and Wait for Command Completion in Tokio

Source: https://docs.rs/tokio/latest/tokio/process/index

This example demonstrates how to spawn a child process (`echo hello world`) using `tokio::process::Command` and wait for its execution to complete. It then prints the exit status of the command. Dependencies include the `tokio` crate.

```rust
use tokio::process::Command;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // The usage is similar as with the standard library's `Command` type
    let mut child = Command::new("echo")
        .arg("hello")
        .arg("world")
        .spawn()
        .expect("failed to spawn");

    // Await until the command completes
    let status = child.wait().await?;
    println!("the command exited with: {}", status);
    Ok(())
}
```

--------------------------------

### Tokio TcpListener: Bind and Accept Loop Example

Source: https://docs.rs/tokio/latest/tokio/net/struct.TcpListener

Demonstrates how to bind a TcpListener to an address, then enter a loop to continuously accept incoming connections. It includes a placeholder function `process_socket` for handling accepted connections.

```rust
use tokio::net::TcpListener;

use std::io;

async fn process_socket<T>(socket: T) {
    // do work with socket here
}

#[tokio::main]
async fn main() -> io::Result<()> {
    let listener = TcpListener::bind("127.0.0.1:8080").await?;

    loop {
        let (socket, _) = listener.accept().await?;
        process_socket(socket).await;
    }
}
```

--------------------------------

### Spawn Command and Capture Output in Tokio

Source: https://docs.rs/tokio/latest/tokio/process/index

This example shows how to spawn a child process (`echo hello world`) and capture its complete output (stdout and exit status) using `tokio::process::Command::output()`. It asserts that the command succeeded and its output matches the expected string. Dependencies include the `tokio` crate.

```rust
use tokio::process::Command;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Like above, but use `output` which returns a future instead of
    // immediately returning the `Child`.
    let output = Command::new("echo").arg("hello").arg("world")
                        .output();

    let output = output.await?;

    assert!(output.status.success());
    assert_eq!(output.stdout, b"hello world\n");
    Ok(())
}
```

--------------------------------

### OpenOptions: Initialize New File Options in Tokio Rust

Source: https://docs.rs/tokio/latest/tokio/fs/struct.OpenOptions

Shows how to create a new OpenOptions builder with default settings (all options false) using tokio::fs::OpenOptions::new(). This is the starting point for configuring file open parameters asynchronously.

```rust
use tokio::fs::OpenOptions;

let mut options = OpenOptions::new();
let future = options.read(true).open("foo.txt");
// Note: The 'future' here would typically be awaited within an async context.
```

--------------------------------

### Spawn Child Process and Wait for Completion

Source: https://docs.rs/tokio/latest/tokio/process/struct.Command

Executes a command as a child process and returns a handle to it. The `Child` handle implements `Future`, allowing you to `await` its completion to get the `ExitStatus`. Standard input, output, and error streams are inherited from the parent by default. This example shows basic usage for running the 'ls' command.

```rust
use tokio::process::Command;

async fn run_ls() -> std::process::ExitStatus {
    Command::new("ls")
        .spawn()
        .expect("ls command failed to start")
        .wait()
        .await
        .expect("ls command failed to run")
}
```

--------------------------------

### MutexGuard::mutex Usage Example - Tokio Mutex

Source: https://docs.rs/tokio/latest/tokio/sync/struct.MutexGuard

Shows how to obtain a reference to the original Mutex from a MutexGuard using MutexGuard::mutex. The example demonstrates unlocking and then relocking the mutex after accessing it through the guard.

```rust
use tokio::sync::{Mutex, MutexGuard};

async fn unlock_and_relock<'l>(guard: MutexGuard<'l, u32>) -> MutexGuard<'l, u32> {
    println!("1. contains: {:?}", *guard);
    let mutex = MutexGuard::mutex(&guard);
    drop(guard);
    let guard = mutex.lock().await;
    println!("2. contains: {:?}", *guard);
    guard
}
```

--------------------------------

### UnixDatagram - Basic Usage Example

Source: https://docs.rs/tokio/latest/tokio/net/struct.UnixDatagram

Demonstrates how to create, bind, and read from a Unix datagram socket using Tokio's async runtime. Shows the typical pattern of waiting for readability and handling IO operations.

```APIDOC
## UnixDatagram Basic Usage Example

### Description
Comprehensive example showing socket creation, binding, and reading data from a Unix datagram socket.

### Example Code
```rust
use tokio::net::UnixDatagram;
use std::io;

#[tokio::main]
async fn main() -> io::Result<()> {
    // Create temporary directory for socket files
    let dir = tempfile::tempdir().unwrap();
    let client_path = dir.path().join("client.sock");
    let server_path = dir.path().join("server.sock");
    
    // Bind socket to client path
    let socket = UnixDatagram::bind(&client_path)?;

    loop {
        // Wait for the socket to be readable
        socket.readable().await?;

        // Create buffer on stack (not included in async task)
        let mut buf = [0; 1024];

        // Attempt to receive data
        match socket.try_recv_from(&mut buf) {
            Ok((n, _addr)) => {
                println!("GOT {:?}", &buf[..n]);
                break;
            }
            Err(ref e) if e.kind() == io::ErrorKind::WouldBlock => {
                // Readiness event was false positive, continue waiting
                continue;
            }
            Err(e) => {
                return Err(e);
            }
        }
    }

    Ok(())
}
```

### Key Patterns
- Use `#[tokio::main]` macro for async runtime
- Call `readable().await?` before IO operations
- Handle `WouldBlock` errors in loops
- Buffer allocation on stack within async context
- Use `try_recv_from()` for non-blocking receive attempts
```

--------------------------------

### Build Tokio Runtime with Custom Configuration

Source: https://docs.rs/tokio/latest/tokio/runtime/struct.Builder

Demonstrates building a Tokio Runtime using the Builder with various configuration options such as worker threads, thread name, and thread stack size. This is the primary example for using the Builder.

```rust
use tokio::runtime::Builder;

fn main() {
    // build runtime
    let runtime = Builder::new_multi_thread()
        .worker_threads(4)
        .thread_name("my-custom-name")
        .thread_stack_size(3 * 1024 * 1024)
        .build()
        .unwrap();

    // use runtime ...
}
```

--------------------------------

### Example: Writing to a Pipe (Rust)

Source: https://docs.rs/tokio/latest/tokio/net/unix/pipe/struct.Sender

An example demonstrating how to open a writing end of a FIFO pipe, wait for it to be writable using `writable().await`, and then attempt to write data using `try_write()`. It handles potential `WouldBlock` errors and breaks the loop upon successful write.

```rust
use tokio::net::unix::pipe;
use std::io;

#[tokio::main]
async fn main() -> io::Result<()> {
    // Open a writing end of a fifo
    let tx = pipe::OpenOptions::new().open_sender("path/to/a/fifo")?;

    loop {
        // Wait for the pipe to be writable
        tx.writable().await?;

        // Try to write data, this may still fail with `WouldBlock`
        // if the readiness event is a false positive.
        match tx.try_write(b"hello world") {
            Ok(n) => {
                break;
            }
            Err(e) if e.kind() == io::ErrorKind::WouldBlock => {
                continue;
            }
            Err(e) => {
                return Err(e.into());
            }
        }
    }

    Ok(())
}
```

--------------------------------

### Tokio: Build Runtime

Source: https://docs.rs/tokio/latest/tokio/runtime/struct.Builder

Constructs a configured Tokio `Runtime` instance, ready for spawning tasks. This is a core method for initializing a Tokio execution environment. The example demonstrates building a multi-threaded runtime and using it to execute an async block.

```rust
use tokio::runtime::Builder;

let rt  = Builder::new_multi_thread().build().unwrap();

rt.block_on(async {
    println!("Hello from the Tokio runtime");
});
```

--------------------------------

### Tokio TcpListener: Bind to Address

Source: https://docs.rs/tokio/latest/tokio/net/struct.TcpListener

Shows a basic example of binding a Tokio TcpListener to a specific IP address and port. This is the initial step to creating a server that listens for connections.

```rust
use tokio::net::TcpListener;
use std::io;

#[tokio::main]
async fn main() -> io::Result<()> {
    let listener = TcpListener::bind("127.0.0.1:2345").await?;

    // use the listener

    Ok(())
}
```

--------------------------------

### MutexGuard::try_map Example - Tokio Mutex

Source: https://docs.rs/tokio/latest/tokio/sync/struct.MutexGuard

Illustrates using MutexGuard::try_map to attempt creating a MappedMutexGuard for a component. If the closure returns None, the original guard is returned. This example demonstrates a successful mapping of a Mutex-protected field.

```rust
use tokio::sync::{Mutex, MutexGuard};

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct Foo(u32);

let foo = Mutex::new(Foo(1));

{
    let mut mapped = MutexGuard::try_map(foo.lock().await, |f| Some(&mut f.0))
        .expect("should not fail");
    *mapped = 2;
}

assert_eq!(Foo(2), *foo.lock().await);
```

--------------------------------

### Get Local Address of Tokio UnixDatagram

Source: https://docs.rs/tokio/latest/tokio/net/struct.UnixDatagram

Shows how to retrieve the local socket address for a Tokio UnixDatagram. Examples include getting the address for a socket bound to a file path and for an unbound socket.

```rust
use tokio::net::UnixDatagram;
use tempfile::tempdir;

// We use a temporary directory so that the socket
// files left by the bound sockets will get cleaned up.
let tmp = tempdir()?;

// Bind socket to a filesystem path
let socket_path = tmp.path().join("socket");
let socket = UnixDatagram::bind(&socket_path)?;

assert_eq!(socket.local_addr()?.as_pathname().unwrap(), &socket_path);

// Create an unbound socket
let socket = UnixDatagram::unbound()?;

assert!(socket.local_addr()?.is_unnamed());
```

--------------------------------

### Get Symbol Address of a Backtrace Frame

Source: https://docs.rs/tokio/latest/tokio/runtime/dump/struct.BacktraceFrame

Returns the starting symbol address of the function associated with the `BacktraceFrame`. This can be useful for further introspection or symbolic analysis of the backtrace.

```rust
pub fn symbol_address(&self) -> *mut c_void
```

--------------------------------

### Getting the ID of a LocalSet (Rust)

Source: https://docs.rs/tokio/latest/tokio/task/struct.LocalSet

Provides a simple example of how to retrieve the unique `Id` of a Tokio `LocalSet` instance using the `id()` method.

```rust
use tokio::task;

let local_set = task::LocalSet::new();
println!("Local set id: {}", local_set.id());
```

--------------------------------

### Create tokio::process::Command Instance

Source: https://docs.rs/tokio/latest/tokio/process/struct.Command

Initializes a new `Command` for executing a program. It sets default configurations for arguments, environment, and working directory. The `program` path can be absolute or will be searched in the system's PATH.

```rust
use tokio::process::Command;

// Basic usage:
let mut command = Command::new("sh");
```

--------------------------------

### Example Usage of Trace::capture in Tokio

Source: https://docs.rs/tokio/latest/tokio/runtime/dump/struct.Trace

This example demonstrates how to use `Trace::capture` to trace a future's polling behavior. It shows how to capture the trace, handle the result, and then await the future outside of the capture context to ensure it completes. The captured trace is then printed.

```rust
use std::future::Future;
use std::task::Poll;
use tokio::runtime::dump::Trace;

// some future
let mut test_future = std::pin::pin!(async move { tokio::task::yield_now().await; 0 });

// trace it once, see what it's doing
let (trace, res) = Trace::root(std::future::poll_fn(|cx| {
    let (res, trace) = Trace::capture(|| test_future.as_mut().poll(cx));
    Poll::Ready((trace, res))
})).await;

// await it to let it finish, outside of a `capture`
let output = match res {
   Poll::Ready(output) => output,
   Poll::Pending => test_future.await,
};

println!("{trace}");
```

--------------------------------

### Create a new ServerOptions builder with default settings (Rust)

Source: https://docs.rs/tokio/latest/tokio/net/windows/named_pipe/struct.ServerOptions

Initializes a new ServerOptions builder with default configurations. This is the starting point for creating a named pipe server. It requires the `net` feature flag to be enabled.

```Rust
use tokio::net::windows::named_pipe::ServerOptions;

const PIPE_NAME: &str = r"\\.\pipe\tokio-named-pipe-new";

let server = ServerOptions::new().create(PIPE_NAME)?;
```

--------------------------------

### OnceCell Wrapper Method Example (Rust)

Source: https://docs.rs/tokio/latest/tokio/sync/struct.OnceCell

Shows how to create a convenient wrapper function for accessing an initialized `OnceCell`. This pattern encapsulates the initialization logic and provides a clean interface for retrieving the globally initialized value. Requires the `sync` feature flag.

```rust
use tokio::sync::OnceCell;

static ONCE: OnceCell<u32> = OnceCell::const_new();

async fn get_global_integer() -> &'static u32 {
    ONCE.get_or_init(|| async {
        1 + 1
    }).await
}

// In an async context:
// let result = get_global_integer().await;
// assert_eq!(*result, 2);
```

--------------------------------

### Create New ClientOptions Builder

Source: https://docs.rs/tokio/latest/tokio/net/windows/named_pipe/struct.ClientOptions

Initializes a new ClientOptions builder with default settings. This is the starting point for configuring a named pipe client. It requires the `net` feature flag and is only available on Windows.

```rust
use tokio::net::windows::named_pipe::{ServerOptions, ClientOptions};

const PIPE_NAME: &str = r"\\.\\pipe\\tokio-named-pipe-client-new";

// Server must be created in order for the client creation to succeed.
let server = ServerOptions::new().create(PIPE_NAME)?;
let client = ClientOptions::new().open(PIPE_NAME)?;
```

--------------------------------

### Get Tokio Worker Thread ID

Source: https://docs.rs/tokio/latest/tokio/runtime/struct.RuntimeMetrics

Retrieves the `ThreadId` for a given worker thread index. Returns `None` if the worker thread has not finished starting up. Requires a valid worker index. This metric is available only on `tokio_unstable`.

```rust
use tokio::runtime::Handle;

let metrics = Handle::current().metrics();

let id = metrics.worker_thread_id(0);
println!("worker 0 has id {:?}", id);
```

--------------------------------

### Tokio #[main] Macro - Start Paused (Unstable)

Source: https://docs.rs/tokio/latest/tokio/attr.main

Configures the runtime to start with time paused when using the `current_thread` flavor. This feature requires the `test-util` feature to be enabled and is useful for time-sensitive testing.

```rust
#[tokio::main(flavor = "current_thread", start_paused = true)]
async fn main() {
    println!("Hello world");
}
```

```rust
fn main() {
    tokio::runtime::Builder::new_current_thread()
        .enable_all()
        .start_paused(true)
        .build()
        .unwrap()
        .block_on(async {
            println!("Hello world");
        })
}
```

--------------------------------

### Execute Function on Tokio Thread Start (Rust)

Source: https://docs.rs/tokio/latest/tokio/runtime/struct.Builder

Specifies a function to be executed after each Tokio worker thread starts but before it begins processing tasks. This is primarily for bookkeeping and monitoring purposes and is available on non-`loom` configurations.

```rust
let runtime = runtime::Builder::new_multi_thread()
    .on_thread_start(|| {
        println!("thread started");
    })
    .build();
```

--------------------------------

### Initialize DirBuilder with Default Settings (Rust)

Source: https://docs.rs/tokio/latest/tokio/fs/struct.DirBuilder

Demonstrates creating a new DirBuilder instance with default settings for directory creation. This is the asynchronous equivalent of std::fs::DirBuilder::new.

```rust
use tokio::fs::DirBuilder;

let builder = DirBuilder::new();
```

--------------------------------

### UDP Socket Binding and Connection

Source: https://docs.rs/tokio/latest/tokio/net/struct.UdpSocket

Demonstrates how to bind a UDP socket to a local address and connect to a remote address. This is the foundational setup for UDP communication in Tokio.

```APIDOC
## UDP Socket Binding and Connection

### Description
Bind a UDP socket to a local address and establish a connection to a remote address for bidirectional communication.

### Method
Bind and Connect Operations

### Endpoint
Local socket binding and remote connection establishment

### Parameters
#### Bind Parameters
- **address** (SocketAddr) - Required - Local address to bind to (e.g., "0.0.0.0:8080")

#### Connect Parameters
- **remote_addr** (SocketAddr) - Required - Remote address to connect to (e.g., "127.0.0.1:59600")

### Request Example
```rust
use tokio::net::UdpSocket;
use std::net::SocketAddr;

let sock = UdpSocket::bind("0.0.0.0:8080".parse::<SocketAddr>().unwrap()).await?;
let remote_addr = "127.0.0.1:59600".parse::<SocketAddr>().unwrap();
sock.connect(remote_addr).await?;
```

### Response
#### Success Response
- **sock** (UdpSocket) - Connected UDP socket ready for send/recv operations

### Operations Available
- **recv()** - Receive data from the connected remote address
- **send()** - Send data to the connected remote address
```

--------------------------------

### Resubscribing to Broadcast Channel with Receiver::resubscribe

Source: https://docs.rs/tokio/latest/tokio/sync/broadcast/struct.Receiver

Demonstrates the `resubscribe()` method, which creates a new `Receiver` that starts receiving messages from the current tail element onwards. This example highlights that the new receiver will not receive messages sent before its subscription.

```rust
use tokio::sync::broadcast;

let (tx, mut rx) = broadcast::channel(2);

tx.send(1).unwrap();
let mut rx2 = rx.resubscribe();
tx.send(2).unwrap();

assert_eq!(rx2.recv().await.unwrap(), 2);
assert_eq!(rx.recv().await.unwrap(), 1);
```

--------------------------------

### tokio::sync::futures::Notified::enable Example

Source: https://docs.rs/tokio/latest/tokio/sync/futures/struct.Notified

Demonstrates the usage of the `enable` method on a `Notified` future. This example shows how to implement a multi-producer multi-consumer (mpmc) channel using `tokio::sync::Notify`. The `enable` method is crucial for preventing lost wakeups in concurrent scenarios where multiple senders and receivers might be active.

```rust
use tokio::sync::Notify;

use std::collections::VecDeque;
use std::sync::Mutex;

struct Channel<T> {
    messages: Mutex<VecDeque<T>>,
    notify_on_sent: Notify,
}

impl<T> Channel<T> {
    pub fn send(&self, msg: T) {
        let mut locked_queue = self.messages.lock().unwrap();
        locked_queue.push_back(msg);
        drop(locked_queue);

        // Send a notification to one of the calls currently
        // waiting in a call to `recv`.
        self.notify_on_sent.notify_one();
    }

    pub fn try_recv(&self) -> Option<T> {
        let mut locked_queue = self.messages.lock().unwrap();
        locked_queue.pop_front()
    }

    pub async fn recv(&self) -> T {
        let future = self.notify_on_sent.notified();
        tokio::pin!(future);

        loop {
            // Make sure that no wakeup is lost if we get
            // `None` from `try_recv`.
            future.as_mut().enable();

            if let Some(msg) = self.try_recv() {
                return msg;
            }

            // Wait for a call to `notify_one`.
            //
            // This uses `.as_mut()` to avoid consuming the future,
            // which lets us call `Pin::set` below.
            future.as_mut().await;

            // Reset the future in case another call to
            // `try_recv` got the message before us.
            future.set(self.notify_on_sent.notified());
        }
    }
}

```

--------------------------------

### Get current stream position - Rust AsyncSeekExt

Source: https://docs.rs/tokio/latest/tokio/io/struct.Empty

Creates a future that returns the current seek position from the start of the async stream. Returns a Seek future that resolves to the current position. Requires the `io-util` crate feature and Unpin trait bound.

```rust
fn stream_position(&mut self) -> Seek<'_, Self>
where Self: Unpin
```

--------------------------------

### Get Tokio Poll Time Histogram Bucket Count

Source: https://docs.rs/tokio/latest/tokio/runtime/struct.RuntimeMetrics

Returns the count of task polls falling within a specific bucket's duration range for a given worker. Available on `tokio_unstable` with `target_has_atomic=64`. Each worker maintains its own histogram, and bucket counts start at zero.

```rust
use tokio::runtime::{self, Handle};

fn main() {
    runtime::Builder::new_current_thread()
        .enable_metrics_poll_time_histogram()
        .build()
        .unwrap()
        .block_on(async {
            let metrics = Handle::current().metrics();
            let buckets = metrics.poll_time_histogram_num_buckets();

            for worker in 0..metrics.num_workers() {
                for i in 0..buckets {
                    let count = metrics.poll_time_histogram_bucket_count(worker, i);
                    println!("Poll count {}", count);
                }
            }
        });
}
```

--------------------------------

### Initialize Tokio Runtime Builder

Source: https://docs.rs/tokio/latest/tokio/runtime/struct.Builder

Shows how to obtain new instances of the Builder for creating either a multi-threaded or a current-thread scheduler. These are the entry points for configuring a Tokio Runtime.

```rust
use tokio::runtime::Builder;

// For multi-threaded runtime
let builder_multi = Builder::new_multi_thread();

// For current-thread runtime
let builder_current = Builder::new_current_thread();
```

--------------------------------

### tokio::time::timeout_at Example

Source: https://docs.rs/tokio/latest/tokio/time/fn.timeout_at

Demonstrates how to use `timeout_at` to set a deadline for a future to complete. This example creates a oneshot channel and wraps the receiver future with a `timeout_at` that expires in 10 milliseconds. If the value is not received within this time, it prints a message.

```rust
use tokio::time::{Instant, timeout_at};
use tokio::sync::oneshot;

use std::time::Duration;

let (tx, rx) = oneshot::channel();

// Wrap the future with a `Timeout` set to expire 10 milliseconds into the
// future.
if let Err(_) = timeout_at(Instant::now() + Duration::from_millis(10), rx).await {
    println!("did not receive value within 10 ms");
}

```

--------------------------------

### Create Async Named Pipe with Security QoS Flags in Tokio

Source: https://docs.rs/tokio/latest/tokio/fs/struct.OpenOptions

Demonstrates creating an asynchronous named pipe file handle using Tokio's OpenOptions with Windows security identification flags. The example configures write permissions, file creation mode, and applies SECURITY_IDENTIFICATION quality of service settings before opening the pipe. Requires windows_sys crate for Windows-specific security constants and tokio for async file operations.

```rust
use windows_sys::Win32::Storage::FileSystem::SECURITY_IDENTIFICATION;
use tokio::fs::OpenOptions;

let file = OpenOptions::new()
    .write(true)
    .create(true)
    // Sets the flag value to `SecurityIdentification`.
    .security_qos_flags(SECURITY_IDENTIFICATION)
    .open(r"\\.\pipe\MyPipe").await?;
```

--------------------------------

### Tokio Broadcast Channel Sender Length Example (Rust)

Source: https://docs.rs/tokio/latest/tokio/sync/broadcast/struct.Sender

Shows how to use the `len` method on a Tokio broadcast channel `Sender` to get the number of queued values. It explains that a value is considered queued until all receivers alive at the time of sending have seen it.

```Rust
use tokio::sync::broadcast;

let (tx, mut rx1) = broadcast::channel(16);
let mut rx2 = tx.subscribe();

tx.send(10).unwrap();
tx.send(20).unwrap();
tx.send(30).unwrap();

assert_eq!(tx.len(), 3);

rx1.recv().await.unwrap();

// The len is still 3 since rx2 hasn't seen the first value yet.
assert_eq!(tx.len(), 3);

rx2.recv().await.unwrap();

assert_eq!(tx.len(), 2);
```

--------------------------------

### SetOnce with Arc for Shared Access

Source: https://docs.rs/tokio/latest/tokio/sync/struct.SetOnce

Illustrates using SetOnce with Arc for shared ownership across multiple tasks. This example highlights setting a value from one task and waiting for it in another, demonstrating thread-safe asynchronous initialization.

```rust
use tokio::sync::{SetOnce, SetOnceError};
use std::sync::Arc;

let once = SetOnce::new();

let arc = Arc::new(once);
let first_cl = Arc::clone(&arc);
let second_cl = Arc::clone(&arc);

// set the value inside a task
tokio::spawn(async move { first_cl.set(20) }).await.unwrap()?;

// wait inside task to not block the main thread
tokio::spawn(async move {
    // wait inside async context for the value to be set
    assert_eq!(*second_cl.wait().await, 20);
}).await.unwrap();

// subsequent set calls will fail
assert!(arc.set(30).is_err());

println!("{:?}", arc.get());

Ok(())

```

--------------------------------

### Get Current Runtime ID with Tokio Handle

Source: https://docs.rs/tokio/latest/tokio/runtime/struct.Id

Demonstrates how to retrieve the current runtime's ID using the tokio::runtime::Handle::current() method. This example uses the multi_thread runtime flavor with 4 worker threads and prints the runtime ID to stdout.

```rust
use tokio::runtime::Handle;

#[tokio::main(flavor = "multi_thread", worker_threads = 4)]
async fn main() {
  println!("Current runtime id: {}", Handle::current().id());
}
```

--------------------------------

### Tokio Watch Channel: Print Initial and Updated Values

Source: https://docs.rs/tokio/latest/tokio/sync/watch/index

This example demonstrates how to use a Tokio watch channel to send an initial value and then update it. It uses a loop with `rx.changed().await` to process values and detect when the channel is closed.

```rust
use tokio::sync::watch;
use tokio::time::{Duration, sleep};

let (tx, mut rx) = watch::channel("hello");

tokio::spawn(async move {
    // Use the equivalent of a "do-while" loop so the initial value is
    // processed before awaiting the `changed()` future.
    loop {
        println!("{}! ", *rx.borrow_and_update());
        if rx.changed().await.is_err() {
            break;
        }
    }
});

sleep(Duration::from_millis(100)).await;
tx.send("world")?;
```

--------------------------------

### tokio::io::Stderr Example

Source: https://docs.rs/tokio/latest/tokio/io/struct.Stderr

Demonstrates how to use the `Stderr` struct from `tokio::io` to write data to the standard error stream asynchronously. This example requires the `tokio` runtime and the `io` module. It writes a byte string to stderr and handles potential I/O errors.

```rust
use tokio::io::{self, AsyncWriteExt};

#[tokio::main]
async fn main() -> io::Result<()> {
    let mut stderr = io::stdout();
    stderr.write_all(b"Print some error here.").await?;
    Ok(())
}
```

--------------------------------

### Tokio MPSC Channel Capacity Management Example (Rust)

Source: https://docs.rs/tokio/latest/tokio/sync/mpsc/struct.Receiver

Demonstrates how channel capacity changes when sending messages, reserving capacity, and receiving messages in Tokio's MPSC channel.

```rust
use tokio::sync::mpsc;

let (tx, mut rx) = mpsc::channel::<()>(5);

assert_eq!(rx.capacity(), 5);

// Making a reservation drops the capacity by one.
let permit = tx.reserve().await.unwrap();
assert_eq!(rx.capacity(), 4);
assert_eq!(rx.len(), 0);

// Sending and receiving a value increases the capacity by one.
permit.send(());
assert_eq!(rx.len(), 1);
rx.recv().await.unwrap();
assert_eq!(rx.capacity(), 5);

// Directly sending a message drops the capacity by one.
tx.send(()).await.unwrap();
assert_eq!(rx.capacity(), 4);
assert_eq!(rx.len(), 1);

// Receiving the message increases the capacity by one.
rx.recv().await.unwrap();
assert_eq!(rx.capacity(), 5);
assert_eq!(rx.len(), 0);
```

--------------------------------

### Create Directory Asynchronously with Tokio (Rust)

Source: https://docs.rs/tokio/latest/tokio/fs/struct.DirBuilder

An example of using DirBuilder to asynchronously create a directory, including nested parent directories, using Tokio's runtime. It handles potential I/O errors during creation.

```rust
use tokio::fs::DirBuilder;
use std::io;

#[tokio::main]
async fn main() -> io::Result<()> {
    DirBuilder::new()
        .recursive(true)
        .create("/tmp/foo/bar/baz")
        .await?;

    Ok(())
}
```

--------------------------------

### Create New OpenOptions Instance in Rust

Source: https://docs.rs/tokio/latest/tokio/net/unix/pipe/struct.OpenOptions

Illustrates the creation of a new, blank OpenOptions instance. All configuration options are initially set to their default values (typically `false`), ready to be modified.

```rust
use tokio::net::unix::pipe;

let options = pipe::OpenOptions::new();
```

--------------------------------

### Tokio MPSC Receiver: Receive Buffered Values (async)

Source: https://docs.rs/tokio/latest/tokio/sync/mpsc/struct.Receiver

Illustrates receiving multiple buffered values from a Tokio mpsc channel receiver. The `recv` method can be called repeatedly to get messages as they become available. This example shows receiving two messages that were sent sequentially.

```Rust
use tokio::sync::mpsc;

let (tx, mut rx) = mpsc::channel(100);

tx.send("hello").await.unwrap();
tx.send("world").await.unwrap();

assert_eq!(Some("hello"), rx.recv().await);
assert_eq!(Some("world"), rx.recv().await);
```

--------------------------------

### Send Timeout Example using Tokio MPSC Channel

Source: https://docs.rs/tokio/latest/tokio/sync/mpsc/struct.Sender

Demonstrates sending values into an MPSC channel with a timeout. If the timeout elapses before a value can be sent (e.g., channel is full), an error is returned. This example uses `tokio::sync::mpsc::channel` and `tx.send_timeout`.

```Rust
use tokio::sync::mpsc;
use tokio::time::{sleep, Duration};

let (tx, mut rx) = mpsc::channel(1);

tokio::spawn(async move {
    for i in 0..10 {
        if let Err(e) = tx.send_timeout(i, Duration::from_millis(100)).await {
            println!("send error: #{:?}", e);
            return;
        }
    }
});

while let Some(i) = rx.recv().await {
    println!("got = {}", i);
    sleep(Duration::from_millis(200)).await;
}
```

--------------------------------

### Get Runtime ID with Handle::id (Rust - Unstable)

Source: https://docs.rs/tokio/latest/tokio/runtime/struct.Handle

The `Handle::id` method, available on `tokio_unstable`, returns the `Id` of the current `Runtime`. This is an unstable API, and its behavior may change in future releases. The example shows how to print the runtime ID within a `tokio::main` function.

```rust
use tokio::runtime::Handle;

#[tokio::main(flavor = "current_thread")]
async fn main() {
  println!("Current runtime id: {}", Handle::current().id());
}
```

--------------------------------

### UnixDatagram: Bind and Send/Receive with Named Sockets (Rust)

Source: https://docs.rs/tokio/latest/tokio/net/struct.UnixDatagram

Demonstrates how to create, bind, send, and receive data using named UnixDatagram sockets. It utilizes temporary directories to manage socket file lifecycles. This example requires the 'net' feature flag and the 'tempfile' crate.

```rust
use tokio::net::UnixDatagram;
use tempfile::tempdir;

// We use a temporary directory so that the socket
// files left by the bound sockets will get cleaned up.
let tmp = tempdir()?;

// Bind each socket to a filesystem path
let tx_path = tmp.path().join("tx");
let tx = UnixDatagram::bind(&tx_path)?;
let rx_path = tmp.path().join("rx");
let rx = UnixDatagram::bind(&rx_path)?;

let bytes = b"hello world";
tx.send_to(bytes, &rx_path).await?;

let mut buf = vec![0u8; 24];
let (size, addr) = rx.recv_from(&mut buf).await?;

let dgram = &buf[..size];
assert_eq!(dgram, bytes);
assert_eq!(addr.as_pathname().unwrap(), &tx_path);

```

--------------------------------

### Async TCP Server with tokio::main

Source: https://docs.rs/tokio/latest/tokio/runtime/index

Demonstrates a basic asynchronous TCP server using the `tokio::main` attribute macro. It binds to a port, accepts connections, and spawns a new task for each connection to echo received data back to the client. This is suitable for applications where fine-tuning of the runtime is not required.

```rust
use tokio::net::TcpListener;
use tokio::io::{AsyncReadExt, AsyncWriteExt};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let listener = TcpListener::bind("127.0.0.1:8080").await?;

    loop {
        let (mut socket, _) = listener.accept().await?;

        tokio::spawn(async move {
            let mut buf = [0; 1024];

            // In a loop, read data from the socket and write the data back.
            loop {
                let n = match socket.read(&mut buf).await {
                    // socket closed
                    Ok(0) => return,
                    Ok(n) => n,
                    Err(e) => {
                        println!("failed to read from socket; err = {:?}", e);
                        return;
                    }
                };

                // Write the data back
                if let Err(e) = socket.write_all(&buf[0..n]).await {
                    println!("failed to write to socket; err = {:?}", e);
                    return;
                }
            }
        });
    }
}
```

--------------------------------

### Get Runtime Flavor with Handle::runtime_flavor (Rust)

Source: https://docs.rs/tokio/latest/tokio/runtime/struct.Handle

The `Handle::runtime_flavor` method returns the flavor of the current `Runtime` (e.g., `CurrentThread` or `MultiThread`). This is useful for conditionally executing code based on the runtime's configuration. The example demonstrates asserting the runtime flavor within a `tokio::main` function.

```rust
use tokio::runtime::{Handle, RuntimeFlavor};

#[tokio::main(flavor = "current_thread")]
async fn main() {
  assert_eq!(RuntimeFlavor::CurrentThread, Handle::current().runtime_flavor());
}
```

```rust
use tokio::runtime::{Handle, RuntimeFlavor};

#[tokio::main(flavor = "multi_thread", worker_threads = 4)]
async fn main() {
  assert_eq!(RuntimeFlavor::MultiThread, Handle::current().runtime_flavor());
}
```

--------------------------------

### Tokio UdpSocket: Concurrent Send/Recv with ready()

Source: https://docs.rs/tokio/latest/tokio/net/struct.UdpSocket

This example shows how to concurrently send and receive data on the same UdpSocket using the `ready()` method in Tokio. It waits for both readable and writable interests, demonstrating robust handling of network events and potential "WouldBlock" errors.

```rust
use tokio::io::{self, Interest};
use tokio::net::UdpSocket;

#[tokio::main]
async fn main() -> io::Result<()> {
    let socket = UdpSocket::bind("127.0.0.1:8080").await?;
    socket.connect("127.0.0.1:8081").await?;

    loop {
        let ready = socket.ready(Interest::READABLE | Interest::WRITABLE).await?;

        if ready.is_readable() {
            let mut data = [0; 1024];
            match socket.try_recv(&mut data[..]) {
                Ok(n) => {
                    println!("received {:?}", &data[..n]);
                }
                Err(ref e) if e.kind() == io::ErrorKind::WouldBlock => {} // False-positive, continue
                Err(e) => {
                    return Err(e);
                }
            }
        }

        if ready.is_writable() {
            match socket.try_send(b"hello world") {
                Ok(n) => {
                    println!("sent {} bytes", n);
                }
                Err(ref e) if e.kind() == io::ErrorKind::WouldBlock => {} // False-positive, continue
                Err(e) => {
                    return Err(e);
                }
            }
        }
    }
}
```

--------------------------------

### Get Command Exit Status with Tokio

Source: https://docs.rs/tokio/latest/tokio/process/struct.Command

This example shows how to execute a command using tokio::process::Command and wait for its exit status without collecting its output. By default, stdin, stdout, and stderr are inherited from the parent process. This method is suitable when you only need to know if a command succeeded or failed.

```rust
use tokio::process::Command;

async fn run_ls() -> std::process::ExitStatus {
    Command::new("ls")
        .status()
        .await
        .expect("ls command failed to run")
}
```

--------------------------------

### Bind UdpSocket to an Address

Source: https://docs.rs/tokio/latest/tokio/net/struct.UdpSocket

Example of binding a Tokio UdpSocket to a specific IP address and port. This is a fundamental step before sending or receiving data.

```rust
use tokio::net::UdpSocket;
use std::io;

#[tokio::main]
async fn main() -> io::Result<()> {
    let sock = UdpSocket::bind("0.0.0.0:8080").await?;
    // use `sock`
    Ok(())
}
```

--------------------------------

### OwnedSemaphorePermit: Get Number of Permits (Rust)

Source: https://docs.rs/tokio/latest/tokio/sync/struct.OwnedSemaphorePermit

Shows how to get the number of permits currently held by an `OwnedSemaphorePermit` instance.

```rust
use std::sync::Arc;
use tokio::sync::Semaphore;

let sem = Arc::new(Semaphore::new(5));
let permit = sem.try_acquire_many_owned(3).unwrap();

assert_eq!(permit.num_permits(), 3);
```