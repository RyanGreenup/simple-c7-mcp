### Nuxt Example: Hello World

Source: https://context7_llms

A basic Nuxt application example demonstrating the 'Hello World' setup.

```vue
<template>
  <div>
    <h1>Hello World</h1>
  </div>
</template>

<script setup>
// Script logic if any
</script>

<style scoped>
/* Component styles */
h1 {
  color: blue;
}
</style>
```

--------------------------------

### Render Deployment Build and Start Commands

Source: https://context7_llms

Commands to set up a Nuxt application on Render. This includes installing dependencies and building the application, followed by the command to start the server.

```bash
yarn && yarn build
npm install && npm run build
pnpm i --shamefully-hoist && pnpm build
```

```bash
node .output/server/index.mjs
```

--------------------------------

### Nuxt.js 3 Boilerplate Setup and Development

Source: https://vercel.com/new

This snippet provides instructions for setting up and running a Nuxt.js 3 application. It includes commands for installing dependencies, starting the development server, and building the application for production.

```bash
yarn install
```

```bash
yarn dev
```

```bash
yarn build
```

--------------------------------

### Example: Installing and Using 'uil:github' Icon in Nuxt.js

Source: https://nuxt.com/modules/icon

Demonstrates the process of installing the 'uil' icon collection and then using the 'uil:github' icon. This ensures icons are served locally for optimal performance.

```html
<Icon name="uil:github" />

```

--------------------------------

### Nuxt MCP Setup - Cursor

Source: https://context7_llms

Instructions for installing the Nuxt MCP server in Cursor, either via a deeplink or manual configuration.

```APIDOC
## Nuxt MCP Setup - Cursor

### Description
Integrate the Nuxt MCP server with Cursor using the provided deeplink or by manually updating the MCP configuration.

### Installation Options

**1. Using Deeplink:**
Click the button below to install the Nuxt MCP server directly in Cursor:

`cursor://anysphere.cursor-deeplink/mcp/install?name=nuxt&config=eyJ0eXBlIjoiaHR0cCIsInVybCI6Imh0dHBzOi8vbnV4dC5jb20vbWNwIn0%3D`

**2. Manual Setup:**

   - Open Cursor and go to "Settings" > "Tools & MCP".
   - Add the Nuxt MCP server configuration.

   Or, manually create/update `.cursor/mcp.json` in your project root with the following content:

   ```json
   {
     "mcpServers": {
       "nuxt": {
         "type": "http",
         "url": "https://nuxt.com/mcp"
       }
     }
   }
   ```
```

--------------------------------

### Vue Development Example with Nuxt (app.vue)

Source: https://go.nuxt.com/github

An example of an `app.vue` file demonstrating basic Nuxt setup. It includes meta tags for SEO using `useSeoMeta`, a template with header, main content (`NuxtPage`), and footer, along with scoped CSS styling. This snippet requires Vue.js and Nuxt.js to be installed.

```vue
<script setup lang="ts">
useSeoMeta({
  title: 'Meet Nuxt',
  description: 'The Intuitive Vue Framework.',
})
</script>

<template>
  <div id="app">
    <AppHeader />
    <NuxtPage />
    <AppFooter />
  </div>
</template>

<style scoped>
#app {
  background-color: #020420;
  color: #00DC82;
}
</style>
```

--------------------------------

### Postgres + Nuxt Starter Setup and Development

Source: https://vercel.com/new

This snippet outlines the installation and development commands for a Nuxt starter project integrated with a Postgres database. It covers dependency installation for yarn, npm, and pnpm, as well as commands for running the development server, building for production, and previewing the production build.

```bash
# yarn
yarn install
```

```bash
# npm
npm install
```

```bash
# pnpm
pnpm install
```

```bash
npm run dev
```

```bash
npm run build
```

```bash
npm run preview
```

--------------------------------

### Nuxt Layer Directory Structure Example

Source: https://context7_llms

Demonstrates how to structure a Nuxt application using Nuxt Layers, allowing for modular organization of pages and configurations. This setup is useful for larger projects or when integrating multiple applications.

```bash
-| some-app/
---| nuxt.config.ts
---| pages/
-----| app-page.vue
-| nuxt.config.ts
```

--------------------------------

### Nuxt Module Lifecycle Hooks Example (TypeScript)

Source: https://context7_llms

Demonstrates the use of `onInstall` and `onUpgrade` lifecycle hooks within a Nuxt module for one-time setup and version-specific migrations. It also shows the regular `setup` function for ongoing logic and the use of `addServerHandler`. Dependencies include `nuxt/kit` and `semver`.

```typescript
import { addServerHandler, defineNuxtModule } from 'nuxt/kit'
import semver from 'semver'

