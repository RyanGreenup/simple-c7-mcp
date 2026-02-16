# Papa Parse - Fast CSV Parser for JavaScript

Papa Parse is a powerful, fast, and RFC 4180 compliant CSV parser for browser and Node.js environments. It provides comprehensive CSV parsing capabilities with support for local files, remote files over HTTP, streaming large datasets, worker threads for non-blocking parsing, and bidirectional conversion between CSV and JSON formats. The library has zero dependencies and handles complex CSV edge cases including line breaks within fields, properly escaped quotes, auto-detection of delimiters, and dynamic type conversion.

The library is designed for both simple and advanced use cases, offering synchronous parsing for small datasets and asynchronous streaming for large files that would otherwise block the main thread. It supports pause/resume/abort operations, custom delimiters and quote characters, header row processing, preview mode for parsing only the first N rows, and configurable error handling. Papa Parse can process CSV data from strings, local File objects, remote URLs, or Node.js readable streams, making it versatile for various JavaScript environments.

## API Functions and Usage Examples

### Parse CSV String to JSON

Parse CSV data from a string with automatic delimiter detection and header row support.

```javascript
const Papa = require('papaparse');

// Basic parsing with header row
const csvData = `name,age,city
John,30,New York
Jane,25,Los Angeles
Bob,35,Chicago`;

const results = Papa.parse(csvData, {
  header: true,
  dynamicTyping: true,
  skipEmptyLines: true
});

console.log(results.data);
// Output: [
//   { name: 'John', age: 30, city: 'New York' },
//   { name: 'Jane', age: 25, city: 'Los Angeles' },
//   { name: 'Bob', age: 35, city: 'Chicago' }
// ]

console.log(results.meta);
// Output: { delimiter: ',', linebreak: '\n', aborted: false, fields: ['name', 'age', 'city'] }

console.log(results.errors);
// Output: [] (empty if no errors)
```

### Parse CSV File (Browser)

Parse local files selected by users through file input elements in the browser.

```javascript
// HTML: <input type="file" id="fileInput" accept=".csv" />

document.getElementById('fileInput').addEventListener('change', function(e) {
  const file = e.target.files[0];

  Papa.parse(file, {
    header: true,
    dynamicTyping: true,
    skipEmptyLines: 'greedy',
    complete: function(results) {
      console.log('Parsing complete:', results.data);
      console.log('Row count:', results.data.length);
      console.log('Errors:', results.errors);
    },
    error: function(error) {
      console.error('Parse error:', error);
    }
  });
});

// Expected output for a valid CSV file:
// Parsing complete: [{col1: 'value1', col2: 'value2'}, ...]
// Row count: 150
// Errors: []
```

### Parse Remote CSV File (Download)

Download and parse CSV files from remote URLs with streaming support for large files.

```javascript
Papa.parse('https://example.com/data/sales.csv', {
  download: true,
  header: true,
  dynamicTyping: true,
  step: function(row, parser) {
    // Process each row as it arrives
    console.log('Row:', row.data);

    // Pause parsing to handle backpressure
    if (needsSlowdown()) {
      parser.pause();
      setTimeout(() => parser.resume(), 1000);
    }

    // Abort parsing if needed
    if (shouldStop()) {
      parser.abort();
    }
  },
  complete: function(results) {
    console.log('All rows processed');
    console.log('Total errors:', results.errors.length);
  },
  error: function(error) {
    console.error('Download error:', error);
  }
});

// Expected console output during parsing:
// Row: { product: 'Widget A', sales: 150, revenue: 4500 }
// Row: { product: 'Widget B', sales: 200, revenue: 6000 }
// ...
// All rows processed
// Total errors: 0
```

### Stream Large Files with Chunking

Process large CSV files in chunks to avoid memory issues and maintain UI responsiveness.

