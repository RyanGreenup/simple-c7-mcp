# Granian

Granian is a high-performance Rust HTTP server for Python applications, built on top of Hyper and Tokio. It provides a single, unified HTTP implementation supporting HTTP/1, HTTP/2, HTTPS, mTLS, and WebSockets, while offering stable performance across ASGI, RSGI (a Rust-native protocol), and WSGI interfaces. The server eliminates the traditional Gunicorn + uvicorn + http-tools dependency stack on Unix systems by providing everything in a single package across multiple platforms.

The core design philosophy prioritizes throughput and concurrency by offloading I/O operations to a Rust runtime while maintaining Python application compatibility. Granian is particularly well-suited for applications requiring high concurrency with websockets, HTTP/2 performance optimization, or those seeking a modern single-dependency server solution. It is used in production by notable projects including paperless-ngx, reflex, searxng, and Weblate, as well as companies like Microsoft, Mozilla, and Sentry.

## CLI - Running Granian from Command Line

The primary way to run Granian is through its command-line interface. The CLI provides extensive configuration options for network binding, worker management, HTTP settings, SSL/TLS, logging, and development features like auto-reload.

```bash
# Basic ASGI application
granian --interface asgi main:app

# RSGI application (Granian's native interface)
granian --interface rsgi main:app

# WSGI application
granian --interface wsgi main:app

# Full production configuration
granian --interface asgi main:app \
    --host 0.0.0.0 \
    --port 8000 \
    --workers 4 \
    --http auto \
    --ws \
    --backlog 2048 \
    --log-level info \
    --access-log

# With SSL/TLS enabled
granian --interface asgi main:app \
    --ssl-certificate /path/to/cert.pem \
    --ssl-keyfile /path/to/key.pem \
    --ssl-protocol-min tls1.2

# Development mode with auto-reload
granian --interface asgi main:app --reload --reload-paths ./src

# Unix Domain Socket binding
granian --interface asgi main:app --uds /tmp/granian.sock

# Worker resource management
granian --interface asgi main:app \
    --workers 4 \
    --workers-lifetime 1h \
    --workers-max-rss 512 \
    --respawn-failed-workers

# Environment variables can configure all options (prefix GRANIAN_)
GRANIAN_HOST=0.0.0.0 GRANIAN_PORT=8080 granian --interface asgi main:app
```

## Granian Server Class - Programmatic Python API

The `Granian` (aliased from `Server`) class provides programmatic control over the server, allowing integration into Python applications with full configuration access and lifecycle hooks.

```python
from granian import Granian
from granian.constants import Interfaces, HTTPModes, Loops
from granian.http import HTTP1Settings, HTTP2Settings
from granian.log import LogLevels

# Basic server instantiation
server = Granian(
    target="myapp:application",
    address="127.0.0.1",
    port=8000,
    interface=Interfaces.ASGI,
)
server.serve()

# Full configuration example
server = Granian(
    target="myapp:application",
    address="0.0.0.0",
    port=8000,
    interface=Interfaces.ASGI,
    workers=4,
    runtime_threads=2,
    blocking_threads=None,  # Auto-configured based on interface
    http=HTTPModes.auto,
    websockets=True,
    backlog=1024,
    backpressure=None,  # Defaults to backlog/workers
    http1_settings=HTTP1Settings(
        header_read_timeout=30000,
        keep_alive=True,
        max_buffer_size=417792,
        pipeline_flush=False,
    ),
    http2_settings=HTTP2Settings(
        adaptive_window=False,
        initial_connection_window_size=1048576,
        initial_stream_window_size=1048576,
        keep_alive_timeout=20,
        max_concurrent_streams=200,
    ),
    log_enabled=True,
    log_level=LogLevels.info,
    log_access=True,
    ssl_cert=None,
    ssl_key=None,
    factory=False,  # Set True if target is a factory function
)

# Lifecycle hooks
@server.on_startup
def startup_handler():
    print("Server starting up")

@server.on_reload
def reload_handler():
    print("Server reloading")

@server.on_shutdown
def shutdown_handler():
    print("Server shutting down")

server.serve()
```

## Embedded Server - Async Integration

The embedded server allows Granian to run within an existing asyncio application, providing async interfaces for advanced lifecycle management. This is useful for projects that need to control the server programmatically within their own event loop.

