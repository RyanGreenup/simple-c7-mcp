"""Integration tests for the Context7 MCP API.

Tests all endpoints in IMPLEMENTATION.md. Each test records PASS, FAIL, or SKIP
(501 Not Implemented). Exceptions from individual requests are caught and recorded
as failures rather than crashing the runner.

Run against a live server:
    uv run python tests/test_integration.py [--base-url http://localhost:8000]
    just test-integration
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
# Result tracking
# ---------------------------------------------------------------------------


class Status(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    SKIP = "SKIP"  # endpoint returned 501 Not Implemented


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


# ---------------------------------------------------------------------------
# Core helper: call() makes one request and records the result
# ---------------------------------------------------------------------------

# A check is (predicate_on_body, description_string)
Check = tuple[Callable[[dict[str, Any]], bool], str]


def call(
    suite: Suite,
    name: str,
    fn: Callable[[], httpx.Response],
    expected_status: int,
    *,
    checks: list[Check] | None = None,
) -> dict[str, Any] | None:
    """Execute one HTTP request and record pass/fail/skip in *suite*.

    Args:
        suite: Suite to record the result in.
        name: Human-readable test name.
        fn: Callable that performs the HTTP request.
        expected_status: Expected HTTP status code.
        checks: Optional list of (predicate, description) pairs evaluated
            against the parsed JSON body.

    Returns:
        Parsed JSON body dict on success, None otherwise.
    """
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
# Test suites
# ---------------------------------------------------------------------------


def test_health(client: httpx.Client) -> Suite:
    suite = Suite("Health")
    call(suite, "GET /health → 200 + status=healthy",
         lambda: client.get("/health"), 200,
         checks=[(lambda b: b.get("status") == "healthy", "status == 'healthy'")])
    return suite


def test_libraries(client: httpx.Client) -> tuple[Suite, str | None]:
    """Returns (suite, library_id) for use by downstream suites."""
    suite = Suite("Libraries")
    created_id: str | None = None

    # list (may be empty)
    call(suite, "GET /api/v1/libraries → 200 list",
         lambda: client.get("/api/v1/libraries"), 200,
         checks=[(lambda b: isinstance(b, list), "response is a list")])

    # create
    payload = {
        "name": "IntegrationTestLib",
        "language": "Python",
        "ecosystem": "pypi",
        "description": "Created by integration test",
        "keywords": ["test", "integration"],
    }
    body = call(suite, "POST /api/v1/libraries → 201 created",
                lambda: client.post("/api/v1/libraries", json=payload), 201,
                checks=[(lambda b: "id" in b, "id field present")])
    if body:
        created_id = body.get("id")

    # duplicate → 400
    call(suite, "POST /api/v1/libraries duplicate → 400",
         lambda: client.post("/api/v1/libraries", json=payload), 400)

    # get by id
    if created_id:
        _id = created_id
        call(suite, "GET /api/v1/libraries/{id} → 200",
             lambda: client.get(f"/api/v1/libraries/{_id}"), 200,
             checks=[
                 (lambda b: b.get("id") == _id, "id matches"),
                 (lambda b: b.get("name") == "IntegrationTestLib", "name matches"),
             ])

    # get non-existent → 404
    call(suite, "GET /api/v1/libraries/nonexistent → 404",
         lambda: client.get("/api/v1/libraries/nonexistent-id-xyz"), 404)

    # PUT full update
    if created_id:
        _id = created_id
        call(suite, "PUT /api/v1/libraries/{id} → 200 updated",
             lambda: client.put(f"/api/v1/libraries/{_id}",
                                json={"name": "IntegrationTestLibUpdated", "description": "updated"}),
             200,
             checks=[(lambda b: b.get("name") == "IntegrationTestLibUpdated", "name updated")])

    # PATCH partial update
    if created_id:
        _id = created_id
        call(suite, "PATCH /api/v1/libraries/{id} → 200 patched",
             lambda: client.patch(f"/api/v1/libraries/{_id}",
                                  json={"description": "patched description"}),
             200)

    # list after creation includes the library
    if created_id:
        _id = created_id
        call(suite, "GET /api/v1/libraries includes created library",
             lambda: client.get("/api/v1/libraries"), 200,
             checks=[(lambda b: _id in [lib.get("id") for lib in (b if isinstance(b, list) else [])],
                      f"created id in list")])

    return suite, created_id


def test_documents(client: httpx.Client, library_id: str | None) -> tuple[Suite, str | None]:
    """Returns (suite, doc_id) for use by cleanup suite."""
    suite = Suite("Documents")
    created_doc_id: str | None = None

    # list (may be empty)
    call(suite, "GET /api/v1/documents → 200 list",
         lambda: client.get("/api/v1/documents"), 200,
         checks=[(lambda b: isinstance(b, list), "response is a list")])

    # list filtered by library_id
    if library_id:
        _lib = library_id
        call(suite, "GET /api/v1/documents?library_id=… → 200 list",
             lambda: client.get("/api/v1/documents", params={"library_id": _lib}), 200,
             checks=[(lambda b: isinstance(b, list), "response is a list")])

    # create document
    if library_id:
        _lib = library_id
        body = call(suite, "POST /api/v1/documents → 201 created",
                    lambda: client.post("/api/v1/documents", json={
                        "title": "Test Document",
                        "library_id": _lib,
                        "content": "# Hello\nThis is test content for the integration test.",
                    }), 201,
                    checks=[(lambda b: "id" in b, "id field present")])
        if body:
            created_doc_id = body.get("id")
    else:
        suite.add("POST /api/v1/documents → 201 created", Status.SKIP,
                  "no library_id (library create skipped)")

    # create with invalid library_id → 404
    call(suite, "POST /api/v1/documents bad library_id → 404",
         lambda: client.post("/api/v1/documents", json={
             "title": "Bad Doc",
             "library_id": "nonexistent-lib-xyz",
             "content": "content",
         }), 404)

    # get metadata
    if created_doc_id:
        _doc = created_doc_id
        call(suite, "GET /api/v1/documents/{id} → 200 metadata",
             lambda: client.get(f"/api/v1/documents/{_doc}"), 200,
             checks=[
                 (lambda b: b.get("id") == _doc, "id matches"),
                 (lambda b: "content" not in b, "content excluded from metadata"),
             ])

    # get non-existent → 404
    call(suite, "GET /api/v1/documents/nonexistent → 404",
         lambda: client.get("/api/v1/documents/nonexistent-doc-xyz"), 404)

    # get content
    if created_doc_id:
        _doc = created_doc_id
        call(suite, "GET /api/v1/documents/{id}/content → 200",
             lambda: client.get(f"/api/v1/documents/{_doc}/content"), 200,
             checks=[(lambda b: "content" in b, "content field present")])

    # get pretty (may be 501)
    if created_doc_id:
        _doc = created_doc_id
        call(suite, "GET /api/v1/documents/{id}/pretty → 200",
             lambda: client.get(f"/api/v1/documents/{_doc}/pretty"), 200,
             checks=[(lambda b: "title" in b and "content" in b, "title and content present")])

    # get title (may be 501)
    if created_doc_id:
        _doc = created_doc_id
        call(suite, "GET /api/v1/documents/{id}/title → 200",
             lambda: client.get(f"/api/v1/documents/{_doc}/title"), 200,
             checks=[(lambda b: "title" in b, "title field present")])

    # get embeddings (no embeddings yet → 404)
    if created_doc_id:
        _doc = created_doc_id
        call(suite, "GET /api/v1/documents/{id}/embeddings → 404 (no embeddings yet)",
             lambda: client.get(f"/api/v1/documents/{_doc}/embeddings"), 404)

    # PATCH content (invalidates embeddings)
    if created_doc_id:
        _doc = created_doc_id
        body = call(suite, "PATCH /api/v1/documents/{id}/content → 200",
                    lambda: client.patch(f"/api/v1/documents/{_doc}/content",
                                         json={"content": "Updated content."}), 200,
                    checks=[(lambda b: b.get("has_embeddings") is False,
                              "has_embeddings=False after content update")])

    # PATCH title (may be 501)
    if created_doc_id:
        _doc = created_doc_id
        call(suite, "PATCH /api/v1/documents/{id}/title → 200",
             lambda: client.patch(f"/api/v1/documents/{_doc}/title",
                                   json={"title": "Updated Test Document"}), 200)

    # PATCH embeddings (may be 501)
    if created_doc_id:
        _doc = created_doc_id
        fake_embeddings = [0.1] * 2560
        call(suite, "PATCH /api/v1/documents/{id}/embeddings → 200",
             lambda: client.patch(f"/api/v1/documents/{_doc}/embeddings",
                                   json={"embeddings": fake_embeddings, "model": "test-model"}),
             200,
             checks=[(lambda b: b.get("has_embeddings") is True,
                      "has_embeddings=True after embeddings update")])

    # GET embeddings after upload (may be 501 if PATCH embeddings not implemented)
    if created_doc_id:
        _doc = created_doc_id
        call(suite, "GET /api/v1/documents/{id}/embeddings → 200 (after upload)",
             lambda: client.get(f"/api/v1/documents/{_doc}/embeddings"), 200,
             checks=[
                 (lambda b: "embeddings" in b, "embeddings field present"),
                 (lambda b: b.get("dimension") == 2560, "dimension=2560"),
             ])

    # PUT full update (may be 501)
    if created_doc_id and library_id:
        _doc, _lib = created_doc_id, library_id
        call(suite, "PUT /api/v1/documents/{id} → 200",
             lambda: client.put(f"/api/v1/documents/{_doc}",
                                 json={"title": "Fully Updated Doc",
                                       "content": "New full content",
                                       "library_id": _lib}), 200)

    # PATCH library (move document; may be 501)
    if created_doc_id and library_id:
        _doc, _lib = created_doc_id, library_id
        call(suite, "PATCH /api/v1/documents/{id}/library → 200",
             lambda: client.patch(f"/api/v1/documents/{_doc}/library",
                                   json={"library_id": _lib}), 200)

    # list includes created document
    if created_doc_id:
        _doc = created_doc_id
        call(suite, "GET /api/v1/documents includes created document",
             lambda: client.get("/api/v1/documents"), 200,
             checks=[(lambda b: _doc in [d.get("id") for d in (b if isinstance(b, list) else [])],
                      "created doc id in list")])

    return suite, created_doc_id


def test_document_fetch(client: httpx.Client, library_id: str | None) -> Suite:
    suite = Suite("Document Fetch from URL")

    if not library_id:
        suite.add("POST /api/v1/documents/fetch", Status.SKIP, "no library_id available")
        return suite

    _lib = library_id
    call(suite, "POST /api/v1/documents/fetch → 201",
         lambda: client.post("/api/v1/documents/fetch", json={
             "title": "Example Domain",
             "library_id": _lib,
             "url": "https://example.com",
         }, timeout=30.0), 201)

    # bad URL → 400 (or 501 if not implemented)
    call(suite, "POST /api/v1/documents/fetch bad URL → 400",
         lambda: client.post("/api/v1/documents/fetch", json={
             "title": "Bad",
             "library_id": _lib,
             "url": "https://this-domain-should-not-exist-xyz-abc-123.invalid/",
         }, timeout=30.0), 400)

    return suite


def test_mcp(client: httpx.Client, library_id: str | None) -> Suite:
    suite = Suite("MCP Tools")

    # resolve-library-id
    call(suite, "POST /mcp resolve-library-id → 200",
         lambda: client.post("/mcp", json={
             "jsonrpc": "2.0", "id": 1, "method": "tools/call",
             "params": {"name": "resolve-library-id",
                        "arguments": {"libraryName": "IntegrationTestLib",
                                      "query": "Python test library"}},
         }), 200,
         checks=[
             (lambda b: "result" in b, "result field present"),
             (lambda b: b.get("jsonrpc") == "2.0", "jsonrpc == '2.0'"),
         ])

    # query-docs
    if library_id:
        _lib = library_id
        call(suite, "POST /mcp query-docs → 200",
             lambda: client.post("/mcp", json={
                 "jsonrpc": "2.0", "id": 2, "method": "tools/call",
                 "params": {"name": "query-docs",
                            "arguments": {"libraryId": _lib, "query": "test content"}},
             }), 200,
             checks=[
                 (lambda b: "result" in b, "result field present"),
                 (lambda b: b.get("jsonrpc") == "2.0", "jsonrpc == '2.0'"),
             ])
    else:
        suite.add("POST /mcp query-docs", Status.SKIP, "no library_id available")

    # unsupported method → 400
    call(suite, "POST /mcp unsupported method → 400",
         lambda: client.post("/mcp", json={
             "jsonrpc": "2.0", "id": 3, "method": "tools/unknown",
             "params": {"name": "noop", "arguments": {}},
         }), 400)

    # unknown tool name → 400
    call(suite, "POST /mcp unknown tool name → 400",
         lambda: client.post("/mcp", json={
             "jsonrpc": "2.0", "id": 4, "method": "tools/call",
             "params": {"name": "no-such-tool", "arguments": {}},
         }), 400)

    return suite


def test_cleanup(
    client: httpx.Client, doc_id: str | None, library_id: str | None
) -> Suite:
    suite = Suite("Cleanup (delete)")

    # delete document
    if doc_id:
        _doc = doc_id
        call(suite, "DELETE /api/v1/documents/{id} → 200",
             lambda: client.delete(f"/api/v1/documents/{_doc}"), 200,
             checks=[(lambda b: b.get("success") is True, "success=True")])

        # second delete → 404
        call(suite, "DELETE /api/v1/documents/{id} again → 404",
             lambda: client.delete(f"/api/v1/documents/{_doc}"), 404)

    # delete library
    if library_id:
        _lib = library_id
        call(suite, "DELETE /api/v1/libraries/{id} → 200",
             lambda: client.delete(f"/api/v1/libraries/{_lib}"), 200,
             checks=[(lambda b: b.get("success") is True, "success=True")])

        # second delete → 404
        call(suite, "DELETE /api/v1/libraries/{id} again → 404",
             lambda: client.delete(f"/api/v1/libraries/{_lib}"), 404)

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
                initial_indent="      ", subsequent_indent="      "
            )
            print(line)
            print(wrapped)
        else:
            print(line)


def run_all(base_url: str) -> int:
    """Run all suites. Returns 0 on success (all pass or skip), 1 on failures, 2 on connection error."""
    use_color = sys.stdout.isatty()

    print(f"\nContext7 MCP Integration Tests")
    print(f"Target: {base_url}")
    print("=" * 64)

    # Quick connectivity check before running anything
    try:
        probe = httpx.get(f"{base_url}/health", timeout=5.0)
    except httpx.ConnectError:
        print(f"\nERROR: Cannot connect to {base_url}")
        print("Is the server running? Try: just serve")
        return 2
    except httpx.TimeoutException:
        print(f"\nERROR: Server at {base_url} is not responding (timeout)")
        return 2

    client = httpx.Client(base_url=base_url, timeout=15.0)
    all_suites: list[Suite] = []

    all_suites.append(test_health(client))

    lib_suite, library_id = test_libraries(client)
    all_suites.append(lib_suite)

    doc_suite, doc_id = test_documents(client, library_id)
    all_suites.append(doc_suite)

    all_suites.append(test_document_fetch(client, library_id))
    all_suites.append(test_mcp(client, library_id))
    all_suites.append(test_cleanup(client, doc_id, library_id))

    for suite in all_suites:
        print_suite(suite, use_color)

    total_pass = sum(s.passed for s in all_suites)
    total_fail = sum(s.failed for s in all_suites)
    total_skip = sum(s.skipped for s in all_suites)
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
    parser = argparse.ArgumentParser(description="Integration tests for Context7 MCP API")
    parser.add_argument(
        "--base-url", default=BASE_URL,
        help=f"Base URL of the server (default: {BASE_URL})"
    )
    args = parser.parse_args()
    sys.exit(run_all(args.base_url))


if __name__ == "__main__":
    main()
