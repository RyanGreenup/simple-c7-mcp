### React: Basic Virtualized List Setup

Source: https://tanstack.com/virtual/latest/docs/framework/react/examples/padding

Demonstrates setting up a basic virtualized list in React using TanStack Virtual. It requires installing the `@tanstack/react-virtual` package. The example shows how to use the `useVirtual` hook to manage the virtualizer and render items.

```jsx
import React from 'react';
import { useVirtual } from '@tanstack/react-virtual';

function App() {
  const parentRef = React.useRef();
  const rowVirtualizer = useVirtual({
    size: 10000,
    parentRef,
    estimateSize: React.useCallback(index => 35, []),
  });

  return (
    <div
      ref={parentRef}
      style={{ height: '500px', width: '100%', overflow: 'auto' }}
    >
      <div
        style={{
          height: `${rowVirtualizer.totalSize}px`,
          width: '100%',
          position: 'relative',
        }}
      >
        {rowVirtualizer.virtualItems.map(virtualRow => (
          <div
            key={virtualRow.key}
            style={{
              position: 'absolute',
              top: 0,
              left: 0,
              width: '100%',
              height: `${virtualRow.size}px`,
              transform: `translateY(${virtualRow.start}px)`,
            }}
          >
            Row ${virtualRow.index}
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
```

--------------------------------

### React Root Rendering Setup

Source: https://tanstack.com/virtual/latest/docs/framework/react/examples/dynamic

Configures the React application's entry point. It finds the root DOM element, creates a React root using `createRoot`, and renders the `App` component within `StrictMode` for development-time checks. This is the standard setup for a React application.

```javascript
const container = document.getElementById('root')!
const root = createRoot(container)
const { StrictMode } = React

root.render(
  <StrictMode>
    <App />
  </StrictMode>,
)
```

--------------------------------

### React Root Rendering Setup (React)

Source: https://tanstack.com/virtual/latest/docs/framework/react/examples/dynamic

Sets up the React root using `createRoot` from `react-dom/client` and renders the main `App` component within `StrictMode`. This is the standard entry point for a React application.

```jsx
const container = document.getElementById('root')!
const root = createRoot(container)
const { StrictMode } = React

root.render(
  <StrictMode>
    <App />
  </StrictMode>,
)
```
```

--------------------------------

### React App Initialization with QueryClientProvider

Source: https://tanstack.com/virtual/latest/docs/framework/react/examples/infinite-scroll

This snippet shows the basic setup for a React application using React Query's QueryClientProvider. It wraps the main App component to provide the React Query client context, essential for managing query states and caching.

```javascript
ReactDOM.render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      <App />
    </QueryClientProvider>
  </React.StrictMode>,
  document.getElementById('root'),
)
```

--------------------------------

### App Component for Routing Virtualizer Examples (React)

Source: https://tanstack.com/virtual/latest/docs/framework/react/examples/dynamic

The main App component that handles routing to different virtualization examples (List, Column, Grid, Experimental). It uses React's `location.pathname` to determine which component to render and includes a development mode notice.

```jsx
function App() {
  const pathname = location.pathname
  return (
    <div>
      <p>
        These components are using <strong>dynamic</strong> sizes. This means
        that each element's exact dimensions are unknown when rendered. An
        estimated dimension is used as the initial measurement, then this
        measurement is readjusted on the fly as each element is rendered.
      </p>
      <nav>
        <ul>
          <li>
            <a href="/">List</a>
          </li>
          <li>
            <a href="/columns">Column</a>
          </li>
          <li>
            <a href="/grid">Grid</a>
          </li>
          <li>
            <a href="/experimental">Experimental</a>
          </li>
        </ul>
      </nav>
      {(() => {
        switch (pathname) {
          case '/':
            return <RowVirtualizerDynamic />
          case '/columns':
            return <ColumnVirtualizerDynamic />
          case '/grid': {
            const columns = generateColumns(30)
            const data = generateData(columns)
            return <GridVirtualizerDynamic columns={columns} data={data} />
          }
          case '/experimental':
            return <RowVirtualizerExperimental />
          default:
            return <div>Not found</div>
        }
      })()}
      <br />
      <br />
      {process.env.NODE_ENV === 'development' ? (
        <p>
          <strong>Notice:</strong> You are currently running React in
          development mode. Rendering performance will be slightly degraded
          until this application is built for production.
        </p>
      ) : null}
    </div>
  )
}

const container = document.getElementById('root')!
const root = createRoot(container)
const { StrictMode } = React

root.render(
  <StrictMode>
    <App />
  </StrictMode>,
)
```
```

--------------------------------

### React App Initialization with TanStack Virtual (React)

Source: https://tanstack.com/virtual/latest/docs/framework/react/examples/variable

Standard React application setup using `ReactDOM.render` to mount the main `App` component. It includes necessary imports for React, ReactDOM, and TanStack Virtual, along with basic CSS styling.

```jsx
import React from 'react'
import ReactDOM from 'react-dom'

import './index.css'

import { useVirtualizer } from '@tanstack/react-virtual'

const rows = new Array(10000)
  .fill(true)
  .map(() => 25 + Math.round(Math.random() * 100))

const columns = new Array(10000)
  .fill(true)
  .map(() => 75 + Math.round(Math.random() * 100))

function App() {
  return (
    <div>
      <p>
        These components are using <strong>variable</strong> sizes. This means
        that each element has a unique, but knowable dimension at render time.
      </p>
      <br />
      <br />

      <h3>Rows</h3>
      <RowVirtualizerVariable rows={rows} />
      <br />
    </div>
  )
}

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root'),
)
```

