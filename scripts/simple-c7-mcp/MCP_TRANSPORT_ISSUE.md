# MCP Streamable HTTP Transport Issue

## The Error

```
MCP client for `simple-c7-mcp` failed to start: MCP startup failed:
handshaking with MCP server failed: Send message error Transport
[rmcp::transport::worker::WorkerTransport<
  rmcp::transport::streamable_http_client::StreamableHttpClientWorker<
    reqwest::async_impl::client::Client
  >>] error: Client error: HTTP status client error (422 Unprocessable Entity)
for url (http://localhost:8000/mcp), when send initialize request
```

## What's Happening

The `rmcp` client (used by Claude Code) connects via the **MCP Streamable HTTP transport** — a specific protocol layered on top of HTTP. Our server implements a bare JSON-RPC 2.0 endpoint, which is not the same thing.

The 422 occurs because FastAPI rejects the initialize request during body validation. The Streamable HTTP client sends requests with protocol-specific headers and content negotiation that our bare endpoint doesn't understand.

## Reference vs Our Implementation

The working Context7 MCP server (`@anthropic/context7-mcp`) uses the official `@modelcontextprotocol/sdk` package, which provides `StreamableHTTPServerTransport`. This transport handles the full protocol automatically. Our server skips all of that.

| Aspect | Context7 (reference) | simple-c7-mcp (ours) |
|---|---|---|
| Transport layer | `StreamableHTTPServerTransport` from SDK | Bare `POST /mcp` FastAPI route |
| HTTP methods on `/mcp` | GET, POST, DELETE | POST only |
| Response format | SSE (`text/event-stream`) or JSON | Plain JSON only |
| Session management | `Mcp-Session-Id` header | None |
| Protocol headers | `MCP-Protocol-Version`, `Accept` negotiation | None |
| CORS | Exposes `MCP-Session-Id`, allows protocol headers | None |

## What the Streamable HTTP Protocol Requires

The MCP Streamable HTTP transport (spec: 2024-11-05) defines three HTTP methods on a single endpoint:

### POST — Send messages

- Client sends JSON-RPC 2.0 with `Content-Type: application/json`
- Client includes `Accept: text/event-stream, application/json`
- Server responds with either:
  - `Content-Type: text/event-stream` — SSE stream containing one or more JSON-RPC responses as `event: message` frames
  - `Content-Type: application/json` — single JSON-RPC response (only for requests without streaming)
- After `initialize`, server MUST return `Mcp-Session-Id` header
- Client MUST include `Mcp-Session-Id` on all subsequent requests

### GET — Open SSE stream

- Client opens a long-lived SSE connection for server-initiated messages (notifications, requests)
- Must include `Mcp-Session-Id` header

### DELETE — End session

- Client terminates the session
- Must include `Mcp-Session-Id` header

### SSE Response Framing

Responses are wrapped as Server-Sent Events:

```
event: message
data: {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2024-11-05",...}}

```

This is not plain JSON — the `event:` and `data:` prefixes are part of the SSE wire format.

## Fix Options

### Option A: Use the Python MCP SDK (recommended)

The official `mcp` Python package provides `StreamableHTTPServerTransport` that handles the protocol. Integrate it with FastAPI or use the SDK's built-in server.

```
pip install mcp
```

This is what the reference server does (in JavaScript), and it handles session management, SSE framing, content negotiation, and all protocol details automatically.

### Option B: Implement the transport manually

Add to the `/mcp` endpoint:

1. Handle GET, POST, and DELETE methods
2. Parse `Accept` header and respond with SSE when requested
3. Generate and track `Mcp-Session-Id` values
4. Frame JSON-RPC responses as SSE events
5. Support `MCP-Protocol-Version` header negotiation
6. Add CORS headers for `Mcp-Session-Id` and `MCP-Protocol-Version`

This is significantly more work than Option A and easy to get wrong.

### Option C: Use stdio transport instead of HTTP

If the server only needs to serve a single local client (like Claude Code), switch to stdio transport. The MCP client spawns the server as a subprocess and communicates over stdin/stdout. This avoids the Streamable HTTP protocol entirely.

Configure in Claude Code's MCP settings:

```json
{
  "mcpServers": {
    "simple-c7-mcp": {
      "command": "uv",
      "args": ["run", "c7-mcp", "serve", "--transport", "stdio"]
    }
  }
}
```

This requires adding a stdio transport mode to the CLI.
