# Authorization Models

**Course:** Database Management Systems  
**Module:** 4 | **Lecture:** 3  
**Date:** 06-Oct-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 4  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## What is Authorization?

Authorization is the process of determining what an authenticated user is allowed to do. While authentication answers "who are you?", authorization answers "what are you allowed to do?". Authorization controls access to database objects (tables, views, procedures) and actions (SELECT, INSERT, UPDATE, DELETE).

## Privilege Types

A privilege is a right to perform a specific operation on a specific database object.

### System Privileges
Rights to perform administrative actions. Example: `CREATE USER`, `CREATE TABLE`, `DROP ANY TABLE`, `BACKUP ANY TABLE`. These are typically granted only to database administrators.

### Object Privileges
Rights to perform operations on specific objects (tables, views, sequences, procedures).

| Privilege       | Description                                         |
|-----------------|-----------------------------------------------------|
| SELECT          | Read rows from a table or view.                     |
| INSERT          | Add new rows to a table.                            |
| UPDATE          | Modify existing rows in a table.                    |
| DELETE          | Remove rows from a table.                           |
| REFERENCES      | Create a FOREIGN KEY constraint that references a table. |
| EXECUTE         | Run a stored procedure or function.                 |
| ALL PRIVILEGES  | Grants all available privileges on an object.       |

## The GRANT Statement

The `GRANT` statement gives privileges to a user or role.

**Basic syntax:**

```sql
GRANT privilege_list
ON object
TO user_or_role;
```

**Examples:**

```sql
-- Grant SELECT on the employees table to user alice
GRANT SELECT ON employees TO alice;

-- Grant INSERT and UPDATE on specific columns
GRANT INSERT (emp_id, emp_name, salary), UPDATE (salary) ON employees TO alice;

-- Grant all privileges on the departments table
GRANT ALL PRIVILEGES ON departments TO alice;
```

### WITH GRANT OPTION

When a user receives a privilege `WITH GRANT OPTION`, they can pass that privilege on to other users. This creates a chain of authorization.

```sql
-- Grant SELECT with the ability to grant it further
GRANT SELECT ON employees TO alice WITH GRANT OPTION;
```

Now `alice` can do:

```sql
GRANT SELECT ON employees TO bob;
```

The `WITH GRANT OPTION` is powerful but dangerous because it allows delegation. If `alice` is compromised, the attacker can grant privileges to anyone.

## The REVOKE Statement

The `REVOKE` statement removes previously granted privileges.

**Basic syntax:**

```sql
REVOKE privilege_list
ON object
FROM user_or_role;
```

**Examples:**

```sql
-- Revoke the SELECT privilege on employees from alice
REVOKE SELECT ON employees FROM alice;

-- Revoke all privileges
REVOKE ALL PRIVILEGES ON employees FROM alice;
```

### CASCADE vs RESTRICT

When revoking a privilege that was granted `WITH GRANT OPTION`, the revocation can cascade:

- **CASCADE:** Also revokes privileges that the user granted to others.
- **RESTRICT:** Fails if the user has passed the privilege to others.

```sql
REVOKE SELECT ON employees FROM alice CASCADE;
REVOKE SELECT ON employees FROM alice RESTRICT;
```

## The Authorization Graph

The authorization graph models how privileges propagate through a system.

- **Nodes:** Users (including the Database Administrator / DBA).
- **Edges:** A directed edge from user U to user V means U granted a privilege to V.

```
        DBA
       /    \
      /      \
   Alice     Bob
    |         |
    |         |
   Carol     Dave
```

In this graph:
- DBA granted privileges to Alice and Bob.
- Alice granted her privileges to Carol.
- Bob granted his privileges to Dave.

If DBA revokes privileges from Alice with CASCADE, Carol also loses those privileges. If DBA revokes with RESTRICT, the revoke fails because Alice has already passed privileges to Carol.

## SQL Examples in Detail

### Scenario: A Company Database

```sql
-- Create users
CREATE USER 'hr_manager'@'localhost' IDENTIFIED BY 'HrPass123';
CREATE USER 'payroll_clerk'@'localhost' IDENTIFIED BY 'PayPass456';
CREATE USER 'auditor'@'localhost' IDENTIFIED BY 'AudPass789';

-- Create a table
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    salary DECIMAL(10,2),
    department VARCHAR(50)
);
```

**Step 1: Grant SELECT to the auditor (read-only access).**

```sql
GRANT SELECT ON employees TO auditor;
```

**Step 2: Grant SELECT and INSERT to the HR manager with grant option.**

```sql
GRANT SELECT, INSERT ON employees TO hr_manager WITH GRANT OPTION;
```

**Step 3: HR manager grants SELECT on employees to payroll_clerk.**

```sql
-- Executed by hr_manager
GRANT SELECT ON employees TO payroll_clerk;
```

**Step 4: Revoke SELECT and INSERT from hr_manager (cascade).**

```sql
REVOKE SELECT, INSERT ON employees FROM hr_manager CASCADE;
```

This also removes payroll_clerk's SELECT privilege because it was received through hr_manager's grant.

## PUBLIC and Roles

- **PUBLIC:** A special group that includes all current and future users. Granting to PUBLIC gives the privilege to everyone.

```sql
GRANT SELECT ON employees TO PUBLIC;
```

- **Roles:** A named group of privileges that can be assigned to users. Roles simplify administration. (Covered in detail in L04.)

## Column-Level Privileges

Privileges can be restricted to specific columns rather than the entire table.

```sql
-- Allow SELECT only on emp_id and emp_name, not on salary
GRANT SELECT (emp_id, emp_name) ON employees TO payroll_clerk;

-- Allow UPDATE only on the department column
GRANT UPDATE (department) ON employees TO hr_manager;
```

## View-Based Authorization

Views provide a powerful way to restrict access to specific rows and columns without granting direct table access.

```sql
-- Create a view that hides salary information
CREATE VIEW public_employee_info AS
SELECT emp_id, emp_name, department
FROM employees;

-- Grant access to the view, not the underlying table
GRANT SELECT ON public_employee_info TO auditor;
```

The auditor can see employee names and departments but never the salary column.

## Least Privilege Principle

A fundamental security principle: **a user should be given only the minimum privileges necessary to perform their job.** Never grant more than needed.

Examples:
- An auditor needs only SELECT, not INSERT/UPDATE/DELETE.
- A payroll clerk needs SELECT and UPDATE on salary, not the ability to drop tables.
- A web application should connect with a limited account, not the DBA account.

---

## Practice Problems

1. Write a GRANT statement that gives user `jane` SELECT and INSERT privileges on the `orders` table, with the ability to pass these privileges to others.
2. What is the difference between `REVOKE ... CASCADE` and `REVOKE ... RESTRICT`? Give an example scenario where RESTRICT would prevent an error.
3. Draw an authorization graph for the following: DBA grants SELECT to Alice and Bob. Alice grants SELECT to Carol. Bob grants SELECT to Dave. Then DBA revokes SELECT from Bob with CASCADE. Who retains the privilege?
4. Explain the principle of least privilege and give two concrete examples of its application in a university database.
5. How can views be used as an authorization mechanism? Write SQL to demonstrate.
