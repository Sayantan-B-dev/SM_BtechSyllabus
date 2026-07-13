# Relational Algebra (Basics)

**Course:** Database Management Systems  
**Module:** 2 | **Lecture:** 1  
**Date:** 30-Jul-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## What is Relational Algebra?

Relational algebra is a **procedural query language** for the relational model. It describes *how* to retrieve data by specifying a sequence of operations on relations (tables). The output of every operation is another relation -- this property is called **closure**.

Relational algebra forms the theoretical foundation for SQL. Every SQL query can be translated into an equivalent relational algebra expression.

---

## Basic Operations

There are five basic operations in relational algebra:

| Operation | Symbol | Purpose |
|-----------|--------|---------|
| Select | `sigma` | Choose rows (horizontal subset) |
| Project | `pi` | Choose columns (vertical subset) |
| Rename | `rho` | Rename a relation or its attributes |
| Union | `cup` | Combine tuples from two relations |
| Set Difference | `-` | Tuples in one relation but not another |
| Cartesian Product | `times` | Combine every tuple of one with every tuple of another |

This lecture covers **SELECT, PROJECT, and RENAME**. The set operations and joins are covered in L02.

---

## SELECT Operation (`sigma`)

The SELECT operation selects **rows** (tuples) that satisfy a given predicate.

**Notation:** `sigma_condition(Relation)`

**Example:** Given an `EMPLOYEE` table:

| EmpID | Name | Dept | Salary |
|-------|------|------|--------|
| 101 | Alice | IT | 60000 |
| 102 | Bob | HR | 45000 |
| 103 | Charlie | IT | 55000 |
| 104 | Diana | Finance | 70000 |

Find all employees in the IT department:

`sigma_Dept = 'IT'(EMPLOYEE)`

Result:

| EmpID | Name | Dept | Salary |
|-------|------|------|--------|
| 101 | Alice | IT | 60000 |
| 103 | Charlie | IT | 55000 |

Find employees with salary > 50000:

`sigma_Salary > 50000(EMPLOYEE)`

Result:

| EmpID | Name | Dept | Salary |
|-------|------|------|--------|
| 101 | Alice | IT | 60000 |
| 103 | Charlie | IT | 55000 |
| 104 | Diana | Finance | 70000 |

**Compound conditions** use logical connectives AND (^), OR (v), NOT (~):

`sigma_Dept = 'IT' ^ Salary > 50000(EMPLOYEE)`

Result:

| EmpID | Name | Dept | Salary |
|-------|------|------|--------|
| 101 | Alice | IT | 60000 |
| 103 | Charlie | IT | 55000 |

**Properties of SELECT:**
- Commutative: `sigma_c1(sigma_c2(R)) = sigma_c2(sigma_c1(R))`
- Cascading: `sigma_c1 AND c2(R) = sigma_c1(sigma_c2(R))`
- SELECT size is always <= original relation size (monotonic reduction)

---

## PROJECT Operation (`pi`)

The PROJECT operation selects **columns** (attributes) from a relation.

**Notation:** `pi_A1, A2, ..., An(Relation)`

**Example:** Get only the Name and Salary of all employees:

`pi_Name, Salary(EMPLOYEE)`

Result:

| Name | Salary |
|------|--------|
| Alice | 60000 |
| Bob | 45000 |
| Charlie | 55000 |
| Diana | 70000 |

**Duplicate elimination:** By default, PROJECT removes duplicate tuples. If two employees have the same name and salary, only one row appears.

Get distinct departments:

`pi_Dept(EMPLOYEE)`

Result:

| Dept |
|------|
| IT |
| HR |
| Finance |

**Properties of PROJECT:**
- The number of tuples in `pi` projection is <= number in original (due to duplicate elimination)
- `pi` is not commutative: `pi_A(pi_B(R))` is valid only if A is subset of B

---

## Combining SELECT and PROJECT

