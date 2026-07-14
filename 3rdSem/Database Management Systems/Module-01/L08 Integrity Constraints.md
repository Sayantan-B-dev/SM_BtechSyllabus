# Integrity Constraints

**Course:** Database Management Systems  
**Module:** 1 | **Lecture:** 8  
**Date:** 23-Jul-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## Notes

### What are Integrity Constraints?

**Integrity constraints** are rules that the DBMS enforces to ensure the accuracy, consistency, and validity of data. They protect the database from accidental corruption by preventing invalid data from being inserted, updated, or deleted.

Think of integrity constraints as **guardrails** -- they do not prevent all bad data, but they prevent data that violates explicitly defined rules.

**Categories of integrity constraints:**
1. Domain Constraints
2. Key Constraints
3. Entity Integrity Constraints
4. Referential Integrity Constraints
5. Check Constraints
6. Assertions

---

### 1. Domain Constraints

**Definition:** Restrict the values that an attribute can take. They specify a **domain** of permissible values.

**Enforcement mechanisms:**
- **Data types** -- INTEGER, CHAR, VARCHAR, DATE, BOOLEAN, etc.
- **NOT NULL** -- Attribute must have a value (cannot be NULL).
- **DEFAULT** -- Provides a fallback value when none is supplied.
- **CHECK** -- Boolean condition on the value.

**SQL Examples:**

```sql
-- Data type restricts domain
CREATE TABLE Product (
    product_id  INT PRIMARY KEY,
    price       DECIMAL(10,2),   -- Domain: numbers with 2 decimal places
    quantity    INT,              -- Domain: integers
    name        VARCHAR(100),    -- Domain: up to 100 characters
    is_active   BOOLEAN          -- Domain: TRUE or FALSE
);

-- NOT NULL constraint
CREATE TABLE Student (
    student_id  CHAR(9) PRIMARY KEY,
    name        VARCHAR(50) NOT NULL,   -- Name is mandatory
    dept_id     CHAR(4) NOT NULL        -- Department is mandatory
);

-- DEFAULT constraint
CREATE TABLE Employee (
    emp_id      INT PRIMARY KEY,
    name        VARCHAR(50),
    hire_date   DATE DEFAULT CURRENT_DATE,       -- Defaults to today
    status      VARCHAR(10) DEFAULT 'ACTIVE',    -- Defaults to 'ACTIVE'
    salary      DECIMAL(10,2) DEFAULT 30000.00
);

-- CHECK constraint with conditions
CREATE TABLE Account (
    account_no  INT PRIMARY KEY,
    balance     DECIMAL(12,2) CHECK (balance >= 0),   -- Balance cannot be negative
    type        VARCHAR(10) CHECK (type IN ('SAVINGS', 'CURRENT', 'FD')),
    min_balance DECIMAL(12,2) CHECK (min_balance >= 1000 AND min_balance <= 50000)
);

-- Composite CHECK (checks across multiple columns)
CREATE TABLE OrderItem (
    order_id    INT,
    item_id     INT,
    quantity    INT CHECK (quantity > 0),
    unit_price  DECIMAL(10,2) CHECK (unit_price > 0),
    total_price DECIMAL(12,2),
    CHECK (total_price = quantity * unit_price)   -- Cross-column constraint
);
```

**Violation examples:**

```sql
-- Violates data type domain
INSERT INTO Product VALUES (1, 'abc', 10, 'Widget', TRUE);
-- ERROR: 'abc' is not a valid DECIMAL

-- Violates NOT NULL
INSERT INTO Student (student_id) VALUES ('CS2026001');
-- ERROR: name cannot be NULL

-- Violates CHECK
INSERT INTO Account VALUES (101, -500, 'SAVINGS', 5000);
-- ERROR: CHECK (balance >= 0) violated

-- Malevolent but syntactically valid
INSERT INTO Account VALUES (102, 1000, 'LOAN', 5000);
-- ERROR: CHECK (type IN ('SAVINGS', 'CURRENT', 'FD')) violated
```

