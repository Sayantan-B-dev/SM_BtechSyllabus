# Indexing Techniques

**Course:** Database Management Systems  
**Module:** 3 | **Lecture:** 1  
**Date:** 03-Sep-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## What is an Index?

An index is a data structure that improves the speed of data retrieval operations on a database table at the cost of additional storage space and slower writes. Think of it like the index at the back of a textbook: instead of scanning every page to find a topic, you look up the topic in the index and jump directly to the page number.

In database terms, an index on a column (or set of columns) maintains a mapping from the search-key value to the physical location of the record(s) containing that value.

### Why Use Indexes?

- Without an index, the DBMS must perform a **full table scan** (sequential read of every row) -- O(n) time.
- With an index, the DBMS can locate records in O(log n) or even O(1) time.
- Indexes are critical for large tables. For a table with 10^6 rows, a sequential scan might take seconds; an index reduces this to milliseconds.

### Cost of Indexes

- **Storage overhead:** The index itself occupies disk space.
- **Update overhead:** Every INSERT, DELETE, or UPDATE on the table may require updating the index -- slower writes.
- **Design decision:** Index columns that are frequently used in WHERE clauses, JOIN conditions, or ORDER BY. Avoid indexing columns with low cardinality (few distinct values).

---

## Ordered Indexes vs Hash Indexes

Indexes are broadly classified into two categories:

### 1. Ordered Index (Tree-based)

- Records are stored in sorted order of the search key (or the index references sorted keys).
- The index data structure is typically a balanced tree (B-tree or B+ tree).
- **Supports range queries:** `WHERE salary BETWEEN 50000 AND 70000` is efficient because keys are sorted.

### 2. Hash Index

- The search key is hashed to a bucket address.
- Excellent for **equality lookups**: `WHERE emp_id = 101` is O(1) average.
- **Does not support range queries:** Since keys are distributed randomly across buckets, a range scan requires scanning all buckets.

### Comparison Table

| Feature               | Ordered Index                     | Hash Index                        |
|-----------------------|-----------------------------------|-----------------------------------|
| Lookup by equality    | O(log n)                          | O(1) average                      |
| Range query           | Efficient (sorted order)          | Not supported (inefficient)       |
| Insert/Delete         | O(log n) (may rebalance tree)    | O(1) average (may overflow)      |
| Storage              | Moderate                          | Moderate                          |
| Use case             | General purpose, range queries    | Key-value lookups, data warehouse |

---

## Dense Index vs Sparse Index

### Dense Index

- An index entry exists for **every search-key value** in the table.
- Provides faster lookup (you always find the key in the index).
- Uses more storage.

```
Dense Index on emp_id (primary key):

Index File (dense):
  [101] --> record1
  [102] --> record2
  [103] --> record3
  [104] --> record4
  ...

Data File (unsorted or sorted):
  record1 (101, Alice, ...)
  record2 (102, Bob, ...)
  record3 (103, Carol, ...)
  ...
```

### Sparse Index

- An index entry is created only for **some** search-key values (e.g., one per page/block of data).
- The data file must be **sorted** on the search key.
- To find a record, scan the index to find the largest key <= the search value, then scan forward in the data file.
- Uses less storage but may require a short sequential scan.

```
Sparse Index on emp_id (data file sorted by emp_id):

Index File (sparse, one per data block):
  [101] --> block1
  [201] --> block2
  [301] --> block3

Data File (sorted, 3 records per block):
  Block 1: [101, Alice], [102, Bob], [103, Carol]
  Block 2: [201, Dave], [202, Eve], [203, Frank]
  Block 3: [301, Grace], [302, Heidi], [303, Ivan]
```

To find emp_id = 202:
1. Search index: largest key <= 202 is [201] --> block2.
2. Scan block2 sequentially: found (202, Eve).

### Comparison

| Feature        | Dense Index                     | Sparse Index                     |
|----------------|---------------------------------|----------------------------------|
| Entries        | One per search-key value        | One per data block               |
| Lookup speed   | Faster (direct)                 | Slower (may need block scan)     |
| Storage        | Larger                          | Smaller                          |
| Data file req  | Can be unsorted (if clustered)  | Must be sorted on search key     |
| Use case       | Small tables or frequent lookups| Large tables, fewer index blocks |

