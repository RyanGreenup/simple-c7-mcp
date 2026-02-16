### Install Auth.js for Qwik

Source: https://authjs.dev/getting-started/installation

Installs the Auth.js integration for Qwik using npm, pnpm, yarn, or bun.

```bash
npm run qwik add auth
```

```bash
pnpm run qwik add auth
```

```bash
yarn qwik add auth
```

```bash
bun run qwik add auth
```

--------------------------------

### Install Auth.js for Express

Source: https://authjs.dev/getting-started/installation

Installs the Auth.js integration for Express using npm, pnpm, yarn, or bun.

```bash
npm install @auth/express
```

```bash
pnpm add @auth/express
```

```bash
yarn add @auth/express
```

```bash
bun add @auth/express
```

--------------------------------

### Install Auth.js for SvelteKit

Source: https://authjs.dev/getting-started/installation

Installs the Auth.js integration for SvelteKit using npm, pnpm, yarn, or bun.

```bash
npm install @auth/sveltekit
```

```bash
pnpm add @auth/sveltekit
```

```bash
yarn add @auth/sveltekit
```

```bash
bun add @auth/sveltekit
```

--------------------------------

### Install Auth.js for Next.js

Source: https://authjs.dev/getting-started/installation

Installs the Auth.js beta package for Next.js using npm, pnpm, yarn, or bun.

```bash
npm install next-auth@beta
```

```bash
pnpm add next-auth@beta
```

```bash
yarn add next-auth@beta
```

```bash
bun add next-auth@beta
```

--------------------------------

### Auth.js Basic Configuration for Next.js

Source: https://authjs.dev/getting-started/installation_framework=SvelteKit

Sets up the basic Auth.js configuration file (`auth.ts`) for Next.js. This file initializes Auth.js with an empty array of providers and exports necessary handlers.

```typescript
import NextAuth from "next-auth"

export const { handlers, signIn, signOut, auth } = NextAuth({
  providers: [],
})
```

--------------------------------

### Auth.js Basic Configuration for SvelteKit

Source: https://authjs.dev/getting-started/installation_framework=SvelteKit

Sets up the basic Auth.js configuration file (`auth.ts`) for SvelteKit. This file initializes SvelteKitAuth with an empty array of providers and exports the `handle` method.

```typescript
import { SvelteKitAuth } from "@auth/sveltekit"

export const { handle } = SvelteKitAuth({
  providers: [],
})
```

--------------------------------

### Configure Auth.js in Qwik

Source: https://authjs.dev/getting-started/installation_framework=Next

Sets up the Auth.js plugin (`plugin@auth.ts`) for Qwik applications. This involves importing QwikAuth$ and configuring providers within the plugin.

```typescript
import { QwikAuth$ } from "@auth/qwik"

export const { onRequest, useSession, useSignIn, useSignOut } = QwikAuth$(
  () => ({
    providers: [...],
  })
)
```

--------------------------------

### Clone Next.js Example App

Source: https://authjs.dev/guides/configuring-resend

Clones the official Auth.js Next.js example repository to start the setup. This command is used to quickly get a project with Auth.js pre-installed.

```bash
git clone https://github.com/nextauthjs/next-auth-example.git && cd next-auth-example
```

--------------------------------

### Configure Auth.js in Qwik

Source: https://authjs.dev/getting-started/installation

Sets up the Auth.js configuration for Qwik by creating a `plugin@auth.ts` file. It exports necessary functions for request handling and session management.

```typescript
import { QwikAuth$ } from "@auth/qwik"
 
export const { onRequest, useSession, useSignIn, useSignOut } = QwikAuth$(
  () => ({
    providers: [...],
  })
)
```

--------------------------------

### Qwik Auth.js Configuration with OneLogin

Source: https://authjs.dev/getting-started/providers/onelogin

Shows the setup for the OneLogin provider in a Qwik application using Auth.js. This example illustrates how to integrate the provider using QwikAuth$ and its configuration options.

```typescript
import { QwikAuth$ } from "@auth/qwik"
import OneLogin from "@auth/qwik/providers/onelogin"
 
export const {onRequest, useSession, useSignIn, useSignOut} = QwikAuth$(
  () => ({
    providers: [OneLogin],
  })
)
```

--------------------------------

### SvelteKit Auth.js Configuration

Source: https://authjs.dev/getting-started/installation_framework=Qwik

Sets up the core Auth.js configuration for SvelteKit by creating an `auth.ts` file. It initializes SvelteKitAuth with an empty providers array and exports the `handle` function.

```typescript
import { SvelteKitAuth } from "@auth/sveltekit"
 
export const { handle } = SvelteKitAuth({
  providers: [],
})
```

--------------------------------

### Auth.js v5 Configuration File Example

Source: https://authjs.dev/guides/upgrade-to-v5

Example of a new Auth.js v5 configuration file located at the root of the repository. It sets up providers like GitHub and Google and exports necessary authentication methods.

```typescript
import NextAuth from "next-auth"
import GitHub from "next-auth/providers/github"
import Google from "next-auth/providers/google"
 
export const { auth, handlers, signIn, signOut } = NextAuth({
  providers: [GitHub, Google],
})

```

--------------------------------

### Next.js Auth.js Configuration

Source: https://authjs.dev/getting-started/installation_framework=Qwik

Sets up the core Auth.js configuration in Next.js by creating an `auth.ts` file. It initializes NextAuth with an empty providers array and exports necessary handlers for authentication.

```typescript
import NextAuth from "next-auth"
 
export const { handlers, signIn, signOut, auth } = NextAuth({
  providers: [],
})
```

--------------------------------

### Install NextAuth.js v5 Beta

Source: https://authjs.dev/guides/upgrade-to-v5

Commands to install the beta version of next-auth v5 using different package managers (npm, pnpm, yarn, bun).

```bash
npm install next-auth@beta

```

```bash
pnpm add next-auth@beta

```

```bash
yarn add next-auth@beta

```

