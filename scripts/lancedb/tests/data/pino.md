# pino-pretty

pino-pretty is a prettifier for Pino log lines, designed for development environments. It transforms NDJSON log output from Pino (and compatible loggers) into human-readable, colorized terminal output. The module processes log lines by parsing JSON, extracting key fields like timestamps, log levels, and messages, then formatting them with configurable options including color schemes, custom formatters, and flexible message templates.

This tool can be used as a CLI utility, piped from any NDJSON logger, or integrated programmatically as a Pino transport or transform stream. It supports extensive customization through options for filtering, colorization, custom prettifiers for specific log properties, message formatting templates, and timestamp translation. The prettifier intelligently handles error objects, nested properties, and custom log levels while maintaining high performance through streaming architecture.

## CLI Usage

Basic command-line prettification by piping NDJSON logs.

```bash
# Basic usage - prettify Pino logs from Node.js application
node app.js | pino-pretty

# With colorized output
node app.js | pino-pretty --colorize

# Display log level first, translate timestamps, hide hostname
node app.js | pino-pretty -l -t "yyyy-mm-dd HH:MM:ss" -i hostname

# Filter by minimum log level (only show warnings and above)
node app.js | pino-pretty --minimumLevel warn

# Custom message format with conditional fields
node app.js | pino-pretty -o "{levelLabel} - {if pid}{pid} - {end}url:{req.url}"

# Single-line output with custom colors for levels
node app.js | pino-pretty --singleLine --customColors "error:red,warn:yellow,info:green"

# Hide all objects except errors
node app.js | pino-pretty --hideObject

# Using configuration file
node app.js | pino-pretty --config ./my-pino-pretty.config.js
```

## Programmatic Usage - Pino Transport

Integration as a Pino v7+ transport (recommended approach).

```javascript
const pino = require('pino');

// Basic transport usage
const logger = pino({
  transport: {
    target: 'pino-pretty'
  }
});

logger.info('Server started');
logger.warn('High memory usage detected');
logger.error({ err: new Error('Database connection failed') }, 'Error occurred');

// Transport with full options
const loggerWithOptions = pino({
  transport: {
    target: 'pino-pretty',
    options: {
      colorize: true,
      translateTime: 'SYS:yyyy-mm-dd HH:MM:ss',
      ignore: 'pid,hostname',
      singleLine: false,
      levelFirst: true,
      messageFormat: '{levelLabel} - {pid} - {msg}',
      customColors: 'info:blue,warn:yellow,error:red',
      errorProps: 'stack,code,signal'
    }
  }
});

loggerWithOptions.info({ user: 'john', action: 'login' }, 'User logged in');
// Output: INFO - 12345 - User logged in
//     user: "john"
//     action: "login"
```

## Programmatic Usage - Stream API

Direct usage as a transform stream with custom configuration.

```javascript
const pino = require('pino');
const pretty = require('pino-pretty');

// Create prettified stream with options
const stream = pretty({
  colorize: true,
  translateTime: 'HH:MM:ss.l',
  ignore: 'hostname',
  messageFormat: '{levelLabel} {msg}'
});

const logger = pino(stream);

logger.info('Application starting');
logger.debug({ reqId: '123', method: 'GET', url: '/api/users' }, 'Incoming request');
logger.error({ err: { type: 'DatabaseError', message: 'Connection timeout' } }, 'Database error');

// Stream with conditional message format
const customStream = pretty({
  colorize: true,
  messageFormat: '{levelLabel} - {if reqId}[{reqId}] {end}{msg}'
});

const customLogger = pino(customStream);
customLogger.info({ reqId: 'abc-123' }, 'Request processed');
// Output: INFO - [abc-123] Request processed
customLogger.info('Background job completed');
// Output: INFO - Background job completed
```

## prettyFactory Function

Factory function for creating a prettifier that accepts log data and returns formatted strings.

