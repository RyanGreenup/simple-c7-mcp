#!/bin/bash
set -euo pipefail

VOLUME_NAME="systemd-c7-mcp-data"
CONTAINER_UID=65532
CONTAINER_GID=65532

# Default to ./lancedb_data relative to this script's parent dir
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SOURCE_DIR="${1:-${SCRIPT_DIR}/../lancedb_data}"

# Resolve to absolute path
SOURCE_DIR="$(cd "$SOURCE_DIR" && pwd)"

if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: source directory not found: $SOURCE_DIR"
    echo "Usage: $0 [path/to/lancedb_data]"
    exit 1
fi

echo "Source: $SOURCE_DIR"
echo "Volume: $VOLUME_NAME"
echo "UID/GID: $CONTAINER_UID:$CONTAINER_GID"
echo

# Create volume if it doesn't exist
if ! podman volume exists "$VOLUME_NAME" 2>/dev/null; then
    echo "Creating volume $VOLUME_NAME..."
    podman volume create "$VOLUME_NAME"
else
    echo "Volume $VOLUME_NAME already exists."
fi

echo "Copying data into volume..."
podman run --rm \
    -v "$SOURCE_DIR:/src:ro" \
    -v "$VOLUME_NAME:/dest" \
    docker.io/library/busybox:latest \
    sh -c "cp -a /src/. /dest/ && chown -R ${CONTAINER_UID}:${CONTAINER_GID} /dest"

echo "Done. Volume contents:"
podman run --rm \
    -v "$VOLUME_NAME:/data:ro" \
    docker.io/library/busybox:latest \
    ls -la /data
