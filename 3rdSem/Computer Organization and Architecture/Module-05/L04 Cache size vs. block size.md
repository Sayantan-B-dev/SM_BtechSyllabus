# Cache size vs. block size

**Course:** Computer Organization and Architecture  
**Module:** 5 | **Lecture:** 4  
**Date:** 13-Oct-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 5  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. Effect of Cache Size on Hit Ratio

The cache size (total data capacity) directly affects the hit ratio. Larger caches can hold more blocks, reducing the probability that a requested block has been evicted.

**Relationship:**

```
Cache Size (KB)   |   Hit Ratio (typical)
------------------------------------------
     1            |       0.50 - 0.70
     4            |       0.75 - 0.85
    16            |       0.85 - 0.93
    64            |       0.90 - 0.96
   256            |       0.93 - 0.98
  1024            |       0.95 - 0.99
```

**Key observations:**
- Increasing cache size generally increases the hit ratio.
- The relationship follows a law of diminishing returns: doubling a small cache significantly improves the hit ratio, but doubling a large cache gives a smaller improvement.
- Very large caches eventually approach the hit ratio limit (slightly below 1.0) because of compulsory misses and limited locality in the program.

**Trade-off:**
- Larger cache = higher hit ratio = better performance.
- Larger cache = slower access time (longer wires, larger tag memory, more complex decoding).
- Larger cache = higher cost and power consumption.
- There is an optimal cache size that balances hit ratio improvement against access time penalty.

### 2. Effect of Block Size on Hit Ratio

Block size (also called line size) is the unit of data transfer between cache and main memory. Typical block sizes are 16, 32, 64, or 128 bytes.

**Impact of larger blocks:**
- **Spatial locality benefit:** When a word is accessed, nearby words are brought into cache. If the program accesses these nearby words (spatial locality), future accesses hit in cache.
- **Fewer blocks:** For a fixed cache size, larger blocks mean fewer blocks can be stored. This increases conflict and capacity misses because the cache holds fewer distinct blocks.
- **Larger miss penalty:** Transferring a larger block from main memory takes more time, increasing the cost of a miss.

**Impact of smaller blocks:**
- **More blocks:** More distinct blocks fit in cache, reducing conflict and capacity misses.
- **Less spatial locality benefit:** If the program accesses sequential addresses, smaller blocks may miss more often because nearby words were not prefetched.
- **Smaller miss penalty:** Transfer time is shorter.

### 3. Miss Rate vs. Block Size Graph Description

```
Miss
Rate
 |
 |    *
 |   *  *
 |   *    *
 |  *      *
 |  *        *
 | *          *
 |*             *
 |*               *
 +-------------------------> Block Size
  16  32  64  128  256  (bytes)
```

**Interpretation:**
- Very small blocks (16 bytes): High miss rate because spatial locality is not exploited -- each new word access often requires a new block fetch.
- Moderate blocks (32-64 bytes): Lowest miss rate -- good balance of spatial locality exploitation and number of blocks.
- Large blocks (128+ bytes): Miss rate starts increasing because the cache holds too few blocks, causing more conflict and capacity misses. The additional spatial locality benefit saturates.
- Very large blocks (256+ bytes): Miss rate increases significantly, and the miss penalty (transfer time) also increases.

The optimal block size depends on:
- Cache size (larger caches can support larger blocks)
- Program characteristics (spatial locality pattern)
- Memory latency and bandwidth

### 4. The Three Cs of Cache Misses (3 Cs Model)

Proposed by Mark Hill, this model categorizes all cache misses into three types:

**(a) Compulsory Misses (Cold Start Misses)**
- Caused by the first access to a block that has never been in the cache.
- Occur regardless of cache size or associativity.
- Also called "cold misses" or "first reference misses."
- **Reduction:** Increase block size (prefetch more data on first access), use prefetching.

**(b) Capacity Misses**
- Caused when the cache cannot contain all the blocks needed during program execution.
- Occur because the working set of the program is larger than the cache.
- **Reduction:** Increase cache size, improve program locality.

**(c) Conflict Misses (Collision Misses)**
- Caused when multiple blocks map to the same cache line/set and compete for that location.
- Occur in direct-mapped and set-associative caches (not in fully associative).
- Even if the cache is large enough to hold the working set, conflicts cause misses.
- **Reduction:** Increase associativity, increase cache size, use better mapping functions.

**Summary table:**

