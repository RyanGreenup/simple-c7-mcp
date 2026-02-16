### Install ESLint and TypeScript-ESLint Packages

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/getting-started/Quickstart.mdx

Installs the necessary development dependencies for ESLint, TypeScript, and the `typescript-eslint` tooling using npm. This command should be run in the root of your project.

```bash
npm install --save-dev eslint @eslint/js typescript typescript-eslint
```

--------------------------------

### Configure ESLint with Recommended Rules for TypeScript

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/getting-started/Quickstart.mdx

Creates an `eslint.config.mjs` file in the project root to define the ESLint configuration. This setup imports and applies recommended rules from both ESLint and `typescript-eslint` for basic linting of TypeScript code.

```javascript
// @ts-check

import eslint from '@eslint/js';
import { defineConfig } from 'eslint/config';
import tseslint from 'typescript-eslint';

export default defineConfig(
  eslint.configs.recommended,
  tseslint.configs.recommended,
);
```

--------------------------------

### Install ESLint and TypeScript-ESLint packages

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/getting-started/Legacy_ESLint_Setup.mdx

Installs the required development dependencies for ESLint, TypeScript, and the `@typescript-eslint` parser and plugin. These packages are essential for linting TypeScript code.

```bash
npm install --save-dev @typescript-eslint/parser @typescript-eslint/eslint-plugin eslint typescript
```

--------------------------------

### Run ESLint from the Command Line

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/getting-started/Quickstart.mdx

Executes ESLint across the project to lint all TypeScript-compatible files within the current folder. This command outputs the linting results directly to your terminal.

```bash
npx eslint .
```

```bash
yarn eslint .
```

```bash
pnpm eslint .
```

--------------------------------

### Install `typescript-eslint` package

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/packages/TypeScript_ESLint.mdx

Instructions for installing the `typescript-eslint` package using the npm package manager. This command adds the package as a development dependency to your project, making the tooling available for your ESLint setup.

```bash
npm i typescript-eslint
```

--------------------------------

### Extend ESLint Configuration with Strict and Stylistic Rules

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/getting-started/Quickstart.mdx

Modifies the `eslint.config.mjs` file to include additional `typescript-eslint` configurations. Adding `strict` enables more opinionated rules that may catch bugs, while `stylistic` enforces consistent code styling.

```javascript
export default defineConfig(
  eslint.configs.recommended,
  // Remove this line
  tseslint.configs.recommended,
  // Add this line
  tseslint.configs.strict,
  // Add this line
  tseslint.configs.stylistic,
);
```

--------------------------------

### Install Website Dependencies (yarn)

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/website/README.md

Installs all required project dependencies for the typescript-eslint website using yarn.

```Shell
yarn install
```

--------------------------------

### Configuring TypeScript ESLint RuleTester for Node.js `node:test`

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/packages/Rule_Tester.mdx

This example demonstrates setting up `@typescript-eslint/rule-tester` for Node.js's built-in `node:test` runner. It shows how to map `node:test`'s hooks (`after`, `describe`, `it`) to `RuleTester`'s static properties, and provides the command-line instruction to run tests with a preloaded setup module.

```ts
// setup.js
import * as test from 'node:test';
import { RuleTester } from '@typescript-eslint/rule-tester';

RuleTester.afterAll = test.after;
RuleTester.describe = test.describe;
RuleTester.it = test.it;
RuleTester.itOnly = test.it.only;
```

```sh
node --import setup.js --test
```

--------------------------------

### Enable Project Service for Typed Linting in ESLint Configuration

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/website/blog/2024-05-27-announcing-typescript-eslint-v8-beta.mdx

This example demonstrates how to update your `eslint.config.mjs` to use the new `projectService: true` option instead of `project: true`. The project service automatically locates the closest `tsconfig.json` for each file, simplifying typed linting setup and improving performance.

```JavaScript
import eslint from '@eslint/js';
import tseslint from 'typescript-eslint';

export default tseslint.config(
  eslint.configs.recommended,
  ...tseslint.configs.recommendedTypeChecked,
  {
    languageOptions: {
      parserOptions: {
        // Remove this line
        project: true,
        // Add this line
        projectService: true,
        tsconfigRootDir: import.meta.dirname,
      },
    },
  },
);
```

--------------------------------

### Configure ESLint with `typescript-eslint` recommended settings

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/packages/TypeScript_ESLint.mdx

Example of a basic ESLint flat configuration file (`eslint.config.mjs`) that integrates `typescript-eslint`'s recommended settings alongside core ESLint recommended rules. This setup provides a foundational linting configuration for TypeScript projects, leveraging both ESLint's core capabilities and `typescript-eslint`'s specific TypeScript linting rules.

