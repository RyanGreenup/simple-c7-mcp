# Material React Table V3

Material React Table is a fully-featured React data table component library built on top of Material UI V6 and TanStack Table V8. It provides a TypeScript-first approach to creating professional, responsive data tables with Material Design styling and comprehensive built-in functionality. The library combines the headless table logic of TanStack Table with the polished component system of Material UI to deliver production-ready tables with minimal configuration.

The library supports 50+ features including sorting, filtering, pagination, column ordering, row selection, editing, aggregation, virtualization, and more. All features can be easily enabled or disabled through a declarative API. With built-in support for 38+ languages, extensive customization options, and a small bundle size (30-56KB gzipped), Material React Table offers both developer experience and end-user performance. It ships with TypeScript definitions, comprehensive documentation, and works seamlessly with server-side data fetching patterns.

---

## Basic Table Setup

Create a simple data table with default features enabled.

```tsx
import { useMemo } from 'react';
import {
  MaterialReactTable,
  useMaterialReactTable,
  type MRT_ColumnDef,
} from 'material-react-table';

type Person = {
  name: {
    firstName: string;
    lastName: string;
  };
  address: string;
  city: string;
  state: string;
};

const data: Person[] = [
  {
    name: { firstName: 'John', lastName: 'Doe' },
    address: '261 Erdman Ford',
    city: 'East Daphne',
    state: 'Kentucky',
  },
  {
    name: { firstName: 'Jane', lastName: 'Doe' },
    address: '769 Dominic Grove',
    city: 'Columbus',
    state: 'Ohio',
  },
];

export default function Example() {
  const columns = useMemo<MRT_ColumnDef<Person>[]>(
    () => [
      {
        accessorKey: 'name.firstName', // Access nested data with dot notation
        header: 'First Name',
        size: 150,
      },
      {
        accessorKey: 'name.lastName',
        header: 'Last Name',
        size: 150,
      },
      {
        accessorKey: 'address',
        header: 'Address',
        size: 200,
      },
      {
        accessorKey: 'city',
        header: 'City',
        size: 150,
      },
      {
        accessorKey: 'state',
        header: 'State',
        size: 150,
      },
    ],
    [],
  );

  const table = useMaterialReactTable({
    columns,
    data, // Data must be memoized or stable
  });

  return <MaterialReactTable table={table} />;
}
```

---

## Table Hook with State Management

Use the hook to create a table instance with custom state management and feature toggles.

```tsx
import { useMemo, useState, useEffect } from 'react';
import {
  MaterialReactTable,
  useMaterialReactTable,
  type MRT_ColumnDef,
} from 'material-react-table';

type Person = {
  name: string;
  age: number;
};

const data: Person[] = [
  { name: 'John', age: 30 },
  { name: 'Sara', age: 25 },
];

export default function App() {
  const columns = useMemo<MRT_ColumnDef<Person>[]>(
    () => [
      {
        accessorKey: 'name',
        header: 'Name',
        muiTableHeadCellProps: { sx: { color: 'green' } },
        Cell: ({ cell }) => <span>{cell.getValue()}</span>,
      },
      {
        accessorFn: (row) => row.age, // Alternate accessor method
        id: 'age', // ID required when using accessorFn
        header: 'Age',
        Header: () => <i>Age</i>, // Custom header component
      },
    ],
    [],
  );

  // Manage table state externally
  const [rowSelection, setRowSelection] = useState({});
  const [sorting, setSorting] = useState([]);

  useEffect(() => {
    console.log('Row selection changed:', rowSelection);
  }, [rowSelection]);

  const table = useMaterialReactTable({
    columns,
    data,
    enableColumnOrdering: true,
    enableRowSelection: true,
    enablePagination: false,
    onRowSelectionChange: setRowSelection,
    onSortingChange: setSorting,
    state: { rowSelection, sorting }, // Pass state back to table
  });

  const handleEvent = () => {
    // Access table state from instance
    console.log(table.getState().sorting);
    console.log(table.getState().rowSelection);
  };

  return (
    <div>
      <button onClick={handleEvent}>Log Table State</button>
      <MaterialReactTable table={table} />
    </div>
  );
}
```

---

## CRUD Operations with Row Editing

Implement full Create, Read, Update, Delete operations with inline row editing and validation.

