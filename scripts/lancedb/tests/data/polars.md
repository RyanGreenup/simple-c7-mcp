# Polars: High-Performance DataFrame Library

Polars is a blazingly fast DataFrame library implemented in Rust, designed for high-performance data manipulation and analysis. Built on Apache Arrow's columnar memory format, Polars provides both eager and lazy execution engines with automatic query optimization, multi-threaded operations, and SIMD acceleration. The library is designed to handle datasets ranging from small in-memory workloads to larger-than-RAM streaming operations.

The project is structured as a Rust workspace (edition 2024) with 25 specialized crates, including core data structures (polars-core), lazy query engine (polars-lazy), I/O operations (polars-io, polars-parquet), and execution engines (polars-mem-engine, polars-stream). Language bindings are available for Python, Rust, Node.js, and R, with Python bindings implemented via PyO3. Polars supports multiple file formats (CSV, Parquet, JSON, Excel, Avro) and integrates seamlessly with the Arrow ecosystem for zero-copy data exchange.

## Core APIs and Functions

### Reading CSV Files

Read CSV files into DataFrames with automatic type inference and flexible parsing options.

```python
import polars as pl

# Eager reading - loads entire file into memory
df = pl.read_csv(
    "data/sales.csv",
    has_header=True,
    columns=["date", "product", "quantity", "price"],
    dtypes={"product": pl.Categorical, "quantity": pl.Int32},
    try_parse_dates=True
)
print(df)

# Lazy reading - defers execution for optimization
lf = pl.scan_csv("data/sales.csv")
result = lf.filter(pl.col("quantity") > 10).collect()
print(result)

# Output:
# shape: (3, 4)
# ┌────────────┬─────────┬──────────┬───────┐
# │ date       ┆ product ┆ quantity ┆ price │
# │ ---        ┆ ---     ┆ ---      ┆ ---   │
# │ date       ┆ cat     ┆ i32      ┆ f64   │
# ╞════════════╪═════════╪══════════╪═══════╡
# │ 2024-01-15 ┆ Widget  ┆ 15       ┆ 29.99 │
# │ 2024-01-16 ┆ Gadget  ┆ 12       ┆ 49.99 │
# │ 2024-01-17 ┆ Widget  ┆ 20       ┆ 29.99 │
# └────────────┴─────────┴──────────┴───────┘
```

### Reading and Writing Parquet Files

Work with Parquet files for efficient columnar storage with compression.

```python
import polars as pl

# Write DataFrame to Parquet
df = pl.DataFrame({
    "id": [1, 2, 3, 4],
    "name": ["Alice", "Bob", "Charlie", "David"],
    "score": [95.5, 87.2, 92.8, 78.9]
})
df.write_parquet("output.parquet", compression="snappy")

# Read Parquet file (eager)
df_read = pl.read_parquet("output.parquet")

# Scan Parquet file (lazy) with predicate pushdown
lf = pl.scan_parquet("output.parquet")
result = (
    lf.filter(pl.col("score") > 90)
    .select(["name", "score"])
    .collect()
)
print(result)

# Output:
# shape: (2, 2)
# ┌─────────┬───────┐
# │ name    ┆ score │
# │ ---     ┆ ---   │
# │ str     ┆ f64   │
# ╞═════════╪═══════╡
# │ Alice   ┆ 95.5  │
# │ Charlie ┆ 92.8  │
# └─────────┴───────┘
```

### DataFrame Creation and Basic Operations

Create DataFrames from various sources and perform fundamental data operations.

