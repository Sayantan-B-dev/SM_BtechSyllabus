# Mapping functions

**Course:** Computer Organization and Architecture  
**Module:** 5 | **Lecture:** 5  
**Date:** 14-Oct-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 5  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. Introduction to Mapping Functions

A mapping function determines how main memory blocks are placed into cache lines. There are three primary mapping techniques:

1. **Direct Mapping:** Each main memory block maps to exactly one cache line.
2. **Fully Associative Mapping:** Any main memory block can be placed in any cache line.
3. **Set-Associative Mapping:** Each main memory block maps to a specific set of cache lines (N lines per set).

### 2. Direct Mapping

**Definition:** In direct mapping, main memory block j maps to cache line i, where:
```
i = j mod m
```
- i = cache line number
- j = main memory block number
- m = total number of cache lines

**Address format (three fields):**

```
+---------------------+---------------------+-------------------+
|        Tag          |   Block (Index)     |    Word (Offset)  |
+---------------------+---------------------+-------------------+
```

**Field breakdown:**
- **Word field (w bits):** Identifies the specific word/byte within the block. w = log2(block size in words/bytes)
- **Block field (b bits):** Identifies which cache line to check. Also called the index. b = log2(m), where m = number of cache lines.
- **Tag field (t bits):** Remaining high-order bits. t = total address bits - b - w

**How it works:**
1. Extract the block field (index) from the address.
2. Go to cache line i (selected by the index).
3. Compare the tag field of the address with the tag stored in cache line i.
4. If they match AND the valid bit is set, it is a HIT.
5. If they do not match, it is a MISS -- the block from main memory is fetched and placed into cache line i (replacing whatever was there).

**ASCII diagram:**

```
CPU Address:
+------------------+------------------+------------------+
|     Tag (t)      |   Block/Index(b) |   Word/Offset(w) |
+------------------+------------------+------------------+
                           |
                           v
              Cache Memory (m lines)
              +---------------------------+
              | Line 0: Tag | Data        |
              | Line 1: Tag | Data        |
              | Line 2: Tag | Data        |
              | ...                       |
              | Line i: Tag | Data  <-----+  Selected by index
              | ...                       |
              | Line m-1: Tag | Data     |
              +---------------------------+
                         |
                    +----+----+
                    | Compare |<--- Tag from CPU
                    | Tags    |
                    +----+----+
                         |
                    Match?--> Yes: HIT (return data from line i)
                         |
                    No: MISS (fetch block from memory, store in line i)
```

**Example: Direct mapping**

Given:
- Main memory: 64 MB (26-bit address), 4-byte words
- Cache: 8 KB (8,192 bytes)
- Block size: 16 bytes (4 words per block)

Calculations:
- Number of cache lines = 8,192 / 16 = 512 lines
- Word offset bits = log2(16) = 4 bits (for byte addressing)
- Index bits = log2(512) = 9 bits
- Tag bits = 26 - 9 - 4 = 13 bits

```
25                  13 12                4 3     0
+--------------------+-------------------+-------+
|        Tag         |      Index        | Offset|
|      13 bits       |      9 bits       | 4 bits|
+--------------------+-------------------+-------+
```

Mapping: Cache line for block j = j mod 512.

If main memory block 1000 is accessed:
- Cache line = 1000 mod 512 = 488
- Tag = floor(1000 / 512) ... But block addresses are already in terms of block numbers. Actually j = floor(address / block_size). Tag stored is the portion identifying which of the m blocks that map to this line is currently stored.
- More precisely: Tag = floor(memory_block_number / m), Index = memory_block_number mod m.

### 3. Fully Associative Mapping

**Definition:** Any main memory block can be placed in any cache line. No index field; the entire address (minus offset) becomes the tag.

**Address format (two fields):**

```
+-------------------------------------+-------------------+
|                Tag                  |    Word (Offset)  |
+-------------------------------------+-------------------+
```

**How it works:**
1. Extract the tag from the CPU address.
2. Compare the tag against ALL tags in the cache simultaneously (using parallel comparators).
3. If any tag matches AND the valid bit is set, it is a HIT.
4. If no tag matches, it is a MISS -- the block is fetched and placed in any cache line (using a replacement policy).

**ASCII diagram:**

```
CPU Address:
+----------------------------------+------------------+
|              Tag (t)             |   Word/Offset(w) |
+----------------------------------+------------------+
                   |
         +---------+---------+
         |                   |
    +----v----+         +----v----+
    | Tag (0) |         | Tag (1) |     ...  (all m lines)
    | Data (0)|         | Data (1)|
    +----+----+         +----+----+
         |                    |
    Compare              Compare            ...  (m comparators)
         |                    |
    +----+----+          +----+----+
    | Match?  |          | Match?  |         ...
    +----+----+          +----+----+
         |                    |
         +---------+----------+
                   |
              OR (any match?)
                   |
           Yes: HIT (return data from matching line)
           No: MISS (fetch and apply replacement policy)
```

**Replacement policies for fully associative:**
- Since any block can go anywhere, a policy is needed to choose which existing block to evict on a miss.
- Common policies: LRU, FIFO, Random (covered in L07).

### 4. Set-Associative Mapping (N-way)

