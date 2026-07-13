# Lossless Design

**Course:** Database Management Systems  
**Module:** 2 | **Lecture:** 13  
**Date:** 27-Aug-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## What is Lossless Join Decomposition?

A decomposition `D = {R1, R2, ..., Rn}` of `R` has a **lossless join** if, for every instance `r` of `R` that satisfies the given FDs:

```
r = pi_R1(r) bowtie pi_R2(r) bowtie ... bowtie pi_Rn(r)
```

In plain terms: joining all decomposed relations must give back **exactly** the original relation -- no extra rows (lossy) and no missing rows.

### Lossless vs Lossy

**Lossless:** The natural join of the projections equals the original relation.

**Lossy (or Lossy-Join):** The natural join of the projections produces **extra tuples** (spurious tuples) that were not in the original relation.

---

## Example: Lossless Decomposition

`EMPLOYEE(EmpID, Name, DeptID, Salary)`:

| EmpID | Name | DeptID | Salary |
|-------|------|--------|--------|
| 101 | Alice | D1 | 60000 |
| 102 | Bob | D2 | 45000 |

**Decomposition:** `R1(EmpID, Name, DeptID)` and `R2(EmpID, Salary)`.

**Projection onto R1:**

| EmpID | Name | DeptID |
|-------|------|--------|
| 101 | Alice | D1 |
| 102 | Bob | D2 |

**Projection onto R2:**

| EmpID | Salary |
|-------|--------|
| 101 | 60000 |
| 102 | 45000 |

**Natural Join (R1 bowtie R2):**

| EmpID | Name | DeptID | Salary |
|-------|------|--------|--------|
| 101 | Alice | D1 | 60000 |
| 102 | Bob | D2 | 45000 |

This matches the original. **Lossless.**

---

## Example: Lossy Decomposition

`EMPLOYEE(EmpID, Name, DeptID, Salary)`:

| EmpID | Name | DeptID | Salary |
|-------|------|--------|--------|
| 101 | Alice | D1 | 60000 |
| 102 | Bob | D2 | 45000 |

**Decomposition:** `R1(EmpID, Name)` and `R2(DeptID, Salary)`.

**Projection onto R1:**

| EmpID | Name |
|-------|------|
| 101 | Alice |
| 102 | Bob |

**Projection onto R2:**

| DeptID | Salary |
|--------|--------|
| D1 | 60000 |
| D2 | 45000 |

**Natural Join (R1 bowtie R2):**

| EmpID | Name | DeptID | Salary |
|-------|------|--------|--------|
| 101 | Alice | D1 | 60000 |
| 101 | Alice | D2 | 45000 |
| 102 | Bob | D1 | 60000 |
| 102 | Bob | D2 | 45000 |

This has **4 tuples** instead of the original 2! Spurious tuples were created. **Lossy.**

**Why?** There is no common attribute between R1 and R2 on which to join meaningfully. The join matches every EmpID with every DeptID combination.

---

## Testing Lossless Join: The Tableau Method

The **tableau method** (also called the Chase test) determines if a decomposition is lossless.

### Algorithm

1. Create a tableau (matrix) with one row for each relation `Ri` and one column for each attribute of `R`.
2. In row `i`, put `a_j` for column `j` if attribute `j` is in `Ri`; otherwise put `b_ij`.
3. Repeatedly apply the FDs to make symbols equal:
   - For each FD `X -> Y`, find rows that agree on X. If they disagree on Y, make the Y-values equal.
   - Use the rule: if one symbol is `a_j` (subscripted), make the other `a_j`; otherwise make them the same `b` symbol.
4. If any row becomes all `a`-symbols (`a1, a2, ..., an`), the decomposition is **lossless**.

### Example 1: Testing Lossless

`R(A, B, C)`, FDs: `{A -> B, B -> C}`.
Decomposition: `R1(A, B)`, `R2(A, C)`.

**Step 1:** Create tableau

| Row | A | B | C |
|-----|---|---|---|
| R1 | a1 | a2 | b13 |
| R2 | a1 | b22 | a3 |

**Step 2:** Apply FD `A -> B`. R1 and R2 both have `a1` in A. They disagree on B: R1 has `a2`, R2 has `b22`. Make them equal: set `b22 = a2`.

| Row | A | B | C |
|-----|---|---|---|
| R1 | a1 | a2 | b13 |
| R2 | a1 | a2 | a3 |

**Step 3:** Apply FD `B -> C`. Look for rows with same B value. R1 and R2 both have `a2` in B. They disagree on C: R1 has `b13`, R2 has `a3`. Set `b13 = a3`.

| Row | A | B | C |
|-----|---|---|---|
| R1 | a1 | a2 | a3 |
| R2 | a1 | a2 | a3 |

**Step 4:** Row 1 (for R1) now has all `a`-symbols: `{a1, a2, a3}`. Therefore, the decomposition is **lossless**.

### Example 2: Lossy Result

`R(A, B, C)`, FDs: `{A -> B, B -> C}`.
Decomposition: `R1(A, B)`, `R2(B, C)`.

**Step 1:** Create tableau

| Row | A | B | C |
|-----|---|---|---|
| R1 | a1 | a2 | b13 |
| R2 | b21 | a2 | a3 |

