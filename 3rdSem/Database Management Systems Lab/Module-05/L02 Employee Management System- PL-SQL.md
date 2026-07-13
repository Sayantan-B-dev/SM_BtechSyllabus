# Employee Management System- PL/SQL

**Course:** Database Management Systems Lab  
**Module:** 5 | **Lecture:** 2  
**Date:** 12-Oct-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 3  
**Learning Methodology:** Hands-on Experience  
**Reference:** Lab manual

## Lab Objectives

- Understand explicit cursors: DECLARE, OPEN, FETCH, and CLOSE.
- Use implicit cursors with SELECT INTO and FOR loops.
- Write a cursor to display all employee names and salaries.

## Theory / Concept

A cursor is a database object that allows row-by-row processing of query results. Explicit cursors are manually declared, opened, fetched from, and closed. Implicit cursors are automatically created by MySQL for single-row SELECT INTO statements. The FOR loop (cursor FOR loop in Oracle PL/SQL or using a cursor with a loop in MySQL) simplifies cursor handling by automatically opening, fetching, and closing the cursor.

## SQL Code

```sql
USE EmployeeDB;

-- 1. Explicit cursor: display all employee names and salaries
DELIMITER //

CREATE PROCEDURE DisplayEmployeeSalaries()
BEGIN
    DECLARE v_done INT DEFAULT FALSE;
    DECLARE v_emp_name VARCHAR(100);
    DECLARE v_salary DECIMAL(10,2);
    DECLARE v_dept VARCHAR(50);

    -- Declare cursor
    DECLARE emp_cursor CURSOR FOR
        SELECT emp_name, department, salary FROM Employee ORDER BY department;

    -- Declare NOT FOUND handler
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_done = TRUE;

    -- Temporary table for output
    CREATE TEMPORARY TABLE IF NOT EXISTS emp_salary_report (
        employee_name VARCHAR(100),
        department VARCHAR(50),
        salary DECIMAL(10,2)
    );
    TRUNCATE TABLE emp_salary_report;

    -- Open cursor
    OPEN emp_cursor;

    -- Fetch loop
    read_loop: LOOP
        FETCH emp_cursor INTO v_emp_name, v_dept, v_salary;
        IF v_done THEN
            LEAVE read_loop;
        END IF;

        INSERT INTO emp_salary_report VALUES (v_emp_name, v_dept, v_salary);
    END LOOP;

    -- Close cursor
    CLOSE emp_cursor;

    -- Display results
    SELECT * FROM emp_salary_report;
    DROP TEMPORARY TABLE emp_salary_report;
END //

DELIMITER ;

CALL DisplayEmployeeSalaries();

-- 2. Cursor with parameter: employees by department
DELIMITER //

CREATE PROCEDURE EmployeesByDepartment(IN p_dept_name VARCHAR(50))
BEGIN
    DECLARE v_done INT DEFAULT FALSE;
    DECLARE v_emp_name VARCHAR(100);
    DECLARE v_salary DECIMAL(10,2);

    DECLARE dept_cursor CURSOR FOR
        SELECT emp_name, salary FROM Employee WHERE department = p_dept_name;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_done = TRUE;

    CREATE TEMPORARY TABLE IF NOT EXISTS dept_emp_list (
        employee_name VARCHAR(100),
        salary DECIMAL(10,2)
    );
    TRUNCATE TABLE dept_emp_list;

    OPEN dept_cursor;

    fetch_loop: LOOP
        FETCH dept_cursor INTO v_emp_name, v_salary;
        IF v_done THEN
            LEAVE fetch_loop;
        END IF;

        INSERT INTO dept_emp_list VALUES (v_emp_name, v_salary);
    END LOOP;

    CLOSE dept_cursor;

    SELECT CONCAT('Employees in ', p_dept_name, ' department:') AS Department;
    SELECT * FROM dept_emp_list;
    DROP TEMPORARY TABLE dept_emp_list;
END //

DELIMITER ;

CALL EmployeesByDepartment('IT');

-- 3. Cursor with aggregation: salary statistics per department
DELIMITER //

CREATE PROCEDURE DepartmentSalaryStats()
BEGIN
    DECLARE v_done INT DEFAULT FALSE;
    DECLARE v_dept_name VARCHAR(50);
    DECLARE v_emp_count INT;
    DECLARE v_avg_salary DECIMAL(10,2);
    DECLARE v_max_salary DECIMAL(10,2);

    DECLARE stats_cursor CURSOR FOR
        SELECT department, COUNT(*), AVG(salary), MAX(salary)
        FROM Employee
        GROUP BY department;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_done = TRUE;

    CREATE TEMPORARY TABLE IF NOT EXISTS dept_stats (
        department VARCHAR(50),
        emp_count INT,
        avg_salary DECIMAL(10,2),
        max_salary DECIMAL(10,2)
    );
    TRUNCATE TABLE dept_stats;

    OPEN stats_cursor;

    loop_name: LOOP
        FETCH stats_cursor INTO v_dept_name, v_emp_count, v_avg_salary, v_max_salary;
        IF v_done THEN
            LEAVE loop_name;
        END IF;

        INSERT INTO dept_stats VALUES (v_dept_name, v_emp_count, v_avg_salary, v_max_salary);
    END LOOP;

    CLOSE stats_cursor;

    SELECT * FROM dept_stats;
    DROP TEMPORARY TABLE dept_stats;
END //

DELIMITER ;

CALL DepartmentSalaryStats();
```

## Expected Output

```
mysql> CALL DisplayEmployeeSalaries();
+-----------------+------------+----------+
| employee_name   | department | salary   |
+-----------------+------------+----------+
| Amit Joshi      | Finance    | 55000.00 |
| Sneha Kapoor    | Finance    | 85000.00 |
| Meera Iyer      | HR         | 78000.00 |
| Vikram Singh    | HR         | 50000.00 |
| Ananya Das      | IT         | 93000.00 |
| Karan Patel     | IT         |100000.00 |
| Priya Mehta     | IT         |109500.00 |
| Ravi Sharma     | IT         | 87500.00 |
| Neha Agarwal    | Sales      | 90000.00 |
| Rohit Verma     | Sales      | 72000.00 |
+-----------------+------------+----------+
10 rows in set (0.00 sec)

mysql> CALL EmployeesByDepartment('IT');
+----------------------------+
| Department                 |
+----------------------------+
| Employees in IT department |
+----------------------------+
1 row in set (0.00 sec)

+-----------------+----------+
| employee_name   | salary   |
+-----------------+----------+
| Ravi Sharma     | 87500.00 |
| Priya Mehta     |109500.00 |
| Ananya Das      | 93000.00 |
| Karan Patel     |100000.00 |
+-----------------+----------+
4 rows in set (0.00 sec)

mysql> CALL DepartmentSalaryStats();
+------------+-----------+------------+------------+
| department | emp_count | avg_salary | max_salary |
+------------+-----------+------------+------------+
| Finance    |         2 | 70000.00   |   85000.00 |
| HR         |         2 | 64000.00   |   78000.00 |
| IT         |         4 | 97500.00   |  109500.00 |
| Sales      |         2 | 81000.00   |   90000.00 |
+------------+-----------+------------+------------+
4 rows in set (0.00 sec)
```

## Homework / Practice

1. Write a cursor that displays employees who have been with the company for more than 5 years (based on hire_date).
2. Create a procedure that uses a cursor to update the salary of all employees in a given department by a given percentage.
3. Write a cursor that finds employees earning less than the average salary of their department and prints their names with the difference.
