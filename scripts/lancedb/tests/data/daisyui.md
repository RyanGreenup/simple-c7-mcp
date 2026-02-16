### Navigate, install dependencies, and start SvelteKit development server

Source: https://daisyui.com/blog/how-to-install-sveltekit-and-daisyui

After initializing a SvelteKit project, these commands navigate into the project directory, install all required npm dependencies, and then start the development server. The `--open` flag automatically opens the application in a web browser.

```bash
cd my-app
npm install
npm run dev -- --open
```

--------------------------------

### Create a new Solid Start project

Source: https://daisyui.com/docs/install/solid-start

This command initializes a new Solid Start project in the current directory. It sets up the basic project structure and dependencies required for a Solid.js application, preparing it for further development.

```Terminal
npm init solid@latest ./
```

--------------------------------

### Install Dependencies and Start Development Server (npm)

Source: https://daisyui.com/blog/daisyui-nextjs-online-store-template

These commands are used to initialize and run the daisyUI + Next.js online store template. `npm install` fetches all necessary project dependencies, while `npm run dev` starts the local development server, making the application accessible at `http://localhost:3000`.

```bash
npm install
```

```bash
npm run dev
```

--------------------------------

### Initialize daisyUI with npm

Source: https://daisyui.com/blog/npm-init-daisyui

Single command to start the daisyUI initialization process using npm. This command launches an interactive prompt allowing users to choose their preferred setup configuration.

```bash
npm init daisyui
```

--------------------------------

### HTML daisyUI Quick Start - CDN Setup

Source: https://daisyui.com/pages/ui-library-for-hackaton

Minimal HTML setup for daisyUI using CDN links without build tools or configuration. Demonstrates the lightning-fast setup approach that enables rapid prototyping for hackathon projects.

```html
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Hackathon Project</title>
  <link href="https://cdn.jsdelivr.net/npm/daisyui@5" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
</head>
<body>
  <button class="btn btn-primary">Let's build!</button>
</body>
</html>
```

--------------------------------

### AI Prompt Examples for daisyUI Code Generation

Source: https://daisyui.com/docs/editor/vscode

Example prompts for requesting daisyUI code generation with different MCP servers. These prompts demonstrate how to ask AI for specific daisyUI themes and components with MCP server directives.

```text
give me a light daisyUI 5 theme with tropical color palette. use Blueprint MCP
```

```text
give me a light daisyUI 5 theme with tropical color palette. use context7
```

```text
give me a light daisyUI 5 theme with tropical color palette
```

--------------------------------

### Run Deno Fresh development server

Source: https://daisyui.com/docs/install/fresh

Starts the development server for your Deno Fresh project. This allows you to preview your application and see the changes with daisyUI applied.

```bash
deno task dev
```

--------------------------------

### Example Claude Code Prompt using Blueprint MCP

Source: https://daisyui.com/docs/editor/claudecode

This example demonstrates how to instruct Claude Code to use the Blueprint MCP server. By appending 'use Blueprint MCP' to the prompt, users can guide the AI to generate daisyUI themes with specific styles and color palettes, leveraging the Blueprint server's capabilities.

```prompt
give me a light daisyUI 5 theme with tropical color palette. use Blueprint MCP
```

--------------------------------

### Start Elysia development server

Source: https://daisyui.com/docs/install/elysia

Run the Elysia server in development mode using Bun, which will start the server and enable CSS watching for automatic recompilation.

```bash
bun run dev
```

--------------------------------

### Create a new Waku project

Source: https://daisyui.com/docs/install/waku

This command initializes a new Waku project named 'myapp' and then navigates into the newly created project directory. It's the foundational step for starting a Waku application.

```Terminal
npm create waku@latest -- --project-name=myapp
cd myapp
```

--------------------------------

### Display DaisyUI Toggles, Checkboxes, and Radios with Color Variants in HTML

Source: https://daisyui.com/codepen

This example showcases various input

--------------------------------

### Example Claude Code Prompt using Context7 MCP

Source: https://daisyui.com/docs/editor/claudecode

This example illustrates how to direct Claude Code to utilize the Context7 MCP server. By including 'use context7' in the prompt, users can ensure the AI leverages Context7's enhanced context for generating specific daisyUI themes and components.

```prompt
give me a light daisyUI 5 theme with tropical color palette. use context7
```

--------------------------------

### Start Yew Development Server

Source: https://daisyui.com/docs/install/yew

Launches the Trunk development server with automatic browser opening, enabling hot-reload for development of the Yew application.

```shell
trunk serve --open
```

--------------------------------

### Initialize a new SvelteKit project using npm

Source: https://daisyui.com/blog/how-to-install-sveltekit-and-daisyui

This command initializes a new SvelteKit project named 'my-app' using the latest Svelte CLI. It prompts the user to select a project template, with 'Skeleton project' being the recommended choice for a barebones setup.

```bash
npm create svelte@latest my-app
```

--------------------------------

### Create new Elysia project with Bun

Source: https://daisyui.com/docs/install/elysia

Initialize a new Elysia project using Bun package manager and install the static file serving plugin required for serving HTML and CSS files.

```bash
bun create elysia myapp
cd myapp
bun install @elysiajs/static
```

--------------------------------

### Install daisyUI with Yarn

Source: https://daisyui.com/alternative/preline

Install daisyUI as a development dependency using Yarn package manager. Yarn provides deterministic dependency resolution and improved performance.

```bash
yarn add -D daisyui@latest
```

--------------------------------

### Download daisyUI llms.txt to Project Directory

Source: https://daisyui.com/docs/editor/vscode

Terminal command to permanently save daisyUI's llms.txt documentation file to project workspace for default Copilot access. Creates the .github/instructions directory structure and downloads the file as daisyui.instructions.md for project-level setup.