```bash
bun add next-auth@beta

```

--------------------------------

### Configure Auth.js in Next.js

Source: https://authjs.dev/getting-started/installation_framework=Next

Sets up the Auth.js configuration file (`auth.ts`) and the route handler (`[...nextauth]/route.ts`) for Next.js. This involves importing NextAuth and defining providers.

```typescript
import NextAuth from "next-auth"

export const { handlers, signIn, signOut, auth } = NextAuth({
  providers: [],
})
```

```typescript
import { handlers } from "@/auth" // Referring to the auth.ts we just created
export const { GET, POST } = handlers
```

--------------------------------

### Eventbrite Provider Setup

Source: https://authjs.dev/reference/core/providers/eventbrite

Instructions and code examples for setting up the Eventbrite provider in your Auth.js application.

```APIDOC
## Eventbrite Provider Configuration

### Description
Integrates Eventbrite login into your application using Auth.js. This involves setting up callback URLs and configuring client credentials.

### Setup
#### Callback URL
`https://example.com/api/auth/callback/eventbrite`

#### Configuration
```javascript
import { Auth } from "@auth/core"
import Eventbrite from "@auth/core/providers/eventbrite"
 
const request = new Request(origin)
const response = await Auth(request, {
  providers: [
    Eventbrite({
      clientId: EVENTBRITE_CLIENT_ID,
      clientSecret: EVENTBRITE_CLIENT_SECRET
    })
  ],
})
```

### Resources
- Eventbrite OAuth documentation
- Eventbrite App Management
- Learn more about OAuth
- Source code

### Notes
Auth.js assumes the Eventbrite provider follows the OAuth 2.0 specification. Customizing the default OAuth provider configuration is possible. Auth.js adheres strictly to the specification; deviations by the provider may not be supported.
```

--------------------------------

### Qwik Auth.js Plugin Configuration

Source: https://authjs.dev/getting-started/installation_framework=Express

Configures the Auth.js plugin for Qwik by creating a `plugin@auth.ts` file. This sets up the necessary authentication providers and exports hooks for session management.

```typescript
import { QwikAuth$ } from "@auth/qwik"
 
export const {onRequest, useSession, useSignIn, useSignOut } = QwikAuth$(
  () => ({
    providers: [...],
  })
)
```

--------------------------------

### Install Passkey Peer Dependencies

Source: https://authjs.dev/getting-started/providers/passkey

Installs the necessary peer dependencies for the Passkey provider. The @simplewebauthn/browser is only required for custom sign-in pages.

```bash
npm install @simplewebauthn/browser@9.0.1 @simplewebauthn/server@9.0.3
```

```bash
pnpm add @simplewebauthn/browser@9.0.1 @simplewebauthn/server@9.0.3
```

```bash
yarn add @simplewebauthn/browser@9.0.1 @simplewebauthn/server@9.0.3
```

```bash
bun add @simplewebauthn/browser@9.0.1 @simplewebauthn/server@9.0.3
```

--------------------------------

### Configure Auth.js in Next.js

Source: https://authjs.dev/getting-started/installation

Sets up the basic Auth.js configuration file (`auth.ts`) and the Next.js App Router Route Handler for authentication. This includes exporting handlers for NextAuth.

```typescript
import NextAuth from "next-auth"
 
export const { handlers, signIn, signOut, auth } = NextAuth({
  providers: [],
})
```

```typescript
import { handlers } from "@/auth" // Referring to the auth.ts we just created
export const { GET, POST } = handlers
```

--------------------------------

### WebAuthn Provider Setup Example

Source: https://authjs.dev/reference/core/providers/webauthn

Demonstrates how to set up the WebAuthn provider within an Auth.js application. This example shows importing the provider and integrating it into the Auth configuration, initiating the authentication flow.

```javascript
import { Auth } from "@auth/core"
import WebAuthn from "@auth/core/providers/webauthn"
 
const request = new Request(origin)
const response = await Auth(request, {
  providers: [WebAuthn],
})

```

--------------------------------

### Callback URL Examples for Zitadel Provider

Source: https://authjs.dev/getting-started/providers/zitadel

These are example callback URLs for the Zitadel provider. Ensure your callback URL in the Zitadel console matches one of these patterns, depending on your framework and deployment.

```plaintext
https://example.com/api/auth/callback/zitadel
```

```plaintext
https://example.com/auth/callback/zitadel
```

```plaintext
https://example.com/auth/callback/zitadel
```

--------------------------------

### Configure Auth.js in SvelteKit

Source: https://authjs.dev/getting-started/installation_framework=Next

Sets up the Auth.js configuration file (`auth.ts`) and integrates it with SvelteKit's server hooks (`hooks.server.ts`). This allows accessing session data within server load functions.

```typescript
import { SvelteKitAuth } from "@auth/sveltekit"

export const { handle } = SvelteKitAuth({
  providers: [],
})
```

```typescript
export { handle } from "./auth"
```

```typescript
import type { LayoutServerLoad } from "./$types"

export const load: LayoutServerLoad = async (event) => {
  const session = await event.locals.auth()

  return {
    session,
  }
}
```

--------------------------------

### Asgardeo Provider Setup

Source: https://authjs.dev/reference/core/providers/asgardeo

Configuration and setup guide for the Asgardeo OAuth provider in Auth.js.

```APIDOC
## Setup

### Callback URL
```
https://example.com/api/auth/callback/asgardeo
```

### Configuration
```javascript
import { Auth } from "@auth/core"
import Asgardeo from "@auth/core/providers/asgardeo";

const request = new Request(origin)
const response = await Auth(request, {
  providers: [
    Asgardeo({
      clientId: ASGARDEO_CLIENT_ID,
      clientSecret: ASGARDEO_CLIENT_SECRET,
      issuer: ASGARDEO_ISSUER,
    }),
  ],
})
```

### Configuring Asgardeo

