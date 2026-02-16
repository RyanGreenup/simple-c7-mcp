# Pytest Testing Framework

## Introduction

Pytest is a mature, full-featured Python testing framework that makes it easy to write small, readable tests and scales to support complex functional testing for applications and libraries. The framework provides powerful features including detailed assertion introspection, modular fixtures, parametrization, and a rich plugin architecture with over 1,300 external plugins. Pytest supports Python 3.10 through 3.14 and PyPy3, and can run unittest test suites out of the box while providing its own more pythonic testing approach.

The framework uses automatic test discovery to find test modules (matching `test_*.py` or `*_test.py`), test classes (prefixed with `Test`), and test functions (prefixed with `test_`). It eliminates the need for boilerplate code through its fixture system for dependency injection and uses plain `assert` statements with intelligent introspection to provide detailed failure messages. The plugin-based architecture allows extensive customization through hooks, making pytest adaptable to various testing needs from simple unit tests to complex integration testing scenarios.

## Core APIs and Functions

### Basic Test Function

Write simple test functions using plain assert statements without any special base classes or methods.

```python
# test_sample.py
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4

def test_failure():
    assert inc(3) == 5
```

```bash
$ pytest test_sample.py -v
============================= test session starts =============================
collected 2 items

test_sample.py::test_answer PASSED                                      [ 50%]
test_sample.py::test_failure FAILED                                     [100%]

================================== FAILURES ===================================
_________________________________ test_failure _________________________________

    def test_failure():
>       assert inc(3) == 5
E       assert 4 == 5
E        +  where 4 = inc(3)

test_sample.py:8: AssertionError
========================== 1 failed, 1 passed in 0.03s ===========================
```

### Fixture System - @pytest.fixture

Define reusable setup code and inject dependencies into test functions through fixtures with automatic cleanup support.

```python
# conftest.py
import pytest
import sqlite3
from pathlib import Path

@pytest.fixture
def database(tmp_path):
    """Create a temporary database for testing."""
    db_path = tmp_path / "test.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO users (name) VALUES ('Alice'), ('Bob')")
    conn.commit()

    yield conn  # Provide the connection to the test

    # Cleanup happens after test completes
    conn.close()

@pytest.fixture(scope="session")
def api_token():
    """Session-scoped fixture that runs once for all tests."""
    return "test-token-12345"

# test_database.py
def test_query_users(database):
    cursor = database.cursor()
    cursor.execute("SELECT name FROM users ORDER BY name")
    results = [row[0] for row in cursor.fetchall()]
    assert results == ['Alice', 'Bob']

def test_insert_user(database):
    cursor = database.cursor()
    cursor.execute("INSERT INTO users (name) VALUES ('Charlie')")
    database.commit()
    cursor.execute("SELECT COUNT(*) FROM users")
    assert cursor.fetchone()[0] == 3

def test_api_authentication(api_token):
    assert api_token.startswith("test-token")
```

```bash
$ pytest test_database.py -v
============================= test session starts =============================
collected 3 items

test_database.py::test_query_users PASSED                               [ 33%]
test_database.py::test_insert_user PASSED                               [ 66%]
test_database.py::test_api_authentication PASSED                        [100%]

============================== 3 passed in 0.02s ==============================
```

### Parametrization - @pytest.mark.parametrize

Run a test function multiple times with different input values to avoid code duplication and test edge cases comprehensively.

```python
import pytest

def add(a, b):
    return a + b

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("x", [1, 2, 3])
@pytest.mark.parametrize("y", [10, 20])
def test_multiplication_combinations(x, y):
    """Cartesian product: runs 6 times (3 x values × 2 y values)."""
    result = x * y
    assert result > 0

@pytest.mark.parametrize("input,expected", [
    ("hello", "HELLO"),
    pytest.param("world", "WORLD", id="world-uppercase"),
    pytest.param("error", "FAIL", marks=pytest.mark.xfail, id="known-bug"),
])
def test_uppercase_with_custom_ids(input, expected):
    assert input.upper() == expected
```