```bash
curl -L https://daisyui.com/llms.txt --create-dirs -o .github/instructions/daisyui.instructions.md
```

--------------------------------

### Example Claude Code Prompt using daisyUI GitMCP

Source: https://daisyui.com/docs/editor/claudecode

This example shows a prompt for Claude Code when using the daisyUI GitMCP server. Unlike other MCPs, explicit mention of 'use daisyui' might not be required if it's the default or only configured MCP. It allows users to generate daisyUI themes without specific server directives in the prompt.

```prompt
give me a light daisyUI 5 theme with tropical color palette
```

--------------------------------

### Fast Install daisyUI with Tailwind CSS Standalone - Linux/MacOS

Source: https://daisyui.com/docs/install/standalone

One-line installation script that automatically downloads Tailwind CSS Standalone executable and daisyUI bundle, creates input.css with required imports, and generates initial output.css file. Requires curl and bash.

```bash
curl -sL daisyui.com/fast | bash
```

--------------------------------

### Start Front-end Development Server with Yarn

Source: https://daisyui.com/blog/mary-ui

This command starts the development server using Yarn, typically used for front-end asset compilation and serving. It's essential for seeing real-time changes during development with Livewire, Tailwind CSS, and Vite, applicable for both new and existing project setups.

```bash
yarn dev
```

--------------------------------

### Fast Install daisyUI with Tailwind CSS Standalone - Windows

Source: https://daisyui.com/docs/install/standalone

PowerShell installation script for Windows that automates downloading Tailwind CSS Standalone executable and daisyUI bundle, creates input.css configuration, and generates initial output.css file.

```powershell
powershell -c "irm daisyui.com/fast.ps1 | iex"
```

--------------------------------

### Install daisyUI with Deno

Source: https://daisyui.com/alternative/preline

Install daisyUI as a development dependency using Deno's NPM package support. This allows Deno projects to use NPM packages directly.

```bash
deno i -D npm:daisyui@latest
```

--------------------------------

### Create a new Elixir Phoenix project

Source: https://daisyui.com/docs/install/phoenix

This command initializes a new Elixir Phoenix project in the current directory. The `--no-ecto` flag is used to skip the database setup, which is useful for projects that do not require a database or for quick demonstrations.

```Terminal
mix phx.new ./ --no-ecto
```

--------------------------------

### Create New Laravel Project

Source: https://daisyui.com/docs/install/laravel

Initialize a new Laravel project using the Laravel Installer. This command creates a fresh Laravel application with all necessary dependencies and project structure.

```bash
laravel new my-app
cd my-app
```

--------------------------------

### Create New Yew Project

Source: https://daisyui.com/docs/install/yew

Initializes a new Rust project and navigates into the project directory to set up a Yew application.

```shell
cargo new yew-app
cd yew-app
```

--------------------------------

### Create a new Lit project with Vite using npm

Source: https://daisyui.com/docs/install/lit

This command initializes a new project using Vite, specifically configured with the Lit template. It sets up the basic project structure for a Lit web component application, providing a clean starting point.

```bash
npm create vite@latest ./ -- --template lit
```

--------------------------------

### Run Zola Development Server

Source: https://daisyui.com/docs/install/zola

Start the Zola development server to preview your site locally. Run this command in a separate terminal tab to serve your Zola project with hot-reload capabilities.

```bash
zola serve
```

--------------------------------

### Configure Vite for Tailwind CSS in Solid Start

Source: https://daisyui.com/docs/install/solid-start

This TypeScript configuration file integrates the Tailwind CSS Vite plugin into the Solid Start build process. It imports `defineConfig` and `tailwindcss` to ensure Tailwind CSS is processed correctly during development and build, allowing utility classes to be used.

```TypeScript
import { defineConfig } from "@solidjs/start/config";
import tailwindcss from "@tailwindcss/vite";
export default defineConfig({
  vite: {
    plugins: [tailwindcss()],
  },
});
```

--------------------------------

### Install Node.js dependencies for Astro/daisyUI template

Source: https://daisyui.com/blog/daisyui-astro-tailwind-documentation-template

This command installs all required Node.js packages listed in the `package.json` file for the Astro and daisyUI documentation template. It should be executed in the project's root directory after downloading the template to ensure all necessary libraries are available.

```bash
npm install
```

--------------------------------

### Start Dioxus development server

Source: https://daisyui.com/docs/install/dioxus

This command launches the Dioxus development server, making the application accessible in a web browser. It should be run in a separate terminal from the Tailwind CSS watcher.

```Terminal
dx serve
```

--------------------------------

### Initialize Zola Project

Source: https://daisyui.com/docs/install/zola

Create a new Zola static site generator project and navigate into the project directory. This sets up the basic project structure needed for the installation.

```bash
zola init myblog
cd myblog
```

--------------------------------

### Configure npm Scripts for Electron and Tailwind CSS

Source: https://daisyui.com/docs/install/electron

These commands add two essential scripts to the `package.json` file. The `start` script is configured to launch the Electron application, while the `build:css` script automates the compilation of Tailwind CSS and daisyUI from `src/input.css` to `public/output.css`.

```Terminal
npm pkg set scripts.start="electron ."
npm pkg set scripts.build:css="tailwindcss -i src/input.css -o public/output.css"
```

--------------------------------

### Example metadata.json for Extending Product Details (JSON)

Source: https://daisyui.com/blog/daisyui-nextjs-online-store-template

This JSON example illustrates how to use the `metadata.json` file to enrich product information beyond what's available from Lemon Squeezy. It demonstrates adding custom categories, product variants, additional details, and image URLs.

