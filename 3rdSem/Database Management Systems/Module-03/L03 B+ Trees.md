# B+ Trees

**Course:** Database Management Systems  
**Module:** 3 | **Lecture:** 3  
**Date:** 10-Sep-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## What is a B+ Tree?

A B+ tree is a variant of the B-tree that is the **most commonly used index structure** in modern database systems. It addresses the limitations of B-trees for range queries by storing all actual data (record pointers) only in the leaf nodes and linking the leaf nodes in a sorted linked list.

### B+ Tree Properties

Same as B-tree with the following differences:

- **Internal nodes (routing nodes):** Store only keys (no data pointers). They act as a roadmap to guide the search.
- **Leaf nodes:** Store both keys and pointers to data records (or record IDs). All keys in the database appear in the leaf nodes.
- **Leaf nodes are linked** in a doubly-linked list (or singly in some implementations) to enable efficient sequential (range) scans.
- **Keys may be duplicated:** A key value can appear in both an internal node (as a separator/router) and in a leaf node (as an actual data entry).

---

## Structure of a B+ Tree

```
                Internal Nodes (routing only -- keys)
                         |
    +--------------------+--------------------+
    |                                        |
 [ K1, K2, K3, ... ]                    [ K1, K2, ... ]
    |    |    |                              |
    v    v    v                              v
  child1 child2 child3                    child...

                Leaf Nodes (keys + data pointers)
                         |
    [K1 -> ptr] <-> [K2 -> ptr] <-> [K3 -> ptr] <-> ...
    (linked list)
```

### Example B+ Tree of Order 4 (m=4)

Order 4 means max children = 4, max keys = 3 (internal nodes). Leaf nodes can store at most 3 keys + 3 data pointers.

```
            [50, 100]
           /    |     \
          /     |      \
         /      |       \
    [10,30]  [60,80]  [110,120,130]
       |        |          |
       v        v          v
    Data     Data       Data
    recs     recs       recs
  (linked) (linked)   (linked)

Leaf linked list: [10,30] <-> [60,80] <-> [110,120,130]
```

- The root contains keys 50 and 100.
- All keys < 50 go through the leftmost child.
- Keys between 50 and 100 go through the middle child.
- Keys > 100 go through the rightmost child.
- The actual data is always at the leaves.

---

## Differences from B-Tree (Detailed)

| Aspect              | B-Tree                                    | B+ Tree                                     |
|---------------------|-------------------------------------------|---------------------------------------------|
| Data pointers       | Every node (internal + leaf)              | Leaf nodes only                             |
| Key duplication     | No duplicate keys                         | Keys in internal nodes are duplicated in leaves |
| Leaf node links     | No                                       | Yes (linked list for range scans)           |
| Search termination  | Can end at any level (if found in internal node) | Always ends at leaf level                   |
| Internal node size  | Larger (contains data pointers)          | Smaller (only keys), higher fan-out         |
| Range query speed   | Slow (must traverse up/down tree)         | Fast (traverse to first leaf, then scan leaf list) |
| Common usage        | File systems, some DBMS                   | Most commercial RDBMS (Oracle, MySQL InnoDB, PostgreSQL, SQL Server) |

### Why B+ Trees are Preferred for Databases

1. **Higher fan-out:** Internal nodes store only keys, so many more keys fit in one disk block. A typical block is 4-16 KB. If a key is 8 bytes and a child pointer is 8 bytes, an internal node of a B+ tree can hold ~500 keys per block. The same block in a B-tree would be much smaller because it also holds data pointers.

2. **Shorter tree:** With fan-out of ~500, for 10^7 records, the B+ tree height is log_500(10^7) ~ 3. For 10^12 records, height ~ 5. This means 3-5 disk I/Os for any lookup.

3. **Efficient range queries:** Once the first matching leaf is found, sequential scan through the leaf linked list reads all results with minimal I/O. In a B-tree, you must traverse back up to find the next key, which is expensive.

4. **Predictable performance:** Every search goes exactly to leaf level. No variability.

---

## Fan-Out and Height

### Calculating Fan-Out

Let:
- P = size of a block/pointer (typically 4 or 8 bytes)
- K = size of a key (e.g., 8 bytes for an integer, variable for strings)
- B = block size (e.g., 4096 bytes)

Internal node fan-out (B+ tree):
```
fan_out = floor(B / (P + K))
```

For B = 4096, P = 8, K = 8:
```
fan_out = floor(4096 / 16) = 256
```

So each internal node can have up to 256 children.

### Tree Height

```
height = 1 + log_{fan_out}( N / leaf_capacity )
```

Where leaf_capacity is the number of key-pointer pairs per leaf block.

### Example

Given:
- N = 10^6 records
- Block size = 4 KB
- Key size = 8 B, Pointer size = 8 B
- Internal fan-out = 256
- Leaf capacity (key+ptr pair = 16 B, plus overhead) ~ 250 entries per leaf block

Leaves needed: N / 250 = 4000 leaf blocks.

