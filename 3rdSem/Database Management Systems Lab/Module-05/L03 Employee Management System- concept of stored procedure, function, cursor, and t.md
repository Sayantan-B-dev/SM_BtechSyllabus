# Employee Management System- concept of stored procedure, function, cursor, and trigger.

**Course:** Database Management Systems Lab  
**Module:** 5 | **Lecture:** 3  
**Date:** 26-Oct-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 4  
**Learning Methodology:** Hands-on Experience  
**Reference:** Lab manual

## Lab Objectives

- Create a stored procedure with IN and OUT parameters.
- Call the procedure to get the employee count by department.
- Understand the difference between IN, OUT, and INOUT parameter types.

## Theory / Concept

A stored procedure is a precompiled collection of SQL statements stored in the database. It can have IN (input), OUT (output), and INOUT (both) parameters. Stored procedures improve performance by reducing network traffic and enable code reuse. IN parameters pass values into the procedure; OUT parameters return values to the caller; INOUT parameters do both. Procedures can call other procedures and include transaction control.

## SQL Code

```sql
USE EmployeeDB;

-- Procedure with IN parameter: get employee count by department
DELIMITER //

CREATE PROCEDURE GetEmployeeCountByDept(IN p_dept_name VARCHAR(50), OUT p_count INT)
BEGIN
    SELECT COUNT(*) INTO p_count
    FROM Employee
    WHERE department = p_dept_name;
END //

DELIMITER ;

-- Call the procedure
CALL GetEmployeeCountByDept('IT', @it_count);
SELECT @it_count AS IT_Employee_Count;

CALL GetEmployeeCountByDept('HR', @hr_count);
SELECT @hr_count AS HR_Employee_Count;

-- Procedure with INOUT parameter
DELIMITER //

CREATE PROCEDURE IncrementSalary(INOUT p_salary DECIMAL(10,2), IN p_percent DECIMAL(5,2))
BEGIN
    SET p_salary = p_salary + (p_salary * p_percent / 100);
END //

DELIMITER ;

SET @current_salary = 50000;
CALL IncrementSalary(@current_salary, 10);
SELECT @current_salary AS New_Salary;  -- 55000

-- Procedure with multiple IN parameters and an OUT parameter
DELIMITER //

CREATE PROCEDURE GetEmployeeInfo(
    IN p_emp_id INT,
    OUT p_name VARCHAR(100),
    OUT p_dept VARCHAR(50),
    OUT p_salary DECIMAL(10,2)
)
BEGIN
    SELECT emp_name, department, salary
    INTO p_name, p_dept, p_salary
    FROM Employee
    WHERE emp_id = p_emp_id;
END //

DELIMITER ;

CALL GetEmployeeInfo(1, @name, @dept, @salary);
SELECT @name AS Employee_Name, @dept AS Department, @salary AS Salary;

-- Procedure that returns a result set (SELECT inside procedure)
DELIMITER //

CREATE PROCEDURE GetEmployeesByDept(IN p_dept_name VARCHAR(50))
BEGIN
    SELECT emp_id, emp_name, job_role, salary
    FROM Employee
    WHERE department = p_dept_name
    ORDER BY salary DESC;
END //

DELIMITER ;

CALL GetEmployeesByDept('Finance');

-- Procedure with transaction handling
DELIMITER //

CREATE PROCEDURE TransferEmployee(
    IN p_emp_id INT,
    IN p_new_dept_id INT,
    OUT p_result VARCHAR(100)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SET p_result = 'Error: Transfer failed, rolled back';
    END;

    START TRANSACTION;

    UPDATE Employee SET dept_id = p_new_dept_id WHERE emp_id = p_emp_id;

    -- Assume we need to update department budget or other related tables
    UPDATE Department SET budget = budget + 1000 WHERE dept_id = p_new_dept_id;

    COMMIT;
    SET p_result = 'Success: Employee transferred';
END //

DELIMITER ;

CALL TransferEmployee(1, 2, @result);
SELECT @result AS Transfer_Result;

-- Verify
SELECT emp_name, department FROM Employee WHERE emp_id = 1;
```

## Expected Output

```
mysql> CALL GetEmployeeCountByDept('IT', @it_count);
Query OK, 0 rows affected (0.00 sec)

mysql> SELECT @it_count AS IT_Employee_Count;
+-------------------+
| IT_Employee_Count |
+-------------------+
|                 4 |
+-------------------+

mysql> CALL GetEmployeeInfo(1, @name, @dept, @salary);
Query OK, 1 row affected (0.00 sec)

mysql> SELECT @name AS Employee_Name, @dept AS Department, @salary AS Salary;
+---------------+------------+----------+
| Employee_Name | Department | Salary   |
+---------------+------------+----------+
| Ravi Sharma   | IT         | 87500.00 |
+---------------+------------+----------+

mysql> CALL GetEmployeesByDept('Finance');
+--------+--------------+------------------+----------+
| emp_id | emp_name     | job_role         | salary   |
+--------+--------------+------------------+----------+
|      4 | Sneha Kapoor | Finance Manager  | 85000.00 |
|      3 | Amit Joshi   | Accountant       | 55000.00 |
+--------+--------------+------------------+----------+

mysql> CALL TransferEmployee(1, 2, @result);
Query OK, 0 rows affected (0.01 sec)

mysql> SELECT @result AS Transfer_Result;
+-----------------------------+
| Transfer_Result             |
+-----------------------------+
| Success: Employee transferred|
+-----------------------------+

mysql> SELECT emp_name, department FROM Employee WHERE emp_id = 1;
+-------------+------------+
| emp_name    | department |
+-------------+------------+
| Ravi Sharma | IT         |  (department column not updated, only dept_id)
+-------------+------------+
```

## Homework / Practice

1. Create a stored procedure named `GetDepartmentBudget` that takes a department name as IN parameter and returns the total salary expense as an OUT parameter.
2. Write a procedure `UpdateEmployeeSalary` that takes emp_id and percentage increase as IN parameters and updates the salary. Use a transaction.
3. Create a procedure that returns all employees earning more than a given salary using a result set.
