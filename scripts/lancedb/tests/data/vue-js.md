### Vue Constructor: Runtime vs. Compiler Usage (JavaScript)

Source: https://v2.vuejs.org/v2/guide/installation

Demonstrates when the Vue compiler is required. The first example requires the compiler because it uses the `template` option with a string. The second example does not require the compiler as it uses a `render` function.

```javascript
new Vue({
  template: '<div>{{ hi }}</div>'
})

new Vue({
  render (h) {
    return h('div', this.hi)
  }
})
```

--------------------------------

### Vue.js Installation via CDN (Production)

Source: https://v2.vuejs.org/v2/guide/installation

For production environments, it's recommended to link to a specific version of Vue.js from a CDN to ensure stability. This version is optimized for speed by stripping warnings.

```html
<script src="https://cdn.jsdelivr.net/npm/vue@2.7.16"></script>
```

--------------------------------

### Vue.js Installation via CDN (Development)

Source: https://v2.vuejs.org/v2/guide/installation

Include Vue.js using a script tag from a CDN for development purposes. This version includes full warnings and debug mode to help catch common mistakes. The `Vue` object will be globally available.

```html
<script src="https://cdn.jsdelivr.net/npm/vue@2.7.16/dist/vue.js"></script>
```

--------------------------------

### Vue.js Installation via NPM

Source: https://v2.vuejs.org/v2/guide/installation

The recommended method for installing Vue.js in large-scale applications using NPM. This command installs the latest stable version of Vue 2, pairing well with module bundlers like Webpack.

```bash
# latest stable
$ npm install vue@^2
```

--------------------------------

### Include Vue.js for Small Projects

Source: https://v2.vuejs.org/v2/guide/comparison

This snippet demonstrates how to include the Vue.js library into an HTML page using a script tag from a CDN. This is a straightforward method for getting started with Vue, especially for smaller projects or prototyping, as it requires no build system setup and can be used directly in production.

```html
<script src="https://cdn.jsdelivr.net/npm/vue@2"></script>
```

--------------------------------

### Vue.js ES Modules Installation via CDN

Source: https://v2.vuejs.org/v2/guide/installation

This snippet demonstrates how to include Vue.js using a script tag with `type="module"` for environments that support native ES Modules. It points to an ES Modules compatible build.

```html
<script type="module">
  import Vue from 'https://cdn.jsdelivr.net/npm/vue@2.7.16/dist/vue.esm.browser.js'
</script>
```

--------------------------------

### Vue.js Base Component Naming Convention

Source: https://v2.vuejs.org/v2/style-guide

Details the recommended naming convention for base components (presentational, dumb, or pure components) in Vue.js. These components should start with a specific prefix like 'Base', 'App', or 'V' to ensure consistent styling and behavior across the application. Examples show 'bad' generic names and 'good' examples with the recommended prefixes.

```text
components/
|- MyButton.vue
|- VueTable.vue
|- Icon.vue
```

```text
components/
|- BaseButton.vue
|- BaseTable.vue
|- BaseIcon.vue
```

```text
components/
|- AppButton.vue
|- AppTable.vue
|- AppIcon.vue
```

```text
components/
|- VButton.vue
|- VTable.vue
|- VIcon.vue
```

--------------------------------

### Bundle with Browserify and envify for Production

Source: https://v2.vuejs.org/v2/guide/deployment

This command-line example shows how to use Browserify with the `envify` transform to prepare a production build. It sets the `NODE_ENV` to 'production' and pipes the output through `uglifyjs` for minification and dead code elimination.

```bash
NODE_ENV=production browserify -g envify -e main.js | uglifyjs -c -m > build.js
```

--------------------------------

### Define and Register a Vue Component

Source: https://v2.vuejs.org/v2/guide

Demonstrates how to define a new Vue component named 'todo-item' globally using `Vue.component()`. This component has a simple template and is then used within a Vue instance.

```javascript
Vue.component('todo-item', {
  template: '<li>This is a todo</li>'
})

var app = new Vue({...})

```

--------------------------------

### Vue.js Component File Organization

Source: https://v2.vuejs.org/v2/style-guide

Illustrates the recommended practice of placing each Vue.js component in its own file, especially when using a build system. It contrasts the 'bad' example of defining multiple components within a single block with the 'good' examples showing separate .js or .vue files.

```javascript
Vue.component('TodoList', {
  // ...
})

Vue.component('TodoItem', {
  // ...
})
```

```text
components/
|- TodoList.js
|- TodoItem.js
```

```text
components/
|- TodoList.vue
|- TodoItem.vue
```

--------------------------------

### Use a Vue Component in a Template

Source: https://v2.vuejs.org/v2/guide

Shows how to include a previously registered Vue component, 'todo-item', within the template of another component or the main Vue instance. This illustrates basic component composition.

```html
<ol>
  <todo-item></todo-item>
</ol>

```

--------------------------------

### Installing a Vue Plugin

Source: https://v2.vuejs.org/v2/guide/plugins

Demonstrates how to install a Vue.js plugin using `Vue.use()`. This method can be called before initializing a new Vue instance and supports passing options. It also prevents duplicate installations.

```javascript
Vue.use(MyPlugin)

new Vue({
  //... options
})
```

```javascript
Vue.use(MyPlugin, { someOption: true })
```

--------------------------------

### Vue Instance with Data and Component Registration

Source: https://v2.vuejs.org/v2/guide

Combines component definition with props and a Vue instance that provides the data (`groceryList`) for the components. It shows how to mount the Vue instance to a specific DOM element and manage application data.

