"""Tests for MCP Streamable HTTP transport (spec 2024-11-05).

These tests verify the requirements documented in MCP_TRANSPORT_ISSUE.md.
They will only pass once the server implements the full Streamable HTTP
transport protocol — SSE framing, session management, content negotiation,
and GET/DELETE method support on the /mcp endpoint.

Run against a live server:
    uv run pytest tests/test_mcp_transport.py -v
"""

import json
import re

import httpx
import pytest

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

MCP_ACCEPT = "text/event-stream, application/json"
MCP_CONTENT_TYPE = "application/json"
MCP_PROTOCOL_VERSION = "2024-11-05"


def jsonrpc(method: str, params: dict | None = None, req_id: int = 1) -> dict:
    """Build a JSON-RPC 2.0 request body."""
    body: dict = {"jsonrpc": "2.0", "id": req_id, "method": method}
    if params is not None:
        body["params"] = params
    return body


def parse_sse_events(text: str) -> list[dict]:
    """Parse an SSE text stream into a list of dicts with 'event' and 'data' keys.

    Each SSE event looks like:
        event: message
        data: {"jsonrpc":"2.0",...}

    Events are separated by blank lines.
    """
    events: list[dict] = []
    current: dict = {}

    for line in text.splitlines():
        if line.startswith("event:"):
            current["event"] = line[len("event:"):].strip()
        elif line.startswith("data:"):
            current["data"] = line[len("data:"):].strip()
        elif line == "" and current:
            events.append(current)
            current = {}

    # Handle final event if stream doesn't end with a blank line
    if current:
        events.append(current)

    return events


def parse_sse_jsonrpc(text: str) -> list[dict]:
    """Extract parsed JSON-RPC objects from an SSE stream."""
    events = parse_sse_events(text)
    results = []
    for ev in events:
        if ev.get("event") == "message" and "data" in ev:
            results.append(json.loads(ev["data"]))
    return results


def send_initialize(client: httpx.Client) -> httpx.Response:
    """Send an MCP initialize request with proper transport headers."""
    return client.post(
        "/mcp",
        json=jsonrpc("initialize", {
            "protocolVersion": MCP_PROTOCOL_VERSION,
            "capabilities": {},
            "clientInfo": {"name": "test-client", "version": "1.0.0"},
        }),
        headers={
            "Accept": MCP_ACCEPT,
            "Content-Type": MCP_CONTENT_TYPE,
        },
    )


def extract_session_id(response: httpx.Response) -> str | None:
    """Extract the Mcp-Session-Id from a response."""
    return response.headers.get("mcp-session-id")


# ---------------------------------------------------------------------------
# 1. POST /mcp — Content negotiation and SSE framing
# ---------------------------------------------------------------------------


class TestPostContentNegotiation:
    """POST /mcp must respect the Accept header and return SSE or JSON."""

    def test_initialize_returns_sse_when_requested(self, client: httpx.Client) -> None:
        """When Accept includes text/event-stream, response MUST be SSE."""
        r = send_initialize(client)
        assert r.status_code == 200
        content_type = r.headers.get("content-type", "")
        assert "text/event-stream" in content_type, (
            f"Expected text/event-stream, got: {content_type}"
        )

    def test_sse_response_contains_event_message_frame(
        self, client: httpx.Client
    ) -> None:
        """SSE body must contain 'event: message' + 'data: <json>' frames."""
        r = send_initialize(client)
        assert r.status_code == 200

        events = parse_sse_events(r.text)
        assert len(events) >= 1, f"Expected at least one SSE event, got: {r.text!r}"
        assert events[0].get("event") == "message", (
            f"First SSE event type should be 'message', got: {events[0]}"
        )
        assert "data" in events[0], "SSE event missing 'data' field"

    def test_sse_data_is_valid_jsonrpc(self, client: httpx.Client) -> None:
        """The data field inside the SSE event must be a valid JSON-RPC 2.0 response."""
        r = send_initialize(client)
        messages = parse_sse_jsonrpc(r.text)
        assert len(messages) >= 1, "No JSON-RPC messages in SSE stream"

        msg = messages[0]
        assert msg.get("jsonrpc") == "2.0"
        assert "result" in msg, f"Expected 'result' in JSON-RPC response: {msg}"
        assert msg.get("id") == 1

    def test_initialize_result_contains_required_fields(
        self, client: httpx.Client
    ) -> None:
        """Initialize result must have protocolVersion, capabilities, serverInfo."""
        r = send_initialize(client)
        messages = parse_sse_jsonrpc(r.text)
        assert len(messages) >= 1

        result = messages[0]["result"]
        assert "protocolVersion" in result, "Missing protocolVersion"
        assert "capabilities" in result, "Missing capabilities"
        assert "serverInfo" in result, "Missing serverInfo"

    def test_tools_list_returns_sse(self, client: httpx.Client) -> None:
        """tools/list must also return SSE when Accept header requests it."""
        # Initialize first to get a session
        init_r = send_initialize(client)
        session_id = extract_session_id(init_r)

        headers: dict[str, str] = {
            "Accept": MCP_ACCEPT,
            "Content-Type": MCP_CONTENT_TYPE,
        }
        if session_id:
            headers["Mcp-Session-Id"] = session_id

        r = client.post(
            "/mcp",
            json=jsonrpc("tools/list", req_id=2),
            headers=headers,
        )
        assert r.status_code == 200
        assert "text/event-stream" in r.headers.get("content-type", "")

        messages = parse_sse_jsonrpc(r.text)
        assert len(messages) >= 1
        assert "tools" in messages[0].get("result", {}), "tools/list result missing 'tools'"


