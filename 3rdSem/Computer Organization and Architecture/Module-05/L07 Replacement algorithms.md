# Replacement algorithms

**Course:** Computer Organization and Architecture  
**Module:** 5 | **Lecture:** 7  
**Date:** 28-Oct-2026  
**Faculty:** DR. SUBHANKAR SHOME  
**CO:** CO 5  
**Learning Methodology:** Chalk & Talk  
**Reference:** Computer Organization and Architecture: Designing for Performance, William Stallings, John Dean, 10th edition, Pearson Education

## Notes

### 1. Why Replacement Policies Are Needed

When a cache miss occurs and the cache (or the target set) is full, one existing block must be evicted to make room for the new block. The replacement algorithm decides which block to evict.

- **Direct-mapped cache:** No decision needed -- the new block maps to exactly one line, replacing whatever is there.
- **Set-associative cache:** Replacement decision is needed among the N ways within the target set.
- **Fully associative cache:** Replacement decision is needed among all cache lines.

### 2. Replacement Policies

**(a) LRU (Least Recently Used)**
Evict the block that has not been accessed for the longest time.
- **Rationale:** Temporal locality suggests that recently used blocks are likely to be used again soon; blocks not used recently are unlikely to be needed.
- **Performance:** Best among practical algorithms; closely approximates OPT.
- **Implementation cost:** Moderate to high (see section 3).

**(b) FIFO (First In, First Out)**
Evict the block that has been in the cache the longest.
- **Rationale:** Older blocks have had their chance; newer blocks might be more relevant.
- **Limitation:** Does not consider access frequency or recency. A frequently used block can be evicted simply because it has been in the cache for a long time.
- **Suffers from:** Belady's Anomaly (see section 5).

**(c) LFU (Least Frequently Used)**
Evict the block with the smallest number of accesses.
- **Rationale:** Blocks accessed fewer times are less important.
- **Limitation:** A block accessed many times early but never again will remain in cache (stale popularity). Does not consider recency. Difficult to implement efficiently (need counters and periodic reset).

**(d) Random**
Evict a randomly selected block.
- **Rationale:** Simple to implement. Does not track access history.
- **Performance:** Surprisingly competitive with LRU in many workloads; avoids pathological cases.
- **Implementation:** A pseudo-random number generator.
- **Advantage:** No hardware overhead for tracking.

**Performance comparison (typical miss rates):**

```
Algorithm  | Miss Rate (relative)
-----------+--------------------
LRU        | 1.00x (baseline)
FIFO       | 1.05x - 1.15x
Random     | 1.05x - 1.20x
LFU        | 1.10x - 1.25x
OPT (ideal)| 0.70x - 0.90x
```

### 3. LRU Implementation

Two common hardware implementations:

**(a) Counter-based LRU**

Each cache line has a counter (age register). On each access to a line, its counter is set to 0, and all other counters are incremented by 1. The line with the highest counter value is the LRU candidate.

```
Initial state (4-way set):
   Way 0    Way 1    Way 2    Way 3
   [A, c=0] [B, c=1] [C, c=2] [D, c=3]   (A most recent, D least)

After accessing B (Way 1):
   Way 0    Way 1    Way 2    Way 3
   [A, c=1] [B, c=0] [C, c=2] [D, c=3]   (B most recent)
   counters of all other ways incremented

After accessing D (Way 3):
   Way 0    Way 1    Way 2    Way 3
   [A, c=2] [B, c=1] [C, c=3] [D, c=0]   (D most recent, C least)
```

**Hardware cost:** For each line, log2(associativity) bits for the counter. For a 4-way set: 2 bits per line = 8 bits per set. Plus comparators to find the max value.

**(b) Stack-based LRU (True LRU)**

Maintains a stack of line positions. Most recently used item is at the top; least recently used at the bottom. On each access, the accessed item is moved to the top (if already in stack) or inserted at the top (if new). The bottom item is the victim.

```
Example sequence: Access blocks A, B, C, D, A, B in a 4-line cache

After A:  Stack = [A] (bottom A)
After B:  Stack = [B, A]
After C:  Stack = [C, B, A]
After D:  Stack = [D, C, B, A]  -- cache full
After A:  Stack = [A, D, C, B]  -- A moved to top
After B:  Stack = [B, A, D, C]  -- B moved to top
```

**Hardware cost:** For N-way associativity, N * log2(N) bits (e.g., 4-way: 4 * 2 = 8 bits per set for the stack ordering).

**(c) Approximate LRU (Pseudo-LRU / Tree-based LRU)**

A common practical compromise. Uses a binary tree of bits where each bit indicates which subtree contains the LRU element.

- For a 4-way set: 3 bits (tree with 4 leaves)
- For an 8-way set: 7 bits
- On a miss: traverse the tree following the LRU pointers to find the victim
- On a hit: update the tree bits along the path to the hit way

```
Example: 4-way pseudo-LRU
             bit[0]
           /        \
      bit[1]        bit[2]
      /    \        /    \
    Way0  Way1    Way2  Way3

Leaf = way to replace is found by walking the tree:
  if bit[0] == 0, go left to bit[1]
  if bit[1] == 0, replace Way0; else replace Way1
On hit: flip all tree bits on the path to the hit way
```