```tsx
import { useMemo, useState } from 'react';
import {
  MaterialReactTable,
  type MRT_ColumnDef,
  type MRT_Row,
  type MRT_TableOptions,
  useMaterialReactTable,
} from 'material-react-table';
import { Box, Button, IconButton, Tooltip } from '@mui/material';
import {
  QueryClient,
  QueryClientProvider,
  useMutation,
  useQuery,
  useQueryClient,
} from '@tanstack/react-query';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';

type User = {
  id: string;
  firstName: string;
  lastName: string;
  email: string;
  state: string;
};

const usStates = ['California', 'Texas', 'Florida', 'New York'];

function Example() {
  const [validationErrors, setValidationErrors] = useState<
    Record<string, string | undefined>
  >({});

  const columns = useMemo<MRT_ColumnDef<User>[]>(
    () => [
      {
        accessorKey: 'id',
        header: 'Id',
        enableEditing: false,
        size: 80,
      },
      {
        accessorKey: 'firstName',
        header: 'First Name',
        muiEditTextFieldProps: {
          required: true,
          error: !!validationErrors?.firstName,
          helperText: validationErrors?.firstName,
          onFocus: () =>
            setValidationErrors({
              ...validationErrors,
              firstName: undefined,
            }),
        },
      },
      {
        accessorKey: 'lastName',
        header: 'Last Name',
        muiEditTextFieldProps: {
          required: true,
          error: !!validationErrors?.lastName,
          helperText: validationErrors?.lastName,
          onFocus: () =>
            setValidationErrors({
              ...validationErrors,
              lastName: undefined,
            }),
        },
      },
      {
        accessorKey: 'email',
        header: 'Email',
        muiEditTextFieldProps: {
          type: 'email',
          required: true,
          error: !!validationErrors?.email,
          helperText: validationErrors?.email,
          onFocus: () =>
            setValidationErrors({
              ...validationErrors,
              email: undefined,
            }),
        },
      },
      {
        accessorKey: 'state',
        header: 'State',
        editVariant: 'select',
        editSelectOptions: usStates,
        muiEditTextFieldProps: {
          select: true,
          error: !!validationErrors?.state,
          helperText: validationErrors?.state,
        },
      },
    ],
    [validationErrors],
  );

  // React Query hooks for CRUD operations
  const { mutateAsync: createUser, isPending: isCreatingUser } =
    useCreateUser();
  const {
    data: fetchedUsers = [],
    isError: isLoadingUsersError,
    isFetching: isFetchingUsers,
    isLoading: isLoadingUsers,
  } = useGetUsers();
  const { mutateAsync: updateUser, isPending: isUpdatingUser } =
    useUpdateUser();
  const { mutateAsync: deleteUser, isPending: isDeletingUser } =
    useDeleteUser();

  // CREATE action
  const handleCreateUser: MRT_TableOptions<User>['onCreatingRowSave'] = async ({
    values,
    table,
  }) => {
    const newValidationErrors = validateUser(values);
    if (Object.values(newValidationErrors).some((error) => error)) {
      setValidationErrors(newValidationErrors);
      return;
    }
    setValidationErrors({});
    await createUser(values);
    table.setCreatingRow(null);
  };

  // UPDATE action
  const handleSaveUser: MRT_TableOptions<User>['onEditingRowSave'] = async ({
    values,
    table,
  }) => {
    const newValidationErrors = validateUser(values);
    if (Object.values(newValidationErrors).some((error) => error)) {
      setValidationErrors(newValidationErrors);
      return;
    }
    setValidationErrors({});
    await updateUser(values);
    table.setEditingRow(null);
  };

  // DELETE action
  const openDeleteConfirmModal = (row: MRT_Row<User>) => {
    if (window.confirm('Are you sure you want to delete this user?')) {
      deleteUser(row.original.id);
    }
  };

  const table = useMaterialReactTable({
    columns,
    data: fetchedUsers,
    createDisplayMode: 'row', // 'modal', 'custom' also available
    editDisplayMode: 'row', // 'modal', 'cell', 'table', 'custom' available
    enableEditing: true,
    getRowId: (row) => row.id,
    muiToolbarAlertBannerProps: isLoadingUsersError
      ? {
          color: 'error',
          children: 'Error loading data',
        }
      : undefined,
    muiTableContainerProps: {
      sx: { minHeight: '500px' },
    },
    onCreatingRowCancel: () => setValidationErrors({}),
    onCreatingRowSave: handleCreateUser,
    onEditingRowCancel: () => setValidationErrors({}),
    onEditingRowSave: handleSaveUser,
    renderRowActions: ({ row, table }) => (
      <Box sx={{ display: 'flex', gap: '1rem' }}>
        <Tooltip title="Edit">
          <IconButton onClick={() => table.setEditingRow(row)}>
            <EditIcon />
          </IconButton>
        </Tooltip>
        <Tooltip title="Delete">
          <IconButton color="error" onClick={() => openDeleteConfirmModal(row)}>
            <DeleteIcon />
          </IconButton>
        </Tooltip>
      </Box>
    ),
    renderTopToolbarCustomActions: ({ table }) => (
      <Button
        variant="contained"
        onClick={() => {
          table.setCreatingRow(true);
        }}
      >
        Create New User
      </Button>
    ),
    state: {
      isLoading: isLoadingUsers,
      isSaving: isCreatingUser || isUpdatingUser || isDeletingUser,
      showAlertBanner: isLoadingUsersError,
      showProgressBars: isFetchingUsers,
    },
  });

  return <MaterialReactTable table={table} />;
}

// React Query CRUD hooks
function useCreateUser() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: async (user: User) => {
      await fetch('/api/users', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(user),
      });
    },
    onMutate: (newUserInfo: User) => {
      queryClient.setQueryData(['users'], (prevUsers: any) => [
        ...prevUsers,
        { ...newUserInfo, id: (Math.random() + 1).toString(36).substring(7) },
      ]);
    },
  });
}

function useGetUsers() {
  return useQuery<User[]>({
    queryKey: ['users'],
    queryFn: async () => {
      const response = await fetch('/api/users');
      return response.json();
    },
    refetchOnWindowFocus: false,
  });
}

function useUpdateUser() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: async (user: User) => {
      await fetch(`/api/users/${user.id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(user),
      });
    },
    onMutate: (newUserInfo: User) => {
      queryClient.setQueryData(['users'], (prevUsers: any) =>
        prevUsers?.map((prevUser: User) =>
          prevUser.id === newUserInfo.id ? newUserInfo : prevUser,
        ),
      );
    },
  });
}

