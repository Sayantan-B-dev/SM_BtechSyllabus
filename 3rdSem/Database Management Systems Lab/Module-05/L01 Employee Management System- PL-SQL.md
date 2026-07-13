# Employee Management System- PL/SQL

**Course:** Database Management Systems Lab  
**Module:** 5 | **Lecture:** 1  
**Date:** 12-Oct-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 3  
**Learning Methodology:** Hands-on Experience  
**Reference:** Lab manual

## Lab Objectives

- Understand PL/SQL basic structure: DECLARE, BEGIN, EXCEPTION, END.
- Declare and use variables, IF-THEN-ELSE control structures, and LOOP statements.
- Write anonymous blocks for calculating bonuses and printing employee details.

## Theory / Concept

PL/SQL (Procedural Language extension to SQL) allows procedural logic like variables, conditions, and loops. In MySQL, the equivalent is the stored procedure language with DECLARE, BEGIN, END blocks. Variables are declared with DECLARE and assigned using SET or SELECT INTO. IF-THEN-ELSE provides conditional branching. LOOP, WHILE, and REPEAT provide iteration. Anonymous blocks are PL/SQL blocks that are not stored in the database -- they execute immediately.

## SQL Code

```sql
-- MySQL uses a similar procedural syntax in stored programs
-- These examples use MySQL's stored procedure language

USE EmployeeDB;

-- Basic anonymous block (in MySQL, we use a procedure since standalone blocks need special syntax)
DELIMITER //

CREATE PROCEDURE BasicPLSQL()
BEGIN
    -- Variable declaration
    DECLARE v_emp_name VARCHAR(100);
    DECLARE v_salary DECIMAL(10,2);
    DECLARE v_bonus DECIMAL(10,2);
    DECLARE v_rating INT DEFAULT 4;

    -- Assign value using SELECT INTO
    SELECT emp_name, salary INTO v_emp_name, v_salary
    FROM Employee WHERE emp_id = 1;

    -- IF-THEN-ELSE
    IF v_rating >= 4 THEN
        SET v_bonus = v_salary * 0.20;
    ELSEIF v_rating = 3 THEN
        SET v_bonus = v_salary * 0.10;
    ELSE
        SET v_bonus = v_salary * 0.05;
    END IF;

    -- Display results
    SELECT CONCAT('Employee: ', v_emp_name) AS Info;
    SELECT CONCAT('Salary: ', v_salary) AS Info;
    SELECT CONCAT('Bonus: ', v_bonus) AS Info;
    SELECT CONCAT('Total Compensation: ', (v_salary + v_bonus)) AS Info;
END //

DELIMITER ;

CALL BasicPLSQL();

-- LOOP example: print numbers 1 to 5
DELIMITER //

CREATE PROCEDURE LoopExample()
BEGIN
    DECLARE v_counter INT DEFAULT 1;

    -- Create a temporary table to store results
    CREATE TEMPORARY TABLE IF NOT EXISTS temp_results (message VARCHAR(100));
    TRUNCATE TABLE temp_results;

    my_loop: LOOP
        INSERT INTO temp_results VALUES (CONCAT('Number: ', v_counter));

        SET v_counter = v_counter + 1;

        IF v_counter > 5 THEN
            LEAVE my_loop;
        END IF;
    END LOOP my_loop;

    SELECT * FROM temp_results;
    DROP TEMPORARY TABLE temp_results;
END //

DELIMITER ;

CALL LoopExample();

-- Procedure to calculate bonus for all employees
DELIMITER //

CREATE PROCEDURE CalculateAllBonuses()
BEGIN
    DECLARE v_done INT DEFAULT FALSE;
    DECLARE v_emp_id INT;
    DECLARE v_emp_name VARCHAR(100);
    DECLARE v_salary DECIMAL(10,2);
    DECLARE v_bonus DECIMAL(10,2);

    DECLARE emp_cursor CURSOR FOR SELECT emp_id, emp_name, salary FROM Employee;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_done = TRUE;

    CREATE TEMPORARY TABLE IF NOT EXISTS bonus_results (emp_name VARCHAR(100), salary DECIMAL(10,2), bonus DECIMAL(10,2));
    TRUNCATE TABLE bonus_results;

    OPEN emp_cursor;

    read_loop: LOOP
        FETCH emp_cursor INTO v_emp_id, v_emp_name, v_salary;
        IF v_done THEN
            LEAVE read_loop;
        END IF;

        SET v_bonus = v_salary * 0.10;
        INSERT INTO bonus_results VALUES (v_emp_name, v_salary, v_bonus);
    END LOOP;

    CLOSE emp_cursor;
    SELECT * FROM bonus_results;
    DROP TEMPORARY TABLE bonus_results;
END //

DELIMITER ;

CALL CalculateAllBonuses();
```

## Expected Output

```
mysql> CALL BasicPLSQL();
+---------------------------+
| Info                      |
+---------------------------+
| Employee: Ravi Sharma     |
+---------------------------+
1 row in set (0.00 sec)

+---------------------+
| Info                |
+---------------------+
| Salary: 87500.00    |
+---------------------+
1 row in set (0.00 sec)

+-------------------+
| Info              |
+-------------------+
| Bonus: 17500.00   |
+-------------------+
1 row in set (0.00 sec)

+--------------------------------+
| Info                           |
+--------------------------------+
| Total Compensation: 105000.00  |
+--------------------------------+
1 row in set (0.00 sec)

mysql> CALL LoopExample();
+------------+
| message    |
+------------+
| Number: 1  |
| Number: 2  |
| Number: 3  |
| Number: 4  |
| Number: 5  |
+------------+
5 rows in set (0.00 sec)

mysql> CALL CalculateAllBonuses();
+--------------+----------+---------+
| emp_name     | salary   | bonus   |
+--------------+----------+---------+
| Ravi Sharma  | 87500.00 | 8750.00 |
| Priya Mehta  |109500.00 |10950.00 |
| Amit Joshi   | 55000.00 | 5500.00 |
| Sneha Kapoor | 85000.00 | 8500.00 |
| Vikram Singh | 50000.00 | 5000.00 |
| Ananya Das   | 93000.00 | 9300.00 |
| Rohit Verma  | 72000.00 | 7200.00 |
| Neha Agarwal | 90000.00 | 9000.00 |
| Karan Patel  |100000.00 |10000.00 |
| Meera Iyer   | 78000.00 | 7800.00 |
+--------------+----------+---------+
10 rows in set (0.00 sec)
```

## Homework / Practice

1. Write a PL/SQL procedure that takes an employee ID as input and prints their name, department, and years of service.
2. Write a WHILE loop that prints the first 10 Fibonacci numbers.
3. Modify `CalculateAllBonuses` to give a 20% bonus to employees with salary > 90000 and 10% to others.
