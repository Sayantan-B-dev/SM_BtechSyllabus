# Write policies

**Course:** Computer Organization and Architecture  
**Module:** 5 | **Lecture:** 8  
**Date:** 28-Oct-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 5  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. Write Policies Overview

When the CPU writes data to memory, the cache must coordinate the update. Write policies determine how and when the main memory copy is updated. The two fundamental write policies are **write-through** and **write-back**.

### 2. Write-Through Policy

**Definition:** On a write hit, data is written to both the cache line AND the main memory simultaneously (or in quick succession). The cache and memory always have identical data (cache is always consistent with memory).

```
CPU Write Request (address A, data D)
         |
    +----+----+
    | Cache   |
    | Lookup  |
    +----+----+
         |
    +----+------+
    | Hit?      |
    +----+------+
         |
    Yes  |
    +----+----+     +-----------+
    | Write   |---->| Write     |
    | to Cache|     | to Main   |
    +---------+     | Memory    |
                    +-----------+
```

**Advantages:**
- **Simple:** Memory always has the latest data. No special handling on cache eviction.
- **Reliable:** If the cache fails, memory data is still current.
- **Easy for I/O:** DMA and other I/O devices can read directly from main memory without checking the cache.
- **Easy for multiprocessors:** Snooping protocols are simpler because memory always has valid data.

**Disadvantages:**
- **Slow:** Every write must go to main memory (high latency, ~100 ns). The CPU may stall waiting for the write to complete.
- **High bus traffic:** Writes consume memory bus bandwidth, even for repeated writes to the same location.
- **Energy inefficient:** Each write causes DRAM activations.

**Write Buffer for Write-Through:**

To mitigate the speed issue, a **write buffer** is used. The CPU writes to the cache and write buffer simultaneously. The write buffer then drains to main memory asynchronously.

```
CPU ---> Cache
   |        ^
   |        |
   +--> Write Buffer ---> Main Memory
         (FIFO queue)
```

- **Write buffer absorbs bursts:** CPU can continue executing while the buffer drains.
- **Stall conditions:** CPU stalls only if the write buffer is full.
- **Read after write hazard:** If a subsequent read misses the cache and looks at stale memory, the write buffer must be checked (write buffer snooping).

### 3. Write-Back Policy (also called Copy-Back)

**Definition:** On a write hit, data is written ONLY to the cache line. The memory copy is NOT updated immediately. Memory is updated only when the cache line is evicted (replaced).

```
CPU Write Request (address A, data D)
         |
    +----+----+
    | Cache   |
    | Lookup  |
    +----+----+
         |
    +----+------+
    | Hit?      |
    +----+------+
         |
    Yes  |
    +----+----+
    | Write   |  Set dirty bit = 1
    | to Cache|
    +----+----+

... Later, when this block is evicted:

    +---------+
    | Dirty?  |--- No --> Just discard (memory is current)
    +---------+
         |
        Yes
         |
    +----+----+
    | Write   |
    | block   |
    | to Main |
    | Memory  |
    +---------+
```

**Dirty bit (also called modify bit):**
Each cache line has a dirty bit (1 bit):
- `0` (Clean): Cache copy matches memory copy. No write-back needed on eviction.
- `1` (Dirty): Cache copy has been modified. Memory copy is stale. On eviction, the block must be written back to memory.

**Advantages:**
- **Fast:** Writes only go to cache (1-2 cycles), no main memory access latency.
- **Low bus traffic:** Multiple writes to the same block generate only one memory write (when evicted).
- **Efficient for write-intensive workloads:** Saves memory bandwidth.

**Disadvantages:**
- **Complex:** Memory can become stale. On eviction, must check dirty bit and possibly write back.
- **I/O complexity:** DMA and other bus masters must check cache or be explicitly notified (cache coherency).
- **Cache coherency:** In multiprocessors, one processor may have dirty data for a location that another processor wants to read. Coherency protocols (like MESI) are needed.
- **Eviction penalty:** Evicting a dirty block adds a memory write latency to the miss service time.

