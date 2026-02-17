"""Comprehensive MCP endpoint integration tests.

Tests POST /mcp exhaustively:
  - JSON-RPC 2.0 protocol conformance
  - Tool dispatch: resolve-library-id, query-docs
  - Response structure validated at every nesting level
  - Content correctness (text says expected things, not just correct shape)
  - Error paths and edge cases

Two fixtures are created and cleaned up automatically:
  - MCPTestLib  (pypi/Python) — gets two documents added
  - MCPEmptyLib (pypi/Python) — intentionally left with no documents

Run standalone:
    uv run python tests/test_mcp.py [--base-url http://localhost:8000]
"""

import argparse
import sys
import textwrap
from collections.abc import Callable
from dataclasses import dataclass, field
from enum import Enum
from typing import Any

import httpx

BASE_URL = "http://localhost:8000"

# ---------------------------------------------------------------------------
# Suite infrastructure (mirrors test_integration.py so each file is standalone)
# ---------------------------------------------------------------------------


class Status(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    SKIP = "SKIP"


@dataclass
class TestResult:
    name: str
    status: Status
    detail: str = ""


@dataclass
class Suite:
    name: str
    results: list[TestResult] = field(default_factory=list)

    def add(self, name: str, status: Status, detail: str = "") -> None:
        self.results.append(TestResult(name, status, detail))

    @property
    def passed(self) -> int:
        return sum(1 for r in self.results if r.status == Status.PASS)

    @property
    def failed(self) -> int:
        return sum(1 for r in self.results if r.status == Status.FAIL)

    @property
    def skipped(self) -> int:
        return sum(1 for r in self.results if r.status == Status.SKIP)


Check = tuple[Callable[[dict[str, Any]], bool], str]


def call(
    suite: Suite,
    name: str,
    fn: Callable[[], httpx.Response],
    expected_status: int,
    *,
    checks: list[Check] | None = None,
) -> dict[str, Any] | None:
    try:
        r = fn()
    except httpx.TimeoutException:
        suite.add(name, Status.FAIL, "Request timed out")
        return None
    except httpx.ConnectError as e:
        suite.add(name, Status.FAIL, f"Connection refused: {e}")
        return None
    except httpx.RequestError as e:
        suite.add(name, Status.FAIL, f"Request error: {e}")
        return None

    if r.status_code == 501:
        suite.add(name, Status.SKIP, "501 Not Implemented")
        return None

    if r.status_code != expected_status:
        suite.add(
            name,
            Status.FAIL,
            f"Expected {expected_status}, got {r.status_code}: {r.text[:200]}",
        )
        return None

    body: dict[str, Any] = {}
    try:
        body = r.json()
    except Exception:
        pass

    if checks:
        for predicate, description in checks:
            try:
                ok = predicate(body)
            except Exception as exc:
                suite.add(name, Status.FAIL, f"Check raised: {exc}")
                return body
            if not ok:
                suite.add(name, Status.FAIL, f"Check failed: {description}")
                return body

    suite.add(name, Status.PASS)
    return body


# ---------------------------------------------------------------------------
# MCP helpers
# ---------------------------------------------------------------------------

DOC1_CONTENT = (
    "Authentication tokens are used for securing API access. "
    "Bearer tokens must be validated on every request. "
    "JWT tokens contain encoded claims about the user identity."
)

DOC2_CONTENT = (
    "Database connection pooling improves performance by reusing connections. "
    "Pool size should be tuned to workload. "
    "Idle connections are returned to the pool after each transaction."
)


def mcp_text(body: dict[str, Any]) -> str:
    """Extract text from result.content[0].text; empty string on any failure."""
    try:
        return body["result"]["content"][0]["text"]
    except (KeyError, IndexError, TypeError):
        return ""


def mcp_call(
    suite: Suite,
    name: str,
    client: httpx.Client,
    payload: dict[str, Any],
    expected_status: int = 200,
    *,
    checks: list[Check] | None = None,
) -> dict[str, Any] | None:
    """Thin wrapper: builds the lambda so tests stay concise."""
    _payload = payload  # capture
    return call(
        suite,
        name,
        lambda: client.post("/mcp", json=_payload),
        expected_status,
        checks=checks,
    )


def rpc(
    tool: str,
    arguments: dict[str, Any],
    *,
    req_id: int | str = 1,
    method: str = "tools/call",
) -> dict[str, Any]:
    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "method": method,
        "params": {"name": tool, "arguments": arguments},
    }


# ---------------------------------------------------------------------------
# Fixture setup / teardown
# ---------------------------------------------------------------------------