export default defineNuxtModule({
  meta: {
    name: 'my-database-module',
    version: '1.0.0',
  },
  async onInstall (nuxt) {
    // One-time setup: create database schema, generate config files, etc.
    await generateDatabaseConfig(nuxt.options.rootDir)
  },
  async onUpgrade (nuxt, options, previousVersion) {
    // Handle version-specific migrations
    if (semver.lt(previousVersion, '1.0.0')) {
      await migrateLegacyData()
    }
  },
  setup (options, nuxt) {
    // Regular setup logic that runs on every build
    addServerHandler({ /* ... */ })
  },
})
```

--------------------------------

### Install Nuxt UI v3 with Nuxt CLI

Source: https://context7_llms

Command to create a new Nuxt project pre-configured with Nuxt UI v3. This is the recommended way to start a new project with Nuxt UI.

```bash
npx nuxi@latest init my-app -t ui
```

--------------------------------

### Nuxt Configuration Example

Source: https://nuxt.com/docs/3.x/directory-structure/public

A basic Nuxt configuration file demonstrating module imports and build settings. This example shows how to include modules like '@nuxt/content' and configure build options such as transpile targets. It serves as a starting point for customizing Nuxt.js projects.

```javascript
export default defineNuxtConfig({
  modules: [
    '@nuxt/content'
  ],
  build: {
    transpile: [
      'vue-instant'
    ]
  }
})
```

--------------------------------

### Implement Module Lifecycle Hooks: onInstall and onUpgrade (TypeScript)

Source: https://context7_llms

This TypeScript example illustrates how to implement `onInstall` and `onUpgrade` lifecycle hooks within a Nuxt module. These hooks allow modules to perform setup or upgrade tasks when first installed or updated, triggered by version information in the module's metadata and tracked internally by Nuxt.

```typescript
export default defineNuxtModule({
  meta: {
    name: 'my-module',
    version: '1.0.0',
  },

  onInstall(nuxt) {
    // This will be run when the module is first installed
    console.log('Setting up my-module for the first time!')
  },

  onUpgrade(inlineOptions, nuxt, previousVersion) {
    // This will be run when the module is upgraded
    console.log(`Upgrading my-module from v${previousVersion}`)
  }
})
```

--------------------------------

### Programmatic Module Installation with Options (TypeScript)

Source: https://context7_llms

Shows how to programmatically install a Nuxt module using the `installModule` function from `@nuxt/kit`. This example demonstrates installing `@nuxtjs/fontaine` with specific configuration options for fonts, including fallbacks. Note that `installModule` is deprecated in favor of `moduleDependencies`.

```typescript
import {
  defineNuxtModule,
  installModule
} from '@nuxt/kit'

export default defineNuxtModule({
  async setup () {
    // will install @nuxtjs/fontaine with Roboto font and Impact fallback
    await installModule('@nuxtjs/fontaine', {
      // module configuration
      fonts: [
        {
          family: 'Roboto',
          fallbacks: ['Impact'],
          fallbackName: 'fallback-a',
        },
      ],
    })
  },
})

```

--------------------------------

### Next.js Boilerplate Setup

Source: https://vercel.com/new

Provides instructions for setting up a Next.js boilerplate project, which includes installing dependencies and starting the development server. It's a starter kit for Next.js and React applications.

```shell
yarn install
npm run dev
```

--------------------------------

### Build and Preview Azure Static Web Apps

Source: https://context7_llms

Commands to build a Nuxt application with the Azure preset and start a local preview using the Azure Static Web Apps CLI. Requires Azure Functions Core Tools to be installed.

```bash
npx nuxi build --preset=azure
npx @azure/static-web-apps-cli start .output/public --api-location .output/server
```

--------------------------------

### Start and Set Progress with useLoadingIndicator in Nuxt.js

Source: https://nuxt.com/docs/3.x/api/composables/use-loading-indicator

Shows how to initialize useLoadingIndicator and then use the start and set methods. The example demonstrates setting the progress to 0 immediately with force: true, and then starting the loading indicator.

```typescript
<script setup lang="ts">
const { start, set } = useLoadingIndicator()
// same as set(0, { force: true })
// set the progress to 0, and show loading immediately
start({ force: true })
</script>
```

--------------------------------

### nuxt preview

Source: https://context7_llms

The `preview` command starts a server to preview your Nuxt application after building. It's an alias for the `start` command.

```APIDOC
## `nuxt preview`

### Description
Starts a server to preview your Nuxt application after running the `build` command. Alias for `start` command.

### Method
CLI Command

### Endpoint
`npx nuxt preview [ROOTDIR]`

### Parameters
#### Path Parameters
- **ROOTDIR** (string) - Optional - Specifies the working directory (default: `.`).

#### Query Parameters
- **--cwd** (string) - Optional - Specify the working directory, takes precedence over ROOTDIR (default: `.`).
- **--logLevel** (string) - Optional - Specify build-time log level (`silent`, `info`, `verbose`).
- **--envName** (string) - Optional - The environment to use when resolving configuration overrides (default is `production` when building, `development` when running the dev server).
- **-e, --extends** (string) - Optional - Extend from a Nuxt layer.
- **-p, --port** (number) - Optional - Port to listen on (use `PORT` environment variable to override).
- **--dotenv** (boolean) - Optional - Path to `.env` file to load, relative to the root directory.

### Request Example
```bash
npx nuxt preview --port 4000 --dotenv
```

### Response
#### Success Response
- **Server**: A local server is started to preview the built Nuxt application.

