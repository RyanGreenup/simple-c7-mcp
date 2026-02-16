# Podman - Container Management Tool

## Introduction

Podman (POD MANager) is a daemonless container management tool for managing OCI containers, images, volumes, pods, and artifacts on Linux systems. Unlike Docker, Podman does not require a daemon to run containers, providing improved security and lower resource utilization at idle. It supports both rootless and rootful container execution, allowing standard users to run containers without elevated privileges while maintaining full container lifecycle management capabilities. Podman is based on libpod, a comprehensive library for container lifecycle management that provides programmatic APIs for container, pod, image, volume, and artifact operations.

Podman offers multiple interfaces for interaction: a Docker-compatible CLI that allows seamless migration from Docker workflows, a REST API providing both Docker-compatible and native Podman endpoints, and a Go client library (bindings) for programmatic container management. It runs containers locally on Linux and supports Mac/Windows systems through Podman Machine, a VM-based environment. The tool is built on industry-standard OCI specifications and integrates with various components including runc/crun for runtime execution, Netavark for networking, containers/storage for storage management, and Buildah for image building.

## APIs and Key Functions

### Container Lifecycle - List Containers

Retrieve a list of all containers in local storage with optional filtering by state, label, name, or other criteria.

```go
package main

import (
    "context"
    "fmt"
    "github.com/containers/podman/v6/pkg/bindings"
    "github.com/containers/podman/v6/pkg/bindings/containers"
)

func main() {
    ctx := context.Background()

    // Connect to Podman socket
    conn, err := bindings.NewConnection(ctx, "unix:///run/podman/podman.sock")
    if err != nil {
        panic(err)
    }

    // List all containers (running and stopped)
    opts := new(containers.ListOptions).WithAll(true).WithSize(true)
    containerList, err := containers.List(conn, opts)
    if err != nil {
        panic(err)
    }

    for _, ctr := range containerList {
        fmt.Printf("Container: %s (%s) - State: %s\n",
            ctr.Names[0], ctr.ID[:12], ctr.State)
    }
}
```

### Container Creation and Execution

Create and start a new container from an image with custom configuration including environment variables, volume mounts, and port mappings.

```go
package main

import (
    "context"
    "fmt"
    "github.com/containers/podman/v6/pkg/bindings"
    "github.com/containers/podman/v6/pkg/bindings/containers"
    "github.com/containers/podman/v6/pkg/specgen"
)

func main() {
    ctx := context.Background()
    conn, _ := bindings.NewConnection(ctx, "unix:///run/podman/podman.sock")

    // Create container specification
    s := specgen.NewSpecGenerator("alpine:latest", false)
    s.Name = "myapp"
    s.Command = []string{"sh", "-c", "echo Hello && sleep 30"}
    s.Env = map[string]string{
        "APP_ENV": "production",
        "DEBUG": "false",
    }
    s.Terminal = false

    // Create container
    createResponse, err := containers.CreateWithSpec(conn, s, nil)
    if err != nil {
        panic(err)
    }

    fmt.Printf("Created container: %s\n", createResponse.ID)

    // Start container
    err = containers.Start(conn, createResponse.ID, nil)
    if err != nil {
        panic(err)
    }

    fmt.Println("Container started successfully")

    // Wait for container to finish
    exitCode, err := containers.Wait(conn, createResponse.ID, nil)
    if err != nil {
        panic(err)
    }

    fmt.Printf("Container exited with code: %d\n", exitCode)
}
```

### Container Inspection and Logs

Inspect container metadata and retrieve stdout/stderr logs for debugging and monitoring purposes.