```javascript
Vue.component('todo-item', {
  props: ['todo'],
  template: '<li>{{ todo.text }}</li>'
})

var app7 = new Vue({
  el: '#app-7',
  data: {
    groceryList: [
      { id: 0, text: 'Vegetables' },
      { id: 1, text: 'Cheese' },
      { id: 2, text: 'Whatever else humans are supposed to eat' }
    ]
  }
})

```

--------------------------------

### Vue.js Single-File Component Filename Casing

Source: https://v2.vuejs.org/v2/style-guide

Explains the convention for naming single-file Vue components, recommending either PascalCase or kebab-case for consistency. It shows 'bad' examples with mixed or lowercase names and 'good' examples using PascalCase and kebab-case.

```text
components/
|- mycomponent.vue
```

```text
components/
|- myComponent.vue
```

```text
components/
|- MyComponent.vue
```

```text
components/
|- my-component.vue
```

--------------------------------

### Vue.js CSS Transition Example

Source: https://v2.vuejs.org/v2/guide/transitions

Demonstrates how to use Vue's `<transition>` component with CSS for enter and leave animations. It applies a 'slide-fade' transition with different easing functions for entering and leaving states. The example includes the Vue instance setup and the necessary CSS.

```html
<div id="example-1">
  <button @click="show = !show">
    Toggle render
  </button>
  <transition name="slide-fade">
    <p v-if="show">hello</p>
  </transition>
</div>
```

```javascript
new Vue({
  el: '#example-1',
  data: {
    show: true
  }
})
```

```css
/* Enter and leave animations can use different */
/* durations and timing functions.              */
.slide-fade-enter-active {
  transition: all .3s ease;
}
.slide-fade-leave-active {
  transition: all .8s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active below version 2.1.8 */ {
  transform: translateX(10px);
  opacity: 0;
}
```

--------------------------------

### Vue Application Structure with Multiple Components

Source: https://v2.vuejs.org/v2/guide

Presents an imaginary HTML template structure for a larger Vue application, illustrating how different components (app-nav, app-view, app-sidebar, app-content) can be nested to form a complex UI.

```html
<div id="app">
  <app-nav></app-nav>
  <app-view>
    <app-sidebar></app-sidebar>
    <app-content></app-content>
  </app-view>
</div>

```

--------------------------------

### Load ButterCMS via CDN

Source: https://v2.vuejs.org/v2/cookbook/serverless-blog

This code demonstrates how to include the ButterCMS library in your Vue.js project using a CDN link. This method is an alternative to package installation and is useful for quick setups or when not using a module bundler.

```html
<script src="https://cdnjs.buttercms.com/buttercms-1.1.0.min.js"></script>
```

--------------------------------

### Vue CLI Project Creation with TypeScript

Source: https://v2.vuejs.org/v2/guide/typescript

These shell commands guide the user through installing the Vue CLI and creating a new project that is pre-configured for TypeScript. The process involves choosing manual feature selection to include TypeScript support.

```bash
# 1. Install Vue CLI, if it's not already installed
npm install --global @vue/cli

# 2. Create a new project, then choose the "Manually select features" option
vue create my-project-name
```

--------------------------------

### Browserify Configuration for Vue Runtime-only (JSON)

Source: https://v2.vuejs.org/v2/guide/installation

Configures Browserify to use the runtime-only build of Vue by specifying an alias in the `package.json` file under the 'browser' key. This is typically used with older bundlers.

```json
{
  // ...
  "browser": {
    "vue": "vue/dist/vue.common.js"
  }
}
```

--------------------------------

### Include Vue.js Development Version via CDN

Source: https://v2.vuejs.org/v2/guide

This snippet shows how to include the development version of Vue.js (version 2) in an HTML file using a CDN. This version includes helpful console warnings for debugging purposes. It is suitable for development environments.

```html
<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
```

--------------------------------

### Vue.js: Declarative Rendering with Template Syntax

Source: https://v2.vuejs.org/v2/guide

Demonstrates basic Vue.js declarative rendering using template syntax to display data. It binds a message to a div element. Requires Vue.js library.

```html
<div id="app">  
  {{ message }}  
</div>  
```

```javascript
var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!'
  }
})
```

--------------------------------

### Initializing Data Properties (JavaScript)

Source: https://v2.vuejs.org/v2/guide/instance

Provides an example of how to initialize various data properties for a Vue instance. It's crucial to define properties upfront for reactivity.

```javascript
data: {
  newTodoText: '',
  visitCount: 0,
  hideCompletedTodos: false,
  todos: [],
  error: null
}
```

--------------------------------

### Configure Browserify with Grunt and envify for Production

Source: https://v2.vuejs.org/v2/guide/deployment

This Grunt configuration uses `grunt-browserify` and the `envify` transform to prepare a production build. It customizes the Browserify setup to include `vueify` and `envify`, ensuring `NODE_ENV` is set to 'production' for Vue.js.

```javascript
// Use the envify custom module to specify environment variables
var envify = require('envify/custom')

browserify: {
  dist: {
    options: {
      // Function to deviate from grunt-browserify's default order
      configure: b => b
        .transform('vueify')
        .transform(
          // Required in order to process node_modules files
          { global: true },
          envify({ NODE_ENV: 'production' })
        )
        .bundle()
    }
  }
}
```

--------------------------------

### Writing a Vue Plugin with an Install Method

Source: https://v2.vuejs.org/v2/guide/plugins

Illustrates the structure of a Vue.js plugin, which must expose an `install` method. This method receives the `Vue` constructor and optional options, allowing the plugin to add global methods, directives, mixins, or instance methods.