#### Response Example
(No direct response body, but a server is started and accessible via a local URL.)
```

--------------------------------

### SST Initialization Command

Source: https://context7_llms

Command to initialize SST in a Nuxt project. This command will guide the user through the setup process, including detecting the Nuxt framework.

```bash
npx sst@latest init
```

--------------------------------

### Install and Use Zerops CLI for Deployment

Source: https://context7_llms

This snippet demonstrates how to install the Zerops CLI globally using npm and then log in with an access token. It concludes with the command to trigger the build and deploy pipeline.

```sh
npm i -g @zerops/zcli
```

```sh
zcli login <token>
```

```sh
zcli push
```

--------------------------------

### Nuxt.js Configuration Example

Source: https://nuxt.com/docs/4.x/api/utils/update-app-config

A basic configuration file for a Nuxt.js application. It includes settings for modules, CSS, and plugins, demonstrating a typical setup for a Nuxt project.

```javascript
export default defineNuxtConfig({
  modules: [
    '@nuxtjs/eslint-module',
    '@pinia/nuxt',
    '@vueuse/nuxt',
    '@unhead/vue',
    '@nuxt/content'
  ],
  css: [
    '~/assets/css/main.css'
  ],
  plugins: [
    '~/plugins/i18n.client.ts'
  ],
  devtools: {
    enabled: true
  }
})
```

--------------------------------

### Configure Nuxt for Heroku Deployment

Source: https://context7_llms

This example shows how to configure a Nuxt application for deployment on Heroku. It includes commands to create a Heroku app, set the Node.js buildpack, configure the server preset, and defines the necessary 'build' and 'start' scripts in package.json.

```bash
heroku create myapp
heroku buildpacks:set heroku/nodejs
heroku config:set SERVER_PRESET=heroku
```

```json
{
  "scripts": {
    "build": "nuxt build",
    "start": "node .output/server/index.mjs"
  }
}
```

--------------------------------

### Create React App Build and Development Commands

Source: https://vercel.com/new

Specifies commands for creating and managing React applications using Create React App. Includes commands for installation, building with `react-scripts build`, and starting development with `react-scripts start`. The output directory is 'build'.

```json
{
  "name": "Create React App",
  "slug": "create-react-app",
  "envPrefix": "REACT_APP_",
  "settings": {
    "installCommand": {
      "placeholder": "`yarn install`, `pnpm install`, `npm install`, or `bun install`"
    },
    "buildCommand": {
      "value": "react-scripts build"
    },
    "devCommand": {
      "value": "react-scripts start"
    },
    "outputDirectory": {
      "value": "build"
    }
  }
}
```

--------------------------------

### Install vue-gtag-next using bun

Source: https://context7_llms

Command to install the `vue-gtag-next` package as a development dependency using bun.

```bash
bun add -D vue-gtag-next
```

--------------------------------

### Create Nuxt UI Starter Template

Source: https://ui.nuxt.com/pro/getting-started

Commands to create a new Nuxt project using the official Nuxt UI starter template or specific Nuxt UI templates. This is a quick way to get started with a pre-configured Nuxt UI project.

```bash
npm create nuxt@latest -- -t ui
```

```bash
npm create nuxt@latest -- -t ui/landing
```

```bash
npm create nuxt@latest -- -t ui/docs
```

```bash
npm create nuxt@latest -- -t ui/saas
```

```bash
npm create nuxt@latest -- -t ui/dashboard
```

```bash
npm create nuxt@latest -- -t ui/chat
```

```bash
npm create nuxt@latest -- -t ui/portfolio
```

```bash
npm create nuxt@latest -- -t ui/changelog
```

```bash
npm create nuxt@latest -- -t ui/editor
```

--------------------------------

### Basic Nuxt Page Example

Source: https://nuxt.com/mcp

This snippet demonstrates a simple Nuxt page component. It uses the Vue 3 Composition API with the `<script setup>` syntax for a concise component definition. The page displays a heading and a paragraph, showcasing a basic structure for a Nuxt application page.

```vue
<template>
  <div>
    <h1>Welcome to the Nuxt LLMs Project</h1>
    <p>This is a basic page demonstrating the structure of a Nuxt application.</p>
  </div>
</template>

<script setup>
// No script logic needed for this basic example
</script>

<style scoped>
/* Add any page-specific styles here */
div {
  padding: 20px;
}

h1 {
  color: var(--ui-color-primary-500);
}
</style>
```

--------------------------------

### Start Nuxt Development Server

Source: https://context7_llms

Commands to start the Nuxt development server using various package managers. The '-o' or '--open' flag automatically opens the application in your default browser.

```bash
npm run dev -- -o
```

```bash
yarn dev --open
```

```bash
pnpm dev -o
```

```bash
bun run dev -o

# To use the Bun runtime during development
# bun --bun run dev -o
```

```bash
deno run dev -o
```

--------------------------------

### Install vue-gtag-next using deno

Source: https://context7_llms

Command to install the `vue-gtag-next` package as a development dependency using deno.

```bash
deno add -D npm:vue-gtag-next
```

--------------------------------

### Setup Function Configuration

Source: https://context7_llms

Configuration options for the setup function in Nuxt Test Utils E2E, including build, server, port, host, browser, browserOptions, and runner.

```APIDOC
## Setup Function Configuration

### Description
Configuration options for the `setup` function in Nuxt Test Utils E2E. These options control the testing environment, including whether to build the project, launch a server, specify ports, use a target host, enable browser testing, and configure browser options.

### Method
`setup(options)`

### Parameters
#### Path Parameters
None

#### Query Parameters
None