```bash
$ pytest test_parametrize.py -v
============================= test session starts =============================
collected 10 items

test_parametrize.py::test_add[2-3-5] PASSED                             [ 10%]
test_parametrize.py::test_add[0-0-0] PASSED                             [ 20%]
test_parametrize.py::test_add[-1-1-0] PASSED                            [ 30%]
test_parametrize.py::test_add[100-200-300] PASSED                       [ 40%]
test_parametrize.py::test_multiplication_combinations[10-1] PASSED      [ 50%]
test_parametrize.py::test_multiplication_combinations[10-2] PASSED      [ 60%]
test_parametrize.py::test_multiplication_combinations[10-3] PASSED      [ 70%]
test_parametrize.py::test_multiplication_combinations[20-1] PASSED      [ 80%]
test_parametrize.py::test_multiplication_combinations[20-2] PASSED      [ 90%]
test_parametrize.py::test_multiplication_combinations[20-3] PASSED      [100%]

============================== 10 passed in 0.03s ==============================
```

### Exception Testing - pytest.raises

Assert that code raises specific exceptions with optional message matching using regular expressions.

```python
import pytest

def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age exceeds reasonable human lifespan")
    return age

def test_invalid_type():
    with pytest.raises(TypeError, match="Age must be an integer"):
        validate_age("25")

def test_negative_age():
    with pytest.raises(ValueError, match="cannot be negative"):
        validate_age(-5)

def test_excessive_age():
    exc_info = pytest.raises(ValueError, match="exceeds reasonable")
    with exc_info:
        validate_age(200)

    # Access exception details after the context
    assert "lifespan" in str(exc_info.value)
    assert exc_info.type is ValueError

def test_valid_age():
    # No exception should be raised
    result = validate_age(25)
    assert result == 25

# Alternative functional syntax
def risky_operation():
    raise RuntimeError("Something went wrong")

def test_functional_raises():
    pytest.raises(RuntimeError, risky_operation)
```

```bash
$ pytest test_exceptions.py -v
============================= test session starts =============================
collected 5 items

test_exceptions.py::test_invalid_type PASSED                            [ 20%]
test_exceptions.py::test_negative_age PASSED                            [ 40%]
test_exceptions.py::test_excessive_age PASSED                           [ 60%]
test_exceptions.py::test_valid_age PASSED                               [ 80%]
test_exceptions.py::test_functional_raises PASSED                       [100%]

============================== 5 passed in 0.02s ==============================
```

### Approximate Comparisons - pytest.approx

Compare floating-point numbers with configurable tolerance to avoid precision issues in numerical computations.

```python
import pytest
import math

def test_float_comparison():
    """Basic floating-point comparison with default tolerance."""
    assert 0.1 + 0.2 == pytest.approx(0.3)
    assert math.pi == pytest.approx(3.14159, abs=1e-5)

def test_list_comparison():
    """Compare lists of floats element-wise."""
    computed = [0.1 + 0.1, 0.2 + 0.2, 0.3 + 0.3]
    expected = [0.2, 0.4, 0.6]
    assert computed == pytest.approx(expected)

def test_dict_comparison():
    """Compare dictionary values with tolerance."""
    result = {"x": 0.1 + 0.2, "y": 0.2 + 0.4}
    assert result == pytest.approx({"x": 0.3, "y": 0.6})

def test_custom_tolerance():
    """Use custom relative and absolute tolerance."""
    # Relative tolerance: 10% difference allowed
    assert 100 == pytest.approx(105, rel=0.1)

    # Absolute tolerance: 0.01 difference allowed
    assert 1.0 == pytest.approx(1.005, abs=0.01)

    # Both tolerances
    assert 99.5 == pytest.approx(100, rel=0.01, abs=1.0)

def test_numpy_arrays():
    """Works with numpy arrays if numpy is installed."""
    try:
        import numpy as np
        result = np.array([0.1, 0.2]) + np.array([0.2, 0.3])
        expected = np.array([0.3, 0.5])
        assert result == pytest.approx(expected)
    except ImportError:
        pytest.skip("numpy not installed")
```

