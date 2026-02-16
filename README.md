# Context7 MCP Testing

This project tests the Context7 MCP server endpoints using a Python script driven by a Justfile.

## Prerequisites

- [uv](https://github.com/astral-sh/uv) - Python package installer and runner
- [just](https://github.com/casey/just) - Command runner (optional, but recommended)

## Quick Start

### Using Just (Recommended)

```bash
# Show available commands
just

# Setup the script
just setup

# Run a forward pass test (resolve + query)
just forward

# Test with Next.js
just nextjs

# Test with React
just react "How to manage state with useState"

# Test with Supabase
just supabase "How to authenticate users"

# List available MCP tools
just list

# Run all test examples
just test-all
```

### Direct Python Usage

```bash
# Run forward pass (full workflow)
./context7_test.py forward-pass "React" "How to use useState hook"

# Resolve library ID only
./context7_test.py resolve "Next.js" "How to create API routes"

# Query docs only (requires library ID)
./context7_test.py query "/vercel/next.js" "How to use middleware"

# List available tools
./context7_test.py list-tools

# Show help
./context7_test.py --help
```

## Commands

### Forward Pass
The main command that demonstrates the complete workflow:

```bash
just forward "Library Name" "Your question"
```

This will:
1. Call `resolve-library-id` to convert the library name to a Context7 ID
2. Call `query-docs` to retrieve documentation

### Individual Endpoints

**Resolve Library ID:**
```bash
just resolve "Express.js" "How to set up routes"
./context7_test.py resolve "Express.js" "How to set up routes"
```

**Query Documentation:**
```bash
just query "/expressjs/express" "How to use middleware"
./context7_test.py query "/expressjs/express" "How to use middleware"
```

## Pre-configured Examples

The Justfile includes several pre-configured examples:

- `just react [query]` - Test with React
- `just nextjs [query]` - Test with Next.js
- `just supabase [query]` - Test with Supabase
- `just mongodb [query]` - Test with MongoDB

## With API Key

For higher rate limits, use an API key from [context7.com/dashboard](https://context7.com/dashboard):

```bash
# With Just
just forward-with-key "React" "How to use hooks" "your-api-key"

# Direct Python
./context7_test.py forward-pass "React" "How to use hooks" --api-key "your-api-key"
```

Or set it as an environment variable:
```bash
export CONTEXT7_API_KEY="your-api-key"
```

## Output

The script uses Rich formatting to display:
- 📤 Request payloads (formatted JSON)
- 📥 Response data (formatted JSON)
- ✅ Success indicators
- ❌ Error messages with details

## Script Features

- **Inline dependencies**: Uses PEP 723 inline script metadata for uv
- **Rich output**: Formatted, colored console output
- **Error handling**: Comprehensive error reporting
- **Auto-extraction**: Attempts to automatically extract library IDs from responses
- **Multiple commands**: Supports testing individual endpoints or full workflow

## Dependencies

The script automatically manages its dependencies via uv:
- `typer` - CLI framework
- `rich` - Terminal formatting
- `httpx` - HTTP client

No manual installation required when using uv!

## Troubleshooting

**Script not executable:**
```bash
just setup
# or
chmod +x context7_test.py
```

**uv not found:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**just not found:**
```bash
# On Linux
cargo install just
# or use your package manager
```

**Rate limiting:**
Get an API key from [context7.com/dashboard](https://context7.com/dashboard) and use `--api-key` flag.

## Examples

```bash
# Test React hooks
just react "How to use useEffect for data fetching"

# Test Next.js App Router
just nextjs "How to use Server Actions in Next.js 14"

# Test Supabase authentication
just supabase "How to implement email authentication"

# Test MongoDB connection
just mongodb "How to connect to Atlas with connection string"

# Custom query with Express
just forward "Express.js" "How to handle file uploads with multer"
```

## Project Structure

```
.
├── context7_test.py           # Main Python script with inline deps
├── justfile                   # Command runner recipes
├── context7-mcp-documentation.md  # Full MCP documentation
└── README.md                  # This file
```
