# Database Recovery Techniques

**Course:** Database Management Systems  
**Module:** 3 | **Lecture:** 10  
**Date:** 29-Sep-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## Introduction

Database recovery is the process of restoring the database to a correct, consistent state after a failure. The **recovery manager** is the DBMS component responsible for ensuring **atomicity** (undoing uncommitted transactions) and **durability** (re-doing committed transactions whose changes were lost due to the failure).

### Why Recovery is Needed

Despite all precautions, failures happen:
- Power outage during a transaction.
- Operating system crash.
- Disk head crash (media failure).
- Software bug causing DBMS to terminate.
- Transaction abort (due to deadlock, constraint violation, etc.).

The recovery manager must handle all these scenarios.

---

## Failure Classification

Failures are broadly classified into three categories:

### 1. Transaction Failure

The transaction itself fails to complete normally.

**Causes:**
- Logical error: Division by zero, constraint violation, duplicate key.
- System error: Deadlock (transaction chosen as victim), resource limit exceeded.
- User intervention: Manual ROLLBACK command.

**Effect:** The transaction must be **aborted** and rolled back. The database must be restored to the state before the transaction started.

### 2. System Crash

The DBMS or operating system fails unexpectedly, but the disk storage remains intact.

**Causes:**
- Power failure.
- OS panic or crash.
- DBMS software bug.

**Effect:** All transactions in progress are terminated. The contents of main memory (buffers, caches) are lost, but data on disk survives. After restart, the recovery manager must:
- **Undo** the changes of uncommitted transactions (atomicity).
- **Redo** the changes of committed transactions whose data may not have been flushed to disk (durability).

### 3. Disk Failure

The disk storage itself fails.

**Causes:**
- Disk head crash.
- Bad sectors.
- Fire, flood, physical destruction.

**Effect:** Some or all of the database on disk is permanently lost. Recovery requires **archival backups** (database snapshots stored on separate media) and the **log** to replay changes since the last backup.

---

## Log-Based Recovery

### The Log

A **log** is a sequential file of **log records** stored on **stable storage** (a storage medium that survives failures). Every modification to the database is recorded in the log BEFORE the actual data page is modified on disk.

### Log Record Types

Each log record contains:

- `<START T>`: Transaction T has started.
- `<T, X, old_value, new_value>`: Transaction T has modified data item X. Old value (before image) and new value (after image) are recorded.
- `<COMMIT T>`: Transaction T has committed (all changes will persist).
- `<ABORT T>`: Transaction T has aborted (changes must be undone).
- `<CKPT>`: A checkpoint record (explained below).

### Write-Ahead Logging (WAL)

**Write-ahead logging** is the fundamental rule:

1. **Before** a data item on disk is modified, the log record describing the modification must be written to stable storage (the log).
2. **Before** a transaction commits, all its log records (including the COMMIT record) must be written to stable storage.

**Purposes of WAL:**
- If a crash occurs, the log can be used to undo incomplete transactions (atomicity).
- The log can be used to redo completed transactions whose data pages were not yet flushed from buffer to disk (durability).

### Stable Storage

Stable storage is typically implemented as:
- Write-ahead log on a separate disk drive.
- Battery-backed RAM (non-volatile RAM).
- RAID-1 (mirrored disks) for the log.
- Multiple copies of the log (multiplexing).

---

## Undo Logging

### Principle

In undo logging, the log records the **old value** (before image) of modified data items. If a transaction aborts or a crash occurs, the recovery manager undoes the changes by restoring old values.

### Log Record Format

```
<T, X, old_value>
```

Note: No new_value in pure undo logging.

### Protocol

1. For each modification, write `<T, X, old_value>` to log (before modifying disk).
2. When transaction commits, write `<COMMIT T>` to log.
3. Data pages can be flushed to disk at any time (before or after commit).
4. On recovery: scan log backwards. For each `<T, X, old_value>` where T has not committed, restore X = old_value.

### Example

```
Transaction T:
  A = 1000 -> 500   (write)
  B = 2000 -> 2500  (write)
  COMMIT

Log:
  <START T>
  <T, A, 1000>    -- written BEFORE modifying A on disk
  <T, B, 2000>    -- written BEFORE modifying B on disk
  <COMMIT T>
```

