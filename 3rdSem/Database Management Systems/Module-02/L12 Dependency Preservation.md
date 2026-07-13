# Dependency Preservation

**Course:** Database Management Systems  
**Module:** 2 | **Lecture:** 12  
**Date:** 25-Aug-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## What is Dependency Preservation?

When we normalize a relation by decomposing it into multiple relations, we want to ensure that all functional dependencies from the original schema can still be enforced **without joining the decomposed relations**.

**Dependency Preservation Definition:** A decomposition `D = {R1, R2, ..., Rn}` of `R` is **dependency-preserving** if the union of the projections of FDs onto each `Ri` logically implies all FDs in `F`.

Formally: `(F1 cup F2 cup ... cup Fn)+ = F+`

Where `Fi` is the projection of `F` onto `Ri`.

---

## Projection of FDs onto a Relation

The projection of a set of FDs `F` onto a relation `Ri` is the set of all FDs in `F+` that involve only attributes of `Ri`.

**Algorithm to compute `pi_Ri(F)`:**
1. For every subset `X` of attributes of `Ri`, compute `X+` (closure under `F`)
2. For every attribute `A` in `Ri` such that `A` is in `X+ - X`, add the FD `X -> A` to the projection
3. Remove redundant FDs to get a minimal cover

### Example

`R(A, B, C, D)` with `F = {A -> B, B -> C, C -> D}`.
Decomposition: `R1(A, B, C)`, `R2(C, D)`.

**Projection onto R1(A, B, C):**
- Compute closures for subsets of {A, B, C}:
  - `A+ = {A, B, C, D}`. Attributes in R1: A, B, C. So `A -> B`, `A -> C` hold in R1.
  - `B+ = {B, C, D}`. Attributes in R1: B, C. So `B -> C` holds in R1.
  - `C+ = {C, D}`. No new attributes in R1. So no new FDs.
  - `AB+ = all`. Already covered.
- Projection `F1 = {A -> B, A -> C, B -> C}`. Minimal: `{A -> B, B -> C}`.

**Projection onto R2(C, D):**
- Compute closures for subsets of {C, D}:
  - `C+ = {C, D}`. So `C -> D` holds.
- Projection `F2 = {C -> D}`.

**Check preservation:** `F1 cup F2 = {A -> B, B -> C, C -> D}` which is exactly `F`. So preservation holds.

---

## Checking Dependency Preservation

### Algorithm

```
Input: Decomposition D = {R1, R2, ..., Rn}, set of FDs F
Output: TRUE if decomposition is dependency-preserving

For each FD X -> Y in F:
    result = X
    for each Ri in D:
        t = (result intersect Ri)+ under F
        result = result union t
    if Y is NOT subset of result:
        return FALSE
return TRUE
```

The algorithm computes the **closure of X with respect to the decomposed schema** without actually reconstructing the full relation.

### Worked Example

`R(A, B, C)` with `F = {A -> B, B -> C}`. Decomposition: `R1(A, B)`, `R2(A, C)`.

**Check `A -> B`:**
- `result = {A}`
- For R1(A,B): `result intersect R1 = {A}`, `A+ = {A,B,C}`, `result = {A,B,C}`
- For R2(A,C): `result intersect R2 = {A,C}`, `(A,C)+ = {A,B,C}`, `result = {A,B,C}`
- Y = {B} subset of result = {A,B,C}. OK.

**Check `B -> C`:**
- `result = {B}`
- For R1(A,B): `result intersect R1 = {B}`, `B+ = {B,C}`, `result = {B,C}`
- For R2(A,C): `result intersect R2 = {C}`, `C+ = {C}`, `result = {B,C}`
- Y = {C} subset of result = {B,C}. OK.

Both FDs are preserved. The decomposition is dependency-preserving.

---

## Example: Non-Dependency-Preserving Decomposition

`R(A, B, C, D)` with `F = {A -> B, A -> C, B -> D}`.
Decomposition: `R1(A, B, C)`, `R2(B, D)`.

**Projections:**
- `F1` (onto R1): From `A+ = {A,B,C,D}`, we get `A -> B`, `A -> C`. `F1 = {A -> B, A -> C}`.
- `F2` (onto R2): `B+ = {B,D}`, so `B -> D`. `F2 = {B -> D}`.

`F1 cup F2 = {A -> B, A -> C, B -> D} = F`. Preserved. Good.

**Now consider a non-preserving case:**

