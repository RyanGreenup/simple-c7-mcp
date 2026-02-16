### Create Turborepo Vite Example (Quickstart)

Source: https://turborepo.com/docs/guides/frameworks/vite

This command initiates a new Turborepo project pre-configured with Vite, utilizing the 'with-vite' example. It's a quick way to get started with Vite in a monorepo structure.

```bash
pnpm dlx create-turbo@latest -e with-vite
```

```bash
yarn dlx create-turbo@latest -e with-vite
```

```bash
npx create-turbo@latest -e with-vite
```

```bash
bunx create-turbo@latest -e with-vite
```

--------------------------------

### Install Turborepo Globally (npm, yarn, pnpm)

Source: https://turborepo.com/docs/getting-started

Installs the 'turbo' CLI tool globally, enabling 'turbo' commands from any directory. Supports npm, yarn, and pnpm package managers.

```bash
npm install turbo --global
```

```bash
yarn global add turbo
```

```bash
pnpm add turbo --global
```

--------------------------------

### Create Turborepo Project with Package Managers

Source: https://turborepo.com/docs/getting-started/installation

Initialize a new Turborepo project using various package managers. This command downloads and sets up the starter repository with pre-configured applications and libraries.

```bash
pnpm dlx create-turbo@latest
```

```bash
yarn dlx create-turbo@latest
```

```bash
npx create-turbo@latest
```

```bash
bunx create-turbo@latest
```

--------------------------------

### Install Turborepo Globally with Package Managers

Source: https://turborepo.com/docs/getting-started/installation

Install the Turborepo CLI globally on your system using different package managers. Global installation allows for quick execution of Turborepo commands from any directory.

```bash
pnpm add turbo --global
```

```bash
yarn global add turbo
```

```bash
npm install turbo --global
```

```bash
bun install turbo --global
```

--------------------------------

### Create SvelteKit App with Turborepo (Quickstart)

Source: https://turborepo.com/docs/guides/frameworks/sveltekit

Initiates a new Turborepo project with a SvelteKit example application. This command-line interface (CLI) tool automatically sets up the necessary project structure and configurations. No specific inputs are required beyond choosing the package manager.

```bash
pnpm dlx create-turbo@latest -e with-svelte
```

```bash
yarn dlx create-turbo@latest -e with-svelte
```

```bash
npx create-turbo@latest -e with-svelte
```

```bash
bunx create-turbo@latest -e with-svelte
```

--------------------------------

### Install Turborepo Locally (Dev Dependency) with Package Managers

Source: https://turborepo.com/docs/getting-started/installation

Add Turborepo as a development dependency to your project's root. This ensures a consistent version of Turborepo across all developers working on the repository.

```bash
pnpm add turbo --save-dev --ignore-workspace-root-check
```

```bash
yarn add turbo --dev --ignore-workspace-root-check
```

```bash
npm install turbo --save-dev
```

```bash
bun install turbo --dev
```

--------------------------------

### Run Setup Tasks Before Development in turbo.json

Source: https://turborepo.com/docs/crafting-your-repository/developing-applications

Configures a 'dev' task to depend on a setup task (`//#dev:setup`) in `turbo.json`. This ensures that setup scripts or package builds complete before the main development task starts. The setup task can specify outputs like '.codegen/**'.

```json
{
  "tasks": {
    "dev": {
      "cache": false,
      "persistent": true,
      "dependsOn": ["//#dev:setup"]
    },
    "//#dev:setup": {
      "outputs": [".codegen/**"]
    }
  }
}
```

--------------------------------

### Install Turbo CLI using npm

Source: https://turborepo.com/docs/getting-started/add-to-existing-repository

Installs the Turbo CLI globally and as a dev dependency in your repository using npm. This is the standard installation method for npm users.

```bash
# Global install
npm install turbo --global
# Install in repository
npm install turbo --save-dev
```

--------------------------------

### Install Turbo CLI using pnpm

Source: https://turborepo.com/docs/getting-started/add-to-existing-repository

Installs the Turbo CLI globally and as a dev dependency in your repository using pnpm. Requires a `pnpm-workspace.yaml` file to be present.

```bash
# Global install
pnpm add turbo --global
# Install in repository
pnpm add turbo --save-dev --workspace-root
```

--------------------------------

### Install Turbo CLI using bun

Source: https://turborepo.com/docs/getting-started/add-to-existing-repository

Installs the Turbo CLI globally and as a dev dependency in your repository using bun. This is a quick way to add turbo if you are using bun.

```bash
# Global install
bun install turbo --global
# Install in repository
bun install turbo --dev
```

--------------------------------

### Run Package Manager Install Command

Source: https://turborepo.com/docs/guides/migrating-from-nx

Installs project dependencies and updates the lockfile after configuring the workspace and package manager. This step ensures all packages are correctly resolved and added to the monorepo.

```bash
pnpm install
```

```bash
yarn install
```

```bash
npm install
```

```bash
bun install
```

--------------------------------

### Install Turbo CLI using yarn

Source: https://turborepo.com/docs/getting-started/add-to-existing-repository

Installs the Turbo CLI globally and as a dev dependency in your repository using yarn. This method is straightforward for yarn users.

```bash
# Global install
yarn global add turbo
# Install in repository
yarn add turbo --dev
```

--------------------------------

### Install UI and Tailwind Config Packages (bun)

Source: https://turborepo.com/docs/guides/tools/tailwind

Installs the shared UI package and Tailwind CSS configuration using bun with filtering for specific packages. This command adds the dependencies to the 'web' application and the '@repo/ui' package.

```bash
bun install @repo/ui @repo/tailwind-config --dev --filter=@repo/ui --filter=web
```

--------------------------------