Height = 1 + log_256(4000) = 1 + log(4000)/log(256) = 1 + 3.6/2.4 = 1 + 1.5 = 2.5 --> 3 levels.

So any lookup requires at most 3 disk I/Os.

---

## Insertion Algorithm

### Steps

1. Find the correct leaf node by traversing from root using key comparisons.
2. Insert the key and data pointer into the leaf node in sorted order.
3. If leaf node has <= max_keys (fan-out - 1), insertion is complete.
4. If leaf node overflows (has more than max_keys):
   - Split leaf into two: first half and second half.
   - The first half remains in the current node.
   - The second half goes into a new node (right sibling).
   - Copy the smallest key of the right node up to the parent (as a separator).
   - Adjust the linked list: new node's next = old node's next, old node's next = new node.
5. If the parent overflows after insertion, repeat step 4 for internal nodes.
   - For internal node splits: **move** (not copy) the middle key up.
6. If root overflows, create a new root with two children.

### Key Difference from B-tree Insertion

- When a leaf splits: the smallest key of the right leaf is **copied** up to the parent (the key remains in the leaf).
- When an internal node splits: the middle key is **moved** up (removed from the internal node).

### Worked Example: Insert into B+ Tree of Order 4 (max keys = 3)

```
Insert 10, 20, 30:

  Leaf: [10, 20, 30]

Insert 40 (overflow):

  Split leaf: [10, 20] and [30, 40]
  Copy smallest key of right leaf (30) up to new root.

       [30]
      /    \
  [10,20] [30,40]

Insert 50:

       [30]
      /    \
  [10,20] [30,40,50]

Insert 60 (overflow in right leaf):

  Split: [30,40] and [50,60]
  Copy 50 up to parent.

       [30, 50]
      /    |    \
  [10,20] [30,40] [50,60]

Insert 70:

       [30, 50]
      /    |    \
  [10,20] [30,40] [50,60,70]

Insert 80 (overflow in right leaf):

  Split: [50,60] and [70,80]
  Copy 70 up to parent.

       [30, 50, 70]
      /    |    |    \
  [10,20] [30,40] [50,60] [70,80]

Insert 90 (overflow in parent -- internal node [30,50,70] with 3 keys + 4 children, inserting key 70... wait, root already has 3 keys:

  Actually, the leaf [70,80] does not overflow -- it has 2 keys (max 3).
  Insert 90 goes to leaf [70,80] -> [70,80,90]. OK.

Insert 25:

       [30, 50, 70]
      /    |    |    \
  [10,20,25] [30,40] [50,60] [70,80,90]
```

---

## Deletion Algorithm

### Steps

1. Find the leaf node containing the key.
2. Delete the key and its pointer from the leaf node.
3. If leaf has >= min_keys, done. (min_keys = ceil(max_children/2) - 1)
4. If leaf underflows:
   - **Borrow from sibling:** If an adjacent sibling has more than min_keys, redistribute keys via the parent.
   - **Merge with sibling:** If sibling only has min_keys, merge the two leaves and delete the separator key from the parent.
5. After merging, if parent underflows, apply borrowing/merging at the internal level.
6. If root becomes empty, delete it.

### Worked Example: Delete from B+ Tree of Order 4

```
Initial tree (order 4, max keys = 3, min keys = 1):

       [30, 50]
      /    |    \
  [10,20] [30,40] [50,60,70]

Delete 20:

  Leaf [10,20] becomes [10] (underflow? min=1, so 1 key is OK).
  Tree unchanged.

Delete 40:

  Leaf [30,40] becomes [30] (still 1 key >= min = 1). OK.

Delete 30:

  Leaf [30] becomes empty. Underflow!
  Sibling [10] has 1 key (min). Cannot borrow. Merge.
  Merge [10] and [] with parent key 30.
  New leaf: [10,30]. Remove separator 30 from parent.

       [50]
      /    \
  [10,30] [50,60,70]

Delete 60:

  Leaf [50,60,70] becomes [50,70] (still >= min = 1). OK.

Delete 70:

  Leaf [50,70] becomes [50] (still >= min = 1). OK.

Delete 50:

  Leaf [50] becomes empty. Sibling [10,30] has 2 keys, can borrow.
  But borrowing in B+ tree: we need to adjust parent separator.
  Actually let us reexamine: after deleting 50, leaf is [].
  Sibling [10,30] has 2 keys (min=1, max=3). It can spare one.
  Redistribution: move the first key from sibling to underflow leaf through parent.
  After redistribution:
    Leaf L: [30]
    Leaf R: [10]
    Parent separator becomes 30.
  But wait -- we need to maintain sorted order. Let me redo.

Better to merge: merge [] with [10,30] and update parent.
  After merge: [10,30,50]? No -- key 50 is the one being deleted.

Let me trace carefully:

  Initial before deleting 50: 
       [50]
      /    \
  [10,30] [50,60,70]

  Delete 50: leaf R = [50,60,70] -> [60,70]
  Root = [50]. But 50 is still in the internal node! We need to replace it.
  Actually after deleting 50 from leaf, the separator key in the root still says 50.
  In B+ trees, internal separators are approximate guides. We can replace 50 with 60 (the smallest key in the right subtree).
  So root becomes [60].

  Tree:
       [60]
      /    \
  [10,30] [60,70]
```