--------------------------------

### React Virtualizer for Grid with Variable Sizes

Source: https://tanstack.com/virtual/latest/docs/framework/react/examples/variable

Demonstrates a virtualized grid where both row and column sizes can vary. This example uses nested loops to render cells and applies dynamic styling for positioning and sizing based on virtual item data. It requires React and TanStack Virtual.

```jsx
function GridVirtualizerVariable() {
  const parentRef = React.useRef<HTMLDivElement>(null)

  const rowVirtualizer = useVirtualizer({
    count: rows.length,
    getScrollElement: () => parentRef.current,
    estimateSize: (i) => rows[i],
    overscan: 5,
  })

  const columnVirtualizer = useVirtualizer({
    horizontal: true,
    count: columns.length,
    getScrollElement: () => parentRef.current,
    estimateSize: (i) => columns[i],
    overscan: 5,
  })

  return (
    <>
      <div
        ref={parentRef}
        className="List"
        style={{
          height: `400px`,
          width: `400px`,
          overflow: 'auto',
        }}
      >
        <div
          style={{
            height: `${rowVirtualizer.getTotalSize()}px`,
            width: `${columnVirtualizer.getTotalSize()}px`,
            position: 'relative',
          }}
        >
          {rowVirtualizer.getVirtualItems().map((virtualRow) => (
            <React.Fragment key={virtualRow.index}>
              {columnVirtualizer.getVirtualItems().map((virtualColumn) => (
                <div
                  key={virtualColumn.index}
                  className="ListItem"
                  style={{
                    position: 'absolute',
                    top: 0,
                    left: 0,
                    width: `${columns[virtualColumn.index]}px`,
                    height: `${rows[virtualRow.index]}px`,
                    transform: `translateX(${virtualColumn.start}px) translateY(${virtualRow.start}px)`,
                  }}
                >
                  Cell {virtualRow.index}, {virtualColumn.index}
                </div>
              ))}
            </React.Fragment>
          ))}
        </div>
      </div>
    </>
  )
}
```

--------------------------------

### React App Routing and Rendering

Source: https://tanstack.com/virtual/latest/docs/framework/react/examples/dynamic

The main `App` component handles routing for different virtualizer examples based on the URL pathname. It uses a switch statement to conditionally render `RowVirtualizerDynamic`, `ColumnVirtualizerDynamic`, `GridVirtualizerDynamic`, or `RowVirtualizerExperimental`. It also includes a development mode notice.

```javascript
function App() {
  const pathname = location.pathname
  return (
    <div>
      <p>
        These components are using <strong>dynamic</strong> sizes. This means
        that each element's exact dimensions are unknown when rendered. An
        estimated dimension is used as the initial measurement, then this
        measurement is readjusted on the fly as each element is rendered.
      </p>
      <nav>
        <ul>
          <li>
            <a href="/">List</a>
          </li>
          <li>
            <a href="/columns">Column</a>
          </li>
          <li>
            <a href="/grid">Grid</a>
          </li>
          <li>
            <a href="/experimental">Experimental</a>
          </li>
        </ul>
      </nav>
      {(() => {
        switch (pathname) {
          case '/':
            return <RowVirtualizerDynamic />
          case '/columns':
            return <ColumnVirtualizerDynamic />
          case '/grid': {
            const columns = generateColumns(30)
            const data = generateData(columns)
            return <GridVirtualizerDynamic columns={columns} data={data} />
          }
          case '/experimental':
            return <RowVirtualizerExperimental />
          default:
            return <div>Not found</div>
        }
      })()}
      <br />
      <br />
      {process.env.NODE_ENV === 'development' ? (
        <p>
          <strong>Notice:</strong> You are currently running React in
          development mode. Rendering performance will be slightly degraded
          until this application is built for production.
        </p>
      ) : null}
    </div>
  )
}
```

--------------------------------

### React App Initialization

Source: https://tanstack.com/virtual/latest/docs/framework/react/examples/table

Initializes the React application and renders the main App component within a StrictMode context. It targets the 'root' element in the HTML and uses createRoot for concurrent rendering.

```javascript
const container = document.getElementById('root')
const root = createRoot(container!)
const { StrictMode } = React

root.render(
  <StrictMode>
    <App />
  </StrictMode>,
)
```

--------------------------------

### React Column Virtualizer with Dynamic Sizes

Source: https://tanstack.com/virtual/latest/docs/framework/react/examples/padding

Implements a horizontal virtualizer for columns where each column can have a dynamic width. It uses `useVirtualizer` hook from TanStack Virtual to efficiently render only the visible columns. The `estimateSize` and `columns` array determine the width of each column.

