# Justfile for Context7 MCP Testing

# Default recipe - show available commands
default:
    @just --list

# Make script executable
setup:
    chmod +x context7_test.py
    @echo "✅ Script is now executable"

# Run the forward pass test (resolve + query)
forward library="React" query="How to use useState hook":
    ./context7_test.py forward-pass "{{library}}" "{{query}}"

# Test resolve-library-id endpoint
resolve library="Next.js" query="How to create API routes":
    ./context7_test.py resolve "{{library}}" "{{query}}"

# Test query-docs endpoint
query library_id="/vercel/next.js" query="How to use middleware":
    ./context7_test.py query "{{library_id}}" "{{query}}"

# List available MCP tools
list:
    ./context7_test.py list-tools

# Run forward pass with Next.js
nextjs query="How to create API routes in Next.js 14":
    ./context7_test.py forward-pass "Next.js" "{{query}}"

# Run forward pass with React
react query="How to use useEffect hook":
    ./context7_test.py forward-pass "React" "{{query}}"

# Run forward pass with Supabase
supabase query="How to authenticate users":
    ./context7_test.py forward-pass "Supabase" "{{query}}"

# Run forward pass with MongoDB
mongodb query="How to connect to database":
    ./context7_test.py forward-pass "MongoDB" "{{query}}"

# Run forward pass with custom API key
forward-with-key library query api_key:
    ./context7_test.py forward-pass "{{library}}" "{{query}}" --api-key "{{api_key}}"

# Debug the MCP endpoint connection
debug:
    ./context7_test.py debug

# Clean up any generated files
clean:
    @echo "🧹 Cleaning up..."
    rm -f *.pyc __pycache__
    @echo "✅ Cleaned"

# Show help for the Python script
help:
    ./context7_test.py --help

# Run all test examples
test-all:
    @echo "🧪 Testing React..."
    just react "How to use useState"
    @echo "\n🧪 Testing Next.js..."
    just nextjs "How to create API routes"
    @echo "\n🧪 Testing Supabase..."
    just supabase "How to query data"
