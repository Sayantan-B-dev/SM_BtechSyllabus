# Concept of hierarchical memory organization

**Course:** Computer Organization and Architecture  
**Module:** 5 | **Lecture:** 2  
**Date:** 07-Oct-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 5  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. The Memory Hierarchy Pyramid

Computer memory is organized as a hierarchy to balance three conflicting goals: speed (fast access), capacity (large storage), and cost (economical). No single memory technology can simultaneously provide the fastest speed, the largest capacity, and the lowest cost. The hierarchy uses different technologies at different levels.

```
                   +-----------+
                   | Registers |   Level 0  (Fastest, Smallest, Most Expensive)
                   |  (CPU)    |
                   +-----------+
                        |
                   +-----------+
                   |   Cache   |   Level 1
                   |  (SRAM)   |
                   +-----------+
                        |
                   +-----------+   Level 2
                   | Main Mem  |
                   |  (DRAM)   |
                   +-----------+
                        |
                   +-----------+   Level 3
                   | Secondary |
                   | Storage   |
                   |  (SSD)    |
                   +-----------+
                        |
                   +-----------+   Level 4
                   | Tertiary  |
                   | Storage   |
                   | (Tape)    |
                   +-----------+

Characteristics per level (typical values):

    Level    |  Technology | Access Time  | Capacity    | Cost/bit
    ---------+-------------+--------------+-------------+------------
    Registers| Flip-flops  |  < 1 ns      |  < 1 KB     | Highest
    Cache L1 |  SRAM       |  1-2 ns      |  32-64 KB   | High
    Cache L2 |  SRAM       |  3-10 ns     |  256-512 KB | Moderate
    Cache L3 |  SRAM       |  10-40 ns    |  2-8 MB     | Lower
    Main Mem |  DRAM       |  50-100 ns   |  4-32 GB    | Low
    SSD      |  Flash      |  10-100 us   |  256 GB-2 TB| Very Low
    HDD      |  Magnetic   |  5-15 ms     |  1-10 TB    | Lowest
```

### 2. Goals of the Memory Hierarchy

The memory hierarchy aims to give the illusion of:
- **Speed of the fastest level** (registers) -- most frequent accesses are to fast, small memory
- **Capacity of the largest level** (disk) -- infrequent accesses can use large, slow storage
- **Cost of the cheapest level** (disk per bit) -- the bulk of storage uses inexpensive technology

This is achieved through the principle of **locality of reference**.

### 3. Locality of Reference

Programs tend to access a relatively small portion of the address space at any given time. Two types:

**(a) Temporal Locality (Locality in Time)**
If a memory location is accessed, it is likely to be accessed again soon.
- Example: Loop counters, frequently used variables, code in a loop body.
- Reason: Programs exhibit iterative behavior (loops, repeated function calls).
- How hierarchy exploits it: Recently accessed data is kept in cache (higher level). Subsequent accesses hit the cache and avoid going to main memory.

**(b) Spatial Locality (Locality in Space)**
If a memory location is accessed, nearby locations are likely to be accessed soon.
- Example: Array traversal, sequential instruction execution.
- Reason: Programs tend to access data structures and instructions sequentially.
- How hierarchy exploits it: When a block of data is fetched from memory to cache, the entire block (containing nearby addresses) is brought in. Subsequent accesses to nearby addresses find the data already in cache.

### 4. Hit Ratio and Miss Ratio

When the CPU requests data:

- **Hit:** The requested data is found at a given level of the hierarchy.
- **Miss:** The requested data is not found at that level and must be fetched from a lower level.

Definitions:
- **Hit Rate (H):** Fraction of memory accesses found in the faster (upper) level. H = (Number of hits) / (Total accesses)
- **Miss Rate (1 - H):** Fraction of accesses not found in the upper level. Miss Rate = 1 - H

A high hit rate (close to 1.0) is desirable because it means most accesses are serviced quickly.

### 5. Effective Access Time (EAT)

The Effective Access Time (EAT) is the average time to access memory considering both hits and misses.

**Two-level hierarchy formula:**
```
EAT = H * T_cache + (1 - H) * T_memory
```
where:
- H = hit rate (cache hit ratio)
- T_cache = access time of cache (fast level)
- T_memory = access time of main memory (slow level)
- (1 - H) = miss rate

**Three-level hierarchy (L1, L2, Main Memory):**
```
EAT = H1 * T_L1 + (1 - H1) * [ H2 * T_L2 + (1 - H2) * T_MM ]
```
where:
- H1 = L1 cache hit rate
- H2 = L2 cache hit rate (given a miss in L1)
- T_L1, T_L2, T_MM = access times at each level