function useDeleteUser() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: async (userId: string) => {
      await fetch(`/api/users/${userId}`, { method: 'DELETE' });
    },
    onMutate: (userId: string) => {
      queryClient.setQueryData(['users'], (prevUsers: any) =>
        prevUsers?.filter((user: User) => user.id !== userId),
      );
    },
  });
}

// Validation helpers
const validateRequired = (value: string) => !!value.length;
const validateEmail = (email: string) =>
  !!email.length &&
  email
    .toLowerCase()
    .match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/);

function validateUser(user: User) {
  return {
    firstName: !validateRequired(user.firstName) ? 'First Name is Required' : '',
    lastName: !validateRequired(user.lastName) ? 'Last Name is Required' : '',
    email: !validateEmail(user.email) ? 'Incorrect Email Format' : '',
  };
}

// App wrapper with React Query
const queryClient = new QueryClient();

export default function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Example />
    </QueryClientProvider>
  );
}
```

---

## Aggregation and Grouping

Enable data grouping with aggregation functions and custom rendering.

```tsx
import { useMemo } from 'react';
import { Box, Stack } from '@mui/material';
import {
  MaterialReactTable,
  useMaterialReactTable,
  type MRT_ColumnDef,
} from 'material-react-table';

type Person = {
  firstName: string;
  lastName: string;
  age: number;
  gender: string;
  state: string;
  salary: number;
};

const data: Person[] = [
  {
    firstName: 'John',
    lastName: 'Doe',
    age: 35,
    gender: 'Male',
    state: 'California',
    salary: 75000,
  },
  {
    firstName: 'Jane',
    lastName: 'Smith',
    age: 42,
    gender: 'Female',
    state: 'California',
    salary: 85000,
  },
  {
    firstName: 'Bob',
    lastName: 'Johnson',
    age: 28,
    gender: 'Male',
    state: 'Texas',
    salary: 65000,
  },
];