```javascript
// @ts-check

import eslint from '@eslint/js';
import { defineConfig } from 'eslint/config';
import tseslint from 'typescript-eslint';

export default defineConfig(
  eslint.configs.recommended,
  tseslint.configs.recommended,
);
```

--------------------------------

### Start local development server for typescript-eslint website

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/contributing/Local_Development.mdx

Command to start the Docusaurus-based local development server for the documentation website. It's recommended to build other packages first.

```shell
yarn start
```

--------------------------------

### Configure ESLint for TypeScript with recommended rules (legacy format)

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/getting-started/Legacy_ESLint_Setup.mdx

Creates a `.eslintrc.cjs` file in the project root to configure ESLint. This setup enables the `@typescript-eslint/parser` for TypeScript code and extends `eslint:recommended` and `plugin:@typescript-eslint/recommended` rule sets.

```javascript
/* eslint-env node */
module.exports = {
  extends: ['eslint:recommended', 'plugin:@typescript-eslint/recommended'],
  parser: '@typescript-eslint/parser',
  plugins: ['@typescript-eslint'],
  root: true,
};
```

--------------------------------

### Start Local Development Server (yarn)

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/website/README.md

Starts a local development server for the website and opens it in a browser. Most changes are hot-reloaded without requiring a server restart.

```Shell
yarn start
```

--------------------------------

### Example 'Cannot Find Module' Error Message

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/contributing/local-development/Local_Linking.mdx

This plaintext example displays a common error message encountered when a local `@typescript-eslint/*` package has a dependency that is not found in the downstream repository. It indicates a missing module, often requiring manual installation to resolve.

```plaintext
Error: Failed to load parser '@typescript-eslint/parser' declared in '.eslintrc.js': Cannot find module 'ts-api-utils'
Require stack:
- /repos/typescript-eslint/packages/typescript-estree/dist/convert-comments.js
```

--------------------------------

### Install typescript-eslint v6 for existing users

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/website/blog/2023-07-09-announcing-typescript-eslint-v6.md

This command installs the latest stable versions of the core typescript-eslint packages, `@typescript-eslint/eslint-plugin` and `@typescript-eslint/parser`, as development dependencies. It is specifically for existing users upgrading from a previous version of typescript-eslint to v6.

```shell
npm i @typescript-eslint/eslint-plugin@latest @typescript-eslint/parser@latest --save-dev
```

--------------------------------

### Install ESLint and TypeScript dependencies for v7

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/website/blog/2024-02-12-announcing-typescript-eslint-v7.md

This command installs the necessary peer dependencies for `typescript-eslint` v7, including `eslint`, `typescript`, and the `@typescript-eslint` parser and plugin, aligning with the updated requirements.

```bash
npm i eslint typescript @typescript-eslint/parser @typescript-eslint/eslint-plugin
```

--------------------------------

### Install typescript-eslint v8 beta for ESLint Legacy Config

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/website/blog/2024-05-27-announcing-typescript-eslint-v8-beta.mdx

This command installs the individual `@typescript-eslint/eslint-plugin` and `@typescript-eslint/parser` packages at their `rc-v8` release candidate versions. It is designed for existing users who are still utilizing ESLint's older Legacy Config format, enabling them to try out the v8 beta.

```shell
npm i @typescript-eslint/eslint-plugin@rc-v8 @typescript-eslint/parser@rc-v8 --save-dev
```

--------------------------------

### Configure TypeScript ESLint Recommended Rules

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/users/Shared_Configurations.mdx

This configuration applies recommended rules for code correctness and disables core ESLint rules that conflict with TypeScript. It's a good starting point for most TypeScript projects without requiring additional setup, focusing on common bad practices and likely bugs.

```JavaScript
export default defineConfig(
  tseslint.configs.recommended,
);
```

```JavaScript
module.exports = {
  extends: ['plugin:@typescript-eslint/recommended'],
};
```

--------------------------------

### Install typescript-eslint v8 beta for ESLint Flat Config

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/website/blog/2024-05-27-announcing-typescript-eslint-v8-beta.mdx

This command installs the `typescript-eslint` package at its `rc-v8` release candidate version. It is intended for existing users who are configuring ESLint with the newer Flat Config format, allowing them to test the upcoming v8 features and breaking changes.

```shell
npm i typescript-eslint@rc-v8 --save-dev
```

--------------------------------

### Set up local development environment for typescript-eslint

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/contributing/Local_Development.mdx

Instructions to clone the typescript-eslint repository from GitHub, navigate into the directory, and install project dependencies using Yarn.

```shell
git clone https://github.com/<your-name-here>/typescript-eslint
cd typescript-eslint
yarn
```

--------------------------------

### Configure ESLint `extraFileExtensions` for Frameworks (Vue)

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/troubleshooting/faqs/Frameworks.mdx