### 4. Write Miss Policies

When the CPU writes to an address that is NOT in the cache (write miss), two options exist:

**(a) Write-Allocate (Fetch on Write)**
- On a write miss, the block is fetched from main memory into cache first, then the write is performed on the cache.
- Used typically with write-back caches.
- Rationale: Anticipates future reads/writes to the same block (spatial / temporal locality).

```
Write Miss -> Fetch block from memory -> Place in cache -> Write to cache (set dirty=1)
```

**(b) Write-No-Allocate (Write Around / No Fetch on Write)**
- On a write miss, the data is written directly to main memory WITHOUT bringing the block into cache.
- Used typically with write-through caches.
- Rationale: If the program writes a block and never reads it (e.g., streaming writes), caching it wastes space.

```
Write Miss -> Write directly to main memory (cache unchanged)
```

### 5. Advantages and Disadvantages Summary

```
Write Policy | Write Miss  | Advantages                     | Disadvantages
-------------+-------------+--------------------------------+------------------------------
Write-through| No-allocate | Simple, memory always current  | Slow writes, high bus traffic
Write-through| Allocate    | Good for temporal writes       | Slower miss handling
Write-back   | Allocate    | Fast writes, low bus traffic   | Complex eviction, stale memory
Write-back   | No-allocate | Good for streaming writes      | Miss on later reads
```

### 6. Write Buffer for Write-Through

A write buffer is a small FIFO queue that holds write addresses and data waiting to be written to main memory.

```
Structure:
+------+------+------+------+------+
| Addr | Addr | Addr | Addr | Addr |
| Data | Data | Data | Data | Data |
+------+------+------+------+------+
  Head                         Tail
  (next to drain)              (next to fill)
```

**Operation:**
1. On a write hit: CPU writes to cache AND pushes address+data into write buffer (fast, buffer is on-chip SRAM).
2. Write buffer controller drains entries to main memory as bus bandwidth permits.
3. CPU stalls only if write buffer is full (buffer full condition).

**Depth:** Typical write buffer depth: 4-8 entries.

**Coherency considerations:**
- On a subsequent read miss: The snooping logic must check both the cache AND the write buffer. If the write buffer contains the requested address, the latest data is in the buffer (not memory).
- On a read hit to a line that has a pending write in the buffer: The cache already has the latest data (write-through updates cache simultaneously), so no issue.

### 7. Snooping Implications

**Snooping** is the process by which cache controllers monitor (snoop) the bus to maintain cache coherence.

**Write-through and snooping:**
- Simple: Since memory always has current data, a snooping cache only needs to invalidate its copy if another processor writes to that address.
- Snoop hit on write-through: The writing processor broadcasts the write address on the bus. Other caches snoop the address and invalidate their copy if present.

**Write-back and snooping:**
- Complex: Memory may NOT have current data. A snooping cache that wants to read a block must find the processor that holds the dirty copy.
- Snoop hit on write-back: The snooping cache must signal the owning processor to supply the data (or write it back to memory first).
- Requires a protocol like MESI, MOESI, etc. (detailed in L09).

### 8. Comparison Table

```
Feature                    | Write-Through                     | Write-Back
---------------------------+-----------------------------------+-----------------------------------
Write hit action           | Write cache + write memory        | Write cache only
Write miss action (common) | Write-no-allocate (write memory)  | Write-allocate (fetch block first)
Memory always consistent   | Yes                               | No (memory can be stale)
Write latency seen by CPU  | Memory write latency (unless buf) | Cache write latency (fast)
Bus traffic per write      | One bus transaction (write)       | Zero (dirty bit set)
Bus traffic per eviction   | Zero (memory already current)     | One write if dirty
Dirty bit needed           | No                                | Yes (1 bit per line)
Hardware complexity        | Lower                             | Higher
Suitability for I/O        | Good (memory is always current)   | Poor (needs cache flushing)
Multiprocessor support     | Simpler                           | Needs complex coherency protocol
Energy consumption         | Higher (many memory writes)       | Lower (fewer memory writes)
Typical use                | L1 caches (some systems)          | L2/L3 caches, some L1
```