export default function Example() {
  const averageSalary = useMemo(
    () => data.reduce((acc, curr) => acc + curr.salary, 0) / data.length,
    [],
  );

  const maxAge = useMemo(
    () => data.reduce((acc, curr) => Math.max(acc, curr.age), 0),
    [],
  );

  const columns = useMemo<MRT_ColumnDef<Person>[]>(
    () => [
      {
        header: 'First Name',
        accessorKey: 'firstName',
        enableGrouping: false, // Prevent grouping by this column
      },
      {
        header: 'Last Name',
        accessorKey: 'lastName',
      },
      {
        header: 'Age',
        accessorKey: 'age',
        aggregationFn: 'max', // Built-in aggregation function
        AggregatedCell: ({ cell, table }) => (
          <>
            Oldest by{' '}
            {table.getColumn(cell.row.groupingColumnId ?? '').columnDef.header}:{' '}
            <Box
              sx={{ color: 'info.main', display: 'inline', fontWeight: 'bold' }}
            >
              {cell.getValue<number>()}
            </Box>
          </>
        ),
        Footer: () => (
          <Stack>
            Max Age:
            <Box color="warning.main">{Math.round(maxAge)}</Box>
          </Stack>
        ),
      },
      {
        header: 'Gender',
        accessorKey: 'gender',
        GroupedCell: ({ cell, row }) => (
          <Box sx={{ color: 'primary.main' }}>
            <strong>{cell.getValue<string>()}s</strong> ({row.subRows?.length})
          </Box>
        ),
      },
      {
        header: 'State',
        accessorKey: 'state',
      },
      {
        header: 'Salary',
        accessorKey: 'salary',
        aggregationFn: 'mean', // Average aggregation
        AggregatedCell: ({ cell, table }) => (
          <>
            Average by{' '}
            {table.getColumn(cell.row.groupingColumnId ?? '').columnDef.header}:{' '}
            <Box sx={{ color: 'success.main', fontWeight: 'bold' }}>
              {cell.getValue<number>()?.toLocaleString('en-US', {
                style: 'currency',
                currency: 'USD',
                minimumFractionDigits: 0,
                maximumFractionDigits: 0,
              })}
            </Box>
          </>
        ),
        Cell: ({ cell }) => (
          <>
            {cell.getValue<number>()?.toLocaleString('en-US', {
              style: 'currency',
              currency: 'USD',
              minimumFractionDigits: 0,
              maximumFractionDigits: 0,
            })}
          </>
        ),
        Footer: () => (
          <Stack>
            Average Salary:
            <Box color="warning.main">
              {averageSalary?.toLocaleString('en-US', {
                style: 'currency',
                currency: 'USD',
                minimumFractionDigits: 0,
                maximumFractionDigits: 0,
              })}
            </Box>
          </Stack>
        ),
      },
    ],
    [averageSalary, maxAge],
  );

  const table = useMaterialReactTable({
    columns,
    data,
    displayColumnDefOptions: {
      'mrt-row-expand': {
        enableResizing: true,
      },
    },
    enableColumnResizing: true,
    enableGrouping: true,
    enableStickyHeader: true,
    enableStickyFooter: true,
    initialState: {
      density: 'compact',
      expanded: true, // Expand all groups by default
      grouping: ['state'], // Group by state
      pagination: { pageIndex: 0, pageSize: 20 },
      sorting: [{ id: 'state', desc: false }],
    },
    muiToolbarAlertBannerChipProps: { color: 'primary' },
    muiTableContainerProps: { sx: { maxHeight: 700 } },
  });

  return <MaterialReactTable table={table} />;
}
```

---

## Custom Filter Functions

Use custom filter functions for specialized filtering logic.

```tsx
import { useMemo } from 'react';
import {
  MaterialReactTable,
  useMaterialReactTable,
  type MRT_ColumnDef,
  MRT_FilterFns,
} from 'material-react-table';

type Product = {
  id: string;
  name: string;
  price: number;
  category: string;
  tags: string[];
};

const data: Product[] = [
  {
    id: '1',
    name: 'Laptop',
    price: 1200,
    category: 'Electronics',
    tags: ['computer', 'portable', 'work'],
  },
  {
    id: '2',
    name: 'Mouse',
    price: 25,
    category: 'Electronics',
    tags: ['computer', 'accessory'],
  },
];