---

## Primary Index (Clustering Index)

- A **primary index** (also called **clustering index**) is an ordered index on the **primary key** of the table.
- The data file is **physically ordered** (clustered) in the same order as the index.
- There can be **at most one** primary/clustering index per table because data can be stored in only one physical order.

### Example

```sql
CREATE TABLE Employee (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    salary DECIMAL(10,2)
);

-- A primary index is automatically created on emp_id
-- In most DBMS, PRIMARY KEY creates a clustered index by default
```

**Visual representation:**

```
Primary Index (clustered, on emp_id):

Index:
  [101] --> block1
  [201] --> block2
  [301] --> block3

Data blocks (actually sorted like the index):
  block1: [101] [102] [103]
  block2: [201] [202] [203]
  block3: [301] [302] [303]
```

Since the data is sorted in the same order as the index, a sparse index can be used. The DBMS typically builds a sparse primary index with one entry per block of data records.

---

## Secondary Index (Non-clustering Index)

- A **secondary index** (also called **non-clustering index**) is an index on a non-primary key or on a column that is not the clustering key.
- The data file is **not** physically ordered by this search key.
- The index points to the records, but the records themselves may be scattered across disk blocks.
- Multiple secondary indexes can exist on the same table (unlike clustering index).

### Example

```sql
CREATE INDEX idx_salary ON Employee(salary);
```

**Visual representation:**

```
Secondary Index on salary:

Index (sorted by salary):
  [30000] --> record1, record4
  [40000] --> record2
  [50000] --> record3, record5

Data file (physically ordered by emp_id, NOT by salary):
  record1: emp_id=101, name=Alice, salary=30000
  record2: emp_id=102, name=Bob, salary=40000
  record3: emp_id=103, name=Carol, salary=50000
  record4: emp_id=104, name=Dave, salary=30000
  record5: emp_id=105, name=Eve, salary=50000
```

A secondary index is always **dense** (one pointer per record) because the data is not sorted by the search key, so you cannot rely on block-level ordering.

### Clustering vs Secondary: Summary

| Property          | Clustering Index (Primary)    | Secondary Index (Non-clustering) |
|-------------------|-------------------------------|----------------------------------|
| Data ordering     | Same as index order           | Independent of index order       |
| Max per table     | 1                             | Many                             |
| Index density     | Can be sparse                 | Always dense                     |
| Lookup speed      | Fast (few block accesses)     | May need multiple block accesses |
| Range query       | Excellent (sequential blocks) | Good (but random IO)             |

---

## Single-Level Index vs Multi-Level Index

### Single-Level Index

- The index file itself is stored as a single sorted file (or a B-tree of one level).
- For very large tables, the index file itself can be huge. Searching a large sorted index file still requires log2(N) block accesses.

### Multi-Level Index

- When the single-level index grows too large to fit in main memory, we treat the index file as a data file and build an index **on the index**.
- **Outer index** (top level): sparse index on the inner index.
- **Inner index** (bottom level): dense (or sparse) index on the data file.

```
Multi-Level Index (2 levels):

    Outer Index (sparse, on inner index blocks):
      [key_1] --> index_block_1
      [key_k] --> index_block_2
      ...

    Inner Index (dense/sparse, on data blocks):
      index_block_1: [101] --> data_block_1
      index_block_2: [201] --> data_block_2
      ...

    Data File:
      data_block_1: [101] [102] [103] ...
      data_block_2: [201] [202] [203] ...
```

This reduces the search time from O(log n) for a single-level index to O(log_m n) where m is the fan-out of each index node. In practice, B+ trees (Lecture 3) are the standard implementation of multi-level indexes.

---

## Trade-offs: Search Speed vs Update Cost vs Storage

| Aspect          | Trade-off Description                                                        |
|-----------------|------------------------------------------------------------------------------|
| **Search speed**| More indexes = faster reads (index seek vs full scan).                       |
| **Update cost** | More indexes = slower writes (must maintain every index on INSERT/UPDATE/DELETE). |
| **Storage**     | More indexes = more disk space. Dense indexes use more space than sparse.     |
| **Clustering**  | One clustered index is fast for range queries; secondary indexes add flexibility at the cost of space and slower writes. |