This configuration demonstrates how to add `parserOptions.extraFileExtensions` to your ESLint setup to allow custom file extensions, such as `.vue` files used by frameworks like Vue. This prevents errors like 'You should add `parserOptions.extraFileExtensions` to your config' when linting non-TypeScript files. Examples are provided for both Flat Config (`eslint.config.mjs`) and Legacy Config (`.eslintrc.js`).

```javascript
export default defineConfig(
  // ... the rest of your config ...
  {
    languageOptions: {
      parserOptions: {
        // Add this line
        extraFileExtensions: ['.vue'],
        projectService: true,
        tsconfigRootDir: import.meta.dirname,
      },
    },
  },
);
```

```javascript
module.exports = {
  // ... the rest of your config ...
  parserOptions: {
    // Add this line
    extraFileExtensions: ['.vue'],
    projectService: true,
    tsconfigRootDir: __dirname,
  },
};
```

--------------------------------

### Install typescript-eslint v6 Beta for Existing Users

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/website/blog/2023-03-13-announcing-typescript-eslint-v6-beta.md

This command is for existing users of typescript-eslint to upgrade their development dependencies to the v6 release candidate versions. It installs `@typescript-eslint/eslint-plugin@rc-v6` and `@typescript-eslint/parser@rc-v6`, enabling beta testing of the new features and breaking changes.

```Shell
npm i @typescript-eslint/eslint-plugin@rc-v6 @typescript-eslint/parser@rc-v6 --save-dev
```

--------------------------------

### Install typescript-eslint v8 for Flat Config with npm

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/website/blog/2024-07-31-announcing-typescript-eslint-v8.md

Installs the `typescript-eslint@8` package as a development dependency using npm. This command is specifically for projects utilizing ESLint's new Flat Config file format.

```shell
npm i typescript-eslint@8 --save-dev
```

--------------------------------

### Configure `parserOptions.project` for Custom TSConfig

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/troubleshooting/typed-linting/index.mdx

These examples demonstrate how to specify a custom TSConfig file (e.g., `tsconfig.eslint.json`) for `parserOptions.project` in `@typescript-eslint/parser` to enable type-aware linting. The first snippet shows the setup for ESLint Flat Config, using `import.meta.dirname` for `tsconfigRootDir`. The second snippet provides the equivalent configuration for ESLint Legacy Config, utilizing `__dirname` for path resolution.

```JavaScript
export default defineConfig({
  // ...
  languageOptions: {
    parserOptions: {
      project: './tsconfig.eslint.json',
      tsconfigRootDir: import.meta.dirname,
    },
  },
  // ...
});
```

```JavaScript
module.exports = {
  // ...
  parserOptions: {
    project: './tsconfig.eslint.json',
    tsconfigRootDir: __dirname,
  },
  // ...
};
```

--------------------------------

### Install typescript-eslint v8 for Legacy Config with npm

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/website/blog/2024-07-31-announcing-typescript-eslint-v8.md

Installs the `@typescript-eslint/eslint-plugin@8` and `@typescript-eslint/parser@8` packages as development dependencies using npm. This command is intended for projects still using ESLint's older Legacy Config file format.

```shell
npm i @typescript-eslint/eslint-plugin@8 @typescript-eslint/parser@8 --save-dev
```

--------------------------------

### Example `PackageSpecifier` Configurations

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/packages/type-utils/TypeOrValueSpecifier.mdx

Shows how to configure `PackageSpecifier` to match types or values imported from specific packages. Examples include matching `SafePromise` from `@reduxjs/toolkit` and multiple testing functions from `vitest`.

```json
{ "from": "package", "name": "SafePromise", "package": "@reduxjs/toolkit" }
```

```json
{ "from": "package", "name": ["describe", "it", "test"], "package": "vitest" }
```

--------------------------------

### Example `FileSpecifier` Configurations

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/packages/type-utils/TypeOrValueSpecifier.mdx

Illustrates how to configure `FileSpecifier` to match types or values. The first example matches `Props` in any file, while the second specifies `Props` within `file.tsx`.

```json
{ "from": "file", "name": "Props" }
```

```json
{ "from": "file", "name": "Props", "path": "file.tsx" }
```

--------------------------------

### Example `LibSpecifier` Configurations

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/packages/type-utils/TypeOrValueSpecifier.mdx

Demonstrates how to configure `LibSpecifier` to match types or values from TypeScript's built-in libraries. Examples include matching `Array` and matching both `Promise` and `PromiseLike`.

```json
{ "from": "lib", "name": "Array" }
```

```json
{ "from": "lib", "name": ["Promise", "PromiseLike"] }
```

--------------------------------

