# Context7 MCP Documentation

## Overview

Context7 is an MCP (Model Context Protocol) server that provides up-to-date, version-specific documentation and code examples for programming libraries and frameworks directly into LLM prompts.

## MCP Tools

Context7 provides two primary tools for integration:

### 1. `resolve-library-id`

**Purpose:** Resolves a package/product name to a Context7-compatible library ID and returns matching libraries.

**Required Parameters:**
- `libraryName` (string): Library name to search for and retrieve a Context7-compatible library ID
- `query` (string): The user's original question or task, used to rank library results by relevance

**Returns:** Context7-compatible library ID in the format `/org/project` or `/org/project/version`

**Usage Example:**
```
libraryName: "Next.js"
query: "How to set up API routes in Next.js"
→ Returns: "/vercel/next.js"
```

**Selection Criteria:**
- Name similarity to the query (exact matches prioritized)
- Description relevance to the query's intent
- Documentation coverage (libraries with higher Code Snippet counts)
- Source reputation (High or Medium reputation prioritized)
- Benchmark Score (quality indicator, 100 is highest)

**Important Notes:**
- You MUST call this function before `query-docs` to obtain a valid library ID UNLESS the user explicitly provides a library ID in the format `/org/project` or `/org/project/version`
- Do not call this tool more than 3 times per question
- Do not include sensitive information (API keys, passwords, credentials) in queries

### 2. `query-docs`

**Purpose:** Retrieves and queries up-to-date documentation and code examples from Context7 for any programming library or framework.

**Required Parameters:**
- `libraryId` (string): Exact Context7-compatible library ID (e.g., `/mongodb/docs`, `/vercel/next.js`, `/supabase/supabase`, `/vercel/next.js/v14.3.0-canary.87`)
- `query` (string): The question or task you need help with

**Usage Example:**
```
libraryId: "/vercel/next.js"
query: "How to set up authentication with JWT in Next.js"
```

**Query Guidelines:**
- Be specific and include relevant details
- Good: "How to set up authentication with JWT in Express.js" or "React useEffect cleanup function examples"
- Bad: "auth" or "hooks"
- Do not include sensitive information (API keys, passwords, credentials)

**Important Notes:**
- You must call `resolve-library-id` first to obtain the library ID, unless the user provides it explicitly
- Do not call this tool more than 3 times per question
- If you cannot find what you need after 3 calls, use the best information available

## Library ID Format

Context7 library IDs follow these formats:
- Standard: `/org/project` (e.g., `/mongodb/docs`, `/vercel/next.js`)
- Version-specific: `/org/project/version` (e.g., `/vercel/next.js/v14.3.0-canary.87`)

## Workflow Pattern

1. **Identify the library** the user is asking about
2. **Call `resolve-library-id`** with:
   - The library name
   - The user's original question (for relevance ranking)
3. **Get the library ID** from the response
4. **Call `query-docs`** with:
   - The obtained library ID
   - A specific, detailed query about what you need to know

## User Invocation Methods

Users can trigger Context7 documentation retrieval through:

1. **Explicit keyword:** Add "use context7" to any prompt
2. **Specific library:** "use library /supabase/supabase for API and docs"
3. **Version specification:** Mention the version (e.g., "Next.js 14") in prompts
4. **Automatic rules:** Configure MCP client rules for automatic invocation

## Installation

### Remote MCP Server
- **Standard HTTP endpoint:** `https://mcp.context7.com/mcp`
- **OAuth endpoint:** `https://mcp.context7.com/mcp/oauth`

### Local Installation
```bash
# Using npm/npx
npx -y @upstash/context7-mcp --api-key YOUR_API_KEY

# Using Bun
bunx @upstash/context7-mcp --api-key YOUR_API_KEY

# Using Deno
deno run --allow-net npm:@upstash/context7-mcp --api-key YOUR_API_KEY
```

## Authentication

- **API Key:** Set via `CONTEXT7_API_KEY` environment variable or header (recommended for higher rate limits)
- **OAuth 2.0:** Supported for compatible MCP clients
- **Free Tier:** Available at [context7.com/dashboard](https://context7.com/dashboard)

## Best Practices

1. **Always resolve library IDs first** unless you know the exact ID format
2. **Limit tool calls** to 3 per question to avoid excessive API usage
3. **Be specific in queries** to get the most relevant documentation
4. **Never include sensitive data** in query parameters
5. **Use version-specific IDs** when working with specific library versions
6. **Check library reputation and benchmark scores** when selecting from multiple matches

## Rate Limits

- Higher rate limits available with API key authentication
- Free tier available for development and testing
- Exact limits depend on your Context7 account tier

## Sources

- [GitHub - upstash/context7](https://github.com/upstash/context7)
- [Context7 MCP Blog Post](https://upstash.com/blog/context7-mcp)
- [Context7 Documentation](https://context7.com/docs/resources/all-clients)
- [Smithery - Context7 MCP Server](https://smithery.ai/server/@upstash/context7-mcp)
- [npm - @upstash/context7-mcp](https://www.npmjs.com/package/@upstash/context7-mcp)
