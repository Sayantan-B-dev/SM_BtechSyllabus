# ACID Properties

**Course:** Database Management Systems  
**Module:** 3 | **Lecture:** 6  
**Date:** 17-Sep-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## Overview

ACID is an acronym that defines the four essential properties of a reliable database transaction. These properties guarantee that database transactions are processed reliably, even in the presence of system failures, crashes, and concurrent access.

| Property      | Brief Meaning                                                |
|---------------|--------------------------------------------------------------|
| **A**tomicity | The transaction is an indivisible unit. All or nothing.      |
| **C**onsistency| The transaction preserves database integrity constraints.   |
| **I**solation | Concurrent transactions do not interfere with each other.    |
| **D**urability| Committed changes survive future system or media failures.   |

---

## Atomicity

### Definition

A transaction is **atomic** if it executes completely or not at all. There is no partial execution.

### Why Atomicity is Necessary

Consider the fund transfer transaction:

```sql
BEGIN TRANSACTION;
  UPDATE Account SET balance = balance - 500 WHERE acc_no = 'A';
  -- CRASH HAPPENS HERE
  UPDATE Account SET balance = balance + 500 WHERE acc_no = 'B';
COMMIT;
```

If the system crashes after the first UPDATE but before the second, $500 has been removed from A but not added to B. The database is now inconsistent (money has disappeared). The DBMS must **undo** the first UPDATE (rollback) so that the database returns to the state it was in before the transaction began.

### Implementation Mechanisms

**Recovery Manager** handles atomicity via:

1. **Undo logging:** Before modifying a data item, the DBMS writes the old value to a log. If the transaction aborts, it uses the log to restore the old values.

2. **Redo logging:** The DBMS writes the new value to the log before committing. On crash recovery, it replays committed transactions.

3. **Shadow paging:** Two copies of the database are maintained (current and shadow). Atomicity is achieved by atomically switching the pointer between them.

### Detailed Example: Atomicity with Undo Logging

```
Transaction T: A = A - 500, B = B + 500

Log entries written during execution:
<START T>
<T, A, OLD=1000>    -- before writing A
<T, A, NEW=500>     -- after writing A to buffer
<T, B, OLD=2000>    -- before writing B
<T, B, NEW=2500>    -- after writing B to buffer

If T aborts:
  Recovery reads log backwards.
  Restore A = 1000 (old value).
  Restore B = 2000 (old value).
  Write <ABORT T>
```

### Key Point

Atomicity is about **failure handling** -- ensuring that partial executions are not visible in the final database state.

---

## Consistency

### Definition

A transaction is **consistent** if it takes the database from one consistent state (satisfying all integrity constraints) to another consistent state.

### What Does Consistency Mean?

The database has a set of **integrity constraints**:
- **Domain constraints:** salary >= 0, age between 0 and 150.
- **Key constraints:** Primary keys must be unique.
- **Referential integrity:** Foreign keys must reference existing primary keys.
- **Business rules:** Total balance in all accounts must equal the bank's liability.

A consistent transaction ensures that if the database is consistent before the transaction starts, it is consistent after the transaction completes.

### Example

```sql
-- Constraint: balance >= 0
BEGIN TRANSACTION;
  UPDATE Account SET balance = balance - 1000 WHERE acc_no = 'A';
  -- If A has balance = 500, this violates balance >= 0.
  -- The transaction must abort.
  UPDATE Account SET balance = balance + 1000 WHERE acc_no = 'B';
COMMIT;
```

**Consistency check:** Before committing, the DBMS verifies that balance >= 0 holds. It does not. The transaction is aborted (atomicity ensures rollback of the first UPDATE).

### Who Ensures Consistency?

- **Application programmer:** Writes transactions that preserve business rules (e.g., total sum of debits = total sum of credits in a transfer).
- **DBMS:** Enforces domain constraints, key constraints, referential integrity, and constraint checks via `CHECK` clauses.

### Example: Consistency Violation by Programmer Bug

```sql
-- Buggy transaction: transfers 500 from A to B
BEGIN TRANSACTION;
  UPDATE Account SET balance = balance - 500 WHERE acc_no = 'A';
  -- A = 500 (if A was 1000)
  -- OOPS! Forgot the second UPDATE
COMMIT; -- But this is atomic. When commit is called, only the debit happens.
```