### Run ESLint on your project

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/getting-started/Legacy_ESLint_Setup.mdx

Executes ESLint from the terminal to lint all TypeScript-compatible files within the current folder. This command will output the linting results directly to your terminal.

```bash
npx eslint .
```

```bash
yarn eslint .
```

```bash
pnpm eslint .
```

--------------------------------

### Test Untyped ESLint Rules with TypeScript ESLint RuleTester

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/developers/Custom_Rules.mdx

This snippet illustrates the basic setup for testing ESLint rules that do not require TypeScript type information using `@typescript-eslint/rule-tester`. It shows how to instantiate `RuleTester` without any specific parser options and then run tests for valid and invalid code examples.

```ts
import { RuleTester } from '@typescript-eslint/rule-tester';
import rule from './my-rule';

const ruleTester = new RuleTester();

ruleTester.run('my-rule', rule, {
  valid: [
    /* ... */
  ],
  invalid: [
    /* ... */
  ],
});
```

--------------------------------

### Configure TypeScript ESLint Project Service for out-of-project files

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/website/blog/2025-05-29-project-service.mdx

Demonstrates how to enable typed linting for files not included in a project's `tsconfig.json` using the new `projectService` API's `allowDefaultProject` option. This example covers both ESLint Flat Config (`eslint.config.js`) and Legacy Config (`.eslintrc.cjs`) setups, allowing files like `*.js` to be linted with type information without additional `tsconfig` files.

```JavaScript
export default tseslint.config({
  // ...
  languageOptions: {
    parserOptions: {
      projectService: {
        allowDefaultProject: ['*.js'],
      },
      tsconfigRootDir: import.meta.dirname,
    },
  },
  // ...
});
```

```JavaScript
module.exports = {
  // ...
  parser: '@typescript-eslint/parser',
  parserOptions: {
    projectService: {
      allowDefaultProject: ['*.js'],
      tsconfigRootDir: __dirname,
    },
  },
  // ...
};
```

--------------------------------

### Example `tsconfig.eslint.json` for extended linting scope

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/packages/Parser.mdx

Provides an example of a `tsconfig.eslint.json` file that extends an existing `tsconfig.json` to include additional source files (e.g., `src`, `test`, `typings`, `js` files) for linting purposes, especially when the main TSConfig doesn't cover all desired files.

```JSON
{
  // extend your base config so you don't have to redefine your compilerOptions
  "extends": "./tsconfig.json",
  "include": [
    "src/**/*.ts",
    "test/**/*.ts",
    "typings/**/*.ts",
    // etc

    // if you have a mixed JS/TS codebase, don't forget to include your JS files
    "src/**/*.js"
  ]
}
```

--------------------------------

### Install TypeScript ESLint Canary Versions via npm

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/users/Releases.mdx

This command demonstrates how to install the latest canary versions of `@typescript-eslint/eslint-plugin` and `@typescript-eslint/parser` using npm. The `--save-dev` flag adds them as development dependencies, and `--force` is used to override potential version conflicts or requirements.

```Bash
npm i @typescript-eslint/eslint-plugin@canary @typescript-eslint/parser@canary --save-dev --force
```

--------------------------------

### Enforcing 'method' Signature - Correct Examples

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/docs/rules/method-signature-style.mdx

Shows code examples that are considered correct when the rule is configured with the 'method' option. These examples correctly use the method shorthand signature syntax for function properties.

```typescript
interface T1 {
  func(arg: string): number;
}
type T2 = {
  func(arg: boolean): void;
};
```

--------------------------------

### TypeScript: Examples for `no-empty-interface` rule

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/docs/rules/no-empty-interface.mdx

Demonstrates incorrect and correct usage of interfaces according to the `@typescript-eslint/no-empty-interface` rule. Incorrect examples show empty interfaces or interfaces extending a single type without adding members, while correct examples show interfaces with members or extending multiple types.

```TypeScript
// an empty interface
interface Foo {}

// an interface with only one supertype (Bar === Foo)
interface Bar extends Foo {}

// an interface with an empty list of supertypes
interface Baz {}
```

```TypeScript
// an interface with any number of members
interface Foo {
  name: string;
}

// same as above
interface Bar {
  age: number;
}

// an interface with more than one supertype
// in this case the interface can be used as a replacement of an intersection type.
interface Baz extends Foo, Bar {}
```

--------------------------------

### Migrate to new `typescript-eslint` package for flat configs

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/website/blog/2024-02-12-announcing-typescript-eslint-v7.md

These commands demonstrate how to uninstall the old `@typescript-eslint/parser` and `@typescript-eslint/eslint-plugin` packages and install the new unified `typescript-eslint` package, which provides full support for ESLint flat configurations.