export default function Example() {
  const columns = useMemo<MRT_ColumnDef<Product>[]>(
    () => [
      {
        accessorKey: 'name',
        header: 'Product Name',
        filterFn: 'fuzzy', // Fuzzy matching filter
      },
      {
        accessorKey: 'price',
        header: 'Price',
        filterVariant: 'range', // Range filter with min/max
        filterFn: 'betweenInclusive',
        Cell: ({ cell }) => `$${cell.getValue<number>()}`,
      },
      {
        accessorKey: 'category',
        header: 'Category',
        filterVariant: 'select',
        filterSelectOptions: ['Electronics', 'Clothing', 'Food'],
        filterFn: 'equals',
      },
      {
        accessorKey: 'tags',
        header: 'Tags',
        filterFn: 'arrIncludesSome', // Array filter - matches if any tag matches
        Cell: ({ cell }) => cell.getValue<string[]>().join(', '),
      },
    ],
    [],
  );

  const table = useMaterialReactTable({
    columns,
    data,
    enableColumnFilterModes: true, // Allow switching filter modes
    enableFacetedValues: true, // Show count of unique values
    initialState: {
      showColumnFilters: true,
    },
  });

  return <MaterialReactTable table={table} />;
}

// Available filter functions:
// - fuzzy: Best match filtering using ranking
// - contains: Case-insensitive substring match
// - startsWith: Starts with filter
// - endsWith: Ends with filter
// - equals: Exact match (case-insensitive)
// - notEquals: Not equal
// - between: Range filter (exclusive)
// - betweenInclusive: Range filter (inclusive)
// - greaterThan, greaterThanOrEqualTo: Numeric comparison
// - lessThan, lessThanOrEqualTo: Numeric comparison
// - isEmpty: Check if empty/null
// - notEmpty: Check if not empty
// - arrIncludes: Array exact match
// - arrIncludesSome: Array matches any value
// - arrIncludesAll: Array matches all values
```

---

## Column Customization and Styling

Customize column appearance, behavior, and Material UI props.

```tsx
import { useMemo } from 'react';
import {
  MaterialReactTable,
  useMaterialReactTable,
  type MRT_ColumnDef,
} from 'material-react-table';
import { Box, Chip } from '@mui/material';

type Employee = {
  id: string;
  name: string;
  department: string;
  status: 'active' | 'inactive';
  salary: number;
};

const data: Employee[] = [
  {
    id: '1',
    name: 'John Doe',
    department: 'Engineering',
    status: 'active',
    salary: 95000,
  },
];

export default function Example() {
  const columns = useMemo<MRT_ColumnDef<Employee>[]>(
    () => [
      {
        accessorKey: 'name',
        header: 'Employee Name',
        size: 200,
        minSize: 150,
        maxSize: 300,
        enableColumnOrdering: true,
        enablePinning: true,
        muiTableHeadCellProps: {
          sx: {
            fontWeight: 'bold',
            fontSize: '16px',
            color: 'primary.main',
          },
        },
        muiTableBodyCellProps: {
          sx: {
            backgroundColor: 'background.paper',
          },
        },
      },
      {
        accessorKey: 'department',
        header: 'Department',
        enableColumnFilter: true,
        filterVariant: 'multi-select',
        muiTableHeadCellProps: {
          align: 'center',
        },
        muiTableBodyCellProps: {
          align: 'center',
        },
      },
      {
        accessorKey: 'status',
        header: 'Status',
        Cell: ({ cell }) => {
          const status = cell.getValue<string>();
          return (
            <Chip
              label={status}
              color={status === 'active' ? 'success' : 'default'}
              size="small"
            />
          );
        },
        muiTableBodyCellProps: ({ cell }) => ({
          sx: {
            backgroundColor:
              cell.getValue<string>() === 'active'
                ? 'success.light'
                : 'grey.100',
          },
        }),
      },
      {
        accessorKey: 'salary',
        header: 'Salary',
        Cell: ({ cell }) => (
          <Box sx={{ textAlign: 'right' }}>
            {cell.getValue<number>().toLocaleString('en-US', {
              style: 'currency',
              currency: 'USD',
            })}
          </Box>
        ),
        muiTableHeadCellProps: {
          align: 'right',
        },
        muiTableBodyCellProps: {
          align: 'right',
          sx: {
            fontFamily: 'monospace',
          },
        },
      },
    ],
    [],
  );

  const table = useMaterialReactTable({
    columns,
    data,
    enableColumnOrdering: true,
    enableColumnPinning: true,
    enableColumnResizing: true,
    columnResizeMode: 'onChange',
    layoutMode: 'grid', // Alternative: 'semantic'
    muiTableProps: {
      sx: {
        border: '1px solid rgba(81, 81, 81, 0.5)',
      },
    },
    muiTableHeadProps: {
      sx: {
        backgroundColor: 'primary.light',
      },
    },
    muiTableBodyProps: {
      sx: {
        '& tr:nth-of-type(odd)': {
          backgroundColor: 'grey.50',
        },
      },
    },
  });

  return <MaterialReactTable table={table} />;
}
```

---

## Virtualization for Large Datasets

Enable row and column virtualization for rendering thousands of rows efficiently.

```tsx
import { useMemo } from 'react';
import {
  MaterialReactTable,
  useMaterialReactTable,
  type MRT_ColumnDef,
} from 'material-react-table';