#### Request Body
- **build** (boolean) - Optional - Whether to run a separate build step. Defaults to `true` (or `false` if `browser` or `server` is disabled, or if a `host` is provided).
- **server** (boolean) - Optional - Whether to launch a server to respond to requests in the test suite. Defaults to `true` (or `false` if a `host` is provided).
- **port** (number | undefined) - Optional - If provided, set the launched test server port to the value. Defaults to `undefined`.
- **host** (string) - Optional - If provided, a URL to use as the test target instead of building and running a new server. Useful for running "real" end-to-end tests against a deployed version of your application, or against an already running local server. Defaults to `undefined`.
- **browser** (boolean) - Optional - If set, a browser will be launched and can be controlled in the subsequent test suite. Defaults to `false`.
- **browserOptions** (object) - Optional - Options for configuring the browser instance.
  - **type** (string) - The type of browser to launch: `chromium`, `firefox`, or `webkit`.
  - **launch** (object) - An object of options that will be passed to Playwright when launching the browser. See [Playwright launch options](https://playwright.dev/docs/api/class-browsertype#browser-type-launch).
- **runner** ('vitest' | 'jest' | 'cucumber') - Optional - Specify the runner for the test suite. Defaults to `'vitest'`.

### Request Example
```json
{
  "build": true,
  "server": true,
  "port": 8080,
  "host": "http://localhost:3000",
  "browser": true,
  "browserOptions": {
    "type": "chromium",
    "launch": {
      "headless": false
    }
  },
  "runner": "vitest"
}
```

### Response
#### Success Response (200)
This function typically does not return a value but sets up the testing environment.

#### Response Example
N/A
```

--------------------------------

### Define and Install Nuxt Module with Fontaine

Source: https://nuxt.com/docs/3.x/api/kit/modules

This example demonstrates how to define a Nuxt module using `defineNuxtModule` and then install another module, `@nuxtjs/fontaine`, with specific font configurations. It shows how to set up font families, fallbacks, and configuration options within the Nuxt module lifecycle.

```javascript
import { defineNuxtModule, installModule } from '@nuxt/kit'

export default defineNuxtModule({
  async setup (options, nuxt) {
    // will install @nuxtjs/fontaine with Roboto font and Impact fallback
    await installModule('@nuxtjs/fontaine', {
      // module configuration
      fonts: [
        {
          family: 'Roboto',
          fallbacks: ['Impact'],
          fallbackName: 'fallback-a',
        },
      ],
    })
  },
})
```

--------------------------------

### Route Rules Configuration Example (Nuxt Config)

Source: https://context7_llms

Provides an equivalent configuration for the defineRouteRules example, showing how to set the 'prerender: true' rule for the root path ('/') within the nuxt.config.ts file.

```typescript
export default defineNuxtConfig({
  routeRules: {
    '/': { prerender: true },
  },
})
```

--------------------------------

### Nuxt Tree Shaking Client Configuration Example

Source: https://context7_llms

Provides an example of configuring tree shaking for client builds in Nuxt. This allows specific composables to be excluded from client-side bundles for optimization.

```javascript
treeShake: { client: { myPackage: ['useServerOnlyComposable'] } }
```

--------------------------------

### Local Development Setup for Tailwind CSS Module

Source: https://nuxt.com/modules/tailwindcss

Instructions for setting up the Tailwind CSS module locally for development. This involves cloning the repository, installing dependencies, preparing for development, and starting the development server.

```bash
Clone this repository
Install dependencies using pnpm i
Prepare for development using pnpm dev:prepare
Start development server using pnpm dev

```

--------------------------------

### POST /setup

Source: https://context7_llms

Sets up the Nuxt test environment with the provided configuration.

```APIDOC
## POST /setup

### Description
Sets up the Nuxt test environment with the provided configuration.

### Method
POST

### Endpoint
/setup

### Parameters
#### Request Body
- **build** (boolean) - Optional - Whether to run a separate build step.
- **server** (boolean) - Optional - Whether to launch a server to respond to requests in the test suite.
- **port** (number | undefined) - Optional - If provided, set the launched test server port to the value.
- **host** (string) - Optional - If provided, a URL to use as the test target instead of building and running a new server.
- **browser** (boolean) - Optional - If set, a browser will be launched and can be controlled in the subsequent test suite.
- **browserOptions** (object) - Optional - Options for configuring the browser launch.
  - **type** (string) - The type of browser to launch - either `chromium`, `firefox` or `webkit`.
  - **launch** (object) - Object of options that will be passed to playwright when launching the browser.
- **runner** ('vitest' | 'jest' | 'cucumber') - Optional - Specify the runner for the test suite.

### Request Example
```json
{
  "build": true,
  "server": true,
  "port": 8080,
  "host": "http://localhost:8787",
  "browser": false,
  "browserOptions": {
    "type": "chromium",
    "launch": {}
  },
  "runner": "vitest"
}
```

### Response
#### Success Response (200)
- **message** (string) - A success message indicating the setup is complete.
```

--------------------------------

### Define Build and Start Scripts in package.json

Source: https://context7_llms

Defines the commands to build and start the Nuxt application for production. These scripts are essential for deployment platforms to correctly build and run the application.

```json
{
  "scripts": {
      "build": "nuxt build",
      "start": "node .output/server/index.mjs"
  }
}
```

--------------------------------

### Install and Run Nuxt Hub Project (Bash)

Source: https://nuxt.com/modules/hub

This snippet outlines the essential bash commands for setting up and running the Nuxt Hub project. It covers dependency installation, preparing for development, running the development server, building the project, and executing linting and testing commands.

```bash
# Install dependencies
pnpm i

# Generate type stubs
pnpm dev:prepare

# Develop with the playground
pnpm dev

# Build the playground
pnpm dev:build

# Run ESLint
pnpm lint

# Run Vitest
pnpm test
pnpm test:watch

```

--------------------------------

### Target Host End-to-End Example

Source: https://nuxt.com/docs/4.x/getting-started/testing

Example demonstrating how to use a target host URL for end-to-end tests, which can be faster than building a new server.

```APIDOC
## Target `host` end-to-end example

### Description
A common use-case for end-to-end testing is running the tests against a deployed application running in the same environment typically used for Production. For local development or automated deploy pipelines, testing against a separate local server can be more efficient and is typically faster than allowing the test framework to rebuild between tests.

### Usage
To utilize a separate target host for end-to-end tests, simply provide the `host` property of the `setup` function with the desired URL.

### Code Example
```javascript
import { createPage, setup } from '@nuxt/test-utils/e2e'
import { describe, expect, it } from 'vitest'

describe('login page', async () => {
  await setup({
    host: 'http://localhost:8787',
  })

  it('displays the email and password fields', async () => {
    const page = await createPage('/login')
    expect(await page.getByTestId('email').isVisible()).toBe(true)
    expect(await page.getByTestId('password').isVisible()).toBe(true)
  })
})
```
```

--------------------------------

### E2E Test Execution with Nuxt Test Utils (TypeScript)

Source: https://nuxt.com/docs/4.x/guide/modules/testing

Demonstrates how to write end-to-end tests for a Nuxt module using `@nuxt/test-utils`. It shows the setup process, fetching page content, and asserting expected HTML content within the fixture. This example focuses on testing SSR.

```typescript
import { describe, expect, it } from 'vitest'
import { fileURLToPath } from 'node:url'
import { $fetch, setup } from '@nuxt/test-utils/e2e'

describe('ssr', async () => {
  // 2. Setup Nuxt with this fixture inside your test file
  await setup({
    rootDir: fileURLToPath(new URL('./fixtures/ssr', import.meta.url)),
  })

  it('renders the index page', async () => {
    // 3. Interact with the fixture using utilities from `@nuxt/test-utils`
    const html = await $fetch('/')

    // 4. Perform checks related to this fixture
    expect(html).toContain('<div>ssr</div>')
  })
})

describe('csr', async () => { /* ... */ })
```

--------------------------------

### Nuxt Modules Configuration Example

Source: https://context7_llms

Demonstrates how to configure Nuxt modules, including using package names, local paths, options, and inline functions. Modules are executed sequentially, and their order is important.

```javascript
modules: [
  // Using package name
  '@nuxtjs/axios',
  // Relative to your project srcDir
  '~/modules/awesome.js',
  // Providing options
  ['@nuxtjs/google-analytics', { ua: 'X1234567' }],
  // Inline definition
  function () {}
]
```

--------------------------------

### Nuxt Module Directory Structure Example (Bash)

Source: https://context7_llms

Illustrates how to structure local modules within the `modules/` directory to control their loading order. Prefixes are used to ensure specific modules are loaded first.

```bash
modules/
  1.first-module/
    index.ts
  2.second-module.ts
```

--------------------------------

### Install Dependencies for Remote Git Layer

Source: https://nuxt.com/docs/3.x/guide/going-further/layers

Example of how to configure a remote Git layer to automatically install its npm dependencies. This is done by specifying `install: true` within the layer options.

```typescript
export default defineNuxtConfig({
  extends: [
    ['github:username/repoName', { install: true }],
  ],
})
```

--------------------------------

### Preview Nuxt Application Build (Bash)

Source: https://context7_llms

The `npx nuxt preview` command starts a server to preview your Nuxt application after a build. It's an alias for the `start` command and is intended for production use. Options include specifying the root directory, working directory, log level, environment name, extending layers, port, and dotenv files.

```bash
npx nuxt preview [ROOTDIR] [--cwd=<directory>] [--logLevel=<silent|info|verbose>] [--envName] [-e, --extends=<layer-name>] [-p, --port] [--dotenv]
```

--------------------------------

### defineNuxtModule

Source: https://context7_llms

Defines a Nuxt module, merging defaults, installing hooks, and providing a setup function for customization.

```APIDOC
## `defineNuxtModule`

### Description
Define a Nuxt module, automatically merging defaults with user provided options, installing any hooks that are provided, and calling an optional setup function for full control.

### Method
Not Applicable (This is a function definition, not an HTTP endpoint)

### Endpoint
Not Applicable

### Parameters
This function accepts an optional `definition` object which can include:
- `meta` (object): Metadata for the module, including `name` and `configKey`.
- `defaults` (object): Default options for the module.
- `setup` (function): An optional function to run when the module is set up.

### Request Example
```ts
import { defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  meta: {
    name: 'my-module',
    configKey: 'myModule',
  },
  defaults: {
    enabled: true,
  },
  setup (options) {
    if (options.enabled) {
      console.log('My Nuxt module is enabled!')
    }
  },
})
```

### Response
This function returns a `NuxtModule` type.

#### Success Response
Not Applicable (This is a function definition)

#### Response Example
Not Applicable
```

--------------------------------

### Example of Rendering Nuxt.js Icon in a Custom Component

Source: https://nuxt.com/modules/icon

Illustrates a complete example of creating a custom component (`MyIcon`) that renders the Nuxt.js Icon component. This example uses `<script setup>` and the `h` function for creating the icon element.

```vue
<script setup>
import { Icon } from '#components'
import { h } from 'vue'

const MyIcon = h(Icon, { name: 'uil:twitter' })
</script>

<template>
 <p><MyIcon /></p>
</template>
```

--------------------------------

### Install vue-gtag-next with Package Managers

Source: https://context7_llms

Provides commands for installing the `vue-gtag-next` package using various package managers including npm, yarn, pnpm, bun, and deno.

```bash
npm install --save-dev vue-gtag-next
```

```bash
yarn add --dev vue-gtag-next
```

```bash
pnpm add -D vue-gtag-next
```

```bash
bun add -D vue-gtag-next
```

```bash
deno add -D npm:vue-gtag-next
```

--------------------------------

### GET /api/user/stats

Source: https://context7_llms

An example of a protected API route that requires user authentication. It ensures that only logged-in users can access this endpoint.

```APIDOC
## GET /api/user/stats

### Description
An example of a protected API route that requires user authentication. It ensures that only logged-in users can access this endpoint.

### Method
GET

### Endpoint
/api/user/stats

### Parameters
None

### Request Example
(No request body needed for this GET request)

### Response
#### Success Response (200)
Returns an empty object. In a real-world scenario, this would contain user-specific statistics.

#### Error Response (401)
Returned if the request does not come from a valid user session.

#### Response Example
```json
{}
```
```

--------------------------------

### Debug Module Setup Times in Nuxt

Source: https://context7_llms

This command enables detailed debugging output for Nuxt development, specifically logging the setup time for each module. This helps identify performance bottlenecks by showing how long each module takes to initialize, aiding in optimization efforts.

```sh
DEBUG=1 npx nuxt dev
```

--------------------------------

### Minimal Nuxt.js package.json Example

Source: https://nuxt.com/docs/3.x/directory-structure/package

This is a basic package.json file for a Nuxt.js application. It includes essential dependencies like Nuxt, Vue, and Vue Router, along with common scripts for building, developing, generating, and previewing the application. The 'postinstall' script is crucial for preparing the Nuxt environment after installation.

```json
{
  "name": "nuxt-app",
  "private": true,
  "type": "module",
  "scripts": {
    "build": "nuxt build",
    "dev": "nuxt dev",
    "generate": "nuxt generate",
    "preview": "nuxt preview",
    "postinstall": "nuxt prepare"
  },
  "dependencies": {
    "nuxt": "latest",
    "vue": "latest",
    "vue-router": "latest"
  }
}
```

--------------------------------

### SolidStart (v1) Build and Development Commands

Source: https://vercel.com/new

Specifies the commands for building and developing a SolidStart v1 application. It leverages Vite for building and Vinxi for development, with the output typically going to a '.output' directory.

```bash
npm install
or
pnpm install
or
npm install
or
bun install

vinxi build

vinxi dev
```

--------------------------------

### installModule

Source: https://nuxt.com/docs/4.x/api/kit/modules

Installs another Nuxt module within the current module's setup.

```APIDOC
## installModule

### Description
Installs another Nuxt module programmatically. This is useful for creating meta-modules or composing modules.

### Method
`installModule`

### Parameters
#### Module Name
- **name** (string) - Required - The name of the module to install (e.g., '@nuxtjs/axios').

#### Options
- **options** (object) - Optional - Configuration options for the module being installed.

### Request Example
```javascript
import { defineNuxtModule, installModule } from '@nuxt/kit'

export default defineNuxtModule({
  setup (options, nuxt) {
    await installModule('@nuxtjs/fontaine', {
      fonts: [
        {
          family: 'Roboto',
          fallbacks: ['Impact'],
          fallbackName: 'fallback-a'
        }
      ]
    })
  }
})
```

### Response
#### Success Response
Successfully installs the specified module.

#### Response Example
(No direct response body, module installation is a side effect.)
```

--------------------------------

### Programmatically Install Module in Nuxt.js (Deprecated)

Source: https://nuxt.com/docs/4.x/api/kit/modules

Installs a specified Nuxt module programmatically using the `installModule` function. This is useful when your module depends on other modules. The function accepts the module to install and optional inline options for its setup function. Note: This method is deprecated and `moduleDependencies` should be used instead.

```javascript
import { defineNuxtModule, installModule } from '@nuxt/kit'
export default defineNuxtModule({
  async setup () {
    // will install @nuxtjs/fontaine with Roboto font and Impact fallback
    await installModule('@nuxtjs/fontaine', {
      // module configuration
      fonts: [
        {
          family: 'Roboto',
          fallbacks: ['Impact'],
          fallbackName: 'fallback-a',
        },
      ],
    })
  },
})
```

--------------------------------

### Docusaurus (v2) Build and Development Commands

Source: https://vercel.com/new

Provides commands for building and starting a Docusaurus v2 static documentation site. It utilizes npm or yarn for installation and Docusaurus CLI for development and build processes. The output is directed to a 'build' directory.

```bash
npm install
or
yarn install

npm run build
or
docusaurus build

docusaurus start --port $PORT
```

--------------------------------

### Install vue-gtag-next using npm

Source: https://context7_llms

Command to install the `vue-gtag-next` package as a development dependency using npm.

```bash
npm install --save-dev vue-gtag-next
```

--------------------------------

### Nuxt Project Structure Example

Source: https://context7_llms

Illustrates the default directory structure for a Nuxt 4 project, with application code organized under the 'app/' directory. This structure enhances file watcher performance and provides better IDE context for client/server code.

```bash
my-nuxt-app/
├─ app/
│  ├─ assets/
│  ├─ components/
│  ├─ composables/
│  ├─ layouts/
│  ├─ middleware/
│  ├─ pages/
│  ├─ plugins/
│  ├─ utils/
│  ├─ app.vue
│  ├─ app.config.ts
│  └─ error.vue
├─ content/
├─ public/
├─ shared/
├─ server/
└─ nuxt.config.ts
```

--------------------------------

### Utilize Lifecycle Hooks for Nuxt Module Installation and Upgrade

Source: https://context7_llms

Implement `onInstall` and `onUpgrade` lifecycle hooks in your Nuxt module to perform one-time setup or version-specific tasks. These hooks require `meta.name` and `meta.version` to be defined and run before the main `setup` function.

```typescript
import { defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  meta: {
    name: 'my-module',
    version: '1.0.0', // Required for lifecycle hooks
    // configKey: 'myModule',
  },
  defaults: {
    enabled: true,
  },
  setup (options) {
    // Main module setup
  },
  onInstall () {
    // Runs once when the module is first installed
    console.log('Module installed!')
  },
  onUpgrade () {
    // Runs when the module version increases
    console.log('Module upgraded!')
  },
})
```

--------------------------------

### ESLint Legacy Configuration Example

Source: https://context7_llms

An example of a legacy ESLint configuration file (.eslintrc). This format uses the 'extends' property to include shared configurations and plugins, which can sometimes lead to complex resolution paths.

```jsonc
{
  "extends": [
    "@nuxtjs",
    "plugin:vue/vue3-recommended"
  ],
  "rules": {
    "// ..."
  }
}
```

--------------------------------

### Nuxt MCP Setup - Claude Desktop

Source: https://context7_llms

Instructions for setting up the Nuxt MCP server in Claude Desktop by modifying the configuration file.

```APIDOC
## Nuxt MCP Setup - Claude Desktop

