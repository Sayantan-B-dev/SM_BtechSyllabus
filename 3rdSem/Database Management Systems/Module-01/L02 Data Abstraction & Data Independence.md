# Data Abstraction & Data Independence

**Course:** Database Management Systems  
**Module:** 1 | **Lecture:** 2  
**Date:** 09-Jul-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## Notes

### The Need for Abstraction

A database system is complex. Users should not need to know how data is physically stored on disk (cylinder, track, block, sector). They should interact with the data at a higher level of abstraction. This is analogous to driving a car -- you operate the steering wheel and pedals, not the engine's internal combustion process directly.

**Data abstraction** means hiding the complexities of data storage and representation from the user, providing a simplified interface for interaction.

### Three-Schema Architecture

The ANSI-SPARC architecture defines three levels of abstraction. This separation is crucial for achieving **data independence**.

```
+-------------------------------------------------------+
|                    VIEW LEVEL                          |
|   (External Schemas / User Views)                     |
|   e.g., StudentView, CourseView                       |
+-------------------------------------------------------+
          |                  |                  |
          +---- mapping ----+---- mapping ----+
          |                                     |
+-------------------------------------------------------+
|                  CONCEPTUAL LEVEL                      |
|   (Conceptual Schema)                                 |
|   Describes what data is stored and relationships     |
|   e.g., "Students take Courses"                       |
+-------------------------------------------------------+
          |                                     |
          +---- mapping ----+---- mapping ----+
          |                                     |
+-------------------------------------------------------+
|                  PHYSICAL LEVEL                        |
|   (Internal Schema)                                   |
|   Describes how data is actually stored on disk       |
|   e.g., B+ tree index on student_id, heap file        |
+-------------------------------------------------------+
```

#### 1. Physical Level (Internal Schema)

The lowest level of abstraction. It describes **how** data is physically stored.

**What it describes:**
- Storage structures (heap files, sequential files, hash files).
- Index structures (B+ trees, hash indexes).
- Data compression and encryption.
- Record placement (which disk blocks, cylinders).
- Access paths.

*Example:*
```
Student records are stored in a heap file "students.dat"
on blocks 100-150 of disk.
Each record is 256 bytes.
A B+ tree index on student_id is stored in "idx_student_id".
Compression algorithm: LZ4.
```

This level is of interest to the **DBA and system programmers**, not to end users.

#### 2. Conceptual Level (Conceptual Schema)

The middle level. It describes **what** data is stored and the relationships among data, without any storage details.

**What it describes:**
- All entities, attributes, and relationships.
- Constraints (primary keys, foreign keys, checks).
- Access privileges and security rules.
- Integrity constraints.

*Example -- Conceptual schema for a university:*

```
Student (student_id: INTEGER, name: VARCHAR(50), dept: VARCHAR(20))
Course (course_id: VARCHAR(10), title: VARCHAR(100), credits: INTEGER)
Enrollment (student_id: INTEGER, course_id: VARCHAR(10), semester: VARCHAR(10))
Primary Key of Student: student_id
Foreign Key: Enrollment.student_id references Student.student_id
```

The conceptual schema is the **central reference point**. It must be independent of both the physical storage (below) and the user views (above).

#### 3. View Level (External Schema)

The highest level of abstraction. It describes only a **part** of the entire database that is relevant to a specific user group.

**What it describes:**
- Subsets of the conceptual schema.
- Virtual data (derived/computed).
- Customized formats and names.
- Restricted access (hiding sensitive data).

*Example -- Different views of the same university database:*

**Registrar's View:**
```
CREATE VIEW RegistrarReport AS
SELECT s.student_id, s.name, s.dept, COUNT(e.course_id) AS enrolled_count
FROM Student s LEFT JOIN Enrollment e ON s.student_id = e.student_id
GROUP BY s.student_id, s.name, s.dept;
```

**Student's View (self-service):**
```
CREATE VIEW MyGrades AS
SELECT c.title, e.semester, e.grade
FROM Enrollment e JOIN Course c ON e.course_id = c.course_id
WHERE e.student_id = CURRENT_USER;
```

**HR View (no access to grades):**
```
CREATE VIEW StudentDirectory AS
SELECT student_id, name, dept FROM Student;
```

Each view may present the same data differently, even using different names for the same attributes.

### Data Independence

**Data independence** is the ability to modify a schema at one level of the database system without changing the schema at the next higher level. There are two kinds:

#### Physical Data Independence

**Definition:** The ability to modify the physical schema (storage structures, indexes, file organization) without rewriting application programs that access the conceptual schema.

**What can change:**
- Changing from heap file to sequential file organization.
- Adding or dropping indexes.
- Switching compression algorithms.
- Moving data to a different disk.
- Changing RAID configuration.
- Partitioning tables across multiple disks.

**Example:**

Suppose the `Student` table was stored as a heap file (unordered). The DBA decides to change it to a sequential file ordered by `student_id` to speed up range queries.