```javascript
MyPlugin.install = function (Vue, options) {
  // 1. add global method or property
  Vue.myGlobalMethod = function () {
    // some logic ...
  }

  // 2. add a global asset
  Vue.directive('my-directive', {
    bind (el, binding, vnode, oldVnode) {
      // some logic ...
    }
    ...
  })

  // 3. inject some component options
  Vue.mixin({
    created: function () {
      // some logic ...
    }
    ...
  })

  // 4. add an instance method
  Vue.prototype.$myMethod = function (methodOptions) {
    // some logic ...
  }
}
```

--------------------------------

### Vue.js: List Rendering with v-for

Source: https://v2.vuejs.org/v2/guide

Demonstrates rendering lists of data in Vue.js using the v-for directive. It iterates over an array of objects to create list items. Requires Vue.js library.

```html
<div id="app-4">  
  <ol>  
    <li v-for="todo in todos">  
      {{ todo.text }}  
    </li>  
  </ol>  
</div>  
```

```javascript
var app4 = new Vue({
  el: '#app-4',
  data: {
    todos: [
      { text: 'Learn JavaScript' },
      { text: 'Learn Vue' },
      { text: 'Build something awesome' }
    ]
  }
})
```

--------------------------------

### Rollup Production Mode Configuration (JavaScript)

Source: https://v2.vuejs.org/v2/guide/installation

Configures Rollup to replace `process.env.NODE_ENV` with 'production' using `rollup-plugin-replace`. This ensures Vue runs in production mode and helps in code stripping by minifiers.

```javascript
const replace = require('rollup-plugin-replace')

rollup({
  // ...
  plugins: [
    replace({
      'process.env.NODE_ENV': JSON.stringify('production')
    })
  ]
}).then(...)
```

--------------------------------

### Simulate replace: false with render function

Source: https://v2.vuejs.org/v2/guide/migration

An alternative to simulating `replace: false` is to use a render function. This example demonstrates creating a wrapper `div` with specific attributes.

```javascript
new Vue({
  el: '#app',
  render: function (h) {
    h('div', {
      attrs: {
        id: 'app',
      }
    }, /* ... */)
  }
})
```

--------------------------------

### Vue Router Initialization: Old vs. New

Source: https://v2.vuejs.org/v2/guide/migration-vue-router

Demonstrates the shift from the `router.start` initialization method in older Vue Router versions to passing the router as a property to a Vue instance in newer versions. This covers both standard and runtime-only Vue builds.

```javascript
router.start({
  template: '<router-view></router-view>'
}, '#app')
```

```javascript
new Vue({
  el: '#app',
  router: router,
  template: '<router-view></router-view>'
})
```

```javascript
new Vue({
  el: '#app',
  router: router,
  render: h => h('router-view')
})
```

--------------------------------

### Pass Data to Component using v-bind and v-for

Source: https://v2.vuejs.org/v2/guide

Demonstrates using `v-for` to iterate over a list and `v-bind:todo` to pass individual items as props to the 'todo-item' component. This enables dynamic rendering of lists based on parent data.

```html
<div id="app-7">
  <ol>
    <todo-item
      v-for="item in groceryList"
      v-bind:todo="item"
      v-bind:key="item.id"
    ></todo-item>
  </ol>
</div>

```

--------------------------------

### Rollup Alias Configuration for Vue Runtime-only (JavaScript)

Source: https://v2.vuejs.org/v2/guide/installation

Configures Rollup to use the runtime-only build of Vue by using the `rollup-plugin-alias`. This is recommended when using pre-compiled templates.

```javascript
const alias = require('rollup-plugin-alias')

rollup({
  // ...
  plugins: [
    alias({
      'vue': require.resolve('vue/dist/vue.esm.js')
    })
  ]
})
```

--------------------------------

### Define Vue Component with Props

Source: https://v2.vuejs.org/v2/guide

Illustrates how to define a Vue component ('todo-item') that accepts a prop named 'todo'. This allows the component to receive dynamic data from its parent, making the rendered output customizable.

```javascript
Vue.component('todo-item', {
  props: ['todo'],
  template: '<li>{{ todo.text }}</li>'
})

```

--------------------------------

### Install ButterCMS Package for Vue.js

Source: https://v2.vuejs.org/v2/cookbook/serverless-blog

This snippet shows how to install the ButterCMS package as a dependency for your Vue.js project using npm. This is the first step to integrating ButterCMS content into your application.

```bash
npm install buttercms --save
```

--------------------------------

### Vue.js Private Property Naming Convention

Source: https://v2.vuejs.org/v2/style-guide

Demonstrates the recommended convention for naming private properties in Vue.js plugins or mixins to avoid conflicts with Vue's internal properties and other authors' code. It shows the 'bad' examples using single underscores or dollar signs, and the 'good' examples using a combination of underscore and a scoped prefix.

```javascript
var myGreatMixin = {
  // ...
  methods: {
    update: function () {
      // ...
    }
  }
}
```

```javascript
var myGreatMixin = {
  // ...
  methods: {
    _update: function () {
      // ...
    }
  }
}
```

```javascript
var myGreatMixin = {
  // ...
  methods: {
    $update: function () {
      // ...
    }
  }
}
```

```javascript
var myGreatMixin = {
  // ...
  methods: {
    $_update: function () {
      // ...
    }
  }
}
```

```javascript
var myGreatMixin = {
  // ...
  methods: {
    $_myGreatMixin_update: function () {
      // ...
    }
  }
}
```