The DBMS cannot detect this logical inconsistency. It is the programmer's responsibility to ensure the transaction encodes a correct business operation.

### Detailed Example: Consistency with CHECK Constraint

```sql
CREATE TABLE Account (
    acc_no VARCHAR(10) PRIMARY KEY,
    balance DECIMAL(10,2) CHECK (balance >= 0)
);

BEGIN TRANSACTION;
  UPDATE Account SET balance = balance - 1000 WHERE acc_no = 'A';
  -- If A.balance was 400, new balance = -600 -> violates CHECK
  -- DBMS raises an error, transaction enters FAILED state
  -- ROLLBACK is triggered, A restored to 400
  UPDATE Account SET balance = balance + 1000 WHERE acc_no = 'B';
COMMIT;
```

---

## Isolation

### Definition

**Isolation** ensures that concurrent execution of transactions leaves the database in the same state as if the transactions were executed **serially** (one after another). Each transaction operates as if it is the only transaction in the system.

### Why Isolation is Needed

Without isolation, concurrent transactions can cause:

1. **Dirty Read:** Transaction T2 reads data written by uncommitted transaction T1. If T1 aborts, T2 has read invalid data.

2. **Non-Repeatable Read:** Transaction T2 reads the same data twice and gets different values because T1 modified and committed between the two reads.

3. **Phantom Read:** Transaction T2 runs the same query twice and sees different rows (new rows inserted by T1 between the two queries).

4. **Lost Update:** Two transactions read the same value, both modify it, and one modification overwrites the other.

### Example: Lost Update

```
T1: read(A);  // A = 1000
T2: read(A);  // A = 1000
T1: A = A - 500; write(A);  // A = 500
T2: A = A + 200; write(A);  // A = 1200 (lost T1's update!)
```

Final A = 1200 instead of 700 (1000 - 500 + 200). T1's update is **lost**.

### Implementation Mechanisms

**Concurrency Control Manager** ensures isolation via:

1. **Lock-based protocols (2PL):** Transactions acquire locks on data items before accessing them. Locking prevents conflicts.

2. **Timestamp-based protocols:** Each transaction is assigned a unique timestamp. Operations are ordered by timestamps to ensure serializability.

3. **Multiversion concurrency control (MVCC):** Each write creates a new version of the data item. Reads see a consistent snapshot.

### SQL Isolation Levels (ANSI/ISO)

```sql
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

| Level              | Dirty Read | Non-Repeatable Read | Phantom Read |
|--------------------|------------|---------------------|--------------|
| READ UNCOMMITTED   | Possible   | Possible            | Possible     |
| READ COMMITTED     | Not possible| Possible           | Possible     |
| REPEATABLE READ    | Not possible| Not possible       | Possible     |
| SERIALIZABLE       | Not possible| Not possible       | Not possible |

---

## Durability

### Definition

**Durability** guarantees that once a transaction commits, its changes are **permanent** and will survive any subsequent system or media failures (crashes, power outages, disk failures).

### Implementation Mechanisms

**Recovery Manager** ensures durability via:

1. **Write-ahead logging (WAL):** Before a data page is written to disk, the log record is first written to stable storage. The log can be replayed after a crash to redo committed transactions.

2. **Commit protocol (2PC):** In distributed databases, the two-phase commit protocol ensures that all nodes agree on the commit decision before making it permanent.

3. **Database backups:** Periodic backups to tape or cloud storage protect against media failures (disk corruption, fire, etc.).

### Detailed Example: Durability with Redo Logging

```
Transaction T:
  UPDATE Account SET balance = 500 WHERE acc_no = 'A';  -- initially 1000

Log:
  <START T>
  <T, A, OLD=1000, NEW=500>   -- log record written BEFORE flushing data page
  <COMMIT T>                   -- commit log record flushed to stable storage

Now even if the system crashes immediately after COMMIT:
  - Recovery reads the log.
  - Finds <COMMIT T>.
  - Redoes the change: sets A = 500 (if the data page was not yet flushed).
