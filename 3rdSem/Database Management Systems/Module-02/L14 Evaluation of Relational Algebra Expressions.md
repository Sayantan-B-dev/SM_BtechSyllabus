# Evaluation of Relational Algebra Expressions

**Course:** Database Management Systems  
**Module:** 2 | **Lecture:** 14  
**Date:** 27-Aug-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## Query Evaluation Plan

A **query evaluation plan** (or query execution plan) is a sequence of primitive operations (relational algebra operations) used to execute a query. The DBMS's **query optimizer** chooses the most efficient plan from many possible equivalent plans.

**Example:** Find the names of employees in the IT department who earn more than 50000.

SQL:
```sql
SELECT Name FROM EMPLOYEE WHERE Dept = 'IT' AND Salary > 50000;
```

Possible relational algebra plans:

**Plan A:** `pi_Name(sigma_Dept='IT' AND Salary > 50000(EMPLOYEE))`

**Plan B:** `pi_Name(sigma_Dept='IT'(sigma_Salary > 50000(EMPLOYEE)))`

**Plan C:** `pi_Name(sigma_Salary > 50000(sigma_Dept='IT'(EMPLOYEE)))`

All produce the same result, but execution costs may differ based on indexes and data distribution.

---

## Materialization vs Pipelining

### Materialization

The result of each operation is stored as a **temporary relation** (written to disk or memory) before being used by the next operation.

**Example (Plan A materialized):**
1. Read EMPLOYEE table
2. Apply SELECT condition, store result as Temp1
3. Read Temp1, apply PROJECT, store result as Temp2
4. Return Temp2

**Advantages:** Simple to implement.
**Disadvantages:** High I/O cost (writing and reading temporaries).

### Pipelining

Operations are combined so that the output of one operation is fed directly as input to the next, **without storing intermediate results**.

**Example (Plan A pipelined):**
1. Read EMPLOYEE table one tuple at a time
2. For each tuple, check the SELECT condition
3. If it passes, immediately output the Name (PROJECT)
4. Send to client

**Advantages:** No intermediate storage, lower memory usage, faster.
**Disadvantages:** Harder to implement, especially for operations requiring sorting (ORDER BY, DISTINCT).

**When pipelining is NOT possible:**
- Operations that need all input before producing output (aggregates with GROUP BY, sorting)
- When the same intermediate result is used by multiple operations

---

## Selection Pushdown

**Rule:** Apply SELECT operations as **early** as possible to reduce the size of intermediate relations.

**Example:** Find the names of employees in IT.

Without pushdown: `pi_Name(EMPLOYEE bowtie sigma_DName='IT'(DEPT))`

This joins EMPLOYEE with DEPT first (large intermediate), then projects.

With pushdown: `pi_Name(sigma_Dept='IT'(EMPLOYEE) bowtie DEPT)`

Wait, this needs adjustment. Let me use a clearer example:

`pi_Name(sigma_DName='IT'(DEPARTMENT) bowtie EMPLOYEE)`

First select IT department (small), then join with EMPLOYEE.

**General rule:** Move SELECT operations down the operator tree toward the leaves.

### Before Pushdown
```
        PROJECT(Name)
            |
          JOIN (DeptID)
         /        \
    SELECT        SELECT
   (DName='IT')  (Salary>50000)
       |             |
    DEPT          EMPLOYEE
```

### After Pushdown
```
        PROJECT(Name)
            |
          JOIN (DeptID)
         /        \
    SELECT        SELECT
   (DName='IT')  (Salary>50000)
       |             |
    DEPT          EMPLOYEE
```

In this case, both SELECTs are already at the leaves. Pushdown is already optimal.

### Better Example

Before:
```
       PROJECT(Name)
           |
         JOIN (DeptID)
         /           \
    EMPLOYEE        DEPARTMENT
```

After:
```
       PROJECT(Name)
           |
         JOIN (DeptID)
         /           \
    SELECT            DEPARTMENT
  (Salary>50000)
       |
    EMPLOYEE
```

---

## Projection Pushdown

**Rule:** Apply PROJECT as early as possible to reduce the number of columns carried through operations.

**Example:** 
Before: `sigma_Salary > 50000(pi_EmpID, Name, Dept, Salary, HireDate(EMPLOYEE))`

This projects all columns first, then selects. The projection after the sigma could be more selective.

After: `pi_Name(sigma_Salary > 50000(pi_Name, Salary(EMPLOYEE)))`

But wait, we need DeptID for the join. The key is to project only needed attributes at each stage.

### Combining Pushdown Rules

**Canonical heuristic:**
1. Push SELECTs down
2. Push PROJECTs down
3. Combine CARTESIAN PRODUCT with SELECT to form JOIN

---

## Join Ordering

For joins involving multiple relations, the **order of joins** significantly affects performance.

**Example:** Join `A bowtie B bowtie C` where:
- A has 100 tuples
- B has 1000 tuples
- C has 10000 tuples
- A and B match on 50 tuples
- Result of A bowtie B has 50 tuples

