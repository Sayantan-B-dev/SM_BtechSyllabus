# Normal Forms (1NF - 3NF)

**Course:** Database Management Systems  
**Module:** 2 | **Lecture:** 10  
**Date:** 20-Aug-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## What is Normalization?

Normalization is the process of organizing data in a database to reduce redundancy and avoid anomalies (insertion, update, deletion anomalies). It involves decomposing tables into smaller, well-structured tables based on functional dependencies.

### Types of Anomalies

| Anomaly | Description | Example |
|---------|-------------|---------|
| **Insertion** | Cannot insert data because of unrelated missing data | Cannot add a department if it has no employees |
| **Update** | Changing data in one place requires changes in many places | Updating a department name requires updating every employee row |
| **Deletion** | Deleting one fact accidentally deletes another | Deleting the last employee in a department deletes the department info |

---

## First Normal Form (1NF)

**Definition:** A relation is in 1NF if all attributes have **atomic values** (no multi-valued attributes or repeating groups).

**Characteristics:**
- Each cell contains a single value (not a set, list, or nested relation)
- All entries in a column are of the same type
- Each row is unique (may require a composite key)

### Violation Example (0NF)

| StudentID | Name | Courses |
|-----------|------|---------|
| 101 | Alice | CS101, CS201 |
| 102 | Bob | CS101 |
| 103 | Charlie | CS201, CS301, CS401 |

Here, `Courses` is multi-valued. This violates 1NF.

### Converting to 1NF

**Method:** Flatten the table so each course gets its own row.

| StudentID | Name | Course |
|-----------|------|--------|
| 101 | Alice | CS101 |
| 101 | Alice | CS201 |
| 102 | Bob | CS101 |
| 103 | Charlie | CS201 |
| 103 | Charlie | CS301 |
| 103 | Charlie | CS401 |

