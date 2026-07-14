# Hashing Techniques

**Course:** Database Management Systems  
**Module:** 3 | **Lecture:** 4  
**Date:** 10-Sep-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## Introduction to Hashing

Hashing is a technique that maps a search key directly to a disk block address using a mathematical function called a **hash function**. The goal is to achieve O(1) average time for equality lookups (e.g., `WHERE id = 42`).

### Hash Function

A hash function `h(K)` maps a search key `K` to a bucket address (usually an integer in a fixed range [0, B-1]).

```
h(K) = K mod B  (simple modulo hash function)
```

Where `B` is the number of buckets.

### Bucket

A **bucket** is a storage unit (typically one disk block or multiple blocks) that holds records whose keys hash to the same value.

```
Bucket Address     Records
   0              [10, 20, 30]  (h=0 for keys divisible by B?)
   1              [11, 21, 31]
   2              [12, 22]
   ...
   B-1            [19, 29]
```

---

## Static Hashing

In **static hashing**, the number of buckets `B` is fixed at creation time.

### Components

- **Hash function:** h(K) = K mod B
- **Buckets:** B primary buckets
- **Overflow buckets:** When a primary bucket fills up, an overflow bucket is chained to it (overflow chaining).

### Overflow Chaining

```
Primary Bucket 5:
  [5, 15, 25] -> Overflow chain -> [105, 205] -> [305]

Each block holds at most 3 records.
```

### Problems with Static Hashing

1. **Buckets are fixed.** If the database grows, buckets overflow heavily, degrading performance to O(n).
2. **Wasted space.** If the database shrinks, many buckets are empty.
3. **Poor hash function choice** can cause excessive collisions.

### Hash Function Design

A good hash function:
- Distributes keys uniformly across all buckets.
- Is deterministic (same key always produces same address).
- Is fast to compute.

Common hash functions: modulo, mid-square, folding, multiplicative hashing, cryptographic hashes (MD5, SHA-1 truncated).

---

## Collision Resolution

A **collision** occurs when two different keys hash to the same bucket address. Since the bucket is full, we need a strategy to resolve the collision.

### 1. Open Hashing (Separate Chaining)

- Each bucket is implemented as a linked list (chain) of overflow blocks.
- When a collision occurs, the new record is added to the chain.

```
Bucket Array:
  [0] --> 10 --> 20 --> 30
  [1] --> 11 --> 21
  [2] --> 12
  [3] --> 13 --> 23 --> 33 --> 43
```

**Pros:** Simple, handles any number of collisions, no limit on records per bucket.
**Cons:** Poor cache locality (linked list traversal), extra storage for pointers.

### 2. Closed Hashing (Open Addressing)

- All records are stored directly in the bucket array. No external pointers.
- When a collision occurs, we probe for the next free slot.

#### a. Linear Probing

Probe sequence: `(h(K) + i) mod B` for i = 0, 1, 2, ...

```
Insert keys: 10 (h=0), 20 (h=0), 30 (h=0)
Buckets: B=5
  h(10)=0: slot 0 empty -> place 10 in slot 0.
  h(20)=0: slot 0 occupied -> try slot 1 -> place 20 in slot 1.
  h(30)=0: slot 0 occupied, slot 1 occupied -> try slot 2 -> place 30 in slot 2.

Final array:
  [0]: 10
  [1]: 20
  [2]: 30
  [3]: empty
  [4]: empty
```

**Problem:** **Primary clustering** -- once a cluster forms, new keys that hash anywhere in the cluster extend it, making the cluster grow rapidly.

#### b. Quadratic Probing

Probe sequence: `(h(K) + c1*i + c2*i^2) mod B`

Typically: `(h(K) + i^2) mod B` for i = 0, 1, 2, ...

```
Insert 10 (h=0): slot 0 -> place.
Insert 20 (h=0): slot 0 occupied -> try (0+1^2)=1 -> place.
Insert 30 (h=0): slot 0 occupied, 1 occupied -> try (0+2^2)=4 -> place.
Insert 40 (h=0): slots 0,1,4 occupied -> try (0+3^2)=9 mod 5 = 4 -> occupied -> try (0+4^2)=16 mod 5 = 1 -> ... This can fail if B is not prime.
```

**Pros:** Avoids primary clustering.
**Cons:** **Secondary clustering** (same probe sequence for same h(K)). May not find all slots (cannot guarantee insertion if B is not prime or table is > 50% full).

#### c. Double Hashing

Probe sequence: `(h1(K) + i * h2(K)) mod B`