```javascript
// Even better!
var myGreatMixin = {
  // ...
  methods: {
    publicMethod() {
      // ...
      myPrivateFunction()
    }
  }
}

function myPrivateFunction() {
  // ...
}

export default myGreatMixin
```

--------------------------------

### Vue.js: Handling Click Events with v-on

Source: https://v2.vuejs.org/v2/guide

Shows how to handle user interactions in Vue.js using the v-on directive to attach event listeners, specifically a click event to reverse a message. Requires Vue.js library.

```html
<div id="app-5">  
  <p>{{ message }}</p>  
  <button v-on:click="reverseMessage">Reverse Message</button>  
</div>  
```

```javascript
var app5 = new Vue({
  el: '#app-5',
  data: {
    message: 'Hello Vue.js!'
  },
  methods: {
    reverseMessage: function () {
      this.message = this.message.split('').reverse().join('')
    }
  }
})
```

--------------------------------

### Parcel Alias Configuration for Vue Runtime-only (JSON)

Source: https://v2.vuejs.org/v2/guide/installation

Configures Parcel to use the runtime-only build of Vue by specifying an alias in the `package.json` file under the 'alias' key. This helps in reducing the final bundle size by excluding the compiler.

```json
{
  // ...
  "alias": {
    "vue" : "./node_modules/vue/dist/vue.common.js"
  }
}
```

--------------------------------

### Vue.js: Attribute Binding with v-bind

Source: https://v2.vuejs.org/v2/guide

Shows how to use the v-bind directive in Vue.js to dynamically bind element attributes, such as the 'title' attribute, to data properties. Requires Vue.js library.

```html
<div id="app-2">  
  <span v-bind:title="message">  
    Hover your mouse over me for a few seconds  
    to see my dynamically bound title!  
  </span>  
</div>  
```

```javascript
var app2 = new Vue({
  el: '#app-2',
  data: {
    message: 'You loaded this page on ' + new Date().toLocaleString()
  }
})
```

--------------------------------

### Webpack DefinePlugin for Production Mode (JavaScript)

Source: https://v2.vuejs.org/v2/guide/installation

Configures Webpack (versions 3 and earlier) to use DefinePlugin to set `process.env.NODE_ENV` to 'production'. This allows Vue to run in production mode and enables minifiers to remove development-specific code.

```javascript
var webpack = require('webpack')

module.exports = {
  // ...
  plugins: [
    // ...
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: JSON.stringify('production')
      }
    })
  ]
}
```

--------------------------------

### Initialize ButterCMS with API Token (CommonJS)

Source: https://v2.vuejs.org/v2/cookbook/serverless-blog

This JavaScript snippet shows how to initialize the ButterCMS client using the CommonJS module system and your unique API token. This is typically used in Node.js environments or older browser setups.

```javascript
var butter = require('buttercms')('your_api_token');
```

--------------------------------

### Webpack Alias Configuration for Vue Runtime-only (JavaScript)

Source: https://v2.vuejs.org/v2/guide/installation

Configures Webpack to use the runtime-only build of Vue by creating an alias for 'vue'. This is useful when templates in *.vue files are pre-compiled by `vue-loader` or `vueify`.

```javascript
module.exports = {
  // ...
  resolve: {
    alias: {
      'vue$': 'vue/dist/vue.esm.js' // 'vue/dist/vue.common.js' for webpack 1
    }
  }
}
```

--------------------------------

### Vue.js: Conditional Rendering with v-if

Source: https://v2.vuejs.org/v2/guide

Illustrates conditional rendering in Vue.js using the v-if directive. An element is rendered only if the bound data property is true. Requires Vue.js library.

```html
<div id="app-3">  
  <span v-if="seen">Now you see me</span>  
</div>  
```

```javascript
var app3 = new Vue({
  el: '#app-3',
  data: {
    seen: true
  }
})
```

--------------------------------

### Replacing Vue Resource with Axios in Vue

Source: https://v2.vuejs.org/v2/cookbook/adding-instance-properties

This example shows how to integrate Axios into a Vue project and alias it to `Vue.prototype.$http`. This allows developers to continue using the familiar `this.$http` syntax for making API requests, similar to the retired Vue Resource library. It includes the CDN link for Axios and a basic Vue instance setup.

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/axios/0.15.2/axios.js"></script>

<div id="app">
  <ul>
    <li v-for="user in users">{{ user.name }}</li>
  </ul>
</div>
```

```javascript
Vue.prototype.$http = axios
```

```javascript
new Vue({
  el: '#app',
  data: {
    users: []
  },
  created() {
    var vm = this
    this.$http
      .get('https://jsonplaceholder.typicode.com/users')
      .then(function(response) {
        vm.users = response.data
      })
  }
})
```

--------------------------------

### Query Array Syntax: [] removed

Source: https://v2.vuejs.org/v2/guide/migration-vue-router

Illustrates the removal of the `[]` syntax for array query parameters. Shows the new format and provides a computed property example to ensure `$route.query.users` is always an array.

```javascript
export default {
  // ...
  computed: {
    // users will always be an array
    users () {
      const users = this.$route.query.users
      return Array.isArray(users) ? users : [users]
    }
  }
}
```

--------------------------------

### Vue.js v2: Recommended Component/Instance Options Order

Source: https://v2.vuejs.org/v2/style-guide

This JavaScript code demonstrates the recommended order for component options in Vue.js v2. Following this order improves code readability and maintainability by categorizing options logically.

```javascript
props: {
  value: {
    type: String,
    required: true
  },

  focused: {
    type: Boolean,
    default: false
  },

  label: String,
  icon: String
},