**Note:** When a miss occurs, we pay the access time of the upper level (checking) plus the time to fetch from the lower level. A more precise formula adds the upper level access time even on a miss:
```
EAT = H * T_cache + (1 - H) * (T_cache + T_memory)
     = T_cache + (1 - H) * T_memory
```
The simpler formula EAT = H * T_cache + (1 - H) * T_memory is commonly used, assuming the cache check time is included in both terms.

### 6. Worked Example: Calculating EAT

**Problem 1 (Two-level hierarchy):**
A system has a cache access time of 5 ns and a main memory access time of 80 ns. The cache hit rate is 95%. Calculate the effective access time.

**Solution:**
H = 0.95, T_cache = 5 ns, T_memory = 80 ns

EAT = 0.95 * 5 + 0.05 * 80
EAT = 4.75 + 4.0
EAT = 8.75 ns

Without cache (all accesses to main memory): EAT = 80 ns.
Speedup = 80 / 8.75 = 9.14x

**Problem 2 (Three-level hierarchy):**
A system has:
- L1 cache: 2 ns access time, 90% hit rate
- L2 cache: 10 ns access time, 80% hit rate (on L1 misses)
- Main memory: 100 ns access time

Calculate EAT.

**Solution:**
H1 = 0.90, H2 = 0.80, T_L1 = 2 ns, T_L2 = 10 ns, T_MM = 100 ns

EAT = 0.90 * 2 + 0.10 * [ 0.80 * 10 + 0.20 * 100 ]
EAT = 1.80 + 0.10 * [ 8 + 20 ]
EAT = 1.80 + 0.10 * 28
EAT = 1.80 + 2.80
EAT = 4.60 ns

**Problem 3 (Effect of hit rate on EAT):**
Plot EAT for hit rates from 0.9 to 0.999 given T_cache = 2 ns, T_memory = 100 ns.

- H = 0.90: EAT = 0.90*2 + 0.10*100 = 1.8 + 10.0 = 11.8 ns
- H = 0.95: EAT = 0.95*2 + 0.05*100 = 1.9 + 5.0 = 6.9 ns
- H = 0.98: EAT = 0.98*2 + 0.02*100 = 1.96 + 2.0 = 3.96 ns
- H = 0.99: EAT = 0.99*2 + 0.01*100 = 1.98 + 1.0 = 2.98 ns
- H = 0.999: EAT = 0.999*2 + 0.001*100 = 1.998 + 0.1 = 2.098 ns

Observation: As hit rate approaches 1.0, EAT approaches T_cache. Even a small miss rate (1%) significantly impacts performance when the speed difference is large.

---

## Practice Problems

**Problem 1:** A two-level memory system has T_cache = 10 ns, T_memory = 200 ns, and the hit rate is 97%. What is EAT?

**Answer:** EAT = 0.97 * 10 + 0.03 * 200 = 9.7 + 6.0 = 15.7 ns.

**Problem 2:** For a system with T_cache = 5 ns, what must the hit rate be to achieve EAT <= 10 ns if T_memory = 120 ns?

**Answer:** 10 >= H * 5 + (1-H) * 120 = 5H + 120 - 120H = 120 - 115H => 115H >= 110 => H >= 110/115 = 0.9565 = 95.65%.

**Problem 3:** In a three-level hierarchy, L1 hit rate = 85%, L2 hit rate = 75% (on L1 misses), T_L1 = 1 ns, T_L2 = 8 ns, T_MM = 150 ns. Compute EAT.

**Answer:** EAT = 0.85 * 1 + 0.15 * (0.75 * 8 + 0.25 * 150) = 0.85 + 0.15 * (6 + 37.5) = 0.85 + 0.15 * 43.5 = 0.85 + 6.525 = 7.375 ns.

**Problem 4:** Define temporal locality and spatial locality. Give one code example that exhibits each.

**Answer:** Temporal locality: accessing the same variable repeatedly in a loop: `for(int i=0; i<1000; i++) sum += a[i];` -- `sum` exhibits temporal locality. Spatial locality: accessing consecutive array elements: `for(int i=0; i<1000; i++) sum += a[i];` -- array `a[]` exhibits spatial locality.

**Problem 5:** Explain why the memory hierarchy is necessary in modern computer systems.

**Answer:** No single memory technology can simultaneously provide very fast access (required by modern CPUs), very large capacity (required by modern applications), and very low cost per bit (required for affordability). The hierarchy uses small amounts of fast, expensive SRAM for cache and large amounts of slow, cheap DRAM/disk for bulk storage, relying on locality to give the illusion of a large, fast memory at reasonable cost.