```javascript
Papa.parse(largeFile, {
  header: true,
  chunkSize: 1024 * 1024 * 5, // 5 MB chunks
  chunk: function(results, parser) {
    console.log('Chunk received with', results.data.length, 'rows');

    // Process chunk data
    results.data.forEach(row => {
      // Insert into database, update UI, etc.
      processRow(row);
    });

    // Handle chunk errors
    if (results.errors.length > 0) {
      console.warn('Chunk errors:', results.errors);
    }

    // Pause if processing is slow
    if (isProcessingSlow()) {
      parser.pause();
      setTimeout(() => parser.resume(), 500);
    }
  },
  complete: function() {
    console.log('File streaming complete');
  }
});

// Expected output:
// Chunk received with 10000 rows
// Chunk received with 10000 rows
// Chunk received with 3247 rows
// File streaming complete
```

### Parse with Worker Threads (Non-Blocking)

Offload CSV parsing to a web worker to prevent blocking the main UI thread.

```javascript
Papa.parse(hugeFile, {
  worker: true,
  header: true,
  dynamicTyping: true,
  step: function(row) {
    // Receives parsed rows from worker thread
    updateProgressBar(row.data);
    displayRow(row.data);
  },
  complete: function(results) {
    console.log('Worker parsing complete');
    console.log('Parsed', results.data.length, 'rows');
    hideLoadingSpinner();
  },
  error: function(error) {
    console.error('Worker error:', error);
  }
});

// Main thread remains responsive
document.getElementById('cancelBtn').addEventListener('click', function() {
  // Parser can be controlled from main thread
  console.log('User cancelled parsing');
});

// Expected behavior: UI stays responsive while parsing occurs in background
```

### Parse Node.js Readable Stream

Process CSV data from Node.js streams such as file streams or HTTP responses.

```javascript
const fs = require('fs');
const Papa = require('papaparse');

const fileStream = fs.createReadStream('./data/large-dataset.csv');

Papa.parse(fileStream, {
  header: true,
  dynamicTyping: true,
  encoding: 'utf8',
  step: function(row) {
    // Process each row as it's read from disk
    console.log('Processing:', row.data);
  },
  complete: function(results) {
    console.log('Stream parsing complete');
    console.log('Errors encountered:', results.errors.length);
  },
  error: function(error) {
    console.error('Stream error:', error);
  }
});

// Expected output:
// Processing: { id: 1, name: 'Alice', score: 95 }
// Processing: { id: 2, name: 'Bob', score: 87 }
// ...
// Stream parsing complete
// Errors encountered: 0
```

### Parse with Node.js Stream Piping

Use Node.js streaming API with pipe for advanced stream processing workflows.

```javascript
const fs = require('fs');
const Papa = require('papaparse');

const inputStream = fs.createReadStream('./input.csv');
const parseStream = Papa.parse(Papa.NODE_STREAM_INPUT, {
  header: true,
  dynamicTyping: true
});

let rowCount = 0;

parseStream.on('data', (row) => {
  rowCount++;
  console.log('Row', rowCount, ':', row);

  // Transform and process data
  if (row.score > 90) {
    console.log('High score:', row.name, row.score);
  }
});

parseStream.on('end', () => {
  console.log('Stream ended. Total rows:', rowCount);
});

parseStream.on('error', (error) => {
  console.error('Stream error:', error);
});

inputStream.pipe(parseStream);

// Expected output:
// Row 1 : { id: 1, name: 'Alice', score: 95 }
// High score: Alice 95
// Row 2 : { id: 2, name: 'Bob', score: 87 }
// ...
// Stream ended. Total rows: 1000
```

### Advanced Configuration Options

Configure parsing behavior with custom delimiters, quotes, transformations, and validation.

