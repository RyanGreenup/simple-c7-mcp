# go-github

go-github is a Go client library for accessing the GitHub REST API v3. It provides comprehensive coverage of GitHub's API including repositories, issues, pull requests, users, organizations, actions, gists, and webhooks. The library follows Go's version support policy and uses semantic versioning for releases.

The library is designed around a central `Client` struct that provides access to various GitHub services. Each service corresponds to a section of the GitHub API documentation and offers methods for interacting with those endpoints. Authentication is handled through OAuth tokens or GitHub App installations, and the library provides built-in support for pagination, rate limiting, conditional requests, and webhook validation.

## Installation

```bash
go get github.com/google/go-github/v82
```

```go
import "github.com/google/go-github/v82/github"
```

## Creating a Client

The GitHub client is the entry point for all API interactions. It can be created with or without authentication depending on your needs.

```go
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "github.com/google/go-github/v82/github"
)

func main() {
    // Unauthenticated client (limited rate)
    client := github.NewClient(nil)

    // Authenticated client with Personal Access Token
    token := os.Getenv("GITHUB_TOKEN")
    authenticatedClient := github.NewClient(nil).WithAuthToken(token)

    // Get authenticated user info
    user, resp, err := authenticatedClient.Users.Get(context.Background(), "")
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Logged in as: %s\n", user.GetLogin())
    fmt.Printf("Rate limit remaining: %d/%d\n", resp.Rate.Remaining, resp.Rate.Limit)
    // Output: Logged in as: yourusername
    // Output: Rate limit remaining: 4999/5000
}
```

## Users Service - Get User Information

The Users service provides methods for retrieving and managing user information. Pass an empty string to get the authenticated user, or a username to get a specific user.

```go
package main

import (
    "context"
    "fmt"
    "log"

    "github.com/google/go-github/v82/github"
)

func main() {
    client := github.NewClient(nil)
    ctx := context.Background()

    // Get a specific user
    user, _, err := client.Users.Get(ctx, "octocat")
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("User: %s\n", user.GetLogin())
    fmt.Printf("Name: %s\n", user.GetName())
    fmt.Printf("Bio: %s\n", user.GetBio())
    fmt.Printf("Public Repos: %d\n", user.GetPublicRepos())
    fmt.Printf("Followers: %d\n", user.GetFollowers())
    fmt.Printf("Following: %d\n", user.GetFollowing())
    // Output: User: octocat
    // Output: Name: The Octocat
    // Output: Bio: @github mascot
    // Output: Public Repos: 8
    // Output: Followers: 9500
    // Output: Following: 9
}
```

## Organizations Service - List Organizations

The Organizations service handles organization-related operations including listing organization memberships, managing teams, and organization settings.

```go
package main

import (
    "context"
    "fmt"
    "log"

    "github.com/google/go-github/v82/github"
)

func main() {
    client := github.NewClient(nil)
    ctx := context.Background()

    // List public organizations for a user
    orgs, _, err := client.Organizations.List(ctx, "google", nil)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Organizations for user 'google':\n")
    for i, org := range orgs {
        fmt.Printf("%d. %s - %s\n", i+1, org.GetLogin(), org.GetDescription())
    }

    // Get specific organization details
    org, _, err := client.Organizations.Get(ctx, "github")
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("\nOrganization: %s\n", org.GetLogin())
    fmt.Printf("Name: %s\n", org.GetName())
    fmt.Printf("Public Repos: %d\n", org.GetPublicRepos())
    fmt.Printf("Followers: %d\n", org.GetFollowers())
}
```

## Repositories Service - List and Create Repositories

The Repositories service provides comprehensive repository management including listing, creating, updating, and deleting repositories.