```bash
npm un @typescript-eslint/parser @typescript-eslint/eslint-plugin
npm i typescript-eslint
```

--------------------------------

### Example Usage of `parse` Function

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/packages/TypeScript_ESTree.mdx

This example demonstrates how to import and use the `parse` function from `@typescript-eslint/typescript-estree`. It shows parsing a simple TypeScript string `const hello: string = 'world';` and configuring the parser to include `loc` (location) and `range` (index range) properties in the resulting AST nodes, which are useful for tooling.

```js
import { parse } from '@typescript-eslint/typescript-estree';

const code = `const hello: string = 'world';`;
const ast = parse(code, {
  loc: true,
  range: true,
});
```

--------------------------------

### Check Installed @typescript-eslint Tooling Versions

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/troubleshooting/faqs/General.mdx

Provides a command to list all installed versions of `@typescript-eslint/eslint-plugin` and `@typescript-eslint/parser` within a project. This helps diagnose issues caused by multiple versions of the tooling, which can lead to inconsistent linting results. Users can then use `yarn resolutions` or downgrade root versions to resolve conflicts.

```bash
npm list @typescript-eslint/eslint-plugin @typescript-eslint/parser
```

--------------------------------

### Configure `allowConciseArrowFunctionExpressionsStartingWithVoid` Option

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/docs/rules/explicit-function-return-type.mdx

This option determines if concise arrow function expressions can start with `void`. It shows an incorrect example where `void` is not used for side effects and a correct example demonstrating its proper use.

```TypeScript
var join = (a: string, b: string) => `${a}${b}`;

const log = (message: string) => {
  console.log(message);
};
```

```TypeScript
var log = (message: string) => void console.log(message);
```

--------------------------------

### Disable Type-Aware Linting for JavaScript Files with `tseslint.config`

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/packages/TypeScript_ESLint.mdx

This example illustrates how `tseslint.config` can be used to disable TypeScript-specific linting setups on JavaScript files (e.g., `**/*.js`) by extending `tseslint.configs.disableTypeChecked` and turning off other type-aware or TypeScript-specific rules.

```js
export default tseslint.config({
  files: ['**/*.js'],
  extends: [tseslint.configs.disableTypeChecked],
  rules: {
    // turn off other type-aware rules
    'other-plugin/typed-rule': 'off',

    // turn off rules that don't apply to JS code
    '@typescript-eslint/explicit-function-return-type': 'off',
  },
});
```

--------------------------------

### Enforce custom format for TypeScript directive descriptions

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/docs/rules/ban-ts-comment.mdx

This example illustrates the `descriptionFormat` option, allowing developers to define a regular expression that descriptions following TypeScript directives must match. This ensures consistency and adherence to project-specific documentation standards. The 'Incorrect' example shows a description that doesn't match the specified format, while the 'Correct' example provides a description that conforms to the regex.

```typescript
// @ts-expect-error: the library definition is wrong
const a = doSomething('hello');
```

```typescript
// @ts-expect-error: TS1234 because the library definition is wrong
const a = doSomething('hello');
```

--------------------------------

### Initialize and Use TypeScript Project Service

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/packages/Project_Service.mdx

This snippet demonstrates how to initialize the `@typescript-eslint/project-service`, open a client file, and then retrieve the TypeScript program associated with that file. This is a fundamental step for tools that need to analyze TypeScript code with full type information.

```TypeScript
import { createProjectService } from '@typescript-eslint/project-service';

const filePathAbsolute = '/path/to/your/project/index.ts';
const { service } = createProjectService();

service.openClientFile(filePathAbsolute);

const scriptInfo = service.getScriptInfo(filePathAbsolute)!;
const program = service
  .getDefaultProjectForFile(scriptInfo.fileName, true)!
  .getLanguageService(true)
  .getProgram()!;
```

--------------------------------

### Conceptual Example of Getter/Setter Type Mismatch Impact (TypeScript)

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/docs/rules/related-getter-setter-pairs.mdx

Illustrates a scenario where differing `get()` and `set()` types could lead to unexpected behavior, specifically when attempting to assign a property to itself.

```TypeScript
// Assumes box.value's get() return is assignable to its set() parameter
box.value = box.value;
```

--------------------------------

### Create a TypeScript ESLint Rule with RuleCreator

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/developers/Custom_Rules.mdx

Demonstrates how to define a custom ESLint rule using `ESLintUtils.RuleCreator` from `@typescript-eslint/utils`. This example rule bans function declarations that start with a lowercase letter, showing how to define `meta.messages` for type inference of `messageId`.

```typescript
import { ESLintUtils } from '@typescript-eslint/utils';

const createRule = ESLintUtils.RuleCreator(
  name => `https://example.com/rule/${name}`,
);