---

## Comparison: Search Operations

### Point Query (Equality Search)

```
SELECT * FROM Employee WHERE emp_id = 42;
```

**B+ Tree:** Traverse from root to leaf using key comparisons. Always exactly height I/Os.

**B-tree:** Traverse from root; if key is found in internal node, return early. Average I/O may be slightly less, but worst case is the same.

### Range Query

```
SELECT * FROM Employee WHERE emp_id BETWEEN 10 AND 100;
```

**B+ Tree:**
1. Find leaf containing 10 (height I/Os).
2. Scan forward through leaf linked list until key > 100. Sequential I/O.

The number of I/Os = height + number of leaf blocks in range.

**B-tree:**
1. Find node containing 10.
2. Traverse to next key (may need to go up and down the tree).
Each step can require additional disk I/Os. Much slower for large ranges.

---

## B+ Tree in Practice

Most major databases use B+ trees:

- **MySQL InnoDB:** The primary key index is a clustered B+ tree. Secondary indexes are also B+ trees (non-clustered).
- **PostgreSQL:** The default index type is B+ tree (implemented as `btree` access method).
- **Oracle:** B-tree indexes (actually B+ trees in implementation).
- **SQL Server:** Clustered and non-clustered indexes use B+ tree structures.

---

## Practice Problems

**Problem 1:** A B+ tree with order m=100 (max children = 100) is used to index a table of 5,000,000 records. Each leaf block can hold 50 key-pointer pairs. Estimate the tree height.

<details>
<summary>Answer</summary>

- Number of leaf blocks needed = 5,000,000 / 50 = 100,000.
- Internal fan-out = ~100 (worst case 50% full, but for estimation use 100).
- Height = 1 + log_100(100,000) = 1 + log(100,000)/log(100) = 1 + 5/2 = 1 + 2.5 = 3.5 = 4 levels.

So at most 4 disk I/Os for any lookup.
</details>

**Problem 2:** Draw the B+ tree of order 3 (max keys = 2) after inserting: 1, 2, 3, 4, 5, 6.

<details>
<summary>Answer</summary>

Order 3: max children = 3, max keys = 2, min keys = ceil(3/2)-1 = 1.

Insert 1,2: [1,2]
Insert 3 (overflow):
  Split leaf: [1] and [2,3]
  Copy 2 up.
       [2]
      /   \
   [1]   [2,3]
Insert 4:
       [2]
      /   \
   [1]   [2,3,4]
Insert 5 (right leaf overflow):
  Split: [2,3] and [4,5]
  Copy 4 up.
       [2,4]
      /  |  \
   [1] [2,3] [4,5]
Insert 6:
       [2,4]
      /  |  \
   [1] [2,3] [4,5,6] (OK, 3 keys > max 2! Overflow)
  Split leaf: [4,5] and [6]
  Copy 6 up to parent.
  Parent [2,4,6] overflows. Split internal node: [2] and [6], move 4 up.
       [4]
      /   \
   [2]    [6]
  /   \   /   \
[1] [2,3] [4,5] [6]
</details>

**Problem 3:** What is the main reason B+ trees have higher fan-out than B-trees for the same block size?

<details>
<summary>Answer</summary>

In a B+ tree, internal nodes store only keys and child pointers (no data pointers). For a block size of 4 KB, this means ~250 key-pointer entries. In a B-tree, internal nodes also store data pointers, reducing the number of entries per block to ~125. Higher fan-out = shorter tree = fewer I/Os.
</details>

**Problem 4:** When a leaf node in a B+ tree splits, the smallest key of the right node is COPIED up to the parent. When an internal node splits, the middle key is MOVED up. Explain why the difference matters.

<details>
<summary>Answer</summary>

In leaf splits, the key that is copied up remains in the right leaf node because all keys must appear in the leaf level (all data pointers must be accessible from leaves). In internal node splits, the moved key is removed from the internal node because internal keys serve only as separators; they do not need to appear at the internal level again. If we copied the key, it would appear twice in the internal nodes, wasting space and potentially causing incorrect routing.
</details>

**Problem 5:** Explain how the leaf linked list in a B+ tree enables efficient range queries. What is the time complexity?

<details>
<summary>Answer</summary>

For a range query `WHERE key BETWEEN a AND b`, the DBMS traverses the tree from root to leaf (O(log n) I/Os) to find the first leaf containing `a`. Then it scans the leaf's key list sequentially. When reaching the end of the leaf block, it follows the linked list pointer to the next leaf block. This continues until encountering a key > `b`. Total I/O = O(log n + k) where k is the number of leaf blocks covering the range. In a B-tree without leaf links, each step to the next key could require a parent traversal, making range queries O(k log n).
</details>

---