```python
import polars as pl
import datetime as dt

# Create DataFrame from dictionary
df = pl.DataFrame({
    "name": ["Alice Archer", "Ben Brown", "Chloe Cooper", "Daniel Donovan"],
    "birthdate": [
        dt.date(1997, 1, 10),
        dt.date(1985, 2, 15),
        dt.date(1983, 3, 22),
        dt.date(1981, 4, 30),
    ],
    "weight": [57.9, 72.5, 53.6, 83.1],  # kg
    "height": [1.56, 1.77, 1.65, 1.75],  # meters
})

# Select columns with transformations
result = df.select(
    pl.col("name"),
    pl.col("birthdate").dt.year().alias("birth_year"),
    (pl.col("weight") / (pl.col("height") ** 2)).alias("bmi"),
)
print(result)

# Output:
# shape: (4, 3)
# ┌─────────────────┬────────────┬───────┐
# │ name            ┆ birth_year ┆ bmi   │
# │ ---             ┆ ---        ┆ ---   │
# │ str             ┆ i32        ┆ f64   │
# ╞═════════════════╪════════════╪═══════╡
# │ Alice Archer    ┆ 1997       ┆ 23.79 │
# │ Ben Brown       ┆ 1985       ┆ 23.14 │
# │ Chloe Cooper    ┆ 1983       ┆ 19.69 │
# │ Daniel Donovan  ┆ 1981       ┆ 27.13 │
# └─────────────────┴────────────┴───────┘
```

### Filtering DataFrames

Filter rows based on conditions using expressive boolean expressions.

```python
import polars as pl
import datetime as dt

df = pl.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "birthdate": [
        dt.date(1997, 5, 10),
        dt.date(1985, 8, 15),
        dt.date(1990, 3, 22),
        dt.date(1988, 12, 1),
    ],
    "height": [1.65, 1.80, 1.72, 1.68],
})

# Single condition
result = df.filter(pl.col("birthdate").dt.year() < 1990)
print(result)

# Multiple conditions
result = df.filter(
    pl.col("birthdate").is_between(dt.date(1982, 12, 31), dt.date(1996, 1, 1)),
    pl.col("height") > 1.7,
)
print(result)

# Output:
# shape: (1, 3)
# ┌─────┬────────────┬────────┐
# │ name ┆ birthdate  ┆ height │
# │ ---  ┆ ---        ┆ ---    │
# │ str  ┆ date       ┆ f64    │
# ╞══════╪════════════╪════════╡
# │ Bob  ┆ 1985-08-15 ┆ 1.8    │
# └──────┴────────────┴────────┘
```

### Adding and Modifying Columns

Add new columns or modify existing ones using with_columns.

```python
import polars as pl
import datetime as dt

df = pl.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "birthdate": [dt.date(1997, 1, 10), dt.date(1985, 2, 15), dt.date(1983, 3, 22)],
    "weight": [57.9, 72.5, 83.1],
    "height": [1.56, 1.77, 1.75],
})

# Add multiple columns
result = df.with_columns(
    birth_year=pl.col("birthdate").dt.year(),
    bmi=(pl.col("weight") / (pl.col("height") ** 2)).round(2),
    age=2024 - pl.col("birthdate").dt.year(),
)
print(result)

# Expression expansion with name suffix
result = df.with_columns(
    (pl.col("weight", "height") * 0.95).round(2).name.suffix("_reduced")
)
print(result)

# Output:
# shape: (3, 7)
# ┌─────────┬────────────┬────────┬────────┬────────────┬──────┬─────┐
# │ name    ┆ birthdate  ┆ weight ┆ height ┆ birth_year ┆ bmi  ┆ age │
# │ ---     ┆ ---        ┆ ---    ┆ ---    ┆ ---        ┆ ---  ┆ --- │
# │ str     ┆ date       ┆ f64    ┆ f64    ┆ i32        ┆ f64  ┆ i32 │
# ╞═════════╪════════════╪════════╪════════╪════════════╪══════╪═════╡
# │ Alice   ┆ 1997-01-10 ┆ 57.9   ┆ 1.56   ┆ 1997       ┆23.79 ┆ 27  │
# │ Bob     ┆ 1985-02-15 ┆ 72.5   ┆ 1.77   ┆ 1985       ┆23.14 ┆ 39  │
# │ Charlie ┆ 1983-03-22 ┆ 83.1   ┆ 1.75   ┆ 1983       ┆27.13 ┆ 41  │
# └─────────┴────────────┴────────┴────────┴────────────┴──────┴─────┘
```