### Turborepo Microfrontends Configuration Example (JSON)

Source: https://turborepo.com/docs/guides/microfrontends

A complete JSON configuration for microfrontends in Turborepo, defining applications, their ports, and routing rules. This configuration allows Turborepo to integrate with @vercel/microfrontends.

```json
{
  "$schema": "https://turborepo.com/microfrontends/schema.json",
  "options": {
    "localProxyPort": 3024
  },
  "applications": {
    "web": {
      "packageName": "web",
      "development": {
        "local": {
          "port": 3000
        }
      }
    },
    "docs": {
      "packageName": "documentation",
      "development": {
        "local": {
          "port": 3001
        }
      },
      "routing": [
        {
          "group": "documentation",
          "paths": [
            "/docs",
            "/docs/:path*",
            "/api-reference",
            "/api-reference/:path*"
          ]
        }
      ]
    },
    "blog": {
      "development": {
        "local": {
          "port": 3002
        }
      },
      "routing": [
        {
          "group": "content",
          "paths": [
            "/blog",
            "/blog/:slug",
            "/blog/category/:category",
            "/authors/:author"
          ]
        }
      ]
    },
    "shop": {
      "development": {
        "local": {
          "port": 3003
        }
      },
      "routing": [
        {
          "group": "commerce",
          "paths": [
            "/products",
            "/products/:id",
            "/cart",
            "/checkout",
            "/orders/:orderId"
          ]
        }
      ]
    }
  }
}
```

--------------------------------

### Install eslint-config-turbo with Package Managers

Source: https://turborepo.com/docs/reference/eslint-config-turbo

This section provides installation commands for `eslint-config-turbo` across various package managers (pnpm, yarn, npm, bun). Ensure you have ESLint configured in your project for these commands to be effective.

```bash
pnpm add eslint-config-turbo --filter=@repo/eslint-config
```

```bash
yarn workspace @acme/eslint-config add eslint-config-turbo --dev
```

```bash
npm install --save-dev eslint-config-turbo -w @acme/eslint-config
```

```bash
bun install --dev eslint-config-turbo --filter=@acme/eslint-config
```

--------------------------------

### Basic Vitest Setup in Package JSON

Source: https://turborepo.com/docs/guides/tools/vitest

Shows a minimal package.json configuration for a workspace package, including the 'test' script to run Vitest and the 'vitest' dev dependency.

```json
{
  "scripts": {
    "test": "vitest run"
  },
  "devDependencies": {
    "vitest": "latest"
  }
}
```

--------------------------------

### Install eslint-plugin-turbo with Package Managers

Source: https://turborepo.com/docs/reference/eslint-plugin-turbo

Commands to install the eslint-plugin-turbo package as a dev dependency using pnpm, yarn, npm, and bun. This is typically done in the location where your ESLint configuration is managed.

```bash
pnpm add eslint-plugin-turbo --filter=@repo/eslint-config
```

```bash
yarn workspace @acme/eslint-config add eslint-plugin-turbo --dev
```

```bash
npm i --save-dev eslint-plugin-turbo -w @acme/eslint-config
```

```bash
bun install --dev eslint-plugin-turbo --filter=@acme/eslint-config
```

--------------------------------

### Install Dependencies with Bun

Source: https://turborepo.com/docs/crafting-your-repository/managing-dependencies

This command utilizes Bun to install 'jest' as a dev dependency for the 'web' and '@repo/ui' packages within the monorepo.

```bash
bun install jest --filter=web --filter=@repo/ui --dev
```

--------------------------------

### Importing UI Components for Turborepo Upgrade Guide

Source: https://turborepo.com/docs/crafting-your-repository/upgrading

This snippet demonstrates importing necessary UI components for creating an interactive upgrade guide. It includes components for package manager tabs, general tabs, steps, and callouts, typically used for instructions and user feedback.

```typescript
import { PackageManagerTabs, Tab } from '#components/tabs';
import { Steps, Step } from '#components/steps';
import { Callout } from '#components/callout';
```

--------------------------------

### Install UI and Tailwind Config Packages (pnpm)

Source: https://turborepo.com/docs/guides/tools/tailwind

Installs the shared UI package and Tailwind CSS configuration into the 'web' application and the UI package itself using pnpm. This command ensures both the application and the UI package have access to the necessary dependencies.

```bash
pnpm add @repo/ui @repo/tailwind-config --save-dev --filter=@repo/ui --filter=web
```

--------------------------------

### Install UI and Tailwind Config Packages (npm)

Source: https://turborepo.com/docs/guides/tools/tailwind

Installs the shared UI package and Tailwind CSS configuration using npm workspaces. This command adds the packages as development dependencies to the 'web' application and the '@repo/ui' package.

```bash
npm install @repo/ui @repo/tailwind-config --workspace=web --workspace=@repo/ui --save-dev
```

--------------------------------

### Install Turborepo as a Dev Dependency

Source: https://turborepo.com/docs/guides/migrating-from-nx

Adds Turborepo to the project's development dependencies. This command installs Turborepo in the root of the workspace, making its commands available for use.

```bash
pnpm add turbo --save-dev --workspace-root
```

```bash
yarn add turbo --save-dev --ignore-workspace-root-check
```

```bash
npm install turbo --save-dev
```

```bash
bun install turbo --dev
```

--------------------------------

### Download Cache Artifact JavaScript Example

Source: https://turborepo.com/docs/openapi/artifacts/download-artifact

Example code to download a cache artifact using JavaScript. This snippet assumes an existing API client setup and demonstrates how to make the GET request to the artifact endpoint.

--------------------------------

### Turborepo CLI: Get Microfrontend Port (Bash)