type Row = {
  id: string;
  firstName: string;
  lastName: string;
  email: string;
  city: string;
  state: string;
};

// Generate large dataset
const data: Row[] = Array.from({ length: 10000 }, (_, i) => ({
  id: String(i),
  firstName: `FirstName${i}`,
  lastName: `LastName${i}`,
  email: `user${i}@example.com`,
  city: `City${i}`,
  state: `State${i % 50}`,
}));

export default function Example() {
  const columns = useMemo<MRT_ColumnDef<Row>[]>(
    () => [
      {
        accessorKey: 'id',
        header: 'ID',
        size: 100,
      },
      {
        accessorKey: 'firstName',
        header: 'First Name',
        size: 150,
      },
      {
        accessorKey: 'lastName',
        header: 'Last Name',
        size: 150,
      },
      {
        accessorKey: 'email',
        header: 'Email',
        size: 200,
      },
      {
        accessorKey: 'city',
        header: 'City',
        size: 150,
      },
      {
        accessorKey: 'state',
        header: 'State',
        size: 150,
      },
    ],
    [],
  );

  const table = useMaterialReactTable({
    columns,
    data,
    enableRowVirtualization: true, // Enable row virtualization
    enableColumnVirtualization: true, // Enable column virtualization (optional)
    enablePagination: false, // Disable pagination with virtualization
    enableRowNumbers: true,
    muiTableContainerProps: {
      sx: { maxHeight: '600px' },
    },
    rowVirtualizerOptions: {
      overscan: 10, // Number of rows to render outside viewport
      estimateSize: () => 50, // Estimated row height in pixels
    },
    columnVirtualizerOptions: {
      overscan: 2,
    },
  });

  return <MaterialReactTable table={table} />;
}
```

---

## Localization Support

Use built-in localization or provide custom translations.

```tsx
import { useMemo } from 'react';
import {
  MaterialReactTable,
  useMaterialReactTable,
  type MRT_ColumnDef,
  type MRT_Localization,
} from 'material-react-table';
// Import built-in locales
import { MRT_Localization_ES } from 'material-react-table/locales/es';
import { MRT_Localization_FR } from 'material-react-table/locales/fr';
import { MRT_Localization_DE } from 'material-react-table/locales/de';

type Person = {
  name: string;
  age: number;
  city: string;
};

const data: Person[] = [
  { name: 'Juan', age: 30, city: 'Madrid' },
  { name: 'Maria', age: 25, city: 'Barcelona' },
];

export default function Example() {
  const columns = useMemo<MRT_ColumnDef<Person>[]>(
    () => [
      {
        accessorKey: 'name',
        header: 'Nombre',
      },
      {
        accessorKey: 'age',
        header: 'Edad',
      },
      {
        accessorKey: 'city',
        header: 'Ciudad',
      },
    ],
    [],
  );

  // Use built-in Spanish localization
  const table = useMaterialReactTable({
    columns,
    data,
    localization: MRT_Localization_ES,
  });

  return <MaterialReactTable table={table} />;
}