```bash
$ pytest test_approx.py -v
============================= test session starts =============================
collected 5 items

test_approx.py::test_float_comparison PASSED                            [ 20%]
test_approx.py::test_list_comparison PASSED                             [ 40%]
test_approx.py::test_dict_comparison PASSED                             [ 60%]
test_approx.py::test_custom_tolerance PASSED                            [ 80%]
test_approx.py::test_numpy_arrays SKIPPED (numpy not installed)        [100%]

========================= 4 passed, 1 skipped in 0.03s ========================
```

### Test Markers - Skip and XFail

Control test execution with markers to skip tests conditionally or mark them as expected failures.

```python
import pytest
import sys
import os

@pytest.mark.skip(reason="Feature not implemented yet")
def test_future_feature():
    assert False

@pytest.mark.skipif(sys.platform == "win32", reason="Unix-specific test")
def test_unix_specific():
    assert os.path.exists("/etc/passwd")

@pytest.mark.skipif(sys.version_info < (3, 11), reason="Requires Python 3.11+")
def test_exception_groups():
    """Test exception groups (PEP 654)."""
    pass

@pytest.mark.xfail(reason="Known bug in external library")
def test_buggy_behavior():
    assert False  # Expected to fail

@pytest.mark.xfail(sys.platform == "darwin", reason="Fails on macOS")
def test_platform_dependent():
    assert True  # If passes on macOS, marked as "xpassed"

@pytest.mark.xfail(strict=True)
def test_strict_xfail():
    """Fails if this test unexpectedly passes."""
    assert False

def test_dynamic_skip():
    """Skip test dynamically during execution."""
    if not os.path.exists("/tmp/config.json"):
        pytest.skip("Config file not found")
    # Test continues only if condition is false

def test_import_or_skip():
    """Skip if optional dependency is missing."""
    requests = pytest.importorskip("requests", minversion="2.0")
    response = requests.get("https://api.example.com")
    assert response.status_code == 200
```

```bash
$ pytest test_markers.py -v
============================= test session starts =============================
collected 8 items

test_markers.py::test_future_feature SKIPPED (Feature not implement...) [12%]
test_markers.py::test_unix_specific PASSED                              [25%]
test_markers.py::test_exception_groups SKIPPED (Requires Python 3.11+) [37%]
test_markers.py::test_buggy_behavior XFAIL (Known bug in external...)  [50%]
test_markers.py::test_platform_dependent PASSED                         [62%]
test_markers.py::test_strict_xfail XFAIL                                [75%]
test_markers.py::test_dynamic_skip SKIPPED (Config file not found)     [87%]
test_markers.py::test_import_or_skip SKIPPED (could not import 'req...) [100%]

=================== 4 passed, 4 skipped, 2 xfailed in 0.05s ===================
```

### Warning Testing - pytest.warns

Assert that code produces specific warnings during execution and inspect warning details.

```python
import pytest
import warnings

def legacy_function():
    warnings.warn("This function is deprecated", DeprecationWarning)
    return 42

def test_deprecation_warning():
    """Assert that specific warning is raised."""
    with pytest.warns(DeprecationWarning, match="deprecated"):
        result = legacy_function()
        assert result == 42

def test_multiple_warnings():
    """Capture and inspect multiple warnings."""
    with pytest.warns() as warning_list:
        warnings.warn("First warning", UserWarning)
        warnings.warn("Second warning", UserWarning)

    assert len(warning_list) == 2
    assert "First" in str(warning_list[0].message)
    assert warning_list[1].category == UserWarning

def test_deprecated_call():
    """Convenience function for deprecation warnings."""
    with pytest.deprecated_call():
        warnings.warn("Old API", DeprecationWarning)

def test_no_warnings(recwarn):
    """Verify no warnings were raised using recwarn fixture."""
    result = 1 + 1
    assert result == 2
    assert len(recwarn) == 0

def test_warning_inspection(recwarn):
    """Detailed warning inspection with recwarn fixture."""
    warnings.warn("Custom warning", UserWarning)
    warnings.warn("Another warning", FutureWarning)

    assert len(recwarn) == 2

    # Access specific warnings
    user_warning = recwarn.pop(UserWarning)
    assert "Custom" in str(user_warning.message)

    future_warning = recwarn.pop(FutureWarning)
    assert future_warning.category == FutureWarning
```

