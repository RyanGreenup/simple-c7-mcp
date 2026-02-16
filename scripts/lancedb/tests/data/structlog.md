# structlog: Structured Logging for Python

structlog is a production-ready structured logging library for Python that transforms traditional string-based logging into dictionary-based structured data. It provides a flexible, powerful approach to logging by treating log entries as dictionaries that can be progressively built up with context, then processed through a customizable pipeline of processors before being rendered in various formats (JSON, logfmt, console output). The library works as a standalone solution or integrates seamlessly with Python's standard library logging module, making it suitable for applications of any scale.

Since 2013, structlog has been battle-tested in production environments across different scales and paradigms, from synchronous applications to async frameworks. Its core philosophy centers on simplicity through functions that operate on dictionaries, combined with powerful context management through bound loggers that accumulate key-value pairs across the application lifecycle. The library embraces modern Python features including asyncio, context variables for concurrency-safe logging, type hints, and provides zero-cost abstractions through lazy evaluation and optional caching for high-performance scenarios.

## Core APIs and Functions

### Basic Logger Creation and Usage

Get a configured logger instance and log structured data with automatic timestamp and formatting.

```python
import structlog

# Get a logger instance
log = structlog.get_logger()

# Simple logging with structured data
log.info("user_login", username="alice", ip="192.168.1.100", success=True)
# Output: 2025-12-10 10:30:45 [info     ] user_login    username=alice ip=192.168.1.100 success=True

# Log with positional string formatting
log.warning("failed attempt: %s", "invalid_password", user="bob", attempts=3)
# Output: 2025-12-10 10:30:46 [warning  ] failed attempt: invalid_password user=bob attempts=3

# Log different severity levels
log.debug("processing_request", request_id="req-123")
log.error("database_error", error="connection_timeout", query="SELECT * FROM users")
log.critical("system_failure", component="auth_service", status="down")
```

### Context Binding with bind()

Build up logging context progressively by binding key-value pairs that persist across multiple log calls.

```python
import structlog

# Start with base logger
log = structlog.get_logger()

# Bind user context
log = log.bind(user_id=42, session="sess-abc123")

# This log entry includes the bound context
log.info("page_view", page="/dashboard")
# Output: user_id=42 session=sess-abc123 page=/dashboard event=page_view

# Bind additional context
log = log.bind(request_id="req-456")

# All subsequent logs include all bound context
log.info("api_call", endpoint="/api/data", method="GET")
# Output: user_id=42 session=sess-abc123 request_id=req-456 endpoint=/api/data method=GET event=api_call

# Original logger is unchanged (immutable)
base_log = structlog.get_logger()
base_log.info("server_start")
# Output: event=server_start (no bound context)
```

### Context Variables for Async and Thread Safety

Use context variables for globally accessible, concurrency-safe logging context across async tasks and threads.

```python
import structlog
from structlog.contextvars import (
    bind_contextvars,
    unbind_contextvars,
    clear_contextvars,
    bound_contextvars,
    get_contextvars
)

# Configure structlog to merge context variables
structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.dev.ConsoleRenderer(),
    ]
)

# Bind global context (available to all loggers)
bind_contextvars(request_id="req-789", trace_id="trace-xyz")

log = structlog.get_logger()
log.info("processing")
# Output: request_id=req-789 trace_id=trace-xyz event=processing

# Use as context manager
with bound_contextvars(user="alice", action="checkout"):
    log.info("payment_start")
    # Output: request_id=req-789 trace_id=trace-xyz user=alice action=checkout event=payment_start
# Context automatically restored after with-block

log.info("after_context")
# Output: request_id=req-789 trace_id=trace-xyz event=after_context

# Clear all context variables
clear_contextvars()
log.info("clean_slate")
# Output: event=clean_slate

# Get current context as dict
bind_contextvars(env="production", version="1.2.3")
context = get_contextvars()
print(context)
# Output: {'env': 'production', 'version': '1.2.3'}
```

### Global Configuration with configure()

Configure the global logging behavior including processors, output format, and integration with stdlib logging.

```python
import structlog
import logging
import sys

# Full custom configuration
structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.StackInfoRenderer(),
        structlog.processors.TimeStamper(fmt="iso", utc=True),
        structlog.processors.JSONRenderer()
    ],
    wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
    context_class=dict,
    logger_factory=structlog.PrintLoggerFactory(file=sys.stderr),
    cache_logger_on_first_use=True
)

log = structlog.get_logger()
log.debug("not_shown")  # Filtered out (level < INFO)
log.info("api_request", method="POST", path="/users", status=201)
# Output: {"event": "api_request", "method": "POST", "path": "/users", "status": 201, "level": "info", "timestamp": "2025-12-10T10:30:45.123456Z"}

# Check if structlog is configured
if structlog.is_configured():
    print("structlog is configured")

# Get current configuration
config = structlog.get_config()
print(config["logger_factory"])
# Output: <structlog.PrintLoggerFactory object>

# Reset to defaults
structlog.reset_defaults()
```