### Description
Configure the Nuxt MCP server for Claude Desktop by editing the `claude_desktop_config.json` file.

### Steps

1. Open Claude Desktop and navigate to "Settings" > "Developer".
2. Click on "Edit Config" to open the local Claude directory.
3. Modify the `claude_desktop_config.json` file with the following configuration:

   ```json
   {
     "mcpServers": {
       "nuxt": {
         "command": "npx",
         "args": [
           "mcp-remote",
           "https://nuxt.com/mcp"
         ]
       }
     }
   }
   ```
4. Restart the Claude Desktop app.
```

--------------------------------

### FastHTML Installation Command

Source: https://vercel.com/new

Basic installation command for FastHTML, a library for Starlette-powered web applications.

```Shell
pip install
```

--------------------------------

### Basic Nuxt Page Example

Source: https://nuxt.com/docs/3.x/api/commands/dev

A simple Nuxt.js page component that displays a heading and a paragraph. This example demonstrates the basic structure of a Nuxt page and can be used as a starting point for building more complex interfaces.

```vue
<template>
  <div>
    <h1>Welcome to the Nuxt LLMs Project</h1>
    <p>This is a basic page demonstrating Nuxt.js functionality.</p>
  </div>
</template>

<script setup>
// Script setup for Nuxt 3
</script>