`R(A, B, C)` with `F = {A -> B, B -> C, C -> A}`. Decomposition: `R1(A, B)`, `R2(B, C)`.

**Projections:**
- `F1` (onto R1): `A+ = {A,B,C}`, so `A -> B`. `B+ = {B,A,C}` (since B -> C -> A), so `B -> A`. `F1 = {A -> B, B -> A}`.
- `F2` (onto R2): `B+ = {B,C,A}`, so `B -> C`. `C+ = {C,A,B}`, so `C -> B`. `F2 = {B -> C, C -> B}`.

`F1 cup F2` implies all FDs in F. Preserved.

**Non-preserving example:**

`R(A, B, C)` with `F = {A -> B, C -> B}`. Decomposition: `R1(A, B)`, `R2(A, C)`.

Wait, `C -> B` is interesting. Let's check:

- `F1` (onto R1(A,B)): `A+ = {A,B}`, so `A -> B`. `B+ = {B}`. `F1 = {A -> B}`.
- `F2` (onto R2(A,C)): `A+ = {A,B}`, `C+ = {C,B}`. Only attributes in R2 are A and C. From `A+`, we get no new FDs with only A,C. From `C+`, we get `C -> ...` nothing in R2 (B is not in R2). So `F2` has no non-trivial FDs.

**Now check `C -> B`:**
- `result = {C}`
- For R1(A,B): `result intersect R1 = {}`, `empty+ = {}`, result stays {C}.
- For R2(A,C): `result intersect R2 = {C}`, `C+ = {C,B}`, `result = {C,B}`.
- Y = {B} subset of result = {C,B}. OK!

Wait, it IS preserved! Let me think again...

Actually, the algorithm says YES, it is preserved. But let me think about this differently. Can we enforce `C -> B` without a join?

In R2(A,C), we can compute the projection of C+ onto R2's attributes. But we need to enforce C -> B. In R1(A,B), B exists but C does not. In R2(A,C), C exists but B does not. So no single relation contains both C and B together.

Hmm, the algorithm gave us YES because:
1. Start result = {C}
2. Process R1(A,B): result intersect R1 = {}. No change.
3. Process R2(A,C): result intersect R2 = {C}. C+ = {C,B}. result = {C,B}.
4. Y = {B} is in result. So yes.

But this doesn't mean we can enforce C -> B without a join -- the algorithm checks whether the closure can be computed using the decomposed relations. It says yes because:
- From C (in R2) we can use the FD C -> B to get B, but wait, B is not in R2... 

The algorithm works by iteratively expanding the result set using attribute closures. The point is: the FD C -> B is known in the original F. When we have C as an attribute value, we know B must be a specific value. But if C and B are never in the same relation, how do we enforce this?

Actually, looking at this more carefully: `C -> B` would be preserved if, for every value of C, there is a unique value of B. This is a constraint on the data. If C and B are never in the same table, the DBMS cannot automatically enforce this constraint through a CHECK or UNIQUE constraint -- it would need a trigger or application-level enforcement.

But the formal definition says: a decomposition is dependency-preserving if `(F1 cup F2 cup ... cup Fn)+ = F+`. In our case:
- F = {A -> B, C -> B}
- F1 = {A -> B}
- F2 = {} (no non-trivial FDs on {A, C})
- (F1 cup F2)+ = {A -> B}+ which does NOT include C -> B.
- So this is NOT dependency-preserving!

Let me redo the algorithm more carefully. The standard algorithm checks if the closure of each FD's left side under the decomposed schema gives the right side. Let me re-examine:

The algorithm is: for each X -> Y in F, compute closure of X using the "decomposed" closure algorithm:
1. result = X
2. For each Ri, compute (result intersect Ri)+ under F, add to result
3. Repeat until stable
4. Check if Y subset of result

For X = C, Y = B:
1. result = {C}
2. R1(A,B): result intersect R1 = {}. empty+ = {}. result = {C}
3. R2(A,C): result intersect R2 = {C}. C+ = {C,B}. result = {C,B}
4. Now check again: R1(A,B): result intersect R1 = {B}. B+ = {B}. result = {C,B}. No change.
5. B is in result. Algorithm says PRESERVED.

But (F1 cup F2)+ does not include C -> B! The issue is that the algorithm I described is actually for checking whether we can test FDs efficiently using the decomposed schema. The standard dependency preservation check is:

**Definition:** Decomposition is dependency-preserving iff for every FD X -> Y in F, Y is contained in the closure of X computed using only the projected FDs.

