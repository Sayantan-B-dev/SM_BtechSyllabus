# B-Trees

**Course:** Database Management Systems  
**Module:** 3 | **Lecture:** 2  
**Date:** 08-Sep-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 3  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## What is a B-Tree?

A B-tree is a balanced, multi-level tree data structure that maintains sorted data and allows efficient insertion, deletion, and search operations. It is the most widely used index structure in database systems. Unlike a binary search tree, a B-tree node can have **many children** (high fan-out), which keeps the tree short and minimizes disk I/O.

### Why B-Trees for Databases?

- Disk access is slow (milliseconds per random read). B-trees are shallow: for millions of keys, a B-tree of order ~500 has height 3-4.
- Each node corresponds to a disk block, so reading a node = one disk I/O.
- B-trees are **self-balancing**, so worst-case performance is guaranteed O(log n) for search.

---

## B-Tree Properties

A B-tree of **order m** (also called degree m) satisfies these rules:

1. **Every node has at most m children.** This means a node can hold at most m-1 keys.
2. **Every node (except root) has at least ceil(m/2) children.** This ensures the tree stays balanced (minimum 50% occupancy).
3. **The root has at least 2 children** if it is not a leaf.
4. **All leaves appear at the same depth** (the tree is perfectly balanced).
5. **A non-leaf node with k children contains k-1 keys.**
6. **Keys within a node are stored in sorted order.**
7. **The keys in a subtree between two keys k_i and k_{i+1} are all between k_i and k_{i+1}.**

### Example: B-tree of Order 5 (m=5)

```
Maximum children per node: 5
Maximum keys per node: 4 (m-1)
Minimum children (non-root): ceil(5/2) = 3
Minimum keys (non-root): 2 (ceil(m/2)-1)
```

---

## B-Tree Structure

### Three Types of Nodes

```
[ Root Node ]
  Contains 1 to m-1 keys.
  If not leaf, has 2 to m children.

[ Internal Nodes ]
  Contains ceil(m/2)-1 to m-1 keys.
  Has ceil(m/2) to m children.
  Serve as routing nodes.

[ Leaf Nodes ]
  Contains ceil(m/2)-1 to m-1 keys.
  No children.
  In a B-tree (not B+ tree), leaf nodes contain pointers to data records.
```

### Visual: B-tree of Order 5 (m=5)

```
                     [ 50, 100, 150 ]
                    /     |    |     \
                   /      |    |      \
                  /       |    |       \
    [10, 20, 30]  [60, 70, 80] [110, 120] [160, 170, 180, 190]
        (leaf)        (leaf)      (leaf)         (leaf)
```

- All leaves are at the same depth (depth = 1 from root).
- Each node holds keys in sorted order.
- Between 50 and 100: all keys between 50 and 100 (exclusive) go to the child subtree of 50-100.

---

## Searching in a B-Tree

**Algorithm:**

1. Start at the root.
2. Find the smallest key >= search_key. If found, follow the pointer BEFORE that key.
3. If search_key equals a key in the node, return the record pointer.
4. If leaf is reached and key not found, the key does not exist.

**Example:** Search for key 70 in the tree above.

```
Step 1: Root = [50, 100, 150]. 70 is between 50 and 100, follow middle-left child.
Step 2: Child = [60, 70, 80]. 70 found. Return record pointer.
```

---

## Insertion Algorithm

**Key idea:** Insert into leaf. If leaf overflows (keys > m-1), split the node and promote the middle key to the parent.

### Steps

1. Search the tree to find the correct leaf position for the new key.
2. Insert the key into the leaf in sorted order.
3. If the leaf has <= m-1 keys after insertion, done.
4. If the leaf overflows (has m keys):
   - Split into two nodes: left node with first floor((m)/2) keys, right node with remaining keys.
   - Promote the middle key to the parent.
   - Insert the middle key into the parent in sorted order.
5. If the parent overflows, repeat step 4 recursively up the tree.
6. If the root overflows, create a new root with the promoted middle key.

### Worked Example: Insertion into B-tree of Order 5 (m=5)