### GroupBy Aggregations

Group data and compute aggregate statistics across groups.

```python
import polars as pl
import datetime as dt

df = pl.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "birthdate": [
        dt.date(1997, 1, 10),
        dt.date(1985, 2, 15),
        dt.date(1983, 3, 22),
        dt.date(1991, 4, 30),
        dt.date(1979, 5, 12),
    ],
    "weight": [57.9, 72.5, 83.1, 65.2, 70.8],
    "height": [1.56, 1.77, 1.75, 1.68, 1.71],
})

# Group by decade with aggregations
result = df.group_by(
    (pl.col("birthdate").dt.year() // 10 * 10).alias("decade"),
    maintain_order=True,
).agg(
    pl.len().alias("sample_size"),
    pl.col("weight").mean().round(2).alias("avg_weight"),
    pl.col("height").max().alias("tallest"),
)
print(result)

# Output:
# shape: (3, 4)
# ┌────────┬─────────────┬────────────┬──────────┐
# │ decade ┆ sample_size ┆ avg_weight ┆ tallest  │
# │ ---    ┆ ---         ┆ ---        ┆ ---      │
# │ i32    ┆ u32         ┆ f64        ┆ f64      │
# ╞════════╪═════════════╪════════════╪══════════╡
# │ 1970   ┆ 1           ┆ 70.8       ┆ 1.71     │
# │ 1980   ┆ 2           ┆ 77.8       ┆ 1.77     │
# │ 1990   ┆ 2           ┆ 61.55      ┆ 1.68     │
# └────────┴─────────────┴────────────┴──────────┘
```

### Lazy Execution with Query Optimization

Build query plans that are optimized and executed only when collect() is called.

```python
import polars as pl

# Lazy scan with chained operations
q = (
    pl.scan_csv("docs/assets/data/iris.csv")
    .filter(pl.col("sepal_length") > 5)
    .group_by("species")
    .agg(pl.all().sum())
)

# View optimized query plan
print(q.explain(optimized=True))

# Execute the query
df = q.collect()
print(df)

# Streaming execution for larger-than-RAM datasets
df_streaming = q.collect(engine="streaming")

# Output shows optimized plan with predicate pushdown:
# FILTER [(col("sepal_length")) > (5)] FROM CSV SCAN docs/assets/data/iris.csv
#   PROJECT */6 COLUMNS
#   AGGREGATE
#     [col("sepal_length").sum(), col("sepal_width").sum(), ...]
#     BY
#     [col("species")] FROM
```

### Conditional Expressions with when-then-otherwise

Create conditional logic within expressions using when-then chains.

```python
import polars as pl

df = pl.DataFrame({
    "product": ["Widget", "Gadget", "Doohickey", "Thingamajig"],
    "quantity": [10, 25, 5, 50],
    "price": [29.99, 49.99, 19.99, 39.99],
})

# Conditional column creation
result = df.with_columns(
    pl.when(pl.col("quantity") < 10)
    .then(pl.lit("Low Stock"))
    .when(pl.col("quantity") < 30)
    .then(pl.lit("Medium Stock"))
    .otherwise(pl.lit("High Stock"))
    .alias("stock_level"),

    pl.when(pl.col("price") < 25)
    .then(pl.col("price") * 0.9)  # 10% discount
    .when(pl.col("price") < 40)
    .then(pl.col("price") * 0.95)  # 5% discount
    .otherwise(pl.col("price"))
    .alias("discounted_price"),
)
print(result)

# Output:
# shape: (4, 5)
# ┌──────────────┬──────────┬───────┬──────────────┬──────────────────┐
# │ product      ┆ quantity ┆ price ┆ stock_level  ┆ discounted_price │
# │ ---          ┆ ---      ┆ ---   ┆ ---          ┆ ---              │
# │ str          ┆ i64      ┆ f64   ┆ str          ┆ f64              │
# ╞══════════════╪══════════╪═══════╪══════════════╪══════════════════╡
# │ Widget       ┆ 10       ┆ 29.99 ┆ Medium Stock ┆ 28.49            │
# │ Gadget       ┆ 25       ┆ 49.99 ┆ Medium Stock ┆ 49.99            │
# │ Doohickey    ┆ 5        ┆ 19.99 ┆ Low Stock    ┆ 17.99            │
# │ Thingamajig  ┆ 50       ┆ 39.99 ┆ High Stock   ┆ 37.99            │
# └──────────────┴──────────┴───────┴──────────────┴──────────────────┘
```