```go
package main

import (
    "context"
    "fmt"
    "io"
    "os"
    "github.com/containers/podman/v6/pkg/bindings"
    "github.com/containers/podman/v6/pkg/bindings/containers"
)

func main() {
    ctx := context.Background()
    conn, _ := bindings.NewConnection(ctx, "unix:///run/podman/podman.sock")

    containerID := "myapp"

    // Inspect container
    inspectData, err := containers.Inspect(conn, containerID, nil)
    if err != nil {
        panic(err)
    }

    fmt.Printf("Container Name: %s\n", inspectData.Name)
    fmt.Printf("Image: %s\n", inspectData.ImageName)
    fmt.Printf("State: %s\n", inspectData.State.Status)
    fmt.Printf("Started At: %s\n", inspectData.State.StartedAt)
    fmt.Printf("Exit Code: %d\n", inspectData.State.ExitCode)

    // Get container logs
    logOptions := new(containers.LogOptions).
        WithStdout(true).
        WithStderr(true).
        WithFollow(false)

    logChan := make(chan string)
    go func() {
        err := containers.Logs(conn, containerID, logOptions, logChan, logChan)
        if err != nil {
            fmt.Fprintf(os.Stderr, "Error getting logs: %v\n", err)
        }
    }()

    fmt.Println("\n--- Container Logs ---")
    for log := range logChan {
        fmt.Print(log)
    }
}
```

### Container Stop and Remove

Gracefully stop a running container with timeout and remove it from local storage with optional volume cleanup.

```go
package main

import (
    "context"
    "fmt"
    "time"
    "github.com/containers/podman/v6/pkg/bindings"
    "github.com/containers/podman/v6/pkg/bindings/containers"
)

func main() {
    ctx := context.Background()
    conn, _ := bindings.NewConnection(ctx, "unix:///run/podman/podman.sock")

    containerID := "myapp"

    // Stop container with 10 second timeout
    timeout := 10 * time.Second
    err := containers.Stop(conn, containerID, new(containers.StopOptions).WithTimeout(uint(timeout.Seconds())))
    if err != nil {
        fmt.Printf("Error stopping container: %v\n", err)
    } else {
        fmt.Println("Container stopped successfully")
    }

    // Remove container and its volumes
    rmOptions := new(containers.RemoveOptions).
        WithForce(true).
        WithVolumes(true)

    reports, err := containers.Remove(conn, containerID, rmOptions)
    if err != nil {
        panic(err)
    }

    for _, report := range reports {
        if report.Err != nil {
            fmt.Printf("Error removing %s: %v\n", report.Id, report.Err)
        } else {
            fmt.Printf("Removed container: %s\n", report.Id)
        }
    }
}
```

### Container Execution - Exec Command

Execute commands inside a running container with custom environment, working directory, and I/O handling.

```go
package main

import (
    "context"
    "fmt"
    "github.com/containers/podman/v6/pkg/bindings"
    "github.com/containers/podman/v6/pkg/bindings/containers"
    "github.com/containers/podman/v6/pkg/domain/entities/types"
)

func main() {
    ctx := context.Background()
    conn, _ := bindings.NewConnection(ctx, "unix:///run/podman/podman.sock")

    containerID := "myapp"

    // Create exec session
    execConfig := new(types.ExecOptions)
    execConfig.Cmd = []string{"sh", "-c", "ls -la /tmp && echo Done"}
    execConfig.AttachStdout = true
    execConfig.AttachStderr = true
    execConfig.Env = map[string]string{"EXEC_ENV": "test"}
    execConfig.WorkDir = "/tmp"

    sessionID, err := containers.ExecCreate(conn, containerID, execConfig)
    if err != nil {
        panic(err)
    }

    fmt.Printf("Created exec session: %s\n", sessionID)

    // Start exec session
    err = containers.ExecStart(conn, sessionID, nil)
    if err != nil {
        panic(err)
    }

    // Inspect exec to get exit code
    inspectData, err := containers.ExecInspect(conn, sessionID, nil)
    if err != nil {
        panic(err)
    }

    fmt.Printf("Exec exit code: %d\n", inspectData.ExitCode)
}
```

### REST API - Create Container Endpoint

Create a container using HTTP REST API with Docker-compatible interface.