// Type: RuleModule<"uppercase", ...>
export const rule = createRule({
  create(context) {
    return {
      FunctionDeclaration(node) {
        if (node.id != null) {
          if (/^[a-z]/.test(node.id.name)) {
            context.report({
              messageId: 'uppercase',
              node: node.id,
            });
          }
        }
      },
    };
  },
  name: 'uppercase-first-declarations',
  meta: {
    docs: {
      description:
        'Function declaration names should start with an upper-case letter.',
    },
    messages: {
      uppercase: 'Start this name with an upper-case letter.',
    },
    type: 'suggestion',
    schema: [],
  },
  defaultOptions: [],
});
```

--------------------------------

### TypeScript ESLint: Enforce Optional Chaining for Booleans (checkBoolean Rule)

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/docs/rules/prefer-optional-chain.mdx

Shows the application of the `checkBoolean` rule in TypeScript ESLint, guiding users to use optional chaining (`?.`) instead of `&&` for boolean type checks. Provides examples of both non-compliant and compliant code.

```TypeScript
declare const thing: true;

thing && thing.toString();
```

```TypeScript
declare const thing: true;

thing?.toString();
```

--------------------------------

### JSON Configuration for Naming Convention Rule Evaluation Example 1

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/docs/rules/naming-convention.mdx

Illustrates a JSON configuration for the `typescript-eslint` naming convention rule, demonstrating how `leadingUnderscore`, `prefix`, and `format` options are applied during identifier evaluation for `_IMyInterface`.

```json
{
  "leadingUnderscore": "require",
  "prefix": ["I"],
  "format": ["UPPER_CASE", "StrictPascalCase"]
}
```

--------------------------------

### Configure ESLint to disable formatting rules with eslint-config-prettier

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/users/What_About_Formatting.mdx

This snippet demonstrates how to integrate `eslint-config-prettier` into your ESLint configuration to disable any formatting-related rules. This allows you to use a dedicated formatter like Prettier without conflicts from ESLint. Examples are provided for both Flat Config (ESM) and Legacy Config (CommonJS) setups.

```JavaScript
// @ts-check

import eslint from '@eslint/js';
import { defineConfig } from 'eslint/config';
import someOtherConfig from 'eslint-config-other-configuration-that-enables-formatting-rules';
import prettierConfig from 'eslint-config-prettier';
import tseslint from 'typescript-eslint';