```
Initial tree (empty): [ ]

Insert 10:
  [10]

Insert 20:
  [10, 20]

Insert 30:
  [10, 20, 30]

Insert 40:
  [10, 20, 30, 40]

Insert 50 (OVERFLOW!):
  Before split: [10, 20, 30, 40, 50]
  After split (middle key = 30):
        [30]
       /    \
  [10, 20]  [40, 50]

Insert 60:
        [30]
       /    \
  [10, 20]  [40, 50, 60]

Insert 70:
        [30]
       /    \
  [10, 20]  [40, 50, 60, 70]

Insert 80 (OVERFLOW!):
  Node [40, 50, 60, 70, 80] splits.
  Middle key = 60 promoted.
        [30, 60]
       /    |    \
  [10,20] [40,50] [70,80]

Insert 5:
        [30, 60]
       /    |    \
  [5,10,20] [40,50] [70,80]
```

---

## Deletion Algorithm

**Key idea:** Delete from leaf. If leaf underflows (keys < ceil(m/2)-1), try to borrow from a sibling (redistribution) or merge with a sibling.

### Steps

1. Search for the key to delete.
2. If the key is in an internal node:
   - Replace it with the largest key from the left subtree (predecessor) or the smallest key from the right subtree (successor).
   - Then delete that replacement key from the leaf.
3. If the key is in a leaf, delete it.
4. If after deletion, the node has >= ceil(m/2)-1 keys, done.
5. If underflow (too few keys):
   - **Redistribution:** Try to borrow a key from an adjacent sibling. The parent key is adjusted accordingly.
   - **Merge:** If sibling cannot spare a key, merge the node with a sibling and pull down the parent key.
6. If the parent underflows, apply steps 4-5 recursively upward.
7. If the root becomes empty, remove it.

### Worked Example: Deletion from B-tree of Order 5 (m=5)

```
Start with:
        [30, 60]
       /    |    \
  [10,20] [40,50] [70,80]

Delete 20 (simple, no underflow):
        [30, 60]
       /    |    \
  [10] [40,50] [70,80]
  (Still has 1 key >= min of 2? Wait -- order 5: ceil(5/2)-1 = 2. Node [10] has only 1 key. UNDERFLOW.)

Fix underflow in [10]:
  Try to borrow from sibling [40,50]. Sibling has 2 keys; borrowing one gives:
  Redistribution via parent key 30:
        [40, 60]
       /    |    \
  [10,30] [50] [70,80]
  Wait, we need to be precise.

Let me redo carefully.

Start tree (order 5, min keys = 2):
        [30, 60]
       /    |    \
  [10,20] [40,50] [70,80]

Delete 20:
  Leaf [10,20] becomes [10] -- only 1 key. Min required = 2. Underflow.
  Borrow from sibling [40,50] (has 2 keys, can spare 1):
    Left sibling gets 10, parent key 30 comes down, sibling key 40 goes up.
  Result:
        [40, 60]
       /    |    \
  [10,30] [50] [70,80]

Delete 40:
  Find 40 in root: replace with predecessor (largest in left subtree = 30).
  Delete 30 from leaf [10,30] --> leaf becomes [10] -- underflow (1 < 2).
  Borrow from sibling [50]? Sibling has only 1 key (cannot spare). Must MERGE.
  Merge [10] and [50] with parent key 40.
  Result:
        [60]
       /    \
  [10,40,50] [70,80]

  Check root: [60] has 1 key, OK (root can have 1 key).
  Check leaf [10,40,50]: 3 keys, within limit.
```

---

## B-Tree vs B+ Tree Comparison

| Feature              | B-Tree                                      | B+ Tree                                      |
|----------------------|---------------------------------------------|----------------------------------------------|
| Data pointers        | Internal nodes AND leaf nodes contain data pointers | Only leaf nodes contain data pointers. Internal nodes are pure routers (keys only). |
| Redundancy           | Keys appear at most once in the tree.       | Keys appear in internal nodes (as routers) AND in leaves (as data entries). Keys are duplicated. |
| Leaf node linking    | Leaf nodes are NOT linked.                  | Leaf nodes are linked in a linked list (sequence set). |
| Range query          | Inefficient: must traverse up and down the tree. | Highly efficient: traverse to first leaf, then scan the linked list. |
| Fan-out (internal nodes) | Smaller fan-out because internal nodes store both keys and data pointers (larger node size for same block). | Larger fan-out because internal nodes store only keys (smaller entries per block). |
| Tree height          | Taller (smaller fan-out).                   | Shorter (larger fan-out), better disk I/O.   |
| Space utilization    | Keys stored once, but dat pointers consume space in internal nodes. | Some key duplication, but internal nodes are dense with keys. |
| Typical use          | File systems, some databases.               | Most modern RDBMS (Oracle, MySQL InnoDB, PostgreSQL, SQL Server). |