class Fixtures:
    library_id: str | None = None
    context7_id: str | None = None
    empty_lib_id: str | None = None
    doc1_id: str | None = None
    doc2_id: str | None = None


def setup_fixtures(client: httpx.Client) -> tuple[Suite, Fixtures]:
    suite = Suite("Fixture Setup")
    fix = Fixtures()

    # --- MCPTestLib ---
    lib_payload = {
        "name": "MCPTestLib",
        "language": "Python",
        "ecosystem": "pypi",
        "description": "Library for MCP integration tests",
        "keywords": ["test", "mcp"],
    }
    body = call(
        suite,
        "Create MCPTestLib",
        lambda: client.post("/api/v1/libraries", json=lib_payload),
        201,
        checks=[(lambda b: "id" in b and "context7_id" in b, "id and context7_id present")],
    )
    if body:
        fix.library_id = body["id"]
        fix.context7_id = body["context7_id"]

    # --- MCPEmptyLib ---
    empty_payload = {
        "name": "MCPEmptyLib",
        "language": "Python",
        "ecosystem": "pypi",
        "description": "Empty library for MCP edge-case tests",
    }
    body2 = call(
        suite,
        "Create MCPEmptyLib",
        lambda: client.post("/api/v1/libraries", json=empty_payload),
        201,
        checks=[(lambda b: "id" in b, "id present")],
    )
    if body2:
        fix.empty_lib_id = body2["id"]

    # --- Document 1: authentication content ---
    if fix.library_id:
        _lib = fix.library_id
        doc_body = call(
            suite,
            "Create doc1 (auth content)",
            lambda: client.post("/api/v1/documents", json={
                "title": "Authentication Guide",
                "library_id": _lib,
                "content": DOC1_CONTENT,
            }),
            201,
            checks=[(lambda b: "id" in b, "id present")],
        )
        if doc_body:
            fix.doc1_id = doc_body["id"]
    else:
        suite.add("Create doc1 (auth content)", Status.SKIP, "no library_id")

    # --- Document 2: database content ---
    if fix.library_id:
        _lib = fix.library_id
        doc_body2 = call(
            suite,
            "Create doc2 (database content)",
            lambda: client.post("/api/v1/documents", json={
                "title": "Database Pooling Guide",
                "library_id": _lib,
                "content": DOC2_CONTENT,
            }),
            201,
            checks=[(lambda b: "id" in b, "id present")],
        )
        if doc_body2:
            fix.doc2_id = doc_body2["id"]
    else:
        suite.add("Create doc2 (database content)", Status.SKIP, "no library_id")

    return suite, fix


def teardown_fixtures(client: httpx.Client, fix: Fixtures) -> Suite:
    suite = Suite("Fixture Teardown")

    for doc_id, label in [(fix.doc1_id, "doc1"), (fix.doc2_id, "doc2")]:
        if doc_id:
            _doc = doc_id
            call(
                suite,
                f"Delete {label}",
                lambda: client.delete(f"/api/v1/documents/{_doc}"),
                200,
            )

    for lib_id, label in [
        (fix.library_id, "MCPTestLib"),
        (fix.empty_lib_id, "MCPEmptyLib"),
    ]:
        if lib_id:
            _lib = lib_id
            call(
                suite,
                f"Delete {label}",
                lambda: client.delete(f"/api/v1/libraries/{_lib}"),
                200,
            )

    return suite


# ---------------------------------------------------------------------------
# Test suites
# ---------------------------------------------------------------------------