export default defineConfig(
  eslint.configs.recommended,
  tseslint.configs.recommended,
  someOtherConfig,
  // Add this line
  prettierConfig,
);
```

```JavaScript
/* eslint-env node */
module.exports = {
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'other-configuration-that-enables-formatting-rules',
    // Add this line
    'prettier',
  ],
  parser: '@typescript-eslint/parser',
  plugins: ['@typescript-eslint'],
  root: true,
};
```

--------------------------------

### Disable Type-Checked Linting in TypeScript ESLint

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/users/Shared_Configurations.mdx

This utility ruleset disables type-aware linting and all type-aware rules available in the project. It is useful for conditionally disabling type-aware linting on specific subsets of your codebase using ESLint overrides. This snippet provides examples for both Flat Config and Legacy Config setups.

```JavaScript
export default defineConfig(
  eslint.configs.recommended,
  tseslint.configs.recommendedTypeChecked,
  {
    languageOptions: {
      parserOptions: {
        projectService: true,
        tsconfigRootDir: import.meta.dirname,
      },
    },
  },
  // Added lines start
  {
    files: ['**/*.js'],
    extends: [tseslint.configs.disableTypeChecked],
  },
  // Added lines end
);
```

```JavaScript
module.exports = {
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended-type-checked',
  ],
  parser: '@typescript-eslint',
  parserOptions: {
    projectService: true,
    __tsconfigRootDir: __dirname,
  },
  root: true,
  // Added lines start
  overrides: [
    {
      files: ['**/*.js'],
      extends: ['plugin:@typescript-eslint/disable-type-checked'],
    },
  ],
  // Added lines end
};
```

--------------------------------

### Install Missing Dependency for TypeScript ESLint (Troubleshooting)

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/contributing/local-development/Local_Linking.mdx

If a local `@typescript-eslint/*` package introduces a new dependency not present in the published version, this command demonstrates how to manually install that missing package (e.g., `ts-api-utils`) as a development dependency in the local downstream repository. This resolves 'Cannot find module' errors.

```shell
yarn add ts-api-utils -D
```

--------------------------------

### JSON Configuration for Naming Convention Rule Evaluation Example 2

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/docs/rules/naming-convention.mdx

Shows a JSON configuration for the `typescript-eslint` naming convention rule, detailing the evaluation process for `IMyInterface` with `format`, `trailingUnderscore`, and a `custom` regex option.

```json
{
  "format": ["StrictPascalCase"],
  "trailingUnderscore": "allow",
  "custom": {
    "regex": "^I[A-Z]",
    "match": false
  }
}
```

--------------------------------

### Migrating to New Package Exports in typescript-eslint

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/website/blog/2023-07-09-announcing-typescript-eslint-v6.md

These TypeScript examples demonstrate the transition from deep `dist/` path imports to direct package imports in `@typescript-eslint/*` packages, leveraging Node.js `package.json` exports. The commented-out lines show the old import style, while the active lines illustrate the new, recommended approach for importing modules and types.

```TypeScript
// import * as TSESLint from '@typescript-eslint/utils/dist/ts-eslint';
// -->
import { TSESLint } from '@typescript-eslint/utils';
// The following would also work and be equivalent:
// import * as TSESLint from '@typescript-eslint/utils/ts-eslint';
// But explicit importing should be generally favored over star imports.

// import { RuleModule } from '@typescript-eslint/utils/dist/ts-eslint';
// -->
import { RuleModule } from '@typescript-eslint/utils/ts-eslint';

// import { AST_NODE_TYPES } from "@typescript-eslint/types/dist/generated/ast-spec";
// -->
import { AST_NODE_TYPES } from '@typescript-eslint/types';
```

--------------------------------

### Define and Run TypeScript ESLint Integration Test

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/integration-tests/README.md

This snippet demonstrates how to define a new integration test for `typescript-eslint` using the `integrationTest` helper function, specifying the test file and target extensions. It also provides the command to execute the newly defined integration test, which generates a JSON snapshot of the ESLint run for verification.

```TypeScript
import { integrationTest } from '../tools/integration-test-base';

integrationTest(
  __filename,
  '*.ts' /* UPDATE THIS TO THE EXTENSION(s) TO LINT */,
);
```

```Shell
yarn test-integration ./tests/integration/tests/your-file.test.ts
```

--------------------------------

### Enforce 'as' assertion style and ban object literal type assertions

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/docs/rules/consistent-type-assertions.mdx

Examples demonstrating the `consistent-type-assertions` rule configured with `assertionStyle: 'as'` and `objectLiteralTypeAssertions: 'never'`. This setup requires using the `as` keyword for type assertions and disallows type assertions on object literals, preferring explicit type annotations instead.

```ts
const x = { foo: 1 } as T;

function bar() {
  return { foo: 1 } as T;
}
```

```ts
const x: T = { foo: 1 };
const y = { foo: 1 } as any;
const z = { foo: 1 } as unknown;

function bar(): T {
  return { foo: 1 };
}
```

--------------------------------

### Correct Usage: Calling functions with safe arguments

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/docs/rules/no-unsafe-argument.mdx

Provides examples of how to correctly call functions by ensuring all arguments are properly typed and do not involve `any`. This demonstrates adherence to the `no-unsafe-argument` rule, promoting type safety.

```typescript
declare function foo(arg1: string, arg2: number, arg3: string): void;

foo('a', 1, 'b');

const tuple1 = ['a', 1, 'b'] as const;
foo(...tuple1);

declare function bar(arg1: string, arg2: number, ...rest: string[]): void;
const array: string[] = ['a'];
bar('a', 1, ...array);

declare function baz(arg1: Set<string>, arg2: Map<string, string>): void;
baz(new Set<string>(), new Map<string, string>());
```

--------------------------------

### Query TypeScript AST Nodes in ESLint Rules

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/developers/Custom_Rules.mdx

This example demonstrates how to query for TypeScript-specific Abstract Syntax Tree (AST) nodes, such as `TSInterfaceDeclaration`, within an ESLint rule. It shows how to use rule selectors to identify and process these nodes, treating them like any other AST node. The rule bans interface declaration names that start with a lower-case letter.

```typescript
import { ESLintUtils } from '@typescript-eslint/utils';

export const rule = createRule({
  create(context) {
    return {
      TSInterfaceDeclaration(node) {
        if (/^[a-z]/.test(node.id.name)) {
          // ...
        }
      },
    };
  },
  // ...
});
```

--------------------------------

### TypeScript ESLint: Constructor Parameter Properties - Allow Protected

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/docs/rules/parameter-properties.mdx

Demonstrates correct and incorrect usage of constructor parameter properties when the ESLint rule is configured with `{ "allow": ["protected"] }`. Incorrect examples show other modifiers or lack of modifiers, while correct examples show `protected` or no modifier.

```TypeScript
class Foo {
  constructor(readonly name: string) {}
}

class Foo {
  constructor(private name: string) {}
}

class Foo {
  constructor(public name: string) {}
}

class Foo {
  constructor(private readonly name: string) {}
}