```json
{
  "id": "12345",
  "availability": true,
  "sale": true,
  "category": ["trending", "bestsellers"],
  "original_price": "$50",
  "variant": {
    "size": [
      { "name": "Small", "link": "https://example.com/small" },
      { "name": "Medium", "link": "https://example.com/medium" }
    ]
  },
  "info": {
    "Material": "100% Cotton",
    "Care Instructions": "Machine washable"
  },
  "images": ["https://example.com/image1.jpg", "https://example.com/image2.jpg"]
}
```

--------------------------------

### Download daisyUI llms.txt to Cursor Rules

Source: https://daisyui.com/docs/editor/cursor

Terminal command to download daisyUI's llms.txt documentation file to the Cursor editor's rules directory. This enables Cursor to reference daisyUI documentation when generating code. The file is saved to `.cursor/rules/daisyui.mdc` for project-level permanent setup.

```bash
curl -L https://daisyui.com/llms.txt --create-dirs -o .cursor/rules/daisyui.mdc
```

--------------------------------

### Run Laravel Development Server

Source: https://daisyui.com/docs/install/laravel

Start the Laravel development server using Artisan. This command runs the application on a local development server, typically accessible at http://localhost:8000.

```bash
php artisan serve
```

--------------------------------

### Start Rails Development Server

Source: https://daisyui.com/docs/install/rails

This command initiates the Rails development server, making the application accessible locally in a web browser. It allows developers to view and interact with their application, including the newly integrated daisyUI components, during the development process.

```Terminal
./bin/dev
```

--------------------------------

### Install daisyUI using various package managers and integrate with CSS

Source: https://daisyui.com/compare/bootstrap-vs-flux

This snippet provides commands to install the latest version of daisyUI as a development dependency using popular Node.js package managers like npm, pnpm, yarn, and bun, as well as Deno. It also includes the necessary CSS import for `app.css` to integrate daisyUI with Tailwind CSS, enabling its utility classes and components.

```npm
npm i -D daisyui@latest
```

```pnpm
pnpm add -D daisyui@latest
```

```yarn
yarn add -D daisyui@latest
```

```bun
bun add -D daisyui@latest
```

```deno
deno i -D npm:daisyui@latest
```

```css
@import "tailwindcss";
@plugin "daisyui";
```

--------------------------------

### Add daisyUI from CDN with Tailwind CSS

Source: https://daisyui.com/docs/cdn

Basic setup to use daisyUI components from CDN. Includes the main daisyUI stylesheet (42kB compressed) and Tailwind CSS browser build. This is the quickest way to get started without any installation or build process.

```html
<link href="https://cdn.jsdelivr.net/npm/daisyui@5" rel="stylesheet" type="text/css" />
<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
```

--------------------------------

### Create a new Next.js project

Source: https://daisyui.com/blog/install-daisyui-and-tailwindcss-in-nextjs

This command initializes a new Next.js application using the latest `create-next-app` utility. During the setup process, ensure to enable Tailwind CSS when prompted to streamline the integration.

```bash
npx create-next-app@latest
```

--------------------------------

### Run CSS build script with npm

Source: https://daisyui.com/docs/install/cli

Execute the build script to compile and generate the output CSS file. This creates public/output.css containing all compiled Tailwind CSS and daisyUI styles.

```bash
npm run build:css
```

--------------------------------

### Download daisyUI Bundle Files

Source: https://daisyui.com/docs/install/standalone

Downloads the latest daisyUI JavaScript module files (daisyui.mjs and daisyui-theme.mjs) from GitHub releases and places them in the current directory alongside the Tailwind CSS executable.

```bash
curl -sLO https://github.com/saadeghi/daisyui/releases/latest/download/daisyui.mjs
curl -sLO https://github.com/saadeghi/daisyui/releases/latest/download/daisyui-theme.mjs
```

--------------------------------

### Install Tailwind CSS CLI and daisyUI with npm

Source: https://daisyui.com/docs/install/cli

Install the required npm packages for Tailwind CSS CLI and daisyUI. This command installs the latest versions of tailwindcss, the Tailwind CSS CLI, and daisyUI as project dependencies.

```bash
npm install tailwindcss@latest @tailwindcss/cli@latest daisyui@latest
```

--------------------------------

### Start the Next.js development server

Source: https://daisyui.com/blog/install-daisyui-and-tailwindcss-in-nextjs

Execute this command to launch the Next.js development server. This makes your application accessible locally, typically at `http://localhost:3000/`, and enables features like hot module reloading for efficient development.

```bash
npm run dev
```

--------------------------------

### Run an Elixir Phoenix development server

Source: https://daisyui.com/docs/install/phoenix

This command starts the development server for your Elixir Phoenix project. Once the server is running, the application will be accessible in your web browser, allowing you to use daisyUI class names.

```Terminal
mix phx.server
```

--------------------------------

### Build CSS and Run Electron Application

Source: https://daisyui.com/docs/install/electron

These commands execute the previously configured npm scripts. `npm run build:css` compiles the Tailwind CSS and daisyUI styles, and `npm start` launches the Electron application, displaying the `index.html` with the applied styles.

```Terminal
npm run build:css
npm start
```

--------------------------------

### Preview production build of Nexus dashboard

Source: https://daisyui.com/blog/nexus-dashboard-template

Previews the production-optimized build locally before deployment. Allows testing of the final production version in a local environment.

```bash
npm run preview
```

--------------------------------

### Create a new Qwik project

Source: https://daisyui.com/docs/install/qwik

This command initializes a new Qwik project in the current directory using the `npm create qwik` command, setting up an empty project structure ready for development.

```bash
npm create qwik@latest empty ./
```

--------------------------------