**Recovery if crash after COMMIT:** No action needed (COMMIT guarantees durability).

**Recovery if crash before COMMIT:** The log contains the old values. Undo: restore A=1000, B=2000. The transaction never committed; atomicity is preserved.

### Problem with Pure Undo Logging

If the system crashes after data pages are flushed to disk but before COMMIT, the undo log tells us to restore old values, which works. However, if data pages are flushed AFTER COMMIT, the durability is ensured. The issue is that data pages could be flushed before commit, and if a crash occurs then the COMMIT record will never have been written, so we undo. This is fine.

But what if the data page is flushed to disk, then the system crashes, but the log has `<COMMIT T>` written to stable storage? Then we need the **new values** to redo the transaction. Pure undo logging does not have new values. For this, we need redo logging or undo-redo logging.

---

## Redo Logging

### Principle

In redo logging, the log records the **new value** (after image). If a crash occurs after commit, the recovery manager redoes the transaction by writing the new values to disk.

### Log Record Format

```
<T, X, new_value>
```

### Protocol

1. For each modification, write `<T, X, new_value>` to log.
2. All data pages modified by T MUST wait until after commit to be flushed to disk (deferred update).
3. When transaction commits, write `<COMMIT T>` to log.
4. On recovery: scan log forward. For each `<T, X, new_value>` where T has committed, redo the write (set X = new_value).

### Example

```
Transaction T:
  A = 1000 -> 500
  B = 2000 -> 2500
  COMMIT

Log:
  <START T>
  <T, A, 500>
  <T, B, 2500>
  <COMMIT T>
  -- Only now are data pages flushed to disk
```

**Recovery after crash before commit:** No redo needed (COMMIT not in log). However, A and B may have been partially written to disk (if protocol was violated). If we strictly follow the protocol (deferred update), no data pages are written before commit, so the disk is in a consistent old state.

**Recovery after crash after commit:** Redo: set A=500, B=2500.

---

## Undo-Redo Logging

### Principle

Pure undo logging cannot redo committed transactions (lacks new values). Pure redo logging requires deferred updates (all writes happen after commit), which uses a lot of buffer space. **Undo-redo logging** combines both: the log records both old and new values. Writes to disk can happen at any time (before or after commit).

### Log Record Format

```
<T, X, old_value, new_value>
```

### Protocol

1. For each modification, write `<T, X, old, new>` to log.
2. Data pages can be flushed to disk at any time (STEAL policy -- allows dirty pages to be written before commit).
3. On commit, write `<COMMIT T>` to log.
4. On recovery (after crash):
   - **Undo phase (backward):** For each `<T, X, old, new>` where T has NOT committed, restore X = old_value.
   - **Redo phase (forward):** For each `<T, X, old, new>` where T HAS committed, set X = new_value.

### Comparison

| Property          | Undo Logging | Redo Logging | Undo-Redo Logging |
|-------------------|--------------|--------------|-------------------|
| Log contents      | Old values   | New values   | Both old and new  |
| Disk flush timing| Any time     | After commit only (NO-STEAL) | Any time (STEAL) |
| Recovery actions  | Undo only    | Redo only    | Undo + Redo      |
| Use case          | Simple recovery | Deferred updates | Most general     |

---

## Checkpointing

### Problem

Without checkpoints, recovery requires scanning the **entire log** from the beginning of time. For a database that has been running for weeks, the log could be terabytes. Scanning it would take hours.

### Solution

**Checkpointing** is a periodic operation that:
1. Writes all dirty (modified) buffer pages to disk.
2. Writes a `<CKPT>` record to the log, listing all active transactions.

### Checkpoint Types

#### 1. Consistent Checkpoint (Quiescent)

1. Halt all new transaction starts.
2. Wait for all active transactions to commit or abort.
3. Flush all dirty buffers to disk.
4. Write `<CKPT>` to log.
5. Resume.

**Pros:** Simple. **Cons:** Database is unavailable during checkpoint.

#### 2. Fuzzy Checkpoint (Non-Quiescent)

