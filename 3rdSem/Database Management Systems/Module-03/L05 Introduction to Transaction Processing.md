# Introduction to Transaction Processing

**Course:** Database Management Systems  
**Module:** 3 | **Lecture:** 5  
**Date:** 15-Sep-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## What is a Transaction?

A **transaction** is a logical unit of work that comprises one or more database operations (read, write, insert, delete, update). It represents a single, indivisible unit of work from the user's perspective.

### Formal Definition

A transaction is a collection of operations that forms a **single logical unit of work** on the database. The transaction must be executed completely or not at all.

### Real-World Analogy

Consider a fund transfer from account A to account B:

```
Operation 1: Read balance of A.
Operation 2: Subtract 500 from A's balance.
Operation 3: Write new balance of A.
Operation 4: Read balance of B.
Operation 5: Add 500 to B's balance.
Operation 6: Write new balance of B.
```

These six operations form a single transaction. If the system crashes after step 3 but before step 6, the money is lost (debited from A but not credited to B). The transaction must be **atomic** -- either all steps execute, or none do.

---

## ACID Properties (Introduction)

ACID is an acronym for the four properties that guarantee reliable transaction processing:

| Property      | Meaning                                                       |
|---------------|---------------------------------------------------------------|
| **A**tomicity | All operations of a transaction complete successfully, or none do. "All or nothing." |
| **C**onsistency| The transaction brings the database from one valid state to another valid state. All integrity constraints are preserved. |
| **I**solation | Concurrent transactions execute as if they were serial (one after another). Each transaction sees a consistent state. |
| **D**urability| Once a transaction commits, its changes persist even after a system failure. |

These properties are covered in depth in Lecture 6. Here we provide the basic intuition.

---

## Transaction States

A transaction passes through several states during its execution:

### State Diagram (ASCII)

```
                 +--------+
                 | ACTIVE |
                 +--------+
                  |      |
         (error)  |      |  (success)
                  v      |
            +----------+  |
            | FAILED   |  |
            +----------+  |
                  |       v
                  |   +----------------+
                  |   | PARTIALLY      |
                  |   | COMMITTED      |
                  |   +----------------+
                  |         |
                  |         | (write to disk)
                  |         v
                  |   +-----------+
                  |   | COMMITTED |
                  |   +-----------+
                  v
            +-----------+
            | ABORTED   |
            +-----------+
```

### State Descriptions

1. **ACTIVE:** Initial state. The transaction is executing its read/write operations. It stays in this state for most of its lifetime.

2. **PARTIALLY COMMITTED:** After the final operation of the transaction has been executed. The transaction has done all its work in memory (buffers), but the changes may not yet be written to disk. The system checks if the transaction can be committed without violating consistency.

3. **COMMITTED:** The transaction has successfully completed. All its changes are now permanently written to the database (on disk). The transaction can never be undone after this point.

4. **FAILED:** An error occurred during execution (e.g., constraint violation, system error, deadlock). The transaction can no longer proceed normally. It must be rolled back.

5. **ABORTED:** The transaction has been rolled back to undo all its changes. The database is restored to the state it was in before the transaction started. The transaction may be restarted later or terminated.

6. **TERMINATED:** The transaction has either committed or aborted. It has left the system. This is not always shown as a separate state but is the final outcome.

### State Transitions

| Transition | From               | To                 | Cause                                    |
|------------|---------------------|--------------------|------------------------------------------|
| Begin      | (none)              | ACTIVE             | Transaction started by user or program.  |
| Read/Write | ACTIVE              | ACTIVE             | Normal operation.                        |
| End        | ACTIVE              | PARTIALLY COMMITTED| Final operation executed.                |
| Commit     | PARTIALLY COMMITTED | COMMITTED          | All changes safely written to disk.      |
| Abort (1)  | ACTIVE              | FAILED             | Error during execution.                  |
| Abort (2)  | PARTIALLY COMMITTED | FAILED             | Could not commit (e.g., disk write fails).|
| Rollback   | FAILED              | ABORTED            | Changes undone by recovery manager.      |

---

## Read and Write Operations

The fundamental operations that a transaction performs are:

### Read Operation (read(X))

- Reads the value of database item `X` into a local buffer variable.
- If `X` is not already in main memory, it is brought in from disk.
- The operation does not modify the database.

```
read(X):
  if X is in buffer then
    local_var = buffer[X]
  else
    buffer[X] = disk_read(X)
    local_var = buffer[X]
```

### Write Operation (write(X))

- Writes the value from a local buffer variable to `X` in the database.
- The operation modifies the database (or at least the buffer, which will eventually be flushed to disk).

```
write(X):
  buffer[X] = local_var    // update buffer
  // eventually: disk_write(buffer[X])   // flush to disk
```

### Input and Output Operations

For our discussions, we model the interaction between main memory buffers and disk:

- **input(X):** Reads the block containing X from disk to main memory buffer.
- **output(X):** Writes the block containing X from buffer to disk.

---

## Transaction Example: Fund Transfer

Consider a transaction `T` that transfers $500 from account A to account B.