### Structure a New Blog Post with Markdown and Frontmatter

Source: https://daisyui.com/blog/how-to-make-a-blog-quickly-using-astro-and-daisyUI

This example demonstrates the basic structure for a new blog post using Markdown and Astro's frontmatter. It includes essential metadata such as title, description, date, image, author, and category, followed by the main content of the post.

```markdown
---
title: Boosting Sales with Effective Search Engine Optimization (SEO)
description: Lorem ipsum dolor sit, amet consectetur adipisicing elit. Hic eos odit sequi minima iure natus, odio tempora sit Lorem ipsum dolor sit.
date: 2024/01/12
image: ./images/post-1.jpg
author: antonio
authorImage: /images/about.jpeg
category: seo
---

<script>
  import Translate from "$components/Translate.svelte"
</script>

## **Introduction**

In the digital age, a strong online presence is crucial for businesses looking to thrive. One of the key components of a successful online strategy is Search Engine Optimization (SEO). By optimizing your website for search engines, you can significantly improve your visibility, attract more potential customers, and ultimately boost your sales. In this article, we'll explore some essential SEO strategies to help you achieve these goals.
```

--------------------------------

### Initialize Node.js and install Tailwind CSS/daisyUI via npm

Source: https://daisyui.com/docs/install/dioxus

These commands set up a new Node.js project and install the necessary packages: Tailwind CSS CLI for processing styles and daisyUI as a Tailwind CSS plugin. Node.js and npm are required dependencies.

```Terminal
npm init -y
npm install tailwindcss@latest @tailwindcss/cli@latest daisyui@latest
```

--------------------------------

### Install PostCSS, Tailwind CSS, and daisyUI packages

Source: https://daisyui.com/docs/install/postcss

NPM command to install required dependencies for PostCSS setup with Tailwind CSS and daisyUI. Installs postcss, postcss-cli, tailwindcss, @tailwindcss/postcss, and the latest daisyui package.

```bash
npm i postcss postcss-cli tailwindcss @tailwindcss/postcss daisyui@latest
```

--------------------------------

### Configure daisyUI Plugin Options

Source: https://daisyui.com/blog/daisyui-5-alpha

Configure the daisyUI plugin with advanced options including logging, root selector, component inclusion/exclusion, and theme selection. Allows fine-grained control over which components are loaded and which themes are available.

```css
@plugin "daisyui" {
  logs: true;
  root: ":root";
  include: button, badge, input, card;
  exclude: badge;
  themes: light --default, dark --prefersdark, cupcake;
}
```

--------------------------------

### Setup Elysia server with CSS building and file watching

Source: https://daisyui.com/docs/install/elysia

Create an Elysia server that compiles Tailwind CSS on startup and watches for file changes, serves static files from the public directory, and listens on port 3000. Uses child_process exec for Tailwind CLI and fs watch for file monitoring.

```typescript
import { Elysia } from "elysia";
import { staticPlugin } from '@elysiajs/static'
import { exec } from 'child_process'
import { watch } from 'fs'

const buildCSS = () =>
  new Promise(resolve =>
    exec('tailwindcss -i ./src/app.css -o ./public/output.css',
      (_error, _stdout, stderr) => {
        console.log(stderr);
        resolve(null);
      })
  );

await buildCSS();

const watcher = watch('./public', { recursive: true },
  async () => {
    await buildCSS();
  }
);

process.on('SIGINT', () => {
  watcher.close();
  process.exit(0);
});

const app = new Elysia()
	.use(
		staticPlugin({
			assets: "public",
      prefix: "",
		}),
	)
	.listen(3000, ({ hostname, port }) => {
		console.log(`Server started http://${hostname}:${port}`);
	});
```

--------------------------------

### Structure Content for MDX Documentation Page

Source: https://daisyui.com/blog/daisyui-astro-tailwind-documentation-template

This example demonstrates the basic structure for an `.mdx` file, including frontmatter for metadata (title, description), an import for a Svelte component, and standard Markdown content. This format allows for rich, interactive documentation pages.

```mdx
---
title: Getting Started
description: "Quasi sapiente voluptates aut minima non doloribus similique quisquam. In quo expedita ipsum nostrum corrupti incidunt. Et aut eligendi ea perferendis."
---

<script>
  import Translate from "$components/Translate.svelte"
</script>

## Overview

Authentication is a crucial aspect of any web application, ensuring that users are who they claim to be before granting access to resources or sensitive information. Access Shield simplifies the process of user authentication, offering features such as:

- **User Registration and Login**: Allow users to create accounts and securely log in to your application.
- **Password Hashing and Encryption**: Safeguard user passwords by securely hashing and encrypting them before storage.
- **Session Management**: Manage user sessions to maintain authentication state across requests.
- **OAuth Integration**: Simplify user authentication by integrating with popular OAuth providers.
- **Two-Factor Authentication (2FA)**: Enhance security by requiring an additional authentication factor.
- **Role-Based Access Control (RBAC)**: Define roles and permissions to control access to resources.
```

--------------------------------

### Install daisyUI with PNPM

Source: https://daisyui.com/alternative/preline

Install daisyUI as a development dependency using PNPM package manager. PNPM is a faster and more efficient alternative to NPM.

```bash
pnpm add -D daisyui@latest
```

--------------------------------

### Install Trunk Build Tool

Source: https://daisyui.com/docs/install/yew

Installs Trunk, a build tool for Rust WebAssembly projects that handles bundling and asset management for Yew applications.

```shell
cargo install --locked trunk
```

--------------------------------

### Integrate Pikaday Date Picker with React

Source: https://daisyui.com/components/calendar

This example illustrates the installation and usage of the Pikaday date picker within a React functional component. It leverages React's `useRef` hook to reference the input element and `useEffect` to initialize Pikaday, ensuring proper setup and cleanup during the component's lifecycle.

```shell
npm i pikaday
```

```tsx
import { useEffect, useRef } from "react";
import Pikaday from "pikaday";