computed: {
  formattedValue: function () {
    // ...
  },

  inputClasses: function () {
    // ...
  }
}


```

```javascript
// No spaces are also fine, as long as the component
// is still easy to read and navigate.
props: {
  value: {
    type: String,
    required: true
  },
  focused: {
    type: Boolean,
    default: false
  },
  label: String,
  icon: String
},
computed: {
  formattedValue: function () {
    // ...
  },
  inputClasses: function () {
    // ...
  }
}


```

--------------------------------

### Vue.js Main App Initialization

Source: https://v2.vuejs.org/v2/cookbook/practical-use-of-scoped-slots

This is the main JavaScript file for a Vue.js application. It configures Vue, imports the root App component, and initializes the Vue instance, mounting it to the '#app' element in the HTML.

```javascript
// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from "vue";
import App from "./App";

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: "#app",
  components: { App },
  template: "<App/>"
});
```

--------------------------------

### Simulate replace: false with wrapper element

Source: https://v2.vuejs.org/v2/guide/migration

The `replace: false` option is removed. To achieve similar behavior, wrap your root component in an element. This example shows using a `div` with the ID 'app' for wrapping.

```javascript
new Vue({
  el: '#app',
  template: '<div id="app"> ... </div>'
})
```

--------------------------------

### Create a Vue Instance (JavaScript)

Source: https://v2.vuejs.org/v2/guide/instance

Demonstrates the basic process of creating a Vue instance using the `Vue` constructor and passing an options object. This is the entry point for any Vue application.

```javascript
var vm = new Vue({
  // options
})
```

--------------------------------

### Vue 2 Modal Component Example

Source: https://v2.vuejs.org/v2/examples/modal

An example of a modal component in Vue.js, demonstrating features like component creation, prop passing, content insertion, and transitions. It includes a button to trigger a 'close' event.

```html
<button class="modal-default-button" @click="$emit('close')">

```

--------------------------------

### Vue.js CSS Animation Example

Source: https://v2.vuejs.org/v2/guide/transitions

Illustrates using Vue's `<transition>` component with CSS animations. This example uses a 'bounce' animation for entering and reversing the animation for leaving. It includes the Vue instance configuration and the CSS keyframes and animation classes.

```html
<div id="example-2">
  <button @click="show = !show">Toggle show</button>
  <transition name="bounce">
    <p v-if="show">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris facilisis enim libero, at lacinia diam fermentum id. Pellentesque habitant morbi tristique senectus et netus.</p>
  </transition>
</div>
```

```javascript
new Vue({
  el: '#example-2',
  data: {
    show: true
  }
})
```

```css
.bounce-enter-active {
  animation: bounce-in .5s;
}
.bounce-leave-active {
  animation: bounce-in .5s reverse;
}
@keyframes bounce-in {
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(1.5);
  }
  100% {
    transform: scale(1);
  }
}
```

--------------------------------

### Configure Browserify with Gulp and envify for Production

Source: https://v2.vuejs.org/v2/guide/deployment

This Gulp configuration demonstrates setting up Browserify to include the `envify` transform globally. This ensures that `process.env.NODE_ENV` is correctly set to 'production' during the bundling process, allowing Vue.js to enter production mode.

```javascript
// Use the envify custom module to specify environment variables
var envify = require('envify/custom')

browserify(browserifyOptions)
  .transform(vueify)
  .transform(
    // Required in order to process node_modules files
    { global: true },
    envify({ NODE_ENV: 'production' })
  )
  .bundle()
```

--------------------------------

### Vue Component Setup for Transitions

Source: https://v2.vuejs.org/v2/guide/transitions

Sets up a Vue instance with dynamic components 'v-a' and 'v-b', controlled by the 'view' data property. This is used in conjunction with the <transition> component for animating component changes.

```javascript
new Vue({
  el: '#transition-components-demo',
  data: {
    view: 'v-a'
  },
  components: {
    'v-a': {
      template: '<div>Component A</div>'
    },
    'v-b': {
      template: '<div>Component B</div>'
    }
  }
})
```

--------------------------------

### Vuex Plugins: Replacing Middlewares

Source: https://v2.vuejs.org/v2/guide/migration-vuex

Shows how Vuex middlewares have been replaced by plugins. A plugin is a function that receives the store and can subscribe to mutation events.

```javascript
const myPlugins = store => {
  store.subscribe('mutation', (mutation, state) => {
    // Do something...
  })
}
```

--------------------------------

### Vue Single-File Component Example (.vue)

Source: https://v2.vuejs.org/v2/guide/single-file-components

Demonstrates the structure of a Vue.js single-file component, including template, script, and style sections. This format allows for complete syntax highlighting, CommonJS modules, and component-scoped CSS, and supports preprocessors.

```vue
<template>
  <div>This will be pre-compiled</div>
</template>
<script src="./my-component.js"></script>
<style src="./my-component.css"></style>

```

--------------------------------

### Access Vue.js Version Information

Source: https://v2.vuejs.org/v2/api

Provides the installed version of Vue.js as a string. This is useful for implementing version-specific logic or ensuring compatibility with community plugins and components.

```javascript
var version = Number(Vue.version.split('.')[0])

if (version === 2) {
  // Vue v2.x.x
} else if (version === 1) {
  // Vue v1.x.x
} else {
  // Unsupported versions of Vue
}
```

--------------------------------

### Vue.js component wrapper for module export and auto-install

Source: https://v2.vuejs.org/v2/cookbook/packaging-sfc-for-npm

This JavaScript code serves as a wrapper for a Vue.js Single File Component (SFC). It provides an 'install' function for Vue.use(), attempts to auto-install the component if Vue is globally available, and exports the component for module usage.

```javascript
// Import vue component
import component from './my-component.vue';