```javascript
const { prettyFactory } = require('pino-pretty');

// Create prettifier function
const prettifier = prettyFactory({
  colorize: false,
  translateTime: true,
  levelFirst: false,
  messageKey: 'msg',
  timestampKey: 'time',
  errorProps: 'stack'
});

// Use prettifier on log objects or JSON strings
const logObject = {
  level: 30,
  time: 1522431328992,
  msg: 'hello world',
  pid: 42,
  hostname: 'foo',
  v: 1
};

const formatted = prettifier(logObject);
console.log(formatted);
// Output: [17:35:28.992] INFO (42): hello world

const jsonString = '{"level":50,"time":1522431328992,"msg":"error occurred","err":{"type":"Error","message":"failed"},"pid":42,"hostname":"foo","v":1}';
const formattedError = prettifier(jsonString);
console.log(formattedError);
// Output: [17:35:28.992] ERROR (42): error occurred
//     err: {
//       "type": "Error",
//       "message": "failed"
//     }
```

## Custom Prettifiers

Custom prettifier functions for specific log properties with full control over formatting.

```javascript
const pino = require('pino');
const pretty = require('pino-pretty');

const stream = pretty({
  colorize: true,
  customPrettifiers: {
    // Prettify time field
    time: timestamp => `🕐 ${timestamp}`,

    // Prettify level with access to label and colors
    level: (logLevel, key, log, { label, labelColorized, colors }) => {
      return `[${labelColorized}]`;
    },

    // Prettify hostname
    hostname: (hostname, key, log, { colors }) => {
      return colors.gray(`on ${hostname}`);
    },

    // Prettify custom query property
    query: (value, key, log, { colors }) => {
      return colors.magenta(`SQL: ${value.text} [${value.duration}ms]`);
    },

    // Prettify user objects
    user: (value, key, log, { colors }) => {
      return `${colors.cyan(value.name)} (${value.id})`;
    }
  }
});

const logger = pino(stream);

logger.info({
  query: { text: 'SELECT * FROM users', duration: 45 },
  user: { id: 123, name: 'Alice' }
}, 'Database query executed');
// Output with custom formatting for query and user fields
```

## Message Format Function

Dynamic message formatting using a custom function instead of template strings.

```javascript
const pino = require('pino');
const pretty = require('pino-pretty');

const stream = pretty({
  colorize: true,
  messageFormat: (log, messageKey, levelLabel, { colors }) => {
    // Custom formatting logic
    const baseMessage = log[messageKey];

    if (log.reqId) {
      return `[${colors.yellow(log.reqId)}] ${baseMessage}`;
    }

    if (log.userId) {
      return `${colors.blue(`User ${log.userId}`)} - ${baseMessage}`;
    }

    if (log.err) {
      return `${colors.red('ERROR')} ${baseMessage}: ${log.err.message}`;
    }

    return baseMessage;
  }
});

const logger = pino(stream);

logger.info({ reqId: 'req-789' }, 'Handling HTTP request');
// Output: [17:35:28.992] INFO (42): [req-789] Handling HTTP request

logger.info({ userId: 'user-456' }, 'Action performed');
// Output: [17:35:28.992] INFO (42): User user-456 - Action performed

logger.error({ err: { message: 'Connection timeout' } }, 'Failed to connect');
// Output: [17:35:28.992] ERROR (42): ERROR Failed to connect: Connection timeout
```

## Custom Levels and Colors

Define custom log levels and their corresponding colors.

```javascript
const pino = require('pino');
const pretty = require('pino-pretty');

// Using string format for custom levels and colors
const stream = pretty({
  colorize: true,
  customLevels: 'emergency:80,critical:70,alert:65,info:30,debug:20',
  customColors: 'emergency:bgRed,critical:red,alert:yellow,info:blue,debug:gray',
  useOnlyCustomProps: false // Allow fallback to default levels
});

const logger = pino({
  customLevels: {
    emergency: 80,
    critical: 70,
    alert: 65
  }
}, stream);

logger.emergency('System failure detected');
logger.critical('Database unreachable');
logger.alert('Memory threshold exceeded');
logger.info('Application started');

// Using object format for custom levels and colors
const objectStream = pretty({
  colorize: true,
  customLevels: { emergency: 80, critical: 70 },
  customColors: { emergency: 'bgRed', critical: 'red', default: 'white' },
  useOnlyCustomProps: true // Use only custom properties
});
```

## Colorizer Factory

Create colorizer functions for programmatic color application to log levels and messages.