```go
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "github.com/google/go-github/v82/github"
)

func main() {
    token := os.Getenv("GITHUB_TOKEN")
    client := github.NewClient(nil).WithAuthToken(token)
    ctx := context.Background()

    // List repositories for an organization with options
    opts := &github.RepositoryListByOrgOptions{
        Type:        "public",
        ListOptions: github.ListOptions{PerPage: 10},
    }
    repos, _, err := client.Repositories.ListByOrg(ctx, "github", opts)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println("Public repos for 'github' org:")
    for _, repo := range repos {
        fmt.Printf("- %s: %s (Stars: %d)\n",
            repo.GetName(),
            repo.GetDescription(),
            repo.GetStargazersCount())
    }

    // Create a new repository
    newRepo := &github.Repository{
        Name:        github.Ptr("my-new-repo"),
        Description: github.Ptr("A test repository created via go-github"),
        Private:     github.Ptr(true),
        AutoInit:    github.Ptr(true),
    }

    repo, _, err := client.Repositories.Create(ctx, "", newRepo) // empty string = authenticated user
    if err != nil {
        log.Printf("Could not create repo: %v\n", err)
    } else {
        fmt.Printf("\nCreated repository: %s\n", repo.GetHTMLURL())
    }
}
```

## Repositories Service - Get Repository Contents

Retrieve file and directory contents from a repository, including README files and arbitrary paths.

```go
package main

import (
    "context"
    "fmt"
    "log"

    "github.com/google/go-github/v82/github"
)

func main() {
    client := github.NewClient(nil)
    ctx := context.Background()

    // Get README for a repository
    readme, _, err := client.Repositories.GetReadme(ctx, "google", "go-github", nil)
    if err != nil {
        log.Fatal(err)
    }

    content, err := readme.GetContent()
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("README.md content (first 500 chars):\n%s...\n", content[:500])

    // Get contents of a specific file
    fileContent, _, _, err := client.Repositories.GetContents(
        ctx,
        "google",
        "go-github",
        "go.mod",
        &github.RepositoryContentGetOptions{Ref: "master"},
    )
    if err != nil {
        log.Fatal(err)
    }

    goModContent, _ := fileContent.GetContent()
    fmt.Printf("\ngo.mod content:\n%s\n", goModContent)
}
```

## Repositories Service - Create and Update Files

Create or update files in a repository using the Contents API. This is useful for programmatic commits.

```go
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "github.com/google/go-github/v82/github"
)

func main() {
    token := os.Getenv("GITHUB_TOKEN")
    client := github.NewClient(nil).WithAuthToken(token)
    ctx := context.Background()

    owner := "your-username"
    repo := "your-repo"
    path := "docs/example.md"
    content := []byte("# Example\n\nThis file was created via the GitHub API.")

    // Create a new file
    opts := &github.RepositoryContentFileOptions{
        Message: github.Ptr("Add example documentation"),
        Content: content,
        Branch:  github.Ptr("main"),
        Author: &github.CommitAuthor{
            Name:  github.Ptr("Bot"),
            Email: github.Ptr("bot@example.com"),
        },
    }

    response, _, err := client.Repositories.CreateFile(ctx, owner, repo, path, opts)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("File created: %s\n", response.Content.GetHTMLURL())
    fmt.Printf("Commit SHA: %s\n", response.GetSHA())
    fmt.Printf("Commit message: %s\n", response.Commit.GetMessage())
}
```

## Issues Service - List and Create Issues

The Issues service handles issue tracking operations including listing, creating, updating, and commenting on issues.

```go
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "github.com/google/go-github/v82/github"
)

func main() {
    token := os.Getenv("GITHUB_TOKEN")
    client := github.NewClient(nil).WithAuthToken(token)
    ctx := context.Background()

    // List open issues for a repository
    opts := &github.IssueListByRepoOptions{
        State:       "open",
        Sort:        "created",
        Direction:   "desc",
        ListOptions: github.ListOptions{PerPage: 5},
    }

    issues, _, err := client.Issues.ListByRepo(ctx, "golang", "go", opts)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println("Recent open issues in golang/go:")
    for _, issue := range issues {
        if !issue.IsPullRequest() { // Filter out PRs
            fmt.Printf("#%d: %s\n", issue.GetNumber(), issue.GetTitle())
            fmt.Printf("    Author: %s, Comments: %d\n",
                issue.User.GetLogin(),
                issue.GetComments())
        }
    }

    // Create a new issue (requires write access)
    newIssue := &github.IssueRequest{
        Title:     github.Ptr("Bug: Something is broken"),
        Body:      github.Ptr("## Description\n\nDetailed bug description here.\n\n## Steps to Reproduce\n1. Step 1\n2. Step 2"),
        Labels:    &[]string{"bug", "help wanted"},
        Assignees: &[]string{"your-username"},
    }

    issue, _, err := client.Issues.Create(ctx, "owner", "repo", newIssue)
    if err != nil {
        log.Printf("Could not create issue: %v\n", err)
    } else {
        fmt.Printf("\nCreated issue #%d: %s\n", issue.GetNumber(), issue.GetHTMLURL())
    }
}
```