// Custom localization example
const customLocalization: Partial<MRT_Localization> = {
  actions: 'Acciones',
  cancel: 'Cancelar',
  save: 'Guardar',
  search: 'Buscar',
  clearFilter: 'Limpiar filtro',
  clearSearch: 'Limpiar búsqueda',
  clearSort: 'Limpiar orden',
  columnActions: 'Acciones de columna',
  edit: 'Editar',
  expand: 'Expandir',
  expandAll: 'Expandir todo',
  filterByColumn: 'Filtrar por {column}',
  filterMode: 'Modo de filtro: {filterType}',
  hideAll: 'Ocultar todo',
  hideColumn: 'Ocultar columna de {column}',
  rowsPerPage: 'Filas por página',
  showAll: 'Mostrar todo',
  showAllColumns: 'Mostrar todas las columnas',
  showHideColumns: 'Mostrar/Ocultar columnas',
  showHideFilters: 'Mostrar/Ocultar filtros',
  showHideSearch: 'Mostrar/Ocultar búsqueda',
  sortByColumnAsc: 'Ordenar por {column} ascendente',
  sortByColumnDesc: 'Ordenar por {column} descendente',
};

// Available built-in locales (38+ languages):
// ar, az, bg, cs, da, de, el, en, es, et, fa, fi, fr, he, hr, hu, hy,
// id, it, ja, ko, mk, nl, no, np, pl, pt, pt-BR, ro, ru, sk,
// sr-Cyrl-RS, sr-Latn-RS, sv, tr, uk, vi, zh-Hans, zh-Hant
```

---

## Installation

Install Material React Table and peer dependencies.

```bash
# Install peer dependencies (Material UI V6)
npm install @mui/material @mui/x-date-pickers @mui/icons-material @emotion/react @emotion/styled

# Install Material React Table
npm install material-react-table

# Or with yarn
yarn add @mui/material @mui/x-date-pickers @mui/icons-material @emotion/react @emotion/styled
yarn add material-react-table

# Or with pnpm
pnpm add @mui/material @mui/x-date-pickers @mui/icons-material @emotion/react @emotion/styled
pnpm add material-react-table
```

---

## TypeScript Types

Core TypeScript types for type-safe table configuration.

```typescript
import type {
  MRT_ColumnDef,
  MRT_TableOptions,
  MRT_TableInstance,
  MRT_Row,
  MRT_Cell,
  MRT_Column,
  MRT_RowData,
  MRT_ColumnFiltersState,
  MRT_SortingState,
  MRT_PaginationState,
  MRT_RowSelectionState,
} from 'material-react-table';

// Define your data type
type User = {
  id: string;
  name: string;
  email: string;
  age: number;
};

// Column definition with type safety
const columns: MRT_ColumnDef<User>[] = [
  {
    accessorKey: 'name',
    header: 'Name',
    Cell: ({ cell }) => cell.getValue<string>(),
  },
  {
    accessorKey: 'age',
    header: 'Age',
    Cell: ({ cell }) => cell.getValue<number>(),
  },
];

// Table options with type safety
const tableOptions: MRT_TableOptions<User> = {
  columns,
  data: [],
  enableRowSelection: true,
  onRowSelectionChange: (updater) => {
    // Type-safe state updater
  },
};

// Access typed table instance
function handleTableInstance(table: MRT_TableInstance<User>) {
  const selectedRows: MRT_Row<User>[] = table.getSelectedRowModel().rows;
  const firstRow: User = selectedRows[0].original;
  const state: MRT_RowSelectionState = table.getState().rowSelection;
}
```

---

## Main API Configuration

Primary configuration options for table behavior and features.

```typescript
import {
  MaterialReactTable,
  useMaterialReactTable,
  type MRT_TableOptions,
} from 'material-react-table';

type Data = {
  id: string;
  name: string;
};

const data: Data[] = [];
const columns = [];

