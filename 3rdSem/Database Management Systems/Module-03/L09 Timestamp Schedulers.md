# Timestamp Schedulers

**Course:** Database Management Systems  
**Module:** 3 | **Lecture:** 9  
**Date:** 24-Sep-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## Introduction to Timestamp-Based Concurrency Control

Locking protocols (Lecture 8) use a **pessimistic** approach: transactions acquire locks to prevent conflicts. Timestamp-based protocols take a different approach: each transaction is assigned a unique timestamp, and the concurrency control manager ensures that conflicting operations are executed in timestamp order.

### Key Idea

- Every transaction T receives a unique timestamp `TS(T)` when it begins.
- Timestamps determine the serialization order: if `TS(T_i) < TS(T_j)`, then T_i must appear before T_j in the equivalent serial schedule.
- The DBMS uses timestamps to decide whether to allow or reject an operation.

### How Timestamps Are Generated

1. **System clock:** Use the current system time as the timestamp.
2. **Logical counter:** Maintain a counter that is incremented for each new transaction.
3. **Combination:** Combine clock value with a node ID (for distributed systems).

### Advantages over Locking

| Aspect              | Locking                        | Timestamp Ordering              |
|---------------------|--------------------------------|----------------------------------|
| Deadlocks           | Possible (needs detection)     | Impossible (no waiting)         |
| Starvation          | Possible                       | Possible (restarts)             |
| Overhead            | Lock management, deadlock detection | Timestamp maintenance           |
| Concurrency         | Blocking (waits for locks)     | Non-blocking (abort on conflict)|
| Suitability         | General purpose                | Read-heavy workloads, distributed systems |

---

## Timestamp Ordering Protocol

### Data Structures

For each data item X, the DBMS maintains two timestamps:

- **read_TS(X):** The largest timestamp of any transaction that successfully read X.
- **write_TS(X):** The largest timestamp of any transaction that successfully wrote X.

### Rules for Read Operations

When transaction T with timestamp `TS(T)` issues `read(X)`:

1. If `TS(T) < write_TS(X)`:
   - T is trying to read a value that was written by a "future" transaction (one with a larger timestamp). This would violate the timestamp ordering (the future transaction should come after T in the serial schedule).
   - **Abort T** and restart it with a new (later) timestamp.

2. If `TS(T) >= write_TS(X)`:
   - The read is allowed.
   - Update `read_TS(X) = max(read_TS(X), TS(T))`.

### Rules for Write Operations

When transaction T with timestamp `TS(T)` issues `write(X)`:

1. If `TS(T) < read_TS(X)`:
   - Some transaction with a larger timestamp has already read X. If T writes X now, that future transaction would have read a stale value.
   - **Abort T** and restart.

2. If `TS(T) < write_TS(X)`:
   - A transaction with a larger timestamp has already written X. T's write would be overwritten by that future write anyway. This is an **obsolete write**.
   - **Abort T** (or ignore the write under Thomas Write Rule).

3. If `TS(T) >= max(read_TS(X), write_TS(X))`:
   - The write is allowed.
   - Update `write_TS(X) = TS(T)`.

### Algorithm

```
Read(X) by T with TS(T):
   if TS(T) < write_TS(X) then
     abort T and restart with new timestamp
   else
     perform read(X)
     read_TS(X) = max(read_TS(X), TS(T))

Write(X) by T with TS(T):
   if TS(T) < read_TS(X) then
     abort T and restart with new timestamp
   else if TS(T) < write_TS(X) then
     abort T and restart with new timestamp
   else
     perform write(X)
     write_TS(X) = TS(T)
```

---

## Worked Example: Timestamp Ordering

Let T1 (TS=10) and T2 (TS=20) access data items A and B.

### Example 1: Allowed Operations