### 9. Worked Example: Write-Through vs Write-Back

**Scenario:** A program writes to the same 32-byte block 100 times.

**Write-through (no write buffer):**
- Write 1: write cache + write memory (100 ns)
- Write 2: write cache + write memory (100 ns)
- ...
- Write 100: write cache + write memory (100 ns)
- Total write time: 100 * 100 ns = 10,000 ns (ignoring cache write time)

**Write-through (with 4-entry write buffer, can burst):**
- Same: 100 writes, but CPU may not stall if buffer drains fast enough.
- If buffer drains at bus speed (e.g., 10 ns per write): CPU still generates writes at cache speed. Buffer absorbs bursts.
- Best case: CPU sees ~1-2 ns per write (cache speed), total = 100 * 2 = 200 ns (plus eventual buffer drain overhead).

**Write-back:**
- All 100 writes go to cache only (~1-2 ns each) = 200 ns total.
- On eviction: one block write-back to memory (100 ns + 32-byte transfer).
- Total write time: approximately 200 ns + 100 ns = 300 ns (amortized over many evictions).
- Far better than write-through without buffer.

---

## Practice Problems

**Problem 1:** Distinguish between write-through and write-back policies.

**Answer:** Write-through: every write goes to both cache and main memory; memory is always consistent. Write-back: writes go only to cache; memory is updated only when the dirty block is evicted. Write-through is simpler but slower; write-back is faster but more complex.

**Problem 2:** In a write-back cache, what is the purpose of the dirty bit?

**Answer:** The dirty bit indicates whether the cache line has been modified (written to) since it was loaded from memory. If dirty (1), the block must be written back to memory on eviction. If clean (0), the block can be discarded without writing back because memory already has the current data.

**Problem 3:** A program writes to addresses 0x1000, 0x1004, 0x1008, and 0x100C (all in the same 16-byte block). Compare the number of memory bus transactions for write-through (no-allocate) vs. write-back (allocate).

**Answer:** Write-through: 4 write transactions (one for each write to memory). Write-back (allocate): 1 read transaction (fetch block on first write miss) + 1 write transaction (write-back on eviction) = 2 memory transactions. Write-back uses fewer bus transactions.

**Problem 4:** Explain why write-allocate is typically paired with write-back, and write-no-allocate with write-through.

**Answer:** Write-allocate fetches the block on a write miss, which pairs well with write-back because subsequent writes hit the cache and set dirty bits, reducing memory traffic. Write-no-allocate skips the cache on writes, which pairs well with write-through because the data is written directly to memory anyway -- no benefit from caching it. Write-allocate with write-through would cause unnecessary read traffic (fetch block just to write to it and memory).

**Problem 5:** A write-through cache has a write buffer with 4 entries. The CPU does 10 consecutive writes followed by a read that misses. The write buffer drains at 1 entry per 10 ns. The read miss takes 100 ns to fetch from memory. How long does the CPU stall, assuming the CPU can proceed while writes are buffered but must wait for the write buffer to drain before the read can proceed?

**Answer:** After 10 writes, write buffer has 10 entries but only 4 slots. So after 4 writes (buffer full), the 5th write stalls until at least 1 slot opens. Minimum stall: 10 writes need 10 drain cycles at 10 ns = 100 ns. The last write completes at the drain end. Actually, CPU does writes at cache speed (instant). After all 10 writes, buffer has 10 entries. Next read miss: the read must wait for the write buffer to empty (to avoid reading stale data from memory). Drain 10 entries at 10 ns each = 100 ns stall. Then read miss takes 100 ns. Total stall = 100 (drain) + 100 (read) = 200 ns.