1. Write `<START CKPT (active_txn_list)>` to log.
2. Flush dirty pages to disk (can run concurrently with new transactions).
3. Write `<END CKPT>` to log.

**Pros:** Database remains available. **Cons:** More complex recovery.

### Recovery with Checkpoints

After a crash, recovery starts from the **last checkpoint**, not from the beginning of the log. This bounds the recovery time.

```
Log:
  ... <CKPT> ... <START T1> <T1, A, 100, 50> ... <CKPT (T1, T2)> ... <COMMIT T1> ... CRASH!

Recovery starts from the last checkpoint. Transactions before the checkpoint:
  - If committed: already flushed to disk (checkpoint ensures this for consistent ckpt).
  - If not committed: may or may not have been flushed, but the log from checkpoint onward tells us.
```

---

## Recovery Using Deferred Update

### Principle

The DBMS does NOT write any data page modifications to disk until the transaction commits (NO-STEAL policy). All modifications are kept in buffer pages. On commit, they are flushed to disk.

### Recovery Algorithm

**On crash:**
- Scan log forward.
- For each `<COMMIT T>` record, the data pages of T are then flushed to disk.
- No undo is needed because no uncommitted transaction's data pages were written to disk (by the NO-STEAL property).

### Limitations

- Buffer space: all modified pages must stay in buffer until commit.
- Long transactions consume significant buffer resources.
- Cannot use STEAL-based buffer management.

---

## Recovery Using Immediate Update

### Principle

The DBMS may write modified data pages to disk BEFORE the transaction commits (STEAL policy). This is more flexible for buffer management but requires both undo and redo during recovery.

### Recovery Algorithm (Undo-Redo)

1. **Analysis phase:** Scan log forward to identify all dirty pages and active transactions at the time of crash.
2. **Redo phase:** Scan log forward from the earliest LSN (Log Sequence Number) among dirty pages. Redo all changes of committed and active transactions.
3. **Undo phase:** Scan log backward. Undo all changes of transactions that were active at the time of crash (those that did NOT commit).

---

## ARIES Algorithm Overview

**ARIES** (Algorithm for Recovery and Isolation Exploiting Semantics) is the most widely used recovery algorithm in commercial databases. It is used in IBM DB2, Microsoft SQL Server, and many others.

### Key Principles of ARIES

1. **Write-ahead logging (WAL):** Log records are written before data pages.
2. **Repeating history during redo:** Redo ALL operations (committed and uncommitted) to reconstruct the exact state at the time of crash.
3. **Undo of loser transactions:** Roll back transactions that were uncommitted at the time of crash.

### Data Structures in ARIES

- **LSN (Log Sequence Number):** Monotonically increasing identifier for each log record. Stored in the data page (pageLSN) to track which log record corresponds to the latest update on that page.
- **Dirty Page Table (DPT):** List of pages that have been modified but not yet flushed to disk. Each entry contains the page ID and the LSN of the first change to that page (recLSN).
- **Transaction Table:** List of active transactions, their state, and the LSN of their last log record (lastLSN).

### ARIES Recovery Phases

#### Phase 1: Analysis

- Start from the last checkpoint.
- Read log forward to reconstruct the Transaction Table and Dirty Page Table at the time of crash.
- Determine the **redo LSN** (the smallest recLSN in the DPT) -- the point in the log from which redo must start.

#### Phase 2: Redo

- Scan log forward from the redo LSN.
- For each log record `<T, X, old, new>`:
  - If page X is in the DPT and the page's pageLSN < record's LSN, redo the change (write new value to X).
  - Otherwise, skip (page was already flushed to disk).

#### Phase 3: Undo

- Scan log backward from the end.
- For each log record `<T, X, old, new>` where T is a **loser** (uncommitted):
  - Write a **CLR (Compensation Log Record)** to log: `<T, X, old> CLR>`.
  - Undo the change (restore old value).
- Continue until all loser transactions are fully undone.

### ARIES Example