### Detailed Discussion

**In a B-tree:** Every node stores keys and associated data pointers. Searching can end at any level (if the key is found in an internal node). However, this means internal nodes are bulky, reducing fan-out and increasing tree height.

**In a B+ tree:** Internal nodes are pure routing structures that contain only keys (no data pointers). All actual data resides in the leaves. The leaves form a linked list for efficient sequential access.

**Why B+ trees are preferred for databases:**
- Higher fan-out means shorter tree (fewer disk seeks).
- Sequential scan of leaf nodes supports efficient range queries.
- More predictable performance (all queries traverse exactly to leaf level).
- Higher concurrency (locking only affects leaf nodes during inserts).

---

## Summary of B-Tree Concepts

| Term          | Meaning                                              |
|---------------|------------------------------------------------------|
| Order m       | Maximum children per node.                           |
| Fan-out       | Average number of children per node.                 |
| Root          | Top node (can have as few as 1 key and 2 children).  |
| Leaf          | Bottom node (contains data pointers, no children).   |
| Overflow      | Node has m keys (too many), triggers split.          |
| Underflow     | Node has fewer than ceil(m/2)-1 keys, triggers redistribution or merge. |
| Height        | Number of levels (root to leaf). All leaves at same depth. |

---

## Practice Problems

**Problem 1:** A B-tree of order 7 (m=7) has a root that is not a leaf. How many keys must the root have at minimum? How many children?

<details>
<summary>Show Answer</summary>

For the root, minimum children = 2. Minimum keys = 1 (since keys = children - 1). There is no lower bound on the number of keys in the root (unlike other nodes).
</details>

**Problem 2:** Draw the B-tree of order 3 (m=3, also called a 2-3 tree) after inserting the keys: 10, 5, 15, 3, 7, 12, 18.

<details>
<summary>Show Answer</summary>

m=3: max keys = 2, min keys (non-root) = ceil(3/2)-1 = 1. Min children = 2.

Insert 10: [10]
Insert 5: [5, 10]
Insert 15 (overflow): split -> 
      [10]
     /    \
  [5]     [15]
Insert 3: 
      [10]
     /    \
  [3,5]   [15]
Insert 7:
      [10]
     /    \
  [3,5,7] [15] --> overflow on left:
      [5, 10]
     /   |   \
  [3]  [7]   [15]
Insert 12:
      [5, 10]
     /   |    \
  [3]  [7]  [12,15]
Insert 18:
      [5, 10]
     /   |    \
  [3]  [7]  [12,15,18] --> overflow:
        [5, 10, 15]
       /   |    |   \
    [3]  [7]  [12]  [18]
</details>

**Problem 3:** What is the maximum number of keys in a B-tree of order m=100 and height 3 (root at level 0, leaves at level 3)?

<details>
<summary>Show Answer</summary>

- Root: max m-1 = 99 keys, max m = 100 children.
- Level 1: 100 nodes, each with max 99 keys, max 100 children each.
- Level 2: 100^2 = 10,000 nodes, each with max 99 keys, max 100 children each.
- Level 3 (leaves): 100^3 = 1,000,000 nodes, each with max 99 keys.
- Total max keys = 99 + 100*99 + 10000*99 + 1M*99 = 99 * (1 + 100 + 10,000 + 1,000,000) = 99 * 1,010,101 = 100,000,000 (approx).
</details>

**Problem 4:** In the B-tree deletion algorithm, what is the difference between redistribution and merging? When is each used?

<details>
<summary>Show Answer</summary>

When a node underflows, the DBMS first checks if an adjacent sibling has more than the minimum number of keys. If yes, **redistribution** is used: one key moves from sibling through the parent to the underflowing node. If the sibling also has only the minimum number of keys, **merging** is used: the underflowing node, the sibling, and the parent key between them are combined into a single node.
</details>

**Problem 5:** Why is a B-tree preferred over a binary search tree for database indexing?

<details>
<summary>Show Answer</summary>

A binary search tree has fan-out = 2, so its height is O(log2 n). For n = 10^6, height ~ 20. A B-tree of order 500 has fan-out ~ 250 (average), height ~ log250(10^6) ~ 3. Each node access = one disk I/O. The B-tree requires ~3 I/Os vs ~20 for BST. B-trees are also self-balancing, while BSTs can degenerate to O(n) height in the worst case.
</details>

---
