# BCNF, 4NF, 5NF, 6NF

**Course:** Database Management Systems  
**Module:** 2 | **Lecture:** 11  
**Date:** 20-Aug-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## Boyce-Codd Normal Form (BCNF)

**Definition:** A relation `R` is in BCNF if for every non-trivial FD `X -> Y` that holds in `R`:
- `X` is a **superkey** of `R`.

BCNF is a stricter version of 3NF. Every BCNF relation is in 3NF, but not vice versa.

### BCNF vs 3NF

| Aspect | 3NF | BCNF |
|--------|-----|------|
| Condition | For every FD `X -> Y`, either X is a superkey OR Y is prime | For every FD `X -> Y`, X must be a superkey |
| Allows non-key -> key? | Yes (if RHS attributes are prime) | No |
| Redundancy | May have some redundancy | Minimal redundancy |
| Dependency preservation | Always possible | May lose some FDs |

### BCNF Violation Example

Consider `STUDENT_COURSE(StudentID, CourseID, Instructor)` with FDs:
- `StudentID, CourseID -> Instructor` (key)
- `CourseID -> Instructor` (each course has one instructor)

Candidate key: `(StudentID, CourseID)`

**Check BCNF:** Is `CourseID -> Instructor` violating BCNF?
- `CourseID` is NOT a superkey (CourseID+ = {CourseID, Instructor}, missing StudentID)
- So this violates BCNF.

Is it in 3NF? `Instructor` is non-prime (not part of any candidate key). Since `CourseID -> Instructor` has non-prime RHS and `CourseID` is not a superkey, 3NF also requires the LHS to be a superkey. So 3NF is also violated? Let me check more carefully.

Wait, let's find candidate keys. The only candidate key is `(StudentID, CourseID)`. `Instructor` is non-prime. `CourseID` is not a superkey. So `CourseID -> Instructor` violates both 3NF and BCNF.

Actually, the 3NF condition: For every FD `X -> Y`, either (a) X is a superkey, or (b) each attribute in Y is prime (part of some candidate key). Since `Instructor` is non-prime, condition (b) fails. And `CourseID` is not a superkey. So this violates both 3NF and BCNF.

Let me use a classic example where BCNF is violated but 3NF is satisfied:

`R(A, B, C)` with FDs: `{AB -> C, C -> B}`.
- Candidate keys: `{A, B}` (AB+ = {A,B,C}) and `{A, C}` (AC+ = {A,C,B})
- Prime attributes: `{A, B, C}` (all attributes are prime!)
- Check 3NF: For `C -> B`, X = C (not a superkey? C+ = {C,B}. Missing A. So C is not a superkey). Y = B (B is prime -- it's part of candidate key AB). So condition (b) of 3NF holds. OK for 3NF.
- Check BCNF: For `C -> B`, X must be a superkey. C is not a superkey. Violation!

So this is a relation in 3NF but not BCNF.

### BCNF Decomposition Algorithm

```
result = {R}
while there is a schema Ri in result not in BCNF do
    let X -> Y be a violating FD in Ri
    result = (result - Ri) union (Ri - Y) union (X, Y)
```

**Example:** Decompose `STUDENT_COURSE(StudentID, CourseID, Instructor)`.

Violating FD: `CourseID -> Instructor`

1. Create `R1 = (CourseID, Instructor)` -- key: `CourseID`
2. Create `R2 = (StudentID, CourseID)` -- key: `(StudentID, CourseID)`
   - But does R2 have any FDs? Only trivial ones. So it's in BCNF.

Final decomposition:
- `R1(CourseID, Instructor)` -- BCNF
- `R2(StudentID, CourseID)` -- BCNF

**Note:** The original FD `(StudentID, CourseID) -> Instructor` is lost (cannot be enforced without a join). This is a **non-dependency-preserving** decomposition.

---

## Fourth Normal Form (4NF)

**Definition:** A relation is in 4NF if:
1. It is in BCNF, AND
2. There are no **non-trivial multivalued dependencies (MVDs)** except those that are also functional dependencies.

### Multivalued Dependency (MVD)

**Notation:** `X ->> Y` (read as "X multidetermines Y")

An MVD means: for every pair of tuples with the same X values, the set of Y values associated with each X value is independent of all other attributes.

**Formal Definition:** `X ->> Y` holds if for every pair of tuples `t1`, `t2` with `t1[X] = t2[X]`, there exist tuples `t3`, `t4` such that:
- `t3[X] = t1[X]`, `t3[Y] = t1[Y]`, `t3[R-X-Y] = t2[R-X-Y]`
- `t4[X] = t1[X]`, `t4[Y] = t2[Y]`, `t4[R-X-Y] = t1[R-X-Y]`

If `X ->> Y`, then the set of Y values for a given X is independent of the values of other attributes.

### MVD Example

`EMP_SKILL_LANG(EmpName, Skill, Language)`:

| EmpName | Skill | Language |
|---------|-------|----------|
| Alice | Java | English |
| Alice | Python | English |
| Alice | Java | Hindi |
| Alice | Python | Hindi |
| Bob | SQL | English |

Here: `EmpName ->> Skill` and `EmpName ->> Language`. Each employee's skills are independent of their languages.

This table has redundancy (every skill is paired with every language for each employee).

### 4NF Decomposition

Decompose into:
- `EMP_SKILL(EmpName, Skill)`
- `EMP_LANG(EmpName, Language)`

Both are in 4NF (no MVDs other than FD keys).

---

## Fifth Normal Form (5NF)

**Definition:** A relation is in 5NF (also called Project-Join Normal Form, PJNF) if:
1. It is in 4NF, AND
2. Every **join dependency (JD)** in the relation is implied by the candidate keys.

### Join Dependency (JD)

A join dependency `JD(R1, R2, ..., Rn)` means that `R` can be reconstructed as the natural join of its projections onto `R1, R2, ..., Rn`.

**Notation:** `*(R1, R2, ..., Rn)`

Every MVD is a binary join dependency. 5NF generalizes 4NF to handle non-binary decompositions.

### 5NF Violation Example

`AGENT_COMPANY_PRODUCT(AgentName, Company, Product)`:

| Agent | Company | Product |
|-------|---------|---------|
| Alice | ABC Corp | Insurance |
| Alice | XYZ Inc | Mutual Funds |
| Alice | ABC Corp | Mutual Funds |
| Bob | ABC Corp | Insurance |

If the rule is: An agent sells certain products for certain companies, and the relationship is **ternary** (cannot be split into binary without losing information), then this is a join dependency.

However, if the rule is: If Agent X works with Company Y AND Agent X sells Product Z, then Agent X sells Product Z for Company Y -- this is a ternary constraint that would be violated by splitting into binary tables.

A relation in 5NF has no such **lossy** decomposition into three (or more) relations.

---

## Sixth Normal Form (6NF)

**Definition:** A relation is in 6NF if it cannot be decomposed further without losing information.

6NF is relevant for **temporal databases** and **data warehouses**. In 6NF, each non-key attribute is decomposed into its own relation, along with the key.

### Temporal Database Example

`EMP_SALARY(EmpID, Name, Salary, EffectiveFrom, EffectiveTo)`:

In 6NF, we would decompose into:
- `EMP_NAME(EmpID, Name, EffectiveFrom, EffectiveTo)`
- `EMP_SALARY(EmpID, Salary, EffectiveFrom, EffectiveTo)`

This allows different attributes to have different temporal validity periods.

6NF is rarely used in practice except for specialized temporal/bitemporal databases.

---

## Summary Table

| Normal Form | Criterion | Violation | Keys Reference |
|-------------|-----------|-----------|----------------|
| **1NF** | Atomic values | Repeating groups | -- |
| **2NF** | No partial dependency | Non-key depends on part of composite key | Korth & Silberschatz Ch. 7 |
| **3NF** | No transitive dependency | Non-key determines non-key | Ch. 7 |
| **BCNF** | Every FD has superkey LHS | Non-key determines anything | Ch. 7 |
| **4NF** | No non-trivial MVDs | MVDs not implied by FDs | Ch. 8 |
| **5NF** | No non-trivial JDs | JD not implied by keys | Ch. 8 |
| **6NF** | Cannot decompose further | Temporal redundancy | Ch. 8 |

---

## Practice Problems

1. Given `R(A, B, C)` with FDs `{AB -> C, C -> B}`, is R in BCNF? Is it in 3NF?
<details>
<summary>Show Answer</summary>
Candidate keys: `{A,B}`, `{A,C}`. All attributes are prime. For `C -> B`: X=C is not a superkey, Y=B is prime. So: 3NF = YES (Y is prime). BCNF = NO (X must be superkey).
</details>

2. Decompose `R(Student, Course, Instructor)` with FDs `{Student, Course -> Instructor, Course -> Instructor}` into BCNF.
<details>
<summary>Show Answer</summary>
`Course -> Instructor` violates BCNF. Decompose: `R1(Course, Instructor)` and `R2(Student, Course)`.
</details>

3. Give an example of a multivalued dependency (MVD) and explain how to normalize to 4NF.
<details>
<summary>Show Answer</summary>
`EMP_SKILL_LANG(EmpName, Skill, Language)` has MVD EmpName ->> Skill. Normalize by splitting: `EMP_SKILL(EmpName, Skill)`, `EMP_LANG(EmpName, Language)`.
</details>

4. What is the difference between an MVD and a JD?
<details>
<summary>Show Answer</summary>
An MVD is a binary join dependency (decomposes into 2 projections). A JD can involve more than 2 projections (ternary or higher).
</details>

5. When would you need 6NF?
<details>
<summary>Show Answer</summary>
6NF is used for temporal databases where different attributes have different time-stamping requirements, allowing each attribute to be tracked independently with its own temporal validity period.
</details>