### 4. FIFO Implementation

Maintain a circular buffer of line positions within the set. A pointer keeps track of the next line to replace. On a miss, replace the line at the pointer, then advance the pointer.

```
Initial state:  Set has lines [Way0, Way1, Way2, Way3], Pointer = 0 (Way0)

Access sequence:
  Miss A -> Place in Way0 (pointer position), Pointer -> 1
  Miss B -> Place in Way1, Pointer -> 2
  Miss C -> Place in Way2, Pointer -> 3
  Miss D -> Place in Way3, Pointer -> 0
  Miss E -> Evict A (Way0, pointer position), Place E in Way0, Pointer -> 1
```

**Hardware cost:** A log2(N)-bit pointer per set (e.g., 2 bits for 4-way). Very cheap.

### 5. Belady's Anomaly (FIFO)

Belady's Anomaly is the counterintuitive phenomenon where increasing the cache size (number of lines) causes an increase in the miss rate under FIFO replacement. This contradicts the expectation that more cache always improves performance.

**Example showing Belady's Anomaly:**

Reference string (block addresses): 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5

**Cache with 3 lines (FIFO):**

```
Reference | Cache State   | Miss?
----------+---------------+------
1         | [1]           | Miss
2         | [1,2]         | Miss
3         | [1,2,3]       | Miss
4         | [2,3,4]       | Miss (1 evicted)
1         | [3,4,1]       | Miss (2 evicted)
2         | [4,1,2]       | Miss (3 evicted)
5         | [1,2,5]       | Miss (4 evicted)
1         | [1,2,5]       | Hit
2         | [1,2,5]       | Hit
3         | [2,5,3]       | Miss (1 evicted)
4         | [5,3,4]       | Miss (2 evicted)
5         | [3,4,5]       | Miss (? evicted)
Total misses: 9
```

**Cache with 4 lines (FIFO):**

```
Reference | Cache State       | Miss?
----------+-------------------+------
1         | [1]               | Miss
2         | [1,2]             | Miss
3         | [1,2,3]           | Miss
4         | [1,2,3,4]         | Miss
1         | [1,2,3,4]         | Hit
2         | [1,2,3,4]         | Hit
5         | [2,3,4,5]         | Miss (1 evicted)
1         | [3,4,5,1]         | Miss (2 evicted)
2         | [4,5,1,2]         | Miss (3 evicted)
3         | [5,1,2,3]         | Miss (4 evicted)
4         | [1,2,3,4]         | Miss (5 evicted)
5         | [2,3,4,5]         | Miss (1 evicted)
Total misses: 10
```

With 3 lines: 9 misses. With 4 lines: 10 misses. Increasing cache size made performance worse!

Belady's Anomaly occurs because FIFO does not consider access patterns. A block that arrived early may be retained, while a block that arrived later and is more urgently needed may be evicted. Larger cache can sometimes worsen this effect.

**Note:** LRU does NOT suffer from Belady's Anomaly. For LRU (and OPT), increasing cache size monotonically decreases (or keeps constant) the miss rate. This property is called "stack property" or "inclusion property."

### 6. Optimal Replacement (MIN / OPT)

The theoretical optimal algorithm, proposed by Belady (1966). Evict the block that will be used farthest in the future (or never again).

- **Algorithm:** On a miss, among the blocks currently in cache, choose the one whose next reference (in the future access sequence) is furthest away.
- **Result:** Minimum possible miss rate for any given cache size.
- **Limitation:** Requires knowledge of the future access sequence -- not implementable in practice.
- **Use:** As a baseline for evaluating practical algorithms. The difference between OPT and LRU miss rates indicates room for improvement.

**Example using OPT:**

Reference string: A, B, C, D, A, B, E, A, B, C, D, E (same as Belady example)

Cache with 3 lines (OPT):

```
Ref | Cache before | Next reference | Victim | Cache after  | Miss?
----+--------------+----------------+--------+--------------+------
A   | []           | -              | -      | [A]          | Miss
B   | [A]          | -              | -      | [A,B]        | Miss
C   | [A,B]        | -              | -      | [A,B,C]      | Miss
D   | [A,B,C]      | A=5, B=6, C=10| C(10) | [A,B,D]      | Miss
A   | [A,B,D]      | -              | -      | [A,B,D]      | Hit
B   | [A,B,D]      | -              | -      | [A,B,D]      | Hit
E   | [A,B,D]      | A=8, B=9, D=11| D(11) | [A,B,E]      | Miss
A   | [A,B,E]      | -              | -      | [A,B,E]      | Hit
B   | [A,B,E]      | -              | -      | [A,B,E]      | Hit
C   | [A,B,E]      | A=next=12(inf), B=next=12(inf), E=12 | E(12) or any | [A,B,C] | Miss
D   | [A,B,C]      | ...            | ...    | [A,B,D]      | Miss
E   | [A,B,D]      | ...            | ...    | [A,B,E]      | Miss
Total misses: 7 (better than LRU's 9 with 3 lines)
```

### 7. Worked Example: Comparing Replacement Algorithms

