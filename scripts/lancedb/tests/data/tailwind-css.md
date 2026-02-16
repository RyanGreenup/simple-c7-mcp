### Basic HTML Setup with Tailwind CSS Utility Classes

Source: https://v3.tailwindcss.com/docs/installation/using-postcss

Create an HTML document that links to the compiled Tailwind CSS file and uses Tailwind utility classes for styling. This example demonstrates how to apply responsive and styling utilities like text-3xl, font-bold, and underline to HTML elements.

```html
<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="/dist/main.css" rel="stylesheet">
</head>
<body>
  <h1 class="text-3xl font-bold underline">
    Hello world!
  </h1>
</body>
</html>
```

--------------------------------

### Start Astro Development Server

Source: https://v3.tailwindcss.com/docs/guides/astro

Launch the development server to run your Astro project locally. This command starts the build process and enables hot module reloading for development.

```bash
npm run dev
```

--------------------------------

### Start Parcel Development Server

Source: https://v3.tailwindcss.com/docs/guides/parcel

Run the Parcel build process with the entry point set to src/index.html. This starts the development server and watches for file changes to rebuild automatically.

```bash
npx parcel src/index.html
```

--------------------------------

### Start Tailwind CLI Build Process

Source: https://v3.tailwindcss.com/docs/index

Runs the Tailwind CLI to process the input CSS file, scan template files for classes, and output the compiled CSS to a specified file. The `--watch` flag enables continuous rebuilding during development.

```Terminal
npx tailwindcss -i ./src/input.css -o ./src/output.css --watch
```

--------------------------------

### Start Development Server

Source: https://v3.tailwindcss.com/docs/guides/create-react-app

Run the development server to begin building your application with Tailwind CSS. The build process will watch for changes and recompile styles automatically.

```bash
npm run start
```

--------------------------------

### Start Development Build Process

Source: https://v3.tailwindcss.com/docs/guides/symfony

Run the npm watch script to start the development build process. This watches for file changes and rebuilds assets automatically.

```bash
npm run watch
```

--------------------------------

### Create React App Project Setup

Source: https://v3.tailwindcss.com/docs/guides/create-react-app

Initialize a new React project using Create React App v5.0 or higher. This command creates a new directory with a basic React application structure ready for Tailwind CSS integration.

```bash
npx create-react-app my-project
cd my-project
```

--------------------------------

### Create a new Laravel project using Composer

Source: https://v3.tailwindcss.com/docs/guides/laravel

This command initializes a new Laravel application named 'my-project' using Composer. After creation, it navigates into the project directory, preparing the environment for subsequent setup steps.

```Terminal
composer create-project laravel/laravel my-project
cd my-project
```

--------------------------------

### Create New Phoenix Project

Source: https://v3.tailwindcss.com/docs/guides/phoenix

Start by creating a new Phoenix project if you don't have one set up already, then navigate into its directory. This command initializes a standard Phoenix application structure.

```Terminal
mix phx.new myproject
cd myproject
```

--------------------------------

### Start Development Build Process

Source: https://v3.tailwindcss.com/docs/guides/ruby-on-rails

Run the development server with the build process to watch for file changes and compile Tailwind CSS in real-time.

```bash
./bin/dev
```

--------------------------------

### Start Gatsby development server

Source: https://v3.tailwindcss.com/docs/guides/gatsby

This command initiates the Gatsby development server, compiling your project and making it accessible locally. It allows you to see your changes in real-time as you develop, with Tailwind CSS styles applied.

```Terminal
gatsby develop
```

--------------------------------

### Start the Angular development server

Source: https://v3.tailwindcss.com/docs/guides/angular

This command starts the Angular development server, which compiles the application and serves it locally. It also watches for file changes and automatically reloads the browser, facilitating the development process.

```Terminal
ng serve
```

--------------------------------

### Start Phoenix Server with Tailwind CSS Build

Source: https://v3.tailwindcss.com/docs/guides/phoenix

Run `mix phx.server` to start your Phoenix development server. This command will also trigger the Tailwind CSS build process, compiling your styles and applying them to your application for live preview.

```Terminal
mix phx.server
```

--------------------------------

### Create Qwik Project with npm

Source: https://v3.tailwindcss.com/docs/guides/qwik

Initialize a new Qwik project using Create Qwik. This command scaffolds the project structure and installs base dependencies required for Qwik development.

```bash
npm create qwik@latest my-project
cd my-project
```

--------------------------------

### Enable First-Party Plugins via Query Parameter

Source: https://v3.tailwindcss.com/docs/installation/play-cdn

Load official Tailwind CSS plugins (forms, typography, aspect-ratio, line-clamp, container-queries) by appending them as query parameters to the Play CDN script URL. This example enables multiple plugins simultaneously to extend Tailwind's default functionality without additional configuration.

```html
<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://cdn.tailwindcss.com?plugins=forms,typography,aspect-ratio,line-clamp,container-queries"></script>
</head>
<body>
  <div class="prose">
    <!-- ... -->
  </div>
</body>
</html>
```

--------------------------------

### Install `postcss-import` Plugin via NPM

