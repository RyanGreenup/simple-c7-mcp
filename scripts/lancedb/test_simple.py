#!/usr/bin/env python3
"""Simple test script for LanceDB."""

import lancedb
import pandas as pd

print("1. Creating connection...")
db = lancedb.connect("./test_db")

print("2. Creating sample data...")
data = pd.DataFrame({
    'id': [1, 2, 3],
    'text': ['hello world', 'foo bar', 'test document'],
    'vector': [[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]],
})

print("3. Creating table...")
table = db.create_table("test_table", data, mode="overwrite")

print("4. Performing search...")
results = table.search([0.1, 0.2]).limit(2).to_pandas()

print("5. Results:")
print(results)

print("\n✅ Test successful!")