1.  Log into the Asgardeo console.
2.  Go to the “Application” tab.
3.  Register a standard-based, Open ID connect, application.
4.  Add the **callback URLs**: `http://localhost:3000/api/auth/callback/asgardeo` (development) and `https://{YOUR_DOMAIN}.com/api/auth/callback/asgardeo` (production).
5.  After registering the application, go to the “Protocol” tab.
6.  Check `code` as the grant type.
7.  Add “Authorized redirect URLs” & “Allowed origins fields”.
8.  Make Email, First Name, Photo URL user attributes mandatory from the console.

Then, create a `.env` file in the project root and add the following entries:

```
ASGARDEO_CLIENT_ID="Copy client ID from protocol tab here"
ASGARDEO_CLIENT_SECRET="Copy client from protocol tab here"
ASGARDEO_ISSUER="Copy the issuer url from the info tab here"
```
```

--------------------------------

### Configure Auth.js in SvelteKit

Source: https://authjs.dev/getting-started/installation

Configures Auth.js for SvelteKit by creating an `auth.ts` file and re-exporting the `handle` method in `hooks.server.ts`. This makes the `auth()` method available in server load functions.

```typescript
import { SvelteKitAuth } from "@auth/sveltekit"
 
export const { handle } = SvelteKitAuth({
  providers: [],
})
```

```typescript
export { handle } from "./auth"
```

```typescript
import type { LayoutServerLoad } from "./$types"
 
export const load: LayoutServerLoad = async (event) => {
  const session = await event.locals.auth()
 
  return {
    session,
  }
}
```

--------------------------------

### Install @auth/core and @auth/solid-start with pnpm

Source: https://authjs.dev/reference/solid-start

Installs the @auth/core and @auth/solid-start packages using pnpm. This command is equivalent to the npm installation but uses the pnpm package manager.

```bash
pnpm add @auth/core @auth/solid-start
```

--------------------------------

### Install @auth/core and @auth/solid-start with bun

Source: https://authjs.dev/reference/solid-start

Installs the @auth/core and @auth/solid-start packages using bun. This command is for projects utilizing the bun runtime and package manager.

```bash
bun add @auth/core @auth/solid-start
```

--------------------------------

### Express.js Auth.js Integration

Source: https://authjs.dev/getting-started/installation_framework=Qwik

Integrates Auth.js into an Express.js application by initializing `ExpressAuth` and applying it to a route. It includes setting the application to trust proxy headers and configuring an empty providers array.

```typescript
import { ExpressAuth } from "@auth/express"
import express from "express"
 
const app = express()
 
// If your app is served through a proxy
// trust the proxy to allow us to read the `X-Forwarded-*` headers
app.set("trust proxy", true)
app.use("/auth/*", ExpressAuth({ providers: [] }))
```

--------------------------------

### Configure Auth.js in Express

Source: https://authjs.dev/getting-started/installation_framework=Next

Integrates Auth.js with an Express.js application by using `ExpressAuth` and setting up a route handler for authentication. It also includes proxy configuration if the app is served behind one.

```typescript
import { ExpressAuth } from "@auth/express"
import express from "express"

const app = express()

// If your app is served through a proxy
// trust the proxy to allow us to read the `X-Forwarded-*` headers
app.set("trust proxy", true)
app.use("/auth/*", ExpressAuth({ providers: [] }))
```

--------------------------------

### Getting the Current Session (Client-Side)

Source: https://authjs.dev/reference/solid-start

Example of how to fetch the current session on the client-side using `createServerData$`.

```APIDOC
## Getting the Current Session

Fetch the current session on the client-side.

```typescript
import { getSession } from "@auth/solid-start"
import { createServerData$ } from "solid-start/server"
import { authOpts } from "~/routes/api/auth/[...solidauth]"

export const useSession = () => {
  return createServerData$(
    async (_, { request }) => {
      return await getSession(request, authOpts)
    },
    { key: () => ["auth_user"] }
  )
}

// useSession returns a resource:
const session = useSession()
const loading = session.loading
const user = () => session()?.user
```
```

--------------------------------

### Auth.js Initialization Example (TypeScript)

Source: https://authjs.dev/reference/solid-start

Demonstrates how to import and configure Auth.js for authentication. It shows setting up `AuthConfig` and handling requests and responses. This example is framework-agnostic.

```typescript
import Auth, { type AuthConfig } from "@auth/core"
 
export const authConfig: AuthConfig = {...}
 
const request = new Request("https://example.com")
const response = await AuthHandler(request, authConfig)
```

--------------------------------

### Next.js Auth.js Route Handler

Source: https://authjs.dev/getting-started/installation_framework=Qwik

Defines the API route handler for Auth.js in a Next.js App Router application. This file (`[...nextauth]/route.ts`) exports the GET and POST methods from the handlers created in the main `auth.ts` configuration file.

```typescript
import { handlers } from "@/auth" // Referring to the auth.ts we just created
export const { GET, POST } = handlers
```

--------------------------------

### Installation

Source: https://authjs.dev/reference/surrealdb-adapter

Instructions for installing the SurrealDB adapter using various package managers.

```APIDOC
## Installation

### npm
```bash
npm install @auth/surrealdb-adapter surrealdb.js
```

### pnpm
```bash
pnpm add @auth/surrealdb-adapter surrealdb.js
```

### yarn
```bash
yarn add @auth/surrealdb-adapter surrealdb.js
```

### bun
```bash
bun add @auth/surrealdb-adapter surrealdb.js
```
```

--------------------------------

### Install @auth/core and @auth/solid-start with npm

Source: https://authjs.dev/reference/solid-start

Installs the necessary @auth/core and @auth/solid-start packages using npm. This is the first step to integrate Auth.js with a SolidStart application.

```bash
npm install @auth/core @auth/solid-start
```

--------------------------------

### Auth Handler Setup

Source: https://authjs.dev/reference/solid-start

This section details how to set up the authentication handler for SolidStart, including environment variables and provider configuration.

```APIDOC
## Auth Handler Setup

### Environment Variables