Source: https://v3.tailwindcss.com/docs/using-with-preprocessors

This command installs the `postcss-import` plugin as a development dependency using npm. It is essential for enabling build-time CSS `@import` processing within a PostCSS setup, allowing for modular CSS organization.

```bash
npm install -D postcss-import
```

--------------------------------

### Create SvelteKit Project

Source: https://v3.tailwindcss.com/docs/guides/sveltekit

Initialize a new SvelteKit project using the official CLI tool. This creates the project directory structure and installs base dependencies required for a SvelteKit application.

```bash
npx sv create my-project
cd my-project
```

--------------------------------

### Create Symfony Project

Source: https://v3.tailwindcss.com/docs/guides/symfony

Initialize a new Symfony web project using the Symfony Installer. This creates the basic project structure needed for a Symfony application.

```bash
symfony new --webapp my-project
cd my-project
```

--------------------------------

### Control grid column placement with Tailwind CSS `col-start` and `col-end`

Source: https://v3.tailwindcss.com/docs/grid-column

This example illustrates the use of `col-start-*` and `col-end-*` utilities to position grid items by specifying their starting and ending grid lines. These can also be combined with `col-span-*` for more precise control over column placement and spanning.

```html
<div class="grid grid-cols-6 gap-4">
  <div class="col-start-2 col-span-4 ...">01</div>
  <div class="col-start-1 col-end-3 ...">02</div>
  <div class="col-end-7 col-span-2 ...">03</div>
  <div class="col-start-1 col-end-7 ...">04</div>
</div>
```

--------------------------------

### Button HTML Before and After @apply Extraction

Source: https://v3.tailwindcss.com/docs/reusing-styles

Shows the HTML markup for a button component before and after extracting utility classes into a custom CSS class. The before example uses inline Tailwind utilities, while the after example uses the extracted .btn-primary class for cleaner markup.

```HTML
<!-- Before extracting a custom class -->
<button class="py-2 px-5 bg-violet-500 text-white font-semibold rounded-full shadow-md hover:bg-violet-700 focus:outline-none focus:ring focus:ring-violet-400 focus:ring-opacity-75">
  Save changes
</button>

<!-- After extracting a custom class -->
<button class="btn-primary">
  Save changes
</button>
```

--------------------------------

### Style Qwik Component with Tailwind Utility Classes

Source: https://v3.tailwindcss.com/docs/guides/qwik

Create a Qwik component using the component$ function and apply Tailwind CSS utility classes via the class attribute. This example demonstrates basic text styling with size, weight, and decoration utilities.

```typescript
import { component$ } from '@builder.io/qwik'

export default component$(() => {
  return (
    <h1 class="text-3xl font-bold underline">
      Hello World!
    </h1>
  )
})
```

--------------------------------

### Create a new Nuxt.js project using nuxi init

Source: https://v3.tailwindcss.com/docs/guides/nuxtjs

This command initializes a new Nuxt.js project with a specified name using the Nuxt Command Line Interface (CLI). After creation, it navigates into the new project directory.

```bash
npx nuxi init my-project
cd my-project
```

--------------------------------

### React Component with Tailwind Utility Classes

Source: https://v3.tailwindcss.com/docs/guides/create-react-app

Example React component demonstrating basic Tailwind CSS utility classes for styling. Uses className prop with Tailwind utilities for text size, font weight, and text decoration.

```javascript
export default function App() {
  return (
    <h1 className="text-3xl font-bold underline">
      Hello world!
    </h1>
  )
}
```

--------------------------------

### Install Tailwind CSS and Dependencies

Source: https://v3.tailwindcss.com/docs/guides/symfony

Install Tailwind CSS v3, PostCSS, PostCSS Loader, and Autoprefixer via npm. Then run the Tailwind init command to generate configuration files.

```bash
npm install -D tailwindcss@3 postcss postcss-loader autoprefixer
npx tailwindcss init -p
```

--------------------------------

### Configure Tailwind Template Paths

Source: https://v3.tailwindcss.com/docs/installation/using-postcss

Specify the paths to all template files in tailwind.config.js so Tailwind can scan them for class names and generate only the CSS needed. This configuration uses glob patterns to match HTML and JavaScript files in the src directory.

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

--------------------------------

### Add Play CDN Script to HTML

Source: https://v3.tailwindcss.com/docs/installation/play-cdn

Basic setup to use Tailwind CSS in the browser by adding the Play CDN script tag to the HTML head. This enables immediate access to Tailwind's utility classes for styling without any build configuration. Designed for development and prototyping only, not recommended for production use.

```html
<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
  <h1 class="text-3xl font-bold underline">
    Hello world!
  </h1>
</body>
</html>
```

--------------------------------

### Create Remix Project

Source: https://v3.tailwindcss.com/docs/guides/remix

Initialize a new Remix project using the Create Remix CLI tool. This command creates a new directory with the project name and sets up the basic Remix project structure.

```bash
npx create-remix@latest my-project
cd my-project
```

--------------------------------

### Create Next.js Project with TypeScript

Source: https://v3.tailwindcss.com/docs/guides/nextjs