```jsx
function ColumnVirtualizerDynamic({ columns }: { columns: Array<number> }) {
  const parentRef = React.useRef<HTMLDivElement>(null)

  const columnVirtualizer = useVirtualizer({
    horizontal: true,
    count: columns.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 50,
    paddingStart: 100,
    paddingEnd: 100,
  })

  return (
    <>
      <div
        ref={parentRef}
        className="List"
        style={{
          width: `400px`,
          height: `100px`,
          overflow: 'auto',
        }}>
        <div
          style={{
            width: `${columnVirtualizer.getTotalSize()}px`,
            height: '100%',
            position: 'relative',
          }}>
          {columnVirtualizer.getVirtualItems().map((virtualColumn) => (
            <div
              key={virtualColumn.key}
              data-index={virtualColumn.index}
              ref={columnVirtualizer.measureElement}
              className={
                virtualColumn.index % 2 ? 'ListItemOdd' : 'ListItemEven'
              }
              style={{
                position: 'absolute',
                top: 0,
                left: 0,
                height: '100%',
                width: `${columns[virtualColumn.index]}px`,
                transform: `translateX(${virtualColumn.start}px)`,
              }}>
              Column {virtualColumn.index}
            </div>
          ))}
        </div>
      </div>
    </>
  )
}
```

--------------------------------

### React Virtualized List Component

Source: https://tanstack.com/virtual/latest/docs/framework/react/examples/sticky

Implements a virtualized list using TanStack Virtual in React. It calculates total size, virtual items, and handles sticky positioning for headers or fixed elements. Dependencies include React and TanStack Virtual.

```jsx
import React, { useRef } from 'react';
import { useVirtualizer } from '@tanstack/react-virtual';

const App = ({ rows }) => {
  const parentRef = useRef();

  const rowVirtualizer = useVirtualizer({
    count: rows.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 35,
    overscan: 5,
  });

  const stickyIndexes = [0]; // Example: index 0 is sticky

  const isSticky = (index) => stickyIndexes.includes(index);
  const isActiveSticky = (index) => isSticky(index);

  return (
    <div>
      <div
        ref={parentRef}
        className="List"
        style={{
          height: `300px`,
          width: `400px`,
          overflow: 'auto',
        }}
      >
        <div
          style={{
            height: `${rowVirtualizer.getTotalSize()}px`,
            width: '100%',
            position: 'relative',
          }}
        >
          {rowVirtualizer.getVirtualItems().map((virtualRow) => (
            <div
              key={virtualRow.index}
              className={'ListItem'}
              style={{
                ...(isSticky(virtualRow.index)
                  ? {
                      background: '#fff',
                      borderBottom: '1px solid #ddd',
                      zIndex: 1,
                    }
                  : {}),
                ...(isActiveSticky(virtualRow.index)
                  ? {
                      position: 'sticky',
                    }
                  : {
                      position: 'absolute',
                      transform: `translateY(${virtualRow.start}px)`,
                    }),
                top: 0,
                left: 0,
                width: '100%',
                height: `${virtualRow.size}px`,
              }}
            >
              {rows[virtualRow.index]}
            </div>
          ))}
        </div>
      </div>
      {process.env.NODE_ENV === 'development' ? (
        <p>
          <strong>Notice:</strong> You are currently running React in
          development mode. Rendering performance will be slightly degraded
          until this application is built for production.
        </p>
      ) : null}
    </div>
  );
};

// ReactDOM.render(
//   <React.StrictMode>
//     <App rows={Array.from({ length: 1000 }).map((_, i) => `Row ${i + 1}`)} />
//   </React.StrictMode>,
//   document.getElementById('root'),
// );

```

--------------------------------

### Grid Virtualization with Dynamic Row and Column Sizing (React)

Source: https://tanstack.com/virtual/latest/docs/framework/react/examples/dynamic

Renders a virtualized grid with both dynamic row and column sizing. It utilizes `useWindowVirtualizer` for rows and `useVirtualizer` for columns, managing scroll offsets and element measurements for efficient rendering of large datasets.

```jsx
function GridVirtualizerDynamic({
  columns,
  data,
}: { data: Array<Array<string>>
  columns: Array<Column>
}) {
  const parentRef = React.useRef<HTMLDivElement | null>(null)

  const parentOffsetRef = React.useRef(0)

  React.useLayoutEffect(() => {
    parentOffsetRef.current = parentRef.current?.offsetTop ?? 0
  }, [])

  const getColumnWidth = (index: number) => columns[index].width

  const virtualizer = useWindowVirtualizer({
    count: data.length,
    estimateSize: () => 350,
    overscan: 5,
    scrollMargin: parentOffsetRef.current,
  })

  const columnVirtualizer = useVirtualizer({
    horizontal: true,
    count: columns.length,
    getScrollElement: () => parentRef.current,
    estimateSize: getColumnWidth,
    overscan: 5,
  })
  const columnItems = columnVirtualizer.getVirtualItems()
  const [before, after] =
    columnItems.length > 0
      ? [
          columnItems[0].start,
          columnVirtualizer.getTotalSize() -
            columnItems[columnItems.length - 1].end,
        ]
      : [0, 0]

  return (
    <div
      ref={parentRef}
      style={{ overflowY: 'auto', border: '1px solid #c8c8c8' }}
    >
      <div
        style={{
          height: virtualizer.getTotalSize(),
          position: 'relative',
        }}
      >
        {virtualizer.getVirtualItems().map((row) => {
          return (
            <div
              key={row.key}
              data-index={row.index}
              ref={virtualizer.measureElement}
              style={{
                position: 'absolute',
                top: 0,
                left: 0,
                transform: `translateY(${row.start - virtualizer.options.scrollMargin}px)`,
                display: 'flex',
              }}
            >
              <div style={{ width: `${before}px` }} />
              {columnItems.map((column) => {
                return (
                  <div
                    key={column.key}
                    style={{
                      minHeight: row.index === 0 ? 50 : row.size,
                      width: getColumnWidth(column.index),
                      borderBottom: '1px solid #c8c8c8',
                      borderRight: '1px solid #c8c8c8',
                      padding: '7px 12px',
                    }}
                  >
                    {row.index === 0 ? (
                      <div>{columns[column.index].name}</div>
                    ) : (
                      <div>{data[row.index][column.index]}</div>
                    )}
                  </div>
                )
              })}
              <div style={{ width: `${after}px` }} />
            </div>
          )
        })}
      </div>
    </div>
  )
}
```