```python
import asyncio
from granian.server.embed import Server
from granian.constants import Interfaces

async def my_asgi_app(scope, receive, send):
    if scope['type'] == 'http':
        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [[b'content-type', b'text/plain']],
        })
        await send({
            'type': 'http.response.body',
            'body': b'Hello from embedded server!',
        })

async def main():
    # Create embedded server (accepts app object directly, not import string)
    server = Server(
        target=my_asgi_app,
        address="127.0.0.1",
        port=8000,
        interface=Interfaces.ASGI,
    )

    # Run server as a task alongside other application logic
    server_task = asyncio.create_task(server.serve())

    # Your application logic here
    await asyncio.sleep(60)

    # Graceful shutdown
    server.stop()
    await server_task

# Alternative: reload without stopping
async def with_reload():
    server = Server(target=my_asgi_app, interface=Interfaces.ASGI)
    server_task = asyncio.create_task(server.serve())

    # Trigger reload (reloads workers without full restart)
    server.reload()

    await asyncio.sleep(30)
    server.stop()
    await server_task

asyncio.run(main())
```

## ASGI Interface - Standard Async Server Gateway

Granian fully supports ASGI/3 applications with optional lifespan protocol handling. Use `asgi` interface for full lifespan support or `asginl` to skip lifespan handling.

```python
# Standard ASGI application
async def app(scope, receive, send):
    assert scope['type'] == 'http'

    # Read request body
    body = b''
    while True:
        message = await receive()
        body += message.get('body', b'')
        if not message.get('more_body', False):
            break

    # Send response
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'application/json'],
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': b'{"message": "Hello, World!"}',
    })

# ASGI with lifespan protocol
async def app_with_lifespan(scope, receive, send):
    if scope['type'] == 'lifespan':
        while True:
            message = await receive()
            if message['type'] == 'lifespan.startup':
                # Initialize resources (database connections, etc.)
                await send({'type': 'lifespan.startup.complete'})
            elif message['type'] == 'lifespan.shutdown':
                # Cleanup resources
                await send({'type': 'lifespan.shutdown.complete'})
                return

    elif scope['type'] == 'http':
        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [[b'content-type', b'text/plain']],
        })
        await send({
            'type': 'http.response.body',
            'body': b'Hello!',
        })

# Run with: granian --interface asgi main:app
# Or without lifespan: granian --interface asginl main:app
```

## RSGI Interface - Rust-Native High Performance Protocol

RSGI (Rust Server Gateway Interface) is Granian's native protocol designed for maximum performance by eliminating ASGI's message-passing overhead. It provides direct method calls for responses and efficient body streaming.

```python
# Basic RSGI HTTP application
async def app(scope, proto):
    assert scope.proto == 'http'

    # Read entire body at once
    body = await proto()

    # Or stream body in chunks
    # async for chunk in proto:
    #     process(chunk)

    # Response methods (choose one):
    proto.response_str(
        status=200,
        headers=[('content-type', 'text/plain')],
        body="Hello, World!"
    )

# RSGI with all response types
async def comprehensive_app(scope, proto):
    if scope.proto == 'http':
        path = scope.path

        if path == '/empty':
            proto.response_empty(status=204, headers=[])

        elif path == '/text':
            proto.response_str(
                status=200,
                headers=[('content-type', 'text/plain')],
                body="Text response"
            )

        elif path == '/bytes':
            proto.response_bytes(
                status=200,
                headers=[('content-type', 'application/octet-stream')],
                body=b'\x00\x01\x02\x03'
            )

        elif path == '/file':
            proto.response_file(
                status=200,
                headers=[('content-type', 'image/png')],
                file='/path/to/image.png'
            )

        elif path == '/stream':
            # Streaming response
            transport = proto.response_stream(
                status=200,
                headers=[('content-type', 'text/event-stream')]
            )
            await transport.send_str("data: event 1\n\n")
            await transport.send_str("data: event 2\n\n")
            await transport.send_bytes(b"data: binary\n\n")

# RSGI with lifecycle methods (class-based)
class App:
    def __rsgi_init__(self, loop):
        """Called during server startup with the asyncio event loop"""
        # Initialize resources
        loop.run_until_complete(self.setup_database())

    async def setup_database(self):
        # Async initialization
        pass

    def __rsgi_del__(self, loop):
        """Called during server shutdown"""
        loop.run_until_complete(self.cleanup())

    async def cleanup(self):
        # Async cleanup
        pass

    async def __rsgi__(self, scope, proto):
        """Main request handler"""
        proto.response_str(200, [], "Hello from RSGI class!")

app = App()
# Run with: granian --interface rsgi main:app
```