Initialize a new Next.js project with TypeScript and ESLint enabled using Create Next App. This command creates the project directory structure and installs necessary dependencies.

```bash
npx create-next-app@latest my-project --typescript --eslint
cd my-project
```

--------------------------------

### Install Tailwind CSS and Dependencies

Source: https://v3.tailwindcss.com/docs/guides/remix

Install Tailwind CSS v3 and required PostCSS plugins as development dependencies, then generate configuration files. The init command creates tailwind.config.ts and postcss.config.js automatically.

```bash
npm install -D tailwindcss@3 postcss autoprefixer
npx tailwindcss init --ts -p
```

--------------------------------

### Create a new Angular project using Angular CLI

Source: https://v3.tailwindcss.com/docs/guides/angular

This command initializes a new Angular application with the specified project name. It also navigates into the newly created project directory, preparing for subsequent installation steps.

```Terminal
ng new my-project
cd my-project
```

--------------------------------

### Create Astro Project with npm

Source: https://v3.tailwindcss.com/docs/guides/astro

Initialize a new Astro project using the create-astro CLI tool. This command creates a new directory with the project name and sets up the basic Astro project structure.

```bash
npm create astro@latest my-project
cd my-project
```

--------------------------------

### Create a new SolidJS project using Vite

Source: https://v3.tailwindcss.com/docs/guides/solidjs

This command initializes a new SolidJS project using the Vite template for JavaScript and then navigates into the newly created project directory. It's the foundational step for setting up your development environment.

```bash
npx degit solidjs/templates/js my-project
cd my-project
```

--------------------------------

### Create Parcel Project with npm

Source: https://v3.tailwindcss.com/docs/guides/parcel

Initialize a new Parcel project by creating a project directory, initializing npm, installing Parcel as a dev dependency, and setting up the source directory structure. This establishes the foundation for adding Tailwind CSS.

```bash
mkdir my-project
cd my-project
npm init -y
npm install -D parcel
mkdir src
touch src/index.html
```

--------------------------------

### Create Vite React Project

Source: https://v3.tailwindcss.com/docs/guides/vite

Initialize a new React project using Create Vite with the React template. This command creates a new directory with all necessary Vite configuration and React dependencies pre-configured.

```bash
npm create vite@latest my-project -- --template react
cd my-project
```

--------------------------------

### Install Tailwind CSS and Dependencies

Source: https://v3.tailwindcss.com/docs/guides/nextjs

Install Tailwind CSS v3 along with peer dependencies (PostCSS and Autoprefixer) as development dependencies. The init command generates tailwind.config.js and postcss.config.js configuration files.

```bash
npm install -D tailwindcss@3 postcss autoprefixer
npx tailwindcss init -p
```

--------------------------------

### Install Tailwind CSS via npm

Source: https://v3.tailwindcss.com/docs/guides/create-react-app

Install Tailwind CSS as a development dependency and generate the default configuration file. The init command creates a tailwind.config.js file needed for customization.

```bash
npm install -D tailwindcss@3
npx tailwindcss init
```

--------------------------------

### Install Tailwind CSS and initialize configuration in Angular

Source: https://v3.tailwindcss.com/docs/guides/angular

This step installs `tailwindcss`, `postcss`, and `autoprefixer` as development dependencies via npm. After installation, it runs the `npx tailwindcss init` command to generate a `tailwind.config.js` file, which is crucial for configuring Tailwind CSS.

```Terminal
npm install -D tailwindcss@3 postcss autoprefixer
npx tailwindcss init
```

--------------------------------

### Create a new Rspack project using npm

Source: https://v3.tailwindcss.com/docs/guides/rspack

This command initializes a new Rspack project using the `rspack@latest` CLI. It sets up the basic project structure and necessary configuration files.

```bash
npm create rspack@latest
```

--------------------------------

### Implementing a Chat Notification UI with Traditional CSS

Source: https://v3.tailwindcss.com/docs/reusing-styles

This example shows a chat notification UI using traditional HTML structure and corresponding CSS classes. It highlights the need to duplicate the HTML structure every time the component is used, even when custom CSS is defined, illustrating a limitation compared to component-based approaches.

```html
<!-- Even with custom CSS, you still need to duplicate this HTML structure -->
<div class="chat-notification">
  <div class="chat-notification-logo-wrapper">
    <img class="chat-notification-logo" src="/img/logo.svg" alt="ChitChat Logo">
  </div>
  <div class="chat-notification-content">
    <div class="chat-notification-title">ChitChat</div>
    <p class="chat-notification-message">You have a new message!</p>
  </div>
</div>

<style>
  .chat-notification { /* ... */ }
  .chat-notification-logo-wrapper { /* ... */ }
  .chat-notification-logo { /* ... */ }
  .chat-notification-content { /* ... */ }
  .chat-notification-title { /* ... */ }
  .chat-notification-message { /* ... */ }
</style>
```

--------------------------------

### Initialize a new AdonisJS project using npm

Source: https://v3.tailwindcss.com/docs/guides/adonisjs

This command creates a new AdonisJS project named 'my-project' with the 'web' kit, which includes common web development tools. It sets up the basic project structure and dependencies.