// Declare install function executed by Vue.use()
export function install(Vue) {
	if (install.installed) return;
	install.installed = true;
	Vue.component('MyComponent', component);
}

// Create module definition for Vue.use()
const plugin = {
	install,
};

// Auto-install when vue is found (eg. in browser via <script> tag)
let GlobalVue = null;
if (typeof window !== 'undefined') {
	GlobalVue = window.Vue;
} else if (typeof global !== 'undefined') {
	GlobalVue = global.Vue;
}
if (GlobalVue) {
	GlobalVue.use(plugin);
}

// To allow use as module (npm/webpack/etc.) export component
export default component;
```

--------------------------------

### Initialize ButterCMS with API Token (CDN)

Source: https://v2.vuejs.org/v2/cookbook/serverless-blog

This JavaScript code shows how to initialize the ButterCMS client after loading it via CDN. It uses the globally available `Butter` object and your API token to set up the client for use in the browser.

```html
<script src="https://cdnjs.buttercms.com/buttercms-1.1.0.min.js"></script>
<script>
  var butter = Butter('your_api_token');
</script>
```

--------------------------------

### Vue Router Dynamic Route Generation and Addition

Source: https://v2.vuejs.org/v2/guide/migration-vue-router

Shows how to programmatically generate routes using `routes.push` and how to add new routes after the router has been instantiated by replacing the router's matcher. This replaces the functionality of the removed `router.on`.

```javascript
// Normal base routes
var routes = [
  // ...
]

// Dynamically generated routes
marketingPages.forEach(function (page) {
  routes.push({
    path: '/marketing/' + page.slug,
    component: {
      extends: MarketingComponent,
      data: function () {
        return { page: page }
      }
    }
  })
})