## RSGI WebSocket Protocol

RSGI provides efficient WebSocket handling with direct transport access and typed messages.

```python
from granian.rsgi import WebsocketMessageType

async def websocket_app(scope, proto):
    if scope.proto == 'ws':
        # Accept the WebSocket connection
        transport = await proto.accept()

        try:
            while True:
                # Receive message
                message = await transport.receive()

                if message.kind == WebsocketMessageType.close:
                    break
                elif message.kind == WebsocketMessageType.bytes:
                    # Echo binary data
                    await transport.send_bytes(message.data)
                elif message.kind == WebsocketMessageType.string:
                    # Echo text data
                    await transport.send_str(f"Echo: {message.data}")

        except Exception:
            pass

    elif scope.proto == 'http':
        proto.response_str(200, [], "WebSocket endpoint")

# Alternative: reject WebSocket connection
async def reject_ws(scope, proto):
    if scope.proto == 'ws':
        # Close with status code
        proto.close(status=4000)

# Run with: granian --interface rsgi --ws main:websocket_app
```

## WSGI Interface - Synchronous Application Support

Granian supports traditional synchronous WSGI applications, handling the GIL and threading automatically for optimal performance.

```python
def app(environ, start_response):
    """Standard WSGI application"""
    path = environ.get('PATH_INFO', '/')
    method = environ.get('REQUEST_METHOD', 'GET')

    if method == 'POST':
        # Read request body
        content_length = int(environ.get('CONTENT_LENGTH', 0))
        body = environ['wsgi.input'].read(content_length)

    # Send response
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)

    return [b"Hello from WSGI!"]

# WSGI with iterator response (for streaming)
def streaming_app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])

    def generate():
        for i in range(10):
            yield f"Chunk {i}\n".encode()

    return generate()

# Flask/Django integration
from flask import Flask
flask_app = Flask(__name__)

@flask_app.route('/')
def hello():
    return "Hello from Flask on Granian!"

# Run with: granian --interface wsgi main:flask_app
# Or: granian --interface wsgi "myproject.wsgi:application" (Django)
```

## Proxy Headers Middleware

Granian provides middleware wrappers for applications running behind reverse proxies, handling `X-Forwarded-For` and `X-Forwarded-Proto` headers securely.

```python
from granian.utils.proxies import (
    wrap_asgi_with_proxy_headers,
    wrap_wsgi_with_proxy_headers,
)

# ASGI application with proxy support
async def my_asgi_app(scope, receive, send):
    # scope['client'] and scope['scheme'] will be updated from proxy headers
    client_ip = scope['client'][0]
    scheme = scope['scheme']

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [[b'content-type', b'text/plain']],
    })
    await send({
        'type': 'http.response.body',
        'body': f"Your IP: {client_ip}, Scheme: {scheme}".encode(),
    })

# Wrap with specific trusted hosts
app = wrap_asgi_with_proxy_headers(
    my_asgi_app,
    trusted_hosts="192.168.1.1"  # Single IP
)

# Multiple trusted hosts
app = wrap_asgi_with_proxy_headers(
    my_asgi_app,
    trusted_hosts=["192.168.1.1", "10.0.0.0/8"]  # IP and CIDR range
)

# Trust all hosts (use with caution!)
app = wrap_asgi_with_proxy_headers(my_asgi_app, trusted_hosts="*")

# WSGI equivalent
def my_wsgi_app(environ, start_response):
    # environ['REMOTE_ADDR'] and environ['wsgi.url_scheme'] will be updated
    client_ip = environ['REMOTE_ADDR']
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [f"Your IP: {client_ip}".encode()]

wsgi_app = wrap_wsgi_with_proxy_headers(my_wsgi_app, trusted_hosts="127.0.0.1")
```

## Custom Event Loop Registration