```
Initial: read_TS(A)=0, write_TS(A)=0, read_TS(B)=0, write_TS(B)=0

T1: read(A)   -- TS(T1)=10 >= write_TS(A)=0. Allowed. read_TS(A)=10.
T1: write(A)  -- TS(T1)=10 >= read_TS(A)=10, >= write_TS(A)=0. Allowed. write_TS(A)=10.
T2: read(A)   -- TS(T2)=20 >= write_TS(A)=10. Allowed. read_TS(A)=20.
T2: write(B)  -- TS(T2)=20 >= read_TS(B)=0, >= write_TS(B)=0. Allowed. write_TS(B)=20.
```

Serial order: T1 (TS=10) before T2 (TS=20). Equivalent to T1 -> T2.

### Example 2: Abort (Read too late)

```
Initial: read_TS(A)=0, write_TS(A)=10

T2 (TS=20): write(A)   -- Allowed. write_TS(A)=20.
T1 (TS=10): read(A)    -- TS(T1)=10 < write_TS(A)=20. ABORT!
```

T1 tries to read a value written after T1 should have been serialized. T1 is too late. T1 must abort.

### Example 3: Abort (Write too late)

```
Initial: read_TS(A)=20, write_TS(A)=0

T1 (TS=10): write(A) -- TS(T1)=10 < read_TS(A)=20. ABORT!
```

T1 tries to write A, but a future transaction already read A. T1 must abort.

---

## Thomas Write Rule

### Problem

Under the basic protocol, a write is aborted if `TS(T) < write_TS(X)`. This abort is often unnecessary.

### Thomas Write Rule (TWR)

If `TS(T) < write_TS(X)`, the write is **ignored** (not executed) instead of aborting the transaction.

### Why This is Safe

If a later transaction has already written X, then T's write would be overwritten anyway. Since no transaction will ever read T's write (the later write supersedes it), we can skip it safely.

### Revised Write Rule with TWR

```
Write(X) by T with TS(T):
   if TS(T) < read_TS(X) then
     abort T and restart with new timestamp
   else if TS(T) < write_TS(X) then
     IGNORE the write (do nothing) -- Thomas Write Rule
   else
     perform write(X)
     write_TS(X) = TS(T)
```

### Example with TWR

```
Initial: read_TS(A)=0, write_TS(A)=0

T1 (TS=10): write(A) -- Allowed. write_TS(A)=10.
T2 (TS=20): write(A) -- Allowed. write_TS(A)=20.
T1 (TS=10): write(A) -- TS(T1)=10 < write_TS(A)=20. Under base: ABORT.
                                                    Under TWR: IGNORE.
T1: read(B)... commit.
```

Under TWR, T1 is not aborted unnecessarily. The write to A by T1 would have been overwritten by T2 anyway.

### Comparison

| Scenario                          | Base Protocol          | Thomas Write Rule      |
|-----------------------------------|------------------------|------------------------|
| TS(T) < read_TS(X)                | Abort T                | Abort T                |
| TS(T) < write_TS(X)               | Abort T                | Ignore write (safe)    |
| TS(T) >= read_TS(X), write_TS(X)  | Allow write            | Allow write            |

---

## Multiversion Concurrency Control (MVCC) Introduction

### Motivation

Timestamp ordering still aborts transactions on conflicts. MVCC takes a fundamentally different approach: instead of overwriting data, each write creates a **new version** of the data item. Readers always see a consistent snapshot based on their timestamp.

### Key Idea

- Every write to data item X creates a new version of X, tagged with the writer's timestamp.
- A read operation reads the version of X with the largest timestamp <= the reader's timestamp.
- Writers do not block readers, and readers do not block writers.

### Version Selection

When transaction T with timestamp TS(T) reads X:

```
Find the version of X with write_TS(X, v) such that:
  - write_TS(X, v) <= TS(T) (version written before or by T)
  - No other version v' exists where write_TS(X, v') > write_TS(X, v) and write_TS(X, v') <= TS(T)
In other words: read the most recent version that is not newer than T.
```

### Example: MVCC

```
T1 (TS=10): write(A, 100)  -- creates version A_v10 = 100
T2 (TS=20): read(A)        -- reads A_v10 = 100 (largest version <= TS=20)
T3 (TS=15): write(A, 200)  -- creates version A_v15 = 200
T2 (TS=20): read(A)        -- reads A_v15 = 200 (largest version <= TS=20)
T4 (TS=25): read(A)        -- reads A_v15 = 200
```