```bash
# Create a container via REST API (Docker-compatible endpoint)
curl -X POST http://localhost:8080/v4.0.0/containers/create \
  -H "Content-Type: application/json" \
  -d '{
    "Image": "alpine:latest",
    "Cmd": ["echo", "Hello from REST API"],
    "Env": ["APP_NAME=myapp", "ENVIRONMENT=production"],
    "HostConfig": {
      "Memory": 536870912,
      "CpuShares": 512,
      "Binds": ["/host/path:/container/path:ro"]
    },
    "Labels": {
      "app": "myapp",
      "version": "1.0"
    }
  }'

# Response:
# {
#   "Id": "7f3c8b4d2a1e...",
#   "Warnings": []
# }

# Start the container
curl -X POST http://localhost:8080/v4.0.0/containers/7f3c8b4d2a1e/start

# Get container logs
curl -X GET "http://localhost:8080/v4.0.0/containers/7f3c8b4d2a1e/logs?stdout=true&stderr=true"

# Inspect container
curl -X GET http://localhost:8080/v4.0.0/containers/7f3c8b4d2a1e/json | jq .
```

### REST API - List and Filter Containers

Query containers with filtering options using both Docker-compatible and Podman native endpoints.

```bash
# List all containers (Docker-compatible API)
curl -X GET "http://localhost:8080/v4.0.0/containers/json?all=true&size=true"

# List containers with filters
curl -X GET "http://localhost:8080/v4.0.0/containers/json?all=true&filters=%7B%22status%22%3A%5B%22running%22%5D%7D"

# Response:
# [
#   {
#     "Id": "7f3c8b4d2a1e...",
#     "Names": ["/myapp"],
#     "Image": "alpine:latest",
#     "ImageID": "sha256:c059bfaa849c...",
#     "State": "running",
#     "Status": "Up 2 minutes",
#     "Created": 1679420400,
#     "Ports": [],
#     "Labels": {"app": "myapp"},
#     "SizeRw": 1024,
#     "SizeRootFs": 5242880
#   }
# ]

# Podman native API - list with namespace info
curl -X GET "http://localhost:8080/libpod/v4.0.0/containers/json?namespace=true"

# Stop a container
curl -X POST "http://localhost:8080/v4.0.0/containers/7f3c8b4d2a1e/stop?t=10"

# Remove container with volumes
curl -X DELETE "http://localhost:8080/v4.0.0/containers/7f3c8b4d2a1e?v=true&force=true"
```

### Pod Management - Create and Manage Pods

Create a pod (group of containers sharing network namespace) and add containers to it.

```go
package main

import (
    "context"
    "fmt"
    "github.com/containers/podman/v6/pkg/bindings"
    "github.com/containers/podman/v6/pkg/bindings/pods"
    "github.com/containers/podman/v6/pkg/bindings/containers"
    "github.com/containers/podman/v6/pkg/specgen"
)

func main() {
    ctx := context.Background()
    conn, _ := bindings.NewConnection(ctx, "unix:///run/podman/podman.sock")

    // Create pod specification
    podSpec := specgen.NewPodSpecGenerator()
    podSpec.Name = "webapp-pod"
    podSpec.Labels = map[string]string{"app": "webapp"}
    podSpec.PortMappings = []specgen.PortMapping{
        {HostPort: 8080, ContainerPort: 80, Protocol: "tcp"},
    }

    // Create pod
    createResponse, err := pods.CreatePodFromSpec(conn, podSpec, nil)
    if err != nil {
        panic(err)
    }

    fmt.Printf("Created pod: %s\n", createResponse.Id)

    // Add web server container to pod
    webSpec := specgen.NewSpecGenerator("nginx:alpine", false)
    webSpec.Name = "web"
    webSpec.Pod = createResponse.Id

    webContainer, err := containers.CreateWithSpec(conn, webSpec, nil)
    if err != nil {
        panic(err)
    }

    fmt.Printf("Added web container: %s\n", webContainer.ID)

    // Add app container to pod
    appSpec := specgen.NewSpecGenerator("alpine:latest", false)
    appSpec.Name = "app"
    appSpec.Pod = createResponse.Id
    appSpec.Command = []string{"sleep", "3600"}

    appContainer, err := containers.CreateWithSpec(conn, appSpec, nil)
    if err != nil {
        panic(err)
    }

    fmt.Printf("Added app container: %s\n", appContainer.ID)

    // Start entire pod
    err = pods.Start(conn, createResponse.Id, nil)
    if err != nil {
        panic(err)
    }

    fmt.Println("Pod started successfully")

    // Inspect pod
    podData, err := pods.Inspect(conn, createResponse.Id, nil)
    if err != nil {
        panic(err)
    }

    fmt.Printf("Pod State: %s\n", podData.State)
    fmt.Printf("Number of containers: %d\n", podData.NumContainers)
}
```