Granian allows customization of the asyncio event loop initialization through its loops registry, enabling integration with alternative event loop implementations.

```python
import asyncio
from granian import Granian, loops

# Override the 'auto' loop policy
@loops.register('auto')
def build_custom_loop():
    # Example: Use selector event loop on Windows
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    return asyncio.new_event_loop()

# Register a completely custom loop implementation
@loops.register('custom', packages=['my_custom_loop'])
def build_my_loop(my_custom_loop):
    loop = my_custom_loop.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop

# Use the custom loop
server = Granian(
    target="main:app",
    interface="asgi",
    loop="custom",  # Reference your registered loop
)
server.serve()

# Available built-in loops:
# - 'auto': Automatically selects best available (rloop > uvloop > winloop > asyncio)
# - 'asyncio': Standard library asyncio
# - 'uvloop': uvloop (requires granian[uvloop])
# - 'rloop': rloop (requires granian[rloop])
# - 'winloop': winloop for Windows (requires granian[winloop])
```

## HTTP Settings Configuration

Fine-tune HTTP/1 and HTTP/2 protocol settings for optimal performance based on your application's needs.

```python
from granian import Granian
from granian.http import HTTP1Settings, HTTP2Settings

server = Granian(
    target="main:app",
    interface="asgi",
    http1_settings=HTTP1Settings(
        header_read_timeout=30000,  # 30 seconds in milliseconds
        keep_alive=True,            # Enable HTTP/1.1 keep-alive
        max_buffer_size=417792,     # ~408KB buffer
        pipeline_flush=False,       # Experimental pipelining support
    ),
    http2_settings=HTTP2Settings(
        adaptive_window=False,              # Adaptive flow control
        initial_connection_window_size=1048576,  # 1MB connection window
        initial_stream_window_size=1048576,      # 1MB stream window
        keep_alive_interval=None,           # Ping interval (ms), None to disable
        keep_alive_timeout=20,              # Ping timeout (seconds)
        max_concurrent_streams=200,         # Max concurrent HTTP/2 streams
        max_frame_size=16384,               # 16KB frame size
        max_headers_size=16777216,          # 16MB max header size
        max_send_buffer_size=409600,        # 400KB send buffer per stream
    ),
)
server.serve()

# CLI equivalent:
# granian --interface asgi main:app \
#     --http1-keep-alive \
#     --http1-buffer-size 417792 \
#     --http2-max-concurrent-streams 200 \
#     --http2-keep-alive-timeout 20
```

## Logging Configuration

Granian uses Python's standard logging module with two loggers: `_granian` for runtime messages and `granian.access` for access logs.

```python
import logging
import json
from granian import Granian
from granian.log import LogLevels

# Basic logging configuration
server = Granian(
    target="main:app",
    interface="asgi",
    log_enabled=True,
    log_level=LogLevels.info,
    log_access=True,
    log_access_format='[%(time)s] %(addr)s - "%(method)s %(path)s %(protocol)s" %(status)d %(dt_ms).3f',
)

# Custom logging with dictconfig
log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "custom": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    },
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": "granian.log",
            "formatter": "custom"
        }
    },
    "loggers": {
        "_granian": {"handlers": ["file"], "level": "INFO"},
        "granian.access": {"handlers": ["file"], "level": "INFO"}
    }
}

server = Granian(
    target="main:app",
    interface="asgi",
    log_dictconfig=log_config,
)

# Access log format atoms:
# %(addr)s      - Client remote address
# %(time)s      - Datetime of request
# %(dt_ms).3f   - Request duration in milliseconds
# %(status)d    - HTTP response status code
# %(path)s      - Request path (without query string)
# %(query_string)s - Request query string
# %(method)s    - HTTP method
# %(scheme)s    - URL scheme (http/https)
# %(protocol)s  - HTTP protocol version

# CLI with JSON config file:
# granian --interface asgi main:app --log-config logging.json --access-log
```

## Static File Serving

Granian can serve static files directly without requiring a separate web server or middleware.