<style scoped>
/* Component-specific styles */
h1 {
  color: var(--ui-color-primary-500);
}
</style>
```

--------------------------------

### Install vue-gtag-next using pnpm

Source: https://context7_llms

Command to install the `vue-gtag-next` package as a development dependency using pnpm.

```bash
pnpm add -D vue-gtag-next
```

--------------------------------

### Define a Nuxt Module with Options and Setup

Source: https://nuxt.com/docs/3.x/api/kit/modules

Defines a Nuxt module using `defineNuxtModule`. It merges default options with user-provided ones, installs hooks, and executes a setup function. This is the primary way to create reusable Nuxt modules.

```javascript
import { defineNuxtModule } from '@nuxt/kit'

export default defineNuxtModule({
  meta: {
    name: 'my-module',
    configKey: 'myModule',
  },
  defaults: {
    enabled: true,
  },
  setup (options) {
    if (options.enabled) {
      console.log('My Nuxt module is enabled!')
    }
  },
})
```

--------------------------------

### Nuxt Plugin Registration Order Example

Source: https://context7_llms

Shows how to control the order of plugin execution in Nuxt by prefixing filenames with numerical strings. This ensures that plugins depending on others are loaded in the correct sequence, preventing potential runtime errors.

```bash
plugins/
 | - 01.myPlugin.ts
 | - 02.myOtherPlugin.ts