### Image Management - Pull and List Images

Pull container images from registries and list images in local storage with size and tag information.

```go
package main

import (
    "context"
    "fmt"
    "github.com/containers/podman/v6/pkg/bindings"
    "github.com/containers/podman/v6/pkg/bindings/images"
)

func main() {
    ctx := context.Background()
    conn, _ := bindings.NewConnection(ctx, "unix:///run/podman/podman.sock")

    // Pull image
    pullOptions := new(images.PullOptions).
        WithQuiet(false).
        WithAllTags(false)

    pullReports, err := images.Pull(conn, "docker.io/library/redis:alpine", pullOptions)
    if err != nil {
        panic(err)
    }

    for _, report := range pullReports {
        fmt.Printf("Pulled: %s\n", report.ID)
    }

    // List all images
    imageList, err := images.List(conn, nil)
    if err != nil {
        panic(err)
    }

    fmt.Println("\nLocal Images:")
    for _, img := range imageList {
        for _, name := range img.Names {
            fmt.Printf("  %s - Size: %d MB\n", name, img.Size/(1024*1024))
        }
    }

    // Inspect specific image
    imageData, err := images.GetImage(conn, "redis:alpine", nil)
    if err != nil {
        panic(err)
    }

    fmt.Printf("\nImage Details:\n")
    fmt.Printf("  ID: %s\n", imageData.ID)
    fmt.Printf("  Created: %s\n", imageData.Created)
    fmt.Printf("  Architecture: %s\n", imageData.Architecture)
    fmt.Printf("  OS: %s\n", imageData.Os)
}
```

### Volume Management - Create and Mount Volumes

Create named volumes for persistent container data and mount them in containers.

```bash
# Create volume via REST API
curl -X POST http://localhost:8080/v4.0.0/volumes/create \
  -H "Content-Type: application/json" \
  -d '{
    "Name": "postgres-data",
    "Driver": "local",
    "Labels": {
      "app": "database",
      "environment": "production"
    },
    "Options": {
      "type": "tmpfs",
      "device": "tmpfs"
    }
  }'

# Response:
# {
#   "Name": "postgres-data",
#   "Driver": "local",
#   "Mountpoint": "/var/lib/containers/storage/volumes/postgres-data/_data",
#   "CreatedAt": "2024-01-15T10:30:00Z",
#   "Labels": {"app": "database"}
# }

# List volumes
curl -X GET http://localhost:8080/v4.0.0/volumes | jq .

# Create container with volume mount
curl -X POST http://localhost:8080/v4.0.0/containers/create \
  -H "Content-Type: application/json" \
  -d '{
    "Image": "postgres:15",
    "Env": ["POSTGRES_PASSWORD=secret"],
    "HostConfig": {
      "Binds": ["postgres-data:/var/lib/postgresql/data"]
    }
  }'

# Inspect volume
curl -X GET http://localhost:8080/v4.0.0/volumes/postgres-data | jq .

# Remove volume
curl -X DELETE "http://localhost:8080/v4.0.0/volumes/postgres-data?force=true"
```

### CLI Usage - Container Operations

Command-line interface examples for common container management tasks using Podman CLI.

