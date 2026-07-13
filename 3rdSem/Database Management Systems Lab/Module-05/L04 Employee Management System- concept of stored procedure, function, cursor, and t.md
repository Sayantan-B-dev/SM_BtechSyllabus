# Employee Management System- concept of stored procedure, function, cursor, and trigger.

**Course:** Database Management Systems Lab  
**Module:** 5 | **Lecture:** 4  
**Date:** 26-Oct-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 4  
**Learning Methodology:** Hands-on Experience  
**Reference:** Lab manual

## Lab Objectives

- Create a stored function that returns a value (e.g., calculate years of service).
- Understand the difference between stored procedures and functions.
- Create triggers: BEFORE INSERT and AFTER UPDATE, with an audit trigger example.

## Theory / Concept

A stored function returns a single value (scalar) and can be used in SQL expressions. Unlike procedures, functions must return a value and cannot use OUT/INOUT parameters. A trigger is a database object that automatically executes in response to INSERT, UPDATE, or DELETE events on a table. BEFORE triggers run before the operation, AFTER triggers after. Triggers are commonly used for auditing, validation, and maintaining derived data.

## SQL Code

```sql
USE EmployeeDB;

-- Stored function: calculate years of service
DELIMITER //

CREATE FUNCTION YearsOfService(p_emp_id INT)
RETURNS DECIMAL(5,1)
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE v_hire_date DATE;
    DECLARE v_years DECIMAL(5,1);

    SELECT hire_date INTO v_hire_date FROM Employee WHERE emp_id = p_emp_id;

    SET v_years = DATEDIFF(CURDATE(), v_hire_date) / 365.25;
    RETURN ROUND(v_years, 1);
END //

DELIMITER ;

-- Use the function in a query
SELECT emp_name, hire_date, YearsOfService(emp_id) AS years_of_service
FROM Employee
ORDER BY years_of_service DESC;

-- Function: calculate bonus based on salary and rating
DELIMITER //

CREATE FUNCTION CalculateBonus(p_salary DECIMAL(10,2), p_rating INT)
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    DECLARE v_bonus DECIMAL(10,2);

    IF p_rating >= 4 THEN
        SET v_bonus = p_salary * 0.20;
    ELSEIF p_rating = 3 THEN
        SET v_bonus = p_salary * 0.10;
    ELSE
        SET v_bonus = p_salary * 0.05;
    END IF;

    RETURN v_bonus;
END //

DELIMITER ;

SELECT emp_name, salary, CalculateBonus(salary, 4) AS bonus FROM Employee LIMIT 5;

-- Difference: Procedures vs Functions
-- Procedures: Can have IN/OUT/INOUT, may return result sets, called with CALL
-- Functions: Must return a single value, used in expressions, cannot have OUT

-- TRIGGER: BEFORE INSERT - auto-set hire_date if not provided
DELIMITER //

CREATE TRIGGER before_employee_insert
BEFORE INSERT ON Employee
FOR EACH ROW
BEGIN
    IF NEW.hire_date IS NULL THEN
        SET NEW.hire_date = CURDATE();
    END IF;

    IF NEW.status IS NULL THEN
        SET NEW.status = 'Active';
    END IF;
END //

DELIMITER ;

-- Test the trigger
INSERT INTO Employee (emp_name, email, phone, department, job_role, salary, dept_id)
VALUES ('New Employee', 'new.emp@company.com', '9999999999', 'IT', 'Trainee', 35000.00, 1);

SELECT emp_name, hire_date, status FROM Employee WHERE emp_name = 'New Employee';

-- TRIGGER: AFTER UPDATE - audit log for salary changes
CREATE TABLE IF NOT EXISTS SalaryAudit (
    audit_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_id INT,
    old_salary DECIMAL(10,2),
    new_salary DECIMAL(10,2),
    changed_by VARCHAR(100),
    change_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DELIMITER //

CREATE TRIGGER after_employee_salary_update
AFTER UPDATE ON Employee
FOR EACH ROW
BEGIN
    IF OLD.salary <> NEW.salary THEN
        INSERT INTO SalaryAudit (emp_id, old_salary, new_salary, changed_by)
        VALUES (NEW.emp_id, OLD.salary, NEW.salary, USER());
    END IF;
END //

DELIMITER ;

-- Test the audit trigger
UPDATE Employee SET salary = 38000 WHERE emp_name = 'New Employee';

-- View audit log
SELECT * FROM SalaryAudit;

-- TRIGGER: BEFORE DELETE - prevent deletion of managers
DELIMITER //

CREATE TRIGGER before_employee_delete
BEFORE DELETE ON Employee
FOR EACH ROW
BEGIN
    DECLARE v_report_count INT;

    SELECT COUNT(*) INTO v_report_count
    FROM Employee WHERE manager_id = OLD.emp_id;

    IF v_report_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cannot delete employee who has direct reports';
    END IF;
END //

DELIMITER ;

-- Test: try to delete Ravi Sharma (has 3 direct reports)
-- DELETE FROM Employee WHERE emp_name = 'Ravi Sharma';
-- This would trigger an error
```