Now the relation is in 1NF. However, it has redundancy (Alice's name repeats for each course).

### Another 1NF Example

**Violation:** Table with repeating group columns:

| EmpID | Name | Project1 | Project2 | Project3 |
|-------|------|----------|----------|----------|
| 101 | Alice | P1 | P2 | NULL |

**Convert to 1NF:**

| EmpID | Name | Project |
|-------|------|---------|
| 101 | Alice | P1 |
| 101 | Alice | P2 |

---

## Second Normal Form (2NF)

**Definition:** A relation is in 2NF if:
1. It is in 1NF, AND
2. **No partial dependency** -- no non-prime attribute is functionally dependent on a **proper subset** of any candidate key.

**Partial dependency:** Occurs when a non-prime attribute depends on only part of a composite candidate key.

### Violation Example

Consider `ENROLLMENT(StudentID, CourseID, InstructorName, Grade)` with FDs:
- `StudentID, CourseID -> Grade` (full key determines grade)
- `CourseID -> InstructorName` (partial dependency: InstructorName depends only on CourseID)

Candidate key: `(StudentID, CourseID)`
Non-prime attributes: `InstructorName`, `Grade`

**Problem:** `CourseID -> InstructorName` is a partial dependency because `CourseID` is a proper subset of the candidate key.

### Converting to 2NF

**Step 1:** Remove the partial dependency by decomposition.

**Relation 1:** `ENROLLMENT(StudentID, CourseID, Grade)` -- key: `(StudentID, CourseID)`

**Relation 2:** `COURSE(CourseID, InstructorName)` -- key: `CourseID`

Now:
- `ENROLLMENT` has FD `StudentID, CourseID -> Grade` (full key dependency, OK)
- `COURSE` has FD `CourseID -> InstructorName` (key determines non-key, OK)

Both are in 2NF.

---

## Third Normal Form (3NF)

**Definition:** A relation is in 3NF if:
1. It is in 2NF, AND
2. **No transitive dependency** -- no non-prime attribute is functionally dependent on another non-prime attribute (i.e., non-key attribute determines another non-key attribute).

**Transitive dependency:** If `X -> Y` and `Y -> Z` where Y is not a key and Z is non-prime, then `Z` is transitively dependent on `X`.

### Violation Example

`EMP_DEPT(EmpID, Name, DeptID, DeptLocation)` with FDs:
- `EmpID -> Name, DeptID` (key determines everything)
- `DeptID -> DeptLocation` (non-key determines non-key -- transitive)

Candidate key: `EmpID`
Non-prime attributes: `Name`, `DeptID`, `DeptLocation`

**Problem:** `EmpID -> DeptID -> DeptLocation` creates a transitive dependency. If a department moves, we must update every employee in that department.

### Converting to 3NF

**Step 1:** Remove the transitive dependency by decomposition.

**Relation 1:** `EMPLOYEE(EmpID, Name, DeptID)` -- key: `EmpID`

**Relation 2:** `DEPARTMENT(DeptID, DeptLocation)` -- key: `DeptID`

Now:
- `EMPLOYEE` has FDs: `EmpID -> Name, DeptID` (OK)
- `DEPARTMENT` has FD: `DeptID -> DeptLocation` (OK)

Both are in 3NF.

---

## Step-by-Step Normalization: 0NF to 3NF

### Initial Table (0NF)

| OrderID | CustomerName | CustomerPhone | Items |
|---------|-------------|---------------|-------|
| 1001 | Alice | 555-0101 | {Laptop, Mouse} |
| 1002 | Bob | 555-0102 | {Keyboard} |
| 1003 | Alice | 555-0101 | {Monitor, USB Cable} |

### Step 1: Convert to 1NF

Flatten the multi-valued Items column:

| OrderID | CustomerName | CustomerPhone | Item |
|---------|-------------|---------------|------|
| 1001 | Alice | 555-0101 | Laptop |
| 1001 | Alice | 555-0101 | Mouse |
| 1002 | Bob | 555-0102 | Keyboard |
| 1003 | Alice | 555-0101 | Monitor |
| 1003 | Alice | 555-0101 | USB Cable |

Candidate key: `(OrderID, Item)`

### Step 2: Identify FDs

- `OrderID -> CustomerName, CustomerPhone` (each order has one customer)
- `CustomerName -> CustomerPhone` (each customer has one phone)

### Step 3: Convert to 2NF

Remove partial dependencies. The FD `OrderID -> CustomerName, CustomerPhone` is a partial dependency since `OrderID` is part of the key.

**Relation 1:** `ORDER_ITEM(OrderID, Item)` -- key: `(OrderID, Item)`
**Relation 2:** `ORDER(OrderID, CustomerName)` -- key: `OrderID`

But `CustomerPhone` is still in the mix...

Let me redo this more carefully. Our 1NF table is:

`ORDER_DETAIL(OrderID, CustomerName, CustomerPhone, Item)` with FD:
- `OrderID, Item -> CustomerName, CustomerPhone` (full key)
- Actually `OrderID -> CustomerName, CustomerPhone` (partial)
- `CustomerName -> CustomerPhone`

Candidate key: `(OrderID, Item)`

**Partial dependency:** `OrderID -> CustomerName, CustomerPhone` (since OrderID is part of the key)

**Decompose to 2NF:**

**Relation A:** `ORDER_ITEM(OrderID, Item)` -- key: `(OrderID, Item)`
**Relation B:** `ORDER(OrderID, CustomerName, CustomerPhone)` -- key: `OrderID`

Now check Relation B: is it in 2NF? Key is `OrderID` (single attribute), so no partial dependencies possible. Yes, 2NF.

### Step 4: Convert to 3NF

Check Relation B (`ORDER`) for transitive dependency:
- `OrderID -> CustomerName`
- `CustomerName -> CustomerPhone` (transitive!)

**Decompose to 3NF:**

**Relation B1:** `ORDER(OrderID, CustomerName)` -- key: `OrderID`
**Relation B2:** `CUSTOMER(CustomerName, CustomerPhone)` -- key: `CustomerName`

**Final 3NF Schema:**
1. `ORDER_ITEM(OrderID, Item)` -- key: `(OrderID, Item)`
2. `ORDER(OrderID, CustomerName)` -- key: `OrderID`
3. `CUSTOMER(CustomerName, CustomerPhone)` -- key: `CustomerName`

---

## Summary

| Normal Form | Condition | How to Fix |
|-------------|-----------|------------|
| **1NF** | Atomic values, no repeating groups | Flatten repeating groups into separate rows |
| **2NF** | 1NF + no partial dependency | Decompose to separate tables for each part of the key |
| **3NF** | 2NF + no transitive dependency | Decompose to separate tables when a non-key determines another non-key |

---

## Practice Problems

1. Is the following relation in 1NF? If not, convert it.

| Student | Subjects |
|---------|----------|
| Ram | Math, Physics |
| Shyam | Chemistry |

2. Consider `R(A, B, C, D)` with FDs `{AB -> C, B -> D}` and candidate key `{A, B}`. Is R in 2NF?

3. Consider `R(A, B, C, D)` with FD `{A -> B, B -> C}` and candidate key `{A}`. Is R in 3NF?

4. Normalize the following to 3NF: `SALES(InvoiceNo, CustomerName, ProductName, Quantity, CustomerCity)` with FDs: `InvoiceNo -> CustomerName, CustomerCity` and `CustomerName -> CustomerCity`.

5. Explain the difference between partial dependency and transitive dependency.

**Answers:**
1. No (Subjects is multi-valued). Convert by flattening: `(Ram, Math), (Ram, Physics), (Shyam, Chemistry)`.

2. No. `B -> D` is a partial dependency (B is a proper subset of the candidate key AB, and D is non-prime). Decompose: `R1(A, B, C)` and `R2(B, D)`.

3. Check FDs: `A -> B` (key -> non-key, OK), `B -> C` (non-key -> non-key, transitive). Not in 3NF. Decompose: `R1(A, B)` and `R2(B, C)`.

4. 1NF: Already atomic. Key: `InvoiceNo, ProductName`. 2NF: Remove partial dependency `InvoiceNo -> CustomerName, CustomerCity`. Get `SALE(InvoiceNo, ProductName, Quantity)` and `INVOICE(InvoiceNo, CustomerName, CustomerCity)`. 3NF: Remove transitive dependency `CustomerName -> CustomerCity` from INVOICE. Get `INVOICE(InvoiceNo, CustomerName)` and `CUSTOMER(CustomerName, CustomerCity)`.

5. **Partial dependency:** A non-key attribute depends on only part of a composite key (e.g., `CourseID -> Instructor` when the key is `(StudentID, CourseID)`). **Transitive dependency:** A non-key attribute depends on another non-key attribute (e.g., `EmpID -> DeptID` and `DeptID -> Location`, so Location is transitively dependent on EmpID).