```bash
# Run a container interactively
podman run -it --name myapp \
  -e APP_ENV=production \
  -v /host/data:/data:Z \
  -p 8080:80 \
  alpine:latest sh

# Run container in detached mode
podman run -d --name web \
  --restart=always \
  -p 80:80 \
  nginx:alpine

# List running containers
podman ps

# List all containers (including stopped)
podman ps -a

# Execute command in running container
podman exec -it web sh -c "nginx -t"

# View container logs
podman logs -f web

# Monitor container resource usage
podman stats web

# Inspect container details (JSON output)
podman inspect web | jq '.[0].State'

# Stop container gracefully
podman stop -t 30 web

# Kill container immediately
podman kill web

# Remove container and volumes
podman rm -v web

# Prune all stopped containers
podman container prune -f

# Create container without starting
podman create --name app alpine:latest echo "Hello"
podman start app
podman wait app
```

### CLI Usage - Pod Operations

Manage groups of containers as cohesive units using Podman pods.

```bash
# Create a pod with port mapping
podman pod create --name webapp \
  -p 8080:80 \
  --label app=myapp

# Run containers in the pod
podman run -d --pod webapp --name web nginx:alpine
podman run -d --pod webapp --name app alpine:latest sleep infinity

# List pods
podman pod ps

# Inspect pod
podman pod inspect webapp

# Get logs from all containers in pod
podman pod logs webapp

# Stop entire pod
podman pod stop webapp

# Start entire pod
podman pod start webapp

# Restart pod
podman pod restart webapp

# Remove pod and all containers
podman pod rm -f webapp

# Generate Kubernetes YAML from pod
podman generate kube webapp > webapp.yaml

# Create pod from Kubernetes YAML
podman play kube webapp.yaml

# Remove pod created from Kubernetes YAML
podman play kube --down webapp.yaml
```

### CLI Usage - Image Operations

Build, pull, push, and manage container images using Podman CLI.

```bash
# Pull image from registry
podman pull docker.io/library/python:3.11-alpine

# Pull with authentication
podman login quay.io
podman pull quay.io/myorg/myimage:latest

# List local images
podman images

# List images with digests
podman images --digests

# Build image from Dockerfile
podman build -t myapp:1.0 .

# Build with build arguments
podman build --build-arg VERSION=1.0 \
  --build-arg BASE_IMAGE=alpine:3.18 \
  -t myapp:1.0 -f Containerfile .

# Tag image
podman tag myapp:1.0 quay.io/myorg/myapp:1.0

# Push image to registry
podman push quay.io/myorg/myapp:1.0

# Save image to tar archive
podman save -o myapp.tar myapp:1.0

# Load image from tar archive
podman load -i myapp.tar

# Remove image
podman rmi myapp:1.0

# Remove unused images
podman image prune -a

# Inspect image
podman inspect --type image alpine:latest

# View image history
podman history alpine:latest

# Search for images
podman search nginx --limit 10
```

### Artifact Management - OCI Artifacts

Manage OCI artifacts such as AI/ML models, configuration files, and other non-container data using Podman's artifact commands.

