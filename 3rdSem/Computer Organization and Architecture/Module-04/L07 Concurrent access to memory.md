# Concurrent access to memory

**Course:** Computer Organization and Architecture  
**Module:** 4 | **Lecture:** 7  
**Date:** 29-Sep-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 4  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Cache Coherence Problem

In a shared-memory multiprocessor system, each processor typically has its own private cache. When multiple processors cache copies of the same memory block, and one processor writes to its cached copy, the other copies become **stale** (incoherent). The **cache coherence problem** is ensuring that all caches see a consistent view of memory.

### The Problem Illustrated

Consider two processors P0 and P1, both with private caches, sharing main memory:

```
Initial state: X = 10 in main memory.

Step 1: P0 reads X  -> P0's cache gets X=10 (copy from memory)
Step 2: P1 reads X  -> P1's cache gets X=10 (copy from memory)
Step 3: P0 writes X=20 -> P0's cache has X=20. Memory may or may not be updated.
Step 4: P1 reads X  -> Is X=10 (stale) or X=20?
```

**Problem**: After P0 writes X=20, P1's cache still has X=10. If P1 reads its cached copy, it gets the stale value. This is the **cache coherence problem**.

### Formal Definition

A memory system is **coherent** if:
1. A read by processor P to address X, after a write by P to X (with no other writes in between), returns the written value.
2. A read by processor P to address X, after a write by another processor Q to X, returns the written value if sufficient time has elapsed.
3. Writes to the same address are serialized: all processors see writes in the same order.

## Cache Coherence Protocols

A **cache coherence protocol** ensures that all caches have a consistent view of memory. There are two fundamental approaches:

### Write-Invalidate Protocol

When a processor writes to a cached block, it **invalidates** all other cached copies. The writing processor now has the only valid copy (exclusive ownership).

```
Step 1: P0 reads X  -> P0 cache: X=10 (Shared)
Step 2: P1 reads X  -> P1 cache: X=10 (Shared)
Step 3: P0 writes X=20 -> P0 cache: X=20 (Modified)
                         P1 cache: X=10 (Invalidated!)
                         Bus signal: "Invalidate X" broadcast
Step 4: P1 reads X  -> Cache miss! P1 sees invalidation.
                       P1 reads from P0's cache (or memory via P0's write-back)
                       P1 cache: X=20 (Shared)
```

**Key**: On write, ALL other copies are invalidated. Subsequent reads by other processors miss and fetch the new value.

**Advantage**: Only one invalidation message per write (not per-reader).
**Disadvantage**: A write causes other processors to miss on their next read.

### Write-Update Protocol

When a processor writes to a cached block, it **updates** all other cached copies with the new value.

```
Step 1: P0 reads X  -> P0 cache: X=10 (Shared)
Step 2: P1 reads X  -> P1 cache: X=10 (Shared)
Step 3: P0 writes X=20 -> P0 cache: X=20 (Updated)
                         P1 cache: X=20 (Updated!)
                         Bus signal: "Update X to 20" broadcast
Step 4: P1 reads X  -> Cache hit! X=20 (updated)
```

**Key**: On write, ALL other copies are updated with the new value.

**Advantage**: Other processors always have up-to-date data (no write-miss on next read).
**Disadvantage**: Frequent update broadcasts consume bus bandwidth, especially for multiple writes to the same location.

### Comparison: Invalidate vs Update

| Aspect | Write-Invalidate | Write-Update |
|---|---|---|
| On write to shared block | Invalidate all other copies | Update all other copies |
| Subsequent read by others | Cache miss (fetch new value) | Cache hit (has updated value) |
| Bus traffic for single write | 1 invalidation message | N update messages (one per sharer) |
| Multiple writes | 1 invalidation + 1 write-back | N updates per write |
| Preferred when | Multiple writes between reads | Many reads between writes |

Write-invalidate is more commonly used due to lower bus traffic in common scenarios. Most modern processors use write-invalidate protocols (e.g., MESI).

## Snooping Protocols

In a **snooping protocol**, all caches **snoop** (monitor) the bus for transactions. Each cache controller watches the bus and takes appropriate action when it sees a transaction that affects a block it holds.

### How Snooping Works