**Step 2:** Apply FD `A -> B`. No two rows have same A value (R2 has `b21`). No change.

**Step 3:** Apply FD `B -> C`. R1 and R2 both have `a2` in B. Disagree on C: R1 has `b13`, R2 has `a3`. Set `b13 = a3`.

| Row | A | B | C |
|-----|---|---|---|
| R1 | a1 | a2 | a3 |
| R2 | b21 | a2 | a3 |

**Step 4:** No row has all `a`-symbols. R1 is missing `a` in no column... wait, R1 has A=a1, B=a2, C=a3. That's all `a`! So actually it is lossless!

Let me reconsider. R1(A,B) has {A,B}. The tableau row for R1 should have `a` for columns A and B, and `b` for C. After applying B->C, the b value for C in row R1 becomes a3. So row R1 becomes (a1, a2, a3) -- all a-symbols. Lossless.

Hmm, so `{AB, BC}` with `{A->B, B->C}` is actually lossless. Let me find a truly lossy example.

### Example 3: Truly Lossy

`R(A, B, C)`, FDs: `{A -> B}`.
Decomposition: `R1(A, C)`, `R2(B, C)`.

**Step 1:** Create tableau

| Row | A | B | C |
|-----|---|---|---|
| R1 | a1 | b12 | a3 |
| R2 | b21 | a2 | a3 |

**Step 2:** Apply FD `A -> B`. R1 has A=a1, R2 has A=b21. No match. No change.

**Step 3:** No more FDs to apply.

**Step 4:** No row has all `a`-symbols. R1 has A=a1, C=a3 but B=b12. R2 has B=a2, C=a3 but A=b21. **Lossy.**

---

## Sufficient Condition for Lossless Binary Decomposition

For a decomposition of R into **two** relations R1 and R2, the decomposition is lossless if and only if:

`R1 cap R2 -> R1` OR `R1 cap R2 -> R2`

(The common attributes of R1 and R2 form a superkey for at least one of them.)

### Examples

- `R1(EmpID, Name, DeptID)`, `R2(EmpID, Salary)`: Common = `EmpID`. `EmpID -> R1`? EmpID determines Name and DeptID, so YES. Lossless.

- `R1(EmpID, Name)`, `R2(DeptID, Salary)`: Common = {} (no common attributes). Neither empty set -> anything. LOSSY.

- `R1(A, B)`, `R2(A, C)`: Common = A. Does A -> AB? Yes, if `A -> B` holds. Does A -> AC? Yes, always. So if `A -> B` is an FD, lossless.

---

## Importance in Normalization

When normalizing (decomposing) relations, we want both:
1. **Lossless join** -- no information is lost
2. **Dependency preservation** -- all FDs can be enforced

Every decomposition algorithm for 3NF and BCNF guarantees lossless join.

| Property | 3NF Decomposition | BCNF Decomposition |
|----------|-------------------|---------------------|
| Lossless Join | Always guaranteed | Always guaranteed |
| Dependency Preservation | Always guaranteed | Not always guaranteed |

---

## Practice Problems

1. Given `R(A, B, C)` with `F = {A -> B}`, decomposition `R1(A, B)`, `R2(B, C)`. Is it lossless?

2. Given `R(A, B, C, D)` with `F = {AB -> C, C -> D}`, decomposition `R1(A, B, C)`, `R2(C, D)`. Is it lossless? Use both the sufficient condition and the tableau method.

3. Explain why lossless decomposition is important.

4. Given `R(A, B, C, D, E)` with `F = {A -> BC, CD -> E, B -> D, E -> A}`, decomposition `R1(A, B, C)`, `R2(A, D, E)`. Is it lossless?

5. What is the difference between lossless and dependency-preserving decomposition?

**Answers:**
1. Common = {B}. Does B -> R1(A,B)? Not necessarily (B -> A is not given). Does B -> R2(B,C)? Yes (B -> C is not given either). Hmm, B+ under F: B+ = {B}. So neither `B -> R1` nor `B -> R2` holds. But let me use the tableau:
   R1: (a1, a2, b13), R2: (b21, a2, a3). Apply FD A->B: no two rows have same A. So no change. Row 1: (a1, a2, b13). Row 2: (b21, a2, a3). Neither is all-a. Lossy.

2. Common = {C}. Does C -> R1(A,B,C)? C+ = {C,D}. Missing A,B. No. Does C -> R2(C,D)? C+ = {C,D}. C -> D is in F. Yes! So lossless.

3. Lossless decomposition ensures that when we join the decomposed relations, we get back exactly the original data without any spurious tuples. Without it, queries that join the decomposed tables would produce incorrect (extra) results.

4. Common = {A}. Compute A+ under F: A->BC, B->D, so A+ = {A,B,C,D}. Also CD->E, so A+ = {A,B,C,D,E}. A determines all attributes. So A is a superkey of R. Does A -> R1? Yes (A+ contains all of R1's attributes). Lossless.

5. Lossless ensures no spurious tuples upon joining; dependency preservation ensures all FDs can be checked on individual relations without joins. A decomposition can be lossless but not dependency-preserving, or vice versa (though the latter is less useful).
