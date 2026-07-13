# Write policies

**Course:** Computer Organization and Architecture  
**Module:** 5 | **Lecture:** 9  
**Date:** 03-Nov-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 5  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. Write Policies in Multiprocessors

In a multiprocessor system, multiple CPUs (each with their own cache) share the same main memory. When one processor writes to a memory location, other processors may have a copy of that location in their caches. This creates the **cache coherence problem**: all processors must see a consistent view of memory.

Two fundamental approaches to maintain coherence on writes:

- **Write-Invalidate Protocol:** On a write, all other caches' copies are invalidated.
- **Write-Update Protocol:** On a write, all other caches' copies are updated with the new data.

### 2. Write-Invalidate Protocol

**How it works:**
1. Processor P1 writes to address X.
2. P1's cache controller broadcasts an "invalidate" message on the bus (or via directory).
3. All other caches snoop the bus and invalidate any copy of block X they hold.
4. P1 now has the exclusive (modified) copy.

```
Before P1 writes to X:
  P1 Cache: [X=10]    P2 Cache: [X=10]    Memory: [X=10]

P1 writes X = 20:
  1. P1 updates its cache: [X=20]
  2. P1 broadcasts INVALIDATE for X on bus
  3. P2 snoops INVALIDATE: invalidates its [X=10]
  4. Memory may or may not be updated (depends on write policy)

After:
  P1 Cache: [X=20]    P2 Cache: [X=INV]    Memory: [X=10 or 20]
```

**Advantages:**
- Multiple writes to the same block by the same processor generate only ONE invalidation (first write).
- Low bus traffic for write-intensive workloads.
- Most widely used (basis for MESI, MOESI, etc.).

**Disadvantages:**
- Subsequent reads by other processors miss (need to fetch updated value).
- Invalidation overhead can be high if many processors share data.

### 3. Write-Update Protocol (also called Write-Broadcast)

**How it works:**
1. Processor P1 writes to address X.
2. P1 broadcasts the new data (address + value) on the bus.
3. All other caches that have a copy of X update their copy with the new value.

```
Before P1 writes to X:
  P1 Cache: [X=10]    P2 Cache: [X=10]    Memory: [X=10]

P1 writes X = 20:
  1. P1 updates its cache: [X=20]
  2. P1 broadcasts UPDATE (X, 20) on bus
  3. P2 snoops UPDATE: updates its [X=10] to [X=20]

After:
  P1 Cache: [X=20]    P2 Cache: [X=20]    Memory: [X=10 or 20]
```

**Advantages:**
- Other processors always have the latest data (no read misses after updates).
- Predictable performance for shared read-mostly data.

**Disadvantages:**
- Every write generates a bus transaction (even repeated writes to the same location).
- High bus traffic for write-intensive workloads.
- More complex and less scalable than invalidate.

### 4. MESI Protocol (Illinois Protocol)

The MESI protocol is a **write-invalidate** cache coherence protocol used in most modern processors. Each cache line has a 2-bit state field indicating one of four states:

| State        | Meaning                                                                 |
|--------------|-------------------------------------------------------------------------|
| **M**odified | Line is dirty (modified), exclusive to this cache. Memory copy is stale.|
| **E**xclusive| Line is clean, exclusive to this cache. Memory copy is current.         |
| **S**hared   | Line is clean, may exist in multiple caches. Memory copy is current.    |
| **I**nvalid  | Line is not valid (empty or stale).                                     |

**State transitions on writes:**

**(a) Write Hit in M state:**
- Already modified and exclusive. Stay in M. Update data locally.

**(b) Write Hit in E state:**
- Exclusive and clean. Transition to M. No bus transaction needed (no other cache has a copy).

**(c) Write Hit in S state:**
- Shared (other caches may have copies). Must broadcast an invalidate on the bus. After invalidation, transition to M (exclusive modified).

**(d) Write Miss (all states):**
- Fetch the block from memory (or from another cache), invalidate other copies. Transition to M.

**MESI state transition diagram (simplified for writes):**

```
              Write Hit
              +--------+
              |        v
    +----> [E] -----> [M] <----+
    |         |         |       |
    |   Write |         | Write |
    |   Miss  |         | Hit   |
    |         v         |       |
    |        [I] <-----[S]      |
    |         ^         |       |
    +----+----+---Write|Hit    |
         |            (w/      |
         |          invalidate)|
         +--------------------+
```

**Write behavior examples with MESI:**

**Example 1: Single processor, write-back cache**

