# Locking Protocols

**Course:** Database Management Systems  
**Module:** 3 | **Lecture:** 8  
**Date:** 24-Sep-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## Introduction

Locking is the most common mechanism used by DBMS to control concurrent access to data. A **lock** is a synchronization primitive that grants a transaction exclusive or shared access to a data item.

### Why Locking?

Without locking, concurrent transactions can produce incorrect results (lost updates, dirty reads, non-repeatable reads). Locking enforces **isolation** by preventing conflicting operations from interleaving.

---

## Lock Types: Shared (S) and Exclusive (X)

### Shared Lock (S-Lock)

- A transaction holding a shared lock on data item X **can read** X but **cannot write** X.
- Multiple transactions can hold shared locks on the same data item simultaneously.
- Also called a **read lock**.

### Exclusive Lock (X-Lock)

- A transaction holding an exclusive lock on data item X **can both read and write** X.
- Only one transaction can hold an exclusive lock on a data item at any time.
- Also called a **write lock**.

### Lock Requests

A transaction requests a lock before accessing a data item:
- `lock-S(X)`: Request shared lock on X.
- `lock-X(X)`: Request exclusive lock on X.
- `unlock(X)`: Release the lock on X.

---

## Lock Compatibility Matrix

The **compatibility matrix** shows whether a new lock request can be granted when a lock is already held on the same data item.

| Requested Lock | Already Held: S | Already Held: X |
|----------------|-----------------|-----------------|
| **S** (Shared) | YES (compatible) | NO (conflict)   |
| **X** (Exclusive)| NO (conflict)  | NO (conflict)   |

**Table Format:**

```
           Lock Held
          S     X
Request  --------
S         Y     N
X         N     N
```

### Explanation

- S-S: Compatible. Two (or more) readers can read simultaneously. No conflict because reads do not modify data.
- S-X: Not compatible. A writer cannot write while a reader is reading (would produce dirty read or non-repeatable read).
- X-S: Not compatible. A reader cannot read while a writer is writing (would read uncommitted data).
- X-X: Not compatible. Two writers cannot write simultaneously (would cause lost update).

### Lock Manager

The **lock manager** is a subsystem of the DBMS that:
- Maintains a **lock table** (hash table mapping data items to lists of held and waiting locks).
- Grants lock requests when compatible.
- Queues lock requests when conflicts exist.
- Detects and resolves deadlocks.

---

## Two-Phase Locking (2PL)

**Two-phase locking (2PL)** is a protocol that ensures conflict serializability. It divides each transaction into two phases:

### Phase 1: Growing Phase

- The transaction **acquires** locks but **never releases** any lock.
- The transaction can obtain locks as needed.

### Phase 2: Shrinking Phase

- The transaction **releases** locks but **never acquires** any new lock.
- Once a lock is released, no more locks can be obtained.

```
Transaction Lifecycle:

  Number of Locks
      |
      |   /----------- Start releasing locks
      |  /            (Shrinking phase begins)
      | /
      |/
      |------------------> Time
      |  Growing    Shrinking
      |  Phase      Phase
```

### Example: 2PL

```
T1:
  lock-X(A)     -- Growing phase (acquire)
  read(A)
  A = A - 500
  write(A)
  lock-X(B)     -- Still growing (acquire)
  read(B)
  B = B + 500
  write(B)
  unlock(A)     -- Shrinking phase begins (release)
  unlock(B)     -- (release)

T2:
  lock-S(A)     -- Growing
  read(A)
  lock-S(B)     -- Growing
  read(B)
  unlock(A)     -- Shrinking
  unlock(B)
```

### Why 2PL Ensures Serializability

2PL ensures that the **locking points** of all transactions form a total order. If T_i acquires its last lock before T_j acquires its last lock, then T_i's data accesses precede T_j's conflicting accesses. This prevents cycles in the precedence graph.

### Theorem

If all transactions follow the 2PL protocol, then all schedules are conflict serializable.

### Limitation: Cascading Rollbacks

2PL allows a transaction to release locks before commit. This can cause **cascading rollbacks**: if T1 releases a lock, T2 reads the data, and then T1 aborts, T2 must also abort (because it read uncommitted data).

```
T1: lock-X(A), write(A), unlock(A), ... abort!
T2:                         lock-S(A), read(A) -- dirty read!
                          T2 must abort too -> cascade
```

---

## Strict 2PL

**Strict two-phase locking (Strict 2PL)** is a refinement of 2PL that addresses the cascading rollback problem.

### Rule

- **All exclusive locks are held until the transaction commits or aborts.**
- Shared locks can be released early (or also held until commit in the rigorous variant).

### Effect