---

### 2. Key Constraints

**Definition:** Ensure that each tuple (row) in a relation is uniquely identified by its key attributes.

**Concepts:**
- **UNIQUE constraint** -- All values in a column (or combination of columns) must be distinct. Allows exactly one NULL (in most DBMS).
- **PRIMARY KEY constraint** -- UNIQUE + NOT NULL. The chosen candidate key.

**SQL Examples:**

```sql
-- Single-column primary key
CREATE TABLE Customer (
    cust_id  INT PRIMARY KEY,            -- Unique and NOT NULL
    email    VARCHAR(100) UNIQUE,        -- No two customers share an email
    phone    VARCHAR(15) UNIQUE          -- No two customers share a phone
);

-- Composite primary key (multiple columns)
CREATE TABLE Enrollment (
    student_id  CHAR(9),
    course_id   CHAR(8),
    semester    VARCHAR(6),
    year        INT,
    grade       CHAR(2),
    PRIMARY KEY (student_id, course_id, semester, year)
    -- All four columns together must be unique
);

-- UNIQUE constraint on a combination of columns
CREATE TABLE RoomBooking (
    building    VARCHAR(20),
    room_no     VARCHAR(10),
    date        DATE,
    time_slot   VARCHAR(20),
    UNIQUE (building, room_no, date, time_slot)
    -- No double-booking: same room cannot be booked at same time
);

-- Named constraints (easier to drop/reference)
CREATE TABLE Employee (
    emp_id  INT,
    pan     VARCHAR(10),
    CONSTRAINT pk_employee PRIMARY KEY (emp_id),
    CONSTRAINT uk_employee_pan UNIQUE (pan)
);
```

**Violation examples:**

```sql
-- Duplicate primary key
INSERT INTO Customer VALUES (1, 'alice@u.com', '1234567890');
INSERT INTO Customer VALUES (1, 'bob@u.com', '0987654321');
-- ERROR: Duplicate primary key value (1)

-- Duplicate unique value
INSERT INTO Customer VALUES (2, 'alice@u.com', '1111111111');
-- ERROR: Duplicate email 'alice@u.com' violates UNIQUE constraint
```

---

### 3. Entity Integrity Constraint

**Definition:** No component of the primary key can be NULL. This is automatically enforced when you declare a PRIMARY KEY.

**Rationale:** If even one part of the primary key is NULL, we cannot guarantee unique identification of the tuple.

```sql
-- This table has entity integrity automatically
CREATE TABLE Student (
    student_id  CHAR(9) PRIMARY KEY    -- Implicitly NOT NULL
);

-- Composite primary key -- none of the columns can be NULL
CREATE TABLE Enrollment (
    student_id CHAR(9) NOT NULL,   -- Explicit NOT NULL
    course_id  CHAR(8) NOT NULL,   -- Explicit NOT NULL
    semester   VARCHAR(6),         -- Implicit NOT NULL (part of PK)
    PRIMARY KEY (student_id, course_id, semester)
);

-- Violation:
INSERT INTO Enrollment (student_id, course_id) VALUES ('CS2026001', 'CS301');
-- If semester is part of PK but not provided, DBMS may either:
-- (a) ERROR: NULL value in primary key column 'semester', or
-- (b) Accept if semester has a DEFAULT and is NOT NULL
```

**Note:** Some DBMS implementations (e.g., MySQL with nullable columns in a composite PK) may silently convert the column to NOT NULL. Standard SQL requires all PK attributes to be implicitly NOT NULL.

---

### 4. Referential Integrity Constraint

**Definition:** A foreign key value must either:
- Match a primary key value in the referenced table, OR
- Be completely NULL (if all FK columns are nullable).

**Purpose:** Ensures that references between tables remain valid (no "dangling pointers").

**SQL Syntax:**
```sql
FOREIGN KEY (local_columns) REFERENCES parent_table(parent_columns)
[ON DELETE referential_action]
[ON UPDATE referential_action]
```