```

--------------------------------

### Nuxt navigateTo: Parameter Examples

Source: https://context7_llms

Provides examples of using the 'to' parameter with Nuxt.js's navigateTo function. It demonstrates redirecting to a path string, a named route, and a named route with parameters.

```typescript
// Passing the URL directly will redirect to the '/blog' page
await navigateTo('/blog')

// Using the route object, will redirect to the route with the name 'blog'
await navigateTo({ name: 'blog' })

// Redirects to the 'product' route while passing a parameter (id = 1) using the route object.
await navigateTo({ name: 'product', params: { id: 1 } })
```

--------------------------------

### Initialize Firebase Project with CLI

Source: https://context7_llms

These commands guide you through setting up your Nuxt.js project for Firebase deployment using the Firebase CLI. It includes logging in, initializing Firebase hosting, and configuring the public directory and rewrites for server rendering.

```bash
npm install -g firebase-tools@latest
firebase login
firebase init hosting
```

--------------------------------

### Install nuxt-auth-utils Module

Source: https://context7_llms

This command installs the `nuxt-auth-utils` module as a project dependency and automatically adds it to the `modules` array in your `nuxt.config.ts` file, preparing your Nuxt application for session management and authentication features.

```bash
npx nuxt module add auth-utils
```

--------------------------------

### Install and Use Vue-Gtag Plugin in Nuxt

Source: https://nuxt.com/docs/3.x/directory-structure/plugins

This example demonstrates how to integrate a Vue.js plugin (vue-gtag-next) into a Nuxt application using a Nuxt plugin. It includes installation commands for various package managers and the Nuxt plugin code to initialize the Vue plugin and track the router.

```bash
npm install --save-dev vue-gtag-next
```

```bash
yarn add --dev vue-gtag-next
```

```bash
pnpm add -D vue-gtag-next
```

```bash
bun add -D vue-gtag-next
```

```bash
deno add -D npm:vue-gtag-next
```

```typescript
import VueGtag, { trackRouter } from 'vue-gtag-next'