## Pull Requests Service - List and Create PRs

The Pull Requests service manages pull request operations including creation, listing, reviewing, and merging.

```go
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "github.com/google/go-github/v82/github"
)

func main() {
    token := os.Getenv("GITHUB_TOKEN")
    client := github.NewClient(nil).WithAuthToken(token)
    ctx := context.Background()

    // List open pull requests
    opts := &github.PullRequestListOptions{
        State:       "open",
        Sort:        "created",
        Direction:   "desc",
        ListOptions: github.ListOptions{PerPage: 10},
    }

    prs, _, err := client.PullRequests.List(ctx, "kubernetes", "kubernetes", opts)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println("Recent open PRs in kubernetes/kubernetes:")
    for _, pr := range prs {
        fmt.Printf("#%d: %s\n", pr.GetNumber(), pr.GetTitle())
        fmt.Printf("    Author: %s, Base: %s <- Head: %s\n",
            pr.User.GetLogin(),
            pr.Base.GetRef(),
            pr.Head.GetRef())
    }

    // Create a pull request
    newPR := &github.NewPullRequest{
        Title:               github.Ptr("Add new feature"),
        Head:                github.Ptr("feature-branch"),
        Base:                github.Ptr("main"),
        Body:                github.Ptr("## Summary\nThis PR adds a new feature.\n\n## Changes\n- Added feature X\n- Updated tests"),
        MaintainerCanModify: github.Ptr(true),
    }

    pr, _, err := client.PullRequests.Create(ctx, "owner", "repo", newPR)
    if err != nil {
        log.Printf("Could not create PR: %v\n", err)
    } else {
        fmt.Printf("\nCreated PR #%d: %s\n", pr.GetNumber(), pr.GetHTMLURL())
    }
}
```

## Search Service - Search Repositories, Code, and Issues

The Search service provides access to GitHub's powerful search functionality across repositories, code, issues, and users.

```go
package main

import (
    "context"
    "fmt"
    "log"

    "github.com/google/go-github/v82/github"
)

func main() {
    client := github.NewClient(nil)
    ctx := context.Background()

    // Search repositories
    repoOpts := &github.SearchOptions{
        Sort:  "stars",
        Order: "desc",
        ListOptions: github.ListOptions{PerPage: 5},
    }

    repoResults, _, err := client.Search.Repositories(ctx, "language:go stars:>10000", repoOpts)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Top Go repositories (found %d total):\n", repoResults.GetTotal())
    for _, repo := range repoResults.Repositories {
        fmt.Printf("- %s: %s (Stars: %d)\n",
            repo.GetFullName(),
            repo.GetDescription(),
            repo.GetStargazersCount())
    }

    // Search issues
    issueOpts := &github.SearchOptions{
        Sort:  "created",
        Order: "desc",
        ListOptions: github.ListOptions{PerPage: 5},
    }

    issueResults, _, err := client.Search.Issues(ctx, "is:issue is:open label:bug language:go", issueOpts)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("\nRecent open bug issues in Go repos (found %d total):\n", issueResults.GetTotal())
    for _, issue := range issueResults.Issues {
        fmt.Printf("- %s#%d: %s\n",
            issue.GetRepositoryURL(),
            issue.GetNumber(),
            issue.GetTitle())
    }
}
```

## Actions Service - Manage Workflows and Secrets

The Actions service provides access to GitHub Actions including workflows, workflow runs, artifacts, and secrets management.