```

The key is that the `COMMIT` log record must be on **stable storage** (usually non-volatile memory or a disk with battery-backed cache) before the DBMS reports success to the user.

### Durability Failure Scenarios and Mitigation

| Failure Type          | Durability Threat                        | Mitigation                        |
|-----------------------|------------------------------------------|-----------------------------------|
| Transaction abort     | Did not commit; no durability needed     | Undo changes via log              |
| System crash (power)  | Committed data not flushed to disk       | Redo from log after restart       |
| Disk head crash       | Physical destruction of data             | RAID, backups, off-site replication |
| Media errors (bad sectors)| Partial data corruption              | Checksums, RAID, backups          |

---

## ACID Interactions

The four properties are interconnected:

```
           Consistency
           /        \
   Atomicity          Durability
           \        /
           Isolation
```

- **Atomicity** and **Durability** are about failure handling (recovery).
- **Consistency** is about correctness of state (constraints + application logic).
- **Isolation** is about concurrency control.
- **Atomicity + Isolation -> Consistency:** If each transaction is consistent (defined as "preserves consistency when run alone") and isolation ensures concurrent execution = serial execution, then consistency is preserved.
- **Durability** is independent but relies on atomicity (committed data is not rolled back).

### Example: How ACID Properties Work Together

```
T1: Transfer $100 from A to B.

Initial: A = $500, B = $500. Constraint: balance >= 0.

T1 executes:
  read(A);  // A = 500
  read(B);  // B = 500
  A = A - 100;  // A = 400
  B = B + 100;  // B = 600
  write(A);     // A = 400
  write(B);     // B = 600
  COMMIT;

Property Check:
  Atomicity:  If crash after write(A), DBMS rolls back both writes (A=500, B=500).
  Consistency: A = 400 >= 0, B = 600 >= 0. Balance sum = 1000 (preserved). OK.
  Isolation:   If T2 reads A and B concurrently, it sees either (500,500) or (400,600), never (400,500).
  Durability:  After commit, A=400 and B=600 survive any subsequent crash.
```

---

## Practice Problems

**Problem 1:** Which ACID property is violated by a dirty read?

<details>
<summary>Show Answer</summary>

Isolation is violated. Dirty read means transaction T2 reads data written by uncommitted transaction T1, violating the isolation principle that transactions should not see partial (uncommitted) changes of other transactions.
</details>

**Problem 2:** A transaction deducts $100 from account X and adds $100 to account Y. The constraint is total money (X + Y) is conserved. If the system crashes after deducting from X but before adding to Y, which ACID property must be enforced and how?

<details>
<summary>Show Answer</summary>

Atomicity must be enforced. The recovery manager must undo the debit to X (rollback) to restore the database to its state before the transaction began. Without atomicity, the database would lose $100.
</details>

**Problem 3:** Explain why isolation is necessary for consistency, even if each individual transaction is consistent when run alone.

<details>
<summary>Show Answer</summary>

Without isolation, concurrent transactions can interfere: one transaction may see partial results of another (dirty read), or two transactions may overwrite each other's updates (lost update). This can lead to a final state that no serial execution of the same transactions could produce, potentially violating consistency even though each transaction individually preserved consistency.
</details>

**Problem 4:** A DBMS writes a COMMIT log record to stable storage, then immediately crashes before flushing the modified data pages to disk. When the system restarts, which ACID property ensures the changes are not lost, and how does the DBMS restore them?

<details>
<summary>Show Answer</summary>

Durability ensures the committed changes survive the crash. The DBMS uses the log: during recovery (after restart), it finds the COMMIT record and redoes the transaction's updates on the data pages, bringing them up to date.
</details>

**Problem 5:** Can a transaction be atomic and durable but not consistent? Provide an example.

<details>
<summary>Show Answer</summary>

Yes. Suppose a transaction transfers $500 from A to B but accidentally writes $500 to B without debiting A. The transaction is atomic (both writes happen or neither) and durable (committed changes persist), but the database is inconsistent (money was created out of nowhere, violating the business rule that total money is conserved). This is a logical error in the transaction, not an ACID violation by the DBMS.
</details>

---