var router = new Router({
  routes: routes
})
```

```javascript
router.match = createMatcher(
  [{ 
    path: '/my/new/path',
    component: MyComponent
  }].concat(router.options.routes)
)
```

--------------------------------

### Multi-column Sorting with lodash `orderBy` (JavaScript)

Source: https://v2.vuejs.org/v2/guide/migration

Demonstrates sorting an array of objects by multiple columns using lodash's `orderBy` function. This example specifies sorting by 'name' in ascending order and 'last_login' in descending order. It requires the lodash library to be included.

```javascript
_.orderBy(this.users, ['name', 'last_login'], ['asc', 'desc'])
```

--------------------------------

### Named Parameters: '*' replaced with ':param+'

Source: https://v2.vuejs.org/v2/guide/migration-vue-router

Details the syntax change for matching one or more named parameters in routes. The previous `*` syntax is replaced with the more specific `:param+`.

```regex
/category/*tags
```

```regex
/category/:tags+
```

--------------------------------

### Configure KeyCodes with Vue.config.keyCodes

Source: https://v2.vuejs.org/v2/guide/migration

Replaces the deprecated `Vue.directive('on').keyCodes` with the more concise `Vue.config.keyCodes`. This allows direct mapping of key codes to names, simplifying keyboard event handling.

```javascript
// enable v-on:keyup.f1  
Vue.config.keyCodes.f1 = 112  

```

--------------------------------

### Vue Provide/Inject Basic Example

Source: https://v2.vuejs.org/v2/api

Shows the basic usage of 'provide' and 'inject' in Vue.js (v2.2.0+). The 'provide' option allows an ancestor component to make data available to its descendants. The 'inject' option allows descendants to access this data.

```javascript
// parent component providing 'foo'
var Provider = {
  provide: {
    foo: 'bar'
  },
  // ...
}

// child component injecting 'foo'
var Child = {
  inject: ['foo'],
  created () {
    console.log(this.foo) // => "bar"
  }
  // ...
}
```

--------------------------------

### Replace vm.$before with insertBefore

Source: https://v2.vuejs.org/v2/guide/migration

The `vm.$before` method is no longer available. Use the native DOM API's `insertBefore` method. The usage is `myElement.parentNode.insertBefore(vm.$el, myElement)`.

```javascript
myElement.parentNode.insertBefore(vm.$el, myElement)
```

--------------------------------

### Vue Component Data Initialization

Source: https://v2.vuejs.org/v2/style-guide

Demonstrates how to initialize component data in Vue.js. Returning data from a function ensures each component instance has its own unique data object, preventing state conflicts when components are reused. This is crucial for maintaining independent component states.

```javascript
data: function () {
  return {
    listTitle: '',
    todos: []
  }
}
```

```javascript
export default {
  data () {
    return {
      foo: 'bar'
    }
  }
}
```

```javascript
new Vue({
  data: {
    foo: 'bar'
  }
})
```

--------------------------------

### Vuex store.watch: String Path to Function

Source: https://v2.vuejs.org/v2/guide/migration-vuex

Demonstrates the change in Vuex's `store.watch` method, requiring a function to return the observed property instead of a string path. This provides more control over reactive property observation.

```javascript
store.watch('user.notifications', callback)
```

```javascript
store.watch(
  // When the returned result changes...
  function (state) {
    return state.user.notifications
  },
  // Run this callback
  callback
)
```

--------------------------------

### Serve Vue CLI Application with npm

Source: https://v2.vuejs.org/v2/cookbook/debugging-in-vscode

This command is used to serve a Vue CLI application from the root folder using npm. It starts the development server, allowing the application to be accessed in the browser and debugged with VS Code.

```bash
npm run serve
```

--------------------------------

### JavaScript-Only Transition with Velocity.js Example

Source: https://v2.vuejs.org/v2/guide/transitions

Example demonstrating a JavaScript-only transition using Velocity.js. It disables CSS detection with `v-bind:css="false"` and utilizes `enter` and `leave` hooks with `done` callbacks for animation completion. Requires Velocity.js library.

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/velocity/1.2.3/velocity.min.js"></script>

<div id="example-4">
  <button @click="show = !show">
    Toggle
  </button>
  <transition
    v-on:before-enter="beforeEnter"
    v-on:enter="enter"
    v-on:leave="leave"
    v-bind:css="false"
  >
    <p v-if="show">
      Demo
    </p>
  </transition>
</div>
```

```javascript
new Vue({
  el: '#example-4',
  data: {
    show: false
  },
  methods: {
    beforeEnter: function (el) {
      el.style.opacity = 0
      el.style.transformOrigin = 'left'
    },
    enter: function (el, done) {
      Velocity(el, { opacity: 1, fontSize: '1.4em' }, { duration: 300 })
      Velocity(el, { fontSize: '1em' }, { complete: done })
    },
    leave: function (el, done) {
      Velocity(el, { translateX: '15px', rotateZ: '50deg' }, { duration: 600 })
      Velocity(el, { rotateZ: '100deg' }, { loop: 2 })
      Velocity(el, {
        rotateZ: '45deg',
        translateY: '30px',
        translateX: '30px',
        opacity: 0
      }, { complete: done })
    }
  }
})
```

--------------------------------

### Vue Component with Slot for Content Distribution

Source: https://v2.vuejs.org/v2/guide/components

This snippet demonstrates how to create a Vue component ('alert-box') that accepts and renders content passed to it via a slot. It shows the component's template with a slot element and an example of how to use the component with content.

```html
<alert-box>
  Something bad happened.
</alert-box>
```

```javascript
Vue.component('alert-box', {
  template: '
    <div class="demo-alert-box">
      <strong>Error!</strong>
      <slot></slot>
    </div>
  '
})
```

--------------------------------

### Fetch API Data with Axios in Vue.js (Base Example)

Source: https://v2.vuejs.org/v2/cookbook/using-axios-to-consume-apis

This snippet shows the basic implementation of fetching data from an API using Axios within a Vue.js application. It initializes a 'info' data property and uses the 'mounted' lifecycle hook to make a GET request. The response is then stored in 'this.info'. Dependencies include Vue.js and Axios.

```javascript
new Vue({
  el: '#app',
  data () {
    return {
      info: null
    }
  },
  mounted () {
    axios
      .get('https://api.coindesk.com/v1/bpi/currentprice.json')
      .then(response => (this.info = response))
  }
})
```

--------------------------------

### Include deepstream.io Client Library in HTML

Source: https://v2.vuejs.org/v2/examples/deepstream

This snippet shows how to include the deepstream.io client JavaScript library using a CDN link in an HTML file. This is a prerequisite for using deepstreamHub's realtime features in a web application.

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/deepstream.io-client-js/2.1.1/deepstream.js"></script>
```

--------------------------------

### Vue.js: Anchored Heading Component Example

Source: https://v2.vuejs.org/v2/guide/render-function

A complete Vue.js component example demonstrating the use of createElement within a render function to create an anchored heading. It includes logic to generate an ID from the heading text and create a link.

```javascript
var getChildrenTextContent = function (children) {
  return children.map(function (node) {
    return node.children
      ? getChildrenTextContent(node.children)
      : node.text
  }).join('')
}

Vue.component('anchored-heading', {
  render: function (createElement) {
    // create kebab-case id
    var headingId = getChildrenTextContent(this.$slots.default)
      .toLowerCase()
      .replace(/\W+/g, '-')
      .replace(/(^-|-$)/g, '')

    return createElement(
      'h' + this.level,
      [
        createElement('a', {
          attrs: {
            name: headingId,
            href: '#' + headingId
          }
        }, this.$slots.default)
      ]
    )
  },
  props: {
    level: {
      type: Number,
      required: true
    }
  }
})
```

--------------------------------

### Vue List Transition Setup

Source: https://v2.vuejs.org/v2/guide/transitions

Configures a Vue instance to manage a list of items with add and remove functionality. It utilizes the <transition-group> component for animating individual list item changes.

```javascript
new Vue({
  el: '#list-demo',
  data: {
    items: [1,2,3,4,5,6,7,8,9],
    nextNum: 10
  },
  methods: {
    randomIndex: function () {
      return Math.floor(Math.random() * this.items.length)
    },
    add: function () {
      this.items.splice(this.randomIndex(), 0, this.nextNum++)
    },
    remove: function () {
      this.items.splice(this.randomIndex(), 1)
    },
  }
})
```

--------------------------------

### Dockerfile for Vue.js App with http-server

Source: https://v2.vuejs.org/v2/cookbook/dockerize-vuejs-app

This Dockerfile sets up an environment to build and serve a Vue.js application using the 'http-server' package. It installs dependencies, builds the app, and exposes port 8080 for access. It's suitable for simple deployments and prototyping.

```dockerfile
FROM node:lts-alpine  
  
# install simple http server for serving static content  
RUN npm install -g http-server  
  
# make the 'app' folder the current working directory  
WORKDIR /app  
  
# copy both 'package.json' and 'package-lock.json' (if available)  
COPY package*.json ./
  
# install project dependencies  
RUN npm install  
  
# copy project files and folders to the current working directory (i.e. 'app' folder)  
COPY . .
  
# build app for production with minification  
RUN npm run build  
  
EXPOSE 8080  
CMD [ "http-server", "dist" ]  

```

--------------------------------

### Vue.js Custom Transition Classes Example

Source: https://v2.vuejs.org/v2/guide/transitions

Shows how to apply custom CSS classes for transitions in Vue.js using attributes like `enter-active-class` and `leave-active-class`. This example integrates with the Animate.css library to apply 'tada' and 'bounceOutRight' animations during enter and leave states, respectively.

```html
<link href="https://cdn.jsdelivr.net/npm/animate.css@3.5.1" rel="stylesheet" type="text/css">

<div id="example-3">
  <button @click="show = !show">
    Toggle render
  </button>
  <transition
    name="custom-classes-transition"
    enter-active-class="animated tada"
    leave-active-class="animated bounceOutRight"
  >
    <p v-if="show">hello</p>
  </transition>
</div>
```

```javascript
new Vue({
  el: '#example-3',
  data: {
    show: true
  }
})
```

--------------------------------

### HTML Structure for Vue.js Application

Source: https://v2.vuejs.org/v2/examples

Basic HTML file structure for a Vue.js application, including a link to an external CSS stylesheet. This is a common setup for front-end projects using Vue.

```html
<link rel="stylesheet" type="text/css" href="/style.css" />
```

--------------------------------

### Configure Vue Router for Blog Navigation

Source: https://v2.vuejs.org/v2/cookbook/serverless-blog

Sets up routes for the blog home page ('/blog/') and individual blog posts ('/blog/:slug') using Vue Router. It imports necessary components and configures the router instance.

```javascript
import Vue from 'vue'
import Router from 'vue-router'
import BlogHome from '@/components/BlogHome'
import BlogPost from '@/components/BlogPost'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/blog/',
      name: 'blog-home',
      component: BlogHome
    },
    {
      path: '/blog/:slug',
      name: 'blog-post',
      component: BlogPost
    }
  ]
})
```

--------------------------------

### Vue Tree View Component Implementation

Source: https://v2.vuejs.org/v2/examples/tree-view

A simple tree view component in Vue.js that demonstrates recursive component usage. This example allows users to interact with list items, turning them into folders upon double-clicking. It's a foundational piece for building hierarchical data displays.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vue Tree View Example</title>
    <style>
        /* Basic styling for the tree view */
        .tree-node {
            cursor: pointer;
            padding: 5px;
        }
        .folder::before {
            content: '\1F4C1 '; /* Folder emoji */
        }
        .file::before {
            content: '\1F4C4 '; /* File emoji */
        }
    </style>