```bash
$ pytest test_warnings.py -v
============================= test session starts =============================
collected 5 items

test_warnings.py::test_deprecation_warning PASSED                       [ 20%]
test_warnings.py::test_multiple_warnings PASSED                         [ 40%]
test_warnings.py::test_deprecated_call PASSED                           [ 60%]
test_warnings.py::test_no_warnings PASSED                               [ 80%]
test_warnings.py::test_warning_inspection PASSED                        [100%]

============================== 5 passed in 0.03s ==============================
```

### Output Capturing - capsys and capfd

Capture and inspect stdout/stderr output written by the code under test.

```python
import pytest
import sys
import os

def greet(name):
    print(f"Hello, {name}!")
    return name

def log_error(message):
    print(f"ERROR: {message}", file=sys.stderr)

def test_stdout_capture(capsys):
    """Capture standard output."""
    result = greet("Alice")

    captured = capsys.readouterr()
    assert captured.out == "Hello, Alice!\n"
    assert captured.err == ""
    assert result == "Alice"

def test_stderr_capture(capsys):
    """Capture standard error."""
    log_error("Something went wrong")

    captured = capsys.readouterr()
    assert "ERROR: Something went wrong" in captured.err
    assert captured.out == ""

def test_multiple_captures(capsys):
    """Capture output multiple times during test."""
    print("First message")
    captured1 = capsys.readouterr()
    assert "First" in captured1.out

    print("Second message")
    captured2 = capsys.readouterr()
    assert "Second" in captured2.out
    assert "First" not in captured2.out  # Previous output was consumed

def test_disabled_capture(capsys):
    """Temporarily disable output capturing."""
    print("Captured output")

    with capsys.disabled():
        print("This goes directly to console")

    print("Captured again")
    captured = capsys.readouterr()
    assert "Captured output" in captured.out
    assert "Captured again" in captured.out
    assert "This goes directly" not in captured.out

def test_binary_output(capfd):
    """Capture file descriptor output (including subprocesses)."""
    os.write(1, b"Binary data\n")

    captured = capfd.readouterr()
    assert "Binary data" in captured.out
```

```bash
$ pytest test_capture.py -v -s
============================= test session starts =============================
collected 5 items

test_capture.py::test_stdout_capture PASSED                             [ 20%]
test_capture.py::test_stderr_capture PASSED                             [ 40%]
test_capture.py::test_multiple_captures PASSED                          [ 60%]
test_capture.py::test_disabled_capture This goes directly to console
PASSED                                                                  [ 80%]
test_capture.py::test_binary_output PASSED                              [100%]

============================== 5 passed in 0.03s ==============================
```

### Monkeypatching - monkeypatch

Safely modify objects, environment variables, and system paths with automatic restoration after tests.