## Expected Output

```
mysql> SELECT emp_name, hire_date, YearsOfService(emp_id) AS years_of_service
FROM Employee ORDER BY years_of_service DESC;
+--------------+------------+-------------------+
| emp_name     | hire_date  | years_of_service  |
+--------------+------------+-------------------+
| Neha Agarwal | 2017-05-30 |               9.1 |
| Priya Mehta  | 2018-03-01 |               8.4 |
| Meera Iyer   | 2019-08-14 |               6.9 |
| Sneha Kapoor | 2019-01-20 |               7.5 |
| Ravi Sharma  | 2020-06-15 |               6.1 |
| Ananya Das   | 2020-11-12 |               5.7 |
| Amit Joshi   | 2021-09-10 |               4.8 |
| Rohit Verma  | 2021-07-22 |               5.0 |
| Karan Patel  | 2022-01-18 |               4.5 |
| Vikram Singh | 2022-04-05 |               4.3 |
+--------------+------------+-------------------+

mysql> SELECT emp_name, salary, CalculateBonus(salary, 4) AS bonus FROM Employee LIMIT 5;
+--------------+----------+----------+
| emp_name     | salary   | bonus    |
+--------------+----------+----------+
| Ravi Sharma  | 87500.00 | 17500.00 |
| Priya Mehta  |109500.00 | 21900.00 |
| Amit Joshi   | 55000.00 | 11000.00 |
| Sneha Kapoor | 85000.00 | 17000.00 |
| Vikram Singh | 50000.00 | 10000.00 |
+--------------+----------+----------+

mysql> -- Test before insert trigger
INSERT INTO Employee ...;
SELECT emp_name, hire_date, status FROM Employee WHERE emp_name = 'New Employee';
+-------------+------------+--------+
| emp_name    | hire_date  | status |
+-------------+------------+--------+
| New Employee| 2026-10-26 | Active |
+-------------+------------+--------+

mysql> -- Test audit trigger
UPDATE Employee SET salary = 38000 WHERE emp_name = 'New Employee';
SELECT * FROM SalaryAudit;
+----------+--------+------------+------------+----------------+---------------------+
| audit_id | emp_id | old_salary | new_salary | changed_by     | change_date         |
+----------+--------+------------+------------+----------------+---------------------+
|        1 |     12 |   35000.00 |   38000.00 | root@localhost | 2026-10-26 10:30:00 |
+----------+--------+------------+------------+----------------+---------------------+
```

## Homework / Practice

1. Create a function that returns the department name for a given employee ID.
2. Write an AFTER DELETE trigger that logs deleted employee records into an `EmployeeDeletionLog` table.
3. Create a BEFORE UPDATE trigger that prevents setting a salary below 30000.