```javascript
const results = Papa.parse(csvData, {
  delimiter: '|',              // Custom delimiter (auto-detected if not specified)
  newline: '\n',               // Line break character (auto-detected if not specified)
  quoteChar: '"',              // Quote character
  escapeChar: '"',             // Escape character for quotes
  header: true,                // First row is header
  dynamicTyping: true,         // Auto-convert numbers and booleans
  preview: 100,                // Parse only first 100 rows
  skipEmptyLines: 'greedy',    // Skip empty lines (true, false, or 'greedy')
  comments: '#',               // Treat lines starting with # as comments
  delimitersToGuess: ['|', '\t', ',', ';'], // Delimiters to try when auto-detecting

  // Transform headers
  transformHeader: function(header, index) {
    return header.trim().toLowerCase().replace(/ /g, '_');
  },

  // Transform values
  transform: function(value, field) {
    if (field === 'email') {
      return value.toLowerCase();
    }
    return value;
  },

  // Custom dynamic typing per field
  dynamicTyping: function(field) {
    return field === 'age' || field === 'score';
  },

  // Before first chunk is parsed (streaming only)
  beforeFirstChunk: function(chunk) {
    // Modify chunk before parsing (e.g., remove BOM)
    return chunk.replace(/^\uFEFF/, '');
  },

  // Skip first N lines (useful for files with metadata)
  skipFirstNLines: 2
});

console.log(results.data);
// Output: Transformed data with custom processing applied

console.log(results.meta.delimiter);
// Output: '|'
```

### Convert JSON to CSV (Unparse)

Convert JavaScript objects or arrays back to CSV format with configurable output options.

```javascript
const Papa = require('papaparse');

// Array of objects
const data = [
  { name: 'John Doe', age: 30, city: 'New York', email: 'john@example.com' },
  { name: 'Jane Smith', age: 25, city: 'Los Angeles', email: 'jane@example.com' },
  { name: 'Bob Johnson', age: 35, city: 'Chicago', email: 'bob@example.com' }
];

const csv = Papa.unparse(data, {
  quotes: false,               // Don't quote fields (true to quote all)
  quoteChar: '"',              // Quote character
  escapeChar: '"',             // Escape character
  delimiter: ',',              // Field delimiter
  header: true,                // Include header row
  newline: '\r\n',             // Line break
  skipEmptyLines: false,       // Skip empty lines
  columns: ['name', 'age', 'city']  // Only include these columns
});

console.log(csv);
// Output:
// name,age,city
// John Doe,30,New York
// Jane Smith,25,Los Angeles
// Bob Johnson,35,Chicago

// Save to file in Node.js
const fs = require('fs');
fs.writeFileSync('./output.csv', csv, 'utf8');
```

### Unparse Arrays of Arrays

Convert two-dimensional arrays to CSV format, useful when data doesn't have field names.

```javascript
const data = [
  ['Name', 'Age', 'City'],
  ['John', 30, 'New York'],
  ['Jane', 25, 'Los Angeles'],
  ['Bob', 35, 'Chicago']
];

const csv = Papa.unparse(data, {
  delimiter: ',',
  newline: '\n'
});

console.log(csv);
// Output:
// Name,Age,City
// John,30,New York
// Jane,25,Los Angeles
// Bob,35,Chicago
```

### Unparse with Custom Quoting Rules

Apply selective quoting based on field content or position to minimize file size.

```javascript
const data = [
  { name: 'John, Jr.', description: 'Product "Alpha"', price: 29.99 },
  { name: 'Jane Doe', description: 'Standard item', price: 19.99 }
];

const csv = Papa.unparse(data, {
  // Quote only fields that need it (contain delimiter, newline, or quotes)
  quotes: false,

  // Or quote specific columns
  quotes: [true, true, false],  // Quote first two columns only

  // Or use a function for dynamic quoting
  quotes: function(value, columnIndex) {
    // Quote if value contains comma or quotes
    return typeof value === 'string' && /[,"]/.test(value);
  },

  delimiter: ',',
  header: true
});

console.log(csv);
// Output:
// name,description,price
// "John, Jr.","Product ""Alpha""",29.99
// Jane Doe,Standard item,19.99
```