--------------------------------

### React Grid Virtualizer with Dynamic Row and Column Sizes

Source: https://tanstack.com/virtual/latest/docs/framework/react/examples/padding

Implements a virtualized grid that supports both dynamic row and column heights/widths. It uses two `useVirtualizer` instances, one for rows and one for columns, to manage virtualization in both dimensions. This allows for efficient rendering of large grids with varying cell dimensions.

```jsx
function GridVirtualizerDynamic({
  rows,
  columns,
}: { rows: Array<number>
  columns: Array<number> }) {
  const parentRef = React.useRef<HTMLDivElement>(null)

  const rowVirtualizer = useVirtualizer({
    count: rows.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 50,
    paddingStart: 200,
    paddingEnd: 200,
    indexAttribute: 'data-row-index',
  })

  const columnVirtualizer = useVirtualizer({
    horizontal: true,
    count: columns.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 50,
    paddingStart: 200,
    paddingEnd: 200,
    indexAttribute: 'data-column-index',
  })

  const [show, setShow] = React.useState(true)

  const halfWay = Math.floor(rows.length / 2)

  return (
    <>
      <button onClick={() => setShow((old) => !old)}>Toggle</button>
      <button onClick={() => rowVirtualizer.scrollToIndex(halfWay)}>
        Scroll to index {halfWay}
      </button>
      <button onClick={() => rowVirtualizer.scrollToIndex(rows.length - 1)}>
        Scroll to index {rows.length - 1}
      </button>
      {show ? (
        <div
          ref={parentRef}
          className="List"
          style={{
            height: `400px`,
            width: `500px`,
            overflow: 'auto',
          }}>
          <div
            style={{
              height: `${rowVirtualizer.getTotalSize()}px`,
              width: `${columnVirtualizer.getTotalSize()}px`,
              position: 'relative',
            }}>
            {rowVirtualizer.getVirtualItems().map((virtualRow) => (
              <React.Fragment key={virtualRow.key}>
                {columnVirtualizer.getVirtualItems().map((virtualColumn) => (
                  <div
                    key={virtualColumn.key}
                    data-row-index={virtualRow.index}
                    data-column-index={virtualColumn.index}
                    ref={(el) => {
                      rowVirtualizer.measureElement(el)
                      columnVirtualizer.measureElement(el)
                    }}
                    className={
                      virtualColumn.index % 2
                        ? virtualRow.index % 2 === 0
                          ? 'ListItemOdd'
                          : 'ListItemEven'
                        : virtualRow.index % 2
                          ? 'ListItemOdd'
                          : 'ListItemEven'
                    }
                    style={{
                      position: 'absolute',
                      top: 0,
                      left: 0,
                      width: `${columns[virtualColumn.index]}px`,
                      height: `${rows[virtualRow.index]}px`,
                      transform: `translateX(${virtualColumn.start}px) translateY(${virtualRow.start}px)`,
                    }}>
                    Cell {virtualRow.index}, {virtualColumn.index}
                  </div>
                ))}
              </React.Fragment>
            ))}
          </div>
        </div>
      ) : null}
      <br />
      <br />
      {process.env.NODE_ENV === 'development' ? (
        <p>
          <strong>Notice:</strong> You are currently running React in
          development mode. Rendering performance will be slightly degraded
          until this application is built for production.
        </p>
      ) : null}
    </>
  )
}

```

--------------------------------

### React Grid Virtualizer: Window Scrolling with `useWindowVirtualizer`

Source: https://tanstack.com/virtual/latest/docs/framework/react/examples/dynamic

Demonstrates grid virtualization using `useWindowVirtualizer`, which optimizes scrolling by leveraging the browser window as the scrollable element. This is useful for large grids where the entire container doesn't need to be the scrollable element. It calculates column widths dynamically.

```tsx
interface Column {
  key: string
  name: string
  width: number
}

function GridVirtualizerDynamic({
  columns,
  data,
}: { 
  data: Array<Array<string>>
  columns: Array<Column>
}) {
  const parentRef = React.useRef<HTMLDivElement | null>(null)

  const parentOffsetRef = React.useRef(0)

  React.useLayoutEffect(() => {
    parentOffsetRef.current = parentRef.current?.offsetTop ?? 0
  }, [])

  const getColumnWidth = (index: number) => columns[index].width

  const virtualizer = useWindowVirtualizer({

```

--------------------------------

### Horizontal Virtualization with Dynamic Column Sizing (React)

Source: https://tanstack.com/virtual/latest/docs/framework/react/examples/dynamic

