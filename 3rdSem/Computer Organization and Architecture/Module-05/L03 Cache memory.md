# Cache memory

**Course:** Computer Organization and Architecture  
**Module:** 5 | **Lecture:** 3  
**Date:** 13-Oct-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 5  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. Cache Operation: CPU Requests Data

Cache memory is a small, fast memory located between the CPU and main memory. It stores copies of frequently used data and instructions from main memory.

**Operation flowchart:**

```
CPU generates memory address
          |
          v
   +-----+------+
   | Is data in |  Yes
   |  cache?    |---------> Return data to CPU (HIT)
   +-----+------+
          |
          | No (MISS)
          v
   +-----+------+
   | Fetch block |     The block containing the requested
   | from main   |----> word is copied from main memory
   | memory      |     into cache
   +-----+------+
          |
          v
   +-----+------+
   | Return data |
   | to CPU      |
   +-------------+
```

**Read operation steps:**
1. CPU sends a memory address to the cache controller.
2. Cache controller checks if the requested data exists in the cache.
3. **Cache Hit:** If found, the data is returned to the CPU immediately (fast access).
4. **Cache Miss:** If not found, the entire block containing the requested word is fetched from main memory, stored in cache, and then the requested word is returned to the CPU.

**Write operation:** (covered in detail in L08 and L09)
- Write-through: Data is written to both cache and main memory.
- Write-back: Data is written only to cache; main memory is updated when the block is evicted.

### 2. Cache Structure: Tag, Index, Offset

Each cache entry (cache line) stores:
- **Tag:** A portion of the memory address used to identify which block from main memory is currently stored in that cache line.
- **Data block:** The actual data (multiple consecutive words from main memory).
- **Valid bit:** Indicates whether the cache line contains valid data.
- **Dirty bit (for write-back):** Indicates whether the data has been modified in cache (not yet written to memory).

A memory address is divided into three fields:

```
+---------------+---------------+---------------+
|     Tag       |    Index      |    Offset     |
+---------------+---------------+---------------+
```

- **Offset:** Least significant bits. Selects the specific byte/word within the cache block.
- **Index:** Middle bits. Selects which cache line (or set) to check.
- **Tag:** Most significant bits. Compared against the tag stored in the selected cache line to determine a hit or miss.

### 3. Direct-Mapped Cache

In a direct-mapped cache, each main memory block maps to exactly one cache line. The mapping is deterministic.

**Mapping function:**
```
Cache Line Number = (Block Address) mod (Number of Cache Lines)
```

**Address division for direct-mapped cache:**

```
+---------------------+---------------------+-------------------+
|        Tag          |       Index         |     Offset        |
+---------------------+---------------------+-------------------+
```

Number of bits for each field:
- Offset bits = log2(Block Size in bytes)
- Index bits = log2(Number of Cache Lines)
- Tag bits = Address bits - Index bits - Offset bits

**Example: 16 KB cache, 4-byte blocks, 32-bit address**

Given:
- Cache size = 16 KB = 16,384 bytes
- Block size = 4 bytes
- Number of blocks (lines) in cache = 16,384 / 4 = 4,096 lines

Address division:
- Offset: 4-byte blocks => 2 bits to select byte within block (log2 4 = 2)
- Index: 4,096 lines => 12 bits to select cache line (log2 4096 = 12)
- Tag: 32 - 12 - 2 = 18 bits

```
31                    14 13                   2 1  0
+-----------------------+-----------------------+-----+
|         Tag           |        Index          |Offset|
|       18 bits         |       12 bits         |2 bits|
+-----------------------+-----------------------+-----+
```

**ASCII diagram of direct-mapped cache lookup:**

```
CPU Address: 32 bits
+---------------+-------------+-----+
|    Tag (18)   | Index (12)  | Off |
+---------------+-------------+-----+
                       |
                       v
              +--------+--------+
              | Cache Memory     |
              | Index 0: Tag A  |
              |        Data A    |
              | Index 1: Tag B  |
              |        Data B    |
              | ...              |
              | Index i: Tag X  |<--- Select line at Index
              |        Data X    |
              +--------+--------+
                       |
                   Tag Compare
                  +----+----+
                  | Tag | Tag|---> Match? HIT (return Data)
                  |from |from|---> No match? MISS (fetch from memory)
                  | CPU |Line|
                  +----+----+
```

### 4. Fully Associative Cache

In a fully associative cache, any main memory block can be placed in any cache line. The entire tag must be compared against all tags in the cache simultaneously (associative search).

**Address division:**

```
+-------------------------------+-------------------+
|             Tag               |     Offset        |
+-------------------------------+-------------------+
```

No index field -- the entire address (minus offset) is the tag.

**Advantages:** No conflict misses -- any block can go anywhere.
**Disadvantages:** Requires a comparator for each cache line, making it expensive and slow for large caches. High hardware complexity.

**Example:** Fully associative cache with 4 lines, 4-byte blocks, 32-bit address:
- Offset bits: 2 (log2 4)
- Tag bits: 30 (32 - 2)