**Example -- University Database:**

```sql
CREATE TABLE Department (
    dept_id   CHAR(4) PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL
);

CREATE TABLE Student (
    student_id CHAR(9) PRIMARY KEY,
    name       VARCHAR(50),
    dept_id    CHAR(4),
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

CREATE TABLE Course (
    course_id CHAR(8) PRIMARY KEY,
    title     VARCHAR(100),
    dept_id   CHAR(4) NOT NULL,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

CREATE TABLE Instructor (
    instructor_id CHAR(5) PRIMARY KEY,
    name          VARCHAR(50),
    dept_id       CHAR(4),
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

CREATE TABLE Section (
    section_id    INT PRIMARY KEY,
    course_id     CHAR(8),
    instructor_id CHAR(5),
    semester      VARCHAR(6),
    FOREIGN KEY (course_id) REFERENCES Course(course_id),
    FOREIGN KEY (instructor_id) REFERENCES Instructor(instructor_id)
);

CREATE TABLE Takes (
    student_id CHAR(9),
    section_id INT,
    grade      CHAR(2),
    PRIMARY KEY (student_id, section_id),
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (section_id) REFERENCES Section(section_id)
);
```

**Violations:**

```sql
-- Insert a student with a non-existent department
INSERT INTO Student VALUES ('CS2026001', 'Alice', 'XYZ');
-- ERROR: Foreign key violation -- no Department with dept_id = 'XYZ'

-- Delete a department that still has students
DELETE FROM Department WHERE dept_id = 'CS';
-- ERROR: Referential integrity violation (students reference this dept)
```

#### Referential Actions (Handling Violations)

When a referenced row is deleted or updated, we need rules to maintain integrity.

| Action | Description |
|---|---|
| **RESTRICT** (default in some DBMS) | Reject the delete/update if any referencing rows exist. |
| **NO ACTION** (SQL standard default) | Similar to RESTRICT; check at end of transaction. |
| **CASCADE** | Propagate the change to all referencing rows. |
| **SET NULL** | Set the foreign key in referencing rows to NULL. |
| **SET DEFAULT** | Set the foreign key to its default value. |

**SQL examples with referential actions:**

```sql
-- ON DELETE CASCADE: Delete enrollments when a student is deleted
CREATE TABLE Enrollment (
    student_id CHAR(9),
    course_id  CHAR(8),
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES Student(student_id)
        ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
        ON DELETE RESTRICT
);

-- ON DELETE SET NULL: Set instructor to NULL when instructor is deleted
CREATE TABLE Course (
    course_id      CHAR(8) PRIMARY KEY,
    title          VARCHAR(100),
    coordinator_id CHAR(5),
    FOREIGN KEY (coordinator_id) REFERENCES Instructor(coordinator_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- ON DELETE SET DEFAULT: Set department to default when dept is deleted
CREATE TABLE Student (
    student_id CHAR(9) PRIMARY KEY,
    name       VARCHAR(50),
    dept_id    CHAR(4) DEFAULT 'GEN',
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
        ON DELETE SET DEFAULT
);

-- ON DELETE NO ACTION: Reject if references exist
CREATE TABLE Project (
    project_id INT PRIMARY KEY,
    manager_id INT,
    FOREIGN KEY (manager_id) REFERENCES Employee(emp_id)
        ON DELETE NO ACTION
);
```

**Examples of what happens:**

Scenario: Delete Department 'CS' which has 50 students.

| Referential Action | Result |
|---|---|
| **RESTRICT** | DELETE fails. Error: "Cannot delete because dependent rows exist." |
| **CASCADE** | All 50 students are also deleted. Their enrollments cascade further. |
| **SET NULL** | All 50 students get `dept_id = NULL`. They become "un-departmented." |
| **SET DEFAULT** | All 50 students get `dept_id = 'GEN'` (if 'GEN' department exists). |

---

### 5. CHECK Constraints

**Definition:** A boolean condition that each row must satisfy. More powerful than domain constraints because they can involve multiple columns and even subqueries (with limitations).