Implements horizontal virtualization for columns, allowing for dynamic sizing of each column. It uses `useVirtualizer` with `horizontal: true` to manage the scrollable container and renders virtualized columns based on their estimated size.

```jsx
function ColumnVirtualizerDynamic() {
  const parentRef = React.useRef<HTMLDivElement | null>(null)

  const virtualizer = useVirtualizer({
    horizontal: true,
    count: sentences.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 45,
  })

  return (
    <>
      <div
        ref={parentRef}
        className="List"
        style={{ width: 400, height: 400, overflowY: 'auto' }}
      >
        <div
          style={{
            width: virtualizer.getTotalSize(),
            height: '100%',
            position: 'relative',
          }}
        >
          {virtualizer.getVirtualItems().map((virtualColumn) => (
            <div
              key={virtualColumn.key}
              data-index={virtualColumn.index}
              ref={virtualizer.measureElement}
              className={
                virtualColumn.index % 2 ? 'ListItemOdd' : 'ListItemEven'
              }
              style={{
                position: 'absolute',
                top: 0,
                left: 0,
                height: '100%',
                transform: `translateX(${virtualColumn.start}px)`,
              }}
            >
              <div style={{ width: sentences[virtualColumn.index].length }}>
                <div>Column {virtualColumn.index}</div>
                <div>{sentences[virtualColumn.index]}</div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </>
  )
}
```

--------------------------------

### Render Row Virtualizer with Dynamic Sizing (React)

Source: https://tanstack.com/virtual/latest/docs/framework/react/examples/dynamic

Renders a virtualized list of rows where each row's size is estimated and then measured dynamically. It uses `useVirtualizer` hook from TanStack Virtual and includes controls for scrolling and toggling the virtualizer.

```jsx
import * as React from 'react'
import { createRoot } from 'react-dom/client'
import { faker } from '@faker-js/faker'

import { useVirtualizer, useWindowVirtualizer } from '@tanstack/react-virtual'

import './index.css'

const randomNumber = (min, max) =>
  faker.number.int({ min, max })

const sentences = new Array(10000)
  .fill(true)
  .map(() => faker.lorem.sentence(randomNumber(20, 70)))

function RowVirtualizerDynamic() {
  const parentRef = React.useRef(null)

  const [enabled, setEnabled] = React.useState(true)

  const count = sentences.length
  const virtualizer = useVirtualizer({
    count,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 45,
    enabled,
  })

  const items = virtualizer.getVirtualItems()

  return (
    <div>
      <button
        onClick={() => {
          virtualizer.scrollToIndex(0)
        }}
      >
        scroll to the top
      </button>
      <span style={{ padding: '0 4px' }} />
      <button
        onClick={() => {
          virtualizer.scrollToIndex(count / 2)
        }}
      >
        scroll to the middle
      </button>
      <span style={{ padding: '0 4px' }} />
      <button
        onClick={() => {
          virtualizer.scrollToIndex(count - 1)
        }}
      >
        scroll to the end
      </button>
      <span style={{ padding: '0 4px' }} />
      <button
        onClick={() => {
          setEnabled((prev) => !prev)
        }}
      >
        turn {enabled ? 'off' : 'on'} virtualizer
      </button>
      <hr />
      <div
        ref={parentRef}
        className="List"
        style={{
          height: 400,
          width: 400,
          overflowY: 'auto',
          contain: 'strict',
          overflowAnchor: 'none',
        }}
      >
        <div
          style={{
            height: virtualizer.getTotalSize(),
            width: '100%',
            position: 'relative',
          }}
        >
          <div
            style={{
              position: 'absolute',
              top: 0,
              left: 0,
              width: '100%',
              transform: `translateY(${items[0]?.start ?? 0}px)`,
            }}
          >
            {items.map((virtualRow) => (
              <div
                key={virtualRow.key}
                data-index={virtualRow.index}
                ref={virtualizer.measureElement}
                className={
                  virtualRow.index % 2 ? 'ListItemOdd' : 'ListItemEven'
                }
              >
                <div style={{ padding: '10px 0' }}>
                  <div>Row {virtualRow.index}</div>
                  <div>{sentences[virtualRow.index]}</div>

```

--------------------------------

### React Dynamic Row Virtualization with TanStack Virtualizer

Source: https://tanstack.com/virtual/latest/docs/framework/react/examples/padding

Implements a virtualized list of rows where each row has a dynamic height. It uses `useVirtualizer` with `estimateSize` and padding to efficiently render a large number of rows. The `measureElement` function is used to dynamically adjust element sizes.