### Decision Guidelines

- **OLTP (many writes):** Keep indexes minimal. Cluster on the primary key.
- **OLAP / Reporting (many reads, complex queries):** Add indexes on columns used in WHERE, JOIN, GROUP BY, ORDER BY.
- **Composite indexes:** Index on (col1, col2) can speed up queries filtering on col1 or (col1, col2), but generally not queries filtering only on col2.
- **Cardinality:** Columns with high cardinality (many distinct values) benefit more from indexing than low-cardinality columns (e.g., a boolean column).

---

## CREATE INDEX in SQL

### Syntax

```sql
-- Basic syntax (non-clustered secondary index)
CREATE INDEX index_name
ON table_name (column1, column2, ...);

-- Unique index (enforces uniqueness)
CREATE UNIQUE INDEX index_name
ON table_name (column);

-- Clustered index (SQL Server syntax)
CREATE CLUSTERED INDEX index_name
ON table_name (column);

-- In PostgreSQL, CLUSTER command physically reorders the table
CLUSTER table_name USING index_name;

-- Drop an index
DROP INDEX index_name;
```

### Examples

```sql
-- Single-column secondary index
CREATE INDEX idx_emp_dept ON Employee(dept_id);

-- Composite index (multi-column)
CREATE INDEX idx_emp_name_dept ON Employee(last_name, dept_id);

-- Unique index on email
CREATE UNIQUE INDEX idx_unique_email ON Employee(email);

-- In PostgreSQL, create an index with a condition (partial index)
CREATE INDEX idx_high_salary ON Employee(salary)
WHERE salary > 100000;

-- In Oracle/PostgreSQL, create a hash index
CREATE INDEX idx_hash_emp ON Employee USING HASH(emp_id);
```

### How the DBMS Uses the Index

When you run:

```sql
SELECT * FROM Employee WHERE salary = 50000;
```

1. The query optimizer checks if an index on `salary` exists.
2. If yes, it uses the index to find the disk addresses of matching records.
3. It fetches only those records (instead of scanning the whole table).

You can verify index usage with `EXPLAIN`:

```sql
EXPLAIN SELECT * FROM Employee WHERE salary = 50000;
```

---

## Practice Problems

**Problem 1:** A table `Student(roll_no, name, age)` has 10,000 records stored in 500 blocks. You create a sparse primary index on `roll_no` with one entry per block. How many index entries are there? If each index entry is 10 bytes, what is the size of the index?

<details>
<summary>Answer</summary>

- Number of index entries = number of data blocks = 500.
- Index size = 500 * 10 bytes = 5000 bytes (approx 5 KB).
</details>

**Problem 2:** Consider the query `SELECT * FROM Orders WHERE order_date BETWEEN '2024-01-01' AND '2024-01-31'`. Would a hash index on `order_date` help? Explain.

<details>
<summary>Answer</summary>

No. A hash index supports only equality lookups, not range queries. For range queries, an ordered (B+ tree) index on `order_date` is required.
</details>

**Problem 3:** Why can a table have only one clustered (primary) index but multiple secondary indexes?

<details>
<summary>Answer</summary>

A clustered index determines the physical order of data records on disk. Since the data can be sorted in only one physical order at a time, only one clustered index is possible. Secondary indexes are separate data structures that point to records independently of the physical order, so any number can exist.
</details>

**Problem 4:** Given a dense index of size 2000 entries and a sparse index (one per 10 records) on the same table, which uses more storage? Which provides faster lookup for a single record?

<details>
<summary>Answer</summary>

- Dense index uses more storage (one entry per record).
- Dense index provides faster lookup (direct pointer vs needing to scan a block).
</details>

**Problem 5:** Write a SQL statement to create an index on the `email` column of a `Users` table such that duplicate emails are not allowed.

<details>
<summary>Answer</summary>

```sql
CREATE UNIQUE INDEX idx_unique_email ON Users(email);
```
</details>

---