### Unparse with Formula Escaping

Prevent CSV injection attacks by escaping cells that start with formula characters.

```javascript
const potentiallyDangerousData = [
  { name: 'Safe Data', formula: 'Normal text' },
  { name: '=MALICIOUS()', formula: '+1+1' },
  { name: '@LOOKUP', formula: '-5*3' },
  { name: 'Regular', formula: '\tTabbed' }
];

const csv = Papa.unparse(potentiallyDangerousData, {
  header: true,
  escapeFormulae: true,  // Escape =, +, -, @, tab, and carriage return at start
  // Or use custom regex: escapeFormulae: /^[=+\-@\t\r].*/
});

console.log(csv);
// Output:
// name,formula
// Safe Data,Normal text
// '=MALICIOUS(),'+1+1
// '@LOOKUP,'-5*3
// Regular,'	Tabbed

// Formulas are prefixed with single quote to prevent execution in Excel/LibreOffice
```

### Error Handling and Validation

Handle parsing errors gracefully with detailed error information for debugging and validation.

```javascript
const malformedCsv = `name,age,city
John,30,New York
Jane,25,"Los Angeles
Bob,35,Chicago,"extra"`;

const results = Papa.parse(malformedCsv, {
  header: true,
  skipEmptyLines: true,
  error: function(error, file) {
    console.error('Parse error occurred:', error);
  }
});

console.log('Data:', results.data);
// Output: Data with available parsed rows

console.log('Errors:', results.errors);
// Output: [
//   {
//     type: 'Quotes',
//     code: 'MissingQuotes',
//     message: 'Quoted field unterminated',
//     row: 2,
//     index: 23
//   },
//   {
//     type: 'FieldMismatch',
//     code: 'TooManyFields',
//     message: 'Too many fields: expected 3 fields but parsed 4',
//     row: 3
//   }
// ]

console.log('Meta:', results.meta);
// Output: { delimiter: ',', linebreak: '\n', aborted: false, fields: [...] }

// Check if parsing was successful
if (results.errors.length === 0) {
  console.log('Parsing successful!');
  processData(results.data);
} else {
  console.warn('Parsing completed with errors');
  displayErrors(results.errors);
}
```

### Parse with jQuery Integration

Use Papa Parse with jQuery for convenient file input handling in legacy applications.

```javascript
// HTML: <input type="file" id="csvFile" multiple />

$('#csvFile').parse({
  config: {
    header: true,
    dynamicTyping: true,
    skipEmptyLines: true,
    complete: function(results, file) {
      console.log('Parsed file:', file.name);
      console.log('Data:', results.data);
    }
  },
  before: function(file, inputElem) {
    console.log('Parsing file:', file.name);
    // Return { action: 'abort', reason: 'File too large' } to abort
    // Return { action: 'skip' } to skip this file
    // Return { config: {...} } to modify config for this file
  },
  error: function(error, file) {
    console.error('Error parsing', file.name, ':', error);
  },
  complete: function() {
    console.log('All files parsed');
  }
});

// Expected output when selecting 2 files:
// Parsing file: data1.csv
// Parsed file: data1.csv
// Data: [{...}, {...}, ...]
// Parsing file: data2.csv
// Parsed file: data2.csv
// Data: [{...}, {...}, ...]
// All files parsed
```

### Auto-Detect Delimiter

Let Papa Parse automatically detect the delimiter from common options.