def test_protocol(client: httpx.Client, fix: Fixtures) -> Suite:
    """JSON-RPC 2.0 envelope conformance."""
    suite = Suite("MCP Protocol")

    # --- Envelope shape ---
    mcp_call(
        suite,
        "response has jsonrpc='2.0'",
        client,
        rpc("resolve-library-id", {"libraryName": "MCPTestLib", "query": "test"}),
        200,
        checks=[(lambda b: b.get("jsonrpc") == "2.0", "jsonrpc == '2.0'")],
    )

    mcp_call(
        suite,
        "response has 'result' key",
        client,
        rpc("resolve-library-id", {"libraryName": "MCPTestLib", "query": "test"}),
        200,
        checks=[(lambda b: "result" in b, "result key present")],
    )

    mcp_call(
        suite,
        "result.content is a list",
        client,
        rpc("resolve-library-id", {"libraryName": "MCPTestLib", "query": "test"}),
        200,
        checks=[
            (
                lambda b: isinstance(b.get("result", {}).get("content"), list),
                "result.content is list",
            )
        ],
    )

    mcp_call(
        suite,
        "result.content[0].type == 'text'",
        client,
        rpc("resolve-library-id", {"libraryName": "MCPTestLib", "query": "test"}),
        200,
        checks=[
            (
                lambda b: b.get("result", {}).get("content", [{}])[0].get("type") == "text",
                "content[0].type == 'text'",
            )
        ],
    )

    mcp_call(
        suite,
        "result.content[0].text is a non-empty string",
        client,
        rpc("resolve-library-id", {"libraryName": "MCPTestLib", "query": "test"}),
        200,
        checks=[
            (
                lambda b: isinstance(mcp_text(b), str) and len(mcp_text(b)) > 0,
                "content[0].text is non-empty string",
            )
        ],
    )

    # --- Request ID round-trip ---
    mcp_call(
        suite,
        "integer request id is echoed",
        client,
        rpc("resolve-library-id", {"libraryName": "x", "query": "y"}, req_id=42),
        200,
        checks=[(lambda b: b.get("id") == 42, "id == 42")],
    )

    mcp_call(
        suite,
        "string request id is echoed",
        client,
        rpc("resolve-library-id", {"libraryName": "x", "query": "y"}, req_id="abc-123"),
        200,
        checks=[(lambda b: b.get("id") == "abc-123", "id == 'abc-123'")],
    )

    # --- Method dispatch errors ---
    call(
        suite,
        "tools/list → 400 (not supported)",
        lambda: client.post("/mcp", json={
            "jsonrpc": "2.0", "id": 1, "method": "tools/list",
            "params": {"name": "noop", "arguments": {}},
        }),
        400,
    )

    call(
        suite,
        "tools/initialize → 400 (not supported)",
        lambda: client.post("/mcp", json={
            "jsonrpc": "2.0", "id": 1, "method": "tools/initialize",
            "params": {"name": "noop", "arguments": {}},
        }),
        400,
    )

    call(
        suite,
        "arbitrary unknown method → 400",
        lambda: client.post("/mcp", json={
            "jsonrpc": "2.0", "id": 1, "method": "foobar",
            "params": {"name": "noop", "arguments": {}},
        }),
        400,
    )

    call(
        suite,
        "unknown tool name → 400",
        lambda: client.post("/mcp", json={
            "jsonrpc": "2.0", "id": 1, "method": "tools/call",
            "params": {"name": "no-such-tool", "arguments": {}},
        }),
        400,
    )

    return suite


def test_resolve_library(client: httpx.Client, fix: Fixtures) -> Suite:
    """resolve-library-id tool — all branches."""
    suite = Suite("MCP resolve-library-id")

    # --- Exact match ---
    mcp_call(
        suite,
        "exact name match → 200",
        client,
        rpc("resolve-library-id", {"libraryName": "MCPTestLib", "query": "test"}),
        200,
    )

    mcp_call(
        suite,
        "result text contains 'Context7-compatible library ID:'",
        client,
        rpc("resolve-library-id", {"libraryName": "MCPTestLib", "query": "test"}),
        200,
        checks=[
            (
                lambda b: "Context7-compatible library ID:" in mcp_text(b),
                "text mentions Context7-compatible library ID",
            )
        ],
    )

    if fix.context7_id:
        _c7id = fix.context7_id
        mcp_call(
            suite,
            "result text contains the library's context7_id",
            client,
            rpc("resolve-library-id", {"libraryName": "MCPTestLib", "query": "test"}),
            200,
            checks=[
                (
                    lambda b: _c7id in mcp_text(b),
                    f"text contains context7_id {_c7id!r}",
                )
            ],
        )
    else:
        suite.add(
            "result text contains the library's context7_id",
            Status.SKIP,
            "context7_id not captured (library creation failed)",
        )

    mcp_call(
        suite,
        "result text contains library name",
        client,
        rpc("resolve-library-id", {"libraryName": "MCPTestLib", "query": "test"}),
        200,
        checks=[
            (lambda b: "MCPTestLib" in mcp_text(b), "text contains library name")
        ],
    )

    # --- Partial / fuzzy match (LIKE search) ---
    # "MCPTest" is a prefix of "MCPTestLib"; the LIKE fallback should catch it
    mcp_call(
        suite,
        "partial name match (LIKE prefix) → 200",
        client,
        rpc("resolve-library-id", {"libraryName": "MCPTest", "query": "test library"}),
        200,
        checks=[
            (lambda b: len(mcp_text(b)) > 0, "non-empty result for partial match")
        ],
    )

    # --- Not found ---
    mcp_call(
        suite,
        "not-found → 200 with 'No libraries found' message",
        client,
        rpc("resolve-library-id", {"libraryName": "ThisLibraryDefinitelyDoesNotExistXYZ", "query": "anything"}),
        200,
        checks=[
            (
                lambda b: "No libraries found" in mcp_text(b),
                "text says 'No libraries found'",
            )
        ],
    )

    # --- camelCase argument names are required ---
    # Verify that 'libraryName' (camelCase alias) is the correct key;
    # using the wrong snake_case key 'library_name' should cause a 422.
    call(
        suite,
        "snake_case 'library_name' argument → 422 (wrong key)",
        lambda: client.post("/mcp", json={
            "jsonrpc": "2.0", "id": 1, "method": "tools/call",
            "params": {
                "name": "resolve-library-id",
                "arguments": {"library_name": "MCPTestLib", "query": "test"},
            },
        }),
        422,
    )

    # --- query param is optional-ish: should not crash with empty string ---
    mcp_call(
        suite,
        "empty query string is accepted",
        client,
        rpc("resolve-library-id", {"libraryName": "MCPTestLib", "query": ""}),
        200,
    )

    # --- query param is long: should not crash ---
    long_query = "test " * 200
    mcp_call(
        suite,
        "very long query string is accepted",
        client,
        rpc("resolve-library-id", {"libraryName": "MCPTestLib", "query": long_query}),
        200,
    )

    return suite