```sql
-- Simple check on one column
CREATE TABLE Employee (
    emp_id INT PRIMARY KEY,
    salary DECIMAL(10,2) CHECK (salary > 0)
);

-- Check with multiple columns (row-level check)
CREATE TABLE Employee (
    emp_id       INT PRIMARY KEY,
    salary       DECIMAL(10,2),
    commission   DECIMAL(10,2),
    CHECK (commission IS NULL OR commission < salary)
    -- Commission cannot exceed salary
);

-- Check with date validation
CREATE TABLE Contract (
    contract_id   INT PRIMARY KEY,
    start_date    DATE NOT NULL,
    end_date      DATE,
    CHECK (end_date IS NULL OR end_date > start_date)
    -- End date must be after start date (if provided)
);

-- Named check constraint (easier to reference in error messages)
CREATE TABLE Student (
    student_id CHAR(9),
    age        INT,
    CONSTRAINT chk_student_age CHECK (age >= 16 AND age <= 100)
);
```

---

### 6. Assertions

**Definition:** An **assertion** is a constraint that involves multiple tables or aggregate conditions. It is a predicate that the database must always satisfy.

**Note:** While assertions are part of the SQL standard, most DBMS do not fully support them. Instead, use **CHECK constraints with subqueries** (limited support) or **triggers** (for complex cross-table validations).

**Standard SQL syntax:**
```sql
CREATE ASSERTION assertion_name CHECK (boolean_condition);
```

**Example -- Ensure every instructor teaches at most 3 courses per semester:**

```sql
CREATE ASSERTION MaxCoursesPerInstructor CHECK (
    NOT EXISTS (
        SELECT instructor_id, semester, year
        FROM Teaches
        GROUP BY instructor_id, semester, year
        HAVING COUNT(*) > 3
    )
);
```

**DBMS workaround using triggers (PostgreSQL example):**
```sql
CREATE OR REPLACE FUNCTION check_max_courses()
RETURNS TRIGGER AS $$
BEGIN
    IF (SELECT COUNT(*) FROM Teaches
        WHERE instructor_id = NEW.instructor_id
        AND semester = NEW.semester
        AND year = NEW.year) > 3 THEN
        RAISE EXCEPTION 'Instructor cannot teach more than 3 courses';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_max_courses
BEFORE INSERT ON Teaches
FOR EACH ROW EXECUTE FUNCTION check_max_courses();
```

**Example -- Ensure department budget is not exceeded by total salaries:**

```sql
CREATE ASSERTION BudgetNotExceeded CHECK (
    NOT EXISTS (
        SELECT d.dept_id
        FROM Department d
        WHERE d.total_budget < (
            SELECT COALESCE(SUM(e.salary), 0)
            FROM Employee e
            WHERE e.dept_id = d.dept_id
        )
    )
);
```

---

### Handling Violations -- Summary

| Violation Type | SQL Mechanism | DBMS Action |
|---|---|---|
| NULL in primary key | PRIMARY KEY | Reject with error |
| Duplicate primary key | PRIMARY KEY | Reject with error |
| Duplicate unique value | UNIQUE | Reject with error |
| Invalid data type | Column type | Reject with error |
| NULL in NOT NULL column | NOT NULL | Reject with error |
| CHECK condition false | CHECK | Reject with error |
| Invalid foreign key value | FOREIGN KEY | Reject with error |
| Delete referenced row | ON DELETE clause | RESTRICT / CASCADE / SET NULL / SET DEFAULT |
| Update referenced key | ON UPDATE clause | RESTRICT / CASCADE / SET NULL / SET DEFAULT |
| Cross-table condition | Assertion / Trigger | Reject or execute custom logic |

### Complete Example -- All Constraints in One Schema