**Reference sequence:** 0, 1, 2, 3, 0, 1, 4, 0, 1, 2, 3, 4

**Cache:** 3 lines, fully associative (so all 3 are candidates)

**(a) LRU:**

```
Ref | Cache (LRU order: most recent first) | Miss?
----+--------------------------------------+------
0   | [0]                                  | Miss
1   | [1, 0]                               | Miss
2   | [2, 1, 0]                            | Miss
3   | [3, 2, 1]  (evict 0)                | Miss
0   | [0, 3, 2]  (evict 1)                | Miss
1   | [1, 0, 3]  (evict 2)                | Miss
4   | [4, 1, 0]  (evict 3)                | Miss
0   | [0, 4, 1]  (hit)                    | Hit
1   | [1, 0, 4]  (hit)                    | Hit
2   | [2, 1, 0]  (evict 4)                | Miss
3   | [3, 2, 1]  (evict 0)                | Miss
4   | [4, 3, 2]  (evict 1)                | Miss
```
Total misses: 10 out of 12 (miss rate = 83.3%)

**(b) FIFO:**

```
Ref | Cache (FIFO order) | Miss?
----+--------------------+------
0   | [0]                | Miss
1   | [0, 1]             | Miss
2   | [0, 1, 2]          | Miss
3   | [1, 2, 3] (evict 0)| Miss
0   | [2, 3, 0] (evict 1)| Miss
1   | [3, 0, 1] (evict 2)| Miss
4   | [0, 1, 4] (evict 3)| Miss
0   | [0, 1, 4] (hit)    | Hit
1   | [0, 1, 4] (hit)    | Hit
2   | [1, 4, 2] (evict 0)| Miss
3   | [4, 2, 3] (evict 1)| Miss
4   | [4, 2, 3] (hit)    | Hit
```
Total misses: 9 out of 12 (miss rate = 75%)

Wait -- that gives FIFO as better than LRU for this sequence. This can happen for specific sequences but LRU generally performs better over a wide range of workloads.

**Miss rate comparison summary for this example:**

```
Algorithm | Misses | Miss Rate
----------+--------+----------
LRU       | 10     | 83.3%
FIFO      | 9      | 75%
Random    | varies | ~75-85%
OPT       | 7      | 58.3%
```

Note: LRU sometimes performs worse than FIFO on specific access patterns (e.g., repeated scans over a set larger than the cache), but on average over diverse workloads, LRU outperforms FIFO.

---

## Practice Problems

**Problem 1:** For a 2-line fully associative cache, apply LRU to the reference string: 1, 2, 3, 1, 2, 3. Count misses.

<details>
<summary>Show Answer</summary>
Ref 1 -> [1] Miss
Ref 2 -> [2, 1] Miss
Ref 3 -> [3, 2] Miss (evict 1)
Ref 1 -> [1, 3] Miss (evict 2)
Ref 2 -> [2, 1] Miss (evict 3)
Ref 3 -> [3, 2] Miss (evict 1)
Total: 6 misses (no hits). This is thrashing -- the working set (3 items) is larger than the cache (2 lines).
</details>

**Problem 2:** Same as Problem 1 but with Random replacement. Is the miss rate always the same?

<details>
<summary>Show Answer</summary>
No. Random could occasionally get a hit if it evicts a block that is not immediately needed. For example, if Random evicts block 3 instead of 1 on the 3rd reference, the 4th reference (1) would hit. The miss rate varies between runs.
</details>

**Problem 3:** What is Belady's anomaly? Which replacement algorithms suffer from it?

<details>
<summary>Show Answer</summary>
Belady's anomaly is the phenomenon where increasing cache size increases the miss rate. It occurs with FIFO but not with LRU or OPT. LRU and OPT have the "stack property" guaranteeing monotonic improvement with larger cache.
</details>

**Problem 4:** Explain why OPT is unimplementable in practice.

<details>
<summary>Show Answer</summary>
OPT requires knowledge of all future memory references to determine which cached block will be used farthest in the future. Since the future is unknown, OPT can only be used as a theoretical upper bound for comparison.
</details>

**Problem 5:** In a 4-way set-associative cache using LRU, a set contains blocks A, B, C, D in LRU order (D is LRU). The access sequence is: X (miss), A (hit), Y (miss), C (hit), Z (miss). Show the state after each access.

<details>
<summary>Show Answer</summary>
Initial: [A (MRU), B, C, D (LRU)]
After X (miss): D evicted, [X, A, B, C]
After A (hit): [A, X, B, C] (A moved to MRU)
After Y (miss): C evicted, [Y, A, X, B]
After C (hit): C not in cache -- this is a miss for C actually. Wait, C was evicted. So C is a miss.
Let me redo:
Initial: [A (MRU), B, C, D (LRU)]
Access X (miss): evict D, insert X. State: [X, A, B, C]
Access A (hit): move A to front. State: [A, X, B, C]
Access Y (miss): evict C, insert Y. State: [Y, A, X, B]
Access C (miss): evict B, insert C. State: [C, Y, A, X]
Access Z (miss): evict X, insert Z. State: [Z, C, Y, A]
</details>