### Joining DataFrames

Combine DataFrames using various join strategies (inner, left, outer, cross).

```python
import polars as pl

df_customers = pl.DataFrame({
    "customer_id": [1, 2, 3, 4],
    "name": ["Alice", "Bob", "Charlie", "Diana"],
})

df_orders = pl.DataFrame({
    "order_id": [101, 102, 103, 104],
    "customer_id": [1, 1, 3, 5],
    "amount": [250.00, 175.50, 420.25, 99.99],
})

# Left join
result = df_customers.join(df_orders, on="customer_id", how="left")
print(result)

# Inner join with multiple keys
df_products = pl.DataFrame({
    "order_id": [101, 102, 103],
    "product": ["Widget", "Gadget", "Widget"],
})

result = df_orders.join(
    df_products,
    on="order_id",
    how="inner"
).join(
    df_customers,
    on="customer_id",
    how="left"
)
print(result)

# Output:
# shape: (5, 4)
# ┌─────────────┬─────────┬──────────┬────────┐
# │ customer_id ┆ name    ┆ order_id ┆ amount │
# │ ---         ┆ ---     ┆ ---      ┆ ---    │
# │ i64         ┆ str     ┆ i64      ┆ f64    │
# ╞═════════════╪═════════╪══════════╪════════╡
# │ 1           ┆ Alice   ┆ 101      ┆ 250.0  │
# │ 1           ┆ Alice   ┆ 102      ┆ 175.5  │
# │ 2           ┆ Bob     ┆ null     ┆ null   │
# │ 3           ┆ Charlie ┆ 103      ┆ 420.25 │
# │ 4           ┆ Diana   ┆ null     ┆ null   │
# └─────────────┴─────────┴──────────┴────────┘
```

### Concatenating DataFrames

Combine multiple DataFrames vertically or horizontally.

```python
import polars as pl
import datetime as dt

df1 = pl.DataFrame({
    "name": ["Alice", "Bob"],
    "age": [25, 30],
    "city": ["New York", "London"],
})

df2 = pl.DataFrame({
    "name": ["Charlie", "Diana"],
    "age": [35, 28],
    "city": ["Tokyo", "Paris"],
})

# Vertical concatenation (stack rows)
result = pl.concat([df1, df2], how="vertical")
print(result)

# Horizontal concatenation (side by side)
df_scores = pl.DataFrame({
    "math_score": [95, 87],
    "english_score": [88, 92],
})

result = pl.concat([df1, df_scores], how="horizontal")
print(result)

# Output (vertical):
# shape: (4, 3)
# ┌─────────┬─────┬──────────┐
# │ name    ┆ age ┆ city     │
# │ ---     ┆ --- ┆ ---      │
# │ str     ┆ i64 ┆ str      │
# ╞═════════╪═════╪══════════╡
# │ Alice   ┆ 25  ┆ New York │
# │ Bob     ┆ 30  ┆ London   │
# │ Charlie ┆ 35  ┆ Tokyo    │
# │ Diana   ┆ 28  ┆ Paris    │
# └─────────┴─────┴──────────┘
```