```go
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "github.com/google/go-github/v82/github"
)

func main() {
    token := os.Getenv("GITHUB_TOKEN")
    client := github.NewClient(nil).WithAuthToken(token)
    ctx := context.Background()

    owner := "owner"
    repo := "repo"

    // List workflows
    workflows, _, err := client.Actions.ListWorkflows(ctx, owner, repo, nil)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println("Repository workflows:")
    for _, wf := range workflows.Workflows {
        fmt.Printf("- %s (ID: %d, State: %s)\n",
            wf.GetName(),
            wf.GetID(),
            wf.GetState())
    }

    // Trigger a workflow dispatch
    event := github.CreateWorkflowDispatchEventRequest{
        Ref: "main",
        Inputs: map[string]any{
            "environment": "staging",
            "debug":       "true",
        },
    }

    _, err = client.Actions.CreateWorkflowDispatchEventByFileName(
        ctx, owner, repo, "ci.yml", event)
    if err != nil {
        log.Printf("Could not dispatch workflow: %v\n", err)
    } else {
        fmt.Println("\nWorkflow dispatch triggered successfully")
    }

    // List repository secrets (names only, values are encrypted)
    secrets, _, err := client.Actions.ListRepoSecrets(ctx, owner, repo, nil)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println("\nRepository secrets:")
    for _, secret := range secrets.Secrets {
        fmt.Printf("- %s (Updated: %s)\n", secret.Name, secret.UpdatedAt)
    }
}
```

## Actions Service - Create Repository Secrets

Create encrypted secrets for GitHub Actions using the repository's public key.

```go
package main

import (
    "context"
    "crypto/rand"
    "encoding/base64"
    "fmt"
    "log"
    "os"

    "github.com/google/go-github/v82/github"
    "golang.org/x/crypto/nacl/box"
)

func main() {
    token := os.Getenv("GITHUB_TOKEN")
    client := github.NewClient(nil).WithAuthToken(token)
    ctx := context.Background()

    owner := "owner"
    repo := "repo"
    secretName := "MY_SECRET"
    secretValue := "super-secret-value"

    // Get the repository's public key
    publicKey, _, err := client.Actions.GetRepoPublicKey(ctx, owner, repo)
    if err != nil {
        log.Fatal(err)
    }

    // Decode the public key
    decodedPublicKey, err := base64.StdEncoding.DecodeString(publicKey.GetKey())
    if err != nil {
        log.Fatal(err)
    }

    // Encrypt the secret value
    var boxKey [32]byte
    copy(boxKey[:], decodedPublicKey)

    encryptedBytes, err := box.SealAnonymous(nil, []byte(secretValue), &boxKey, rand.Reader)
    if err != nil {
        log.Fatal(err)
    }

    encryptedValue := base64.StdEncoding.EncodeToString(encryptedBytes)

    // Create or update the secret
    encryptedSecret := &github.EncryptedSecret{
        Name:           secretName,
        KeyID:          publicKey.GetKeyID(),
        EncryptedValue: encryptedValue,
    }

    _, err = client.Actions.CreateOrUpdateRepoSecret(ctx, owner, repo, encryptedSecret)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Secret '%s' created/updated successfully\n", secretName)
}
```

## Gists Service - Create and Manage Gists

The Gists service handles GitHub Gist operations including creating, listing, starring, and forking gists.

```go
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "github.com/google/go-github/v82/github"
)

func main() {
    token := os.Getenv("GITHUB_TOKEN")
    client := github.NewClient(nil).WithAuthToken(token)
    ctx := context.Background()

    // List gists for a user
    gists, _, err := client.Gists.List(ctx, "defunkt", nil)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println("Gists for user 'defunkt':")
    for _, gist := range gists {
        fmt.Printf("- %s: %s\n", gist.GetID(), gist.GetDescription())
        for filename := range gist.Files {
            fmt.Printf("    File: %s\n", filename)
        }
    }

    // Create a new gist
    newGist := &github.Gist{
        Description: github.Ptr("Example gist created via go-github"),
        Public:      github.Ptr(false),
        Files: map[github.GistFilename]github.GistFile{
            "hello.go": {
                Content: github.Ptr(`package main

