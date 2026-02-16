# Justfile Commands Reference

Quick reference for all available `just` commands in the C7 MCP project.

## 🚀 Quick Start

```bash
# Start the server
just serve

# In another terminal, run the demo
just demo
```

---

## 📋 Table of Contents

- [Development Commands](#development-commands)
- [Library Management](#library-management)
- [Document Management](#document-management)
- [Demo Commands](#demo-commands)
- [Installation Commands](#installation-commands)

---

## Development Commands

### `just run [args]`
Run the CLI without installing.

```bash
just run serve
just run --help
```

### `just serve [port]`
Start the FastAPI server with auto-reload.

**Parameters:**
- `port` - Server port (default: 8000)

```bash
just serve           # Start on port 8000
just serve 8080      # Start on port 8080
```

### `just health [port]`
Check the health endpoint.

```bash
just health          # Check http://127.0.0.1:8000/health
just health 8080     # Check http://127.0.0.1:8080/health
```

### `just lint`
Run type checking and linting.

```bash
just lint
# Runs: ruff check, pyright, basedpyright
```

### `just format`
Auto-format code with ruff.

```bash
just format
# Runs: ruff check --fix, ruff format
```

### `just test`
Run tests with pytest.

```bash
just test
```

---

## Library Management

### `just create-library name language ecosystem [description] [port]`
Create a new library via the API.

**Parameters:**
- `name` - Library name (required)
- `language` - Programming language (required)
- `ecosystem` - Package ecosystem like npm, pypi (required)
- `description` - Library description (optional, default: "")
- `port` - API port (optional, default: 8000)

**Examples:**

```bash
# Minimal library
just create-library "FastAPI" "Python" "pypi"

# With description
just create-library "React" "JavaScript" "npm" "A JavaScript library for building UIs"

# Custom port
just create-library "Vue" "JavaScript" "npm" "Progressive framework" 8080
```

**Response:**
```json
{
  "id": "lib-pypi-fastapi-abc123",
  "name": "FastAPI",
  "context7_id": "/pypi/fastapi",
  "language": "Python",
  "ecosystem": "pypi",
  ...
}
```

### `just list-libraries [port]`
List all libraries in the system.

```bash
just list-libraries           # List on port 8000
just list-libraries 8080      # List on port 8080
```

---

## Document Management

### `just upload-doc file library_id [title] [port]`
Upload a document from a local file.

**Parameters:**
- `file` - Path to file (required)
- `library_id` - Library ID to associate with (required)
- `title` - Document title (optional, defaults to filename)
- `port` - API port (optional, default: 8000)

**Examples:**

```bash
# Upload with auto-generated title
just upload-doc docs/api.md lib-pypi-fastapi-abc123

# Upload with custom title
just upload-doc README.md lib-npm-react-xyz789 "React Getting Started"

# Custom port
just upload-doc guide.md lib-123 "User Guide" 8080
```

**Output:**
```
📤 Uploading: api.md
   Title: api
   Library: lib-pypi-fastapi-abc123
   Size: 5432 bytes

✅ Document uploaded successfully!
   ID: doc-456
   Title: api
```

### `just fetch-doc library query [port]`
Fetch documentation from Context7 and upload to our API.

This command:
1. Resolves library name to Context7 library ID using your query
2. Downloads documentation from Context7
3. Creates library in our system (if doesn't exist)
4. Uploads document to our API

**Parameters:**
- `library` - Library name (required)
- `query` - **Your actual question or use case** (required)
- `port` - API port (optional, default: 8000)

**💡 Pro Tip:** The `query` should be your **real question or use case**, not just "documentation". This helps Context7:
- Find the most relevant library match
- Improve disambiguation when multiple libraries have similar names
- Return more relevant documentation sections

**Examples:**

```bash
# Good: Specific question
just fetch-doc "solidstart" "How to throw a redirect in SolidStart"

# Good: Use case description
just fetch-doc "fastapi" "How to create a REST API with authentication and validation"

# Good: Feature-focused
just fetch-doc "react" "useState and useEffect hooks documentation"

# Bad: Generic (less helpful for Context7)
just fetch-doc "solidstart" "documentation"
just fetch-doc "fastapi" "general info"
```

**Quick Fetch Commands:**

For common libraries, use the convenience commands:
```bash
just fetch-solidstart   # Pre-configured query for SolidStart
just fetch-fastapi      # Pre-configured query for FastAPI
just fetch-react        # Pre-configured query for React
just fetch-vue          # Pre-configured query for Vue
just fetch-daisyui      # Pre-configured query for DaisyUI
```

**Output:**
```
🔍 Step 1: Resolving library: solid-js
✅ Resolved: Solid.js
   Context7 ID: /npm/solid-js
   Score: 0.95

📥 Step 2: Downloading documentation...
   URL: https://context7.com/npm/solid-js/llms.txt
✅ Downloaded: 125430 bytes

📚 Step 3: Creating library in our API...
✅ Library created: solid-js
   ID: lib-npm-solid-js-def456

📤 Step 4: Uploading document to our API...
✅ Document uploaded!
   ID: doc-789
   Title: solid-js Documentation

🎉 Complete! solid-js documentation is now in the system
   Library ID: lib-npm-solid-js-def456
   Context7 ID: /npm/solid-js
```

**Environment Variables:**
- `CONTEXT7_API_KEY` - Optional API key for Context7 (if required)

---

## Demo Commands

### `just demo [port]`
Run a complete demo workflow.

Creates a FastAPI library, generates a sample document, and uploads it.

```bash
just demo           # Demo on port 8000
just demo 8080      # Demo on port 8080
```

**What it does:**
1. Creates FastAPI library
2. Creates sample markdown file
3. Uploads document to the library

### `just demo-fetch [library] [port]`
Demo: Fetch a library from Context7 and upload.

```bash
just demo-fetch                    # Fetch solid-js
just demo-fetch "fastapi"          # Fetch fastapi
just demo-fetch "vue" 8080         # Fetch vue on port 8080
```

---

## Installation Commands

### `just install`
Install the CLI tool globally using `uv tool`.

```bash
just install
# Now you can run: c7-mcp --help
```

### `just uninstall`
Uninstall the CLI tool.

```bash
just uninstall
```

### `just reinstall`
Reinstall the CLI tool (useful after changes).

```bash
just reinstall
```

---

## Utility Commands

### `just clean-db`
Delete the LanceDB database directory.

```bash
just clean-db
# Deletes: lancedb_data/
```

**⚠️ Warning:** This permanently deletes all libraries and documents!

---

## Common Workflows

### 1. Start Development

```bash
# Terminal 1: Start server
just serve

# Terminal 2: Run commands
just health
just list-libraries
```

### 2. Create Library and Upload Docs

```bash
# Create library
just create-library "MyLib" "Python" "pypi" "My awesome library"

# Upload documentation
just upload-doc README.md lib-pypi-mylib-abc123 "MyLib Documentation"
```

### 3. Fetch from Context7

```bash
# Start server
just serve

# In another terminal, fetch libraries
just fetch-doc "solid-js"
just fetch-doc "fastapi"
just fetch-doc "daisyui"
```

### 4. Full Demo

```bash
# Terminal 1
just serve

# Terminal 2
just demo
just demo-fetch "solid-js"
```

---

## Tips & Tricks

### Check if server is running
```bash
just health
# Should return: {"status":"healthy","service":"c7-mcp"}
```

### View OpenAPI docs
```bash
just serve
# Then visit: http://127.0.0.1:8000/docs
```

### Debug failed uploads
Check the server logs in Terminal 1 for detailed error messages.

### Use with different ports
Most commands support a `port` parameter:
```bash
just serve 8080
just health 8080
just create-library "Test" "Python" "pypi" "" 8080
```

---

## Error Handling

### Server not running
```
❌ Error: [Errno 111] Connection refused
```
**Solution:** Start the server with `just serve`

### Library already exists
```
❌ Error 400: Library 'FastAPI' already exists in ecosystem 'pypi'
```
**Solution:** Use a different name or delete the existing library

### File not found
```
❌ File not found: docs/missing.md
```
**Solution:** Check the file path is correct

### Context7 API failure
```
❌ Context7 API request failed: HTTP Error 404
```
**Solution:** Library may not be available on Context7, check the library name

---

## Advanced Usage

### Pipe library creation JSON to file
```bash
just create-library "Test" "Python" "pypi" > library.json
```

### Batch upload multiple files
```bash
for file in docs/*.md; do
  just upload-doc "$file" "lib-id-123"
done
```

### Check API response format
```bash
just create-library "Test" "Python" "pypi" | jq '.context7_id'
# Output: "/pypi/test"
```

---

## See Also

- [IMPLEMENTATION.md](./IMPLEMENTATION.md) - Full implementation checklist
- [LANCEDB_SCHEMA.md](./LANCEDB_SCHEMA.md) - Database schema documentation
- [IMPLEMENTATION_STATUS.md](./IMPLEMENTATION_STATUS.md) - Current status

---

**Last Updated:** 2026-02-16
**Version:** 1.0
