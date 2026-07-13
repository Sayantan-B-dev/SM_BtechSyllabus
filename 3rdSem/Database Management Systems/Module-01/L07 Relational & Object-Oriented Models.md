# Relational & Object-Oriented Models

**Course:** Database Management Systems  
**Module:** 1 | **Lecture:** 7  
**Date:** 23-Jul-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## Notes

### The Relational Model

The **relational model** was proposed by Dr. Edgar F. Codd in 1970 at IBM. It revolutionized database management by providing a simple, mathematical foundation for data organization.

#### Core Concepts

| Term | Formal Definition | Everyday Equivalent |
|---|---|---|
| **Relation** | A set of tuples sharing the same attributes | A table |
| **Tuple** | An ordered set of attribute values (ordered by attribute name) | A row |
| **Attribute** | A named column of a relation | A column |
| **Domain** | A set of atomic values from which an attribute takes values | Data type + constraints |
| **Degree** | Number of attributes in a relation | Number of columns |
| **Cardinality** | Number of tuples in a relation | Number of rows |
| **Relation Schema** | Name + list of attributes with domains | Table definition (CREATE TABLE) |
| **Relation Instance** | A set of tuples at a particular time | The actual data in a table |
| **Relation State** | The instance at a given moment | Snapshot of data |

**Formal definition:**

Let a set of domains `D1, D2, ..., Dn` be given. A relation `R` is a subset of the Cartesian product `D1 x D2 x ... x Dn`. That is:

```
R subset of (D1 x D2 x ... x Dn)
```

A tuple `t` is an ordered list of values `(v1, v2, ..., vn)` where each `vi` is in `Di`.

**Example -- Formal:**

```
Domain D1 = set of valid student IDs: {'CS2026001', 'CS2026002', 'EE2026003'}
Domain D2 = set of names: {'Alice', 'Bob', 'Charlie'}
Domain D3 = set of departments: {'CS', 'EE', 'ME'}

Relation Student = {
    ('CS2026001', 'Alice', 'CS'),
    ('CS2026002', 'Bob', 'CS'),
    ('EE2026003', 'Charlie', 'EE')
}
```

