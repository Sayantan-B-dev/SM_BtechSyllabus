# Mapping functions

**Course:** Computer Organization and Architecture  
**Module:** 5 | **Lecture:** 6  
**Date:** 14-Oct-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 5  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. Comparison of Mapping Functions

The three mapping techniques differ in hardware complexity, hit time, miss rate, and implementation cost.

```
Feature                | Direct Mapped          | Set-Associative           | Fully Associative
-----------------------+------------------------+---------------------------+--------------------------
Placement of block     | Fixed line             | Fixed set, any line       | Any line anywhere
                      |                        | in the set                |
Hit detection          | 1 tag compare          | N tag compares            | m tag compares
                      |                        | (N = associativity)       | (m = total lines)
Tag size               | Smallest               | Medium                   | Largest
Address bits as tag    | addr - index - offset  | addr - set - offset       | addr - offset
Conflict misses        | Most                   | Fewer as N increases      | None
Hardware complexity    | Low (1 comparator)     | Medium (N comparators)    | High (m comparators)
Access time            | Fastest                | Moderate (slightly slower)| Slowest (must compare all)
Power consumption      | Lowest                 | Moderate                  | Highest
Common usage           | L1 caches              | L2/L3 caches, TLBs        | Small TLBs, branch predictors
```

### 2. Hardware Complexity

**Direct-Mapped Cache Hardware:**
- One comparator (compare CPU tag against stored tag at the indexed line)
- Multiplexer: select the data from the indexed line
- Decoder: decode the index bits to select one cache line
- Total hardware: O(1) for the comparator logic

```
Index bits ----> Decoder ----> Selects 1 of m lines
                   |
Tag bits -----------> Comparator ----> Hit/Miss
```

**Fully Associative Cache Hardware:**
- m comparators (one per cache line)
- Priority encoder: if multiple matches (should not happen), select one
- Data selector: select data from the matching line
- Total hardware: O(m) for comparators -- very expensive for large m

```
Tag bits ---+---[Comp 0]---+
            |              |
            +---[Comp 1]---|---+
            |              |   |
            +---[Comp m-1]-+---|---+
                            |   |   |
                           OR  |   |
                            |   |   |
                           Hit  |   |
                        (any match)
```

**Set-Associative Cache Hardware:**
- N comparators (one per way in the selected set)
- Multiplexer: select data from the matching way
- Decoder: decode set bits to select one set (which contains N lines/ways)
- Total hardware: O(N) comparators, independent of cache size

```
Set bits ----> Decoder ----> Selects 1 set (containing N ways)
                  |
Tag bits ---+---[Comp Way 0]---+---(OR)---> Hit
            |                  |
            +---[Comp Way 1]---+
            |                  |
            ...                ...
            |                  |
            +---[Comp Way N-1]-+
```

### 3. Hit Time Comparison

Hit time is the time from address presentation to data availability.

**Direct-mapped hit time = T_decoder + T_tag_compare + T_data_select**
- T_decoder: decode index bits (fast, ~1 gate delay per bit)
- T_tag_compare: compare tag bits (fast, ~1-2 gate delays)
- T_data_select: select the data word from the block (mux delay)

**Set-associative hit time = T_decoder + T_tag_compare (N ways) + T_mux**
- Same decoder delay for set bits
- N comparators run in parallel (same delay as one comparator)
- Additional delay: multiplexing among N ways adds ~log2(N) gate delays
- Overall: slightly slower than direct-mapped due to mux

**Fully associative hit time = T_tag_compare_all + T_priority_encoder + T_data_select**
- Tag comparison with all m lines (same delay as one comparator, but high fanout on tag lines)
- Priority encoder: adds log2(m) gate delays
- For large m, this is significantly slower
- Word line loading: the address tag must drive all m comparators, increasing wire delay

**Typical values (relative):**

```
Mapping             | Hit Time (cycles)
--------------------+-------------------
Direct-mapped       | 1-2 cycles
2-way set-assoc     | 2-3 cycles
4-way set-assoc     | 2-4 cycles
8-way set-assoc     | 3-5 cycles
Fully associative   | 4-10+ cycles (for large caches)
```

### 4. Implementation Examples

**Direct-Mapped Cache Implementation (simplified):**

```
CPU Address [31:0]
     |
     +--[Tag (31:b+w)] --> Comparator --> Hit
     |
     +--[Index (b+w-1:w)] --> Address Decoder
     |                            |
     |                       +----v------+
     |                       | Tag Array |  --> Tag value for line
     |                       | (1 read   |
     |                       |  port)    |
     |                       +-----------+
     |
     +--[Offset (w-1:0)] --> Byte/Word Select
                                     |
                                +----v------+
                                | Data Array|  --> Data value
                                | (1 read   |
                                |  port)    |
                                +-----------+
```

**Set-Associative Cache Implementation (4-way):**

```
CPU Address [31:0]
     |
     +--[Tag (31:s+w)] --> +--[Compare Way 0]--+
     |                     |                    |
     |                     +--[Compare Way 1]--+---OR--> Hit
     |                     |                    |
     |                     +--[Compare Way 2]--+
     |                     |                    |
     |                     +--[Compare Way 3]--+
     |
     +--[Set (s+w-1:w)] --> Set Decoder
     |                            |
     |                       +----v------+
     |                       | Tag Array |--> Tag for Way 0
     |                       | Tag Array |--> Tag for Way 1
     |                       | Tag Array |--> Tag for Way 2
     |                       | Tag Array |--> Tag for Way 3
     |                       +-----------+
     |
     +--[Offset (w-1:0)] --> +--[Data Array Way 0]--+
                             |                       |
                             +--[Data Array Way 1]--+---MUX--> Data (select matching way)
                             |                       |
                             +--[Data Array Way 2]--+
                             |                       |
                             +--[Data Array Way 3]--+
```