Generate an auth secret and set it as an environment variable:
```
AUTH_SECRET=your_auth_secret
```

For specific providers like GitHub, set their respective environment variables:
```
GITHUB_ID=your_github_oauth_id
GITHUB_SECRET=your_github_oauth_secret
```

### Creating the API handler

This example uses GitHub as an OAuth provider.

```typescript
// routes/api/auth/[...solidauth].ts
import { SolidAuth, type SolidAuthConfig } from "@auth/solid-start"
import GitHub from "@auth/core/providers/github"

export const authOpts: SolidAuthConfig = {
  providers: [
    GitHub({
      clientId: process.env.GITHUB_ID,
      clientSecret: process.env.GITHUB_SECRET,
    }),
  ],
  debug: false,
}

export const { GET, POST } = SolidAuth(authOpts)
```
```

--------------------------------

### Install @auth/core and @auth/solid-start with yarn

Source: https://authjs.dev/reference/solid-start

Installs the @auth/core and @auth/solid-start packages using yarn. This command is suitable for projects managed with the yarn package manager.

```bash
yarn add @auth/core @auth/solid-start
```

--------------------------------

### Start Local Development Server with Different Package Managers

Source: https://authjs.dev/guides/configuring-github

This section provides commands to start the local development server using various package managers like npm, pnpm, yarn, and bun. These commands are essential for testing your Auth.js integration locally before deploying to production. Ensure you have the project dependencies installed before running these commands.

```bash
npm run dev
```

```bash
pnpm run dev
```

```bash
yarn dev
```

```bash
bun run dev
```

--------------------------------

### Installation

Source: https://authjs.dev/reference/pouchdb-adapter

Instructions for installing the @auth/pouchdb-adapter along with its dependencies.

```APIDOC
## Installation

### npm
```bash
npm install pouchdb pouchdb-find @auth/pouchdb-adapter
```

### pnpm
```bash
pnpm add pouchdb pouchdb-find @auth/pouchdb-adapter
```

### yarn
```bash
yarn add pouchdb pouchdb-find @auth/pouchdb-adapter
```

### bun
```bash
bun add pouchdb pouchdb-find @auth/pouchdb-adapter
```
```

--------------------------------

### Wikimedia Provider Callback URL Examples

Source: https://authjs.dev/getting-started/providers/wikimedia

Provides examples of callback URLs for the Wikimedia provider in different deployment scenarios. These URLs are used by Wikimedia to redirect users back to the application after authentication.

```plaintext
https://example.com/api/auth/callback/wikimedia
```

```plaintext
https://example.com/auth/callback/wikimedia
```

--------------------------------

### Configure Auth.js in Express

Source: https://authjs.dev/getting-started/installation

Integrates Auth.js with an Express application by importing `ExpressAuth` and adding the authentication handler to a route. It also includes proxy trust configuration.

```typescript
import { ExpressAuth } from "@auth/express"
import express from "express"
 
const app = express()

// If your app is served through a proxy
// trust the proxy to allow us to read the `X-Forwarded-*` headers
app.set("trust proxy", true)
app.use("/auth/*", ExpressAuth({ providers: [] }))
```

--------------------------------

### Battle.net Provider Callback URLs

Source: https://authjs.dev/getting-started/providers/battlenet

Example callback URLs for the Battle.net OAuth provider in Next.js, Qwik, SvelteKit, and Express applications. Ensure this matches your configured URL in the Battle.net developer portal.

```plaintext
https://example.com/api/auth/callback/battlenet
```

```plaintext
https://example.com/auth/callback/battlenet
```

--------------------------------

### Installation

Source: https://authjs.dev/reference/azure-tables-adapter

Instructions on how to install the @auth/azure-tables-adapter using various package managers.

```APIDOC
## Installation

This section provides installation instructions for the @auth/azure-tables-adapter.

### npm
```bash
npm install next-auth @auth/azure-tables-adapter
```

### pnpm
```bash
pnpm add next-auth @auth/azure-tables-adapter
```

### yarn
```bash
yarn add next-auth @auth/azure-tables-adapter
```

### bun
```bash
bun add next-auth @auth/azure-tables-adapter
```
```

--------------------------------

### Install Prisma Adapter and Prisma Client (bun)

Source: https://authjs.dev/getting-started/adapters/prisma

Installs the necessary packages for the Auth.js Prisma adapter and Prisma client using bun. It also installs Prisma as a development dependency.

```bash
bun add @prisma/client @prisma/extension-accelerate @auth/prisma-adapter
bun add prisma --dev
```

--------------------------------

### Setup New Framework Integration Script (npm)

Source: https://authjs.dev/guides/creating-a-framework-integration

This command uses npm to execute a setup script for a new framework integration. It copies template files and renames placeholders based on the provided framework name. This is the initial step for creating a new official integration.

```bash
npm setup-fw-integration <framework-name>
```

--------------------------------

### Install NextAuth.js using npm

Source: https://authjs.dev/reference/nextjs

Installs the NextAuth.js beta version using the npm package manager. Ensure you have Node.js and npm installed.

```bash
npm install next-auth@beta
```

--------------------------------

### Install Upstash Redis Adapter for Auth.js (npm, pnpm, yarn, bun)

Source: https://authjs.dev/getting-started/adapters/upstash-redis

Install the necessary packages for the Upstash Redis Adapter with Auth.js. This includes the core Upstash Redis client and the Auth.js adapter package. Ensure you have Node.js and a package manager installed.

```bash
npm install @upstash/redis @auth/upstash-redis-adapter
```

```bash
pnpm add @upstash/redis @auth/upstash-redis-adapter
```

```bash
yarn add @upstash/redis @auth/upstash-redis-adapter
```

```bash
bun add @upstash/redis @auth/upstash-redis-adapter
```

--------------------------------

### Install @auth/pg-adapter with bun

Source: https://authjs.dev/reference/pg-adapter

Installs the @auth/pg-adapter, next-auth, and pg packages using bun. This command is suitable for users who prefer the bun runtime.

```bash
bun add next-auth @auth/pg-adapter pg
```

--------------------------------

### Auth.js ClickUp Provider Setup (JavaScript)

Source: https://authjs.dev/reference/core/providers/click-up

Example of how to set up the ClickUp provider within an Auth.js application. Requires ClickUp client ID and secret for authentication.

```javascript
import { Auth } from "@auth/core"
import ClickUp from "@auth/core/providers/click-up"
 