```bash
npm init adonisjs@latest my-project -- --kit=webcd my-project
```

--------------------------------

### Install Tailwind CSS CLI with Phoenix Mix Task

Source: https://v3.tailwindcss.com/docs/guides/phoenix

Run the `mix tailwind.install` command to download the standalone Tailwind CLI executable. This command also generates a default `tailwind.config.js` file in your `./assets` directory, setting up the core configuration for Tailwind CSS.

```Terminal
mix tailwind.install
```

--------------------------------

### Install Webpack Encore Bundle

Source: https://v3.tailwindcss.com/docs/guides/symfony

Install the Symfony Webpack Encore bundle using Composer. This package handles building and managing assets in your Symfony project.

```bash
composer require symfony/webpack-encore-bundle
```

--------------------------------

### Install Tailwind CSS and PostCSS dependencies for Gatsby

Source: https://v3.tailwindcss.com/docs/guides/gatsby

This command installs `tailwindcss`, `postcss`, `autoprefixer`, and `gatsby-plugin-postcss` as development dependencies using npm. It then initializes Tailwind CSS, generating `tailwind.config.js` and `postcss.config.js` for further configuration.

```Terminal
npm install -D tailwindcss@3 postcss autoprefixer gatsby-plugin-postcss
npx tailwindcss init -p
```

--------------------------------

### Create New Rails Project

Source: https://v3.tailwindcss.com/docs/guides/ruby-on-rails

Initialize a new Rails project using the Rails command line interface. This creates the basic project structure needed for a Rails application.

```bash
rails new my-project
cd my-project
```

--------------------------------

### Installing Autoprefixer as a Development Dependency

Source: https://v3.tailwindcss.com/docs/browser-support

This command demonstrates how to install `autoprefixer` using npm, saving it as a development dependency. Autoprefixer is a PostCSS plugin that automatically adds vendor prefixes to CSS rules, ensuring wider browser support without manual intervention.

```bash
npm install -D autoprefixer
```

--------------------------------

### Install Tailwind CSS and PostCSS dependencies for AdonisJS

Source: https://v3.tailwindcss.com/docs/guides/adonisjs

This command installs Tailwind CSS, PostCSS, and Autoprefixer as development dependencies. It then initializes Tailwind CSS, generating `tailwind.config.js` and `postcss.config.js` files for configuration.

```bash
npm install -D tailwindcss@3 postcss autoprefixernpx tailwindcss init -p
```

--------------------------------

### Install Tailwind CSS and PostCSS

Source: https://v3.tailwindcss.com/docs/guides/parcel

Install Tailwind CSS v3 and PostCSS as dev dependencies via npm, then generate the default tailwind.config.js configuration file using the Tailwind CLI init command.

```bash
npm install -D tailwindcss@3 postcss
npx tailwindcss init
```

--------------------------------

### Install Tailwind CSS with Astro Integration

Source: https://v3.tailwindcss.com/docs/guides/astro

Install Tailwind CSS and the official Astro integration using the astro add command. This automatically installs tailwindcss, @astrojs/tailwind, and generates a tailwind.config.cjs configuration file.

```bash
npx astro add tailwind
```

--------------------------------

### Create a new Gatsby project using Gatsby CLI

Source: https://v3.tailwindcss.com/docs/guides/gatsby

This command initializes a new Gatsby project with a specified name and then navigates into the project directory. It's the first step to set up a Gatsby application before integrating Tailwind CSS.

```Terminal
gatsby new my-project
cd my-project
```

--------------------------------

### Install Tailwind CSS and PostCSS dependencies in Ember.js

Source: https://v3.tailwindcss.com/docs/guides/emberjs

This command installs Tailwind CSS, PostCSS, postcss-loader, and autoprefixer as development dependencies. Following installation, it initializes Tailwind CSS, generating `tailwind.config.js` and `postcss.config.js` files for project-specific configuration.

```bash
npm install -D tailwindcss@3 postcss postcss-loader autoprefixernpx tailwindcss init -p
```

--------------------------------

### Create a new Meteor project using CLI

Source: https://v3.tailwindcss.com/docs/guides/meteor

This command initializes a new Meteor application named 'my-project' and then navigates into the newly created project directory. It's the first step to set up your development environment.

```terminal
meteor create my-project
cd my-project
```

--------------------------------

### Customize Tailwind CSS `gridRowStart` for `row-start-*` utilities

Source: https://v3.tailwindcss.com/docs/grid-row

This example illustrates how to extend the `gridRowStart` section within your Tailwind CSS theme configuration. It enables the creation of custom `row-start-*` utilities by mapping specific numeric values to their corresponding grid line positions.

```javascript
module.exports = {
  theme: {
    extend: {
      gridRowStart: {
        '8': '8',
        '9': '9',
        '10': '10',
        '11': '11',
        '12': '12',
        '13': '13'
      }
    }
  }
}
```

--------------------------------

### Integrate Compiled Tailwind CSS into HTML

Source: https://v3.tailwindcss.com/docs/index