```
Action            | State Before | Bus Transaction | State After
------------------+--------------+-----------------+------------
Read A (miss)     | I            | BusRd (read)    | E (exclusive, no other cache has it)
Write A           | E            | None            | M (modified)
Write A again     | M            | None            | M (still modified)
Read B (miss)     | M            | BusRd + WriteBack A (if A is evicted)| E (for B)
```

**Example 2: Two processors, sharing data**

```
Action                          | P1 State  | P2 State  | Bus Transaction
--------------------------------+-----------+-----------+----------------
P1: Read X (miss)               | E         | I         | BusRd
P2: Read X (miss)               | S         | S         | BusRd (P1 supplies data)
P1: Write X (hit in S)          | M         | I         | BusUpgr (invalidate)
P2: Read X (miss)               | S (snoop)| S         | BusRd (P1 writes back, both get it)
P2: Write X (hit in S -> need)  | I         | M         | BusUpgr
  wait, P2 has I (invalidated)  |           |           |
P2: Write X (miss actually)     | I         | M         | BusRd (fetch from P1's write-back)
P2: Write X again               | I         | M         | None
```

**Exclusive state optimization:**
The E state is crucial for performance. If a cache line is in E state, a write hit does NOT need any bus transaction (no invalidation needed since no other cache has it). This saves bus bandwidth compared to always treating a clean line as Shared.

### 5. Write Merging

Write merging is a technique used in write buffers to combine multiple writes to the same cache block before sending them to memory.

**How it works:**
When multiple write entries in the write buffer target the same cache block (or even the same address), they can be combined into a single entry with the latest data.

```
Write buffer before merging:
  Entry 0: Addr=0x100, Data=0xAABBCCDD
  Entry 1: Addr=0x104, Data=0x11223344   (same block as above)
  Entry 2: Addr=0x100, Data=0x55667788   (same address as entry 0)

After write merging:
  Entry 0: Addr=0x100, Data=0x55667788, 0x11223344 (partial)
  Entry 1: empty
```

**Benefits:**
- Reduces the number of memory bus transactions.
- Saves memory bandwidth and power.
- Particularly effective for consecutive word writes (e.g., storing an array).

**Hardware requirement:** Each write buffer entry must have a comparator to check if the incoming address matches any existing entry. If matched, the data is merged into the existing entry's data mask.

### 6. Write-Combining for Graphics Memory

Write-combining is a special write policy used for graphics frame buffers and other write-intensive memory-mapped I/O regions. It is an extension of write merging.

**Characteristics:**
- Multiple writes to consecutive addresses in the same cache block are combined into a single write transaction.
- The writes are NOT cached (write-no-allocate) to avoid cache pollution.
- The writes are committed to memory as a burst (full cache line at a time).

**Where used:**
- Graphics frame buffer updates (pixel writes).
- Memory-mapped I/O regions where data is written but not read back.
- Streaming data writes (e.g., DMA output buffers).

**x86 processors:** Use write-combining (WC) as a memory type, distinct from write-back (WB), write-through (WT), and uncacheable (UC).

```
Memory Type        | Behavior
-------------------+-----------------------------------------------
Uncacheable (UC)   | No caching, no merging, serialized writes
Write-Combining(WC)| No caching, but writes are merged/combined
Write-Through (WT) | Cache reads, write-through policy
Write-Back (WB)    | Cache reads and writes, write-back policy
```

### 7. Performance Analysis of Different Write Policies

**Factors affecting write policy performance:**

1. **Write frequency:** Programs with many writes benefit more from write-back.
2. **Write spatial locality:** Writes to consecutive addresses benefit from write merging.
3. **Cache size:** Larger caches reduce eviction frequency, benefiting write-back.
4. **Memory latency:** Higher memory latency makes write-back more attractive.
5. **Multiprocessor sharing:** High sharing increases coherence traffic, affecting both policies.

**Performance comparison (relative execution time):**

```
Workload Type    | Write-Through | Write-Back | Write-Combining
-----------------+---------------+---------------+-----------------
Scientific (low writes)  | 1.00x | 1.00x        | 1.00x
Database (moderate writes)| 1.15x | 1.00x       | 1.00x
Graphics (high writes)   | 1.40x | 1.10x        | 1.00x
Streaming (write-only)   | 2.00x | 1.50x        | 1.00x
```

**Miss penalty with write-back vs. write-through:**

In write-back, evicting a dirty block adds write-back time to the miss penalty:
```
Miss Penalty (write-back, dirty eviction) = T_read_block + T_write_back
```
where T_write_back is the time to write the old block to memory.

In write-through, no write-back is needed on eviction:
```
Miss Penalty (write-through) = T_read_block
```

