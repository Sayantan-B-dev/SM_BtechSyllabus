# Relational Algebra (Advanced Operations)

**Course:** Database Management Systems  
**Module:** 2 | **Lecture:** 2  
**Date:** 30-Jul-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## Set Operations

Set operations combine tuples from two relations. Both relations must be **union-compatible**: they must have the same number of attributes, and corresponding attributes must have the same domain.

### Union (`cup`)

**Notation:** `R cup S`

Returns all tuples that appear in R or S (or both). Duplicates are eliminated.

**Example:**

`IT_EMP(EmpID, Name)` and `HR_EMP(EmpID, Name)`:

```
IT_EMP:
EmpID | Name
101   | Alice
103   | Charlie

HR_EMP:
EmpID | Name
102   | Bob
104   | Diana
```

`IT_EMP cup HR_EMP`:

```
EmpID | Name
101   | Alice
102   | Bob
103   | Charlie
104   | Diana
```

### Set Difference (`-`)

**Notation:** `R - S`

Returns all tuples that appear in R but NOT in S.

`IT_EMP - HR_EMP`:

```
EmpID | Name
101   | Alice
103   | Charlie
```

### Intersection (`cap`)

**Notation:** `R cap S`

Returns all tuples that appear in both R and S.

`cap` can be expressed using difference: `R cap S = R - (R - S)`

**Example:**

If `MANAGERS(EmpID, Name)` contains `(101, Alice), (102, Bob)`, then `IT_EMP cap MANAGERS` returns `(101, Alice)`.

---

## Cartesian Product (`times`)

**Notation:** `R times S`

Combines EVERY tuple from R with EVERY tuple from S. If R has `m` tuples and S has `n` tuples, the result has `m * n` tuples.

**Example:**

`EMPLOYEE(EmpID, Name, DeptID)`:

| EmpID | Name | DeptID |
|-------|------|--------|
| 101 | Alice | D1 |
| 102 | Bob | D2 |

`DEPARTMENT(DeptID, DName)`:

| DeptID | DName |
|--------|-------|
| D1 | IT |
| D2 | HR |

`EMPLOYEE times DEPARTMENT`:

| EmpID | Name | DeptID | DeptID | DName |
|-------|------|--------|--------|-------|
| 101 | Alice | D1 | D1 | IT |
| 101 | Alice | D1 | D2 | HR |
| 102 | Bob | D2 | D1 | IT |
| 102 | Bob | D2 | D2 | HR |

Notice that `times` alone produces many meaningless combinations. We usually follow it with a SELECT to keep only matching rows.

---

## Join Operations

A join combines a Cartesian product with a selection condition.

### Theta Join (`bowtie_theta`)

**Notation:** `R bowtie_theta S`

Performs `sigma_theta(R times S)`. The condition `theta` is any comparison predicate.

`EMPLOYEE bowtie_EMP.DeptID = DEPT.DeptID DEPARTMENT`:

| EmpID | Name | DeptID | DeptID | DName |
|-------|------|--------|--------|-------|
| 101 | Alice | D1 | D1 | IT |
| 102 | Bob | D2 | D2 | HR |

Only the meaningful combinations (where DeptID matches) survive.

### Equi Join

A theta join where the condition uses only equality (`=`). The result contains both join attributes.

`EMPLOYEE bowtie_EMP.DeptID = DEPT.DeptID DEPARTMENT` (same as above) is an equi join.

### Natural Join (`bowtie`)

**Notation:** `R bowtie S`

An equi join that **eliminates duplicate join attributes**. The join condition is implicitly equality on all attributes with the same name.

`EMPLOYEE bowtie DEPARTMENT` (assuming both have `DeptID`):

| EmpID | Name | DeptID | DName |
|-------|------|--------|-------|
| 101 | Alice | D1 | IT |
| 102 | Bob | D2 | HR |

Note: `DeptID` appears only once (unlike theta/equi join).

If the two relations share NO common attribute names, natural join degenerates to Cartesian product.

---

## Worked Examples

### Example 1: Combining Employee and Department

`EMPLOYEE(EmpID, Name, DeptID, Salary)` and `DEPT(DeptID, DName, Location)`:

**Query:** Find names of employees working in the 'IT' department located in 'New York'.

**Step-by-step RA:**

1. Natural join: `EMPLOYEE bowtie DEPT`
2. Select: `sigma_DName = 'IT' AND Location = 'New York'(EMPLOYEE bowtie DEPT)`
3. Project: `pi_Name(sigma_DName = 'IT' AND Location = 'New York'(EMPLOYEE bowtie DEPT))`

### Example 2: Using Set Operations

**Query:** Find employees who work in both the IT and HR departments (intersection of employees in each dept).

This requires more work since an employee can belong to only one department in the basic schema. A more realistic example:

`SKILLS(EmpID, Skill)`:

| EmpID | Skill |
|-------|-------|
| 101 | Java |
| 101 | Python |
| 102 | Java |
| 103 | SQL |

**Query:** EmpIDs who have both Java AND Python skills.

`rho_JAVA(SkillMap) = pi_EmpID(sigma_Skill='Java'(SKILLS))`
`rho_PYTHON(SkillMap) = pi_EmpID(sigma_Skill='Python'(SKILLS))`
Result: `JAVA cap PYTHON` returns `(101)`.

---

## Summary of Join Types

| Join Type | Notation | Condition | Duplicate Attributes |
|-----------|----------|-----------|---------------------|
| Theta Join | `R bowtie_theta S` | Any condition `theta` | Kept |
| Equi Join | `R bowtie_eq S` | Equality only | Kept |
| Natural Join | `R bowtie S` | Equality on same-named attrs | Removed |

---

## Practice Problems

1. Given `STUDENT(SID, SName, Major)` and `ENROLLED(SID, CID, Grade)`, write RA to find names of students enrolled in course 'CS101'.
<details>
<summary>Show Answer</summary>
`pi_SName(STUDENT bowtie sigma_CID = 'CS101'(ENROLLED))`
</details>

2. Find the names of students enrolled in ALL courses offered -- explain why the division operator would be needed.
<details>
<summary>Show Answer</summary>
This requires division (`÷`) : `pi_SID,CID(ENROLLED) ÷ pi_CID(Courses)`. Division is covered in advanced topics.
</details>

3. Given `R(A,B) = {(1,2), (3,4)}` and `S(B,C) = {(2,5), (6,7)}`, compute `R bowtie S` (natural join).
<details>
<summary>Show Answer</summary>
Only `(1,2,5)` because the only matching B value is 2.
</details>

4. Express intersection using only union and set difference.
<details>
<summary>Show Answer</summary>
`R cap S = R - (R - S)`
</details>

5. Why must relations be union-compatible for `cup` and `-`?
<details>
<summary>Show Answer</summary>
The result must be a relation with a fixed schema. Without union-compatibility, the result would not have a well-defined set of attributes.
</details>