const request = new Request(origin)
const response = await Auth(request, {
  providers: [
    ClickUp({
      clientId: CLICKUP_CLIENT_ID,
      clientSecret: CLICKUP_CLIENT_SECRET,
    }),
  ],
})
```

--------------------------------

### Setup New Framework Integration Script (bun)

Source: https://authjs.dev/guides/creating-a-framework-integration

This command uses bun to execute a setup script for a new framework integration. It copies template files and renames placeholders based on the provided framework name. This is the initial step for creating a new official integration.

```bash
bun setup-fw-integration <framework-name>
```

--------------------------------

### Install Prisma Adapter and Prisma Client (npm)

Source: https://authjs.dev/getting-started/adapters/prisma

Installs the necessary packages for the Auth.js Prisma adapter and Prisma client using npm. It also installs Prisma as a development dependency.

```bash
npm install @prisma/client @prisma/extension-accelerate @auth/prisma-adapter
npm install prisma --save-dev
```

--------------------------------

### Notion Provider Callback URLs

Source: https://authjs.dev/getting-started/providers/notion

Example callback URLs for the Notion provider integration. These URLs are used to handle the redirection after user authentication with Notion.

```url
https://example.com/api/auth/callback/notion
```

```url
https://example.com/auth/callback/notion
```

--------------------------------

### Installation

Source: https://authjs.dev/reference/kysely-adapter

Instructions on how to install the @auth/kysely-adapter and its dependencies using different package managers.

```APIDOC
## Installation

### npm
```
npm install @auth/kysely-adapter kysely
```

### pnpm
```
pnpm add @auth/kysely-adapter kysely
```

### yarn
```
yarn add @auth/kysely-adapter kysely
```

### bun
```
bun add @auth/kysely-adapter kysely
```
```

--------------------------------

### Express Auth.js Configuration with OneLogin

Source: https://authjs.dev/getting-started/providers/onelogin

Illustrates how to set up the OneLogin provider for an Express.js application using Auth.js. This example demonstrates using ExpressAuth middleware to enable the provider.

```javascript
import { ExpressAuth } from "@auth/express"
import OneLogin from "@auth/express/providers/onelogin"
 
app.use("/auth/*", ExpressAuth({ providers: [OneLogin] }))
```

--------------------------------

### Install Sequelize Adapter with bun

Source: https://authjs.dev/getting-started/adapters/sequelize

Installs the Auth.js Sequelize adapter and the Sequelize package using bun. This command utilizes the bun package manager for installation.

```bash
bun add @auth/sequelize-adapter sequelize
```

--------------------------------

### OneLogin Callback URL Examples

Source: https://authjs.dev/getting-started/providers/onelogin

Specifies the valid callback URLs for the OneLogin provider in Auth.js. These URLs are used by OneLogin to redirect users back to your application after successful authentication.

```plaintext
https://example.com/api/auth/callback/onelogin
```

```plaintext
https://example.com/auth/callback/onelogin
```

```plaintext
https://example.com/auth/callback/onelogin
```

--------------------------------

### Auth.js GitHub Provider Configuration Example

Source: https://authjs.dev/reference/core/providers/github

Example demonstrating how to configure the GitHub provider within an Auth.js application. This setup requires GitHub client ID and client secret. The provider is initialized with these credentials and added to the list of authentication providers.

```javascript
import { Auth } from "@auth/core"
import GitHub from "@auth/core/providers/github"

const request = new Request(origin)
const response = await Auth(request, {
  providers: [
    GitHub({ clientId: GITHUB_CLIENT_ID, clientSecret: GITHUB_CLIENT_SECRET }),
  ],
})
```

--------------------------------

### Accessing Session in SvelteKit Load Function

Source: https://authjs.dev/getting-started/installation_framework=SvelteKit

Demonstrates how to access the user's session within a SvelteKit `load` function using the `event.locals.auth()` method. This is made available by the Auth.js integration in `hooks.server.ts`.

```typescript
import type { LayoutServerLoad } from "./$types"

export const load: LayoutServerLoad = async (event) => {
  const session = await event.locals.auth()

  return {
    session,
  }
}
```

--------------------------------

### Apple Provider Configuration for Qwik

Source: https://authjs.dev/getting-started/providers/apple

Example of setting up the Apple provider for Qwik applications using Auth.js. This snippet demonstrates how to import QwikAuth$ and the Apple provider from the Qwik-specific Auth.js package to enable authentication flows.

```typescript
import { QwikAuth$ } from "@auth/qwik"
import Apple from "@auth/qwik/providers/apple"
 
export const { onRequest, useSession, useSignIn, useSignOut } = QwikAuth$(
  () => ({
    providers: [Apple],
  })
)
```

--------------------------------

### Setup BankID Norway Provider

Source: https://authjs.dev/reference/core/providers/bankid-no

Guides on how to set up and configure the BankID Norway provider for authentication.

```APIDOC
## default()

```
function default(config): OIDCConfig<BankIDNorwayProfile>
```

### Setup
#### Callback URL
```
https://example.com/api/auth/callback/bankid-no
```

#### Configuration
```typescript
import { Auth } from "@auth/core"
import BankIDNorge from "@auth/core/providers/bankid-no"
 
const request = new Request(origin)
const response = await Auth(request, {
  providers: [
    BankIDNorge({
      clientId: process.env.AUTH_BANKID_NO_ID,
      clientSecret: process.env.AUTH_BANKID_NO_SECRET,
    }),
  ],
})
```

### Resources
  * OpenID Connect Provider from BankID