export default function App() {
  const myDatepicker = useRef(null);
  useEffect(() => {
    const picker = new Pikaday({
      field: myDatepicker.current
    });
    return () => picker.destroy();
  }, []);
  return (
    <input type="text" className="input pika-single" defaultValue="Pick a date" ref={myDatepicker} />
  );
}
```

--------------------------------

### Install daisyUI with Bun

Source: https://daisyui.com/alternative/preline

Install daisyUI as a development dependency using Bun package manager. Bun is a modern JavaScript runtime with built-in package management.

```bash
bun add -D daisyui@latest
```

--------------------------------

### Create HTML Entry Point for Yew App

Source: https://daisyui.com/docs/install/yew

Sets up the root HTML file that serves as the entry point for the Yew application, linking to the compiled Tailwind CSS output file.

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Yew App</title>
    <link rel="stylesheet" href="output.css" />
  </head>
  <body></body>
</html>
```

--------------------------------

### Install styling dependencies for SvelteKit

Source: https://daisyui.com/blog/how-to-install-sveltekit-and-daisyui

This command installs Tailwind CSS, PostCSS, Autoprefixer, and daisyUI as development dependencies. It then initializes Tailwind CSS, generating `tailwind.config.js` and `postcss.config.js` files, which are necessary for configuring the styling frameworks.

```bash
npm install -D tailwindcss postcss autoprefixer daisyui
npx tailwindcss init -p
```

--------------------------------

### Create a new Dioxus project using CLI

Source: https://daisyui.com/docs/install/dioxus

This command initializes a new Dioxus project in the current directory. It requires Rust, WebAssembly Target, and the Dioxus CLI to be installed beforehand.

```Terminal
dx new ./
```

--------------------------------

### Install daisyUI with NPM

Source: https://daisyui.com/alternative/preline

Install daisyUI as a development dependency using NPM package manager. This command fetches the latest version of daisyUI from the NPM registry.

```bash
npm i -D daisyui@latest
```

--------------------------------

### Initialize daisyUI with Yarn and Bun

Source: https://daisyui.com/blog/npm-init-daisyui

Alternative package managers for initializing daisyUI. Yarn and Bun provide equivalent functionality to npm with their respective create commands.

```bash
yarn create daisyui
```

```bash
bun create daisyui
```

```bash
npm create daisyui
```

--------------------------------

### Advanced daisyUI configuration example with multiple themes and custom settings (CSS)

Source: https://daisyui.com/llms

This comprehensive CSS configuration example enables a wide range of built-in daisyUI themes, setting 'bumblebee' as the default and 'synthwave' as the preferred dark theme. It also customizes the prefix for daisyUI classes to 'daisy-', excludes specific components like 'rootscrollgutter' and 'checkbox', and disables console logging for a cleaner output.

```css
@plugin "daisyui" {
  themes: light, dark, cupcake, bumblebee --default, emerald, corporate, synthwave --prefersdark, retro, cyberpunk, valentine, halloween, garden, forest, aqua, lofi, pastel, fantasy, wireframe, black, luxury, dracula, cmyk, autumn, business, acid, lemonade, night, coffee, winter, dim, nord, sunset, caramellatte, abyss, silk;
  root: ":root";
  include: ;
  exclude: rootscrollgutter, checkbox;
  prefix: daisy-;
  logs: false;
}
```

--------------------------------

### Create a new SvelteKit project

Source: https://daisyui.com/docs/install/sveltekit

This command initializes a new SvelteKit project in the current directory. It sets up the basic project structure and necessary configuration files.

```Terminal
npx sv create ./
```

--------------------------------

### Create Rails Homepage with daisyUI Button

Source: https://daisyui.com/docs/install/rails

This demonstrates how to establish a basic homepage within a Rails application, allowing for immediate testing of daisyUI components. It involves defining a controller action, configuring a root route in `config/routes.rb`, and rendering a simple ERB view that incorporates a daisyUI button class. This setup provides a functional page to verify the successful integration of daisyUI.

```Ruby
class PagesController < ApplicationController
  def home
  end
end
```

```Ruby
Rails.application.routes.draw do
  root to: 'pages#home'
end
```

```HTML
<button class="btn btn-primary">Hello daisyUI!</button>
```

--------------------------------

### Initialize Node.js Project for Electron

Source: https://daisyui.com/docs/install/electron

This command sequence initializes a new Node.js project within a dedicated directory. It creates a folder, navigates into it, and runs `npm init` to generate a `package.json` file, setting up the basic project structure.

```Terminal
mkdir myapp
cd myapp
npm init
```

--------------------------------

### Install daisyUI Blueprint MCP Server in Claude Code

Source: https://daisyui.com/blueprint

This bash command facilitates the installation of the daisyUI Blueprint MCP server within Claude Code. It sets up the server by specifying environment variables for the license key, email, and an optional Figma API key, then executes the `daisyui-blueprint` package using `npx`.

```bash
claude mcp add daisyui-blueprint
    --env LICENSE=YOUR_LICENSE_KEY
    --env EMAIL=YOUR_EMAIL
    --env FIGMA=YOUR_FIGMA_API_KEY
    -- npx -y daisyui-blueprint@latest
```

--------------------------------

### Install Eleventy, PostCSS, Tailwind CSS, Typography, and daisyUI

Source: https://daisyui.com/docs/install/11ty