Links the generated `output.css` file in the `<head>` section of an HTML document. This step makes Tailwind's utility classes available for styling your content directly within your HTML markup.

```html
<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="./output.css" rel="stylesheet">
</head>
<body>
  <h1 class="text-3xl font-bold underline">
    Hello world!
  </h1>
</body>
</html>
```

--------------------------------

### Integrate Official Tailwind CSS Plugins into tailwind.config.js

Source: https://v3.tailwindcss.com/docs/plugins

This example illustrates how to add official Tailwind CSS plugins to your project. After installing them via npm, you can include them in the `plugins` array within your `tailwind.config.js` file, enabling their features for use in your application.

```JavaScript
/** @type {import('tailwindcss').Config} */
module.exports = {
  // ...
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
    require('@tailwindcss/aspect-ratio'),
    require('@tailwindcss/container-queries'),
  ]
}
```

--------------------------------

### Align Grid Item to Start with place-self-start

Source: https://v3.tailwindcss.com/docs/place-self

Shows how to use place-self-start to align a grid item to the start position on both horizontal and vertical axes. Useful for positioning items at the top-left corner of their grid cell.

```html
<div class="grid grid-cols-3 gap-4 ...">
  <div>01</div>
  <div class="place-self-start ...">02</div>
  <div>03</div>
  <div>04</div>
  <div>05</div>
  <div>06</div>
</div>
```

--------------------------------

### Use Tailwind Utility Classes in React Component

Source: https://v3.tailwindcss.com/docs/guides/remix

Apply Tailwind CSS utility classes to React components using the className attribute. This example demonstrates basic text styling with Tailwind's responsive and utility classes.

```typescript
export default function Index() {
  return (
    <h1 className="text-3xl font-bold underline">
      Hello world!
    </h1>
  )
}
```

--------------------------------

### Create a new Ember.js project using Ember CLI

Source: https://v3.tailwindcss.com/docs/guides/emberjs

This command initializes a new Ember.js project named 'my-project' with Embroider support and without a welcome page. It then navigates into the newly created project directory, preparing it for further configuration.

```bash
npx ember-cli new my-project --embroider --no-welcomecd my-project
```

--------------------------------

### Override Component Classes with Tailwind Utilities

Source: https://v3.tailwindcss.com/docs/adding-custom-styles

Demonstrates how utility classes can override component styles defined in the components layer. In this example, the rounded-none utility overrides the border-radius from the card component.

```HTML
<!-- Will look like a card, but with square corners -->
<div class="card rounded-none">
  <!-- ... -->
</div>
```

--------------------------------

### Customize Tailwind Config with Theme Extension

Source: https://v3.tailwindcss.com/docs/installation/play-cdn

Extend the default Tailwind theme by modifying the tailwind.config object within a script tag. This example adds a custom color 'clifford' that can be used in utility classes. Allows design token customization directly in HTML without requiring a build step.

```html
<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            clifford: '#da373d',
          }
        }
      }
    }
  </script>
</head>
<body>
  <h1 class="text-3xl font-bold underline text-clifford">
    Hello world!
  </h1>
</body>
</html>
```

--------------------------------

### Apply Tailwind CSS Utility Classes in Astro

Source: https://v3.tailwindcss.com/docs/guides/astro

Use Tailwind CSS utility classes to style HTML elements in Astro components. This example demonstrates applying text sizing, font weight, and text decoration utilities to a heading element.

```astro
<h1 class="text-3xl font-bold underline">
  Hello world!
</h1>
```

--------------------------------

### Place Items Start - Tailwind CSS Grid Alignment

Source: https://v3.tailwindcss.com/docs/place-items

Aligns grid items to the start of their grid areas on both axes using the place-items-start utility class. Creates a 3-column grid layout with 4px gaps and positions all items at the start position.

```html
<div class="grid grid-cols-3 gap-4 place-items-start ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
  <div>04</div>
  <div>05</div>
  <div>06</div>
</div>
```

--------------------------------

### Install Tailwind CSS Typography Plugin

Source: https://v3.tailwindcss.com/docs/typography-plugin

Install the @tailwindcss/typography package from npm as a development dependency. This plugin provides prose classes for styling vanilla HTML content.

```bash
npm install -D @tailwindcss/typography
```

--------------------------------

### Examples of Tailwind CSS Prefixed Classes

Source: https://v3.tailwindcss.com/docs/configuration

Illustrates the practical application and output of the `prefix` configuration. This includes how prefixed classes appear in generated CSS, their usage in HTML, and how they interact with variant modifiers and negative values.

```css
.tw-text-left {
  text-align: left;
}
.tw-text-center {
  text-align: center;
}
.tw-text-right {
  text-align: right;
}
/* etc. */
```

```html
<div class="tw-text-lg md:tw-text-xl tw-bg-red-500 hover:tw-bg-blue-500">
  <!-- -->
</div>
```

```html
<div class="-tw-mt-8">
  <!-- -->
</div>
```

--------------------------------

### Use arbitrary grid column values in HTML

Source: https://v3.tailwindcss.com/docs/grid-column