```go
package main

import (
    "context"
    "fmt"
    "os"
    "github.com/containers/podman/v6/pkg/bindings"
    "github.com/containers/podman/v6/pkg/bindings/artifacts"
)

func main() {
    ctx := context.Background()
    conn, _ := bindings.NewConnection(ctx, "unix:///run/podman/podman.sock")

    // Pull an artifact from a registry
    pullOptions := new(artifacts.PullOptions).
        WithQuiet(false).
        WithTlsVerify(true)

    pullReport, err := artifacts.Pull(conn, "quay.io/myorg/ml-model:latest", pullOptions)
    if err != nil {
        panic(err)
    }

    fmt.Printf("Pulled artifact: %s\n", pullReport.ID)

    // List all artifacts in local store
    listReport, err := artifacts.List(conn, nil)
    if err != nil {
        panic(err)
    }

    fmt.Println("\nLocal Artifacts:")
    for _, artifact := range listReport {
        fmt.Printf("  %s - Size: %d bytes\n", artifact.Repository, artifact.Size)
    }

    // Inspect specific artifact
    inspectData, err := artifacts.Inspect(conn, "quay.io/myorg/ml-model:latest", nil)
    if err != nil {
        panic(err)
    }

    fmt.Printf("\nArtifact Details:\n")
    fmt.Printf("  ID: %s\n", inspectData.ID)
    fmt.Printf("  Digest: %s\n", inspectData.Digest)
    fmt.Printf("  Created: %s\n", inspectData.CreatedAt)
    fmt.Printf("  Type: %s\n", inspectData.Type)

    // Add a local file to an artifact
    addOptions := new(artifacts.AddOptions).
        WithArtifactMIMEType("application/vnd.oci.image.manifest.v1+json").
        WithFileMIMEType("application/vnd.gguf")

    file, err := os.Open("/tmp/model.gguf")
    if err != nil {
        panic(err)
    }
    defer file.Close()

    addReport, err := artifacts.Add(conn, "quay.io/myorg/new-model:v1", "model.gguf", file, addOptions)
    if err != nil {
        panic(err)
    }

    fmt.Printf("\nAdded artifact: %s\n", addReport.ID)

    // Push artifact to registry
    pushOptions := new(artifacts.PushOptions).
        WithQuiet(false).
        WithTlsVerify(true)

    pushReport, err := artifacts.Push(conn, "quay.io/myorg/new-model:v1", pushOptions)
    if err != nil {
        panic(err)
    }

    fmt.Printf("Pushed artifact to: %s\n", pushReport.ID)
}
```

### REST API - Artifact Operations

Manage OCI artifacts through REST API endpoints for pulling, pushing, listing, and inspecting artifacts.

```bash
# Pull an artifact from registry
curl -X POST http://localhost:8080/libpod/v4.0.0/artifacts/pull \
  -H "Content-Type: application/json" \
  -d '{
    "name": "quay.io/myorg/ml-model:latest",
    "quiet": false,
    "tlsVerify": true
  }'

# Response:
# {
#   "ID": "sha256:abc123...",
#   "Images": ["quay.io/myorg/ml-model:latest"]
# }

# List all artifacts
curl -X GET http://localhost:8080/libpod/v4.0.0/artifacts/json

# Response:
# [
#   {
#     "Repository": "quay.io/myorg/ml-model",
#     "Tag": "latest",
#     "Digest": "sha256:abc123...",
#     "CreatedAt": "2024-01-15T10:30:00Z",
#     "Size": 1073741824
#   }
# ]

# Inspect specific artifact
curl -X GET http://localhost:8080/libpod/v4.0.0/artifacts/quay.io%2Fmyorg%2Fml-model:latest/json

# Response:
# {
#   "ID": "sha256:abc123...",
#   "Digest": "sha256:abc123...",
#   "CreatedAt": "2024-01-15T10:30:00Z",
#   "Type": "application/vnd.oci.image.manifest.v1+json",
#   "Layers": [...]
# }

# Add artifact from file (multipart upload)
curl -X POST http://localhost:8080/libpod/v4.0.0/artifacts/add \
  -F "name=quay.io/myorg/new-model:v1" \
  -F "fileName=model.gguf" \
  -F "file=@/tmp/model.gguf" \
  -F "artifactMIMEType=application/vnd.oci.image.manifest.v1+json" \
  -F "fileMIMEType=application/vnd.gguf"

# Push artifact to registry
curl -X POST "http://localhost:8080/libpod/v4.0.0/artifacts/quay.io%2Fmyorg%2Fml-model:latest/push?tlsVerify=true"

# Extract artifact contents
curl -X GET "http://localhost:8080/libpod/v4.0.0/artifacts/quay.io%2Fmyorg%2Fml-model:latest/extract" \
  --output artifact-contents.tar

# Extract specific blob by title
curl -X GET "http://localhost:8080/libpod/v4.0.0/artifacts/quay.io%2Fmyorg%2Fml-model:latest/extract?title=model.gguf" \
  --output model.gguf

# Remove artifact
curl -X DELETE http://localhost:8080/libpod/v4.0.0/artifacts/quay.io%2Fmyorg%2Fml-model:latest

# Remove multiple artifacts
curl -X DELETE "http://localhost:8080/libpod/v4.0.0/artifacts/remove" \
  -H "Content-Type: application/json" \
  -d '{
    "artifacts": ["model1:latest", "model2:v1"],
    "ignore": false
  }'
```