- No transaction can read uncommitted data written by another transaction (because the writer holds its exclusive lock until commit).
- Cascading rollbacks are eliminated.
- Still ensures conflict serializability (like 2PL).

### Example: Strict 2PL

```
T1:
  lock-X(A)
  read(A); A = A - 500; write(A)
  lock-X(B)
  read(B); B = B + 500; write(B)
  unlock(A)     -- Wait! In Strict 2PL, X-locks held until commit.
  unlock(B)
  commit

Actually, in Strict 2PL:
  lock-X(A); read(A); A = A - 500; write(A)
  lock-X(B); read(B); B = B + 500; write(B)
  commit
  unlock(A)    -- locks released after commit
  unlock(B)
```

### Comparison: 2PL vs Strict 2PL

| Aspect            | 2PL                            | Strict 2PL                     |
|-------------------|--------------------------------|--------------------------------|
| Lock release      | X-locks can be released early  | X-locks held until commit/abort|
| Cascading rollbacks| Possible                      | Not possible                   |
| Concurrency       | Higher (locks released earlier)| Lower (locks held longer)      |
| Recovery          | Complex (undo may need to be undone)| Simpler                      |
| Serializability   | Yes                            | Yes                            |

---

## Rigorous 2PL

**Rigorous two-phase locking (Rigorous 2PL)** is even stricter:

### Rule

- **All locks (both shared and exclusive) are held until the transaction commits or aborts.**

This is the most commonly implemented protocol in commercial DBMS.

### Effect

- Simplifies recovery (no dirty writes, no dirty reads).
- Transactions can be serialized in commit order (the order of commit events matches the serialization order).
- Lower concurrency than Strict 2PL, but recovery is significantly simpler.

---

## Deadlock

A **deadlock** occurs when two or more transactions are each waiting for a lock that the other holds, resulting in a circular wait.

### Example: Deadlock

```
T1: lock-X(A)    -- succeeds
T2: lock-X(B)    -- succeeds
T1: lock-X(B)    -- waits (T2 holds X-lock on B)
T2: lock-X(A)    -- waits (T1 holds X-lock on A)

Circular wait: T1 -> B -> T2 -> A -> T1
```

### Deadlock Detection (Wait-For Graph)

The DBMS maintains a **wait-for graph**:
- **Nodes:** Active transactions.
- **Edges:** T_i -> T_j if T_i is waiting for a lock held by T_j.

A cycle in the wait-for graph indicates deadlock.

```
Wait-For Graph for the example:

  T1 ----> T2
   ^        |
   |        |
   +--------+

Cycle detected! DBMS must break the deadlock.
```

### Deadlock Resolution

Once a deadlock is detected, the DBMS **chooses a victim** transaction to abort. Selection criteria:

- Transaction with the fewest locks.
- Transaction that has done the least work.
- Transaction that is the oldest or youngest.
- Rollback cost estimation.

After selecting the victim, the DBMS:
1. Aborts the victim transaction.
2. Releases all its locks.
3. Restarts the victim (optionally).

### Deadlock Prevention

Instead of detecting deadlocks, the DBMS can prevent them by assigning priorities.

#### Wait-Die (Non-Preemptive)

- If T_i (older) requests a lock held by T_j (younger): T_i **waits**.
- If T_i (younger) requests a lock held by T_j (older): T_i **dies** (aborts and restarts).

Rule: Older transaction waits for younger; younger transaction aborts if it conflicts with older.

```
T_i older, T_j younger:
  T_i wants lock held by T_j: T_i waits.
  T_j wants lock held by T_i: T_j dies (aborts).
```

#### Wound-Wait (Preemptive)

- If T_i (older) requests a lock held by T_j (younger): T_i **wounds** T_j (T_j aborts). T_i gets the lock.
- If T_i (younger) requests a lock held by T_j (older): T_i **waits**.

```
T_i older, T_j younger:
  T_i wants lock held by T_j: T_i wounds T_j (T_j aborts).
  T_j wants lock held by T_i: T_j waits.
```

### Comparison: Detection vs Prevention

| Approach         | Pros                              | Cons                              |
|------------------|-----------------------------------|-----------------------------------|
| Detection        | No unnecessary aborts             | Overhead of cycle detection       |
| (Wait-For Graph) | Only aborts when deadlock occurs  | Periodic detection latency        |
| Prevention       | No deadlock overhead              | May abort transactions unnecessarily|
| (Wait-Die / Wound-Wait)| Deterministic, no cycles     | Restart overhead                  |

---

## Deadlock vs Starvation

### Starvation

**Starvation** occurs when a transaction waits indefinitely for a lock because other transactions keep acquiring and releasing the lock before it.

### Example of Starvation