```python
import pytest
import os
import sys
from pathlib import Path

def get_username():
    return os.environ.get("USER", "unknown")

def test_environment_variable(monkeypatch):
    """Modify environment variable for test."""
    monkeypatch.setenv("USER", "testuser")
    assert get_username() == "testuser"

    monkeypatch.delenv("USER")
    assert get_username() == "unknown"

def test_attribute_patching(monkeypatch):
    """Patch object attributes."""
    import os

    # Replace os.getcwd with a mock function
    monkeypatch.setattr(os, "getcwd", lambda: "/fake/path")
    assert os.getcwd() == "/fake/path"

    # Original os.getcwd is restored after test

def test_dictionary_patching(monkeypatch):
    """Modify dictionary entries."""
    config = {"debug": False, "timeout": 30}

    monkeypatch.setitem(config, "debug", True)
    monkeypatch.setitem(config, "timeout", 60)

    assert config["debug"] is True
    assert config["timeout"] == 60

def test_sys_path(monkeypatch):
    """Prepend to sys.path."""
    original_length = len(sys.path)

    monkeypatch.syspath_prepend("/custom/lib")
    assert sys.path[0] == "/custom/lib"
    assert len(sys.path) == original_length + 1

def test_chdir(monkeypatch, tmp_path):
    """Change working directory."""
    test_dir = tmp_path / "subdir"
    test_dir.mkdir()

    original_dir = os.getcwd()
    monkeypatch.chdir(test_dir)

    assert os.getcwd() == str(test_dir)
    # Original directory restored after test

class Calculator:
    def add(self, a, b):
        return a + b

def test_method_patching(monkeypatch):
    """Patch class methods."""
    calc = Calculator()

    # Replace method with mock
    monkeypatch.setattr(Calculator, "add", lambda self, a, b: a * b)

    assert calc.add(3, 4) == 12  # Uses multiplication instead
```

```bash
$ pytest test_monkeypatch.py -v
============================= test session starts =============================
collected 6 items

test_monkeypatch.py::test_environment_variable PASSED                   [ 16%]
test_monkeypatch.py::test_attribute_patching PASSED                     [ 33%]
test_monkeypatch.py::test_dictionary_patching PASSED                    [ 50%]
test_monkeypatch.py::test_sys_path PASSED                               [ 66%]
test_monkeypatch.py::test_chdir PASSED                                  [ 83%]
test_monkeypatch.py::test_method_patching PASSED                        [100%]

============================== 6 passed in 0.03s ==============================
```

### Temporary Directories - tmp_path

Create temporary directories automatically cleaned up after tests using pathlib.Path interface.

```python
import pytest
from pathlib import Path
import json

def test_create_file(tmp_path):
    """Create and read a file in temporary directory."""
    test_file = tmp_path / "test.txt"
    test_file.write_text("Hello, World!")

    assert test_file.read_text() == "Hello, World!"
    assert test_file.exists()

def test_directory_structure(tmp_path):
    """Create nested directory structure."""
    nested_dir = tmp_path / "level1" / "level2" / "level3"
    nested_dir.mkdir(parents=True)

    config_file = nested_dir / "config.json"
    config_file.write_text(json.dumps({"debug": True}))

    assert config_file.exists()
    assert json.loads(config_file.read_text())["debug"] is True

def test_multiple_files(tmp_path):
    """Work with multiple files."""
    for i in range(5):
        file = tmp_path / f"file_{i}.txt"
        file.write_text(f"Content {i}")

    files = list(tmp_path.glob("*.txt"))
    assert len(files) == 5

def save_data(directory: Path, data: dict):
    """Helper function that writes to filesystem."""
    output_file = directory / "output.json"
    output_file.write_text(json.dumps(data))
    return output_file

def test_function_with_filesystem(tmp_path):
    """Test function that requires filesystem access."""
    test_data = {"name": "Alice", "age": 30}
    result_file = save_data(tmp_path, test_data)

    assert result_file.exists()
    loaded_data = json.loads(result_file.read_text())
    assert loaded_data == test_data

def test_session_temp_directory(tmp_path_factory):
    """Create temp directory shared across test session."""
    session_dir = tmp_path_factory.mktemp("session_data")
    cache_file = session_dir / "cache.txt"
    cache_file.write_text("Shared data")

    assert cache_file.exists()
```