export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.vueApp.use(VueGtag, {
    property: {
      id: 'GA_MEASUREMENT_ID',
    },
  })

  trackRouter(useRouter())
})
```

--------------------------------

### nuxt prepare

Source: https://context7_llms

The `prepare` command generates types and creates a `.nuxt` directory, useful for CI or postinstall scripts.

```APIDOC
## `nuxt prepare`

### Description
Generates types and creates a `.nuxt` directory. Useful in CI environments or as a `postinstall` command.

### Method
CLI Command

### Endpoint
`npx nuxt prepare [ROOTDIR]`

### Parameters
#### Path Parameters
- **ROOTDIR** (string) - Optional - Specifies the working directory (default: `.`).

#### Query Parameters
- **--dotenv** (boolean) - Optional - Path to `.env` file to load, relative to the root directory.
- **--cwd** (string) - Optional - Specify the working directory, takes precedence over ROOTDIR (default: `.`).
- **--logLevel** (string) - Optional - Specify build-time log level (`silent`, `info`, `verbose`).
- **--envName** (string) - Optional - The environment to use when resolving configuration overrides (default is `production` when building, `development` when running the dev server).
- **-e, --extends** (string) - Optional - Extend from a Nuxt layer.

### Request Example
```bash
npx nuxt prepare --cwd ./my-app --logLevel verbose
```

### Response
#### Success Response
- **Output**: Creates a `.nuxt` directory and generates necessary types.

#### Response Example
(No direct response body, but file system changes occur.)
```

--------------------------------

### Install Module Programmatically (Deprecated)

Source: https://nuxt.com/docs/3.x/api/kit/modules

Programmatically install a specified Nuxt module using the `installModule` function. This is useful when your module depends on other modules. Options can be passed to the module's `setup` function via `inlineOptions`. Note: This function is deprecated and `moduleDependencies` is recommended.

```APIDOC
## Install Module Programmatically (Deprecated)

### Description
Install specified Nuxt module programmatically. This is helpful when your module depends on other modules. You can pass the module options as an object to `inlineOptions` and they will be passed to the module's `setup` function. **Deprecated:** Use the [`moduleDependencies`](#specifying-module-dependencies) option in `defineNuxtModule` instead.

### Method
`installModule`

### Endpoint
N/A (Function within Nuxt context)

### Parameters
#### Path Parameters
None

#### Query Parameters
None

#### Request Body
- **moduleToInstall** (string | NuxtModule) - Required - The module to install. Can be either a string with the module name or a module object itself.
- **inlineOptions** (any) - Optional - An object with the module options to be passed to the module's `setup` function.
- **nuxt** (Nuxt) - Optional - Nuxt instance. If not provided, it will be retrieved from the context via `useNuxt()` call.

### Request Example
```javascript
import { defineNuxtModule, installModule } from '@nuxt/kit'

export default defineNuxtModule({
  async setup () {
    // will install @nuxtjs/fontaine with Roboto font and Impact fallback
    await installModule('@nuxtjs/fontaine', {
      // module configuration
      fonts: [
        {
          family: 'Roboto',
          fallbacks: ['Impact'],
          fallbackName: 'fallback-a',
        },
      ],
    })
  },
})
```

### Response
#### Success Response (200)
N/A (This is a function call, not an HTTP response)

#### Response Example
N/A
```

--------------------------------

### Nuxt Example: State Management

Source: https://context7_llms

Shows an example of state management in Nuxt, potentially using the useState composable for shared state across components.

```vue
<template>
  <div>
    <p>Count: {{ count }}</p>
    <button @click="increment">Increment</button>
  </div>
</template>

<script setup>
const count = useState('count', () => 0);
const increment = () => {
  count.value++;
};
</script>
```