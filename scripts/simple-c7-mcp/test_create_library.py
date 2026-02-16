"""Test script to create a library directly."""

from datetime import datetime

from c7_mcp.db import get_db, init_schema
from c7_mcp.services.library import create_library

# Initialize schema
print("Initializing schema...")
status = init_schema()
print(f"Schema status: {status}")

# Create a library
print("\nCreating library...")
try:
    library = create_library(
        name="FastAPI",
        language="Python",
        ecosystem="pypi",
        description="Modern Python web framework",
        short_description="Fast web framework",
        keywords=["web", "async"],
        category="web-framework",
    )
    print(f"Library created successfully!")
    print(f"ID: {library['id']}")
    print(f"Name: {library['name']}")
    print(f"Context7 ID: {library['context7_id']}")
    print(f"Language: {library['language']}")
    print(f"Ecosystem: {library['ecosystem']}")
except Exception as e:
    print(f"Error creating library: {e}")
    import traceback

    traceback.print_exc()

# List libraries
print("\nListing libraries...")
db = get_db()
libraries_table = db.open_table("libraries")
results = libraries_table.search().limit(10).to_list()
print(f"Found {len(results)} libraries")
for lib in results:
    print(f"  - {lib['name']} ({lib['ecosystem']})")