Source: https://turborepo.com/docs/guides/microfrontends

Example of how to use the `turbo get-mfe-port` command, specifically when inferring the port is skipped and the repository root needs to be specified. This is useful when running the command from a package directory.

```bash
turbo --skip-infer --cwd ../.. get-mfe-port
```

--------------------------------

### Configure eslint-plugin-turbo with Flat Config (Recommended)

Source: https://turborepo.com/docs/reference/eslint-plugin-turbo

Example of how to integrate eslint-plugin-turbo using the recommended settings in an ESLint Flat Config file (`eslint.config.js`). This enables the plugin and its default rules.

```javascript
import turbo from 'eslint-plugin-turbo';

export default [turbo.configs['flat/recommended']];
```

--------------------------------

### Install UI and Tailwind Config Packages (yarn)

Source: https://turborepo.com/docs/guides/tools/tailwind

Installs the shared UI package and Tailwind CSS configuration using yarn workspaces. This command adds the packages as development dependencies to both the 'web' application and the '@repo/ui' package.

```bash
yarn workspace web add @repo/ui @repo/tailwind-config --dev
yarn workspace @repo/ui add @repo/ui @repo/tailwind-config --dev
```

--------------------------------

### Buildkite Pipeline Configuration for CI/CD

Source: https://turborepo.com/docs/guides/ci-vendors/buildkite

Sets up Buildkite pipeline steps for installing dependencies, running tests, and building the project. Supports multiple package managers (pnpm, yarn, npm, bun).

```yaml
steps:
  - label: ":test_tube: Test"
    command: |
      pnpm install
      pnpm test

  - label: ":hammer: Build"
    command: |
      pnpm install
      pnpm build
```

```yaml
steps:
  - label: ":test_tube: Test"
    command: |
      yarn
      yarn test

  - label: ":hammer: Build"
    command: |
      yarn
      yarn build
```

```yaml
steps:
  - label: ":test_tube: Test"
    command: |
      npm install
      npm test

  - label: ":hammer: Build"
    command: |
      npm install
      npm run build
```

```yaml
steps:
  - label: ":test_tube: Test"
    command: |
      bun install
      bun run test

  - label: ":hammer: Build"
    command: |
      bun install
      bun run build
```

--------------------------------

### Install Turborepo using Package Managers

Source: https://turborepo.com/docs/guides/single-package-workspaces

Installs the `turbo` package as a development dependency across various package managers. This is a prerequisite for using Turborepo's features.

```bash
pnpm add turbo --save-dev
```

```bash
yarn add turbo --dev
```

```bash
npm install turbo --save-dev
```

```bash
bun install turbo --dev
```

--------------------------------

### Build Dockerfile with Turborepo Prune

Source: https://turborepo.com/docs/guides/tools/docker

This Dockerfile example demonstrates a multi-stage build process for a Next.js application within a Turborepo monorepo. It utilizes `turbo prune` to create an isolated workspace for the 'web' application before installing dependencies and building the project. The final stage is optimized for production.

```docker
FROM node:18-alpine AS base
RUN apk update
RUN apk add --no-cache libc6-compat
# Set working directory
WORKDIR /app

# ---
FROM base AS prepare
# Replace <your-major-version> with the major version installed in your repository. For example:
# RUN yarn global add turbo@^2
RUN yarn global add turbo@^<your-major-version>
COPY . .
# Add lockfile and package.json's of isolated subworkspace
# Generate a partial monorepo with a pruned lockfile for a target workspace.
# Assuming "web" is the name entered in the project's package.json: { name: "web" }
RUN turbo prune web --docker

# ---
FROM base AS builder
# First install the dependencies (as they change less often)
COPY --from=prepare /app/out/json/ .
RUN yarn install
# Build the project
COPY --from=prepare /app/out/full/ .

# Uncomment and use build args to enable remote caching
# ARG TURBO_TEAM
# ENV TURBO_TEAM=$TURBO_TEAM

# ARG TURBO_TOKEN
# ENV TURBO_TOKEN=$TURBO_TOKEN

RUN yarn turbo build

# ---
FROM base AS runner
# Don't run production as root for security reasons
RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs
USER nextjs

# Automatically leverage output traces to reduce image size
# https://nextjs.org/docs/advanced-features/output-file-tracing
COPY --from=builder --chown=nextjs:nodejs /app/apps/web/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/apps/web/.next/static ./apps/web/.next/static
COPY --from=builder --chown=nextjs:nodejs /app/apps/web/public ./apps/web/public

CMD node apps/web/server.js
```

--------------------------------

### Travis CI Configuration for Bun

Source: https://turborepo.com/docs/guides/ci-vendors/travis-ci

Integrates Travis CI with Node.js LTS, installs Bun, caches the npm directory, and executes Bun install and run commands for build and test.

```yaml
language: node_js
node_js:
  - lts/*
cache:
  npm: false
  directories:
    - "~/.pnpm-store"
before_install:
  - curl -fsSL https://bun.sh/install | bash
install:
  - bun install
script:
  - bun run build
script:
  - bun run test
```

--------------------------------

### Install Dependencies with npm Workspaces

Source: https://turborepo.com/docs/crafting-your-repository/managing-dependencies

This command installs 'jest' as a dev dependency in the 'web' and '@repo/ui' workspaces using npm's workspace flag.

```bash
npm install jest --workspace=web --workspace=@repo/ui --save-dev
```

--------------------------------

### Filter Turbo tasks with CLI flags

Source: https://turborepo.com/docs/crafting-your-repository/running-tasks

These bash examples illustrate how to use Turborepo's CLI flags to customize task execution. The first example shows filtering a `build` task to a specific package (`@repo/ui`), while the second demonstrates running a `dry` build to preview changes without execution. The third example overrides the `outputLogs` configuration for a `lint` task.