```
31                                   2 1  0
+-------------------------------------+-----+
|                Tag                  |Offset|
|              30 bits                |2 bits|
+-------------------------------------+-----+
```

When a CPU address arrives, ALL 4 lines compare their 30-bit tag simultaneously using parallel comparators. If any matches, it is a hit.

### 5. Set-Associative Cache (N-way Set-Associative)

A compromise between direct-mapped and fully associative. The cache is divided into sets, where each set contains N cache lines (ways). A main memory block maps to a specific set (like direct-mapped), but can be placed in any of the N lines within that set (like associative).

**Mapping function:**
```
Set Number = (Block Address) mod (Number of Sets)
```
Number of sets = (Number of Cache Lines) / N  (where N = associativity)

**Address division for N-way set-associative cache:**

```
+---------------------+---------------------+-------------------+
|        Tag          |        Set          |     Offset        |
+---------------------+---------------------+-------------------+
```

- Set bits = log2(Number of Sets)
- Offset bits = log2(Block Size)
- Tag bits = Address bits - Set bits - Offset bits

**Example:** 16 KB cache, 4-byte blocks, 4-way set-associative, 32-bit address:
- Cache lines = 4,096
- Sets = 4,096 / 4 = 1,024 sets
- Set bits = log2(1024) = 10 bits
- Offset bits = 2 bits
- Tag bits = 32 - 10 - 2 = 20 bits

```
31                    12 11                  2 1  0
+-----------------------+-----------------------+-----+
|         Tag           |        Set            |Offset|
|       20 bits         |       10 bits         |2 bits|
+-----------------------+-----------------------+-----+
```

**ASCII diagram of set-associative cache lookup (4-way):**

```
CPU Address: 32 bits
+---------------+-------------+-----+
|    Tag (20)   |  Set (10)   | Off |
+---------------+-------------+-----+
                       |
                       v
              +--------+--------+
              | Set S            |
              | +------+------+ |     Tag comparison with
              | |Way 0 |Way 1 | |---> all 4 ways in parallel
              | |Tag A |Tag B | |     (4 comparators)
              | |Data A|Data B| |
              | +------+------+ |
              | +------+------+ |
              | |Way 2 |Way 3 | |
              | |Tag C |Tag D | |
              | |Data C|Data D| |
              | +------+------+ |
              +-----------------+
                       |
                  +----+----+
                  | Match?  |---> Yes: HIT from matching way
                  +----+----+---> No: MISS (fetch from memory)
```

### 6. Comparison Summary

```
Feature               | Direct-Mapped  | Set-Associative | Fully Associative
----------------------+----------------+-----------------+------------------
Hardware complexity   | Low            | Medium          | High
Hit time              | Fast           | Moderate        | Slow (N-way compare)
Conflict misses       | High           | Moderate        | None
Tag size              | Smallest       | Medium          | Largest
Number of comparators | 1              | N               | Number of lines
Cost                  | Cheapest       | Moderate        | Most expensive
Typical usage         | L1 caches      | L2/L3 caches    | Small TLBs
```

---

## Practice Problems

**Problem 1:** A cache has 64 lines, each storing 8 words (32 bytes). The main memory is 32-bit byte-addressable. For a direct-mapped cache, determine the number of bits in tag, index, and offset.

<details>
<summary>Show Answer</summary>
Offset = log2(32) = 5 bits. Index = log2(64) = 6 bits. Tag = 32 - 5 - 6 = 21 bits.
</details>

**Problem 2:** For the same cache configured as 4-way set-associative, determine tag, set, and offset bits.

<details>
<summary>Show Answer</summary>
Offset = 5 bits. Number of sets = 64 / 4 = 16. Set bits = log2(16) = 4 bits. Tag = 32 - 5 - 4 = 23 bits.
</details>

**Problem 3:** In a direct-mapped cache with 8 lines and 4-byte blocks, which cache line does memory address 0x2C (44 decimal) map to?

<details>
<summary>Show Answer</summary>
Word address = 44 / 4 = 11 (block address 11). Cache line = 11 mod 8 = 3. So address 0x2C maps to cache line 3.
</details>

**Problem 4:** Explain why fully associative caches are impractical for large cache sizes.

<details>
<summary>Show Answer</summary>
Fully associative caches require a comparator for every cache line to simultaneously compare all tags. For a cache with thousands of lines, this requires thousands of comparators, consuming enormous chip area and power. The parallel comparison also increases access time, defeating the purpose of a fast cache.
</details>

**Problem 5:** A 2-way set-associative cache has 4 sets, each with 2 lines. Cache block size is 1 word. Show the set mapping for addresses 0, 1, 2, 3, 4, 5, 6, 7.

<details>
<summary>Show Answer</summary>
Set number = Block Address mod 4. Addr 0 -> Set 0, Addr 1 -> Set 1, Addr 2 -> Set 2, Addr 3 -> Set 3, Addr 4 -> Set 0, Addr 5 -> Set 1, Addr 6 -> Set 2, Addr 7 -> Set 3. Each set has 2 ways, so up to 2 different blocks can be stored per set.
</details>