However, write-through pays the write penalty on every store, while write-back pays it only on dirty evictions.

### 8. Cache State Transitions on Writes

**Summary table of state transitions for write-back cache with MESI:**

```
Current  | Event          | Bus Action        | New State | Description
---------+----------------+-------------------+-----------+-------------------------
I        | Write Miss     | BusRdX (read+inv) | M         | Fetch block, exclusive modify
E        | Write Hit      | None              | M         | No other cache has it
S        | Write Hit      | BusUpgr (inval)   | M         | Invalidate other copies
M        | Write Hit      | None              | M         | Already modified
S        | Snoop: BusRd   | Provide data      | S         | Shared read from another CPU
E        | Snoop: BusRd   | Provide data      | S         | Give up exclusivity
M        | Snoop: BusRd   | Write-back + data | S         | Supply data, memory updated
M        | Snoop: BusRdX  | Write-back + data | I         | Another CPU wants to write
S        | Snoop: BusRdX  | None              | I         | Invalidated by another CPU's write
E        | Snoop: BusRdX  | None              | I         | Invalidated by another CPU's write
```

### 9. Worked Example: Cache State Transitions on Writes

**System:** Two processors (P1, P2), each with write-back cache using MESI protocol.

**Sequence of operations:**

```
Step | Operation       | P1 State | P2 State | Bus Traffic       | Notes
-----+-----------------+----------+----------+-------------------+----------------------
1    | P1: Read A      | E        | I        | BusRd             | A brought from memory
2    | P1: Write A=5   | M        | I        | None              | E->M transition
3    | P1: Write A=10  | M        | I        | None              | Stays in M
4    | P2: Read A      | S        | S        | BusRd + WriteBack | P1 supplies data (flush)
     |                 |          |          | (P1 writes back)  | M->S transition
5    | P2: Write A=20  | I        | M        | BusUpgr           | P2 broadcasts invalidate
     |                 |          |          |                   | P1: S->I
6    | P2: Write A=30  | I        | M        | None              | Stays in M (exclusive)
7    | P1: Read A      | S        | S        | BusRd + WriteBack | P2 supplies data
     |                 |          |          |                   | P2: M->S
8    | P1: Write A=40  | M        | I        | BusUpgr           | Invalidate P2
     |                 |          |          |                   | P2: S->I
```

**Key observations:**
- No bus traffic for M->M or E->M transitions (exclusive access).
- BusRdX (read+invalidate) is used for write misses.
- BusUpgr (upgrade/invalidate) is used for write hits in S state.
- Dirty data is never lost; the owning cache supplies it on snoop reads.

---

## Practice Problems

**Problem 1:** In the MESI protocol, why is there a separate Exclusive (E) state instead of directly putting a fetched block in Shared (S) state?

**Answer:** The E state allows a processor to write to a cache line without any bus transaction. If the line were always in S on a read miss, then the first write would require a BusUpgr (invalidate) transaction. The E state saves this bus transaction when no other cache has the block, significantly reducing bus traffic for private data.

**Problem 2:** Differentiate between write-invalidate and write-update protocols.

**Answer:** Write-invalidate: on a write, other caches' copies are invalidated (marked as unusable). Write-update: on a write, other caches' copies are updated with the new data. Invalidate generates less bus traffic for repeated writes but causes read misses; update avoids read misses but generates bus traffic on every write.

**Problem 3:** A write buffer has 4 entries. The CPU performs writes to addresses 0x100, 0x104, 0x108, 0x10C (all in the same 16-byte block). Without write merging, how many bus transactions? With write merging?

**Answer:** Without merging: 4 bus transactions (one per write). With merging: the write buffer combines all 4 writes into a single bus transaction writing the full 16-byte block. Only 1 bus transaction.

**Problem 4:** Explain write-combining and why it is useful for graphics memory.

**Answer:** Write-combining merges multiple writes to the same cache block into a single burst write to memory. It is useful for graphics frame buffers because pixel writes are sequential and write-only (never read back). Without write-combining, each pixel write would generate a separate bus transaction; combining them into bursts of 64 bytes dramatically reduces bus traffic and improves performance.

**Problem 5:** In a MESI protocol, P1 has block X in M state. P2 does a BusRd for X. What happens? What are the final states?

**Answer:** P1 snoops the BusRd, recognizes it has the modified (dirty) data, writes the block back to memory (so memory is updated), and also supplies the data directly to P2 on the bus. P1 transitions from M to S (shared). P2 gets the data and transitions from I to S (shared). Both now have clean, shared copies.