### Notes
The BankID Norge provider comes with a default configuration. To override the defaults for your use case, check out customizing a built-in OAuth provider.
## Help
If you think you found a bug in the default configuration, you can open an issue. Auth.js strictly adheres to the specification and it cannot take responsibility for any deviation from the spec by the provider. You can open an issue, but if the problem is non-compliance with the spec, we might not pursue a resolution. You can ask for more help in Discussions.
### Parameters
Parameter| Type  
---|---
`config`| `OIDCUserConfig`<`BankIDNorwayProfile`>
### Returns
`OIDCConfig`<`BankIDNorwayProfile`>
```

--------------------------------

### GET Method

Source: https://authjs.dev/reference/solid-start

Details of the GET method provided by the Auth.js adapter.

```APIDOC
## GET()

### Description
Handles GET requests within the Auth.js adapter.

### Method
GET

### Endpoint
`/websites/authjs_dev` (Assumed based on project path)

### Parameters
#### Path Parameters
None

#### Query Parameters
None

#### Request Body
None

### Request Example
None

### Response
#### Success Response (200)
- **result** (Promise<undefined | Response>) - A promise that resolves to undefined or a Response object.

#### Response Example
```json
{
  "result": "undefined | Response"
}
```
```

--------------------------------

### Express Auth Setup

Source: https://authjs.dev/index

This snippet shows how to integrate Auth.js with an Express.js application using the GitHub provider. It sets up an authentication middleware for routes starting with '/auth/*' and utilizes `ExpressAuth` for configuration. Ensure Express and the necessary provider are installed.

```typescript
// server.ts
import { express } from "express"
import { ExpressAuth } from "@auth/express"
import GitHub from "@auth/express/providers/github"

const app = express()

app.use("/auth/*", ExpressAuth({
  providers: [GitHub]
}))


```

--------------------------------

### Install @auth/surrealdb-adapter

Source: https://authjs.dev/reference/surrealdb-adapter

Installation commands for the @auth/surrealdb-adapter using npm, pnpm, yarn, and bun. These commands install the adapter and its peer dependency, surrealdb.js.

```bash
npm install @auth/surrealdb-adapter surrealdb.js
```

```bash
pnpm add @auth/surrealdb-adapter surrealdb.js
```

```bash
yarn add @auth/surrealdb-adapter surrealdb.js
```

```bash
bun add @auth/surrealdb-adapter surrealdb.js
```

--------------------------------

### Install @auth/neon-adapter with bun

Source: https://authjs.dev/reference/neon-adapter

Installs the next-auth package and the @auth/neon-adapter using bun. This command is for projects using the bun runtime and package manager.

```bash
bun add next-auth @auth/neon-adapter
```

--------------------------------

### Battle.net Provider Configuration for SvelteKit

Source: https://authjs.dev/getting-started/providers/battlenet

Example configuration for integrating the Battle.net OAuth provider within a SvelteKit application using Auth.js. Ensure environment variables for client ID, secret, and issuer are set.

```typescript
import { SvelteKitAuth } from "@auth/sveltekit";
import BattleNet from "@auth/sveltekit/providers/battlenet";
 
export const { handle, signIn, signOut } = SvelteKitAuth({
  providers: [BattleNet({
    clientId: AUTH_BATTLENET_CLIENT_ID
    clientSecret: AUTH_BATTLENET_CLIENT_SECRET
    issuer: AUTH_BATTLENET_ISSUER
  })]
});
```

--------------------------------

### SolidStart API Handler Setup (TypeScript)

Source: https://authjs.dev/reference/solid-start

Sets up the API handler for SolidStart using Auth.js, including environment variable configuration for the authentication secret and a specific OAuth provider (GitHub).

```typescript
// routes/api/auth/[...solidauth].ts
import { SolidAuth, type SolidAuthConfig } from "@auth/solid-start"
import GitHub from "@auth/core/providers/github"

export const authOpts: SolidAuthConfig = {
  providers: [
    GitHub({
      clientId: process.env.GITHUB_ID,
      clientSecret: process.env.GITHUB_SECRET,
    }),
  ],
  debug: false,
}

export const { GET, POST } = SolidAuth(authOpts)
```

--------------------------------

### Callback URL Examples for Twitch Provider

Source: https://authjs.dev/getting-started/providers/twitch

These are example callback URLs for the Twitch provider. The specific URL depends on the framework and routing setup used.

```plaintext
https://example.com/api/auth/callback/twitch
```

```plaintext
https://example.com/auth/callback/twitch
```

--------------------------------

### Install PostgreSQL Adapter for Auth.js (npm, pnpm, yarn, bun)

Source: https://authjs.dev/getting-started/adapters/pg

Commands to install the PostgreSQL adapter and the pg package using different package managers. These are the initial steps for setting up the adapter.

```bash
npm install @auth/pg-adapter pg
```

```bash
pnpm add @auth/pg-adapter pg
```

```bash
yarn add @auth/pg-adapter pg
```

```bash
bun add @auth/pg-adapter pg
```

--------------------------------

### Install NextAuth.js using bun

Source: https://authjs.dev/reference/nextjs

Installs the NextAuth.js beta version using the bun package manager. Bun offers a fast alternative for JavaScript runtime and package management.

```bash
bun add next-auth@beta
```

--------------------------------

### Add Middleware for Session in Next.js

Source: https://authjs.dev/getting-started/installation

Implements optional middleware in Next.js to keep the session alive by updating its expiry time on each request. This uses the `auth` function exported from the Auth.js configuration.

```typescript
export { auth as middleware } from "@/auth"
```

--------------------------------

### Next.js Auth.js Mastodon Provider Configuration

Source: https://authjs.dev/getting-started/providers/mastodon

Example configuration for integrating the Mastodon provider with Auth.js in a Next.js application. This setup uses the NextAuth handler and imports the Mastodon provider.

```typescript
import NextAuth from "next-auth"
import Mastodon from "next-auth/providers/mastodon"
 