This command installs all necessary development dependencies for an Eleventy project using Tailwind CSS and daisyUI. It includes `@11ty/eleventy` for static site generation, `postcss` for CSS processing, `tailwindcss` and its PostCSS plugin, `@tailwindcss/typography` for styling rich text, and `daisyui` for UI components.

```Terminal
npm install @11ty/eleventy postcss tailwindcss@latest @tailwindcss/postcss@latest @tailwindcss/typography@latest daisyui@latest
```

--------------------------------

### Install daisyUI Alpha via npm

Source: https://daisyui.com/blog/daisyui-5-alpha

Install the daisyUI alpha version as a development dependency using npm. This command fetches the latest alpha release from the npm registry for use with Tailwind CSS 4 alpha.

```bash
npm i -D daisyui@alpha
```

--------------------------------

### Configure daisyUI GitMCP Server in Windsurf

Source: https://daisyui.com/docs/editor/windsurf

Setup the daisyUI GitMCP server in Windsurf to access the official daisyUI GitHub repository as an MCP source. This enables AI to reference the latest daisyUI code and documentation directly from the repository.

```json
{
  "mcpServers": {
    "daisyui-github": {
      "serverUrl": "https://gitmcp.io/saadeghi/daisyui"
    }
  }
}
```

--------------------------------

### Initialize a new Bun project

Source: https://daisyui.com/docs/install/bun

This command initializes a new Bun project in the current directory, creating a `package.json` file with default settings. It's the first step to set up any Bun-based application.

```shell
bun init -y
```

--------------------------------

### Install Electron, Tailwind CSS, and daisyUI via npm

Source: https://daisyui.com/docs/install/electron

This command installs all necessary project dependencies. It includes `electron` for building cross-platform desktop applications, `tailwindcss` and `@tailwindcss/cli` for the utility-first CSS framework, and `daisyui` for pre-built UI components.

```Terminal
npm install electron tailwindcss@latest @tailwindcss/cli@latest daisyui@latest
```

--------------------------------

### Combine Tailwind CSS and daisyUI Prefixes

Source: https://daisyui.com/docs/config

Use both Tailwind CSS prefix and daisyUI prefix together in the same configuration. daisyUI classes get both prefixes (e.g., 'btn' becomes 'tw:d-btn'), except theme-controller which only gets the daisyUI prefix.

```css
@import "tailwindcss" prefix(tw);
@plugin "daisyui" {
  prefix: "d-";
}
```

--------------------------------

### Implement DaisyUI Toggles and Checkboxes in HTML

Source: https://daisyui.com/tailwindplay

This snippet provides examples of DaisyUI form elements, specifically toggles and checkboxes. It shows a basic toggle and a primary-themed toggle, demonstrating how to use the `toggle` class for styling and `toggle-primary` for theme variations.

```html
<!-- toggle, checkbox, radio -->
<div class="p-4">
<input type="checkbox" class="toggle" />
<input type="checkbox" class="toggle toggle-primary" />
</div>
```

--------------------------------

### Fast Install Tailwind CSS and daisyUI

Source: https://daisyui.com/docs/install/django

These commands quickly download and set up Tailwind CSS and daisyUI. They fetch the necessary executables and bundles, then generate the initial `output.css` for the respective operating systems.

```Terminal
cd myapp/static/css && curl -sL daisyui.com/fast | bash
```

```PowerShell
cd myapp/static/css && powershell -c "irm daisyui.com/fast.ps1 | iex"
```

--------------------------------

### Apply daisyUI material theme to HTML element

Source: https://daisyui.com/blog/nexus-dashboard-template

Applies the material theme from daisyUI to the HTML document by setting the data-theme attribute. Requires Tailwind CSS 4 and daisyUI 5 to be properly installed.

```html
<html data-theme="material">
  <!-- content -->
</html>
```

--------------------------------

### Create new Solid project with degit

Source: https://daisyui.com/docs/install/solid

Initialize a new Solid.js project using the official template. This command clones the Solid.js JavaScript template into the current directory, providing a starter project structure.

```bash
npx degit solidjs/templates/js
```

--------------------------------

### Configure Claude Desktop for daisyUI GitMCP Server

Source: https://daisyui.com/docs/editor/claude

This configuration snippet adds the daisyUI GitMCP server to Claude desktop's `mcpServers` settings. It specifies the `npx` command with `mcp-remote` and the GitMCP repository URL `https://gitmcp.io/saadeghi/daisyui` as arguments. This setup allows Claude to interact with the GitMCP server for daisyUI-related queries, leveraging its specific knowledge base.

```json
{
  "mcpServers": {
    "daisyui-github": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://gitmcp.io/saadeghi/daisyui"]
    }
  }
}
```

--------------------------------

### Create new Astro project with npm

Source: https://daisyui.com/docs/install/astro

Initialize a new Astro project in the current directory using npm's create command. This sets up the basic Astro project structure and dependencies.

```bash
npm create astro@latest ./
```

--------------------------------

### Setup daisyUI GitMCP Server for Current Workspace

Source: https://daisyui.com/docs/editor/vscode

JSON configuration to add daisyUI GitMCP server to a specific VSCode workspace using SSE protocol. Create .vscode/mcp.json file in project root to enable AI assistance with daisyUI documentation in Agent Mode.

```json
{
  "servers": {
    "daisyUI": {
      "type": "sse",
      "url": "https://gitmcp.io/saadeghi/daisyui"
    }
  }
}
```

--------------------------------

### Install Headless UI for Vue and React

Source: https://daisyui.com/blog/how-to-use-headless-ui-and-daisyui

These commands demonstrate how to install the Headless UI library for both Vue and React projects using npm. Headless UI provides unstyled, accessible UI components that can be combined with styling libraries like daisyUI to add visual design.

```shell
npm install @headlessui/vue
```