1. When a processor wants to access a cache block, it sends a request on the bus.
2. All other cache controllers observe the request.
3. If another cache has the requested block, it responds (supplies data or signals its state).
4. The requesting cache updates its state accordingly.

```
Bus:
+---+    +---+    +---+
| P0|    | P1|    | P2|
|Cac|    |Cac|    |Cac|
+---+    +---+    +---+
  |        |        |
  +--------+--------+--- Bus
           |
        +------+
        |Memory|
        +------+

P0's cache controller snoops all bus transactions from P1 and P2.
P1's cache controller snoops all bus transactions from P0 and P2.
P2's cache controller snoops all bus transactions from P0 and P1.
```

**Limitation**: Bus-based snooping does not scale well beyond 8-16 processors because the shared bus becomes a bottleneck.

## MESI Protocol

**MESI** (Modified, Exclusive, Shared, Invalid) is the most widely used write-invalidate cache coherence protocol. It is also known as the **Illinois protocol**.

### Four States

| State | Description | This cache has valid data | Other caches have copy | Memory has valid copy |
|---|---|---|---|---|
| **M** (Modified) | Cache line is modified (dirty). Only this cache has the valid copy. Memory is stale. | Yes | No | No |
| **E** (Exclusive) | Cache line is clean. Only this cache has the copy. Memory is up-to-date. | Yes | No | Yes |
| **S** (Shared) | Cache line is clean. May exist in other caches. Memory is up-to-date. | Yes | Yes | Yes |
| **I** (Invalid) | Cache line does not contain valid data. | No | -- | -- |

### State Transition Diagram

```
                    +-----------+
                    |           |
                    v           |
    +--------+   Read hit   +--------+
    |        | -----------> |        |
    |   I    |              |   S    |
    |        | <----------- |        |
    +--------+   Write by   +--------+
        |       another CPU     |
        | Read miss             | Write hit
        | (no sharer)           | (invalidate others)
        v                       v
    +--------+              +--------+
    |        |              |        |
    |   E    |              |   M    |
    |        |              |        |
    +--------+              +--------+
        |                       |
        | Read miss             | Read miss
        | (sharer exists)       | (sharer exists)
        +---->----+------->----+
                  |   S    |
                  +--------+
```

### Detailed State Transitions

The following table shows all transitions based on local and remote (bus) operations:

**Local processor operations (requests from this CPU)**

| Current State | Operation | Action | Next State | Bus Transaction |
|---|---|---|---|---|
| I | Read hit | -- | I | -- (impossible) |
| I | Read miss (no sharer) | Fetch from memory | E | BusRd (read) |
| I | Read miss (sharer exists) | Fetch from memory or other cache | S | BusRd (read) |
| I | Write miss (no sharer) | Fetch block, modify | M | BusRdX (read exclusive) |
| I | Write miss (sharer exists) | Invalidate others, fetch, modify | M | BusRdX |
| E | Read hit | Use cache data | E | None |
| E | Write hit | Modify cache | M | None (silent upgrade) |
| S | Read hit | Use cache data | S | None |
| S | Write hit | Modify cache, invalidate others | M | BusUpgr (upgrade) |
| M | Read hit | Use cache data | M | None |
| M | Write hit | Modify cache | M | None |

**Bus operations observed by snooping (transactions from other CPUs)**

| Current State | Bus Transaction Observed | Action | Next State |
|---|---|---|---|
| E | BusRd (read request by another) | Supply data if requested, share | S |
| S | BusRd (read request by another) | Keep shared, no change | S |
| S | BusUpgr (upgrade by another) | Invalidate local copy | I |
| M | BusRd (read request by another) | Flush data to memory/bus, share | S |
| M | BusRdX (read-exclusive by another) | Flush data to memory/bus | I |
| E | BusRdX | Invalidate | I |
| I | Any | No action | I |

### Example: MESI State Transitions

Consider three processors P0, P1, P2. Initial state: all caches empty, X = 5 in memory.