### String Operations

Perform string manipulations using the str namespace.

```python
import polars as pl

df = pl.DataFrame({
    "name": ["Alice Archer", "Bob Brown", "Chloe Cooper"],
    "email": ["alice@example.com", "bob@example.com", "chloe@example.com"],
})

# String operations
result = df.with_columns(
    first_name=pl.col("name").str.split(by=" ").list.first(),
    last_name=pl.col("name").str.split(by=" ").list.last(),
    username=pl.col("email").str.split(by="@").list.first(),
    email_upper=pl.col("email").str.to_uppercase(),
    name_length=pl.col("name").str.len_chars(),
)
print(result)

# Pattern matching
result = df.filter(pl.col("name").str.contains("^[AB]"))
print(result)

# Output:
# shape: (3, 7)
# ┌──────────────┬────────────────────┬────────────┬───────────┬──────────┬─────────────────┬─────────────┐
# │ name         ┆ email              ┆ first_name ┆ last_name ┆ username ┆ email_upper     ┆ name_length │
# │ ---          ┆ ---                ┆ ---        ┆ ---       ┆ ---      ┆ ---             ┆ ---         │
# │ str          ┆ str                ┆ str        ┆ str       ┆ str      ┆ str             ┆ u32         │
# ╞══════════════╪════════════════════╪════════════╪═══════════╪══════════╪═════════════════╪═════════════╡
# │ Alice Archer ┆ alice@example.com  ┆ Alice      ┆ Archer    ┆ alice    ┆ ALICE@EXAMPLE...┆ 12          │
# │ Bob Brown    ┆ bob@example.com    ┆ Bob        ┆ Brown     ┆ bob      ┆ BOB@EXAMPLE.COM ┆ 9           │
# │ Chloe Cooper ┆ chloe@example.com  ┆ Chloe      ┆ Cooper    ┆ chloe    ┆ CHLOE@EXAMPLE...┆ 12          │
# └──────────────┴────────────────────┴────────────┴───────────┴──────────┴─────────────────┴─────────────┘
```

### Working with Lists and Arrays

Manipulate list columns with operations like explode, slice, and aggregations.

```python
import polars as pl

df = pl.DataFrame({
    "student": ["Alice", "Bob", "Charlie"],
    "test_scores": [[85, 90, 88], [92, 87, 95], [78, 82, 80]],
    "subjects": [["Math", "Science", "English"], ["Math", "Science", "English"], ["Math", "Science", "English"]],
})

# List operations
result = df.with_columns(
    avg_score=pl.col("test_scores").list.mean(),
    max_score=pl.col("test_scores").list.max(),
    num_tests=pl.col("test_scores").list.len(),
    first_score=pl.col("test_scores").list.first(),
)
print(result)

# Explode lists into rows
result = df.explode("test_scores", "subjects")
print(result)

# Output (with aggregations):
# shape: (3, 7)
# ┌─────────┬───────────────┬─────────────────────┬───────────┬───────────┬───────────┬─────────────┐
# │ student ┆ test_scores   ┆ subjects            ┆ avg_score ┆ max_score ┆ num_tests ┆ first_score │
# │ ---     ┆ ---           ┆ ---                 ┆ ---       ┆ ---       ┆ ---       ┆ ---         │
# │ str     ┆ list[i64]     ┆ list[str]           ┆ f64       ┆ i64       ┆ u32       ┆ i64         │
# ╞═════════╪═══════════════╪═════════════════════╪═══════════╪═══════════╪═══════════╪═════════════╡
# │ Alice   ┆ [85, 90, 88]  ┆ ["Math", "Science"..┆ 87.67     ┆ 90        ┆ 3         ┆ 85          │
# │ Bob     ┆ [92, 87, 95]  ┆ ["Math", "Science"..┆ 91.33     ┆ 95        ┆ 3         ┆ 92          │
# │ Charlie ┆ [78, 82, 80]  ┆ ["Math", "Science"..┆ 80.0      ┆ 82        ┆ 3         ┆ 78          │
# └─────────┴───────────────┴─────────────────────┴───────────┴───────────┴───────────┴─────────────┘
```