```bash
turbo build --filter=@repo/ui
```

```bash
turbo build --dry
```

```bash
turbo lint --output-logs=errors-only
```

--------------------------------

### CircleCI Configuration for Turborepo (bun)

Source: https://turborepo.com/docs/guides/ci-vendors/circleci

This CircleCI configuration (`.circleci/config.yml`) demonstrates how to set up a CI pipeline for Turborepo projects using the bun package manager. It covers checking out code, installing Node.js, installing bun globally, and then executing the build and test tasks via Turborepo. The `TURBO_UI=false` environment variable is used to ensure compatibility with CircleCI's execution environment.

```yaml
version: 2.1
orbs:
  node: circleci/node@5.0.2 workflows:
  test:
    jobs:
      - test
jobs:
  test:
    docker:
      - image: cimg/node:lts
    steps:
      - checkout
      - node/install-packages
      - run:
          command: npm i -g bun
          environment:
            TURBO_UI: "false"
      - run:
          command: bun run build
          environment:
            TURBO_UI: "false"
      - run:
          command: bun run test
          environment:
            TURBO_UI: "false"

```

--------------------------------

### Compare Package-Specific vs. Package Configurations in turbo.json

Source: https://turborepo.com/docs/reference/package-configurations

This JSON example demonstrates how package-specific tasks in the root turbo.json overwrite baseline configurations, requiring duplication of settings like 'outputLogs' and 'inputs'. Package Configurations, in contrast, merge configurations, simplifying task definitions.

```jsonc
{
  "tasks": {
    "build": {
      "outputLogs": "hash-only",
      "inputs": ["src/**"],
      "outputs": [".next/**", "!.next/cache/**"]
    },
    "my-sveltekit-app#build": {
      "outputLogs": "hash-only", // must duplicate this
      "inputs": ["src/**"], // must duplicate this
      "outputs": [".svelte-kit/**"]
    }
  }
}
```

--------------------------------

### Install Jest using Package Managers

Source: https://turborepo.com/docs/guides/tools/jest

Installs Jest as a development dependency in specified workspaces (`@repo/ui` and `web`) using various package managers (pnpm, yarn, npm, bun). This is a prerequisite for setting up test suites.

```bash
pnpm add jest --save-dev --filter=@repo/ui --filter=web
```

```bash
yarn workspace web add jest --dev
yarn workspace @repo/ui add jest --dev
```

```bash
npm install jest --workspace=web --workspace=@repo/ui --save-dev
```

```bash
bun install jest --dev --filter=@repo/ui --filter=web
```

--------------------------------

### CircleCI Configuration for Turborepo (npm)

Source: https://turborepo.com/docs/guides/ci-vendors/circleci

This CircleCI configuration (`.circleci/config.yml`) is designed for Turborepo projects managed with npm. It includes standard CI steps such as code checkout, Node.js setup, and package installation. It then proceeds to run Turborepo's build and test commands, ensuring `TURBO_UI` is set to `false` to bypass potential terminal UI conflicts within the CircleCI environment.

```yaml
version: 2.1
orbs:
  node: circleci/node@5.0.2 workflows:
  test:
    jobs:
      - test
jobs:
  test:
    docker:
      - image: cimg/node:lts
    steps:
      - checkout
      - node/install-packages
      - run:
          command: npm run build
          environment:
            TURBO_UI: "false"

      - run:
          command: npm run test
          environment:
            TURBO_UI: "false"

```

--------------------------------

### Get Turbo Binary Path using `turbo bin`

Source: https://turborepo.com/docs/reference/bin

This command retrieves the absolute path to the `turbo` binary. The output will vary based on whether `turbo` was installed globally or locally within a repository. It's useful for scripting or locating the executable for direct use.

```bash
turbo bin
```

--------------------------------

### Install Dependencies with Yarn 1 Workspaces

Source: https://turborepo.com/docs/crafting-your-repository/managing-dependencies

Demonstrates how to add 'jest' as a dev dependency to individual packages ('web', '@repo/ui') using Yarn 1's workspace command.

```bash
yarn workspace web add jest --dev
yarn workspace @repo/ui add jest --dev
```

--------------------------------

### Add @repo/math dependency to web app (bun)

Source: https://turborepo.com/docs/crafting-your-repository/creating-an-internal-package

This snippet demonstrates adding the '@repo/math' package as a dependency in 'apps/web/package.json' using Bun. 'workspace:*' is used to link to the local workspace package. After changes, run your package manager's install command.

```json
{
  "dependencies": {
    "@repo/math": "workspace:*",
    "next": "latest",
    "react": "latest",
    "react-dom": "latest"
  }
}
```

--------------------------------

### Run All Turborepo Codemods for Upgrade

Source: https://turborepo.com/docs/reference/turbo-codemod

Automatically applies all necessary codemods to upgrade your Turborepo installation. This is the recommended command for most version upgrades.

```bash
npx @turbo/codemod
```

--------------------------------

### Example: Configure Allow List for Undefined Env Vars (Legacy Config)

Source: https://turborepo.com/docs/reference/eslint-plugin-turbo

An example demonstrating the configuration of the `turbo/no-undeclared-env-vars` rule in a legacy ESLint configuration (`.eslintrc.json`). It includes an `allowList` to specify environment variable patterns that should be ignored by the rule.

```json
{
  "plugins": ["turbo"],
  "rules": {
    "turbo/no-undeclared-env-vars": [
      "error",
      {
        "allowList": ["^ENV_[A-Z]+$"]
      }
    ]
  }
}
```

--------------------------------

### Add SvelteKit App to Existing Monorepo