- Before: Heap file -- insert is O(1), but range query on student_id scans entire file.
- After: Sequential file -- insert is O(n), but range query is O(log n).

**No change needed** at the conceptual level:
```sql
SELECT * FROM Student WHERE student_id BETWEEN 'CS101' AND 'CS200';
```
This query works identically before and after the change.

**No change needed** at the view level:
```sql
SELECT * FROM RegistrarReport;
```
The view continues to work unchanged.

#### Logical Data Independence

**Definition:** The ability to modify the conceptual schema (adding/removing attributes, splitting/merging tables) without changing external views or application programs.

**What can change:**
- Adding a new column to a table.
- Removing a column (affects views that use it -- those views must be updated).
- Splitting one table into two (normalization).
- Merging two tables into one.
- Adding a new relationship.

**Example -- Adding a column:**

The university decides to add `email` to the `Student` table at the conceptual level:

```sql
ALTER TABLE Student ADD COLUMN email VARCHAR(100);
```

The existing view `StudentDirectory` does not include `email`, so it works unchanged:
```sql
CREATE VIEW StudentDirectory AS
SELECT student_id, name, dept FROM Student;
```

However, any view that used `SELECT *` would now include `email`, which might break applications. Good practice dictates explicitly listing columns in views.

**Example -- Splitting a table (vertical fragmentation):**

The `Student` table is split for normalization:

**Before:**
```sql
Student (student_id, name, dept, address, phone, email, advisor_id)
```

**After (3NF normalization):**
```sql
Student (student_id, name, dept, advisor_id)
StudentContact (student_id, address, phone, email)
```

If a view `StudentDirectory` selects `student_id, name, dept`, it works unchanged. But if an application queries `SELECT address FROM Student`, it must be updated to reference `StudentContact`.

**Logical data independence is harder to achieve** than physical data independence because views may depend on specific columns and structures.

### Mapping Between Levels

**Mapping** is the process of transforming requests and data between levels.

**Conceptual-to-Internal Mapping (Physical Mapping):**
- Translates conceptual operations (e.g., "find student with ID 101") into physical operations (e.g., "read disk block 50 at offset 256").
- The DBMS uses catalog tables to know the mapping.
- Example: The query `SELECT * FROM Student WHERE student_id = 101` is mapped to a B+ tree index lookup on `student_id`.

**External-to-Conceptual Mapping (Logical Mapping):**
- Translates view-level operations into conceptual-level operations.
- Example: A query on `RegistrarReport` (a view) is internally rewritten as the underlying `SELECT` query on `Student` and `Enrollment` tables.

### Why Three Levels?

| Aspect | Benefit |
|---|---|
| **Modularity** | Each level can be modified independently. |
| **Security** | Users see only their authorized view. |
| **Simplicity** | Users interact with a simplified model. |
| **Data Independence** | Changes at one level don't propagate upward. |
| **Multiple Views** | Different users see the same data differently. |

### Real-World Analogy

Think of a library:
- **Physical level**: How books are shelved (by ISBN, by Dewey Decimal, on which floor, which row).
- **Conceptual level**: The library catalog -- each book has a title, author, ISBN, and location. You don't need to know the floor/row.
- **View level**: 
  - Students see only available books.
  - Librarians see borrower history and overdue status.
  - Management sees acquisition costs and borrowing trends.

When the library reorganizes shelves (physical change), the catalog (conceptual) remains the same. When a new field (e.g., "ebook link") is added to the catalog, user views can remain unchanged if they don't use that field.

---

## Practice Problems

**1.** Explain the difference between physical and logical data independence with one example each.
<details>
<summary>Show Answer</summary>
Physical independence: Changing storage structure (e.g., adding an index) without changing conceptual schema. Logical independence: Changing conceptual schema (e.g., adding a column) without changing external views.
</details>

**2.** A university's Student table is stored as a heap file. The DBA decides to reorganize it as a hash file on student_id. Which level(s) of the architecture are affected?
<details>
<summary>Show Answer</summary>
Only the physical level. The conceptual schema (Student table definition) and external views remain unchanged. This is an example of physical data independence.
</details>

**3.** If a column `date_of_birth` is added to the `Employee` table but a view `EmployeeList` (which selects only `emp_id` and `name`) exists, does the view need modification?
<details>
<summary>Show Answer</summary>
No, because the view explicitly lists only `emp_id` and `name`. However, if the view used `SELECT *`, it would now include `date_of_birth`, potentially breaking dependent applications.
</details>

**4.** Draw a diagram of the three-schema architecture and label each level.
<details>
<summary>Show Answer</summary>
Top: View Level (External Schema) -- multiple user views. Middle: Conceptual Level (Conceptual Schema) -- logical structure. Bottom: Physical Level (Internal Schema) -- storage details. Arrows represent mappings between levels.
</details>

**5.** Why is logical data independence harder to achieve than physical data independence?
<details>
<summary>Show Answer</summary>
Logical changes (adding/removing columns, splitting tables) can break views and application programs that reference the changed structures. Physical changes (indexing, file organization) are transparent to users.
</details>