```
Database state before crash:
  A = 100, B = 200, C = 300

Log:
  1: <START T1>
  2: <T1, A, 100, 50>    -- T1 sets A=50
  3: <START T2>
  4: <T1, B, 200, 150>   -- T1 sets B=150
  5: <T2, C, 300, 400>   -- T2 sets C=400
  6: <COMMIT T1>
  7: <T1, ... > (more)
  -- CRASH

Analysis phase:
  Transaction Table: T1 (COMMIT found), T2 (active, lastLSN=5)
  Dirty Page Table: A (recLSN=2), B (recLSN=4), C (recLSN=5)
  Redo LSN = min(recLSN) = 2

Redo phase (from LSN=2):
  LSN 2: A -> 50 (redo)
  LSN 4: B -> 150 (redo)
  LSN 5: C -> 400 (redo)

Undo phase (T2 is loser):
  Undo LSN 5: C -> 300 (write CLR <T2, C, 300, UNDO>)
  No more T2 records.
  Write <ABORT T2> to log.

Final state: A=50, B=150, C=300
```

---

## Summary: Recovery Matrix

| Failure Type      | What is Lost        | Recovery Method                      | Components Needed              |
|-------------------|---------------------|--------------------------------------|--------------------------------|
| Transaction abort| Buffer changes      | Undo from log                       | Log (old values)               |
| System crash      | Buffer, cache       | Undo uncommitted, Redo committed    | Log + checkpoint               |
| Disk failure      | Disk data           | Restore from backup + Redo from log | Archival backup + full log    |

---

## Practice Problems

**Problem 1:** A system crash occurs. The log contains `<COMMIT T1>` and `<START T2>` but no `<COMMIT T2>`. T1 modified A (old=100, new=50). T2 modified B (old=200, new=300). What recovery actions are needed?

<details>
<summary>Answer</summary>

- T1: Committed. Must **redo**: set A = 50 (if not already flushed).
- T2: NOT committed. Must **undo**: restore B = 200.
</details>

**Problem 2:** What is the purpose of write-ahead logging (WAL)? Why must the log be written before the data page?

<details>
<summary>Answer</summary>

WAL ensures that the log contains the information needed for recovery BEFORE a data page is modified on disk. If the system crashes after modifying a data page but before the corresponding log record is written, there is no record of the change, making recovery impossible (the change cannot be undone because there is no old value, and it cannot be redone because there is no new value). WAL guarantees that the log always has enough information for undo and redo.
</details>

**Problem 3:** In ARIES, what information does the Dirty Page Table (DPT) contain, and how is it used during the analysis phase?

<details>
<summary>Answer</summary>

The DPT contains page IDs and the recLSN (the LSN of the first log record that dirtied the page). During analysis, the DPT is reconstructed from the log starting at the last checkpoint. It is used to determine the **redo LSN** (the smallest recLSN), which is the point in the log from which redo must begin. Pages whose lastLSN >= recLSN need redo; pages already flushed to disk (pageLSN >= recLSN but data on disk is current) are skipped.
</details>

**Problem 4:** Distinguish between undo logging and redo logging. When would you use each?

<details>
<summary>Answer</summary>

- **Undo logging:** Records old values. Used when the DBMS uses a STEAL policy (dirty pages can be written to disk before commit). On recovery, undo restores old values for uncommitted transactions. Problem: cannot redo committed transactions (no new values recorded).
- **Redo logging:** Records new values. Used when the DBMS uses a NO-STEAL policy (dirty pages NOT written to disk before commit). On recovery, redo writes new values for committed transactions. Problem: cannot undo uncommitted transactions.
- **Undo-redo logging:** Records both. Supports both STEAL and NO-STEAL. Most general approach.
</details>

**Problem 5:** ARIES uses three recovery phases: Analysis, Redo, Undo. Why is the Redo phase performed BEFORE the Undo phase?

<details>
<summary>Answer</summary>

Redo is performed first to "repeat history" -- reconstruct the exact state of the database as it was at the time of the crash, including both committed and uncommitted changes. This ensures that the undo phase sees the correct state. If Undo were performed first, it would undo changes that might need to be redone later (for committed transactions), leading to inconsistency. Redo-first guarantees that all committed changes are in place before any undo begins.
</details>

---