```
Step 1: P0 reads X
  - BusRd issued by P0.
  - No other cache has X; memory supplies data.
  - P0 cache: X=5 in state E (Exclusive, only copy, clean).
  - State: P0=E

Step 2: P1 reads X
  - BusRd issued by P1.
  - P0 snoops: sees BusRd, has X in E, transitions to S.
  - P0 supplies data to P1 (or memory does).
  - Both P0 and P1: X=5 in state S (Shared).
  - State: P0=S, P1=S

Step 3: P2 reads X
  - BusRd issued by P2.
  - P0 and P1 snoop: they have X in S, respond.
  - All three have X=5 in state S.
  - State: P0=S, P1=S, P2=S

Step 4: P0 writes X=10
  - P0 has X in S. Write hit requires BusUpgr (upgrade).
  - P0 broadcasts BusUpgr on bus.
  - P1 and P2 snoop: they have X in S, invalidate their copies.
  - P1: X=5 -> I (Invalid).
  - P2: X=5 -> I (Invalid).
  - P0: X=10 -> M (Modified). No bus write (write-back cache).
  - State: P0=M, P1=I, P2=I

Step 5: P2 reads X
  - P2 has X in I (miss). BusRd issued.
  - P0 snoops: sees BusRd, has X in M. P0 flushes X=10 to memory and bus.
  - P0 transitions to S (copy exists elsewhere).
  - P2 gets X=10 from bus/memory, state S.
  - Memory now updated to X=10.
  - State: P0=S, P1=I, P2=S

Step 6: P1 writes X=20
  - P1 has X in I (miss). BusRdX (read exclusive) issued.
  - P0 snoops: has X in S, invalidates (I).
  - P2 snoops: has X in S, invalidates (I).
  - Memory supplies X=10 to P1.
  - P1 modifies to X=20, state M.
  - State: P0=I, P1=M, P2=I
```

### Bus Transactions

| Transaction | Meaning | Caused by |
|---|---|---|
| BusRd | Read block (shared) | Read miss, no intent to write |
| BusRdX | Read block exclusively (intent to write) | Write miss |
| BusUpgr | Upgrade from S to M | Write hit on S block |
| Flush | Write back modified block to memory | M block evicted or snooped |

---

## Practice Problems

**Problem 1**: Consider a 2-processor system with MESI protocol. Initially, both caches are empty. Trace the states for:
```
P0: Read X
P1: Read X
P1: Write X = 50
P0: Read X
```

**Answer**:
- P0 Read X: P0=E (BusRd, no sharer)
- P1 Read X: P0=S, P1=S (BusRd, P0 shares)
- P1 Write X=50: P1=M, P0=I (BusUpgr, P0 invalidates)
- P0 Read X: P0=S, P1=S (BusRd, P1 flushes to S)

**Problem 2**: In a write-update protocol, how many bus messages are needed for: 4 processors share block X, then P0 writes X 3 times, then P1 reads X?

**Answer**: Write-update: Each write broadcasts update to all 3 other processors = 3 messages x 3 writes = 9 update messages. No subsequent read miss for P1 (already updated). Total: 9 bus messages.
Write-invalidate: First write broadcasts 1 invalidation. P1's subsequent read misses (1 read broadcast). For 3 writes: 1 invalidation + 1 write-back + 1 read = 3 messages (much less).

**Problem 3**: In MESI, why does a read miss on a block in state I with no sharer result in Exclusive (E) state instead of Shared (S)?

**Answer**: Because the requesting processor will be the only one with a copy. Marking it E allows the processor to silently upgrade to M on a subsequent write (no BusUpgr needed), saving a bus transaction.

**Problem 4**: What happens in MESI when a cache in state M receives a BusRd from another processor?

**Answer**: The cache supplies the modified data to the bus (so the requester and memory get it). Then it transitions from M to S (shared). Memory is updated with the flushed data.

**Problem 5**: A system uses write-invalidate with 4 caches. A block is in state S in all 4 caches. P0 writes to the block. How many messages? Now P1 writes again. How many messages?

**Answer**: First write (P0, S hit): Broadcast BusUpgr, 3 invalidations sent (1 message, received by 3 caches). P0 goes to M, others to I. Second write (P1, I miss): Broadcast BusRdX (1 message). P0 snoops, flushes data, goes to I. P1 gets data, goes to M. One more message for the flush = 2 messages. Total: 1 + 2 = 3 bus messages.