```shell
npm install @headlessui/react
```

--------------------------------

### Setup Context7 MCP Server for Current Workspace

Source: https://daisyui.com/docs/editor/vscode

JSON configuration to add Context7 MCP server to a specific VSCode workspace. Create .vscode/mcp.json file in project root and add this configuration to enable AI assistance with daisyUI in Agent Mode.

```json
{
  "servers": {
    "context7": {
      "type": "stdio",
      "command": "npx",
      "args": [
        "-y",
        "@upstash/context7-mcp@latest"
      ]
    }
  }
}
```

--------------------------------

### Applying daisyUI Theming and Spacing with HTML Classes

Source: https://daisyui.com/pages/easy-css-library

This HTML example showcases how daisyUI simplifies design decisions by providing predefined classes for common UI elements. It demonstrates applying primary, secondary, and accent colors to buttons, and how card components automatically handle spacing and typography without explicit CSS rules.

```html
<!-- No color decisions needed -->
<button class="btn btn-primary">Primary Action</button>
<button class="btn btn-secondary">Secondary Action</button>
<button class="btn btn-accent">Accent Action</button>

<!-- No spacing decisions needed -->
<div class="card">
  <div class="card-body">
    <!-- Perfect spacing automatically -->
  </div>
</div>

<!-- No typography decisions needed -->
<h1 class="text-4xl font-bold">Heading</h1>
<p class="text-base">Body text with proper line height.</p>
```

--------------------------------

### Install daisyUI using various package managers

Source: https://daisyui.com/alternative/nuxtui

Instructions for installing the latest version of daisyUI as a development dependency using popular Node.js and Deno package managers. This step is required before configuring daisyUI in your project.

```npm
npm i -D daisyui@latest
```

```pnpm
pnpm add -D daisyui@latest
```

```yarn
yarn add -D daisyui@latest
```

```bun
bun add -D daisyui@latest
```

```deno
deno i -D npm:daisyui@latest
```

--------------------------------

### Import DaisyUI and Tailwind CSS with Theme Support

Source: https://daisyui.com/codepen

Loads DaisyUI version 5 component library and all available themes via CDN, along with Tailwind CSS browser build. This setup enables rapid UI development with pre-built components and theme switching capabilities.

```html
<!-- daisyUI -->
<link href="https://cdn.jsdelivr.net/npm/daisyui@5" rel="stylesheet" type="text/css" />

<!-- All daisyUI themes -->
<link href="https://cdn.jsdelivr.net/npm/daisyui@5/themes.css" rel="stylesheet" type="text/css" />

<!-- Tailwind CSS -->
<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
```

--------------------------------

### Create New Vike Project (npm)

Source: https://daisyui.com/docs/install/vike

Initializes a new Vike project in the current directory using npm. This command sets up the basic Vike project structure.

```bash
npm create vike ./
```

--------------------------------

### Add Prefix to All daisyUI Classes

Source: https://daisyui.com/docs/config

Prefix all daisyUI class names with a custom string to avoid naming conflicts. For example, with prefix 'd-', the 'btn' class becomes 'd-btn'.

```css
@plugin "daisyui" {
  prefix: "d-";
}
```

--------------------------------

### Enable daisyUI Configuration in CSS

Source: https://daisyui.com/docs/config

Convert daisyUI plugin syntax from semicolon to bracket notation to enable configuration options. This is the basic setup required before applying any configuration parameters.

```css
- @plugin "daisyui";
+ @plugin "daisyui" {
+ }
```

--------------------------------

### Create new Next.js project with npm

Source: https://daisyui.com/docs/install/nextjs

Initialize a new Next.js project in the current directory using npm create next-app. This sets up the basic Next.js project structure and configuration files needed for development.

```bash
npm create next-app@latest ./
```

--------------------------------

### Create New Vite Project with Vanilla Template

Source: https://daisyui.com/docs/install/vite

Initialize a new Vite project in the current directory using the vanilla JavaScript template. This command sets up the basic Vite project structure with minimal configuration.

```bash
npm create vite@latest ./ -- --template vanilla
```

--------------------------------

### Create a New Preact Project with Vite

Source: https://daisyui.com/docs/install/preact

This command initializes a new Preact project in the current directory using Vite. It sets up the basic project structure and dependencies for a Preact application, providing a modern development environment.

```bash
npm create vite@latest ./ -- --template preact
```

--------------------------------

### Configure daisyUI in Tailwind CSS

Source: https://daisyui.com/alternative/preline

Add daisyUI plugin to your Tailwind CSS configuration by importing it in your app.css file. This enables all daisyUI components and themes in your project.

```css
@import "tailwindcss";
@plugin "daisyui";
```

--------------------------------

### Create a new Deno Fresh project with Tailwind CSS

Source: https://daisyui.com/docs/install/fresh

Initializes a new Deno Fresh project in the current directory. This command uses `jsr` to set up the project, including Tailwind CSS integration and VS Code configuration.

```bash
deno run -Ar jsr:@fresh/init ./ --tailwind --vscode
```

--------------------------------

### Make Tailwind CSS Executable - Linux/MacOS

Source: https://daisyui.com/docs/install/standalone

Sets execute permissions on the Tailwind CSS Standalone executable file for Linux and MacOS systems using chmod command.

```bash
chmod +x tailwindcss
```

--------------------------------

### Create new Nuxt project with CLI

Source: https://daisyui.com/docs/install/nuxt

Initialize a new Nuxt project in the current directory using the latest version of Nuxi. This command scaffolds a basic Nuxt project structure with all necessary configuration files.

```bash
npx nuxi@latest init ./
```

--------------------------------

### Create New Rsbuild Project