```bash
$ pytest test_tmpdir.py -v
============================= test session starts =============================
collected 6 items

test_tmpdir.py::test_create_file PASSED                                 [ 16%]
test_tmpdir.py::test_directory_structure PASSED                         [ 33%]
test_tmpdir.py::test_multiple_files PASSED                              [ 50%]
test_tmpdir.py::test_function_with_filesystem PASSED                    [ 66%]
test_tmpdir.py::test_session_temp_directory PASSED                      [ 83%]

============================== 6 passed in 0.04s ==============================
```

### Plugin Hooks - conftest.py

Customize pytest behavior by implementing hook functions in conftest.py files.

```python
# conftest.py
import pytest
import time

def pytest_configure(config):
    """Register custom markers."""
    config.addinivalue_line(
        "markers", "slow: mark test as slow running"
    )
    config.addinivalue_line(
        "markers", "integration: mark test as integration test"
    )
    config.addinivalue_line(
        "markers", "unit: mark test as unit test"
    )

def pytest_addoption(parser):
    """Add custom command-line options."""
    parser.addoption(
        "--runslow",
        action="store_true",
        default=False,
        help="run slow tests"
    )
    parser.addoption(
        "--integration",
        action="store_true",
        default=False,
        help="run integration tests"
    )

def pytest_collection_modifyitems(config, items):
    """Modify test collection based on command-line options."""
    if not config.getoption("--runslow"):
        skip_slow = pytest.mark.skip(reason="need --runslow option to run")
        for item in items:
            if "slow" in item.keywords:
                item.add_marker(skip_slow)

    if not config.getoption("--integration"):
        skip_integration = pytest.mark.skip(reason="need --integration option")
        for item in items:
            if "integration" in item.keywords:
                item.add_marker(skip_integration)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Add custom information to test reports."""
    outcome = yield
    report = outcome.get_result()

    # Add test duration to report
    if report.when == "call":
        report.custom_duration = f"{report.duration:.4f}s"

def pytest_report_header(config):
    """Add custom header to test output."""
    return ["Custom Test Suite v1.0", f"Platform: {config.option.platform}"]

@pytest.fixture(autouse=True)
def timing_fixture(request):
    """Automatically time all tests."""
    start = time.time()
    yield
    duration = time.time() - start
    print(f"\n[Test {request.node.name} took {duration:.4f}s]")

# test_custom.py
import pytest
import time

@pytest.mark.unit
def test_fast_unit():
    """Fast unit test."""
    assert 1 + 1 == 2

@pytest.mark.slow
def test_slow_operation():
    """Slow test that requires --runslow flag."""
    time.sleep(2)
    assert True

@pytest.mark.integration
def test_integration():
    """Integration test requiring --integration flag."""
    assert True

def test_custom_fixture_usage(request):
    """Test using custom fixtures from conftest."""
    assert hasattr(request.config, "option")
```

```bash
$ pytest test_custom.py -v
============================= test session starts =============================
Custom Test Suite v1.0
Platform: linux
collected 4 items

test_custom.py::test_fast_unit PASSED                                   [ 25%]
test_custom.py::test_slow_operation SKIPPED (need --runslow option)    [ 50%]
test_custom.py::test_integration SKIPPED (need --integration option)   [ 75%]
test_custom.py::test_custom_fixture_usage PASSED                        [100%]

========================= 2 passed, 2 skipped in 0.05s ========================

$ pytest test_custom.py --runslow --integration -v
============================= test session starts =============================
Custom Test Suite v1.0
Platform: linux
collected 4 items

test_custom.py::test_fast_unit PASSED                                   [ 25%]
test_custom.py::test_slow_operation PASSED                              [ 50%]
test_custom.py::test_integration PASSED                                 [ 75%]
test_custom.py::test_custom_fixture_usage PASSED                        [100%]

============================== 4 passed in 2.08s ===============================
```

### Configuration Files - pytest.ini and pyproject.toml

Configure pytest behavior through configuration files for consistent test execution across environments.