```python
from granian import Granian

server = Granian(
    target="main:app",
    interface="asgi",
    static_path_route="/static",          # URL path prefix
    static_path_mount="./public",          # Local directory to serve
    static_path_expires=86400,             # Cache-Control max-age (1 day)
)
server.serve()

# CLI equivalent:
# granian --interface asgi main:app \
#     --static-path-route /static \
#     --static-path-mount ./public \
#     --static-path-expires 86400

# Disable caching:
# granian --interface asgi main:app \
#     --static-path-route /assets \
#     --static-path-mount ./assets \
#     --static-path-expires 0
```

## Worker Management and Resource Limits

Configure worker processes, lifetime limits, memory constraints, and automatic respawning for production deployments.

```python
from granian import Granian

server = Granian(
    target="main:app",
    interface="asgi",
    workers=4,                      # Number of worker processes
    runtime_threads=1,              # Rust runtime threads per worker
    runtime_blocking_threads=512,   # I/O blocking threads per worker
    blocking_threads=1,             # Python interpreter threads (WSGI only: can be > 1)
    blocking_threads_idle_timeout=30,  # Idle thread shutdown timeout
    backlog=1024,                   # Global connection backlog
    backpressure=256,               # Max concurrent requests per worker

    # Worker lifecycle
    workers_lifetime=3600,          # Respawn workers after 1 hour
    workers_max_rss=512,            # Respawn if memory exceeds 512 MiB
    workers_kill_timeout=30,        # Force kill after 30s if graceful shutdown fails
    respawn_failed_workers=True,    # Auto-respawn crashed workers
    respawn_interval=3.5,           # Delay between respawns

    # Resource monitoring
    rss_sample_interval=30,         # Memory check interval
    rss_samples=1,                  # Consecutive samples over limit before respawn
)
server.serve()

# CLI equivalent:
# granian --interface asgi main:app \
#     --workers 4 \
#     --workers-lifetime 1h \
#     --workers-max-rss 512 \
#     --workers-kill-timeout 30s \
#     --respawn-failed-workers \
#     --backpressure 256

# Duration formats supported: 30 (seconds), 30s, 5m, 1h, 1d, 1h30m
```

## SSL/TLS and mTLS Configuration

Enable HTTPS with certificate configuration and optional mutual TLS (mTLS) for client verification.

```python
from granian import Granian
from granian.constants import SSLProtocols

# Basic HTTPS
server = Granian(
    target="main:app",
    interface="asgi",
    ssl_cert="/path/to/certificate.pem",
    ssl_key="/path/to/private-key.pem",  # PKCS#8 format only
    ssl_key_password="optional-password",
    ssl_protocol_min=SSLProtocols.tls13,  # Minimum TLS 1.3
)

# mTLS with client certificate verification
server = Granian(
    target="main:app",
    interface="asgi",
    ssl_cert="/path/to/server-cert.pem",
    ssl_key="/path/to/server-key.pem",
    ssl_ca="/path/to/ca-cert.pem",           # CA for client verification
    ssl_crl=["/path/to/revocation-list.pem"], # Certificate revocation lists
    ssl_client_verify=True,                   # Require valid client cert
    ssl_protocol_min=SSLProtocols.tls12,
)
server.serve()

# CLI equivalent:
# granian --interface asgi main:app \
#     --ssl-certificate /path/to/cert.pem \
#     --ssl-keyfile /path/to/key.pem \
#     --ssl-protocol-min tls1.3 \
#     --ssl-ca /path/to/ca.pem \
#     --ssl-client-verify
```

## Summary

Granian serves as a modern, high-performance HTTP server that bridges the gap between Python web applications and Rust's efficient networking capabilities. Its primary use cases include serving production ASGI applications (like FastAPI, Starlette, or Django ASGI), running WSGI applications (Flask, Django) with better concurrency handling, and building performance-critical services using the RSGI protocol. The server excels in scenarios requiring HTTP/2, websockets, or high throughput where traditional Python servers become bottlenecks.

Integration patterns typically involve either CLI-based deployment for straightforward production use or programmatic Server instantiation for applications requiring custom lifecycle management. For microservices and containerized deployments, Granian's single-worker-per-container model with Kubernetes or Docker orchestration is recommended. The embedded server mode enables advanced use cases where Granian needs to coexist with other asyncio tasks. When running behind reverse proxies like Nginx or cloud load balancers, the proxy headers middleware ensures correct client IP and protocol detection while maintaining security through trusted host verification.