Source: https://daisyui.com/docs/install/rsbuild

This command initializes a new Rsbuild project in the current directory. It uses `npm create` to scaffold the project, setting up the necessary file structure and initial configurations.

```bash
npm create rsbuild -d ./
```

--------------------------------

### Create a New Ruby on Rails Project

Source: https://daisyui.com/docs/install/rails

Initializes a new Ruby on Rails application and navigates into its directory, setting up the basic project structure. This command is the first step in creating any new Rails project.

```Terminal
rails new my-app
cd my-app
```

--------------------------------

### Styled Form Component with Extensive CSS Classes

Source: https://daisyui.com/pages/easy-css-library

Compares simple functional HTML (5 minutes) with extensively styled version (2 hours) using utility classes. Demonstrates how professional styling requires deep CSS knowledge and significant implementation time, creating a productivity bottleneck in feature development.

```html
<!-- The functionality: 5 minutes -->
<form onSubmit={handleSubmit}>
  <input name="email" type="email" />
  <button type="submit">Subscribe</button>
</form>

<!-- The styling: 2 hours -->
<form className="bg-white p-8 rounded-lg shadow-lg max-w-md mx-auto">
  <div className="mb-6">
    <label className="block text-gray-700 text-sm font-bold mb-2">
      Email Address
    </label>
    <input 
      className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline focus:border-blue-500 transition duration-200"
      name="email" 
      type="email" 
    />
  </div>
  <button 
    className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline transition duration-200 w-full"
    type="submit"
  >
    Subscribe
  </button>
</form>
```

--------------------------------

### Customize dashboard layout CSS variables

Source: https://daisyui.com/blog/nexus-dashboard-template

Modifies layout-related CSS variables in styles/custom/layout.css. Enables customization of sidebar width, topbar, rightbar, and content area dimensions and styling.

```css
:root {
  /* update: sidebar width,as you want */
  --layout-sidebar-width: 256px;
}

/* update: layout related styles ... */
```

--------------------------------

### Create new Vite React project

Source: https://daisyui.com/docs/install/react

Initialize a new React project using Vite template in the current directory. This command scaffolds a basic React application with Vite as the build tool and development server.

```bash
npm create vite@latest ./ -- --template react
```

--------------------------------

### Run Django Development Server

Source: https://daisyui.com/docs/install/django

Starts the Django development server on the default port (8000). Execute this command in a terminal to begin serving your daisyUI-enabled Django application. The server will automatically reload on code changes.

```bash
python manage.py runserver
```

--------------------------------

### Initialize a New Next.js Project with `create-next-app`

Source: https://daisyui.com/resources/videos/daisyui-and-tailwind-css-crash-course-daisyui-tutorial-for-nextjs-and-react-th8oswsaq6q

This command-line instruction uses `npx` to create a new Next.js application. It fetches and executes the `create-next-app` package, setting up a fresh project directory. Users should replace `[project-folder-name]` with their desired project name.

```bash
npx create-next-app@latest [project-folder-name]
```

--------------------------------

### Configure daisyUI in Tailwind CSS config

Source: https://daisyui.com/blog/what-is-daisyui

Add daisyUI to the plugins array in your tailwind.config.js file to enable daisyUI component classes in your Tailwind CSS project. This configuration step is required after installing the daisyUI package.

```javascript
module.exports = {
  //...
  plugins: [require("daisyui")],
}
```

--------------------------------

### Add CSS build script to package.json

Source: https://daisyui.com/docs/install/cli

Configure an npm script in package.json to compile CSS using Tailwind CSS CLI. The script takes app.css as input and outputs the compiled CSS to public/output.css.

```json
{
  "scripts": {
    "build:css": "npx @tailwindcss/cli -i app.css -o public/output.css"
  }
}
```

--------------------------------

### Initialize Node.js Project and Configure Eleventy Scripts

Source: https://daisyui.com/docs/install/11ty

This snippet initializes a new Node.js project using `npm init -y` and then adds `dev` and `build` scripts to the `package.json` file. The `dev` script runs Eleventy with a development server, while the `build` script compiles the site for production.

```Terminal
npm init -y
npm pkg set scripts.dev="eleventy --serve"
npm pkg set scripts.build="eleventy"
```

--------------------------------

### Link compiled CSS in HTML file

Source: https://daisyui.com/docs/install/cli

Add a link tag in your HTML file to reference the compiled CSS output. This makes all Tailwind CSS utilities and daisyUI component classes available in your HTML markup.

```html
<link href="./output.css" rel="stylesheet">
```

--------------------------------

### Basic Button Styling with CSS

Source: https://daisyui.com/pages/easy-css-library

Demonstrates the complexity of creating a professional interactive button with CSS. Shows 25+ CSS properties required for a single button component including layout, typography, interactions, and states. Illustrates why CSS knowledge requirements are overwhelming for beginners.

```css
.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.5rem 1rem;
  border: 1px solid transparent;
  border-radius: 0.375rem;
  font-size: 0.875rem;
  font-weight: 500;
  line-height: 1.25rem;
  text-decoration: none;
  cursor: pointer;
  transition: all 0.15s ease-in-out;
  user-select: none;
  white-space: nowrap;
}

.button:hover {
  background-color: #e5e7eb;
}

.button:focus {
  outline: 2px solid transparent;
  outline-offset: 2px;
  box-shadow: 0 0 0 2px #3b82f6;
}

.button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.button:active {
  transform: translateY(0.5px);
}
```

--------------------------------

### Create new React Router project with npm

Source: https://daisyui.com/docs/install/reactrouter

Initialize a new React Router project in the current directory using npm's create command. This sets up the basic project structure and dependencies needed for a React Router application.

```bash
npm create react-router@latest ./
```