import "fmt"

func main() {
    fmt.Println("Hello from go-github!")
}
`),
            },
            "README.md": {
                Content: github.Ptr("# Example Gist\n\nThis gist was created programmatically."),
            },
        },
    }

    gist, _, err := client.Gists.Create(ctx, newGist)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("\nCreated gist: %s\n", gist.GetHTMLURL())
}
```

## Pagination - Iterate Through All Results

go-github supports pagination for all list operations. Use the iterator pattern with Go 1.23+ or manual pagination for earlier versions.

```go
package main

import (
    "context"
    "fmt"
    "log"

    "github.com/google/go-github/v82/github"
)

func main() {
    client := github.NewClient(nil)
    ctx := context.Background()

    // Method 1: Manual pagination
    opts := &github.RepositoryListByOrgOptions{
        ListOptions: github.ListOptions{PerPage: 30},
    }

    var allRepos []*github.Repository
    for {
        repos, resp, err := client.Repositories.ListByOrg(ctx, "github", opts)
        if err != nil {
            log.Fatal(err)
        }
        allRepos = append(allRepos, repos...)

        if resp.NextPage == 0 {
            break
        }
        opts.Page = resp.NextPage
    }

    fmt.Printf("Total repos (manual pagination): %d\n", len(allRepos))

    // Method 2: Using iterators (Go 1.23+)
    allRepos = nil
    iter := client.Repositories.ListByOrgIter(ctx, "github", nil)
    for repo, err := range iter {
        if err != nil {
            log.Fatal(err)
        }
        allRepos = append(allRepos, repo)
    }

    fmt.Printf("Total repos (iterator): %d\n", len(allRepos))
}
```

## Rate Limiting - Handle API Limits

go-github provides built-in rate limit handling and error detection for both primary and secondary rate limits.

```go
package main

import (
    "context"
    "errors"
    "fmt"
    "log"
    "os"
    "time"

    "github.com/google/go-github/v82/github"
)

func main() {
    token := os.Getenv("GITHUB_TOKEN")
    client := github.NewClient(nil).WithAuthToken(token)
    ctx := context.Background()

    // Check current rate limit status
    limits, _, err := client.RateLimits(ctx)
    if err != nil {
        log.Fatal(err)
    }

    core := limits.Core
    fmt.Printf("Core Rate Limit:\n")
    fmt.Printf("  Limit: %d\n", core.Limit)
    fmt.Printf("  Remaining: %d\n", core.Remaining)
    fmt.Printf("  Resets at: %s\n", core.Reset.Time.Format(time.RFC3339))

    search := limits.Search
    fmt.Printf("\nSearch Rate Limit:\n")
    fmt.Printf("  Limit: %d\n", search.Limit)
    fmt.Printf("  Remaining: %d\n", search.Remaining)

    // Making requests with rate limit error handling
    repos, _, err := client.Repositories.List(ctx, "", nil)

    // Check for primary rate limit error
    var rateLimitErr *github.RateLimitError
    if errors.As(err, &rateLimitErr) {
        fmt.Printf("\nHit primary rate limit! Reset at: %s\n",
            rateLimitErr.Rate.Reset.Time.Format(time.RFC3339))
        fmt.Printf("Used %d of %d requests\n", rateLimitErr.Rate.Used, rateLimitErr.Rate.Limit)
        return
    }

    // Check for secondary (abuse) rate limit error
    var abuseErr *github.AbuseRateLimitError
    if errors.As(err, &abuseErr) {
        fmt.Printf("\nHit secondary rate limit! Retry after: %v\n", abuseErr.RetryAfter)
        return
    }

    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("\nFetched %d repositories\n", len(repos))
}
```

## Webhooks - Validate and Parse Webhook Payloads

go-github provides utilities for validating webhook signatures and parsing webhook payloads into typed event structs.