We can compose operations. Find the **names of employees in IT**:

`pi_Name(sigma_Dept = 'IT'(EMPLOYEE))`

Step 1: `sigma_Dept = 'IT'(EMPLOYEE)` gives:

| EmpID | Name | Dept | Salary |
|-------|------|------|--------|
| 101 | Alice | IT | 60000 |
| 103 | Charlie | IT | 55000 |

Step 2: `pi_Name` on the above gives:

| Name |
|------|
| Alice |
| Charlie |

---

## RENAME Operation (`rho`)

The RENAME operation gives a name to the result of an expression. It is essential for self-joins and complex queries.

**Notation:** `rho_S(B1, B2, ..., Bn)(R)` renames relation R to S and its attributes to B1, B2, ..., Bn.

**Examples:**

1. Rename only the relation: `rho_IT_Dept(sigma_Dept = 'IT'(EMPLOYEE))`

2. Rename relation and attributes: `rho_E2(ID, Name, Dept, Salary)(EMPLOYEE)` creates a copy named E2 with attribute names ID, Name, Dept, Salary.

3. Rename using assignment: `Temp = sigma_Salary > 50000(EMPLOYEE)` This assigns the result to a temporary relation name.

---

## Worked Example

**Problem:** Consider `STUDENT(RollNo, Name, Age, Major)`. Find the names of students who are older than 20 and majoring in CS.

**Solution:**
1. Select rows: `sigma_Age > 20 AND Major = 'CS'(STUDENT)`
2. Project names: `pi_Name(sigma_Age > 20 AND Major = 'CS'(STUDENT))`

**Sample Data:**

| RollNo | Name | Age | Major |
|--------|------|-----|-------|
| 1 | Ram | 21 | CS |
| 2 | Shyam | 19 | Math |
| 3 | Sita | 22 | CS |
| 4 | Gita | 20 | Physics |

Step 1: `sigma_Age > 20 AND Major = 'CS'(STUDENT)`

| RollNo | Name | Age | Major |
|--------|------|-----|-------|
| 1 | Ram | 21 | CS |
| 3 | Sita | 22 | CS |

Step 2: `pi_Name` gives:

| Name |
|------|
| Ram |
| Sita |

---

## Summary Table

| Operation | Symbol | Effect | Unary/Binary |
|-----------|--------|--------|--------------|
| SELECT | `sigma` | Horizontal subset (rows) | Unary |
| PROJECT | `pi` | Vertical subset (columns) | Unary |
| RENAME | `rho` | Rename relation/attributes | Unary |

---

## Practice Problems

1. Given `PRODUCT(ProdID, Name, Price, Category)`, write a relational algebra expression to find the names of all products in the 'Electronics' category with a price less than 500.

2. Given `EMP(EmpID, Name, Dept, Salary, City)`, write RA to find the employee IDs and names of employees who work in 'Sales' OR earn more than 80000.

3. What is the difference between SELECT and PROJECT in relational algebra?

4. Show that SELECT is commutative: `sigma_c1(sigma_c2(R)) = sigma_c2(sigma_c1(R))` with a brief explanation.

5. Given `R(A, B, C)` with tuples `(1,2,3), (1,2,4), (2,3,4)`, what does `pi_A,B(R)` return?

**Answers:**
1. `pi_Name(sigma_Category = 'Electronics' AND Price < 500(PRODUCT))`
2. `pi_EmpID, Name(sigma_Dept = 'Sales' OR Salary > 80000(EMP))`
3. SELECT picks rows (horizontal subset) using a condition; PROJECT picks columns (vertical subset) and removes duplicates.
4. Both orderings produce the same set of tuples satisfying both c1 and c2 because AND is commutative.
5. `(1,2), (2,3)` -- note that tuples `(1,2,3)` and `(1,2,4)` collapse to `(1,2)` once after projection, and `(2,3,4)` gives `(2,3)`.