Source: https://turborepo.com/docs/guides/frameworks/sveltekit

Adds a new SvelteKit application to an existing Turborepo monorepo using the Svelte scaffolding tool. This process involves running a package manager command to initiate the SvelteKit project setup within your monorepo's package structure. It requires no specific inputs.

```bash
pnpm dlx sv create
```

```bash
yarn dlx sv create
```

```bash
npx sv create
```

```bash
bunx sv create
```

--------------------------------

### CircleCI Configuration for Turborepo (pnpm)

Source: https://turborepo.com/docs/guides/ci-vendors/circleci

This is a CircleCI configuration file (`.circleci/config.yml`) specifically set up for projects using Turborepo with the pnpm package manager. It includes steps for checking out code, installing Node.js, installing pnpm globally, and then running Turborepo's build and test commands. The `TURBO_UI=false` environment variable is crucial for compatibility with CircleCI's non-interactive terminal.

```yaml
version: 2.1
orbs:
  node: circleci/node@5.0.2 workflows:
  test:
    jobs:
      - test
jobs:
  test:
    docker:
      - image: cimg/node:lts
    steps:
      - checkout
      - node/install-packages
      - run:
          command: npm i -g pnpm
          environment:
            TURBO_UI: "false"
      - run:
          command: pnpm build
          environment:
            TURBO_UI: "false"
      - run:
          command: pnpm test
          environment:
            TURBO_UI: "false"

```

--------------------------------

### Configure Turbo.json with Web Schema

Source: https://turborepo.com/docs/getting-started/editor-integration

Use the `$schema` key in your `turbo.json` to enable auto-completion and linting in your editor by sourcing the JSON schema directly from the web. This method does not require running package manager install commands.

```json
{
  "$schema": "https://turborepo.com/schema.json"
}
```

```json
{
  "$schema": "https://turborepo.com/schema.v1.json"
}
```

--------------------------------

### Package Configurations: Task Dependencies Example in turbo.json

Source: https://turborepo.com/docs/reference/package-configurations

This JSON configuration demonstrates how a 'build' task within a package's turbo.json can still depend on a package-specific task from another package, like 'some-pkg#compile'. This highlights how dependencies can be managed even with Package Configuration limitations.

```jsonc
{
  "tasks": {
    "build": {
      "dependsOn": ["some-pkg#compile"] // [!code highlight]
    }
  }
}
```

--------------------------------

### GitHub Actions CI Workflow (bun)

Source: https://turborepo.com/docs/guides/ci-vendors/github-actions

Sets up a GitHub Actions CI workflow for a Turborepo project using bun. It checks out code, sets up Bun and Node.js, installs dependencies, and runs build scripts.

```yaml
name: CI

on:
  push:
    branches: ["main"]
  pull_request:
    types: [opened, synchronize]

jobs:
  build:
    name: Build and Test
    timeout-minutes: 15
    runs-on: ubuntu-latest
    # To use Remote Caching, uncomment the next lines and follow the steps below.
    # env:
    #  TURBO_TOKEN: ${{ secrets.TURBO_TOKEN }}
    #  TURBO_TEAM: ${{ vars.TURBO_TEAM }}

    steps:
      - name: Check out code
        uses: actions/checkout@v4
        with:
          fetch-depth: 2

      - uses: oven-sh/setup-bun@v2

      - name: Setup Node.js environment
        uses: actions/setup-node@v4
        with:
          node-version: 20

      - name: Install dependencies
        run: bun install

      - name: Build
        run: bun run build

```

--------------------------------

### Create Storybook App Directory

Source: https://turborepo.com/docs/guides/tools/storybook

This command sequence creates a new directory named 'apps/storybook' and changes the current directory into it, preparing for Storybook installation.

```bash
mkdir apps/storybook
cd apps/storybook
```

--------------------------------

### Install Dependencies with Yarn 2+ Workspaces Foreach

Source: https://turborepo.com/docs/crafting-your-repository/managing-dependencies

This command uses Yarn 2+ 'workspaces foreach' to add 'jest' as a dev dependency to specified packages ('web', '@repo/ui') recursively.

```bash
yarn workspaces foreach -R --from '{web,@repo/ui}' add jest --dev
```

--------------------------------

### Turborepo Task Configuration with Dependencies and Outputs

Source: https://turborepo.com/docs/guides/multi-language

Example of a turbo.json configuration defining a 'build' task. It includes `dependsOn` to specify build order and `outputs` to manage cached artifacts, accommodating both JavaScript and non-JavaScript project outputs.

```json
{
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**", "target/release/**"]
    }
  }
}
```

--------------------------------

### Example: Configure Allow List for Undefined Env Vars (Flat Config)

Source: https://turborepo.com/docs/reference/eslint-plugin-turbo

An example showcasing how to configure the `turbo/no-undeclared-env-vars` rule in ESLint Flat Config to include an allow list for environment variable patterns. This prevents errors for environment variables matching the specified regex.

```javascript
import turbo from 'eslint-plugin-turbo';

export default [
  {
    plugins: {
      turbo,
    },
    rules: {
      'turbo/no-undeclared-env-vars': [
        'error',
        {
          allowList: ['^ENV_[A-Z]+$'],
        },
      ],
    },
  },
];
```

--------------------------------

### Travis CI Configuration for pnpm

Source: https://turborepo.com/docs/guides/ci-vendors/travis-ci

Sets up Travis CI to use Node.js LTS, caches the pnpm store, and installs/runs pnpm commands. Requires explicit pnpm installation.