Use a **second hash function** h2(K) to determine the step size.

```
h1(K) = K mod 7
h2(K) = 1 + (K mod 5)

Insert 10: h1=3, h2=1+0=1. Probe: 3 -> place.
Insert 17: h1=3, h2=1+2=3. Probe: 3 occupied -> (3+3)=6 -> place.
Insert 24: h1=3, h2=1+4=5. Probe: 3 occupied -> (3+5)=8 mod 7 = 1 -> place.
```

**Pros:** Eliminates primary and secondary clustering. Best distribution.
**Cons:** More computation.

### Comparison of Collision Resolution Methods

| Method            | Space       | Search Time         | Clustering     | Deletion Difficulty |
|-------------------|-------------|---------------------|----------------|---------------------|
| Separate Chaining | Extra ptrs  | O(1) avg, O(n) worst| None           | Easy                |
| Linear Probing    | In-place    | O(1) avg, O(n) worst| Primary        | Hard (need tombstones) |
| Quadratic Probing | In-place    | O(1) avg, O(n) worst| Secondary      | Hard                |
| Double Hashing    | In-place    | O(1) avg, O(n) worst| Minimal        | Hard                |

---

## Dynamic Hashing

Static hashing fails when the database size changes dramatically. **Dynamic hashing** schemes allow the number of buckets to grow or shrink as needed.

### 1. Extendible Hashing (Directory-Based)

Extendible hashing uses a **directory** of pointers to buckets. The directory size doubles on overflow, but most buckets remain unchanged.

#### Key Concepts

- **Global depth (d):** Number of bits used for directory indexing.
- **Local depth (d_local):** Number of bits used to distinguish records in a specific bucket.
- **Directory:** An array of size 2^d, where each entry points to a bucket.
- **Bucket:** Stores records that share a common hash prefix of d_local bits.

#### How It Works

1. Compute h(K). Use the last d bits (or first d bits) as the directory index.
2. Follow the pointer to the bucket.
3. If bucket is full:
   - If local depth < global depth: split the bucket, increment local depth. Update directory pointers.
   - If local depth == global depth: double the directory size (global depth++), then split the bucket.

#### Example: Extendible Hashing

```
Initial: d = 1, 2 directories pointing to one bucket.

Directory [0] --> Bucket A (d_local=1) [keys with bit 0 or 1: 2, 4]
          [1] --> Bucket A

Now insert 6 (binary 110). Last 1 bit = 0.
Bucket A is full (capacity = 2).
  global depth d = 1, local depth of A = 1. d_local == d, so double directory.
  New d = 2. Directory size = 4.
  Split A: keys with last 2 bits 00 (4) stay in A; 10 (2,6) go to B.
  Update: d_local(A)=2, d_local(B)=2.

Directory [00] --> A (keys: 4)
          [01] --> A  (but A only has keys ending in 00... No, actually [01] points to a bucket that should contain keys ending in 01. Since there are none, point to an empty bucket or to A temporarily.)
          [10] --> B (keys: 2, 6)
          [11] --> B
```

**Pros:** No overflow chaining, good performance for growing databases.
**Cons:** Directory can become large (2^d). Directory doubling is expensive but infrequent.

#### Visual: Extendible Hashing Directory Structure

```
                    Directory (size = 2^d)
                    +-------+
                    | 000   |-----> Bucket A (d_local=2)
                    +-------+        keys: [4]
                    | 001   |-----> Bucket A (or empty)
                    +-------+
                    | 010   |-----> Bucket B (d_local=2)
                    +-------+        keys: [2, 6]
                    | 011   |-----> Bucket B
                    +-------+
```

### 2. Linear Hashing (Directoryless)

Linear hashing grows buckets **one at a time** in a round-robin fashion without a directory. It uses a **split pointer** that cycles through the buckets.

#### Key Concepts

- Maintains `n` primary buckets (initially some base number).
- A **split pointer `sp`** points to the next bucket to split.
- Two hash functions: `h0(K) = K mod n` and `h1(K) = K mod (2n)`.
- When overflow occurs at bucket `i`, split bucket `sp` (not necessarily `i`).

#### How It Works

1. Initially, `n = n0` (e.g., 4), split pointer `sp = 0`.
2. For a key K, compute `h0(K) = K mod n`.
3. If `h0(K) < sp` (bucket already split), use `h1(K) = K mod (2n)` to find the new bucket.
4. When a bucket overflows, split bucket `sp`:
   - Distribute its records between `sp` and `sp + n` using `h1`.
   - Increment split pointer `sp`.
   - If `sp == n`, reset `sp = 0` and `n = 2n` (a round is complete).