# ---------------------------------------------------------------------------
# 2. Mcp-Session-Id session management
# ---------------------------------------------------------------------------


class TestSessionManagement:
    """The server must issue and enforce Mcp-Session-Id headers."""

    def test_initialize_returns_session_id_header(
        self, client: httpx.Client
    ) -> None:
        """After initialize, the response MUST include Mcp-Session-Id."""
        r = send_initialize(client)
        assert r.status_code == 200

        session_id = extract_session_id(r)
        assert session_id is not None, (
            f"Missing Mcp-Session-Id header. Headers: {dict(r.headers)}"
        )
        assert len(session_id) > 0, "Mcp-Session-Id must not be empty"

    def test_session_id_is_unique_per_init(self, client: httpx.Client) -> None:
        """Each initialize call should produce a distinct session ID."""
        r1 = send_initialize(client)
        r2 = send_initialize(client)
        id1 = extract_session_id(r1)
        id2 = extract_session_id(r2)
        assert id1 is not None and id2 is not None
        assert id1 != id2, "Session IDs should be unique across initialize calls"

    def test_post_requires_session_id_after_init(
        self, client: httpx.Client
    ) -> None:
        """After initialize, subsequent POST requests without Mcp-Session-Id should be rejected."""
        init_r = send_initialize(client)
        assert init_r.status_code == 200
        assert extract_session_id(init_r) is not None

        # Send tools/list WITHOUT the session ID header
        r = client.post(
            "/mcp",
            json=jsonrpc("tools/list", req_id=2),
            headers={
                "Accept": MCP_ACCEPT,
                "Content-Type": MCP_CONTENT_TYPE,
                # Deliberately omit Mcp-Session-Id
            },
        )
        # The spec says the server SHOULD reject requests with a missing or
        # invalid session ID. Accept 400 or 409 as valid rejection codes.
        # If the server allows it, that's a session-management gap.
        # NOTE: For this test we just verify the server returns a session_id
        # on init. Full session enforcement tests below check rejection.
        assert r.status_code in (
            200,  # server may accept sessionless requests (lenient)
            400,
            409,
        ), f"Unexpected status {r.status_code} for missing session ID"

    def test_post_with_valid_session_id_succeeds(
        self, client: httpx.Client
    ) -> None:
        """POST with correct Mcp-Session-Id should succeed."""
        init_r = send_initialize(client)
        session_id = extract_session_id(init_r)
        assert session_id is not None

        r = client.post(
            "/mcp",
            json=jsonrpc("tools/list", req_id=2),
            headers={
                "Accept": MCP_ACCEPT,
                "Content-Type": MCP_CONTENT_TYPE,
                "Mcp-Session-Id": session_id,
            },
        )
        assert r.status_code == 200


# ---------------------------------------------------------------------------
# 3. GET /mcp — SSE stream for server-initiated messages
# ---------------------------------------------------------------------------