```go
package main

import (
    "fmt"
    "log"
    "net/http"

    "github.com/google/go-github/v82/github"
)

func main() {
    webhookSecret := []byte("your-webhook-secret")

    http.HandleFunc("/webhook", func(w http.ResponseWriter, r *http.Request) {
        // Validate the webhook signature
        payload, err := github.ValidatePayload(r, webhookSecret)
        if err != nil {
            http.Error(w, "Invalid signature", http.StatusUnauthorized)
            return
        }

        // Parse the webhook event
        event, err := github.ParseWebHook(github.WebHookType(r), payload)
        if err != nil {
            http.Error(w, "Could not parse webhook", http.StatusBadRequest)
            return
        }

        // Handle different event types
        switch e := event.(type) {
        case *github.PushEvent:
            fmt.Printf("Push to %s by %s\n",
                e.GetRepo().GetFullName(),
                e.GetSender().GetLogin())
            fmt.Printf("Commits: %d\n", len(e.Commits))

        case *github.PullRequestEvent:
            fmt.Printf("PR %s: #%d %s\n",
                e.GetAction(),
                e.GetPullRequest().GetNumber(),
                e.GetPullRequest().GetTitle())

        case *github.IssuesEvent:
            fmt.Printf("Issue %s: #%d %s\n",
                e.GetAction(),
                e.GetIssue().GetNumber(),
                e.GetIssue().GetTitle())

        case *github.IssueCommentEvent:
            fmt.Printf("Comment on issue #%d by %s\n",
                e.GetIssue().GetNumber(),
                e.GetComment().GetUser().GetLogin())

        case *github.CheckRunEvent:
            fmt.Printf("Check run %s: %s\n",
                e.GetAction(),
                e.GetCheckRun().GetName())

        default:
            fmt.Printf("Unhandled event type: %s\n", github.WebHookType(r))
        }

        w.WriteHeader(http.StatusOK)
    })

    log.Println("Webhook server starting on :8080")
    log.Fatal(http.ListenAndServe(":8080", nil))
}
```

## GitHub App Authentication

Authenticate as a GitHub App using installation tokens. This requires an external library like ghinstallation or go-githubauth.

```go
package main

import (
    "context"
    "fmt"
    "log"
    "net/http"

    "github.com/bradleyfalzon/ghinstallation/v2"
    "github.com/google/go-github/v82/github"
)

func main() {
    // Create a transport using GitHub App credentials
    // Parameters: http.Transport, App ID, Installation ID, private key file
    itr, err := ghinstallation.NewKeyFromFile(
        http.DefaultTransport,
        12345,                       // App ID
        67890,                       // Installation ID
        "path/to/private-key.pem",   // Private key file
    )
    if err != nil {
        log.Fatal(err)
    }

    // Create client with the installation transport
    client := github.NewClient(&http.Client{Transport: itr})
    ctx := context.Background()

    // Now you can make API calls as the GitHub App installation
    repos, _, err := client.Repositories.ListByOrg(ctx, "your-org", nil)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Repositories accessible by this installation:\n")
    for _, repo := range repos {
        fmt.Printf("- %s\n", repo.GetFullName())
    }

    // For JWT authentication (some endpoints like listing app installations)
    // Use AppsTransport instead:
    // jwtTransport, _ := ghinstallation.NewAppsTransportKeyFromFile(
    //     http.DefaultTransport, 12345, "private-key.pem")
}
```

## Git Service - Low-Level Git Operations

The Git service provides low-level git operations for creating commits, trees, refs, and blobs programmatically.

