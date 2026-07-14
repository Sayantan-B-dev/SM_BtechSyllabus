# SQL3 Advanced Queries

**Course:** Database Management Systems  
**Module:** 2 | **Lecture:** 6  
**Date:** 11-Aug-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## Aggregate Functions

Aggregate functions compute a single value from a set of rows.

| Function | Returns | Example |
|----------|---------|---------|
| `COUNT` | Number of rows | `COUNT(*)` |
| `SUM` | Sum of values | `SUM(Salary)` |
| `AVG` | Average of values | `AVG(Salary)` |
| `MAX` | Maximum value | `MAX(Salary)` |
| `MIN` | Minimum value | `MIN(Salary)` |

**Sample Data -- EMPLOYEE:**

| EmpID | Name | DeptID | Salary |
|-------|------|--------|--------|
| 101 | Alice | D1 | 60000 |
| 102 | Bob | D2 | 45000 |
| 103 | Charlie | D1 | 55000 |
| 104 | Diana | D3 | 70000 |
| 105 | Eve | D1 | 48000 |
| 106 | Frank | D2 | 45000 |

**Examples:**
```sql
SELECT COUNT(*) AS TotalEmployees FROM EMPLOYEE;          -- 6
SELECT COUNT(DISTINCT DeptID) FROM EMPLOYEE;              -- 3
SELECT AVG(Salary) AS AvgSalary FROM EMPLOYEE;            -- 53833.33
SELECT MAX(Salary) AS Highest, MIN(Salary) AS Lowest
FROM EMPLOYEE;                                            -- 70000, 45000
SELECT SUM(Salary) AS TotalPayroll FROM EMPLOYEE;         -- 323000
```

---

## GROUP BY and HAVING

**GROUP BY** groups rows that have the same values in specified columns. Aggregate functions then operate on each group.

**HAVING** filters groups (like WHERE filters rows, but HAVING works after grouping).

```sql
-- Average salary per department
SELECT DeptID, AVG(Salary) AS AvgSalary
FROM EMPLOYEE
GROUP BY DeptID;

-- Result:
-- D1 | 54333.33
-- D2 | 45000.00
-- D3 | 70000.00
```

```sql
-- Departments with average salary > 50000
SELECT DeptID, AVG(Salary) AS AvgSalary
FROM EMPLOYEE
GROUP BY DeptID
HAVING AVG(Salary) > 50000;

-- Result:
-- D1 | 54333.33
-- D3 | 70000.00
```

**Order of execution in SQL:**
1. FROM -- source tables
2. WHERE -- filter rows
3. GROUP BY -- form groups
4. HAVING -- filter groups
5. SELECT -- choose columns
6. ORDER BY -- sort result

**Important:** Any column in SELECT must either be in GROUP BY or be an aggregate function.

---

## NULL Handling

NULL represents **unknown** or **missing** data. Operations with NULL:

```sql
-- Find employees with unknown salary
SELECT * FROM EMPLOYEE WHERE Salary IS NULL;

-- Find employees with known salary
SELECT * FROM EMPLOYEE WHERE Salary IS NOT NULL;

-- Arithmetic with NULL yields NULL
-- NULL + 1000 = NULL
-- NULL > 50000 is UNKNOWN (not TRUE, not FALSE)
```

### Three-Valued Logic

SQL uses three logic values: TRUE, FALSE, UNKNOWN.

| A | B | A AND B | A OR B | NOT A |
|---|---|---------|--------|-------|
| TRUE | UNKNOWN | UNKNOWN | TRUE | FALSE |
| FALSE | UNKNOWN | FALSE | UNKNOWN | TRUE |
| UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |

**Impact on WHERE:** WHERE clause only includes rows where the condition evaluates to TRUE. Rows evaluating to FALSE or UNKNOWN are excluded.

```sql
-- What if some salaries are NULL?
SELECT * FROM EMPLOYEE WHERE Salary > 50000;
-- NULL salaries are NOT included (NULL > 50000 is UNKNOWN)
```

**COALESCE** and **IFNULL** handle NULLs:
```sql
SELECT Name, COALESCE(Salary, 0) AS Salary FROM EMPLOYEE;
-- Replaces NULL salary with 0
```

---

## Set Operations

Set operations combine results from two queries. Both queries must have the same number and types of columns.

### UNION

Combines results, removing duplicates. Use `UNION ALL` to keep duplicates.

```sql
-- Employees from D1 or D2
SELECT EmpID, Name FROM EMPLOYEE WHERE DeptID = 'D1'
UNION
SELECT EmpID, Name FROM EMPLOYEE WHERE DeptID = 'D2';
```

### INTERSECT

Returns rows present in both results.

```sql
-- Employees who are in D1 AND earn > 50000
SELECT EmpID FROM EMPLOYEE WHERE DeptID = 'D1'
INTERSECT
SELECT EmpID FROM EMPLOYEE WHERE Salary > 50000;
```