#### Example: Linear Hashing

```
Initial: n = 4, sp = 0.
h0(K) = K mod 4

Buckets:
  [0]: 4, 8, 12 (overflow!)
  [1]: 1, 5, 9
  [2]: 2, 6
  [3]: 3, 7, 11

Overflow at bucket [0] triggers split of bucket [0]:
  Use h1(K) = K mod 8 to redistribute keys 4,8,12.
  h1(4)=4, h1(8)=0, h1(12)=4.
  Bucket [0]: 8
  Bucket [4] (new): 4, 12
  Split pointer sp = 1.

Now lookups use:
  For key K, compute h0 = K mod 4.
  If h0 < sp (1), use h1 = K mod 8 instead.
  This means bucket [0] is already at the new hashing scheme.
```

**Pros:** No directory (less memory). Grows gracefully. Splits are distributed evenly.
**Cons:** Can have significant overflow chains during growth.

---

## Comparison: Static vs Dynamic Hashing

| Feature              | Static Hashing                   | Extendible Hashing              | Linear Hashing                   |
|----------------------|----------------------------------|---------------------------------|----------------------------------|
| Bucket count         | Fixed                            | Grows (directory doubles)       | Grows (one at a time)            |
| Directory           | None                             | Yes (2^d entries)               | None                             |
| Lookup              | O(1) average (may degrade)       | O(1) (two steps: directory + bucket) | O(1) (one hash + optional rehash) |
| Space overhead      | Overflow chains                  | Directory (can be large)        | Minimal                          |
| Handle growth       | Poor (overflow chains)           | Good                            | Good                             |
| Handle shrinkage    | Not possible                     | Can shrink (directory)          | Can shrink                       |
| Concurrency         | Moderate                         | Good (directory allows fine-grained locks) | Good                         |
| Use case            | Small, stable datasets           | Growing datasets, real-time systems | Growing datasets with limited memory |

---

## Practice Problems

**Problem 1:** A hash table uses linear probing with B = 7 buckets. Insert keys: 14, 21, 28, 35, 42. Use h(K) = K mod 7. Show the final hash table.

<details>
<summary>Show Answer</summary>

h(14)=0, h(21)=0, h(28)=0, h(35)=0, h(42)=0.

- Step 1: Insert 14 -> slot 0.
- Step 2: Insert 21 -> slot 0 full, try 1 -> slot 1.
- Step 3: Insert 28 -> slot 0,1 full, try 2 -> slot 2.
- Step 4: Insert 35 -> slots 0,1,2 full, try 3 -> slot 3.
- Step 5: Insert 42 -> slots 0,1,2,3 full, try 4 -> slot 4.

Final:
[0]: 14, [1]: 21, [2]: 28, [3]: 35, [4]: 42, [5]: empty, [6]: empty
</details>

**Problem 2:** In extendible hashing, global depth = 3, directory size = 8. A key has hash bits ...110. Which directory entry does it use? (Assume last d bits are used.)

<details>
<summary>Show Answer</summary>

d = 3. Use last 3 bits = 110 (binary) = 6 (decimal). Directory entry [6] is used.
</details>

**Problem 3:** What is the primary advantage of double hashing over linear probing?

<details>
<summary>Show Answer</summary>

Double hashing uses a second hash function to determine the probe step, so keys that hash to the same initial slot use different probe sequences. This eliminates primary clustering (which causes long runs of occupied slots in linear probing) and provides more uniform distribution, leading to better performance as the table fills up.
</details>

**Problem 4:** In linear hashing, n = 8, split pointer sp = 3. A key K has h0(K) = 5. Which hash function should be used for lookup?

<details>
<summary>Show Answer</summary>

h0(K) = 5. Since 5 >= sp (= 3), bucket [5] has not been split yet. Use h0 (K mod 8) to find the bucket.
</details>

**Problem 5:** Compare open hashing (chaining) with closed hashing (open addressing) in terms of deletion and load factor tolerance.

<details>
<summary>Show Answer</summary>

- **Open hashing (chaining):** Deletion is simple (remove from linked list). Can tolerate load factors > 1 (overflow chains just get longer). Uses extra space for pointers.
- **Closed hashing (open addressing):** Deletion requires tombstones or rehashing (otherwise search breaks). Performance degrades rapidly as load factor approaches 1 (clustering). Typically kept below 0.7-0.8 load factor for acceptable performance. No pointer overhead.
</details>

---
