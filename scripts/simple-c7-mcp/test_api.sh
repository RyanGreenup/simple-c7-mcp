#!/bin/bash
# Test script for library creation API

echo "Creating FastAPI library..."
curl -s -X POST 'http://127.0.0.1:8000/api/v1/libraries' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "FastAPI",
    "language": "Python",
    "ecosystem": "pypi",
    "description": "FastAPI is a modern, fast web framework for building APIs with Python 3.7+",
    "short_description": "Modern Python web framework",
    "keywords": ["web", "framework", "async", "api"],
    "category": "web-framework",
    "homepage_url": "https://fastapi.tiangolo.com",
    "repository_url": "https://github.com/tiangolo/fastapi",
    "author": "Sebastián Ramírez",
    "license": "MIT"
  }' | python3 -m json.tool

echo -e "\n\nCreating React library..."
curl -s -X POST 'http://127.0.0.1:8000/api/v1/libraries' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "React",
    "language": "JavaScript",
    "ecosystem": "npm",
    "description": "A JavaScript library for building user interfaces",
    "short_description": "JavaScript library for UIs",
    "keywords": ["ui", "components", "jsx", "frontend"],
    "category": "ui-library"
  }' | python3 -m json.tool

echo -e "\n\nListing all libraries..."
curl -s 'http://127.0.0.1:8000/api/v1/libraries' | python3 -m json.tool