```tsx
import React from 'react'
import ReactDOM from 'react-dom'

import './index.css'

import { useVirtualizer } from '@tanstack/react-virtual'

const rows = new Array(10000)
  .fill(true)
  .map(() => 25 + Math.round(Math.random() * 100))

const columns = new Array(10000)
  .fill(true)
  .map(() => 75 + Math.round(Math.random() * 100))

function App() {
  return (
    <div>
      <p>
        These components are using <strong>dynamic</strong> sizes. This means
        that each element's exact dimensions are unknown when rendered. An
        estimated dimension is used as the initial measurement, then this
        measurement is readjusted on the fly as each element is rendered.
      </p>
      <br />
      <br />

      <h3>Rows</h3>
      <RowVirtualizerDynamic rows={rows} />
      <br />
      <br />
      <h3>Columns</h3>
      <ColumnVirtualizerDynamic columns={columns} />
      <br />
      <br />
      <h3>Grid</h3>
      <GridVirtualizerDynamic rows={rows} columns={columns} />
    </div>
  )
}

function RowVirtualizerDynamic({ rows }: { rows: Array<number> }) {
  const parentRef = React.useRef<HTMLDivElement>(null)

  const rowVirtualizer = useVirtualizer({
    count: rows.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 50,
    paddingStart: 100,
    paddingEnd: 100,
  })

  return (
    <>
      <div
        ref={parentRef}
        className="List"
        style={{
          height: `200px`,
          width: `400px`,
          overflow: 'auto',
        }}
      >
        <div
          style={{
            height: `${rowVirtualizer.getTotalSize()}px`,
            width: '100%',
            position: 'relative',
          }}
        >
          {rowVirtualizer.getVirtualItems().map((virtualRow) => (
            <div
              key={virtualRow.key}
              data-index={virtualRow.index}
              ref={rowVirtualizer.measureElement}
              className={virtualRow.index % 2 ? 'ListItemOdd' : 'ListItemEven'}
              style={{
                position: 'absolute',
                top: 0,
                left: 0,
                width: '100%',
                height: `${rows[virtualRow.index]}px`,
                transform: `translateY(${virtualRow.start}px)`,
              }}
            >
              Row {virtualRow.index}
            </div>
          ))}
        </div>
      </div>
    </>
  )
}

function ColumnVirtualizerDynamic({ columns }: { columns: Array<number> }) {
  const parentRef = React.useRef<HTMLDivElement>(null)

  const columnVirtualizer = useVirtualizer({
    horizontal: true,
    count: columns.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 50,
    paddingStart: 100,
    paddingEnd: 100,
  })

  return (
    <>
      <div
        ref={parentRef}
        className="List"
        style={{
          width: `400px`,
          height: `100px`,
          overflow: 'auto',
        }}
      >
        <div
          style={{
            width: `${columnVirtualizer.getTotalSize()}px`,
            height: '100%',
            position: 'relative',
          }}
        >
          {columnVirtualizer.getVirtualItems().map((virtualColumn) => (
            <div
              key={virtualColumn.key}
              data-index={virtualColumn.index}
              ref={columnVirtualizer.measureElement}
              className={
                virtualColumn.index % 2 ? 'ListItemOdd' : 'ListItemEven'
              }
              style={{
                position: 'absolute',
                top: 0,
                left: 0,
                height: '100%',
                width: `${columns[virtualColumn.index]}px`,
                transform: `translateX(${virtualColumn.start}px)`,
              }}
            >
              Column {virtualColumn.index}
            </div>
          ))}
        </div>
      </div>
    </>
  )
}

function GridVirtualizerDynamic({
  rows,
  columns,
}: {
  rows: Array<number>
  columns: Array<number>
}) {
  const parentRef = React.useRef<HTMLDivElement>(null)

  const rowVirtualizer = useVirtualizer({
    count: rows.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 50,
    paddingStart: 200,
    paddingEnd: 200,
    indexAttribute: 'data-row-index',
  })

  const columnVirtualizer = useVirtualizer({
    horizontal: true,
    count: columns.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 50,
    paddingStart: 200,
    paddingEnd: 200,
    indexAttribute: 'data-column-index',
  })

  const [show, setShow] = React.useState(true)

  const halfWay = Math.floor(rows.length / 2)

  return (
    <>
      <button onClick={() => setShow((old) => !old)}>Toggle</button>

```

--------------------------------

### React Virtualizer with Variable Column Widths (Horizontal)

Source: https://tanstack.com/virtual/latest/docs/framework/react/examples/variable

Implements a horizontally virtualized list where each column can have a different width. It utilizes the `useVirtualizer` hook with the `horizontal` option enabled. Dependencies include React and TanStack Virtual.

```jsx
function MasonryHorizontalVirtualizerVariable({
  rows,
}: { rows: Array<number> }) {
  const parentRef = React.useRef<HTMLDivElement>(null)

  const columnVirtualizer = useVirtualizer({
    horizontal: true,
    count: columns.length,
    getScrollElement: () => parentRef.current,
    estimateSize: (i) => columns[i],
    overscan: 5,
    lanes: 4,
  })

  return (
    <>
      <div
        ref={parentRef}
        className="List"
        style={{
          width: `500px`,
          height: `400px`,
          overflow: 'auto',
        }}
      >
        <div
          style={{
            width: `${columnVirtualizer.getTotalSize()}px`,
            height: '100%',
            position: 'relative',
          }}
        >
          {columnVirtualizer.getVirtualItems().map((virtualColumn) => (
            <div
              key={virtualColumn.index}
              className={
                virtualColumn.index % 2 ? 'ListItemOdd' : 'ListItemEven'
              }
              style={{
                position: 'absolute',
                top: `${virtualColumn.lane * 25}%`,
                left: 0,
                height: '25%',
                width: `${columns[virtualColumn.index]}px`,
                transform: `translateX(${virtualColumn.start}px)`,
              }}
            >
              Column {virtualColumn.index}
            </div>
          ))}
        </div>
      </div>
    </>
  )
}
```

--------------------------------