```yaml
language: node_js
node_js:
  - lts/*
cache:
  npm: false
  directories:
    - "~/.pnpm-store"
before_install:
  - curl -f https://get.pnpm.io/v6.16.js | node - add --global pnpm@6.32.2
  - pnpm config set store-dir ~/.pnpm-store
install:
  - pnpm install
script:
  - pnpm build
script:
  - pnpm test
```

--------------------------------

### Configure package.json Scripts for Turborepo

Source: https://turborepo.com/docs/guides/single-package-workspaces

Defines various scripts within a project's `package.json` file. These scripts represent individual tasks that can be orchestrated by Turborepo, such as starting a dev server, building, linting, or database-related operations.

```json
{
  "name": "@acme/my-app",
  "version": "0.0.0",
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "check-types": "tsc --noEmit",
    "db:up": "docker-compose up -d",
    "db:push": "your-orm-tool schema-push",
    "db:seed": "node ./db-seed.js"
  }
}
```

--------------------------------

### Install Dependencies Recursively with pnpm

Source: https://turborepo.com/docs/crafting-your-repository/managing-dependencies

This command uses pnpm to add 'jest' as a dev dependency to multiple specified packages ('web', '@repo/ui', 'docs') within the monorepo.

```bash
pnpm add jest --save-dev --recursive --filter=web --filter=@repo/ui --filter=docs
```

--------------------------------

### Configure build task dependencies in turbo.json

Source: https://turborepo.com/docs/crafting-your-repository/configuring-tasks

Shows how to set up task dependencies using the `dependsOn` key in `turbo.json`. This example ensures that dependent builds (like application builds) wait for their library builds (denoted by '^build') to complete, establishing the correct execution order.

```json
{
  "tasks": {
    "build": {
      "dependsOn": ["^build"] // [!code highlight]
    }
  }
}
```

--------------------------------

### Install Internal Package in package.json (yarn, npm)

Source: https://turborepo.com/docs/core-concepts/internal-packages

Shows how to install internal packages using the wildcard syntax (`*`) in `package.json` for yarn and npm. This method also enables local package linking within the monorepo.

```json
{
  "dependencies": {
    "@repo/ui": "*" // [!code highlight]
  }
}
```

```json
{
  "dependencies": {
    "@repo/ui": "*" // [!code highlight]
  }
}
```

--------------------------------

### Install TypeScript Config in Package

Source: https://turborepo.com/docs/guides/tools/typescript

Installs the shared TypeScript configuration package and the TypeScript compiler as development dependencies in a specific package (e.g., 'web' app).

```json
{
  "devDependencies": {
     "@repo/typescript-config": "workspace:*",
     "typescript": "latest"
  }
}
```

```json
{
  "devDependencies": {
     "@repo/typescript-config": "*",
     "typescript": "latest"
  }
}
```

```json
{
  "devDependencies": {
     "@repo/typescript-config": "*",
     "typescript": "latest"
  }
}
```

```json
{
  "devDependencies": {
     "@repo/typescript-config": "workspace:*",
     "typescript": "latest"
  }
}
```

--------------------------------

### Install Storybook Dependencies in UI Package

Source: https://turborepo.com/docs/guides/tools/storybook

To enable writing Storybook stories within a specific package (like `@repo/ui`), install the necessary Storybook packages, such as `@storybook/react`, as development dependencies for that package. This ensures the package has the required tools for Storybook integration.

```bash
pnpm add @storybook/react --filter=@repo/ui --save-dev
```

```bash
yarn workspace @repo/ui add @storybook/react --dev
```

```bash
npm install @storybook/react --workspace=@repo/ui --save-dev
```

```bash
bun install @storybook/react --filter=@repo/ui --save-dev
```

--------------------------------

### Configure eslint-plugin-turbo Rules (Legacy Config)

Source: https://turborepo.com/docs/reference/eslint-plugin-turbo

Details how to configure specific rules provided by `eslint-plugin-turbo` within a legacy ESLint configuration file. This example enables the 'turbo/no-undeclared-env-vars' rule with an error severity.

```json
{
  "rules": {
    "turbo/no-undeclared-env-vars": "error"
  }
}
```

--------------------------------

### Configure eslint-plugin-turbo Rules with Flat Config

Source: https://turborepo.com/docs/reference/eslint-plugin-turbo

Demonstrates how to manually configure eslint-plugin-turbo and its rules within an ESLint Flat Config setup. This allows for specific rule configurations, such as enabling 'turbo/no-undeclared-env-vars'.

```javascript
import turbo from 'eslint-plugin-turbo';

export default [
  {
    plugins: {
      turbo,
    },
    rules: {
      'turbo/no-undeclared-env-vars': 'error',
    },
  },
];
```

--------------------------------

### Define Boundaries Tags using Package Configurations in turbo.json

Source: https://turborepo.com/docs/reference/package-configurations

This example shows how to add a 'tags' field to a package's turbo.json to declare Tags for Boundaries. This allows for defining rules for dependency relationships based on these tags.

```diff
{
+ "tags": ["my-tag"],
  "extends": ["//"],
  "tasks": {
    "build": {
      "dependsOn": ["compile"]
    },
    "compile": {}
  }
}
```

--------------------------------

### GitHub Actions CI Workflow (npm)

Source: https://turborepo.com/docs/guides/ci-vendors/github-actions

Sets up a GitHub Actions CI workflow for a Turborepo project using npm. It checks out code, sets up Node.js with caching for npm, installs dependencies, and runs build and test scripts.

