# Join Strategies and Query Optimization

**Course:** Database Management Systems  
**Module:** 2 | **Lecture:** 15  
**Date:** 03-Sep-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## Join Strategies

Joins are the most expensive operations in query processing. Choosing the right join algorithm is critical for performance.

**Notation:** We join relation R (with `br` blocks, `nr` tuples) and S (with `bs` blocks, `ns` tuples).

---

## 1. Nested Loop Join

**Algorithm:**
```
for each tuple r in R:
    for each tuple s in S:
        if r.join_attr = s.join_attr:
            output (r, s)
```

**Cost:** `nr * ns` tuple comparisons, `br + nr * bs` block transfers (if S is scanned for each R tuple)

**Best for:** Small relations (specifically, the outer relation should be small).

**Example:** R(100 tuples, 10 blocks), S(1000 tuples, 100 blocks)
- Cost (R outer): 10 + 100 * 100 = 10,010 block transfers
- Cost (S outer): 100 + 1000 * 10 = 10,100 block transfers

Choose the smaller relation as outer.

---

## 2. Block Nested Loop Join

**Algorithm:**
```
for each block Br of R:
    for each block Bs of S:
        for each tuple r in Br:
            for each tuple s in Bs:
                if r.join_attr = s.join_attr:
                    output (r, s)
```

**Cost:** `br * bs` block transfers (processing). If memory holds `M` blocks for the outer relation, blocks of S are read `ceiling(br/(M-1))` times.

**Best for:** When one relation fits in memory.

**Example:** R(10 blocks), S(100 blocks), M = 5 blocks memory
If R is outer (use M-1=4 blocks for R): ceiling(10/4) = 3 passes
Cost = br + 3 * bs = 10 + 3 * 100 = 310 block transfers

If S is outer (use 4 blocks for S): ceiling(100/4) = 25 passes
Cost = bs + 25 * br = 100 + 25 * 10 = 350 block transfers

Better to use the smaller relation as outer.

---

## 3. Indexed Nested Loop Join

**Prerequisite:** An index exists on the join attribute of the **inner** relation.

**Algorithm:**
```
for each tuple r in R:
    use index on S to find tuples s matching r
    for each matching s:
        output (r, s)
```

**Cost:** `br + nr * c` where `c` is the cost of a single index lookup + fetch in S.

**Important:** This is good only when the inner relation has an index on the join attribute.

**Example:** R(100 tuples), S(1000 tuples) with B+ tree index on S.join_attr
- Cost per index lookup: 2-4 block accesses (for a B+ tree of depth 2-4)
- Cost to fetch matching tuple: 1 block access (if clustered) or more (if unclustered)
- Total: ~100 * (3 + 1) = 400 block accesses + reading R (10 blocks) = 410

Compare with nested loop (10,000+ blocks). Indexed join is much faster.

---

## 4. Merge Join (Sort-Merge Join)

**Algorithm:**
1. Sort R and S on the join attribute (if not already sorted)
2. Use two pointers to scan both sorted relations simultaneously

```
sort R on join_attr
sort S on join_attr
i = 1, j = 1
while i <= nr and j <= ns:
    if R[i] < S[j]: i++
    elif R[i] > S[j]: j++
    else:  // equal
        output all matching pairs
        i++ (or j++)
```

**Cost:** `br + bs` (for reading) + sorting cost + `br + bs` (for writing sorted runs)

If both relations are already sorted on the join attribute: cost = `br + bs`.

**Best for:** Large relations where both can be sorted, or are already sorted.

**Example:** R(1000 blocks), S(2000 blocks), both already sorted on join attr.
Cost = 1000 + 2000 = 3000 block transfers.

---

## 5. Hash Join

**Algorithm:**
1. **Partition phase:** Hash both relations on the join attribute into partitions using the same hash function
2. **Probe phase:** For each partition, build a hash table on the smaller relation and probe with the larger