```javascript
const { colorizerFactory, isColorSupported } = require('pino-pretty');

// Check if colors are supported
if (isColorSupported) {
  console.log('Terminal supports colors');
}

// Create basic colorizer
const colorizer = colorizerFactory(true);

// Colorize level by number
console.log(colorizer(30)); // Returns green "INFO"
console.log(colorizer(50)); // Returns red "ERROR"

// Colorize level by name
console.log(colorizer('info')); // Returns green "INFO"
console.log(colorizer('error')); // Returns red "ERROR"

// Colorize messages
console.log(colorizer.message('This is a log message')); // Returns cyan colored text
console.log(colorizer.greyMessage('This is metadata')); // Returns gray colored text

// Custom colorizer with custom levels
const customColorizer = colorizerFactory(
  true,
  [[80, 'bgRed'], [70, 'red'], [30, 'blue']],
  false // useOnlyCustomProps
);

console.log(customColorizer(80)); // Returns bgRed colored level
console.log(customColorizer(70)); // Returns red colored level

// Custom colorizer with options
const levelLabel = customColorizer(30, {
  customLevels: { 30: 'INFO', 80: 'EMERGENCY' },
  customLevelNames: { info: 30, emergency: 80 }
});

// Access color functions directly
const colors = colorizer.colors;
console.log(colors.red('Error text'));
console.log(colors.blue('Info text'));
console.log(colors.bgYellow('Warning background'));
```

## Build Function with File Output

Build a prettifier stream that writes to files or custom destinations.

```javascript
const pino = require('pino');
const { build } = require('pino-pretty');
const SonicBoom = require('sonic-boom');

// Write to file
const fileStream = build({
  colorize: false,
  destination: './logs/app.log',
  mkdir: true,
  append: true,
  sync: false
});

const fileLogger = pino(fileStream);
fileLogger.info('This will be written to file');

// Write to custom SonicBoom destination
const customDestination = new SonicBoom({
  dest: './logs/custom.log',
  mkdir: true,
  sync: true
});

const customStream = build({
  colorize: false,
  destination: customDestination,
  translateTime: 'yyyy-mm-dd HH:MM:ss.l'
});

const customLogger = pino(customStream);
customLogger.info('Using custom SonicBoom destination');

// Write to stdout with formatting
const stdoutStream = build({
  destination: 1, // stdout
  colorize: true,
  levelFirst: true
});

const stdoutLogger = pino(stdoutStream);
stdoutLogger.info('Pretty printed to console');

// Synchronous mode (required for Jest)
const syncStream = build({
  sync: true,
  colorize: true
});

const syncLogger = pino(syncStream);
syncLogger.info('Synchronous logging');
```

## Advanced Filtering Options

Filter log output by including or ignoring specific properties, including nested properties.

```javascript
const pino = require('pino');
const pretty = require('pino-pretty');

// Ignore specific properties
const ignoreStream = pretty({
  colorize: true,
  ignore: 'pid,hostname,time' // Comma-separated list
});

const ignoreLogger = pino(ignoreStream);
ignoreLogger.info({ requestId: 'abc', userId: 123 }, 'Request processed');
// Output will not include pid, hostname, or time

// Ignore nested properties
const ignoreNestedStream = pretty({
  colorize: true,
  ignore: 'req.headers,res.body,log\\.domain\\.corp/foo' // Escape dots in property names
});

const nestedLogger = pino(ignoreNestedStream);
nestedLogger.info({
  req: { method: 'GET', url: '/api', headers: { authorization: 'secret' } },
  res: { status: 200, body: 'large response' }
}, 'Request completed');
// Output will include req.method and req.url but not req.headers or res.body

// Include only specific properties (overrides ignore)
const includeStream = pretty({
  colorize: true,
  include: 'level,time,msg,reqId,userId' // Only these properties
});

const includeLogger = pino(includeStream);
includeLogger.info({
  reqId: 'req-123',
  userId: 'user-456',
  sessionId: 'sess-789',
  extra: 'data'
}, 'User action');
// Output will only include level, time, msg, reqId, userId (not sessionId or extra)

// Minimum level filtering
const filteredStream = pretty({
  colorize: true,
  minimumLevel: 'warn' // Can be number or string
});

const filteredLogger = pino(filteredStream);
filteredLogger.trace('This will not appear');
filteredLogger.debug('This will not appear');
filteredLogger.info('This will not appear');
filteredLogger.warn('This will appear');
filteredLogger.error('This will appear');
```