```yaml
name: CI

on:
  push:
    branches: ["main"]
  pull_request:
    types: [opened, synchronize]

jobs:
  build:
    name: Build and Test
    timeout-minutes: 15
    runs-on: ubuntu-latest
    # To use Remote Caching, uncomment the next lines and follow the steps below.
    # env:
    #  TURBO_TOKEN: ${{ secrets.TURBO_TOKEN }}
    #  TURBO_TEAM: ${{ vars.TURBO_TEAM }}
    #  TURBO_REMOTE_ONLY: true

    steps:
      - name: Check out code
        uses: actions/checkout@v4
        with:
          fetch-depth: 2

      - name: Setup Node.js environment
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'

      - name: Install dependencies
        run: npm install

      - name: Build
        run: npm run build

      - name: Test
        run: npm run test

```

--------------------------------

### Configure Multi-Framework Entrypoints in Package.json

Source: https://turborepo.com/docs/guides/frameworks/framework-bindings

This JSON configuration illustrates how to use the `exports` field in `package.json` to define separate entrypoints for different framework bindings. This allows a single library to provide framework-specific versions of components, like a basic link and a Next.js link, improving bundler compatibility.

```json
{
  "exports": {
    "./link": "./dist/link.js",
    "./next-js/link": "./dist/next-js/link.js"
  },
  "peerDependencies": {
    "next": "*"
  }
}
```

--------------------------------

### Package Configurations: Task Syntax Limitations in turbo.json

Source: https://turborepo.com/docs/reference/package-configurations

This JSON example illustrates the limitations of Package Configurations in Turborepo. It shows that the 'package#task' syntax is not allowed when configuring tasks within a package's turbo.json, as the package is inferred from the configuration's location.

```jsonc
{
  "tasks": {
    "my-nextjs-app#build": {
      // ❌ This is not allowed. Even though it's
      // referencing the correct package, "my-nextjs-app"
      // is inferred, and we don't need to specify it again.
      // This syntax also has different behavior, so we do not want to allow it.
      // (see "Comparison to package-specific tasks" section)
    },
    "my-sveltekit-app#build": {
      // ❌ Changing configuration for the "my-sveltekit-app" package
      // from Package Configuration in "my-nextjs-app" is not allowed.
    },
    "build": {
      // ✅ just use the task name!
    }
  }
}
```

--------------------------------

### Importing from Package Exports in TypeScript

Source: https://turborepo.com/docs/crafting-your-repository/structuring-a-repository

Demonstrates how to import modules from a package that has defined specific entrypoints using the 'exports' field in its package.json. This example shows importing constants and functions from a hypothetical '@repo/math' package, illustrating the benefits of explicit exports for IDE autocompletion and avoiding barrel files.

```ts
import { GRAVITATIONAL_CONSTANT, SPEED_OF_LIGHT } from '@repo/math';
import { add } from '@repo/math/add';
import { subtract } from '@repo/math/subtract';
```

--------------------------------

### Define Build Script for Non-JavaScript Project (Rust CLI)

Source: https://turborepo.com/docs/guides/multi-language

Example of a package.json file for a non-JavaScript project (Rust CLI) within a Turborepo monorepo. It specifies the project name and a 'build' script that Turborepo can execute.

```json
{
  "name": "@repo/rust-cli",
  "scripts": {
    "build": "cargo build --release"
  }
}
```

--------------------------------

### GitLab CI configuration for Turborepo with pnpm

Source: https://turborepo.com/docs/guides/ci-vendors/gitlab-ci

GitLab CI pipeline configuration for a Turborepo project using pnpm. Includes setting up pnpm, installing dependencies, and running build/test scripts. Utilizes caching for the pnpm store.

```yaml
image: node:latest
stages:
  - build
build:
  stage: build
  before_script:
    - curl -f https://get.pnpm.io/v6.16.js | node - add --global pnpm@6.32.2
    - pnpm config set store-dir .pnpm-store
  script:
    - pnpm install
    - pnpm build
    - pnpm test
  cache:
    key:
      files:
        - pnpm-lock.yaml
    paths:
      - .pnpm-store
```

--------------------------------

### GitHub Actions CI Workflow (pnpm)

Source: https://turborepo.com/docs/guides/ci-vendors/github-actions

Sets up a GitHub Actions CI workflow for a Turborepo project using pnpm. It checks out code, sets up Node.js with caching for pnpm, installs dependencies, and runs build and test scripts.

```yaml
name: CI

on:
  push:
    branches: ["main"]
  pull_request:
    types: [opened, synchronize]

jobs:
  build:
    name: Build and Test
    timeout-minutes: 15
    runs-on: ubuntu-latest
    # To use Remote Caching, uncomment the next lines and follow the steps below.
    # env:
    #  TURBO_TOKEN: ${{ secrets.TURBO_TOKEN }}
    #  TURBO_TEAM: ${{ vars.TURBO_TEAM }}

    steps:
      - name: Check out code
        uses: actions/checkout@v4
        with:
          fetch-depth: 2

      - uses: pnpm/action-setup@v3
        with:
          version: 8

      - name: Setup Node.js environment
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - name: Install dependencies
        run: pnpm install

      - name: Build
        run: pnpm build

      - name: Test
        run: pnpm test

```

--------------------------------

### Turborepo CI Environment Variables Setup

Source: https://turborepo.com/docs/guides/ci-vendors

This snippet demonstrates the environment variables required to enable Turborepo's Remote Caching in a CI environment. It includes `TURBO_TOKEN` for authentication and `TURBO_TEAM` for specifying the associated account, particularly relevant for Vercel Remote Cache.

```bash
# Example of setting environment variables in a CI script
export TURBO_TOKEN="your_remote_cache_token"
export TURBO_TEAM="your_team_slug"

# Then run your turbo commands
turbo run build
```

--------------------------------

### GitLab CI configuration for Turborepo with npm

Source: https://turborepo.com/docs/guides/ci-vendors/gitlab-ci

GitLab CI pipeline configuration for a Turborepo project using npm. Installs dependencies and executes build and test scripts.