const tableOptions: MRT_TableOptions<Data> = {
  // Required
  columns, // Column definitions
  data, // Table data

  // Feature toggles (all optional, most default to true)
  enableSorting: true,
  enableMultiSort: true,
  enableFiltering: true,
  enableColumnFilters: true,
  enableGlobalFilter: true,
  enablePagination: true,
  enableRowSelection: true,
  enableMultiRowSelection: true,
  enableRowNumbers: false,
  enableRowActions: false,
  enableRowOrdering: false,
  enableRowDragging: false,
  enableRowPinning: false,
  enableColumnOrdering: false,
  enableColumnDragging: true,
  enableColumnPinning: false,
  enableColumnResizing: false,
  enableEditing: false,
  enableExpanding: false,
  enableGrouping: false,
  enableDensityToggle: true,
  enableFullScreenToggle: true,
  enableClickToCopy: false,
  enableCellActions: false,
  enableStickyHeader: false,
  enableStickyFooter: false,
  enableRowVirtualization: false,
  enableColumnVirtualization: false,
  enableKeyboardShortcuts: true,

  // State management
  state: {
    columnFilters: [],
    globalFilter: '',
    sorting: [],
    pagination: { pageIndex: 0, pageSize: 10 },
    rowSelection: {},
    columnOrder: [],
    columnPinning: { left: [], right: [] },
    expanded: {},
    grouping: [],
  },

  // Initial state (set defaults)
  initialState: {
    density: 'comfortable', // 'comfortable' | 'compact' | 'spacious'
    showColumnFilters: false,
    showGlobalFilter: true,
    pagination: { pageIndex: 0, pageSize: 25 },
  },

  // State change callbacks
  onColumnFiltersChange: (updater) => {},
  onGlobalFilterChange: (updater) => {},
  onSortingChange: (updater) => {},
  onPaginationChange: (updater) => {},
  onRowSelectionChange: (updater) => {},
  onColumnOrderChange: (updater) => {},

  // Editing callbacks
  onCreatingRowSave: async ({ values, table }) => {},
  onCreatingRowCancel: () => {},
  onEditingRowSave: async ({ values, table }) => {},
  onEditingRowCancel: () => {},

  // Display modes
  editDisplayMode: 'modal', // 'modal' | 'row' | 'cell' | 'table' | 'custom'
  createDisplayMode: 'modal', // 'modal' | 'row' | 'custom'

  // Layout
  layoutMode: 'semantic', // 'semantic' | 'grid'
  columnResizeMode: 'onChange', // 'onChange' | 'onEnd'

  // Row configuration
  getRowId: (originalRow) => originalRow.id,
  enableRowSelection: (row) => row.original.isSelectable,

  // Custom render functions
  renderTopToolbarCustomActions: ({ table }) => <div>Actions</div>,
  renderBottomToolbarCustomActions: ({ table }) => <div>Footer</div>,
  renderDetailPanel: ({ row }) => <div>Details</div>,
  renderRowActions: ({ row, table }) => <div>Actions</div>,
  renderToolbarInternalActions: ({ table }) => <div>Internal</div>,

  // Material UI component props (50+ customization points)
  muiTableProps: { sx: {} },
  muiTableHeadProps: { sx: {} },
  muiTableHeadCellProps: { sx: {} },
  muiTableBodyProps: { sx: {} },
  muiTableBodyCellProps: { sx: {} },
  muiTableBodyRowProps: { sx: {} },
  muiTablePaginationProps: {},
  muiToolbarAlertBannerProps: {},
  muiFilterTextFieldProps: {},
  muiEditTextFieldProps: {},

  // Display column options
  displayColumnDefOptions: {
    'mrt-row-select': { size: 50 },
    'mrt-row-expand': { size: 60 },
    'mrt-row-numbers': { size: 50 },
    'mrt-row-actions': { size: 120 },
  },

  // Other options
  rowCount: 100, // For server-side pagination
  manualFiltering: false, // Server-side filtering
  manualPagination: false, // Server-side pagination
  manualSorting: false, // Server-side sorting
  positionActionsColumn: 'last', // 'first' | 'last'
  positionExpandColumn: 'first', // 'first' | 'last'
  positionGlobalFilter: 'left', // 'left' | 'right'
  positionPagination: 'bottom', // 'bottom' | 'top' | 'both'
  positionToolbarAlertBanner: 'top', // 'top' | 'bottom' | 'none'
  defaultColumn: {}, // Default column options
  localization: {}, // i18n strings
};

const table = useMaterialReactTable(tableOptions);
```

---

Material React Table provides a comprehensive solution for building feature-rich data tables in React applications. Its primary use cases include admin dashboards, data management interfaces, reporting tools, and any application requiring advanced table functionality. The library excels at CRUD operations, complex filtering and sorting, large dataset handling through virtualization, and data aggregation and grouping.

Integration patterns are flexible and straightforward. For state management, the library works seamlessly with React Query for server-side operations, supports external state management with useState or Redux, and includes built-in state management for simpler use cases. The component integrates naturally with Material UI's theming system, allowing consistent design across applications. For custom backends, the library supports both client-side and server-side pagination, filtering, and sorting through simple configuration flags. TypeScript support is first-class with full generic type inference, enabling type-safe column definitions and state management throughout the application.