Apply one-off grid column values directly in HTML using square bracket notation without modifying the theme config. This example uses an arbitrary col-[16_/_span_16] utility class for a custom grid span.

```html
<div class="col-[16_/_span_16]">
  <!-- ... -->
</div>
```

--------------------------------

### Example of using Tailwind CSS classes in a SolidJS component

Source: https://v3.tailwindcss.com/docs/guides/solidjs

This SolidJS component demonstrates how to apply Tailwind CSS utility classes directly to HTML elements within your JSX. It shows a basic `h1` element styled with bold text, a large font size, and an underline, illustrating immediate usage of Tailwind.

```jsx
export default function App() {
  return (
    <h1 class="text-3xl font-bold underline">
      Hello world!
    </h1>
  )
}
```

--------------------------------

### Place Content Start - Tailwind CSS Grid Alignment

Source: https://v3.tailwindcss.com/docs/place-content

Packs grid items against the start of the block axis using the place-content-start utility class. Aligns a 2-column grid with 4 items to the top of the container. Useful for top-aligned grid layouts.

```html
<div class="grid grid-cols-2 gap-4 place-content-start h-48 ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
  <div>04</div>
</div>
```

--------------------------------

### Include compiled CSS and use Tailwind classes in app.blade.php

Source: https://v3.tailwindcss.com/docs/guides/laravel

This HTML snippet for `app.blade.php` demonstrates how to include the compiled CSS using Laravel Vite's `@vite` directive within the `<head>` section. It also shows an example of applying Tailwind CSS utility classes to an `<h1>` element.

```HTML
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  @vite('resources/css/app.css')
</head>
<body>
  <h1 class="text-3xl font-bold underline">
    Hello world!
  </h1>
</body>
</html>
```

--------------------------------

### Generate PostCSS and Tailwind CSS config files via CLI

Source: https://v3.tailwindcss.com/docs/configuration

Using the `-p` flag with the `init` command generates both a `tailwind.config.js` and a basic `postcss.config.js` file. This streamlines the setup process for projects using PostCSS with Tailwind CSS.

```bash
npx tailwindcss init -p
```

--------------------------------

### Add Tailwind Plugin Dependency to Phoenix

Source: https://v3.tailwindcss.com/docs/guides/phoenix

Add the `:tailwind` dependency to your `mix.exs` file to integrate the Tailwind CSS plugin into your Phoenix project. After adding, run `mix deps.get` to fetch and install the new dependency.

```Elixir
defp deps do
  [
    {:tailwind, "~> 0.1", runtime: Mix.env() == :dev}
  ]
end
```

--------------------------------

### Define Gradient Starting Color with from-* Utility

Source: https://v3.tailwindcss.com/docs/gradient-color-stops

Sets the starting color of a gradient using Tailwind's from-* utilities. The example demonstrates applying an indigo-500 starting color to a left-to-right gradient. This utility sets the --tw-gradient-from CSS variable which defines where the gradient begins.

```html
<div class="bg-gradient-to-r from-indigo-500 ..."></div>
```

--------------------------------

### Import CSS in SvelteKit Layout

Source: https://v3.tailwindcss.com/docs/guides/sveltekit

Create a root layout component (+layout.svelte) and import the app.css file to make Tailwind styles available globally throughout the application.

```svelte
<script>
  import "../app.css";
</script>

<slot />
```

--------------------------------

### Apply Percentage Sizing with Tailwind CSS

Source: https://v3.tailwindcss.com/docs/size

This example shows how to use the `size-full` utility to make an element take up 100% of its parent's width and height. This is useful for creating responsive layouts where child elements should fill their container.

```html
<div class="h-56 p-2 ...">
  <div class="size-full ...">size-full</div>
</div>
```

--------------------------------

### Position Grid Rows with Tailwind CSS `row-start` and `row-end`

Source: https://v3.tailwindcss.com/docs/grid-row

Illustrates how to use `row-start-*` and `row-end-*` utilities to precisely position grid items by specifying their start and end grid lines. This can also be combined with `row-span-*` utilities to define both position and size within the grid.

```html
<div class="grid grid-rows-3 grid-flow-col gap-4">
  <div class="row-start-2 row-span-2 ...">01</div>
  <div class="row-end-3 row-span-2 ...">02</div>
  <div class="row-start-1 row-end-4 ...">03</div>
</div>
```

--------------------------------

### Example HTML Structure with Tailwind CSS Classes

Source: https://v3.tailwindcss.com/docs/content-configuration

Demonstrates how Tailwind CSS classes are applied directly within HTML attributes. This example highlights various utility classes for layout, styling, and responsiveness, which Tailwind's regex scanner can easily detect.

```html
<div class="md:flex">
  <div class="md:flex-shrink-0">
    <img class="rounded-lg md:w-56" src="/img/shopping.jpg" alt="Woman paying for a purchase">
  </div>
  <div class="mt-4 md:mt-0 md:ml-6">
    <div class="uppercase tracking-wide text-sm text-indigo-600 font-bold">
      Marketing
    </div>
    <a href="/get-started" class="block mt-1 text-lg leading-tight font-semibold text-gray-900 hover:underline">
      Finding customers for your new business
    </a>
    <p class="mt-2 text-gray-600">
      Getting a new business off the ground is a lot of hard work.
      Here are five ideas you can use to find your first customers.
    </p>
  </div>
</div>
```