### Standard Library Integration

Integrate structlog with Python's standard library logging for compatibility with existing logging infrastructure.

```python
import logging
import structlog

# Configure structlog to use stdlib logging
structlog.stdlib.recreate_defaults(log_level=logging.INFO)

# This now uses stdlib logging under the hood
log = structlog.get_logger("myapp")
log.info("application_start", version="2.0.0", env="production")

# Works with stdlib logging configuration
logging.basicConfig(
    format="%(message)s",
    stream=sys.stdout,
    level=logging.INFO
)

# Custom configuration with stdlib integration
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S"),
        structlog.processors.JSONRenderer()
    ],
    wrapper_class=structlog.stdlib.BoundLogger,
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True
)

log = structlog.get_logger("api.handlers")

# Stdlib-style positional formatting
log.warning("Connection timeout after %d seconds", 30, host="db.example.com")
# Output: {"event": "Connection timeout after 30 seconds", "host": "db.example.com", "level": "warning", "logger": "api.handlers", "timestamp": "2025-12-10 10:30:45"}

# Exception logging with traceback
try:
    result = 10 / 0
except ZeroDivisionError:
    log.exception("calculation_error", operation="division")
    # Includes full exception traceback in structured format
```

### Custom Processors

Create custom processors to transform, filter, or enrich log event dictionaries in the processing pipeline.

```python
import structlog
from structlog.typing import EventDict, WrappedLogger

# Custom processor that adds hostname
def add_hostname(logger: WrappedLogger, method_name: str, event_dict: EventDict) -> EventDict:
    import socket
    event_dict["hostname"] = socket.gethostname()
    return event_dict

# Custom processor that filters sensitive data
def mask_sensitive_data(logger: WrappedLogger, method_name: str, event_dict: EventDict) -> EventDict:
    sensitive_keys = ["password", "token", "api_key", "secret"]
    for key in sensitive_keys:
        if key in event_dict:
            event_dict[key] = "***REDACTED***"
    return event_dict

# Custom processor that adds request duration
def add_request_duration(logger: WrappedLogger, method_name: str, event_dict: EventDict) -> EventDict:
    if "start_time" in event_dict and "end_time" in event_dict:
        duration = event_dict["end_time"] - event_dict["start_time"]
        event_dict["duration_ms"] = round(duration * 1000, 2)
    return event_dict

# Conditional processor that drops debug logs in production
def drop_debug_in_production(logger: WrappedLogger, method_name: str, event_dict: EventDict) -> EventDict:
    import os
    if os.environ.get("ENV") == "production" and event_dict.get("level") == "debug":
        raise structlog.DropEvent
    return event_dict

# Configure with custom processors
structlog.configure(
    processors=[
        add_hostname,
        mask_sensitive_data,
        add_request_duration,
        drop_debug_in_production,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer()
    ]
)

log = structlog.get_logger()

import time
start = time.time()
# ... do some work ...
end = time.time()

log.info("api_request",
         path="/login",
         password="secret123",  # Will be masked
         start_time=start,
         end_time=end)
# Output: {"event": "api_request", "path": "/login", "password": "***REDACTED***", "duration_ms": 42.15, "hostname": "web-server-01", "level": "info", "timestamp": "2025-12-10T10:30:45.123456Z"}
```

### Output Rendering Formats

Render log entries in various formats including JSON, logfmt, key-value, and colorful console output.