**Properties of a relation (from Codd's rules):**
1. Each tuple is distinct (no duplicate rows).
2. Order of tuples is irrelevant (a set, not a list).
3. Order of attributes is irrelevant (identified by name).
4. Each attribute value is **atomic** (single, indivisible value -- 1NF).
5. Each attribute has a unique name within the relation.

#### Domains in Detail

A **domain** is a named set of atomic values with an associated data type and constraints.

**Examples:**
- `StudentIDs` = CHAR(9) -- values like 'CS2026001'.
- `Names` = VARCHAR(50) -- values like 'Alice Johnson'.
- `Grades` = CHAR(2) -- values in {'A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'F'}.
- `Ages` = INTEGER -- values from 16 to 100 (with a CHECK constraint).
- `Booleans` = {'TRUE', 'FALSE'}.

Domain constraints ensure that only valid values are stored. For example, if `Age` has domain `INTEGER` with a constraint `CHECK (Age BETWEEN 16 AND 100)`, then inserting `Age = 150` is rejected.

---

### Keys

Keys are essential for uniquely identifying tuples and establishing relationships.

#### Superkey

A **superkey** is a set of one or more attributes that, taken collectively, uniquely identifies a tuple in a relation.

**Properties:**
- A superkey can have extra attributes that are not necessary for uniqueness.
- Every relation has at least one superkey (the set of all its attributes).

**Example:**
In `Student(student_id, name, dept_id, tot_cred)`:
- `{student_id}` -- superkey (guarantees uniqueness)
- `{student_id, name}` -- superkey (contains student_id)
- `{student_id, name, dept_id}` -- superkey
- `{name}` -- NOT a superkey (names can repeat)

#### Candidate Key

A **candidate key** is a minimal superkey -- a superkey such that no proper subset is also a superkey.

**Properties:**
- It is "minimal" -- removing any attribute breaks uniqueness.
- A relation can have multiple candidate keys.
- One candidate key is chosen to be the **primary key**.

**Example:**
In `Employee(emp_id, pan_card, aadhar_id, name, dept)`:
- `{emp_id}` -- candidate key (minimal)
- `{pan_card}` -- candidate key (minimal)
- `{aadhar_id}` -- candidate key (minimal)
- `{emp_id, name}` -- superkey but NOT candidate key (not minimal, emp_id alone suffices)

#### Primary Key

The **primary key** is a candidate key selected by the database designer as the principal identifier for tuples.

**Properties:**
- Must be **NOT NULL** (no part of the primary key can have NULL values).
- Must be **UNIQUE** (no duplicate values).
- Usually indexed for fast lookup.
- Denoted by **underline** in ER diagrams and by `PRIMARY KEY` in SQL.

```sql
CREATE TABLE Student (
    student_id CHAR(9) PRIMARY KEY,
    ...
);
```

#### Foreign Key

A **foreign key** is a set of attributes in one relation that references the primary key of another relation.

**Purpose:** Establishes a link between data in two tables, representing a relationship.

**Example:**
```sql
CREATE TABLE Enrollment (
    student_id CHAR(9),
    course_id  CHAR(8),
    semester   VARCHAR(6),
    grade      CHAR(2),
    PRIMARY KEY (student_id, course_id, semester),
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);
```

Here:
- `Enrollment.student_id` is a foreign key referencing `Student.student_id`.
- `Enrollment.course_id` is a foreign key referencing `Course.course_id`.

The foreign key constraint ensures **referential integrity** -- you cannot enroll a student who does not exist, and you cannot offer a course that is not in the Course table.

---

### Relational Integrity Constraints

Integrity constraints ensure that the data in the database is accurate and consistent.

#### 1. Entity Integrity

**Rule:** No attribute that is part of the primary key can accept NULL values.

**Rationale:** If part of the primary key is NULL, we cannot uniquely identify the tuple.

```sql
-- This is valid: primary key is NOT NULL by definition
CREATE TABLE Student (
    student_id CHAR(9) PRIMARY KEY,  -- Implicitly NOT NULL
    name VARCHAR(50) NOT NULL,
    dept_id CHAR(4)
);

-- This would violate entity integrity:
INSERT INTO Student VALUES (NULL, 'Alice', 'CS');
-- ERROR: NULL value violates PRIMARY KEY constraint
```

#### 2. Referential Integrity

**Rule:** A foreign key value must either:
- Match a primary key value in the referenced table, or
- Be completely NULL (if all FK attributes are nullable).

**Example:**
```sql
-- Valid: This student exists in the Student table
INSERT INTO Enrollment VALUES ('CS2026001', 'CS301', 'Fall', 'A');

-- Invalid: No student with ID 'XXXX'
INSERT INTO Enrollment VALUES ('XXXX', 'CS301', 'Fall', 'A');
-- ERROR: Foreign key violation

-- Valid: NULL foreign key (if allowed)
INSERT INTO Enrollment (course_id, semester) VALUES ('CS301', 'Fall');
-- student_id is NULL, which is allowed if the column is nullable
```

#### 3. Domain Integrity

**Rule:** Every attribute value must be from its defined domain.

**Enforced through:**
- Data types (INT, VARCHAR, DATE, etc.)
- NOT NULL constraints
- CHECK constraints
- DEFAULT values

```sql
CREATE TABLE Student (
    student_id CHAR(9),
    age        INT CHECK (age >= 16 AND age <= 100),
    gender     CHAR(1) CHECK (gender IN ('M', 'F', 'O')),
    email      VARCHAR(100) DEFAULT 'noemail@university.edu',
    dept_id    CHAR(4) NOT NULL
);

-- Violates domain integrity:
INSERT INTO Student VALUES ('CS2026001', 150, 'X', 'alice@u.edu', 'CS');
-- ERROR: age violates CHECK constraint, gender not in allowed set
```

---

### Comparison -- All Four Constraints

| Constraint | Level | What it prevents | Enforced by |
|---|---|---|---|
| **Domain** | Attribute | Invalid values, wrong data types, out-of-range values | Data types, CHECK, NOT NULL, DEFAULT |
| **Key** | Relation | Duplicate tuples | UNIQUE, PRIMARY KEY |
| **Entity Integrity** | Relation | NULL in primary key | PRIMARY KEY (implicit NOT NULL) |
| **Referential Integrity** | Cross-relation | Orphaned foreign keys, dangling references | FOREIGN KEY + REFERENCES |

---

### Object-Oriented Model

#### Motivation

The relational model struggles with:
- **Complex data** -- CAD drawings, GIS maps, medical images, multimedia.
- **Behavior** -- Data is passive; operations are separate (stored procedures).
- **Inheritance** -- Not natively supported (requires workarounds like table-per-class).
- **User-defined types** -- Only primitive types (INT, VARCHAR, DATE).

The **Object-Oriented Database (OODB)** model addresses these by bringing OOP concepts to databases.

#### Core Concepts

**Object:** An entity that encapsulates both **state** (attributes) and **behavior** (methods).
- Every object has a unique **Object Identifier (OID)** -- system-assigned, immutable, globally unique.
- Objects are accessed by OID rather than by key value.

**Class:** A template that defines the attributes and methods for a set of objects.
- Objects are **instances** of a class.
- Correspondence: Class -> Entity Set (ER) / Relation Schema (Relational).

**Inheritance:** A class can inherit attributes and methods from a parent class.
- `GraduateStudent IS-A Student` -- inherits all Student attributes plus has its own (thesis_topic, advisor).

**Encapsulation:** Internal state is hidden; access is only through public methods.

**Polymorphism:** The same method name can behave differently on different classes.

**Example -- OODB Schema (conceptual):**

```
Class Person {
    attribute string name;
    attribute date dob;
    attribute address addr;
    method int age() { return current_year - dob.year; }
}

Class Student extends Person {
    attribute string student_id;
    attribute string dept;
    attribute set<Course> enrolled_courses;
    method void enroll(Course c) { enrolled_courses.add(c); }
    method float calc_gpa() { ... }
}

Class Professor extends Person {
    attribute string emp_id;
    attribute float salary;
    attribute set<Course> teaches;
    method void assign_grade(Student s, Course c, string grade) { ... }
}

Class Course {
    attribute string course_id;
    attribute string title;
    attribute int credits;
    attribute Professor instructor;
    method void set_instructor(Professor p) { instructor = p; }
}
```

#### Object Definition Language (ODL)

ODL was designed by ODMG (Object Data Management Group) to define object-oriented schemas. It is analogous to DDL for relational databases.

```odl
interface Person {
    attribute string name;
    attribute date date_of_birth;
    short age() raises(error);
};

interface Student : Person {
    attribute string student_id;
    attribute string dept_id;
    attribute float tot_cred;
    relationship Set<Course> takes
        inverse Course::taken_by;
};

interface Course {
    attribute string course_id;
    attribute string title;
    attribute short credits;
    relationship Set<Student> taken_by
        inverse Student::takes;
    relationship Professor taught_by
        inverse Professor::teaches;
};

interface Professor : Person {
    attribute string emp_id;
    attribute float salary;
    relationship Set<Course> teaches
        inverse Course::taught_by;
};
```

#### Object Query Language (OQL)

OQL is a declarative query language for OODBs, similar to SQL but operating on objects.

```oql
-- Find all CS students
SELECT s
FROM Students s
WHERE s.dept_id = 'CS';

-- Find students with GPA above 3.5
SELECT s.name, s.calc_gpa()
FROM Students s
WHERE s.calc_gpa() > 3.5;

-- Navigate relationships
SELECT s.name, c.title
FROM Students s, s.takes c
WHERE c.credits > 3;
```

#### Storage in OODB

- Objects are stored persistently (outlives the program that created them).
- An **object store** manages persistent objects.
- The OID is used for direct access.
- Object clustering (storing related objects together) improves performance.

### Comparison: Relational vs Object-Oriented

| Aspect | Relational Model | Object-Oriented Model |
|---|---|---|
| **Basic unit** | Relation (table) | Class |
| **Data representation** | Flat tuples (rows) | Objects (nested, complex) |
| **Identity** | Primary key (user-defined) | OID (system-generated) |
| **Behavior** | None (passive data) | Methods (active data) |
| **Inheritance** | Not natively supported | Full support (IS-A hierarchy) |
| **Encapsulation** | No (all data visible) | Yes (private/protected/public) |
| **Relationships** | Foreign keys + joins | Object references (OIDs) |
| **Query language** | SQL (declarative) | OQL (declarative on objects) |
| **Complex data** | Tables with joins | Nested objects, collections, arrays |
| **Performance** | Excellent for tabular data | Good for complex objects |
| **Maturity** | Highly mature (40+ years) | Less mature; niche adoption |
| **Standard** | SQL (ISO/ANSI) | ODMG 3.0 (defunct since 2001) |
| **Tool support** | Extensive | Limited |
| **Use cases** | Business, banking, web apps | CAD, GIS, scientific, telecom |

### Object-Relational Model (ORDBMS)

A hybrid approach: relational tables with OO extensions.

**Features:**
- User-defined types (UDTs)
- Complex data types (arrays, sets, nested tables)
- Methods on types
- Inheritance on tables
- Reference types (OIDs)

**Example -- PostgreSQL (Object-Relational):**

```sql
-- User-defined type
CREATE TYPE Address AS (
    street VARCHAR(100),
    city VARCHAR(50),
    state CHAR(2),
    zip VARCHAR(10)
);

-- Inheritance
CREATE TABLE Person (
    name VARCHAR(100),
    dob DATE
);

CREATE TABLE Student (
    student_id CHAR(9),
    dept CHAR(4)
) INHERITS (Person);  -- Student inherits all columns from Person

-- Array type
CREATE TABLE Course (
    course_id CHAR(8) PRIMARY KEY,
    title VARCHAR(100),
    instructors TEXT[]  -- Array of instructor names
);

-- Query with array
SELECT title FROM Course WHERE 'Dr. Smith' = ANY(instructors);
```

Most modern relational databases (PostgreSQL, Oracle, DB2) have added OO features, blurring the line between the two models.

---

## Practice Problems

**1.** Define superkey, candidate key, and primary key. Give an example where a superkey is not a candidate key.
<details>
<summary>Answer</summary>
Superkey: set of attributes that uniquely identifies a tuple. Candidate key: minimal superkey. Primary key: chosen candidate key. Example: In Employee(emp_id, pan, name), {emp_id, pan, name} is a superkey but not a candidate key because {emp_id} alone is sufficient.
</details>

**2.** Explain the difference between entity integrity and referential integrity.
<details>
<summary>Answer</summary>
Entity integrity: no primary key attribute can be NULL. Referential integrity: a foreign key value must either match a primary key value in the referenced table or be entirely NULL.
</details>

**3.** How does the object-oriented model overcome limitations of the relational model?
<details>
<summary>Answer</summary>
It supports complex data types (nested objects, collections), encapsulates behavior with methods, provides inheritance for IS-A hierarchies, and uses OIDs for identity instead of user-defined keys.
</details>

**4.** In the object-oriented model, what is an OID and why is it advantageous?
<details>
<summary>Answer</summary>
OID (Object Identifier) is a system-generated, immutable, globally unique identifier for each object. Advantage: identity is independent of attribute values -- if a student changes their name, the OID remains the same. Also, OIDs provide direct access without key lookups.
</details>

**5.** Write SQL to create a `Customer` table with `cust_id` (PK), `name` (NOT NULL), `phone` (UNIQUE), and `age` (CHECK >= 18) including referential integrity with an `Order` table.
<details>
<summary>Answer</summary>

```sql
CREATE TABLE Customer (
    cust_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) UNIQUE,
    age INT CHECK (age >= 18)
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    cust_id INT NOT NULL,
    order_date DATE,
    amount DECIMAL(10,2),
    FOREIGN KEY (cust_id) REFERENCES Customer(cust_id)
);
```
</details>