```
Initial state: A = 1000, B = 2000

T1: read(A);       // A = 1000 (in local variable)
T2: A := A - 500;  // A = 500 (in local variable)
T3: write(A);      // buffer[A] = 500
T4: read(B);       // B = 2000 (in local variable)
T5: B := B + 500;  // B = 2500 (in local variable)
T6: write(B);      // buffer[B] = 2500
```

### Step-by-Step Execution

```
Step  | Action                    | Buffer A | Buffer B | Disk A | Disk B
------|---------------------------|----------|----------|--------|--------
Start |                           | -        | -        | 1000   | 2000
1     | input(A), read(A)        | 1000     | -        | 1000   | 2000
2     | A := A - 500             | 500      | -        | 1000   | 2000
3     | write(A) [buffer update] | 500      | -        | 1000   | 2000
4     | input(B), read(B)        | 500      | 2000     | 1000   | 2000
5     | B := B + 500             | 500      | 2500     | 1000   | 2000
6     | write(B) [buffer update] | 500      | 2500     | 1000   | 2000
7     | output(A), output(B)     | 500      | 2500     | 500    | 2500
      | (COMMIT -- flush to disk)|          |          |        |
```

### What Could Go Wrong?

**Scenario 1:** System crash after Step 3 (write(A)) but before Step 7 (output).

- Disk: A = 1000 (old), B = 2000 (old).
- Buffer: A = 500, B = 2500.
- After crash, buffers are lost. Disk still has A = 1000, B = 2000.
- The transfer is lost, but database is consistent (no partial update visible).
- **Atomicity ensures** that either all changes are reflected, or none are.

**Scenario 2:** System crash after Step 7 (output(A)) but before output(B).

- Disk: A = 500, B = 2000.
- $500 has been debited from A but not credited to B.
- **Atomicity is violated.** The recovery manager must undo the change to A (restore A = 1000) or redo the change to B (B = 2500).

**Scenario 3:** Two concurrent transfers from A to B and A to C.

- T1: Transfer $500 from A to B.
- T2: Transfer $200 from A to C.
- If both read A = 1000 at the same time, they both compute A = 500 and A = 800 respectively.
- Final: A = 500 (T1 writes last) or A = 800 (T2 writes last), but total money is lost either way.
- **Isolation requires** that T1 and T2 appear to execute one after another.

---

## SQL Transaction Statements

```sql
-- Begin a transaction (implicit in most DBMS, or explicitly)
BEGIN TRANSACTION;

-- Perform operations
UPDATE Account SET balance = balance - 500 WHERE acc_no = 'A';
UPDATE Account SET balance = balance + 500 WHERE acc_no = 'B';

-- Make changes permanent
COMMIT;

-- Or undo all changes
ROLLBACK;
```

### PostgreSQL / Oracle Syntax

```sql
START TRANSACTION;
  UPDATE Account SET balance = balance - 500 WHERE acc_no = 'A';
  UPDATE Account SET balance = balance + 500 WHERE acc_no = 'B';
COMMIT;

-- With savepoints
SAVEPOINT sp1;
UPDATE Account SET balance = balance - 500 WHERE acc_no = 'A';
ROLLBACK TO sp1;   -- undo only the update, not the whole transaction
```

---

## Practice Problems

**Problem 1:** What are the six transaction states? Which state comes after PARTIALLY COMMITTED?

<details>
<summary>Show Answer</summary>

Active, Partially Committed, Committed, Failed, Aborted, Terminated. After Partially Committed, the transaction goes to either Committed (if no errors and output succeeds) or Failed (if an error occurs during output).
</details>

**Problem 2:** In the fund transfer example, what is the minimum number of write operations to disk that must be atomic to ensure consistency?

<details>
<summary>Show Answer</summary>

Both output(A) and output(B) must be performed atomically. If only one of the two writes to disk succeeds, the database is inconsistent (money is created or destroyed). The recovery manager ensures this atomicity via logging and recovery.
</details>

**Problem 3:** Draw the transaction state diagram and label all transitions.

<details>
<summary>Show Answer</summary>

See the ASCII diagram in the notes above. Transitions:
- ACTIVE -> PARTIALLY COMMITTED (end of operations)
- ACTIVE -> FAILED (error)
- PARTIALLY COMMITTED -> COMMITTED (successful commit)
- PARTIALLY COMMITTED -> FAILED (output failure)
- FAILED -> ABORTED (rollback)
- COMMITTED -> TERMINATED
- ABORTED -> TERMINATED
</details>

**Problem 4:** A transaction T reads X, increments it by 1, and writes X back. If the initial value of X is 5, and T executes successfully, what is the final value of X? What if T aborts after writing?

<details>
<summary>Show Answer</summary>

If T commits: X = 6. If T aborts after writing: the recovery manager rolls back the write to X, restoring X = 5.
</details>

**Problem 5:** Why is the PARTIALLY COMMITTED state necessary? Why not go directly from ACTIVE to COMMITTED?

<details>
<summary>Show Answer</summary>

The PARTIALLY COMMITTED state is necessary because after the final operation, the changes exist only in memory buffers. The system must verify that all operations have completed successfully, ensure no integrity constraints are violated, and then write the changes to disk (commit). If any of these steps fail, the transaction must abort. PARTIALLY COMMITTED represents this in-between state where the transaction has finished executing but has not yet been permanently recorded.
</details>

---