### Date and Time Operations

Work with temporal data using the dt namespace for date/datetime columns.

```python
import polars as pl
import datetime as dt

df = pl.DataFrame({
    "event": ["Meeting", "Conference", "Workshop", "Seminar"],
    "timestamp": [
        dt.datetime(2024, 1, 15, 10, 30),
        dt.datetime(2024, 3, 22, 14, 0),
        dt.datetime(2024, 6, 10, 9, 15),
        dt.datetime(2024, 9, 5, 16, 45),
    ],
})

# Date/time extractions and transformations
result = df.with_columns(
    date=pl.col("timestamp").dt.date(),
    year=pl.col("timestamp").dt.year(),
    month=pl.col("timestamp").dt.month(),
    day_of_week=pl.col("timestamp").dt.weekday(),
    hour=pl.col("timestamp").dt.hour(),
    quarter=pl.col("timestamp").dt.quarter(),
    days_until_event=(pl.col("timestamp") - dt.datetime.now()).dt.total_days(),
)
print(result)

# Date arithmetic
result = df.with_columns(
    one_week_later=pl.col("timestamp") + pl.duration(weeks=1),
    two_months_ago=pl.col("timestamp") - pl.duration(months=2),
)
print(result)

# Output:
# shape: (4, 8)
# ┌───────────┬─────────────────────┬────────────┬──────┬───────┬─────────────┬──────┬─────────┐
# │ event     ┆ timestamp           ┆ date       ┆ year ┆ month ┆ day_of_week ┆ hour ┆ quarter │
# │ ---       ┆ ---                 ┆ ---        ┆ ---  ┆ ---   ┆ ---         ┆ ---  ┆ ---     │
# │ str       ┆ datetime[μs]        ┆ date       ┆ i32  ┆ i8    ┆ i8          ┆ i8   ┆ i8      │
# ╞═══════════╪═════════════════════╪════════════╪══════╪═══════╪═════════════╪══════╪═════════╡
# │ Meeting   ┆ 2024-01-15 10:30:00 ┆ 2024-01-15 ┆ 2024 ┆ 1     ┆ 1           ┆ 10   ┆ 1       │
# │ Conference┆ 2024-03-22 14:00:00 ┆ 2024-03-22 ┆ 2024 ┆ 3     ┆ 5           ┆ 14   ┆ 1       │
# │ Workshop  ┆ 2024-06-10 09:15:00 ┆ 2024-06-10 ┆ 2024 ┆ 6     ┆ 1           ┆ 9    ┆ 2       │
# │ Seminar   ┆ 2024-09-05 16:45:00 ┆ 2024-09-05 ┆ 2024 ┆ 9     ┆ 4           ┆ 16   ┆ 3       │
# └───────────┴─────────────────────┴────────────┴──────┴───────┴─────────────┴──────┴─────────┘
```

### Handling Missing Data

Fill, drop, or interpolate null values using various strategies.

```python
import polars as pl

df = pl.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "value_a": [10, None, 30, None, 50],
    "value_b": [None, 20, 30, 40, None],
})

# Fill null with literal value
result = df.with_columns(
    pl.col("value_a").fill_null(0),
    pl.col("value_b").fill_null(-1),
)
print(result)

# Fill null with forward fill strategy
result = df.with_columns(
    pl.col("value_a").fill_null(strategy="forward"),
    pl.col("value_b").fill_null(strategy="backward"),
)
print(result)

# Drop rows with any null
result = df.drop_nulls()
print(result)

# Filter for non-null values
result = df.filter(pl.col("value_a").is_not_null())
print(result)

# Output (forward/backward fill):
# shape: (5, 3)
# ┌─────┬─────────┬─────────┐
# │ id  ┆ value_a ┆ value_b │
# │ --- ┆ ---     ┆ ---     │
# │ i64 ┆ i64     ┆ i64     │
# ╞═════╪═════════╪═════════╡
# │ 1   ┆ 10      ┆ 20      │
# │ 2   ┆ 10      ┆ 20      │
# │ 3   ┆ 30      ┆ 30      │
# │ 4   ┆ 30      ┆ 40      │
# │ 5   ┆ 50      ┆ null    │
# └─────┴─────────┴─────────┘
```