### CLI Usage - Artifact Operations

Manage OCI artifacts for storing and distributing non-container data such as AI/ML models, WASM modules, and configuration files.

```bash
# Add a single file to create an artifact
podman artifact add quay.io/myorg/ml-model:latest /tmp/model.gguf

# Add artifact with specific type and file type
podman artifact add \
  --type application/vnd.ai.model \
  --file-type application/vnd.gguf \
  quay.io/myorg/ml-model:v2 /home/user/model.gguf

# Add multiple files to an artifact with annotations
podman artifact add \
  --annotation org.opencontainers.image.title=config \
  quay.io/myorg/app-config:latest \
  config.yaml settings.json

# Append files to an existing artifact
podman artifact add --append \
  quay.io/myorg/ml-model:latest \
  additional-data.bin

# Replace an existing artifact
podman artifact add --replace \
  quay.io/myorg/ml-model:latest \
  updated-model.gguf

# Pull an artifact from a registry
podman artifact pull quay.io/myorg/ml-model:latest

# List all local artifacts
podman artifact ls

# List artifacts with custom format
podman artifact ls --format "{{.Repository}}:{{.Tag}} - {{.Size}}"

# Inspect artifact details
podman artifact inspect quay.io/myorg/ml-model:latest

# Extract artifact contents to local filesystem
podman artifact extract quay.io/myorg/ml-model:latest /tmp/extracted/

# Extract specific blob by title
podman artifact extract --title model.gguf \
  quay.io/myorg/ml-model:latest /tmp/model.gguf

# Extract specific blob by digest
podman artifact extract --digest sha256:abc123... \
  quay.io/myorg/ml-model:latest /tmp/output

# Push artifact to registry
podman artifact push quay.io/myorg/ml-model:latest

# Remove specific artifact
podman artifact rm quay.io/myorg/ml-model:latest

# Remove all artifacts
podman artifact rm --all

# Remove artifacts with ignore flag for non-existent ones
podman artifact rm --ignore model1:latest model2:v1

# Mount artifact into container as file
podman run --mount type=artifact,src=quay.io/myorg/config:v1,dst=/app/config.yaml \
  alpine:latest cat /app/config.yaml

# Mount artifact into container as directory
podman run --mount type=artifact,src=quay.io/myorg/ml-model:latest,dst=/models \
  alpine:latest ls -la /models
```

### Rootless Container Execution

Run containers without root privileges using user namespaces and rootless mode.

```bash
# Check rootless setup
podman info | grep rootless

# Run rootless container
podman run --rm alpine:latest id
# Output: uid=0(root) gid=0(root) groups=0(root)
# This is root inside container, but your user outside

# Port binding in rootless mode (use ports >= 1024 or configure)
podman run -d -p 8080:80 nginx:alpine

# Mount host directory (automatic UID/GID mapping)
podman run -v ~/data:/data:Z alpine:latest ls -la /data

# Use pod in rootless mode
podman pod create --name test -p 3000:3000
podman run -d --pod test nginx:alpine

# Check user namespace mapping
podman unshare cat /proc/self/uid_map

# Run with specific UID/GID mapping
podman run --uidmap 0:1000:1000 --gidmap 0:1000:1000 alpine:latest id

# Access container from host as root (rootless)
podman unshare
# Now in user namespace - can access container storage
```

### System Management and Events

Monitor system information, events, and perform system-level operations.