### 5. Replacement Policies with Different Mapping Functions

The replacement policy needed depends on the mapping function:

| Mapping        | Replacement Needed? | Options                        |
|----------------|---------------------|--------------------------------|
| Direct-mapped  | No                  | None (block maps to fixed line)|
| Set-associative| Yes (within set)    | LRU, FIFO, Random, LFU         |
| Fully assoc.   | Yes (any line)      | LRU, FIFO, Random, LFU         |

**Replacement policy interaction:**
- In direct-mapped: No choice -- the block always replaces the content at i = j mod m.
- In set-associative (N-way): On a miss, N candidates exist within the set. The replacement policy selects which one to evict.
- In fully associative: All m lines are candidates. The replacement policy selects which one to evict.

### 6. Numerical Examples: Calculating Tag, Index, Offset Bits

**Example 1:** System: 16 KB cache, 32-byte blocks, 32-bit byte addresses, direct-mapped.

```
Cache lines = 16,384 / 32 = 512
Offset bits = log2(32) = 5
Index bits  = log2(512) = 9
Tag bits    = 32 - 9 - 5 = 18

Address breakdown:
[31:14] Tag (18 bits) | [13:5] Index (9 bits) | [4:0] Offset (5 bits)
```

**Example 2:** Same system but 2-way set-associative.

```
Lines = 512
Sets = 512 / 2 = 256
Offset bits = 5
Set bits = log2(256) = 8
Tag bits = 32 - 8 - 5 = 19

Address breakdown:
[31:13] Tag (19 bits) | [12:5] Set (8 bits) | [4:0] Offset (5 bits)
```

**Example 3:** Same system but fully associative.

```
Offset bits = 5
Tag bits = 32 - 5 = 27

Address breakdown:
[31:5] Tag (27 bits) | [4:0] Offset (5 bits)
```

### 7. Comprehensive Comparison Table

**Given:** 16 KB cache, 32-byte blocks, 32-bit byte addresses.

```
Parameter                | Direct | 2-way  | 4-way  | 8-way  | Fully
-------------------------+--------+--------+--------+--------+--------
Cache lines              | 512    | 512    | 512    | 512    | 512
Ways per set             | 1      | 2      | 4      | 8      | 512
Number of sets           | 512    | 256    | 128    | 64     | 1
Offset bits              | 5      | 5      | 5      | 5      | 5
Index/Set bits           | 9      | 8      | 7      | 6      | 0
Tag bits                 | 18     | 19     | 20     | 21     | 27
Comparators needed       | 1      | 2      | 4      | 8      | 512
Conflict misses          | High   | Med    | Low    | Very   | None
                         |        |        |        | Low    |
Tag storage overhead     | 18*512 | 19*512 | 20*512 | 21*512 | 27*512
                         | 9,216b | 9,728b | 10,240b| 10,752b| 13,824b
Access time (relative)   | 1.0x   | 1.1x   | 1.2x   | 1.4x   | 3-4x
```

Observation: As associativity increases, tag storage overhead increases, hardware complexity increases, and hit time increases. However, the miss rate decreases (fewer conflict misses), potentially improving overall performance despite the longer hit time.

---

## Practice Problems

**Problem 1:** A 32 KB, 4-way set-associative cache uses 64-byte blocks. The system has 32-bit byte addresses. Calculate the number of tag, set, and offset bits.

<details>
<summary>Show Answer</summary>
Cache lines = 32,768 / 64 = 512. Sets = 512 / 4 = 128. Offset bits = log2(64) = 6. Set bits = log2(128) = 7. Tag bits = 32 - 7 - 6 = 19.
</details>

**Problem 2:** Why does a fully associative cache require more tag bits than a direct-mapped cache of the same size?

<details>
<summary>Show Answer</summary>
Fully associative has no index field -- all address bits above the offset become the tag. Direct-mapped has both tag and index fields. For 32-bit addresses with 32-byte blocks: direct-mapped uses 18 tag + 9 index + 5 offset = 32; fully associative uses 27 tag + 5 offset = 32. The fully associative tag is 9 bits larger.
</details>

**Problem 3:** For a 2-way set-associative cache with 16 sets, 8-byte blocks, and 16-bit byte addresses, show how address 0x1234 (4660 decimal) is mapped.

<details>
<summary>Show Answer</summary>
Block address = 4660 / 8 = 582 (integer division). Set = 582 mod 16 = 6. Tag = floor(582 / 16) = 36. Offset = 4660 mod 8 = 4. So address 0x1234 maps to set 6, tag 36, offset 4.
</details>

**Problem 4:** Compare the number of tag comparisons required per memory access for each mapping scheme (assume a 1024-line cache).

<details>
<summary>Show Answer</summary>
Direct-mapped: 1 comparison. 4-way set-associative: 4 comparisons (parallel within the set). Fully associative: 1024 comparisons (parallel across all lines).
</details>

**Problem 5:** A cache has 256 lines arranged as 64 sets of 4 ways each. Block size is 16 bytes. If a program accesses blocks 0, 64, 128, 192, 256 sequentially, which set does each map to? Will there be conflicts?

<details>
<summary>Show Answer</summary>
Set number = block mod 64. Block 0 -> Set 0. Block 64 -> Set 0. Block 128 -> Set 0. Block 192 -> Set 0. Block 256 -> Set 0. All map to Set 0. With 4 ways, Set 0 can hold at most 4 blocks simultaneously. The 5th access (block 256) will cause a miss and evict one of the previous blocks (conflict miss within the set).
</details>