```
-- Partition
for each tuple r in R:
    h = hash(r.join_attr)
    put r in partition R[h]
for each tuple s in S:
    h = hash(s.join_attr)
    put s in partition S[h]

-- Probe
for each partition i:
    build hash table on R[i] (smaller partition)
    for each tuple s in S[i]:
        probe hash table for matching r
        output (r, s)
```

**Cost:** `3 * (br + bs)` block transfers (reading, writing partitions, reading again)

**Best for:** Large relations, especially when one relation fits in memory.

**Requirement:** The hash function must distribute tuples evenly across partitions.

---

## Cost Comparison Summary

| Join Method | Cost (block transfers) | Best Use Case |
|-------------|----------------------|---------------|
| Nested Loop | `br + nr * bs` | Very small relations |
| Block Nested Loop | `br + br/(M-1) * bs` | Medium, some memory available |
| Indexed Nested Loop | `br + nr * c` | Index exists on inner join attr |
| Merge Join | Sorting + `br + bs` | Already sorted or large relations |
| Hash Join | `3 * (br + bs)` | Large unsorted relations |

---

## Query Optimizer

A **query optimizer** transforms a SQL query into an efficient execution plan.

### Types of Optimizers

| Type | Description | Examples |
|------|-------------|----------|
| **Cost-based** | Estimates cost of each plan using statistics (cardinality, selectivity, indexes) | Oracle, PostgreSQL, DB2 |
| **Rule-based** | Applies heuristic rules (e.g., push selection down) without cost estimation | Older Oracle, some embedded DBs |

### Statistics Used for Optimization

- **Cardinality:** Number of tuples in each relation
- **Selectivity:** Fraction of tuples satisfying a condition (e.g., `Dept = 'IT'` might have selectivity 0.3)
- **Index statistics:** Height of B+ tree, number of distinct keys, clustering factor
- **Data distribution:** Histograms for attribute value distributions

### Cost Estimation Example

**Query:** `SELECT * FROM EMPLOYEE WHERE Salary > 50000`
**Statistics:** EMPLOYEE has 10,000 tuples, Salary histogram shows 2000 tuples with Salary > 50000

**Plan A (Full Table Scan):** 
Cost = 10,000 tuples read = ~1000 block transfers (assuming 10 tuples/block)

**Plan B (Index Scan on Salary):**
B+ tree on Salary with height 3, 2000 tuples to fetch
Cost = 3 (index traversal) + 2000 (tuple fetches, possibly 2000 blocks if unclustered)
= 2003 block transfers

If the index is clustered (Salary-ordered storage), the 2000 tuples might be in ~200 blocks.
Cost = 3 + 200 = 203 block transfers.

With 10,000 tuples, the optimizer might choose the index if it's clustered, or full scan if not.

---

## Choosing a Join Strategy: Decision Process

```
                      +---------------------+
                      | Is one relation very |
                      | small (< 10 blocks)?|
                      +---------+-----------+
                               |
                  YES          |          NO
                  +------------+------------+
                  |                         |
         Block Nested Loop          +-------+--------+
         (small as outer)           | Are relations  |
                                    | already sorted |
                                    | on join attr?  |
                                    +-------+--------+
                                            |
                               YES          |          NO
                              +-------------+-------------+
                              |                           |
                         Merge Join            +----------+----------+
                         (no sorting cost)     | Is there an index   |
                                                | on join attr of one |
                                                | relation?           |
                                                +----------+----------+
                                                           |
                                              YES         |          NO
                                             +------------+------------+
                                             |                         |
                                   Indexed Nested Loop        Hash Join or
                                                               Merge Join
                                                               (with sorting)
```

---

## Worked Example

**Query:** Find employee names and department names for employees in IT.

```sql
SELECT e.Name, d.DName
FROM EMPLOYEE e, DEPARTMENT d
WHERE e.DeptID = d.DeptID AND d.DName = 'IT';
```

