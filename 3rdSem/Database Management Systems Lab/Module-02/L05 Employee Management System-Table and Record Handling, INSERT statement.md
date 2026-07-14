# Employee Management System-Table and Record Handling, INSERT statement

**Course:** Database Management Systems Lab  
**Module:** 2 | **Lecture:** 5  
**Date:** 03-Aug-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Hands-on Experience  
**Reference:** Lab manual

## Lab Objectives

- Understand transaction control statements: START TRANSACTION, COMMIT, ROLLBACK, and SAVEPOINT.
- Perform a fund transfer between departments as a transaction.
- Demonstrate rollback on error and partial rollback using SAVEPOINT.

## Theory / Concept

A transaction is a sequence of SQL statements that execute as a single unit of work. Transactions follow ACID properties (Atomicity, Consistency, Isolation, Durability). START TRANSACTION begins a transaction. COMMIT makes all changes permanent. ROLLBACK undoes all changes since the last COMMIT or START TRANSACTION. SAVEPOINT creates a point within a transaction to which you can later roll back, allowing partial rollbacks without undoing the entire transaction.

## SQL Code

```sql
USE EmployeeDB;

-- View initial budgets
SELECT dept_name, budget FROM Department;

-- Start transaction
START TRANSACTION;

-- Transfer 50000 from Sales budget to IT budget
UPDATE Department SET budget = budget - 50000 WHERE dept_name = 'Sales';
UPDATE Department SET budget = budget + 50000 WHERE dept_name = 'IT';

-- Verify within transaction
SELECT dept_name, budget FROM Department WHERE dept_name IN ('Sales', 'IT');

-- Commit the transaction
COMMIT;

-- Verify after commit
SELECT dept_name, budget FROM Department WHERE dept_name IN ('Sales', 'IT');

-- Example with rollback on error
START TRANSACTION;

UPDATE Employee SET salary = salary + 10000 WHERE dept_id = 1;

-- Suppose we detect a mistake, rollback
ROLLBACK;

-- Verify no change happened
SELECT emp_name, salary FROM Employee WHERE dept_id = 1;

-- Example with SAVEPOINT
START TRANSACTION;

UPDATE Employee SET salary = salary + 5000 WHERE dept_id = 1;
SAVEPOINT after_first_update;

UPDATE Employee SET salary = salary + 3000 WHERE dept_id = 3;

-- Suppose we want to keep the first update but undo the second
ROLLBACK TO SAVEPOINT after_first_update;

-- Commit only the first update
COMMIT;

-- Verify: IT got +5000, HR original
SELECT emp_name, department, salary FROM Employee WHERE dept_id IN (1, 3);
```

## Expected Output

```
mysql> SELECT dept_name, budget FROM Department;
+-----------+-----------+
| dept_name | budget    |
+-----------+-----------+
| IT        | 500000.00 |
| Finance   | 350000.00 |
| HR        | 200000.00 |
| Sales     | 400000.00 |
| Marketing | 250000.00 |
...

mysql> -- After transfer (before commit)
SELECT dept_name, budget FROM Department WHERE dept_name IN ('Sales', 'IT');
+-----------+-----------+
| dept_name | budget    |
+-----------+-----------+
| IT        | 550000.00 |
| Sales     | 350000.00 |
+-----------+-----------+

-- After COMMIT, changes are permanent

mysql> -- ROLLBACK example
SELECT emp_name, salary FROM Employee WHERE dept_id = 1;
-- Salaries remain unchanged because ROLLBACK undid the UPDATE

mysql> -- SAVEPOINT example: only IT got +5000, HR unchanged
SELECT emp_name, department, salary FROM Employee WHERE dept_id IN (1, 3);
+--------------+------------+----------+
| emp_name     | department | salary   |
+--------------+------------+----------+
| Ravi Sharma  | IT         | 87500.00 |  (82500 + 5000)
| Priya Mehta  | IT         |109500.00 |  (104500 + 5000)
| Ananya Das   | IT         | 93000.00 |  (88000 + 5000)
| Karan Patel  | IT         |100000.00 |  (95000 + 5000)
| Vikram Singh | HR         | 50000.00 |  (unchanged)
| Meera Iyer   | HR         | 78000.00 |  (unchanged)
+--------------+------------+----------+
```

## Homework / Practice

1. Start a transaction, insert a new department 'Logistics' with budget 100000, then ROLLBACK. Verify the department was not created.
   <details>
   <summary>Show Answer</summary>
   START TRANSACTION; INSERT INTO Department (dept_name, budget) VALUES ('Logistics', 100000.00); ROLLBACK; SELECT * FROM Department WHERE dept_name = 'Logistics'; -- No rows returned
   </details>

2. Use SAVEPOINT to update employee salaries in steps: add 2000 to IT, set a savepoint, add 3000 to HR, then rollback to the savepoint. Commit and check the results.
   <details>
   <summary>Show Answer</summary>
   START TRANSACTION; UPDATE Employee SET salary = salary + 2000 WHERE department = 'IT'; SAVEPOINT sp1; UPDATE Employee SET salary = salary + 3000 WHERE department = 'HR'; ROLLBACK TO sp1; COMMIT;
   </details>

3. Write a transaction that transfers 25000 from the Marketing budget to the Research budget. Commit only if both UPDATE statements succeed.
   <details>
   <summary>Show Answer</summary>
   START TRANSACTION; UPDATE Department SET budget = budget - 25000 WHERE dept_name = 'Marketing'; UPDATE Department SET budget = budget + 25000 WHERE dept_name = 'Research'; COMMIT;
   </details>