```javascript
const tsvData = `name\tage\tcity
John\t30\tNew York
Jane\t25\tLos Angeles`;

const results = Papa.parse(tsvData, {
  header: true,
  // delimiter: undefined (or omit) to auto-detect
  delimitersToGuess: ['\t', ',', '|', ';']
});

console.log('Detected delimiter:', results.meta.delimiter);
// Output: Detected delimiter: 	 (tab character)

console.log('Data:', results.data);
// Output: [
//   { name: 'John', age: '30', city: 'New York' },
//   { name: 'Jane', age: '25', city: 'Los Angeles' }
// ]

// Works with pipe-delimited data too
const pipeData = `name|age|city
John|30|New York`;

const pipeResults = Papa.parse(pipeData, { header: true });
console.log('Detected delimiter:', pipeResults.meta.delimiter);
// Output: Detected delimiter: |
```

### Pause, Resume, and Abort Parsing

Control parsing flow dynamically for rate limiting, user interactions, or conditional processing.

```javascript
let rowsProcessed = 0;
let parser;

Papa.parse(largeFile, {
  header: true,
  step: function(row, parserHandle) {
    parser = parserHandle;
    rowsProcessed++;

    console.log('Processing row', rowsProcessed, ':', row.data);

    // Pause after every 100 rows to update UI
    if (rowsProcessed % 100 === 0) {
      parser.pause();

      updateProgressUI(rowsProcessed);

      // Resume after a short delay
      setTimeout(() => {
        console.log('Resuming...');
        parser.resume();
      }, 100);
    }

    // Abort if user condition is met
    if (row.data.status === 'STOP' || rowsProcessed > 1000) {
      console.log('Aborting parse at row', rowsProcessed);
      parser.abort();
    }
  },
  complete: function(results) {
    console.log('Parsing complete. Processed', rowsProcessed, 'rows');
    console.log('Aborted:', results.meta.aborted);
  }
});

// User interaction
document.getElementById('pauseBtn').addEventListener('click', () => {
  if (parser) parser.pause();
});

document.getElementById('resumeBtn').addEventListener('click', () => {
  if (parser) parser.resume();
});

document.getElementById('cancelBtn').addEventListener('click', () => {
  if (parser) parser.abort();
});
```

### Handle Duplicate Headers

Papa Parse automatically renames duplicate headers to ensure unique field names.

```javascript
const csvWithDuplicates = `name,age,name,city,age
John,30,Smith,New York,30
Jane,25,Doe,Los Angeles,25`;

const results = Papa.parse(csvWithDuplicates, {
  header: true
});

console.log('Fields:', results.meta.fields);
// Output: Fields: ['name', 'age', 'name_1', 'city', 'age_1']

console.log('Renamed headers:', results.meta.renamedHeaders);
// Output: { 'name_1': 'name', 'age_1': 'age' }

console.log('Data:', results.data);
// Output: [
//   { name: 'John', age: '30', name_1: 'Smith', city: 'New York', age_1: '30' },
//   { name: 'Jane', age: '25', name_1: 'Doe', city: 'Los Angeles', age_1: '25' }
// ]

// Console warning: "Duplicate headers found and renamed."
```

## Summary and Integration Patterns

Papa Parse is the go-to solution for CSV processing in JavaScript applications, whether you're building web applications, Node.js services, or data processing pipelines. Common use cases include importing user data from spreadsheet exports, processing financial transaction logs, analyzing large datasets from scientific instruments, generating CSV reports for download, migrating data between systems, and building data transformation ETL pipelines. The library's streaming capabilities make it particularly well-suited for handling datasets that exceed available memory, while its worker thread support ensures smooth user experiences even when processing millions of rows.

Integration patterns vary by environment and use case. In browser applications, combine Papa Parse with file input elements for user uploads, use worker threads for parsing large files without blocking the UI, and stream data to IndexedDB or backend APIs for persistent storage. In Node.js environments, pipe streams through Papa Parse for memory-efficient processing, integrate with databases by parsing CSV imports in chunks, use with Express.js middleware for handling CSV uploads, or build CLI tools for batch CSV processing. The library's flexible configuration options, robust error handling, comprehensive support for CSV edge cases, and ability to handle both small and massive datasets make it an essential tool for any JavaScript project dealing with tabular data.