### EXCEPT (or MINUS)

Returns rows in the first query but not the second.

```sql
-- Employees in D1 who do NOT earn > 55000
SELECT EmpID FROM EMPLOYEE WHERE DeptID = 'D1'
EXCEPT
SELECT EmpID FROM EMPLOYEE WHERE Salary > 55000;
```

---

## Nested Subqueries

Subqueries are queries within queries. They can appear in WHERE, FROM, or SELECT clauses.

### IN / NOT IN

Checks if a value is in the subquery result.

```sql
-- Employees whose department is in New York
SELECT Name FROM EMPLOYEE
WHERE DeptID IN (
    SELECT DeptID FROM DEPARTMENT WHERE Location = 'New York'
);

-- Equivalent to:
SELECT e.Name
FROM EMPLOYEE e, DEPARTMENT d
WHERE e.DeptID = d.DeptID AND d.Location = 'New York';
```

### EXISTS / NOT EXISTS

Checks if the subquery returns any rows.

```sql
-- Departments that have at least one employee
SELECT DName FROM DEPARTMENT d
WHERE EXISTS (
    SELECT * FROM EMPLOYEE e
    WHERE e.DeptID = d.DeptID
);

-- Departments with NO employees
SELECT DName FROM DEPARTMENT d
WHERE NOT EXISTS (
    SELECT * FROM EMPLOYEE e
    WHERE e.DeptID = d.DeptID
);
```

### ANY and ALL

Used with comparison operators.

```sql
-- Employees who earn more than ANY employee in D1
SELECT Name, Salary FROM EMPLOYEE
WHERE Salary > ANY (
    SELECT Salary FROM EMPLOYEE WHERE DeptID = 'D1'
);
-- > ANY means: greater than at least one value from D1 (48000)
-- So: Alice(60000), Charlie(55000), Diana(70000) qualify

-- Employees who earn more than ALL employees in D1
SELECT Name, Salary FROM EMPLOYEE
WHERE Salary > ALL (
    SELECT Salary FROM EMPLOYEE WHERE DeptID = 'D1'
);
-- > ALL means: greater than every value from D1 (60000, 55000, 48000) -> must be > 60000
-- So: Diana(70000) qualifies
```

---

## Correlated Subqueries

A correlated subquery references columns from the outer query and is re-evaluated for each row of the outer query.

```sql
-- Employees who earn more than the average salary in their own department
SELECT e.Name, e.Salary, e.DeptID
FROM EMPLOYEE e
WHERE e.Salary > (
    SELECT AVG(Salary)
    FROM EMPLOYEE
    WHERE DeptID = e.DeptID
);

-- For each employee e, the subquery computes the average salary of e's department
-- Alice(60000) > avg(D1=54333) -> YES
-- Charlie(55000) > avg(D1=54333) -> YES
-- Eve(48000) > avg(D1=54333) -> NO
-- Diana(70000) > avg(D3=70000) -> NO
-- Bob(45000) > avg(D2=45000) -> NO
-- Frank(45000) > avg(D2=45000) -> NO
```

---

## Worked Example: Complex Query

**Scenario:** Find the department name and its highest-paid employee's name.

```sql
SELECT d.DName, e.Name, e.Salary
FROM DEPARTMENT d
JOIN EMPLOYEE e ON e.DeptID = d.DeptID
WHERE e.Salary = (
    SELECT MAX(Salary)
    FROM EMPLOYEE
    WHERE DeptID = d.DeptID
);
```

---

## Practice Problems

1. Write a query to find the number of employees in each department, sorted by count descending.
<details>
<summary>Show Answer</summary>
```sql
SELECT DeptID, COUNT(*) AS EmpCount
FROM EMPLOYEE
GROUP BY DeptID
ORDER BY EmpCount DESC;
```
</details>

2. Find departments where the average salary is above 50000 and at least 2 employees work.
<details>
<summary>Show Answer</summary>
```sql
SELECT DeptID, AVG(Salary) AS AvgSal
FROM EMPLOYEE
GROUP BY DeptID
HAVING AVG(Salary) > 50000 AND COUNT(*) >= 2;
```
</details>

3. Write a query using EXISTS to find employees who belong to a department with budget > 300000.
<details>
<summary>Show Answer</summary>
```sql
SELECT e.Name FROM EMPLOYEE e
WHERE EXISTS (
    SELECT * FROM DEPARTMENT d
    WHERE d.DeptID = e.DeptID AND d.Budget > 300000
);
```
</details>

4. What is the difference between WHERE and HAVING?
<details>
<summary>Show Answer</summary>
WHERE filters rows **before** grouping; HAVING filters groups **after** grouping.
</details>

5. Find employees who earn more than the average salary of ALL employees (not per department).
<details>
<summary>Show Answer</summary>
```sql
SELECT Name, Salary FROM EMPLOYEE
WHERE Salary > (SELECT AVG(Salary) FROM EMPLOYEE);
```
</details>