--------------------------------

### Generate default Tailwind CSS configuration file using CLI

Source: https://v3.tailwindcss.com/docs/configuration

This command initializes a basic `tailwind.config.js` file at the root of your project. It's the standard way to set up Tailwind CSS configuration, providing a minimal starting point for customization.

```bash
npx tailwindcss init
```

--------------------------------

### Use Tailwind Utility Classes in React Component

Source: https://v3.tailwindcss.com/docs/guides/nextjs

Apply Tailwind CSS utility classes to React components using the className attribute. This example demonstrates basic text styling with size, weight, and decoration utilities.

```typescript
export default function Home() {
  return (
    <h1 className="text-3xl font-bold underline">
      Hello world!
    </h1>
  )
}
```

--------------------------------

### Configure Tailwind Template Paths

Source: https://v3.tailwindcss.com/docs/guides/qwik

Configure content paths in tailwind.config.js to specify which template files Tailwind should scan for class names. This enables Tailwind to generate only the CSS utilities used in your project.

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{js,ts,jsx,tsx,mdx}'],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

--------------------------------

### Configure Tailwind CSS Template Paths in `tailwind.config.js`

Source: https://v3.tailwindcss.com/docs/index

Updates the `content` array in `tailwind.config.js` to specify the files where Tailwind CSS should scan for utility classes. This ensures that only the necessary CSS is generated and included in your final build.

```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

--------------------------------

### Apply justify-start utility in Tailwind CSS

Source: https://v3.tailwindcss.com/docs/justify-content

Demonstrates how to use the `justify-start` utility class in Tailwind CSS to align items at the beginning of a container's main axis within a flexbox layout. This positions the content towards the start of the writing direction.

```html
<div class="flex justify-start ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
</div>
```

--------------------------------

### Align Content Start with Tailwind CSS Grid

Source: https://v3.tailwindcss.com/docs/align-content

Packs grid rows against the start of the cross axis using the content-start utility class. Creates a 3-column grid with 5 items that align to the top of the container with a fixed height of 14rem (56 units).

```html
<div class="h-56 grid grid-cols-3 gap-4 content-start ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
  <div>04</div>
  <div>05</div>
</div>
```

--------------------------------

### Justify Items with Hover State - Tailwind CSS Conditional Styling

Source: https://v3.tailwindcss.com/docs/justify-items

Applies justify-items alignment conditionally on hover using the hover: variant modifier. This example changes grid item alignment from start to center when the user hovers over the grid container.

```html
<div class="grid justify-items-start hover:justify-items-center">
  <!-- ... -->
</div>
```

--------------------------------

### Apply Tailwind CSS classes in a Nuxt Vue component

Source: https://v3.tailwindcss.com/docs/guides/nuxtjs

This example demonstrates how to use Tailwind's utility classes directly within the `template` section of a Vue component in Nuxt. It applies text size, font weight, and underline styles to an `<h1>` element.

```vue
<template>
  <h1 class="text-3xl font-bold underline">
    Hello world!
  </h1>
</template>
```

--------------------------------

### Configure PostCSS for Tailwind CSS

Source: https://v3.tailwindcss.com/docs/guides/parcel

Create a .postcssrc configuration file in the project root to enable the Tailwind CSS plugin. This file tells PostCSS to process Tailwind directives during the build process.

```json
{
  "plugins": {
    "tailwindcss": {}
  }
}
```

--------------------------------

### Use Tailwind Utility Classes in Rails Templates

Source: https://v3.tailwindcss.com/docs/guides/ruby-on-rails

Apply Tailwind CSS utility classes directly to HTML elements in your Rails ERB templates to style content. This example demonstrates using text size, font weight, and text decoration utilities.

```erb
<h1 class="text-3xl font-bold underline">
    Hello world!
</h1>
```

--------------------------------

### Align Self Start with Tailwind CSS

Source: https://v3.tailwindcss.com/docs/align-self

Uses the self-start class to align a flex item to the start of the container's cross axis, overriding the container's align-items value. Useful for positioning specific items independently.

```html
<div class="flex items-stretch ...">
  <div>01</div>
  <div class="self-start ...">02</div>
  <div>03</div>
</div>
```

--------------------------------

### Configure Tailwind Template Paths

Source: https://v3.tailwindcss.com/docs/guides/sveltekit

Specify the paths to all template files in tailwind.config.js so Tailwind can scan and generate CSS for all used utility classes. This configuration supports HTML, JavaScript, Svelte, and TypeScript files.

```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {}
  },
  plugins: []
};
```

--------------------------------

### Force hardware acceleration for transforms in Tailwind CSS

Source: https://v3.tailwindcss.com/docs/translate

This example shows how to apply the `transform-gpu` utility class to an element to force hardware acceleration for its transforms. This can improve performance for transitions by offloading rendering to the GPU. The `transform-cpu` utility is also mentioned for reverting this behavior conditionally.

```html
<div class="translate-y-6 transform-gpu">
  <!-- ... -->