Versions of A: A_v10(100), A_v15(200).

### MVCC in Practice

MVCC is used by:
- **PostgreSQL:** Default concurrency control mechanism. Uses snapshots.
- **Oracle:** Read consistency via undo segments (snapshot isolation).
- **MySQL InnoDB:** Uses MVCC for REPEATABLE READ and READ COMMITTED isolation levels.
- **SQL Server:** Snapshot isolation level uses row versioning.

### MVCC vs Timestamp Ordering

| Aspect              | Timestamp Ordering          | MVCC                         |
|---------------------|-----------------------------|------------------------------|
| Read blocking       | Can abort (read too late)   | Never blocks (reads snapshot)|
| Write blocking      | Can abort (write too late)  | Creates new version          |
| Storage             | Single version              | Multiple versions (old + new)|
| Garbage collection  | Not needed                  | Needed (vacuum old versions) |
| Isolation level     | Serializable                | Snapshot (slightly weaker)   |
| Use case            | Timely conflict detection   | Read-heavy, high concurrency |

---

## Comparison: Locking vs Timestamping vs MVCC

| Property            | 2PL Locking       | Timestamp (T/O)  | MVCC              |
|---------------------|--------------------|--- ----------------|-------------------|
| Deadlocks           | Yes                | No                | No                |
| Read-only tx abort  | No (S-locks)       | Yes (read too late)| No (snapshot)     |
| Write-write conflict| Block or abort     | Abort younger     | New version       |
| Space overhead      | Locks              | Timestamps        | Versions + timestamps |
| Performance         | OLTP (writes)      | Read-heavy        | Read-heavy, mixed |

---

## Practice Problems

**Problem 1:** In the basic timestamp ordering protocol, T1 (TS=5) writes A, then T2 (TS=10) reads A, then T1 tries to write A again. What happens?

<details>
<summary>Show Answer</summary>

After T1 writes A: write_TS(A)=5.
After T2 reads A: read_TS(A)=10.
T1 writes A: TS(T1)=5 < read_TS(A)=10. T1 must ABORT.
</details>

**Problem 2:** Under Thomas Write Rule, would the answer to Problem 1 change?

<details>
<summary>Show Answer</summary>

No. TWR only changes the case TS(T) < write_TS(X). Here, TS(T1) < read_TS(X) still holds, so T1 still aborts. TWR does not help with read conflicts.
</details>

**Problem 3:** T1 (TS=100) reads X, T2 (TS=200) writes X, T1 writes X. What happens under (a) basic timestamp ordering, (b) Thomas Write Rule?

<details>
<summary>Show Answer</summary>

After T1 reads X: read_TS(X)=100.
After T2 writes X: write_TS(X)=200.
T1 writes X:
- (a) Basic: TS(T1)=100 < write_TS(X)=200, so ABORT.
- (b) TWR: TS(T1)=100 < write_TS(X)=200, so IGNORE (T1 continues).
</details>

**Problem 4:** In MVCC, T1 (TS=10) writes A=5, T2 (TS=20) writes A=10, T3 (TS=15) reads A. What value does T3 read?

<details>
<summary>Show Answer</summary>

Versions of A: A_v10=5, A_v20=10.
T3 reads the version with largest write_TS <= TS(T3)=15.
The versions with write_TS <= 15: A_v10 (5). A_v20=10 has write_TS=20 > 15.
So T3 reads A=5 (the version written by T1).
</details>

**Problem 5:** Why does MVCC never block read-only transactions? Why is this beneficial?

<details>
<summary>Show Answer</summary>

In MVCC, reads always see a consistent snapshot of the database as of the reader's timestamp. The reader does not need to acquire locks or wait for writers. If a writer is in progress, the reader simply reads the previous version. This is beneficial for read-heavy workloads (e.g., reporting, analytics) where long-running queries should not be blocked by concurrent updates.
</details>

---