```
T1 requests lock-X(A) repeatedly, but:
  T2 locks-S(A) for a short time, releases.
  T3 locks-S(A) for a short time, releases.
  T2 locks-S(A) again, releases.
  T4 locks-S(A), releases.
  ...
  
T1 never gets the exclusive lock because shared lock requests keep being granted.
```

### Difference from Deadlock

| Aspect        | Deadlock                              | Starvation                           |
|---------------|---------------------------------------|--------------------------------------|
| Progress      | No transaction makes progress         | Only some transactions stuck         |
| Cause         | Circular wait                         | Lock scheduling bias                 |
| Resolution    | Abort one transaction                 | Fair scheduling (e.g., FIFO queue)   |
| Detection     | Wait-for graph cycle                  | Timeout (no specific detection)      |

### Prevention of Starvation

- **First-come-first-served (FCFS):** Grant locks in request order.
- **Priority aging:** Increase the priority of waiting transactions over time.
- **Conditional locking:** `lock-X(A, timeout=10s)` -- if lock not granted within 10 seconds, abort.

---

## Summary Table: Locking Protocols

| Protocol          | Rule                                      | Problems Solved         | Problems Remaining     |
|-------------------|-------------------------------------------|-------------------------|------------------------|
| 2PL               | Acquire all locks before releasing any    | Conflict serializability| Cascading rollbacks    |
| Strict 2PL        | X-locks held until commit/abort           | Cascading rollbacks     | Deadlocks               |
| Rigorous 2PL      | All locks held until commit/abort         | Cascading rollbacks + dirty writes | Deadlocks    |
| Wait-Die          | Older waits, younger dies                 | Deadlocks               | Unnecessary aborts     |
| Wound-Wait        | Older wounds, younger waits               | Deadlocks               | Unnecessary aborts     |

---

## Practice Problems

**Problem 1:** Two transactions T1 and T2 both want to update data items A and B. T1 locks A, T2 locks B. Then T1 requests B, T2 requests A. What is this situation called? Draw the wait-for graph.

<details>
<summary>Answer</summary>

This is a **deadlock**.

Wait-For Graph:
```
T1 ---> T2  (T1 waiting for T2's lock on B)
 ^        |
  \       /
   \     /
    \   /
     \ /
      X
     / \
    /   \
   /     \
  /       \
T2 <--- T1  (T2 waiting for T1's lock on A)
```

Actually just:
```
T1 -> T2 -> T1 (cycle)
```
</details>

**Problem 2:** In the wait-die scheme, T1 (timestamp = 100) holds a lock on X. T2 (timestamp = 200) requests the same lock. What happens?

<details>
<summary>Answer</summary>

T1 is older (smaller timestamp = 100). T2 is younger (timestamp = 200). The rule is: younger requesting from older -> die. T2 aborts (dies) and restarts with its original timestamp (200).
</details>

**Problem 3:** What is the key difference between Strict 2PL and Rigorous 2PL?

<details>
<summary>Answer</summary>

In Strict 2PL, only exclusive (write) locks are held until commit; shared locks can be released earlier. In Rigorous 2PL, ALL locks (both shared and exclusive) are held until commit or abort. Rigorous 2PL simplifies recovery but reduces concurrency slightly more than Strict 2PL.
</details>

**Problem 4:** Consider the schedule: `r1(A) w2(A) r2(B) w1(B)`. Assume 2PL is used with lock requests before each operation. Would this schedule be possible under 2PL? Explain.

<details>
<summary>Answer</summary>

Under 2PL:
- T1: lock-S(A) for read, then later lock-X(B) for write.
- T2: lock-X(A) for write, then lock-S(B) for read? But wait, T2 writes A and reads B.

If T1 reads A first: lock-S(A), r1(A).
Then T2 requests lock-X(A): must wait (S and X conflict). So T2 cannot execute w2(A) until T1 releases its lock on A.

But in the schedule, w2(A) happens after r1(A) but before T1 releases locks. Under 2PL, T1 cannot release lock on A until it enters shrinking phase.

This schedule is NOT possible under 2PL because T2 would be blocked waiting for T1's lock on A.
</details>

**Problem 5:** Is it possible to have a deadlock under Strict 2PL? If yes, provide an example.

<details>
<summary>Answer</summary>

Yes, Strict 2PL does not prevent deadlocks. Example:

```
T1: lock-X(A)  -- granted
T2: lock-X(B)  -- granted
T1: lock-X(B)  -- waits (T2 holds X-lock on B)
T2: lock-X(A)  -- waits (T1 holds X-lock on A)
```

Deadlock (circular wait), even though both use Strict 2PL. The DBMS still needs deadlock detection or prevention.
</details>

---