### Generating Dynamic Columns for Grid Virtualization (React)

Source: https://tanstack.com/virtual/latest/docs/framework/react/examples/dynamic

A utility function to generate an array of column definitions with dynamic widths. It creates column objects, each with a unique key, a name, and a randomly assigned width, suitable for use in a virtualized grid.

```jsx
const generateColumns = (count: number) => {
  return new Array(count).fill(0).map((_, i) => {
    const key: string = i.toString()
    return {
      key,
      name: `Column ${i}`,
      width: randomNumber(75, 300),
    }
  })
}
```

--------------------------------

### React Grid Virtualization with Fixed Sizes

Source: https://tanstack.com/virtual/latest/docs/framework/react/examples/fixed

Demonstrates virtualization for a grid layout with fixed row and column sizes. It utilizes two `useVirtualizer` instances, one for rows and one for columns, to manage the rendering of cells within a scrollable container. Requires React and @tanstack/react-virtual.

```jsx
function GridVirtualizerFixed() {
  const parentRef = React.useRef(null)

  const rowVirtualizer = useVirtualizer({
    count: 10000,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 35,
    overscan: 5,
  })

  const columnVirtualizer = useVirtualizer({
    horizontal: true,
    count: 10000,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 100,
    overscan: 5,
  })

  return (
    <>
      <div
        ref={parentRef}
        className="List"
        style={{
          height: `500px`,
          width: `500px`,
          overflow: 'auto',
        }}
      >
        <div
          style={{
            height: `${rowVirtualizer.getTotalSize()}px`,
            width: `${columnVirtualizer.getTotalSize()}px`,
            position: 'relative',
          }}
        >
          {rowVirtualizer.getVirtualItems().map((virtualRow) => (
            <React.Fragment key={virtualRow.index}>
              {columnVirtualizer.getVirtualItems().map((virtualColumn) => (
                <div
                  key={virtualColumn.index}
                  className={
                    virtualRow.index % 2
                      ? 'ListItemOdd'
                      : 'ListItemEven'
                  }
                  style={{
                    position: 'absolute',
                    top: 0,
                    left: 0,
                    width: `${virtualColumn.size}px`,
                    height: `${virtualRow.size}px`,
                    transform: `translateX(${virtualColumn.start}px) translateY(${virtualRow.start}px)`,
                  }}
                >
                  Cell {virtualRow.index}, {virtualColumn.index}
                </div>
              ))}
            </React.Fragment>
          ))}
        </div>
      </div>
    </>
  )
}
```

--------------------------------

### React Virtualizer with Sticky Headers

Source: https://tanstack.com/virtual/latest/docs/framework/react/examples/sticky

This React component uses TanStack Virtual to render a virtualized list of names. It implements sticky headers for grouped sections of the list, enhancing user experience for long datasets. Dependencies include React, ReactDOM, lodash, and @tanstack/react-virtual.

```tsx
import './index.css'
import * as React from 'react'
import ReactDOM from 'react-dom'
import { faker } from '@faker-js/faker'
import { findIndex, groupBy } from 'lodash'
import { defaultRangeExtractor, useVirtualizer } from '@tanstack/react-virtual'
import type { Range } from '@tanstack/react-virtual'

const groupedNames = groupBy(
  Array.from({ length: 1000 })
    .map(() => faker.person.firstName())
    .sort(),
  (name) => name[0],
)
const groups = Object.keys(groupedNames)
const rows = groups.reduce<Array<string>>(
  (acc, k) => [...acc, k, ...groupedNames[k]],
  [],
)

const App = () => {
  const parentRef = React.useRef<HTMLDivElement>(null)

  const activeStickyIndexRef = React.useRef(0)

  const stickyIndexes = React.useMemo(
    () => groups.map((gn) => findIndex(rows, (n) => n === gn)),
    [],
  )

  const isSticky = (index: number) => stickyIndexes.includes(index)

  const isActiveSticky = (index: number) =>
    activeStickyIndexRef.current === index

  const rowVirtualizer = useVirtualizer({
    count: rows.length,
    estimateSize: () => 50,
    getScrollElement: () => parentRef.current,
    rangeExtractor: React.useCallback(
      (range: Range) => {
        activeStickyIndexRef.current =
          [...stickyIndexes]
            .reverse()
            .find((index) => range.startIndex >= index) ?? 0

        const next = new Set([
          activeStickyIndexRef.current,
          ...defaultRangeExtractor(range),
        ])

        return [...next].sort((a, b) => a - b)
      },
      [stickyIndexes],
    ),
  })

  return (
    <div>
      <div
        ref={parentRef}
        className="List"
        style={{
          height: `300px`,
          width: `400px`,
          overflow: 'auto',
        }}
      >
        <div
          style={{
            height: `${rowVirtualizer.getTotalSize()}px`,
            width: '100%',
            position: 'relative',
          }}
        >
          {rowVirtualizer.getVirtualItems().map((virtualRow) => (
            <div
              key={virtualRow.index}
              className={'ListItem'}
              style={{
                ...(isSticky(virtualRow.index)
                  ? {
                      background: '#fff',
                      borderBottom: '1px solid #ddd',
                      zIndex: 1,
                    }
                  : {}),
                ...(isActiveSticky(virtualRow.index)
                  ? {
                      position: 'sticky',
                    }
                  : {
                      position: 'absolute',
                      transform: `translateY(${virtualRow.start}px)`,
                    }),
                top: 0,
                left: 0,
                width: '100%',
                height: `${virtualRow.size}px`,
              }}
            >
              {rows[virtualRow.index]}
            </div>
          ))}
        </div>
      </div>
      {process.env.NODE_ENV === 'development' ? (
        <p>
          <strong>Notice:</strong> You are currently running React in
          development mode. Rendering performance will be slightly degraded
          until this application is built for production.
        </p>
      ) : null}
    </div>
  )
}

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root'),
)

```