</head>
<body>
    <div id="app">
        <tree-node :node="treeData"></tree-node>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/vue@2.6.14/dist/vue.js"></script>
    <script>
        Vue.component('tree-node', {
            template: '#tree-node-template',
            props: ['node'],
            methods: {
                toggleFolder: function(node) {
                    if (node.isFolder) {
                        node.isOpen = !node.isOpen;
                    }
                },
                makeFolder: function(node) {
                    if (!node.isFolder) {
                        node.isFolder = true;
                        node.isOpen = true;
                    }
                }
            }
        });

        new Vue({
            el: '#app',
            data: {
                treeData: {
                    name: 'Root',
                    isFolder: true,
                    isOpen: true,
                    children: [
                        { name: 'Folder 1', isFolder: true, isOpen: false, children: [
                            { name: 'File 1.txt', isFolder: false },
                            { name: 'File 2.doc', isFolder: false }
                        ]},
                        { name: 'File 3.pdf', isFolder: false },
                        { name: 'Another Folder', isFolder: true, isOpen: true, children: [
                            { name: 'Sub File.jpg', isFolder: false },
                            { name: 'Sub Folder', isFolder: true, isOpen: false, children: [
                                { name: 'Deep File.png', isFolder: false }
                            ]}
                        ]}
                    ]
                }
            }
        });
    </script>

    <script type="text/x-template" id="tree-node-template">
        <div>
            <span @dblclick="makeFolder(node)" @click="toggleFolder(node)" :class="{'folder': node.isFolder, 'file': !node.isFolder}" class="tree-node">
                {{ node.name }}
            </span>
            <div v-if="node.isFolder && node.isOpen" style="margin-left: 20px;">
                <tree-node v-for="(child, index) in node.children" :key="index" :node="child"></tree-node>
            </div>
        </div>
    </script>

    <p>(You can double click on an item to turn it into a folder.)</p>
</body>
</html>
```

--------------------------------

### Vue Dynamic Functional Component Example

Source: https://v2.vuejs.org/v2/guide/render-function

A practical example of a functional component (`smart-list`) that dynamically renders different list components based on the provided props (`items`, `isOrdered`). This highlights the use of `context.props` and conditional rendering.

```javascript
var EmptyList = { /* ... */ }
var TableList = { /* ... */ }
var OrderedList = { /* ... */ }
var UnorderedList = { /* ... */ }
  
Vue.component('smart-list', {
  functional: true,
  props: {
    items: {
      type: Array,
      required: true
    },
    isOrdered: Boolean
  },
  render: function (createElement, context) {
    function appropriateListComponent () {
      var items = context.props.items

      if (items.length === 0)           return EmptyList
      if (typeof items[0] === 'object') return TableList
      if (context.props.isOrdered)      return OrderedList

      return UnorderedList
    }

    return createElement(
      appropriateListComponent(),
      context.data,
      context.children
    )
  }
})
```