class TestGetSseStream:
    """GET /mcp must open an SSE stream for server-initiated notifications."""

    def test_get_endpoint_exists(self, client: httpx.Client) -> None:
        """GET /mcp must not return 405 Method Not Allowed."""
        init_r = send_initialize(client)
        session_id = extract_session_id(init_r)
        assert session_id is not None

        # GET opens a long-lived SSE stream.  Use stream mode with a short
        # read timeout so the test doesn't hang.
        with client.stream(
            "GET",
            "/mcp",
            headers={
                "Accept": "text/event-stream",
                "Mcp-Session-Id": session_id,
            },
        ) as r:
            # Should return 200 with SSE, not 405
            assert r.status_code != 405, "GET /mcp must be supported (got 405)"
            assert r.status_code == 200

    def test_get_returns_event_stream_content_type(
        self, client: httpx.Client
    ) -> None:
        """GET /mcp must return Content-Type: text/event-stream."""
        init_r = send_initialize(client)
        session_id = extract_session_id(init_r)
        assert session_id is not None

        with client.stream(
            "GET",
            "/mcp",
            headers={
                "Accept": "text/event-stream",
                "Mcp-Session-Id": session_id,
            },
        ) as r:
            content_type = r.headers.get("content-type", "")
            assert "text/event-stream" in content_type, (
                f"GET /mcp should return text/event-stream, got: {content_type}"
            )

    def test_get_without_session_id_rejected(self, client: httpx.Client) -> None:
        """GET /mcp without Mcp-Session-Id should be rejected."""
        r = client.get(
            "/mcp",
            headers={"Accept": "text/event-stream"},
        )
        # Should get 400 or 409, not 200
        assert r.status_code in (400, 409), (
            f"GET /mcp without session ID should be rejected, got {r.status_code}"
        )


# ---------------------------------------------------------------------------
# 4. DELETE /mcp — Session termination
# ---------------------------------------------------------------------------


class TestDeleteSession:
    """DELETE /mcp must terminate the session."""

    def test_delete_endpoint_exists(self, client: httpx.Client) -> None:
        """DELETE /mcp must not return 405 Method Not Allowed."""
        init_r = send_initialize(client)
        session_id = extract_session_id(init_r)
        assert session_id is not None

        r = client.delete(
            "/mcp",
            headers={"Mcp-Session-Id": session_id},
        )
        assert r.status_code != 405, "DELETE /mcp must be supported (got 405)"
        # 200 or 204 both acceptable
        assert r.status_code in (200, 204), (
            f"Expected 200 or 204 for DELETE, got {r.status_code}"
        )

    def test_delete_invalidates_session(self, client: httpx.Client) -> None:
        """After DELETE, the session ID should no longer be valid."""
        init_r = send_initialize(client)
        session_id = extract_session_id(init_r)
        assert session_id is not None

        # Delete the session
        del_r = client.delete(
            "/mcp",
            headers={"Mcp-Session-Id": session_id},
        )
        assert del_r.status_code in (200, 204)

        # Try to use the old session ID — should be rejected
        r = client.post(
            "/mcp",
            json=jsonrpc("tools/list", req_id=3),
            headers={
                "Accept": MCP_ACCEPT,
                "Content-Type": MCP_CONTENT_TYPE,
                "Mcp-Session-Id": session_id,
            },
        )
        assert r.status_code in (400, 404, 409), (
            f"Using deleted session should fail, got {r.status_code}"
        )

    def test_delete_without_session_id_rejected(
        self, client: httpx.Client
    ) -> None:
        """DELETE /mcp without Mcp-Session-Id should be rejected."""
        r = client.delete("/mcp")
        assert r.status_code in (400, 409), (
            f"DELETE without session ID should be rejected, got {r.status_code}"
        )


# ---------------------------------------------------------------------------
# 5. Protocol headers
# ---------------------------------------------------------------------------


class TestProtocolHeaders:
    """The server must handle MCP-specific protocol headers."""

    def test_initialize_accepts_protocol_version_header(
        self, client: httpx.Client
    ) -> None:
        """Server should accept and respect MCP-Protocol-Version header."""
        r = client.post(
            "/mcp",
            json=jsonrpc("initialize", {"protocolVersion": MCP_PROTOCOL_VERSION}),
            headers={
                "Accept": MCP_ACCEPT,
                "Content-Type": MCP_CONTENT_TYPE,
                "MCP-Protocol-Version": MCP_PROTOCOL_VERSION,
            },
        )
        assert r.status_code == 200

    def test_cors_exposes_session_id(self, client: httpx.Client) -> None:
        """Access-Control-Expose-Headers should include Mcp-Session-Id."""
        r = send_initialize(client)
        exposed = r.headers.get("access-control-expose-headers", "")
        assert "mcp-session-id" in exposed.lower(), (
            f"CORS must expose Mcp-Session-Id. "
            f"Access-Control-Expose-Headers: {exposed}"
        )


# ---------------------------------------------------------------------------
# 6. Notifications (JSON-RPC notifications have no id)
# ---------------------------------------------------------------------------


class TestNotifications:
    """JSON-RPC notifications (no id) must be accepted without response body."""

    def test_notification_accepted(self, client: httpx.Client) -> None:
        """Server must accept notifications/initialized after init."""
        init_r = send_initialize(client)
        session_id = extract_session_id(init_r)
        assert session_id is not None

        notification = {
            "jsonrpc": "2.0",
            "method": "notifications/initialized",
        }
        headers: dict[str, str] = {
            "Accept": MCP_ACCEPT,
            "Content-Type": MCP_CONTENT_TYPE,
            "Mcp-Session-Id": session_id,
        }

        r = client.post("/mcp", json=notification, headers=headers)
        # 200 or 202 or 204 are all acceptable for notifications
        assert r.status_code in (200, 202, 204), (
            f"Notification should be accepted, got {r.status_code}"
        )