The algorithm I provided above (by checking closure under F, not under projected FDs) is actually incorrect for a strict check. Let me correct:

**Correct dependency preservation algorithm:**
1. Compute Fi = projection of F onto each Ri
2. Check if (F1 cup F2 cup ... cup Fn)+ = F+

For our example:
- F1 = {A -> B} (projection onto {A,B})
- F2 = {} (projection onto {A,C} -- since C -> B has B not in {A,C}, and A -> B has B not in {A,C})
- (F1 cup F2)+ = {A -> B}+ does NOT contain C -> B
- So NOT dependency-preserving.

**Alternative algorithm (testing without computing all Fi):**
For each X -> Y in F:
1. result = X
2. while (result changes) do
     for each Ri in D:
       let t = (result intersect Ri)+ under F
       result = result union t
3. If Y not subset of result, return FALSE

This algorithm checks if each FD can be verified by examining one relation at a time. If it returns TRUE, we don't need a join to check the FD.

For C -> B: result starts as {C}. Process R1: intersect is empty. Process R2: intersect is {C}, C+ = {C,B}. result = {C,B}. B is in result. Algorithm says YES -- we can verify C -> B by just looking at R2? But B isn't even in R2!

The discrepancy is because this algorithm computes closure under the ORIGINAL F, not the projected F. The correct way to think about it: the algorithm checks whether we can compute the closure of X using the decomposed relations, leveraging the fact that each Ri gives us access to the attributes and FDs on those attributes.

In practice, the correct check is:
- Compute projection of F onto each Ri.
- If the union of these projections covers all FDs in F, then dependency-preserving.

For our example: Fi projections don't give us C -> B back. So it's not dependency-preserving.

---

## Importance of Dependency Preservation

| Preserved | Not Preserved |
|-----------|---------------|
| All FDs can be checked on individual relations | Some FDs require joining relations to check |
| Updates are efficient | Updates are expensive (require joins) |
| Data integrity is easy to maintain | Data integrity may degrade performance |

---

## Practice Problems

1. `R(A, B, C)` with `F = {AB -> C, C -> A}`. Decomposition: `R1(A, C)`, `R2(B, C)`. Is this dependency-preserving?

2. `R(A, B, C, D)` with `F = {A -> B, B -> C, C -> D}`. Decomposition: `R1(A, B)`, `R2(B, C)`, `R3(C, D)`. Is this dependency-preserving?

3. What does it mean for a decomposition to be non-dependency-preserving?

4. Explain the algorithm for projecting FDs onto a relation.

5. For the BCNF decomposition of `R(A, B, C)` with `F = {AB -> C, C -> B}`, is the decomposition dependency-preserving? (Decompose first, then check.)

**Answers:**
1. F1 (to R1(A,C)): A+ = {A,C} -> A -> C. C+ = {A,C} -> C -> A. F1 = {A -> C, C -> A}. F2 (to R2(B,C)): C+ = {A,C}. Nothing with only B,C. B+ = {B}. So F2 = {}. Union = {A -> C, C -> A}. Original F = {AB -> C, C -> A}. AB -> C is not implied by {A -> C, C -> A}. NOT dependency-preserving.

2. F1 = {A -> B}, F2 = {B -> C}, F3 = {C -> D}. Union = {A -> B, B -> C, C -> D} = F. YES.

3. A non-dependency-preserving decomposition means that some FDs from the original schema cannot be enforced on the individual decomposed relations without performing a join. The DBMS would need to join the relations to check the FD, which is expensive.

4. For each subset X of attributes in Ri, compute X+ under F. For each attribute A in Ri such that A is in X+ - X, add X -> A. Then minimize.

5. Candidate keys: (A,B), (A,C). Violating FD for BCNF: C -> B. Decompose: R1(A,C), R2(B,C).
   Check preservation: F1 = {C -> A, A -> C} (projection onto R1).
   F2 = {} (C -> B has B in R2 but C -> B is in F. Wait: projection onto R2(B,C): C+ = {C,A,B}. C -> B. Yes! So F2 = {C -> B}).
   Wait: B and C are both in R2. So C -> B is directly in R2. F2 = {C -> B}.
   Union = {C -> A, A -> C, C -> B}. Does this imply AB -> C?
   From A -> C and B (which we have), yes: AB -> C. Since we have A -> C, AB -> C is implied. So YES, dependency-preserving.
   Wait, AB -> C: A -> C means if we know A, we know C. Augment with B: AB -> BC. Decompose: AB -> C. Yes, it's implied. So preserving.