```go
package main

import (
    "context"
    "fmt"
    "log"
    "os"
    "time"

    "github.com/google/go-github/v82/github"
)

func main() {
    token := os.Getenv("GITHUB_TOKEN")
    client := github.NewClient(nil).WithAuthToken(token)
    ctx := context.Background()

    owner := "owner"
    repo := "repo"

    // Get the reference for main branch
    ref, _, err := client.Git.GetRef(ctx, owner, repo, "refs/heads/main")
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Current main SHA: %s\n", ref.Object.GetSHA())

    // Create a new blob (file content)
    blob, _, err := client.Git.CreateBlob(ctx, owner, repo, &github.Blob{
        Content:  github.Ptr("# New File\n\nCreated via Git API"),
        Encoding: github.Ptr("utf-8"),
    })
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Created blob SHA: %s\n", blob.GetSHA())

    // Create a tree with the new file
    tree, _, err := client.Git.CreateTree(ctx, owner, repo, *ref.Object.SHA, []*github.TreeEntry{
        {
            Path: github.Ptr("docs/new-file.md"),
            Mode: github.Ptr("100644"),
            Type: github.Ptr("blob"),
            SHA:  blob.SHA,
        },
    })
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Created tree SHA: %s\n", tree.GetSHA())

    // Create a commit
    date := time.Now()
    commit, _, err := client.Git.CreateCommit(ctx, owner, repo, github.Commit{
        Message: github.Ptr("Add new documentation file"),
        Tree:    tree,
        Parents: []*github.Commit{{SHA: ref.Object.SHA}},
        Author: &github.CommitAuthor{
            Name:  github.Ptr("Bot"),
            Email: github.Ptr("bot@example.com"),
            Date:  &github.Timestamp{Time: date},
        },
    }, nil)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Created commit SHA: %s\n", commit.GetSHA())

    // Update the branch reference
    ref.Object.SHA = commit.SHA
    _, _, err = client.Git.UpdateRef(ctx, owner, repo, "refs/heads/main", github.UpdateRef{
        SHA:   *commit.SHA,
        Force: github.Ptr(false),
    })
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println("Branch reference updated successfully")
}
```

## Using Helper Functions

go-github provides helper functions like `github.Ptr()` for creating pointers to values, which is necessary since all struct fields use pointer types to distinguish unset from zero values.

```go
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "github.com/google/go-github/v82/github"
)

func main() {
    token := os.Getenv("GITHUB_TOKEN")
    client := github.NewClient(nil).WithAuthToken(token)
    ctx := context.Background()

    // Using github.Ptr() for pointer values
    repo := &github.Repository{
        Name:                 github.Ptr("example-repo"),
        Description:          github.Ptr("An example repository"),
        Private:              github.Ptr(true),
        HasIssues:            github.Ptr(true),
        HasWiki:              github.Ptr(false),
        HasProjects:          github.Ptr(true),
        AllowSquashMerge:     github.Ptr(true),
        AllowMergeCommit:     github.Ptr(false),
        AllowRebaseMerge:     github.Ptr(true),
        DeleteBranchOnMerge:  github.Ptr(true),
        AutoInit:             github.Ptr(true),
    }

    created, _, err := client.Repositories.Create(ctx, "", repo)
    if err != nil {
        log.Fatal(err)
    }

    // Using Get* methods to safely access pointer values
    fmt.Printf("Repository created:\n")
    fmt.Printf("  Name: %s\n", created.GetName())
    fmt.Printf("  Full Name: %s\n", created.GetFullName())
    fmt.Printf("  Private: %v\n", created.GetPrivate())
    fmt.Printf("  Default Branch: %s\n", created.GetDefaultBranch())
    fmt.Printf("  HTML URL: %s\n", created.GetHTMLURL())
    fmt.Printf("  Clone URL: %s\n", created.GetCloneURL())

    // Using github.Stringify() for debugging
    fmt.Printf("\nFull repository object:\n%s\n", github.Stringify(created))
}
```

## Summary

go-github serves as a comprehensive Go client for the GitHub REST API v3, enabling developers to build automation tools, CI/CD integrations, GitHub Apps, and workflow automation. Common use cases include repository management, issue tracking, pull request automation, GitHub Actions orchestration, secret management, and webhook processing. The library's design around services that mirror GitHub's API structure makes it intuitive for developers familiar with the GitHub API documentation.

Integration patterns typically involve creating an authenticated client, selecting the appropriate service (Repositories, Issues, PullRequests, Actions, etc.), and calling methods that correspond to REST API endpoints. The library handles pagination through both manual iteration and Go 1.23+ iterators, provides rate limit detection and handling, and supports webhook validation for building GitHub App backends. For advanced scenarios, the Git service enables low-level operations like programmatic commits, and the library integrates well with middleware packages for rate limiting and caching.