```
Miss Type     | Cause                                    | Reduction Strategy
--------------+------------------------------------------+--------------------------------
Compulsory    | First access to a block                  | Larger blocks, prefetching
Capacity      | Working set > cache size                 | Larger cache, loop blocking
Conflict      | Multiple blocks mapping to same location | Higher associativity, larger cache
```

**Distribution (typical):**
The relative proportion depends on cache design:

```
                    Direct-Mapped   |   Fully Associative
                    (small cache)   |   (same size)
Compulsory:            5%           |       5%
Capacity:             25%           |      45%
Conflict:             70%           |       0%  (no conflicts)
Total miss rate:     10%           |      6.8%
```

Note: Conflict misses dominate in direct-mapped caches. Increasing associativity converts conflict misses into capacity misses (since blocks can go anywhere, evictions only happen when the cache is truly full).

### 5. Optimal Block Size

The optimal block size minimizes the product of miss rate and miss penalty, or equivalently maximizes performance.

**Trade-off analysis:**

```
+------------------+-------------------------+-------------------------+
| Block Size       | Advantage               | Disadvantage            |
+------------------+-------------------------+-------------------------+
| Small (16 B)     | Many blocks in cache    | Poor spatial locality   |
|                  | Small miss penalty      | High compulsory miss rate|
+------------------+-------------------------+-------------------------+
| Medium (32-64 B) | Good spatial locality   | Moderate miss penalty   |
|                  | Reasonable # of blocks  |                         |
+------------------+-------------------------+-------------------------+
| Large (128+ B)   | Excellent spatial loc.  | Few blocks in cache     |
|                  | Low compulsory miss rate| High miss penalty       |
|                  |                         | High conflict/capacity  |
+------------------+-------------------------+-------------------------+
```

For most general-purpose processors, 64-byte blocks have been found to be near-optimal for L1 caches, and 64-128 bytes for L2/L3 caches.

**Worked Example: Effect of block size on miss rate**

Consider a 16 KB direct-mapped cache with 32-bit addresses. Evaluate different block sizes.

```
Block Size | # Blocks | Index bits | Tag bits | Remarks
-----------+----------+------------+----------+---------
16 B       | 1024     | 10         | 18       | Many blocks, small spatial benefit
32 B       | 512      | 9          | 19       | Good balance
64 B       | 256      | 8          | 20       | Good balance (commonly used)
128 B      | 128      | 7          | 21       | Fewer blocks, higher conflict
256 B      | 64       | 6          | 22       | Too few blocks, high conflict
```

For a program with good spatial locality (e.g., array traversal), 64-byte blocks typically give the best performance. For programs with poor spatial locality (random access), smaller blocks may be better.

---

## Practice Problems

**Problem 1:** A 32 KB direct-mapped cache has 64-byte blocks. How many blocks does the cache hold? How many index bits are needed?

<details>
<summary>Show Answer</summary>
Number of blocks = 32 KB / 64 B = 32,768 / 64 = 512 blocks. Index bits = log2(512) = 9 bits.
</details>

**Problem 2:** A program's working set is 512 KB. If you have a 256 KB cache, which type of miss will dominate? Why?

<details>
<summary>Show Answer</summary>
Capacity misses will dominate because the working set (512 KB) is twice the cache size (256 KB). The cache cannot hold the entire working set, so blocks will be evicted and later re-fetched.
</details>

**Problem 3:** A direct-mapped cache has a 5% miss rate. Converting it to 4-way set-associative (same size) reduces the miss rate to 3%. What percentage of the original misses were conflict misses?

<details>
<summary>Show Answer</summary>
Original miss rate = 5%. After removing conflicts (associative), miss rate = 3%. Remaining misses are compulsory + capacity = 3%. So conflict misses = 5% - 3% = 2% of total accesses. As a fraction of original misses: 2/5 = 40% of misses were conflict misses.
</details>

**Problem 4:** Explain in one sentence each: compulsory miss, capacity miss, conflict miss.

<details>
<summary>Show Answer</summary>
Compulsory miss: first-ever access to a block. Capacity miss: cache too small for the program's working set. Conflict miss: multiple blocks compete for the same cache location due to limited associativity.
</details>

**Problem 5:** If you increase block size from 32 bytes to 128 bytes in a fixed-size cache, the number of blocks decreases by what factor? How does this affect conflict misses?

<details>
<summary>Show Answer</summary>
Number of blocks decreases by a factor of 4 (128/32 = 4). Fewer blocks means fewer unique cache lines, so more main memory blocks compete for each cache line (higher conflict probability). Conflict misses increase. However, compulsory misses may decrease because each block fetch brings in more data (better spatial locality).
</details>