export const { handlers, auth, signIn, signOut } = NextAuth({
  providers: [Mastodon],
})
```

--------------------------------

### Setup New Framework Integration Script (yarn)

Source: https://authjs.dev/guides/creating-a-framework-integration

This command uses yarn to execute a setup script for a new framework integration. It copies template files and renames placeholders based on the provided framework name. This is the initial step for creating a new official integration.

```bash
yarn setup-fw-integration <framework-name>
```

--------------------------------

### SvelteKit Auth.js Hook Re-export

Source: https://authjs.dev/getting-started/installation_framework=Qwik

Re-exports the `handle` function from the Auth.js configuration file (`./auth`) into the SvelteKit server hooks file (`src/hooks.server.ts`). This makes the authentication handler available globally in the SvelteKit application.

```typescript
export { handle } from "./auth"
```

--------------------------------

### Configure PouchDB Adapter in SvelteKit with Auth.js

Source: https://authjs.dev/getting-started/adapters/pouchdb

This JavaScript code example demonstrates the configuration for SvelteKit applications using Auth.js with the PouchDB adapter. It includes PouchDB setup and integration with SvelteKitAuth.

```javascript
import { SvelteKitAuth } from "@auth/sveltekit"
import { PouchDBAdapter } from "@auth/pouchdb-adapter"
import PouchDB from "pouchdb"

// Setup your PouchDB instance and database
PouchDB.plugin(require("pouchdb-adapter-leveldb")) // Or any other adapter
  .plugin(require("pouchdb-find")) // Don't forget the `pouchdb-find` plugin

const pouchdb = new PouchDB("auth_db", { adapter: "leveldb" })

export const { handle, signIn, signOut } = SvelteKitAuth({
  providers: [],
  adapter: PouchDBAdapter(pouchdb),
})
```

--------------------------------

### Install Neon Adapter with bun

Source: https://authjs.dev/getting-started/adapters/neon

Installs the Neon adapter and the Neon.js serverless client using bun. This command is tailored for the bun runtime and package manager.

```bash
bun add @auth/neon-adapter @neondatabase/serverless
```

--------------------------------

### Install @auth/sequelize-adapter with bun

Source: https://authjs.dev/reference/sequelize-adapter

Installs the @auth/sequelize-adapter package along with next-auth and sequelize using bun. bun is a new, fast JavaScript runtime, bundler, transpiler, and package manager.

```bash
bun add next-auth @auth/sequelize-adapter sequelize
```

--------------------------------

### Install @auth/kysely-adapter with npm

Source: https://authjs.dev/reference/kysely-adapter

Installs the @auth/kysely-adapter and kysely packages using npm. Ensure Node.js and npm are installed.

```bash
npm install @auth/kysely-adapter kysely
```

--------------------------------

### Installation

Source: https://authjs.dev/reference/mongodb-adapter

Instructions for installing the @auth/mongodb-adapter package using various package managers.

```APIDOC
## Installation

### npm
```bash
npm install @auth/mongodb-adapter mongodb
```

### pnpm
```bash
pnpm add @auth/mongodb-adapter mongodb
```

### yarn
```bash
yarn add @auth/mongodb-adapter mongodb
```

### bun
```bash
bun add @auth/mongodb-adapter mongodb
```
```

--------------------------------

### Auth.js Middleware Initialization (Edge)

Source: https://authjs.dev/getting-started/migrating-to-v5

Example of a `middleware.ts` file demonstrating how to initialize Auth.js using only the edge-compatible configuration object imported from `auth.config.ts`. This approach avoids issues with database adapters in edge runtimes.

```typescript
import authConfig from "./auth.config"
import NextAuth from "next-auth"

// Use only one of the two middleware options below
// 1. Use middleware directly
// export const { auth: middleware } = NextAuth(authConfig)

// 2. Wrapped middleware option
const { auth } = NextAuth(authConfig)
export default auth(async function middleware(req: NextRequest) {
  // Your custom middleware logic goes here
})
```

--------------------------------

### Installation

Source: https://authjs.dev/reference/typeorm-adapter

Instructions for installing the TypeORM adapter for Auth.js using npm, pnpm, yarn, and bun.

```APIDOC
## Installation

### npm
```
npm install @auth/typeorm-adapter typeorm
```

### pnpm
```
pnpm add @auth/typeorm-adapter typeorm
```

### yarn
```
yarn add @auth/typeorm-adapter typeorm
```

### bun
```
bun add @auth/typeorm-adapter typeorm
```
```

--------------------------------

### Install MongoDB Adapter for Auth.js

Source: https://authjs.dev/getting-started/adapters/mongodb

Installs the Auth.js MongoDB adapter and the 'mongodb' package using various package managers. Ensure you have Node.js and a package manager installed.

```bash
npm install @auth/mongodb-adapter mongodb
```

```bash
pnpm add @auth/mongodb-adapter mongodb
```

```bash
yarn add @auth/mongodb-adapter mongodb
```

```bash
bun add @auth/mongodb-adapter mongodb
```

--------------------------------

### Install MikroORM Adapter with bun

Source: https://authjs.dev/getting-started/adapters/mikro-orm

Installs the necessary packages for the MikroORM adapter using bun. This is a newer, faster JavaScript runtime and package manager.

```bash
bun add @mikro-orm/core @auth/mikro-orm-adapter
```

--------------------------------

### Install MikroORM Adapter with npm

Source: https://authjs.dev/getting-started/adapters/mikro-orm

Installs the necessary packages for the MikroORM adapter using npm. This is the first step in integrating MikroORM with Auth.js.

```bash
npm install @mikro-orm/core @auth/mikro-orm-adapter
```

--------------------------------

### Install Xata Adapter for Auth.js

Source: https://authjs.dev/getting-started/adapters/xata

Commands to install the Auth.js Xata adapter using different package managers (npm, pnpm, yarn, bun). It also includes instructions for installing and logging in with the Xata CLI.

```bash
npm install @auth/xata-adapter
```

```bash
pnpm add @auth/xata-adapter
```

```bash
yarn add @auth/xata-adapter
```

```bash
bun add @auth/xata-adapter
```

```bash
# Install the Xata CLI globally if you don't already have it
npm install --location=global @xata.io/cli