--------------------------------

### Get Current Scroll Offset (TypeScript)

Source: https://tanstack.com/virtual/latest/docs/api/virtualizer

The `scrollOffset` property represents the current scroll position in pixels from the start of the scrollable area. This value is essential for calculating visible items and managing scroll-related logic.

```tsx
scrollOffset: number
```

--------------------------------

### VirtualItem Properties Explained (TypeScript)

Source: https://tanstack.com/virtual/latest/docs/api/virtual-item

Details the properties of the VirtualItem object, including key, index, start, end, size, and lane. These properties are used to determine an item's position, dimensions, and unique identifier within the virtualizer.

```typescript
// The unique key for the item. By default this is the item index, but should be configured via the `getItemKey` Virtualizer option.
key: string | number | bigint

// The index of the item.
index: number

// The starting pixel offset for the item. This is usually mapped to a css property or transform like `top/left` or `translateX/translateY`.
start: number

// The ending pixel offset for the item. This value is not necessary for most layouts, but can be helpful so we've provided it anyway.
end: number

// The size of the item. This is usually mapped to a css property like `width/height`. Before an item is measured with the `VirtualItem.measureElement` method, this will be the estimated size returned from your `estimateSize` virtualizer option. After an item is measured (if you choose to measure it at all), this value will be the number returned by your `measureElement` virtualizer option (which by default is configured to measure elements with `getBoundingClientRect()`)
size: number

// The lane index of the item. In regular lists it will always be set to `0` but becomes useful for masonry layouts (see variable examples for more details).
lane: number
```

--------------------------------

### Virtualized Grid with Row and Column Virtualization (React)

Source: https://tanstack.com/virtual/latest/docs/framework/react/examples/dynamic

Implements a virtualized grid using TanStack Virtual, handling both row and column virtualization. It dynamically calculates column widths and row heights, optimizing rendering for large datasets. Dependencies include React and TanStack Virtual.

```jsx
function GridVirtualizer() {
  const parentRef = React.useRef(null)
  const parentOffsetRef = React.useRef(0)

  const columns = React.useMemo(() => generateColumns(100), [])
  const data = React.useMemo(() => generateData(columns), [columns])

  const getColumnWidth = (index) => columns[index].width

  const rowVirtualizer = useVirtualizer({
    count: data.length,
    estimateSize: () => 350,
    overscan: 5,
    scrollMargin: parentOffsetRef.current,
  })

  const columnVirtualizer = useVirtualizer({
    horizontal: true,
    count: columns.length,
    getScrollElement: () => parentRef.current,
    estimateSize: getColumnWidth,
    overscan: 5,
  })
  const columnItems = columnVirtualizer.getVirtualItems()
  const [before, after] =
    columnItems.length > 0
      ? [
          columnItems[0].start,
          columnVirtualizer.getTotalSize() -
            columnItems[columnItems.length - 1].end,
        ]
      : [0, 0]

  return (
    <div
      ref={parentRef}
      style={{ overflowY: 'auto', border: '1px solid #c8c8c8' }}
    >
      <div
        style={{
          height: rowVirtualizer.getTotalSize(),
          position: 'relative',
        }}
      >
        {rowVirtualizer.getVirtualItems().map((row) => {
          return (
            <div
              key={row.key}
              data-index={row.index}
              ref={rowVirtualizer.measureElement}
              style={{
                position: 'absolute',
                top: 0,
                left: 0,
                transform: `translateY(${row.start}px)`,
                display: 'flex',
              }}
            >
              <div style={{ width: `${before}px` }} />
              {columnItems.map((column) => {
                return (
                  <div
                    key={column.key}
                    style={{
                      minHeight: row.index === 0 ? 50 : row.size,
                      width: getColumnWidth(column.index),
                      borderBottom: '1px solid #c8c8c8',
                      borderRight: '1px solid #c8c8c8',
                      padding: '7px 12px',
                    }}
                  >
                    {row.index === 0 ? (
                      <div>{columns[column.index].name}</div>
                    ) : (
                      <div>{data[row.index][column.index]}</div>
                    )}
                  </div>
                )
              })}
              <div style={{ width: `${after}px` }} />
            </div>
          )
        })}
      </div>
    </div>
  )
}

const generateColumns = (count) => {
  return new Array(count).fill(0).map((_, i) => {
    const key = i.toString()
    return {
      key,
      name: `Column ${i}`,
      width: randomNumber(75, 300),
    }
  })
}

const generateData = (columns, count = 300) => {
  return new Array(count).fill(0).map((_, rowIndex) =>
    columns.reduce((acc, _curr, colIndex) => {
      const val = faker.lorem.lines(((rowIndex + colIndex) % 10) + 1)
      acc.push(val)
      return acc
    }, []),
  )
}
```