## Error Object Handling

Specialized handling for error objects with stack traces and custom error properties.

```javascript
const pino = require('pino');
const pretty = require('pino-pretty');

const stream = pretty({
  colorize: true,
  errorLikeObjectKeys: ['err', 'error', 'exception'], // Keys to treat as errors
  errorProps: 'stack,code,signal,cause', // Error properties to display
  singleLine: false // Errors always multi-line
});

const logger = pino(stream);

// Standard error logging
try {
  throw new Error('Something went wrong');
} catch (err) {
  logger.error({ err }, 'Error caught');
  // Output includes stack trace and error properties
}

// Custom error-like objects
logger.error({
  exception: {
    type: 'ValidationError',
    message: 'Invalid input',
    code: 'ERR_VALIDATION',
    fields: ['email', 'password']
  }
}, 'Validation failed');

// Error with additional context
logger.error({
  err: new Error('Database timeout'),
  query: 'SELECT * FROM users',
  duration: 5000
}, 'Query failed');
// Output includes error with stack, plus query context

// Nested error cause chains (Node.js 16.9+)
const cause = new Error('Connection refused');
const mainError = new Error('Database unavailable', { cause });

logger.error({ err: mainError }, 'Failed to connect');
// Output includes both error and cause with errorProps: 'stack,cause'
```

## Configuration File Usage

Load configuration from external files for reusable settings.

```javascript
// pino-pretty.config.js
module.exports = {
  colorize: true,
  translateTime: 'SYS:yyyy-mm-dd HH:MM:ss.l',
  ignore: 'pid,hostname',
  messageFormat: '{levelLabel} - {if reqId}[{reqId}] {end}{msg}',
  customColors: 'info:blue,warn:yellow,error:red',
  levelFirst: true,
  singleLine: false,
  errorProps: 'stack,code'
};

// .pino-prettyrc (JSON format)
{
  "colorize": true,
  "translateTime": "HH:MM:ss.l",
  "ignore": "hostname",
  "levelFirst": true
}
```

```bash
# CLI automatically looks for .pino-prettyrc in current directory
node app.js | pino-pretty

# Or specify custom config file
node app.js | pino-pretty --config ./custom-config.js
```

```javascript
// Custom transport wrapper for non-serializable options
// pino-pretty-transport.js
module.exports = opts => require('pino-pretty')({
  ...opts,
  messageFormat: (log, messageKey) => {
    // Custom function not serializable in transport options
    const message = log[messageKey];
    if (log.reqId) {
      return `[REQUEST:${log.reqId}] ${message}`;
    }
    return message;
  },
  customPrettifiers: {
    time: timestamp => `🕐 ${timestamp}`,
    query: value => `SQL: ${value.text} (${value.duration}ms)`
  }
});

// main.js
const pino = require('pino');
const logger = pino({
  transport: {
    target: './pino-pretty-transport',
    options: {
      colorize: true
    }
  }
});

logger.info({ reqId: '123' }, 'Request received');
// Output: [17:35:28.992] INFO (42): [REQUEST:123] Request received
```

## Summary

pino-pretty serves as an essential development tool for Node.js applications using Pino or compatible NDJSON loggers. Its primary use cases include local development debugging with colorized output, automated log formatting in development containers, CI/CD pipeline log prettification, and custom log analysis workflows. The tool integrates seamlessly as a Pino transport, CLI utility, or standalone transform stream, making it adaptable to various deployment scenarios from development laptops to containerized environments.

The module excels at balancing simplicity with power through its layered API design. Basic usage requires no configuration for sensible defaults, while advanced scenarios benefit from custom prettifiers, message format functions, dynamic filtering, and specialized error handling. Integration patterns range from simple CLI piping for quick debugging to sophisticated custom transport modules with non-serializable functions for complex formatting requirements. The streaming architecture ensures minimal performance overhead, while the comprehensive option set enables teams to standardize log formatting across projects through shared configuration files.