# Login
xata auth login
```

--------------------------------

### Basic @auth/sveltekit Configuration

Source: https://authjs.dev/reference/sveltekit

Demonstrates the fundamental setup for @auth/sveltekit by importing necessary modules and initializing SvelteKitAuth with GitHub as a provider.

```typescript
import { SvelteKitAuth } from "@auth/sveltekit"
import GitHub from "@auth/sveltekit/providers/github"

export const { handle, signIn, signOut } = SvelteKitAuth({
  providers: [GitHub],
})
```

--------------------------------

### Generate AUTH_SECRET

Source: https://authjs.dev/getting-started/installation

Generates a secure random value for the AUTH_SECRET environment variable, used for encrypting tokens and hashes. This command also adds the secret to your .env file.

```bash
npx auth secret
```

--------------------------------

### Express Middleware to Get Session

Source: https://authjs.dev/getting-started/session-management/get-session

An example of creating Express middleware to fetch the session using `getSession` from `@auth/express` and attach it to the response locals. This makes the session easily accessible in subsequent route handlers.

```typescript
import {
  getSession
} from "@auth/express"
import {
  Request,
  Response,
  NextFunction
} from "express"

export function authSession(req: Request, res: Response, next: NextFunction) {
  res.locals.session = await getSession(req)
  next()
}

app.use(authSession)

// Now in your route
app.get("/", (req, res) => {
  const { session } = res.locals
  res.render("index", {
    user: session?.user
  })
})
```

--------------------------------

### Client-Side Sign-In and Sign-Out Actions (Svelte)

Source: https://authjs.dev/reference/sveltekit

Demonstrates using `signIn` and `signOut` functions from `@auth/sveltekit/client` to manage user authentication directly within a Svelte component. It shows examples for signing in with different providers like GitHub, Discord, and credentials, as well as a general sign-out action. Ensure the `@auth/sveltekit/client` package is installed.

```svelte
<script>
  import { signIn, signOut } from "@auth/sveltekit/client"
  let password
</script>
 
<nav>
  <p>
    These actions are all using the methods exported from
    <code>@auth/sveltekit/client</code>
  </p>
  <div class="actions">
    <div class="wrapper-form">
      <button on:click={() => signIn("github")}>Sign In with GitHub</button>
    </div>
    <div class="wrapper-form">
      <button on:click={() => signIn("discord")}>Sign In with Discord</button>
    </div>
    <div class="wrapper-form">
      <div class="input-wrapper">
        <label for="password">Password</label>
        <input
          bind:value={password}
          type="password"
          id="password"
          name="password"
          required
        />
      </div>
      <button on:click={() => signIn("credentials", { password })}>
        Sign In with Credentials
      </button>
      <button on:click={() => signOut()}>
        Sign Out
      </button>
    </div>
  </div>
</nav>

```

--------------------------------

### SvelteKit Auth.js Mastodon Provider Configuration

Source: https://authjs.dev/getting-started/providers/mastodon

Example of setting up the Mastodon provider with Auth.js in a SvelteKit application. This uses SvelteKitAuth and imports the Mastodon provider from the SvelteKit Auth package.

```typescript
import { SvelteKitAuth } from "@auth/sveltekit"
import Mastodon from "@auth/sveltekit/providers/mastodon"
 
export const { handle, signIn, signOut } = SvelteKitAuth({
  providers: [Mastodon],
})
```

--------------------------------

### Install Drizzle ORM Adapter for Auth.js

Source: https://authjs.dev/getting-started/adapters/drizzle

Installs the necessary Drizzle ORM adapter packages for Auth.js using npm, pnpm, yarn, or bun. This is the first step to integrate Drizzle with your authentication setup.

```bash
npm install drizzle-orm @auth/drizzle-adapter
npm install drizzle-kit --save-dev
```

```bash
pnpm add drizzle-orm @auth/drizzle-adapter
pnpm add drizzle-kit --save-dev
```

```bash
yarn add drizzle-orm @auth/drizzle-adapter
yarn add drizzle-kit --dev
```

```bash
bun add drizzle-orm @auth/drizzle-adapter
bun add drizzle-kit --dev
```

--------------------------------

### Sequelize Configuration Example (SvelteKit)

Source: https://authjs.dev/getting-started/adapters/sequelize

Configures Auth.js with the Sequelize adapter for a SvelteKit application. It initializes Sequelize using `process.env.DATABASE_URL` and integrates with SvelteKitAuth.

```typescript
import { SvelteKitAuth } from "@auth/sveltekit"
import SequelizeAdapter from "@auth/sequelize-adapter"
import { Sequelize } from "sequelize"

const sequelize = new Sequelize(process.env.DATABASE_URL)

export const { handle, signIn, signOut } = SvelteKitAuth({
  providers: [],
  adapter: SequelizeAdapter(sequelize),
})
```

--------------------------------

### Install PostgreSQL Client for Kysely Adapter

Source: https://authjs.dev/getting-started/adapters/kysely

Installs the 'pg' client and its types for PostgreSQL compatibility with the Kysely adapter. Supports npm, pnpm, yarn, and bun.

```bash
npm install pg
npm install --save-dev @types/pg
```

```bash
pnpm add pg
pnpm add --save-dev @types/pg
```

```bash
yarn add pg
yarn add --dev @types/pg
```

```bash
bun add pg
bun add --dev @types/pg
```

--------------------------------

### Install @auth/d1-adapter with bun

Source: https://authjs.dev/reference/d1-adapter

Installs the @auth/d1-adapter package along with next-auth using bun. Bun is a fast all-in-one JavaScript runtime.

```bash
bun add next-auth @auth/d1-adapter
```