class Foo {
  constructor(protected readonly name: string) {}
}

class Foo {
  constructor(public readonly name: string) {}
}
```

```TypeScript
class Foo {
  constructor(name: string) {}
}

class Foo {
  constructor(protected name: string) {}
}
```

--------------------------------

### Configure ESLint to Ban Specific Language Features

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/troubleshooting/faqs/General.mdx

Demonstrates how to use ESLint's `no-restricted-syntax` rule to prevent the use of certain language features or patterns. This rule allows specifying AST selectors and custom error messages to enforce coding standards. Examples include banning `constructor.name`, `get`/`set` accessors, private class members, TypeScript enums, and unlabelled tuples.

```JSONC
{
  "rules": {
    "no-restricted-syntax": [
      "error",

      // Ban accessing `constructor.name`:
      {
        "selector": "MemberExpression[object.property.name='constructor'][property.name='name']",
        "message": "'constructor.name' is not reliable after code minifier usage.",
      },

      // Ban get and set accessors:
      {
        "selector": "Property:matches([kind = \"get\"] , [kind = \"set\"]), MethodDefinition:matches([kind = \"get\"] , [kind = \"set\"])",
        "message": "Don't use get and set accessors.",
      },
    ],
  },
}
```

```JSONC
{
  "rules": {
    "no-restricted-syntax": [
      "error",

      // Ban `private` members:
      {
        "selector": ":matches(PropertyDefinition, MethodDefinition)[accessibility=\"private\"]",
        "message": "Use `#private` members instead.",
      },

      // Ban `#private` members:
      {
        "selector": ":matches(PropertyDefinition, MethodDefinition) > PrivateIdentifier.key",
        "message": "Use the `private` modifier instead.",
      },

      // Ban static `this`:
      {
        "selector": "MethodDefinition[static = true] ThisExpression",
        "message": "Prefer using the class's name directly.",
      },
    ],
  },
}
```

```JSONC
{
  "rules": {
    "no-restricted-syntax": [
      "error",

      // Ban all enums:
      {
        "selector": "TSEnumDeclaration",
        "message": "My reason for not using any enums at all.",
      },

      // Ban just `const` enums:
      {
        "selector": "TSEnumDeclaration[const=true]",
        "message": "My reason for not using const enums.",
      },

      // Ban just non-`const` enums:
      {
        "selector": "TSEnumDeclaration:not([const=true])",
        "message": "My reason for not using non-const enums.",
      },
    ],
  },
}
```

```JSONC
{
  "rules": {
    "no-restricted-syntax": [
      "error",
      // enforce tuple members have labels
      {
        "selector": "TSTupleType > :not(TSNamedTupleMember)",
        "message": "All tuples should have labels.",
      },
    ],
  },
}
```

--------------------------------

### Configure basic ESLint flat config with `typescript-eslint`

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/website/blog/2024-02-12-announcing-typescript-eslint-v7.md

This JavaScript snippet shows the simplest way to set up an `eslint.config.js` file using the new `typescript-eslint` package. It imports recommended configurations from both ESLint and `typescript-eslint`, enabling their respective plugins and parsers for basic linting.

```javascript
// @ts-check

import eslint from '@eslint/js';
import tseslint from 'typescript-eslint';

export default tseslint.config(
  eslint.configs.recommended,
  ...tseslint.configs.recommended,
);
```

--------------------------------

### Require descriptions for TypeScript comment directives

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/docs/rules/ban-ts-comment.mdx

This snippet demonstrates the `allow-with-description` option, which enforces that TypeScript comment directives must be followed by a descriptive comment on the same line. This helps provide context for why a directive is used. The 'Incorrect' example shows a directive without a description, while the 'Correct' example includes the required description.

```typescript
if (false) {
  // @ts-expect-error
  console.log('hello');
}
if (false) {
  /* @ts-expect-error */
  console.log('hello');
}
```

```typescript
if (false) {
  // @ts-expect-error: Unreachable code error
  console.log('hello');
}
if (false) {
  /* @ts-expect-error: Unreachable code error */
  console.log('hello');
}
```

--------------------------------

### Configure ESLint with recommended TypeScript-ESLint configs

Source: https://github.com/typescript-eslint/typescript-eslint/blob/main/docs/users/Shared_Configurations.mdx

This snippet demonstrates a basic `eslint.config.mjs` setup using ESLint's and TypeScript-ESLint's recommended configurations. It utilizes the new Flat Config format to apply a standard set of linting rules.

```JavaScript
// @ts-check

import eslint from '@eslint/js';
import { defineConfig } from 'eslint/config';
import tseslint from 'typescript-eslint';

export default defineConfig(
  eslint.configs.recommended,
  tseslint.configs.recommended,
);
```