```ini
# pytest.ini
[pytest]
minversion = 6.0
testpaths = tests
python_files = test_*.py *_test.py
python_classes = Test* *Tests
python_functions = test_* check_*

# Add custom markers
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    integration: marks tests as integration tests
    unit: marks tests as unit tests
    smoke: marks tests as smoke tests
    requires_network: test requires network access
    requires_database: test requires database connection

# Logging configuration
log_cli = true
log_cli_level = INFO
log_cli_format = %(asctime)s [%(levelname)8s] %(message)s
log_cli_date_format = %Y-%m-%d %H:%M:%S

# Test output options
addopts =
    -ra
    --strict-markers
    --strict-config
    --showlocals
    --tb=short

# Coverage options (if pytest-cov is installed)
# addopts = --cov=src --cov-report=html --cov-report=term-missing

# Warning filters
filterwarnings =
    error
    ignore::UserWarning
    ignore::DeprecationWarning:importlib.*

# Timeout for tests (requires pytest-timeout)
# timeout = 300
# timeout_method = thread

# Parallel execution (requires pytest-xdist)
# addopts = -n auto
```

```toml
# pyproject.toml
[tool.pytest.ini_options]
minversion = "6.0"
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py"]
python_classes = ["Test*", "*Tests"]
python_functions = ["test_*", "check_*"]

markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "integration: marks tests as integration tests",
    "unit: marks tests as unit tests",
    "smoke: marks tests as smoke tests",
]

addopts = [
    "-ra",
    "--strict-markers",
    "--strict-config",
    "--showlocals",
]

filterwarnings = [
    "error",
    "ignore::UserWarning",
    "ignore::DeprecationWarning:importlib.*",
]

# Example directory structure
[tool.pytest.ini_options.testpaths]
# tests/
#   conftest.py
#   unit/
#     test_models.py
#     test_utils.py
#   integration/
#     test_api.py
#     test_database.py
```

```bash
# Run tests with configuration
$ pytest

# Override configuration from command line
$ pytest -v --tb=long

# Select tests by marker
$ pytest -m "unit and not slow"

# Run specific test paths
$ pytest tests/unit/ tests/integration/test_api.py

# Show available markers
$ pytest --markers
@pytest.mark.slow: marks tests as slow (deselect with '-m "not slow"')
@pytest.mark.integration: marks tests as integration tests
@pytest.mark.unit: marks tests as unit tests
@pytest.mark.smoke: marks tests as smoke tests
```

## Summary and Integration

Pytest serves as a comprehensive testing solution suitable for projects ranging from simple scripts to large-scale applications, with its primary use cases including unit testing individual functions and classes, integration testing of component interactions, end-to-end testing of complete workflows, and regression testing to ensure code changes don't break existing functionality. The framework excels in test-driven development (TDD) workflows, continuous integration pipelines, and exploratory testing scenarios. Its fixture system enables elegant dependency injection and resource management, while parametrization reduces code duplication when testing multiple scenarios, and the plugin ecosystem extends functionality for specific needs like parallel execution (pytest-xdist), coverage reporting (pytest-cov), BDD testing (pytest-bdd), Django/Flask integration, and async testing support.

Integration with pytest typically involves installing the package via pip (`pip install pytest`), organizing tests in a dedicated directory structure following naming conventions, using conftest.py files for shared fixtures and configuration, and running tests through the command-line interface or IDE integration. The framework integrates seamlessly with continuous integration systems through its exit codes and JUnit XML reporting, works alongside type checkers like mypy, and complements code coverage tools. Tests can be organized using custom markers for flexible test selection, parametrized to cover edge cases efficiently, and extended through hooks to customize collection, execution, and reporting. The combination of simplicity for basic tests and power for advanced scenarios makes pytest the de facto standard for Python testing, with extensive documentation and community support ensuring it remains accessible to beginners while providing the sophisticated features required by large projects.