```yaml
image: node:latest
stages:
  - build
build:
  stage: build
  script:
    - npm install
    - npm run build
    - npm run test
```

--------------------------------

### Set up pnpm workspaces

Source: https://turborepo.com/docs/getting-started/add-to-existing-repository

This configuration defines the workspace structure for pnpm by specifying the directories that contain packages. It uses glob patterns to include applications and libraries, ensuring pnpm recognizes the monorepo structure.

```yaml
packages:
  - "apps/*"
  - "packages/*"
```

--------------------------------

### Turbo Bin Command

Source: https://turborepo.com/docs/reference/bin

Retrieves the absolute path to the `turbo` binary. The returned path depends on whether `turbo` is installed globally or locally within a repository.

```APIDOC
## GET /turbo/bin

### Description
Get the path to the `turbo` binary. This command returns the absolute path to the `turbo` executable. The path will differ based on whether `turbo` was installed globally or as a local dependency within a project.

### Method
GET

### Endpoint
/turbo/bin

### Parameters
This endpoint does not accept any parameters.

### Request Example
```bash
turbo bin
```

### Response
#### Success Response (200)
- **path** (string) - The absolute path to the `turbo` binary.

#### Response Example
```json
{
  "path": "/path/to/your/turbo/binary"
}
```
```

--------------------------------

### Travis CI Configuration for npm

Source: https://turborepo.com/docs/guides/ci-vendors/travis-ci

Sets up Travis CI to use Node.js LTS and execute npm install and run scripts for build and test. This is a standard npm configuration.

```yaml
language: node_js
node_js:
  - lts/*
install:
  - npm install
script:
  - npm run build
script:
  - npm run test
```

--------------------------------

### Generate Cache Key Before Turborepo Run (package.json)

Source: https://turborepo.com/docs/guides/handling-platforms

This `package.json` script defines a command `build-for-platforms` that first executes the Node.js script to generate `turbo-cache-key.json`, and then runs the `turbo run build` command. This ensures that Turborepo considers the generated cache key when calculating task hashes.

```json
{
  "scripts": {
    "build-for-platforms": "node ./scripts/create-turbo-cache-key.js && turbo run build"
  }
}

```

--------------------------------

### Define Sequential Tasks in turbo.json

Source: https://turborepo.com/docs/guides/single-package-workspaces

Configures Turborepo tasks, specifying dependencies between them to ensure they run in a defined sequence. This example sets up a development workflow where database seeding depends on schema push, which depends on the database coming up.

```json
{
  "$schema": "https://turborepo.com/schema.json",
  "tasks": {
    "dev": {
      "dependsOn": ["db:seed"],
      "cache": false,
      "persistent": true
    },
    "db:seed": {
      "dependsOn": ["db:push"],
      "cache": false
    },
    "db:push": {
      "dependsOn": ["db:up"],
      "cache": false
    },
    "db:up": {
      "cache": false
    }
  }
}
```

--------------------------------

### GitLab CI configuration for Turborepo with bun

Source: https://turborepo.com/docs/guides/ci-vendors/gitlab-ci

GitLab CI pipeline configuration for a Turborepo project using bun. Sets up bun, installs dependencies, and runs build/test scripts. Caches node_modules based on bun.lock.

```yaml
default:
  image: oven/bun:1.2
  cache:
    key:
      files:
        - bun.lock
    paths:
      - node_modules/
  before_script:
      - bun install

build:
script: - bun run build

test:
script: - bun run test
```

--------------------------------

### Add UI Package to Storybook App

Source: https://turborepo.com/docs/guides/tools/storybook

Installs the '@repo/ui' package into the 'storybook' application. This allows Storybook to render components from your shared UI library. Syntax varies slightly between package managers.

```bash
pnpm add @repo/ui --filter=storybook
```

```bash
yarn workspace storybook add @repo/ui
```

```bash
npm install @repo/ui --workspace=storybook
```

```bash
bun install @repo/ui --filter=storybook
```

--------------------------------

### Run Multiple Tasks Concurrently with Turborepo CLI

Source: https://turborepo.com/docs/guides/single-package-workspaces

Executes multiple Turborepo tasks simultaneously from the command line. This example demonstrates running type checking, linting, and formatting checks in parallel to speed up the development feedback loop.

```bash
turbo check-types lint format
```

--------------------------------

### Create Turborepo Project

Source: https://turborepo.com/docs/crafting-your-repository/caching

Command to create a new Turborepo project. This is the initial step before running builds and experiencing caching.

```bash
npx create-turbo@latest
```

--------------------------------

### Root turbo.json for Multiple Frameworks

Source: https://turborepo.com/docs/reference/package-configurations

This JSON configuration shows a root `turbo.json` intended for a monorepo containing multiple frameworks, like Next.js and SvelteKit. It defines a common 'build' task with `outputs` that encompass build artifacts from both frameworks. This approach requires listing all possible outputs, even those not generated by all packages.

```jsonc
{
  "tasks": {
    "build": {
      "outputs": [".next/**", "!.next/cache/**", ".svelte-kit/**"]
    }
  }
}
```

--------------------------------

### Get Remote Caching Status - Python

Source: https://turborepo.com/docs/openapi/artifacts/status

Sends a GET request to the Turborepo API to retrieve the remote caching status. This Python script includes the necessary Authorization header and can be configured with team ID and slug. It prints the JSON response.

```python
import requests

url = "https://api.vercel.com/v8/artifacts/status?teamId=string&slug=string"
token = "<token>"

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(url, headers=headers)

print(response.json())
```

=== COMPLETE CONTENT === This response contains all available snippets from this library. No additional content exists. Do not make further requests.