</div>
```

--------------------------------

### Add custom col-end utilities in Tailwind config

Source: https://v3.tailwindcss.com/docs/grid-column

Customize the gridColumnEnd section of your Tailwind theme config to add new col-end-* utilities. This example adds col-end utilities for columns 13 through 17 to complement extended grid configurations.

```javascript
module.exports = {
  theme: {
    extend: {
      gridColumnEnd: {
        '13': '13',
        '14': '14',
        '15': '15',
        '16': '16',
        '17': '17',
      }
    }
  }
}
```

--------------------------------

### Create HTML File with Tailwind Styles

Source: https://v3.tailwindcss.com/docs/guides/parcel

Set up the index.html file with proper meta tags for viewport configuration, link the compiled CSS file, and use Tailwind utility classes to style HTML elements. This demonstrates basic Tailwind usage with responsive design support.

```html
<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="./index.css" type="text/css" rel="stylesheet">
</head>
<body>
  <h1 class="text-3xl font-bold underline">
    Hello world!
  </h1>
</body>
</html>
```

--------------------------------

### Add custom col-start utilities in Tailwind config

Source: https://v3.tailwindcss.com/docs/grid-column

Customize the gridColumnStart section of your Tailwind theme config to add new col-start-* utilities. This example adds col-start utilities for columns 13 through 17, extending the default 12-column grid.

```javascript
module.exports = {
  theme: {
    extend: {
      gridColumnStart: {
        '13': '13',
        '14': '14',
        '15': '15',
        '16': '16',
        '17': '17',
      }
    }
  }
}
```

--------------------------------

### Correct `@import` Usage with Separate CSS Files

Source: https://v3.tailwindcss.com/docs/using-with-preprocessors

This example demonstrates the recommended approach for organizing CSS with `postcss-import` by separating imports from actual CSS rules. A main entry-point file handles all `@import` statements, while individual component files contain specific CSS, ensuring `@import` rules are always at the top of their respective files.

```css
/* components.css */
@import "./components/buttons.css";
@import "./components/card.css";
```

```css
/* components/buttons.css */
.btn {
  padding: theme('spacing.4') theme('spacing.2');
  /* ... */
}
```

```css
/* components/card.css */
.card {
  padding: theme('spacing.4');
  /* ... */
}
```

--------------------------------

### Apply Tailwind CSS classes in an AdonisJS Edge template

Source: https://v3.tailwindcss.com/docs/guides/adonisjs

This example demonstrates how to include the compiled CSS in an AdonisJS Edge template and use Tailwind's utility classes to style HTML elements. The `@vite` directive ensures that the CSS and JavaScript assets are properly linked.

```html
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  @vite(['resources/css/app.css', 'resources/js/app.js'])
</head>
<body>
  <h1 class="text-3xl font-bold underline">
    Hello world!
  </h1>
</body>
</html>
```

--------------------------------

### Configure SvelteKit for PostCSS Processing

Source: https://v3.tailwindcss.com/docs/guides/sveltekit

Enable PostCSS processing in SvelteKit style blocks by importing and configuring vitePreprocess in svelte.config.js. This allows Tailwind directives to be processed within component styles.

```javascript
import adapter from '@sveltejs/adapter-auto';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
  kit: {
    adapter: adapter()
  },
  preprocess: vitePreprocess()
};

export default config;
```

--------------------------------

### Justify Items Start - Tailwind CSS Grid Alignment

Source: https://v3.tailwindcss.com/docs/justify-items

Aligns grid items against the start of their inline axis using the justify-items-start utility class. Apply this class to a grid container to left-align (or start-align in RTL) all child items within their grid cells.

```html
<div class="grid justify-items-start ...">
  <div>01</div>
  <div>02</div>
  <div>03</div>
  <div>04</div>
  <div>05</div>
  <div>06</div>
</div>
```

--------------------------------

### Position Replaced Elements with Tailwind CSS Object Utilities

Source: https://v3.tailwindcss.com/docs/object-position

HTML examples demonstrating how to use Tailwind's object-* utility classes to position replaced elements (images) within fixed-size containers. The object-none class prevents content scaling, while object-* classes control positioning. Each example uses a 24x24 pixel container with a yellow background to visualize positioning.

```html
<img class="object-none object-left-top bg-yellow-300 w-24 h-24 ..." src="...">
<img class="object-none object-top bg-yellow-300 w-24 h-24 ..." src="...">
<img class="object-none object-right-top bg-yellow-300 w-24 h-24 ..." src="...">
<img class="object-none object-left bg-yellow-300 w-24 h-24 ..." src="...">
<img class="object-none object-center bg-yellow-300 w-24 h-24 ..." src="...">
<img class="object-none object-right bg-yellow-300 w-24 h-24 ..." src="...">
<img class="object-none object-left-bottom bg-yellow-300 w-24 h-24 ..." src="...">
<img class="object-none object-bottom bg-yellow-300 w-24 h-24 ..." src="...">
<img class="object-none object-right-bottom bg-yellow-300 w-24 h-24 ..." src="...">
```