**Definition:** A compromise between direct and fully associative. The cache is divided into s sets, each containing N lines (ways). Main memory block j maps to set i:
```
i = j mod s
```
- i = set number
- j = main memory block number
- s = number of sets = m / N (N = associativity)

**Address format (three fields):**

```
+---------------------+---------------------+-------------------+
|        Tag          |       Set           |    Word (Offset)  |
+---------------------+---------------------+-------------------+
```

**Field breakdown:**
- **Word field (w bits):** Same as direct mapping.
- **Set field (b bits):** Identifies which set to check. b = log2(s)
- **Tag field (t bits):** t = total address bits - b - w

**How it works:**
1. Extract the set number from the CPU address.
2. Go to set i.
3. Compare the tag from the address against ALL N tags in set i (using N comparators).
4. If any tag matches, it is a HIT -- return data from that way.
5. If none matches, it is a MISS -- fetch block and place in any of the N ways within set i (replacement policy needed).

**ASCII diagram (2-way set-associative):**

```
CPU Address:
+------------------+------------------+------------------+
|     Tag (t)      |     Set (b)      |   Word/Offset(w) |
+------------------+------------------+------------------+
                          |
                          v
                   Set i
              +-------------------+
              | Way 0 | Way 1    |
              |-------+----------|
              | Tag A | Tag B    |<--- Compare tag with both
              | Data A| Data B   |
              +-------------------+
                    |       |
               +----+   +---+---+
               |Tag  |   | Tag   |
               |Equal?|   |Equal? |
               +---+-+   +---+-+-+
                   |          |
                   +----+-----+
                        |
                    +---+---+
                    | ANY   |
                    | MATCH?|
                    +---+---+
                        |
                   Yes: HIT
                   No: MISS (replace one way using policy)
```

**Example: 4-way set-associative cache**

Same system as direct-mapped example: 8 KB cache, 16-byte blocks, 26-bit addresses.

- Cache lines = 8,192 / 16 = 512 lines
- Associativity = 4 (4-way)
- Number of sets = 512 / 4 = 128 sets
- Word offset bits = log2(16) = 4 bits
- Set bits = log2(128) = 7 bits
- Tag bits = 26 - 7 - 4 = 15 bits

```
25                  11 10                4 3     0
+--------------------+-------------------+-------+
|        Tag         |       Set         | Offset|
|      15 bits       |      7 bits       | 4 bits|
+--------------------+-------------------+-------+
```

Mapping: Set for block j = j mod 128.

### 5. Comparison of Address Formats (same system)

For a given system (8 KB cache, 16-byte blocks, 26-bit addresses):

```
Scheme            | Tag bits | Index/Set bits | Offset bits | Mapping
------------------+----------+----------------+-------------+-------------------
Direct-mapped     | 13       | 9 (Index)      | 4           | j mod 512
2-way set-assoc   | 14       | 8 (Set)        | 4           | j mod 256 (sets)
4-way set-assoc   | 15       | 7 (Set)        | 4           | j mod 128 (sets)
Fully associative | 22       | 0 (none)       | 4           | Any line
```

Observation: As associativity increases:
- Tag bits increase (fewer index/set bits)
- Index/set bits decrease
- Number of comparators increases (but fewer entries per comparator group)
- Conflict misses decrease

---

## Practice Problems

**Problem 1:** A 64 KB direct-mapped cache has 32-byte blocks. The system uses 32-bit byte addresses. Determine the number of bits in each address field.

<details>
<summary>Show Answer</summary>
Cache lines = 64 KB / 32 B = 65,536 / 32 = 2,048 lines. Offset bits = log2(32) = 5. Index bits = log2(2048) = 11. Tag bits = 32 - 11 - 5 = 16.
</details>

**Problem 2:** A 4-way set-associative cache has 8 KB capacity, 16-byte blocks, 32-bit addresses. Find tag, set, and offset bits.

<details>
<summary>Show Answer</summary>
Cache lines = 8,192 / 16 = 512. Sets = 512 / 4 = 128. Offset bits = log2(16) = 4. Set bits = log2(128) = 7. Tag bits = 32 - 7 - 4 = 21.
</details>

**Problem 3:** A fully associative cache with 64 lines and 8-byte blocks uses 32-bit byte addresses. Find tag and offset bits.

<details>
<summary>Show Answer</summary>
Offset bits = log2(8) = 3. Tag bits = 32 - 3 = 29.
</details>

**Problem 4:** In a direct-mapped cache with 8 lines and 4-word blocks, which cache line does memory word address 44 map to?

<details>
<summary>Show Answer</summary>
Word address 44 = block address floor(44/4) = 11. Cache line = 11 mod 8 = 3. Address 44 maps to line 3.
</details>

**Problem 5:** Compare the number of comparators needed for direct-mapped, 4-way set-associative, and fully associative caches, assuming a cache with 1,024 lines.

<details>
<summary>Show Answer</summary>
Direct-mapped: 1 comparator. 4-way set-associative: 4 comparators (one per way, used by all sets sequentially, or 4 per set -- actually per access we compare all 4 ways in the selected set in parallel, so 4 comparators total). Fully associative: 1,024 comparators (one per line).
</details>