```python
import structlog
import sys

# JSON Renderer for machine-readable logs
structlog.configure(
    processors=[
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso", utc=True),
        structlog.processors.JSONRenderer(indent=None, sort_keys=True)
    ]
)

log = structlog.get_logger()
log.info("user_action", user_id=123, action="purchase", amount=99.99)
# Output: {"action":"purchase","amount":99.99,"event":"user_action","level":"info","timestamp":"2025-12-10T10:30:45.123456Z","user_id":123}

# Logfmt Renderer for human-readable structured logs
structlog.configure(
    processors=[
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.LogfmtRenderer(sort_keys=True)
    ]
)

log = structlog.get_logger()
log.warning("rate_limit", endpoint="/api/data", limit=100, current=95)
# Output: current=95 endpoint=/api/data event=rate_limit level=warning limit=100 timestamp=2025-12-10T10:30:45.123456Z

# Console Renderer with colors for development
structlog.configure(
    processors=[
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S"),
        structlog.dev.ConsoleRenderer(
            colors=True,
            pad_event=25,
            sort_keys=False,
            exception_formatter=structlog.dev.plain_traceback
        )
    ]
)

log = structlog.get_logger()
log.debug("cache_hit", key="user:123", ttl=3600)
log.info("request_processed", method="GET", status=200, duration_ms=45)
log.error("validation_failed", field="email", reason="invalid_format", value="not-an-email")
# Outputs colorful, aligned console logs with visual hierarchy

# Key-Value Renderer for simple text logs
structlog.configure(
    processors=[
        structlog.processors.KeyValueRenderer(
            key_order=["timestamp", "level", "event"],
            sort_keys=True,
            drop_missing=False
        )
    ]
)

log = structlog.get_logger()
log.info("deployment", service="web-api", version="1.2.3", region="us-east-1")
# Output: event='deployment' region='us-east-1' service='web-api' version='1.2.3'
```

### Testing Support

Use testing utilities to capture and inspect log output in unit tests.

```python
import structlog
from structlog.testing import ReturnLogger, ReturnLoggerFactory, CapturingLogger, CapturingLoggerFactory

# ReturnLogger returns log entries instead of outputting them
structlog.configure(
    processors=[
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
    ],
    logger_factory=ReturnLoggerFactory()
)

log = structlog.get_logger()

# Log calls return the processed event dict
result = log.info("test_event", user="alice", count=5)
assert result == ("test_event",)
assert "user" in log._context or "user" in result

# Better approach: CapturingLogger for test assertions
cap_logger = CapturingLogger()
test_log = structlog.wrap_logger(
    cap_logger,
    processors=[structlog.processors.add_log_level]
)

test_log.info("first_event", x=1)
test_log.warning("second_event", x=2)
test_log.error("third_event", x=3)

# Inspect captured logs
assert len(cap_logger.calls) == 3
assert cap_logger.calls[0].method_name == "info"
assert cap_logger.calls[0].kwargs["x"] == 1
assert cap_logger.calls[1].method_name == "warning"
assert cap_logger.calls[2].kwargs["event"] == "third_event"

# Example test with pytest
def test_user_registration():
    cap_logger = CapturingLogger()
    log = structlog.wrap_logger(cap_logger, processors=[structlog.processors.add_log_level])

    # Code under test
    def register_user(username, email):
        log.info("registration_start", username=username)
        # ... registration logic ...
        log.info("registration_complete", username=username, email=email)
        return True

    result = register_user("bob", "bob@example.com")

    assert result is True
    assert len(cap_logger.calls) == 2
    assert cap_logger.calls[0].kwargs["event"] == "registration_start"
    assert cap_logger.calls[0].kwargs["username"] == "bob"
    assert cap_logger.calls[1].kwargs["email"] == "bob@example.com"
```

### Log Level Filtering

Implement efficient log level filtering to control verbosity without processing overhead.

```python
import logging
import structlog

# Create filtering bound logger with minimum level
structlog.configure(
    processors=[
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer()
    ],
    wrapper_class=structlog.make_filtering_bound_logger(logging.WARNING)
)

log = structlog.get_logger()

# These are filtered out at the bound logger level (very fast)
log.debug("debug_info", details="...")  # Not processed
log.info("info_message", status="ok")   # Not processed

# These pass the filter and get processed
log.warning("warning_event", code=400)
# Output: {"event":"warning_event","code":400,"level":"warning","timestamp":"2025-12-10T10:30:45.123456Z"}

log.error("error_event", code=500)
# Output: {"event":"error_event","code":500,"level":"error","timestamp":"2025-12-10T10:30:45.123456Z"}

# Dynamic log level with stdlib integration
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,  # Processor-based filtering
        structlog.stdlib.add_log_level,
        structlog.processors.JSONRenderer()
    ],
    wrapper_class=structlog.stdlib.BoundLogger,
    logger_factory=structlog.stdlib.LoggerFactory()
)

log = structlog.get_logger()

# Change level at runtime
logging.getLogger().setLevel(logging.ERROR)

log.info("not_shown")  # Filtered
log.error("shown", reason="error_level_active")
# Output: {"event":"shown","reason":"error_level_active","level":"error"}
```

### Exception and Traceback Handling

Log exceptions with full tracebacks in structured format with optional pretty-printing.