**Plan 1:** `(A bowtie B) bowtie C`
- Step 1: Join A(100) x B(1000) = 100,000 comparisons, result = 50 tuples
- Step 2: Join 50 x C(10000) = 500,000 comparisons
- Total: ~600,000 comparisons

**Plan 2:** `(B bowtie C) bowtie A`
- Step 1: Join B(1000) x C(10000) = 10,000,000 comparisons, result = many tuples
- Step 2: Join large result x A(100)
- Total: >10,000,000 comparisons

Plan 1 is clearly better.

---

## Using Indexes

An **index** on an attribute can dramatically speed up SELECT and JOIN operations.

### Index-Based Selection

Without index on Salary: `sigma_Salary > 50000(EMPLOYEE)` scans the entire table (full table scan).

With B+ tree index on Salary: The DBMS can quickly find all tuples with Salary > 50000 by traversing the index.

### Index-Based Join

For `EMPLOYEE bowtie DEPARTMENT` on DeptID:

If there is an index on EMPLOYEE.DeptID:
- For each DEPARTMENT tuple, use the index to find matching EMPLOYEE tuples quickly
- Cost: O(n * log m) where n is DEPARTMENT size, m is EMPLOYEE size

Without index:
- Nested loop join: O(n * m)
- Hash join: O(n + m) with hash table build

---

## Heuristics for Query Optimization

### Summary of Heuristics

| Heuristic | Description | Benefit |
|-----------|-------------|---------|
| **Selection pushdown** | Apply SELECT early | Reduces tuple count early |
| **Projection pushdown** | Apply PROJECT early | Reduces attribute count |
| **Join ordering** | Smallest relations first | Reduces intermediate size |
| **Combine Cartesian with Select** | Replace `times`+`sigma` with join | More efficient join algorithms |
| **Use indexes** | Prefer indexed access paths | Faster data retrieval |

---

## Worked Example: Complex Query Optimization

**Query:** Find names of employees who work in departments with budget > 300000.

SQL:
```sql
SELECT e.Name
FROM EMPLOYEE e, DEPARTMENT d
WHERE e.DeptID = d.DeptID AND d.Budget > 300000;
```

**Step 1: Initial RA Expression**

`pi_Name(sigma_Budget > 300000 AND e.DeptID = d.DeptID(EMPLOYEE times DEPARTMENT))`

**Step 2: Push SELECT down**

Replace Cartesian + Select with Join:
`pi_Name(EMPLOYEE bowtie_DeptID sigma_Budget > 300000(DEPARTMENT))`

**Step 3: Further push SELECT**

The SELECT on Budget > 300000 is already at the leaf for DEPARTMENT. Good.

**Step 4: Projection pushdown**

We only need Name (from EMPLOYEE) and DeptID (for the join). In EMPLOYEE, we need EmpID, Name, DeptID. In DEPARTMENT, we need DeptID (for join) and Budget (for condition).

`pi_Name((pi_Name, DeptID(EMPLOYEE)) bowtie (pi_DeptID(sigma_Budget > 300000(DEPARTMENT))))`

**Step 5: If index on DEPARTMENT.Budget exists, use it.**

---

## Practice Problems

1. Explain how pipelining differs from materialization.
<details>
<summary>Show Answer</summary>
Materialization stores each intermediate result as a temporary relation on disk. Pipelining passes tuples directly between operators without storing intermediates. Pipelining saves I/O but is not always possible (e.g., when sorting is needed).
</details>

2. What is selection pushdown and why is it beneficial?
<details>
<summary>Show Answer</summary>
Selection pushdown moves SELECT operations closer to the leaves of the operator tree, filtering out tuples as early as possible. This reduces the size of intermediate relations, making subsequent operations (joins, projections) faster.
</details>

3. For the query `SELECT * FROM R, S WHERE R.A = S.B AND R.C > 10`, show the initial RA tree and an optimized version.
<details>
<summary>Show Answer</summary>
Initial: `sigma_R.A = S.B AND R.C > 10(R times S)`. Optimized: `sigma_R.A = S.B(sigma_R.C > 10(R) times S)` then replace times+sigma with join: `sigma_R.C > 10(R) bowtie_R.A = S.B S`.
</details>

4. How does the presence of an index affect query evaluation?
<details>
<summary>Show Answer</summary>
An index allows the DBMS to directly access tuples satisfying a condition rather than scanning the entire table. For joins, an index on the join attribute enables indexed nested-loop join which is O(n log m) instead of O(n*m).
</details>

5. Why is join ordering important? Give an example with three relations.
<details>
<summary>Show Answer</summary>
Join ordering determines the size of intermediate results. Joining smaller relations first keeps intermediates small. Example: R(100), S(1000), T(10000). `(R bowtie S) bowtie T` is likely cheaper than `(S bowtie T) bowtie R` because the first joins produce smaller intermediates.
</details>