```sql
CREATE DATABASE Library;

CREATE TABLE Member (
    member_id  INT PRIMARY KEY,                              -- Entity integrity + key constraint
    name       VARCHAR(100) NOT NULL,                        -- Domain: NOT NULL
    email      VARCHAR(100) UNIQUE,                          -- Key: uniqueness
    phone      VARCHAR(15),
    join_date  DATE DEFAULT CURRENT_DATE,                    -- Domain: DEFAULT
    status     VARCHAR(10) DEFAULT 'ACTIVE'
               CHECK (status IN ('ACTIVE', 'SUSPENDED', 'INACTIVE'))  -- CHECK
);

CREATE TABLE Book (
    isbn       CHAR(13) PRIMARY KEY,                         -- Entity integrity
    title      VARCHAR(200) NOT NULL,
    author     VARCHAR(100),
    pub_year   INT CHECK (pub_year >= 1450 AND pub_year <= EXTRACT(YEAR FROM CURRENT_DATE)),
    quantity   INT CHECK (quantity >= 0) DEFAULT 1
);

CREATE TABLE Borrow (
    borrow_id      INT PRIMARY KEY,
    member_id      INT NOT NULL,
    isbn           CHAR(13) NOT NULL,
    borrow_date    DATE NOT NULL DEFAULT CURRENT_DATE,
    due_date       DATE NOT NULL,
    return_date    DATE,
    CHECK (due_date > borrow_date),                           -- Row-level CHECK
    CHECK (return_date IS NULL OR return_date >= borrow_date), -- Composite CHECK
    FOREIGN KEY (member_id) REFERENCES Member(member_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    FOREIGN KEY (isbn) REFERENCES Book(isbn)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    CONSTRAINT chk_max_borrow CHECK (                        -- Assertion-like constraint
        (SELECT COUNT(*) FROM Borrow b
         WHERE b.member_id = Borrow.member_id
         AND b.return_date IS NULL) <= 5
    ) -- Note: subquery in CHECK may not be supported in all DBMS
);
```

---

## Practice Problems

**1.** Write SQL to create a `Product` table with: `product_id` (PK), `name` (NOT NULL), `price` (CHECK > 0), `stock` (DEFAULT 0), and `category` (CHECK IN ('Electronics', 'Clothing', 'Food')).
<details>
<summary>Show Answer</summary>

```sql
CREATE TABLE Product (
    product_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) CHECK (price > 0),
    stock INT DEFAULT 0,
    category VARCHAR(20) CHECK (category IN ('Electronics', 'Clothing', 'Food'))
);
```
</details>

**2.** What happens when you try to delete a department that has employees assigned to it, assuming a foreign key with `ON DELETE RESTRICT`?
<details>
<summary>Show Answer</summary>
The DELETE operation is rejected with an error. The DBMS prevents the deletion because employee rows reference the department's primary key. You must first delete or reassign all employees in that department.
</details>

**3.** Compare `ON DELETE CASCADE` and `ON DELETE SET NULL` with examples.
<details>
<summary>Show Answer</summary>
CASCADE: Deleting a parent row automatically deletes all child rows referencing it. Example: Deleting a customer deletes all their orders. SET NULL: Deleting a parent row sets the foreign key in child rows to NULL. Example: Deleting a department sets employees' dept_id to NULL (employees remain in the database but become unassigned).
</details>

**4.** What is the difference between a CHECK constraint and an assertion?
<details>
<summary>Show Answer</summary>
A CHECK constraint applies to a single column or row within one table (e.g., `CHECK (age >= 18)`). An assertion is a database-wide constraint that can span multiple tables and include aggregate conditions (e.g., ensuring total salaries do not exceed department budget). Most DBMS implement CHECK constraints but not assertions; triggers are used instead.
</details>

**5.** Explain the entity integrity constraint. Can a composite primary key have a NULL value in any of its columns?
<details>
<summary>Show Answer</summary>
Entity integrity states that no component of the primary key can be NULL. For a composite primary key (e.g., `PRIMARY KEY (student_id, course_id, semester)`), none of the three columns can be NULL. If `semester` is NULL, the tuple cannot be uniquely identified, violating entity integrity.
</details>