**Statistics:**
- EMPLOYEE: 10,000 tuples, br = 1000 blocks
- DEPARTMENT: 50 tuples, bs = 5 blocks
- IT department has 200 employees

**Available Indexes:**
- Primary index on EMPLOYEE.EmpID
- No index on EMPLOYEE.DeptID
- Primary index on DEPARTMENT.DeptID

**Plan Options:**

**Plan A:** Nested loop with DEPARTMENT as outer (50 tuples)
- For each of 50 department tuples, scan all 1000 blocks of EMPLOYEE
- Cost: 5 + 50 * 1000 = 50,005 block transfers

**Plan B:** Nested loop with EMPLOYEE as outer (10,000 tuples)
- For each of 10000 employee tuples, scan 5 blocks of DEPARTMENT
- Cost: 1000 + 10000 * 5 = 51,000 block transfers

**Plan C:** Apply selection first on DEPARTMENT (IT), then join
- `sigma_DName='IT'(DEPARTMENT)` gives 1 tuple, 1 block
- Block nested loop with this result as outer:
  - 1 block (DEPARTMENT result) + 1 * 1000 (EMPLOYEE) = 1001 blocks
- Cost: 1001 block transfers

**Plan D:** Indexed nested loop
- Assuming no index on EMPLOYEE.DeptID, use DEPARTMENT as outer
- Need to scan all EMPLOYEE tuples: no benefit

**Winner: Plan C** (Selection pushdown + block nested loop with small outer)

---

## Practice Problems

1. Compare nested loop join and block nested loop join. Which is better and why?
<details>
<summary>Show Answer</summary>
Block nested loop is better because it reads the inner relation block-by-block instead of tuple-by-tuple, significantly reducing I/O. For R(10 blocks) and S(100 blocks), nested loop costs ~10 + 100*100 = 10010 blocks, while block nested loop (M=5) costs ~10 + 3*100 = 310 blocks.
</details>

2. When would you choose a hash join over a merge join?
<details>
<summary>Show Answer</summary>
Hash join is preferred when both relations are large and unsorted, and the hash function can distribute tuples evenly. Merge join is preferred when one or both relations are already sorted on the join attribute.
</details>

3. Given R(500 blocks) and S(2000 blocks), both unsorted, with no indexes. Available memory: 10 blocks. Which join strategy would you recommend?
<details>
<summary>Show Answer</summary>
Neither relation is sorted, no indexes exist. Options:
- Block nested loop: R as outer -> 500 + 500/9 * 2000 = 500 + 111,111 = 111,611 blocks
- Hash join: 3*(500+2000) = 7500 blocks
- Merge join: Sorting cost + 2500 = 500*log(500) + 2000*log(2000) + 2500 blocks
Best choice: Hash join.
</details>

4. Explain how a cost-based optimizer differs from a rule-based optimizer.
<details>
<summary>Show Answer</summary>
Cost-based optimizer uses statistics (cardinality, selectivity, index properties) to estimate actual execution costs and chooses the cheapest plan. Rule-based optimizer applies fixed heuristics (e.g., "always push selection down") without estimating costs. Cost-based is generally more accurate but requires good statistics.
</details>

5. For the query `SELECT * FROM R, S WHERE R.A = S.B`, with R having 100 tuples (20 blocks) and S having 1000 tuples (100 blocks), and a B+ tree index on S.B (height 2, clustered), estimate the cost of an indexed nested loop join.
<details>
<summary>Show Answer</summary>
Steps:
- Read R: 20 blocks
- For each of 100 tuples in R, probe S via index:
  - B+ tree traversal: 2 block accesses (height 2)
  - Fetch matching tuple(s): ~1 block (clustered index, assume 1 match per R tuple on average)
  - Cost per probe: 3 blocks
  - Total probe cost: 100 * 3 = 300 blocks
- Total: 20 + 300 = 320 block transfers
</details>