### SQL Query Interface

Execute SQL queries directly on DataFrames using the SQL context.

```python
import polars as pl

df_customers = pl.DataFrame({
    "customer_id": [1, 2, 3, 4],
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "city": ["New York", "London", "Tokyo", "Paris"],
})

df_orders = pl.DataFrame({
    "order_id": [101, 102, 103, 104],
    "customer_id": [1, 1, 3, 2],
    "amount": [250.00, 175.50, 420.25, 99.99],
})

# Create SQL context and register tables
ctx = pl.SQLContext(customers=df_customers, orders=df_orders)

# Execute SQL query
result = ctx.execute("""
    SELECT
        c.name,
        c.city,
        COUNT(o.order_id) as order_count,
        SUM(o.amount) as total_spent
    FROM customers c
    LEFT JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY c.name, c.city
    ORDER BY total_spent DESC
""").collect()
print(result)

# Output:
# shape: (4, 4)
# ┌─────────┬──────────┬─────────────┬─────────────┐
# │ name    ┆ city     ┆ order_count ┆ total_spent │
# │ ---     ┆ ---      ┆ ---         ┆ ---         │
# │ str     ┆ str      ┆ u32         ┆ f64         │
# ╞═════════╪══════════╪═════════════╪═════════════╡
# │ Alice   ┆ New York ┆ 2           ┆ 425.5       │
# │ Charlie ┆ Tokyo    ┆ 1           ┆ 420.25      │
# │ Bob     ┆ London   ┆ 1           ┆ 99.99       │
# │ Diana   ┆ Paris    ┆ 0           ┆ null        │
# └─────────┴──────────┴─────────────┴─────────────┘
```

### Rust API: Lazy DataFrame Operations

Build and execute optimized query plans using the Rust API.

```rust
use polars::prelude::*;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Scan CSV with lazy evaluation
    let q = LazyCsvReader::new(PlPath::new("data/iris.csv"))
        .with_has_header(true)
        .finish()?
        .filter(col("sepal_length").gt(lit(5)))
        .group_by(vec![col("species")])
        .agg([col("*").sum()]);

    // View optimized plan
    println!("{}", q.explain(true)?);

    // Execute query
    let df = q.collect()?;
    println!("{}", df);

    Ok(())
}

// Output shows optimized execution plan:
// Csv SCAN data/iris.csv
// PROJECT */5 COLUMNS
// SELECTION: [(col("sepal_length")) > (5.0)]
//   AGGREGATE
//     [col("sepal_length").sum(), col("sepal_width").sum(), ...]
//     BY [col("species")]
```

### Rust API: Eager vs Lazy Execution

Compare eager (immediate) and lazy (optimized) execution patterns.