```go
package main

import (
    "context"
    "fmt"
    "github.com/containers/podman/v6/pkg/bindings"
    "github.com/containers/podman/v6/pkg/bindings/system"
)

func main() {
    ctx := context.Background()
    conn, _ := bindings.NewConnection(ctx, "unix:///run/podman/podman.sock")

    // Get system information
    info, err := system.Info(conn, nil)
    if err != nil {
        panic(err)
    }

    fmt.Printf("Podman Version: %s\n", info.Version.Version)
    fmt.Printf("OS: %s\n", info.Host.OS)
    fmt.Printf("Architecture: %s\n", info.Host.Arch)
    fmt.Printf("CPUs: %d\n", info.Host.CPUs)
    fmt.Printf("Memory: %d MB\n", info.Host.MemTotal/(1024*1024))
    fmt.Printf("Kernel: %s\n", info.Host.Kernel)
    fmt.Printf("Rootless: %t\n", info.Host.Security.Rootless)

    // Monitor events
    eventChan := make(chan system.Event)
    errorChan := make(chan error)

    go func() {
        err := system.Events(conn, eventChan, errorChan, nil)
        if err != nil {
            errorChan <- err
        }
    }()

    fmt.Println("\nMonitoring events (Ctrl+C to exit)...")

    for {
        select {
        case event := <-eventChan:
            fmt.Printf("[%s] %s %s: %s\n",
                event.Time, event.Type, event.Action, event.Actor.ID[:12])
        case err := <-errorChan:
            fmt.Printf("Error: %v\n", err)
            return
        }
    }
}
```

### Health Checks and Container Monitoring

Define and monitor container health checks for automated restart and service management.

```bash
# Run container with health check
podman run -d --name web \
  --health-cmd "curl -f http://localhost/ || exit 1" \
  --health-interval 30s \
  --health-timeout 3s \
  --health-retries 3 \
  --health-start-period 5s \
  nginx:alpine

# Check health status
podman healthcheck run web
# Output: healthy

# Inspect health check configuration
podman inspect web | jq '.[0].Config.Healthcheck'

# View health check logs
podman inspect web | jq '.[0].State.Health'

# Create container from image with built-in healthcheck (Dockerfile)
# Dockerfile example:
# HEALTHCHECK --interval=30s --timeout=3s \
#   CMD curl -f http://localhost/ || exit 1

# Prune unhealthy containers
podman ps -a --filter health=unhealthy
```

## Use Cases and Integration

Podman serves as a comprehensive container management solution for development, testing, and production environments. Its primary use cases include local development workflows where developers need to run containerized applications without Docker Desktop requirements, especially valuable on Linux workstations and in rootless environments. CI/CD pipelines benefit from Podman's daemonless architecture, allowing containers to be built and run within isolated CI jobs without requiring privileged Docker daemon access. System administrators use Podman for production deployments with systemd integration through Podman's generate systemd command, enabling containers to run as native systemd services with automatic restarts and dependency management. The artifact management feature enables teams to store and distribute OCI artifacts such as AI/ML models, WASM modules, configuration files, and other non-container data using the same registry infrastructure as container images.

Integration patterns include REST API consumption for programmatic container management from web applications, microservices orchestration where the Go bindings library enables custom automation tools, and Kubernetes YAML compatibility through podman play kube for local testing of Kubernetes manifests. The Docker-compatible socket (/run/podman/podman.sock) allows existing Docker-based tools to work with Podman transparently by setting DOCKER_HOST environment variable. Podman Machine extends container capabilities to macOS and Windows environments through automated VM provisioning, while the project's OCI compliance ensures images and containers remain portable across different container runtimes. Security-conscious deployments leverage Podman's rootless mode combined with SELinux/AppArmor integration, user namespace isolation, and capability dropping for defense-in-depth strategies without sacrificing container functionality or performance. OCI artifact support enables ML/AI workflows where models can be versioned, distributed through registries, and mounted directly into containers for inference workloads, providing a unified approach to managing both application containers and their associated data assets.