def test_query_docs(client: httpx.Client, fix: Fixtures) -> Suite:
    """query-docs tool — all branches."""
    suite = Suite("MCP query-docs")

    # --- By internal library ID ---
    if fix.library_id:
        _lib = fix.library_id
        mcp_call(
            suite,
            "query by internal library_id → 200",
            client,
            rpc("query-docs", {"libraryId": _lib, "query": "authentication"}),
            200,
        )

        mcp_call(
            suite,
            "result text is a non-empty string",
            client,
            rpc("query-docs", {"libraryId": _lib, "query": "authentication"}),
            200,
            checks=[
                (
                    lambda b: isinstance(mcp_text(b), str) and len(mcp_text(b)) > 0,
                    "text is non-empty",
                )
            ],
        )

        mcp_call(
            suite,
            "keyword relevance: 'authentication' query surfaces auth content",
            client,
            rpc("query-docs", {"libraryId": _lib, "query": "authentication tokens bearer"}),
            200,
            checks=[
                (
                    lambda b: "authentication" in mcp_text(b).lower()
                    or "token" in mcp_text(b).lower()
                    or "bearer" in mcp_text(b).lower(),
                    "text contains auth-related keywords",
                )
            ],
        )

        mcp_call(
            suite,
            "keyword relevance: 'database pooling' query surfaces db content",
            client,
            rpc("query-docs", {"libraryId": _lib, "query": "database connection pooling"}),
            200,
            checks=[
                (
                    lambda b: "pool" in mcp_text(b).lower()
                    or "connection" in mcp_text(b).lower()
                    or "database" in mcp_text(b).lower(),
                    "text contains db-related keywords",
                )
            ],
        )

        mcp_call(
            suite,
            "response length ≤ 10000 chars (context-window safe)",
            client,
            rpc("query-docs", {"libraryId": _lib, "query": "anything"}),
            200,
            checks=[
                (lambda b: len(mcp_text(b)) <= 10000, "text ≤ 10000 chars")
            ],
        )
    else:
        for label in [
            "query by internal library_id → 200",
            "result text is a non-empty string",
            "keyword relevance: 'authentication' query surfaces auth content",
            "keyword relevance: 'database pooling' query surfaces db content",
            "response length ≤ 10000 chars (context-window safe)",
        ]:
            suite.add(label, Status.SKIP, "library_id not available")

    # --- By context7_id ---
    if fix.context7_id:
        _c7id = fix.context7_id
        mcp_call(
            suite,
            "query by context7_id → 200",
            client,
            rpc("query-docs", {"libraryId": _c7id, "query": "test"}),
            200,
            checks=[
                (lambda b: len(mcp_text(b)) > 0, "text is non-empty")
            ],
        )
    else:
        suite.add(
            "query by context7_id → 200",
            Status.SKIP,
            "context7_id not captured",
        )

    # --- Library not found ---
    mcp_call(
        suite,
        "non-existent libraryId → 200 with 'not found' message",
        client,
        rpc("query-docs", {"libraryId": "totally-fake-lib-id-xyz-999", "query": "test"}),
        200,
        checks=[
            (
                lambda b: "not found" in mcp_text(b).lower(),
                "text says 'not found'",
            )
        ],
    )

    # --- Empty library (no documents) ---
    if fix.empty_lib_id:
        _elib = fix.empty_lib_id
        mcp_call(
            suite,
            "empty library → 200 with 'No documentation found' message",
            client,
            rpc("query-docs", {"libraryId": _elib, "query": "anything"}),
            200,
            checks=[
                (
                    lambda b: "no documentation found" in mcp_text(b).lower(),
                    "text says 'No documentation found'",
                )
            ],
        )
    else:
        suite.add(
            "empty library → 200 with 'No documentation found' message",
            Status.SKIP,
            "empty_lib_id not captured",
        )

    # --- camelCase argument required ---
    call(
        suite,
        "snake_case 'library_id' argument → 422 (wrong key)",
        lambda: client.post("/mcp", json={
            "jsonrpc": "2.0", "id": 1, "method": "tools/call",
            "params": {
                "name": "query-docs",
                "arguments": {"library_id": "some-id", "query": "test"},
            },
        }),
        422,
    )

    # --- Empty query ---
    if fix.library_id:
        _lib = fix.library_id
        mcp_call(
            suite,
            "empty query string is accepted",
            client,
            rpc("query-docs", {"libraryId": _lib, "query": ""}),
            200,
        )
    else:
        suite.add("empty query string is accepted", Status.SKIP, "no library_id")

    return suite