```rust
use polars::prelude::*;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Eager execution - immediate operations
    let df = CsvReadOptions::default()
        .try_into_reader_with_file_path(Some("data/iris.csv".into()))
        .unwrap()
        .finish()
        .unwrap();

    let mask = df.column("sepal_length")?.f64()?.gt(5.0);
    let df_small = df.filter(&mask)?;
    let df_agg = df_small
        .group_by(["species"])?
        .select(["sepal_width"])
        .mean()?;
    println!("{}", df_agg);

    // Lazy execution - builds query plan first
    let q = LazyCsvReader::new(PlPath::new("data/iris.csv"))
        .with_has_header(true)
        .finish()?
        .filter(col("sepal_length").gt(lit(5)))
        .group_by(vec![col("species")])
        .agg([col("sepal_width").mean()]);

    // Optimize and execute
    let df = q.collect()?;
    println!("{}", df);

    Ok(())
}

// Lazy execution enables:
// - Predicate pushdown (filter before reading full data)
// - Projection pushdown (read only needed columns)
// - Query optimization (reorder operations)
// - Parallel execution planning
```

### Window Functions

Perform calculations across rows related to the current row using window operations.

```python
import polars as pl

df = pl.DataFrame({
    "product": ["Widget", "Widget", "Gadget", "Gadget", "Widget"],
    "date": ["2024-01-01", "2024-01-02", "2024-01-01", "2024-01-02", "2024-01-03"],
    "sales": [100, 150, 200, 180, 120],
})

# Window functions
result = df.with_columns(
    cumulative_sales=pl.col("sales").cum_sum().over("product"),
    avg_sales=pl.col("sales").mean().over("product"),
    rank=pl.col("sales").rank().over("product"),
    row_number=pl.int_range(pl.len()).over("product"),
)
print(result)

# Output:
# shape: (5, 7)
# ┌─────────┬────────────┬───────┬──────────────────┬───────────┬──────┬────────────┐
# │ product ┆ date       ┆ sales ┆ cumulative_sales ┆ avg_sales ┆ rank ┆ row_number │
# │ ---     ┆ ---        ┆ ---   ┆ ---              ┆ ---       ┆ ---  ┆ ---        │
# │ str     ┆ str        ┆ i64   ┆ i64              ┆ f64       ┆ u32  ┆ i64        │
# ╞═════════╪════════════╪═══════╪══════════════════╪═══════════╪══════╪════════════╡
# │ Widget  ┆ 2024-01-01 ┆ 100   ┆ 100              ┆ 123.33    ┆ 1    ┆ 0          │
# │ Widget  ┆ 2024-01-02 ┆ 150   ┆ 250              ┆ 123.33    ┆ 3    ┆ 1          │
# │ Gadget  ┆ 2024-01-01 ┆ 200   ┆ 200              ┆ 190.0     ┆ 2    ┆ 0          │
# │ Gadget  ┆ 2024-01-02 ┆ 180   ┆ 380              ┆ 190.0     ┆ 1    ┆ 1          │
# │ Widget  ┆ 2024-01-03 ┆ 120   ┆ 370              ┆ 123.33    ┆ 2    ┆ 2          │
# └─────────┴────────────┴───────┴──────────────────┴───────────┴──────┴────────────┘
```

## Integration Patterns and Use Cases

Polars excels in analytical workflows requiring high-performance data manipulation, from exploratory data analysis to production ETL pipelines. The lazy execution engine with automatic query optimization makes it ideal for processing large datasets efficiently, while the streaming mode enables working with datasets that exceed available memory. Polars integrates seamlessly with the Python data science ecosystem through zero-copy Arrow conversions with pandas, NumPy, and PyArrow, allowing easy adoption in existing workflows. The library's support for multiple file formats (CSV, Parquet, JSON, Excel) and cloud storage (S3, Azure, GCS) makes it versatile for various data sources.

Common use cases include data cleaning and transformation pipelines, time-series analysis, real-time data processing, and financial analytics. The expression API enables complex transformations with minimal code, while the SQL interface provides a familiar query language for database users. For production environments, Polars can be compiled from Rust source for maximum performance, and Python wheels are available with optional dependencies for extended functionality (connectorx for databases, fsspec for cloud storage, timezone support, Excel readers). The library's Python bindings maintain API compatibility while leveraging Rust's performance, making it an excellent choice for replacing pandas in performance-critical applications or building new data-intensive systems from scratch.