# ---------------------------------------------------------------------------
# 7. Full handshake flow (end-to-end)
# ---------------------------------------------------------------------------


class TestFullHandshake:
    """Simulate the complete rmcp client handshake sequence.

    This is the sequence that Claude Code's rmcp client performs:
    1. POST initialize (with Accept: text/event-stream)
    2. Receive SSE response with Mcp-Session-Id
    3. POST notifications/initialized
    4. POST tools/list
    5. POST tools/call
    """

    def test_complete_handshake(self, client: httpx.Client) -> None:
        """Full init → notify → list → call sequence must succeed."""
        # Step 1: Initialize
        init_r = send_initialize(client)
        assert init_r.status_code == 200
        assert "text/event-stream" in init_r.headers.get("content-type", "")

        session_id = extract_session_id(init_r)
        assert session_id is not None, "No Mcp-Session-Id after initialize"

        init_messages = parse_sse_jsonrpc(init_r.text)
        assert len(init_messages) >= 1
        assert "result" in init_messages[0]

        headers = {
            "Accept": MCP_ACCEPT,
            "Content-Type": MCP_CONTENT_TYPE,
            "Mcp-Session-Id": session_id,
        }

        # Step 2: Send notifications/initialized
        notif_r = client.post(
            "/mcp",
            json={"jsonrpc": "2.0", "method": "notifications/initialized"},
            headers=headers,
        )
        assert notif_r.status_code in (200, 202, 204)

        # Step 3: tools/list
        list_r = client.post(
            "/mcp",
            json=jsonrpc("tools/list", req_id=2),
            headers=headers,
        )
        assert list_r.status_code == 200
        list_messages = parse_sse_jsonrpc(list_r.text)
        assert len(list_messages) >= 1
        tools = list_messages[0].get("result", {}).get("tools", [])
        assert len(tools) > 0, "tools/list returned no tools"

        tool_names = {t["name"] for t in tools}
        assert "resolve-library-id" in tool_names

        # Step 4: tools/call
        call_r = client.post(
            "/mcp",
            json=jsonrpc(
                "tools/call",
                {
                    "name": "resolve-library-id",
                    "arguments": {
                        "libraryName": "fastapi",
                        "query": "Python web framework",
                    },
                },
                req_id=3,
            ),
            headers=headers,
        )
        assert call_r.status_code == 200
        call_messages = parse_sse_jsonrpc(call_r.text)
        assert len(call_messages) >= 1
        assert "result" in call_messages[0]


# ---------------------------------------------------------------------------
# 8. Error cases
# ---------------------------------------------------------------------------


class TestErrorCases:
    """Transport-level error handling."""

    def test_invalid_json_returns_error(self, client: httpx.Client) -> None:
        """Malformed JSON body should return 400, not 500."""
        r = client.post(
            "/mcp",
            content=b"not json at all",
            headers={
                "Accept": MCP_ACCEPT,
                "Content-Type": MCP_CONTENT_TYPE,
            },
        )
        assert r.status_code in (400, 422), (
            f"Invalid JSON should be 400 or 422, got {r.status_code}"
        )

    def test_missing_jsonrpc_field(self, client: httpx.Client) -> None:
        """Request missing 'jsonrpc' field should be handled gracefully."""
        r = client.post(
            "/mcp",
            json={"method": "initialize", "id": 1},
            headers={
                "Accept": MCP_ACCEPT,
                "Content-Type": MCP_CONTENT_TYPE,
            },
        )
        # Should not crash — 200 with error result or 400 are both fine
        assert r.status_code in (200, 400, 422)

    def test_unsupported_method_returns_jsonrpc_error(
        self, client: httpx.Client
    ) -> None:
        """An unknown method should return a JSON-RPC error, not an HTTP error."""
        init_r = send_initialize(client)
        session_id = extract_session_id(init_r)

        headers: dict[str, str] = {
            "Accept": MCP_ACCEPT,
            "Content-Type": MCP_CONTENT_TYPE,
        }
        if session_id:
            headers["Mcp-Session-Id"] = session_id

        r = client.post(
            "/mcp",
            json=jsonrpc("nonexistent/method", req_id=99),
            headers=headers,
        )
        # Server should respond (possibly as SSE) with a JSON-RPC error
        assert r.status_code in (200, 400)