# ---------------------------------------------------------------------------
# Runner + output
# ---------------------------------------------------------------------------

STATUS_ICONS = {Status.PASS: "✓", Status.FAIL: "✗", Status.SKIP: "○"}
STATUS_COLORS = {
    Status.PASS: "\033[32m",
    Status.FAIL: "\033[31m",
    Status.SKIP: "\033[33m",
}
RESET = "\033[0m"


def print_suite(suite: Suite, use_color: bool = True) -> None:
    print(f"\n  {suite.name}")
    print(f"  {'─' * 60}")
    for r in suite.results:
        icon = STATUS_ICONS[r.status]
        color = STATUS_COLORS[r.status] if use_color else ""
        reset = RESET if use_color else ""
        line = f"  {color}{icon}{reset} {r.name}"
        if r.detail and r.status != Status.PASS:
            wrapped = textwrap.fill(
                r.detail, width=72,
                initial_indent="      ", subsequent_indent="      ",
            )
            print(line)
            print(wrapped)
        else:
            print(line)


def run_all(base_url: str) -> int:
    use_color = sys.stdout.isatty()

    print("\nContext7 MCP Endpoint Tests")
    print(f"Target: {base_url}")
    print("=" * 64)

    try:
        httpx.get(f"{base_url}/health", timeout=5.0)
    except httpx.ConnectError:
        print(f"\nERROR: Cannot connect to {base_url}")
        print("Is the server running? Try: just serve")
        return 2
    except httpx.TimeoutException:
        print(f"\nERROR: Server at {base_url} is not responding (timeout)")
        return 2

    client = httpx.Client(base_url=base_url, timeout=15.0)

    # Setup
    setup_suite, fix = setup_fixtures(client)

    # Suites
    suites = [
        setup_suite,
        test_protocol(client, fix),
        test_resolve_library(client, fix),
        test_query_docs(client, fix),
        teardown_fixtures(client, fix),
    ]

    for suite in suites:
        print_suite(suite, use_color)

    total_pass = sum(s.passed for s in suites)
    total_fail = sum(s.failed for s in suites)
    total_skip = sum(s.skipped for s in suites)
    total = total_pass + total_fail + total_skip

    print(f"\n{'=' * 64}")
    print(
        f"Results: {total_pass}/{total} passed, "
        f"{total_skip} skipped (not implemented), "
        f"{total_fail} failed"
    )

    if total_fail:
        color = STATUS_COLORS[Status.FAIL] if use_color else ""
        reset = RESET if use_color else ""
        print(f"\n{color}FAILED{reset} – {total_fail} test(s) did not pass.")
        return 1

    color = STATUS_COLORS[Status.PASS] if use_color else ""
    reset = RESET if use_color else ""
    print(f"\n{color}OK{reset}")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="MCP endpoint integration tests")
    parser.add_argument(
        "--base-url", default=BASE_URL,
        help=f"Base URL of the server (default: {BASE_URL})",
    )
    args = parser.parse_args()
    sys.exit(run_all(args.base_url))


if __name__ == "__main__":
    main()