```python
import structlog

# Configure with exception handling
structlog.configure(
    processors=[
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.dev.set_exc_info,  # Automatically capture exception info
        structlog.dev.ConsoleRenderer(
            exception_formatter=structlog.dev.rich_traceback  # Or plain_traceback
        )
    ]
)

log = structlog.get_logger()

# Log exception with automatic traceback capture
try:
    users = {"alice": 1, "bob": 2}
    user_id = users["charlie"]  # KeyError
except KeyError as e:
    log.exception("user_not_found",
                  username="charlie",
                  available_users=list(users.keys()))
    # Outputs structured log with full colorful traceback

# Manually add exception info
try:
    result = int("not-a-number")
except ValueError as e:
    log.error("conversion_failed",
              value="not-a-number",
              exc_info=True)  # Include exception info

# Structured exception dict processor
structlog.configure(
    processors=[
        structlog.processors.add_log_level,
        structlog.processors.dict_tracebacks,  # Convert to dict
        structlog.processors.JSONRenderer()
    ]
)

log = structlog.get_logger()

try:
    1 / 0
except ZeroDivisionError:
    log.error("math_error", operation="division", exc_info=True)
    # Output: {"event":"math_error","operation":"division","level":"error","exception":[{"exc_type":"ZeroDivisionError","exc_value":"division by zero","syntax_error":null,"is_cause":false,"frames":[...]}]}

# Custom exception rendering
from structlog.tracebacks import ExceptionDictTransformer

def custom_exception_formatter(exc_info):
    transformer = ExceptionDictTransformer()
    return transformer(exc_info)

structlog.configure(
    processors=[
        structlog.processors.add_log_level,
        structlog.processors.format_exc_info,
        structlog.processors.JSONRenderer()
    ]
)
```

### Performance Optimization with Caching

Enable logger caching for high-performance scenarios to avoid repeated logger assembly.

```python
import structlog
import logging

# Enable caching for performance-critical applications
structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer()
    ],
    wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
    cache_logger_on_first_use=True  # Cache assembled logger
)

# First call: logger is assembled and cached
log = structlog.get_logger()
log.info("first_call")  # Assembles and caches logger

# Subsequent calls: uses cached logger (faster)
log.info("second_call")
log.info("third_call")

# Binding creates new cached logger
log_with_context = log.bind(request_id="req-123")
log_with_context.info("cached_with_context")

# Each logger with different context is cached separately
log_user_1 = structlog.get_logger().bind(user_id=1)
log_user_2 = structlog.get_logger().bind(user_id=2)

# These use separate cached loggers
log_user_1.info("user_action")
log_user_2.info("user_action")

# Performance comparison setup
import time

# Without caching
structlog.configure(cache_logger_on_first_use=False)
start = time.time()
for i in range(10000):
    log = structlog.get_logger()
    log.info("test")
no_cache_time = time.time() - start

# With caching
structlog.configure(cache_logger_on_first_use=True)
start = time.time()
for i in range(10000):
    log = structlog.get_logger()
    log.info("test")
cache_time = time.time() - start

print(f"Without cache: {no_cache_time:.4f}s")
print(f"With cache: {cache_time:.4f}s")
print(f"Speedup: {no_cache_time/cache_time:.2f}x")
```

## Integration Patterns and Use Cases

structlog excels in diverse deployment scenarios through its modular architecture and flexible configuration system. For web applications, it provides request-scoped context management using context variables that automatically propagate across async boundaries, making it ideal for frameworks like FastAPI, Django, and Flask. The library can bind request IDs, user information, and other contextual data at the start of request handling, ensuring every log entry within that request includes the relevant context without manual propagation. In microservices architectures, structlog's structured output formats like JSON and logfmt integrate seamlessly with centralized logging systems (ELK stack, Splunk, CloudWatch), while correlation IDs and distributed tracing metadata flow naturally through the logging pipeline.

For production deployments, structlog offers multiple integration strategies with existing logging infrastructure. The standard library integration allows gradual adoption by wrapping existing `logging.Logger` instances while maintaining compatibility with existing handlers, formatters, and configuration. Performance-critical applications benefit from zero-cost abstractions through filtering bound loggers that reject log entries before processing, cached logger assembly, and lazy evaluation. Development environments leverage colorful console output with Rich or better-exceptions integration for enhanced debugging, while production switches to efficient JSON output. Testing is streamlined through specialized testing loggers that capture log entries for assertions, and thread-local or context-variable based context storage ensures correct behavior in multi-threaded and async applications without data corruption or context leakage.

